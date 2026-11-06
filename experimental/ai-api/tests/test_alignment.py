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
        with self.assertRaisesRegex(ContractError, "omit"):
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
        with self.assertRaisesRegex(ContractError, "duplicate"):
            validate_material(align_generated_offsets(generated, SOURCE), SOURCE)


if __name__ == "__main__":
    unittest.main()
