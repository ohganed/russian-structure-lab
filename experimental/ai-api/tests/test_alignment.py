"""Regression tests: bad AI offsets get recalculated, not blindly trusted."""
import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from alignment import align_generated_offsets
from contract import ContractError, validate_material


SOURCE = "Я читаю книгу."


def lesson(text=SOURCE):
    return {
        "schemaVersion": "1.0",
        "language": "ru",
        "originalText": text,
        "sentences": [{
            "id": "s1",
            "text": text,
            "stressedText": text,
            "words": [
                {"id": "w1", "surface": "Я", "start": 77, "end": 88},
                {"id": "w2", "surface": "читаю", "start": 17, "end": 22},
                {"id": "w3", "surface": "книгу", "start": -1, "end": 4},
            ],
            "chunks": [
                {"id": "c1", "text": "Я читаю", "wordIds": ["w1", "w2"], "start": 1, "end": 100},
                {"id": "c2", "text": "книгу", "wordIds": ["w3"], "start": 42, "end": 55},
            ],
            "structure": {"tree": {
                "id": "n1", "refIds": ["w1", "w2", "w3"], "children": []
            }}
        }]
    }


class AlignmentTests(unittest.TestCase):
    def test_repairs_reported_chitayu_offset_error(self):
        generated = lesson()
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["words"][1]["start"], 2)
        self.assertEqual(fixed["sentences"][0]["words"][1]["end"], 7)
        self.assertEqual(fixed["sentences"][0]["words"][2]["start"], 8)
        self.assertEqual(fixed["sentences"][0]["words"][2]["end"], 13)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["start"], 0)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["end"], 7)
        self.assertTrue(validate_material(fixed, SOURCE))
        # The original AI response is not modified.
        self.assertEqual(generated["sentences"][0]["words"][1]["start"], 17)

    def test_repairs_unknown_structure_refs_from_exact_text(self):
        generated = lesson()
        root = generated["sentences"][0]["structure"]["tree"]
        root["text"] = SOURCE
        root["refIds"] = ["word_1", "word_2", "word_3"]
        root["children"] = [
            {"id": "n2", "text": "читаю", "refIds": ["bad-ref"], "children": []},
            {"id": "n3", "text": "книгу", "refIds": ["different-ref"], "children": []},
        ]
        fixed = align_generated_offsets(generated, SOURCE)
        tree = fixed["sentences"][0]["structure"]["tree"]
        self.assertEqual(tree["refIds"], ["w1", "w2", "w3"])
        self.assertEqual(tree["children"][0]["refIds"], ["w2"])
        self.assertEqual(tree["children"][1]["refIds"], ["w3"])
        self.assertTrue(validate_material(fixed, SOURCE))
        self.assertEqual(generated["sentences"][0]["structure"]["tree"]["refIds"],
                         ["word_1", "word_2", "word_3"])

    def test_existing_good_refs_unchanged(self):
        generated = lesson()
        root = generated["sentences"][0]["structure"]["tree"]
        root["text"] = "not source text"
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["structure"]["tree"]["refIds"],
                         ["w1", "w2", "w3"])

    def test_structure_missing_literal_text_rejected(self):
        generated = lesson()
        generated["sentences"][0]["structure"]["tree"]["refIds"] = ["unknown"]
        with self.assertRaisesRegex(ContractError, "literal"):
            align_generated_offsets(generated, SOURCE)

    def test_structure_nonmatching_node_text_rejected(self):
        generated = lesson()
        root = generated["sentences"][0]["structure"]["tree"]
        root["refIds"] = ["unknown"]
        root["text"] = "читала"
        with self.assertRaisesRegex(ContractError, "ambiguous"):
            align_generated_offsets(generated, SOURCE)

    def test_structure_repeated_word_ambiguous_rejected(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "w1", "surface": "Я"},
            {"id": "w2", "surface": "и"},
            {"id": "w3", "surface": "Я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": text, "wordIds": ["w1", "w2", "w3"]}]
        sent["structure"]["tree"] = {"id": "n1", "text": "Я",
                                         "refIds": ["nonexistent"], "children": []}
        with self.assertRaisesRegex(ContractError, "ambiguous"):
            align_generated_offsets(generated, text)

    def test_structure_repeated_word_existing_anchor(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "w1", "surface": "Я"},
            {"id": "w2", "surface": "и"},
            {"id": "w3", "surface": "Я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": text, "wordIds": ["w1", "w2", "w3"]}]
        sent["structure"]["tree"] = {"id": "n1", "text": "Я",
                                         "refIds": ["w3", "nonexistent"], "children": []}
        fixed = align_generated_offsets(generated, text)
        self.assertEqual(fixed["sentences"][0]["structure"]["tree"]["refIds"], ["w3"])
        validate_material(fixed, text)

    def test_repairs_unknown_chunk_word_ids_from_exact_source(self):
        generated = lesson()
        sent = generated["sentences"][0]
        sent["chunks"][0]["wordIds"] = ["word_1", "word_2"]
        sent["chunks"][1]["wordIds"] = ["word_3"]
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["w1", "w2"])
        self.assertEqual(fixed["sentences"][0]["chunks"][1]["wordIds"], ["w3"])
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["start"], 0)
        self.assertTrue(validate_material(fixed, SOURCE))
        self.assertEqual(generated["sentences"][0]["chunks"][0]["wordIds"],
                         ["word_1", "word_2"])

    def test_mixed_valid_and_unknown_chunk_refs_keep_real_anchor(self):
        generated = lesson()
        generated["sentences"][0]["chunks"][0]["wordIds"] = ["w2", "invented"]
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["w1", "w2"])
        self.assertTrue(validate_material(fixed, SOURCE))

    def test_unknown_chunk_refs_not_repaired_for_changed_text(self):
        generated = lesson()
        ch = generated["sentences"][0]["chunks"][0]
        ch["text"] = "Я чита"
        ch["wordIds"] = ["unknown"]
        with self.assertRaisesRegex(ContractError, "unambiguously"):
            align_generated_offsets(generated, SOURCE)

    def test_repeated_chunk_with_unknown_refs_is_ambiguous(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "w1", "surface": "Я"},
            {"id": "w2", "surface": "и"},
            {"id": "w3", "surface": "Я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": "Я", "wordIds": ["invented"]}]
        sent["structure"]["tree"]["refIds"] = ["w1", "w2", "w3"]
        with self.assertRaisesRegex(ContractError, "unambiguously"):
            align_generated_offsets(generated, text)

    def test_repeated_chunk_uses_existing_ref_as_disambiguator(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "w1", "surface": "Я"},
            {"id": "w2", "surface": "и"},
            {"id": "w3", "surface": "Я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": "Я",
                           "wordIds": ["w3", "invented"]}]
        sent["structure"]["tree"]["refIds"] = ["w1", "w2", "w3"]
        fixed = align_generated_offsets(generated, text)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["w3"])
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["start"], 4)
        validate_material(fixed, text)

    def test_known_chunk_refs_remain_unchanged(self):
        generated = lesson()
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["w1", "w2"])

    def test_numeric_chunk_word_ids_repaired_with_real_source_words(self):
        generated = lesson()
        generated["sentences"][0]["chunks"][0]["wordIds"] = [1, 2]
        generated["sentences"][0]["chunks"][1]["wordIds"] = [3]
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["w1", "w2"])
        self.assertEqual(fixed["sentences"][0]["chunks"][1]["wordIds"], ["w3"])
        validate_material(fixed, SOURCE)

    def test_null_chunk_word_id_repaired_when_text_is_unique(self):
        generated = lesson()
        generated["sentences"][0]["chunks"][1]["wordIds"] = [None]
        fixed = align_generated_offsets(generated, SOURCE)
        self.assertEqual(fixed["sentences"][0]["chunks"][1]["wordIds"], ["w3"])
        validate_material(fixed, SOURCE)

    def test_numeric_chunk_word_id_can_disambiguate_repeated_text(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "1", "surface": "Я"},
            {"id": "2", "surface": "и"},
            {"id": "3", "surface": "Я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": "Я", "wordIds": [3]}]
        sent["structure"]["tree"]["refIds"] = ["1", "2", "3"]
        fixed = align_generated_offsets(generated, text)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["wordIds"], ["3"])
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["start"], 4)
        validate_material(fixed, text)

    def test_noninteger_chunk_refs_are_rejected(self):
        for invalid in (True, 1.5, {"id": "w2"}, ["w2"]):
            with self.subTest(invalid=invalid):
                generated = lesson()
                generated["sentences"][0]["chunks"][0]["wordIds"] = [invalid]
                with self.assertRaisesRegex(ContractError, "unsupported"):
                    align_generated_offsets(generated, SOURCE)

    def test_scalar_chunk_word_ids_are_rejected(self):
        for invalid in (2, "w2", None):
            with self.subTest(invalid=invalid):
                generated = lesson()
                generated["sentences"][0]["chunks"][0]["wordIds"] = invalid
                with self.assertRaisesRegex(ContractError, "array"):
                    align_generated_offsets(generated, SOURCE)

    def test_repeated_word_uses_id_anchor(self):
        text = "Я и я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [
            {"id": "w1", "surface": "Я"},
            {"id": "w2", "surface": "и"},
            {"id": "w3", "surface": "я"},
        ]
        sent["chunks"] = [{"id": "c1", "text": "я", "wordIds": ["w3"]}]
        fixed = align_generated_offsets(generated, text)
        self.assertEqual(fixed["sentences"][0]["chunks"][0]["start"], 4)
        self.assertEqual(fixed["sentences"][0]["words"][2]["start"], 4)
        validate_material(fixed, text)

    def test_utf16_surrogate_prefix(self):
        text = "🙂 Я читаю книгу."
        generated = lesson(text)
        fixed = align_generated_offsets(generated, text)
        spans = [(w["start"], w["end"]) for w in fixed["sentences"][0]["words"]]
        self.assertEqual(spans, [(3, 4), (5, 10), (11, 16)])
        validate_material(fixed, text)

    def test_preserves_yo_and_stress(self):
        text = "Ёж."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["stressedText"] = "Ёж."
        sent["words"] = [{"id": "w1", "surface": "Ёж", "stressed": "Ёж"}]
        sent["chunks"] = [{"id": "c1", "text": "Ёж", "wordIds": ["w1"]}]
        sent["structure"]["tree"]["refIds"] = ["w1"]
        fixed = align_generated_offsets(generated, text)
        self.assertEqual(fixed["sentences"][0]["words"][0]["surface"], "Ёж")
        validate_material(fixed, text)

    def test_spelling_changed_never_repaired(self):
        generated = lesson()
        generated["sentences"][0]["words"][1]["surface"] = "четаю"
        with self.assertRaises(ContractError):
            align_generated_offsets(generated, SOURCE)

    def test_missing_word_still_rejected(self):
        generated = lesson()
        generated["sentences"][0]["words"].pop()
        # Auto-alignment must NOT silently invent the missing word.
        with self.assertRaises(ContractError):
            validate_material(align_generated_offsets(generated, SOURCE), SOURCE)

    def test_wrong_source_never_repaired(self):
        generated = lesson()
        generated["originalText"] = "Я читаю."
        with self.assertRaisesRegex(ContractError, "originalText"):
            align_generated_offsets(generated, SOURCE)

    def test_wrong_chunk_text_still_rejected(self):
        generated = lesson()
        generated["sentences"][0]["chunks"][0]["text"] = "Я чита"
        with self.assertRaises(ContractError):
            align_generated_offsets(generated, SOURCE)

    def test_ambiguous_repeated_chunk_without_ids_rejected(self):
        text = "Я и Я."
        generated = lesson(text)
        sent = generated["sentences"][0]
        sent["words"] = [{"id": "w1", "surface": "Я"},
                         {"id": "w2", "surface": "и"},
                         {"id": "w3", "surface": "Я"}]
        sent["chunks"] = [{"id": "c1", "text": "Я"}]
        with self.assertRaisesRegex(ContractError, "unambiguously"):
            align_generated_offsets(generated, text)

    def test_duplicate_ids_not_hidden_by_alignment(self):
        generated = lesson()
        generated["sentences"][0]["words"][1]["id"] = "w1"
        with self.assertRaises(ContractError):
            validate_material(align_generated_offsets(generated, SOURCE), SOURCE)


if __name__ == "__main__":
    unittest.main()
