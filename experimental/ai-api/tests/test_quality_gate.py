"""Linguistic QA tests: contradictions must not masquerade as validated lessons."""
import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from quality_gate import inspect_linguistic_quality


def sample():
    return {
        "sentences": [{
            "id": "s1", "text": "Я читаю книгу.",
            "stressedText": "Я чита́ю книгу.", "ttsText": "Ya chitayu knigu.",
            "words": [
                {"id": "w1", "surface": "Я", "lemma": "я",
                 "partOfSpeech": {"en": "personal pronoun"}},
                {"id": "w2", "surface": "читаю", "lemma": "читать", "stressed": "чита́ю",
                 "partOfSpeech": {"en": "verb"}, "tense": "present",
                 "person": "3rd person singular"},
                {"id": "w3", "surface": "книгу", "lemma": "книга", "gender": "neuter",
                 "stressed": "кни́гу", "partOfSpeech": {"en": "noun"}}
            ],
            "structure": {"tree": {"children": []}},
        }]
    }


class QualityGateTests(unittest.TestCase):
    def test_user_reported_contradictions_are_detected(self):
        result = inspect_linguistic_quality(sample())
        self.assertEqual(result["status"], "review_required")
        self.assertFalse(result["linguisticallyVerified"])
        issues = result["issues"]
        codes = {issue["code"] for issue in issues}
        self.assertIn("known_noun_gender", codes)
        self.assertIn("verb_1sg_person_conflict", codes)
        self.assertIn("stress_not_propagated", codes)
        self.assertIn("tts_not_cyrillic", codes)
        self.assertIn("shallow_syntax_tree", codes)
        self.assertEqual({i["severity"] for i in issues
                          if i["code"] in ("known_noun_gender", "verb_1sg_person_conflict")},
                         {"error"})

    def test_correct_analysis_still_requires_review(self):
        data = sample()
        sent = data["sentences"][0]
        sent["stressedText"] = "Я чита́ю кни́гу."
        sent["ttsText"] = "Я читаю книгу."
        sent["words"][1]["person"] = "1st person singular"
        sent["words"][2]["gender"] = "feminine"
        sent["structure"]["tree"]["children"] = [
            {"type": "subject"}, {"type": "predicate"}, {"type": "object"}
        ]
        self.assertEqual(inspect_linguistic_quality(data),
                         {"status": "review_required", "linguisticallyVerified": False, "issues": []})

    def test_gender_cannot_be_deduced_from_ending_alone(self):
        data = sample()
        w = data["sentences"][0]["words"][2]
        w.update({"surface": "папу", "lemma": "папа", "gender": "masculine"})
        codes = [i["code"] for i in inspect_linguistic_quality(data)["issues"]]
        self.assertNotIn("known_noun_gender", codes)

    def test_do_not_guess_third_person_error_on_valid_verb(self):
        data = sample()
        w = data["sentences"][0]["words"][1]
        w.update({"surface": "читает", "person": "3rd person singular", "tense": "present"})
        codes = [i["code"] for i in inspect_linguistic_quality(data)["issues"]]
        self.assertNotIn("verb_1sg_person_conflict", codes)

    def test_missing_gender_or_person_is_not_falsely_verified(self):
        data = sample()
        data["sentences"][0]["words"][1].pop("person")
        data["sentences"][0]["words"][2].pop("gender")
        codes = [i["code"] for i in inspect_linguistic_quality(data)["issues"]]
        self.assertNotIn("known_noun_gender", codes)
        self.assertNotIn("verb_1sg_person_conflict", codes)


if __name__ == "__main__":
    unittest.main()
