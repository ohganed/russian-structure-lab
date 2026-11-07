"""Conservative Russian linguistic QA for the local Ollama experiment.

This is NOT a full morphological parser. It detects a small set of
high-confidence contradictions and surfaces other quality warnings, while
retaining a separate mandatory expert-review requirement.
"""
import re

# Exact, uncontroversial dictionary facts only. Do not generalize from
# -a/-я endings: e.g. папа and дядя are masculine, сирота is common gender.
KNOWN_NOUN_GENDER = {"книга": "feminine", "газета": "feminine"}
GENDER_ALIASES = {
    "feminine": "feminine", "female": "feminine", "женский": "feminine", "女性": "feminine",
    "masculine": "masculine", "male": "masculine", "мужской": "masculine", "男性": "masculine",
    "neuter": "neuter", "средний": "neuter", "中性": "neuter",
}
THIRD_SINGULAR = {"3", "3rd", "third", "3rd person", "3rd person singular",
                  "third person singular", "3-person singular", "третье лицо",
                  "3-е лицо", "三人称单数", "3人称単数"}
CYRILLIC = re.compile(r"[А-Яа-яЁё]")


def _issue(severity, code, sentence_id, word_id, explanation):
    return {
        "severity": severity,
        "code": code,
        "sentenceId": sentence_id,
        "wordId": word_id,
        "messageJa": explanation,
    }


def inspect_linguistic_quality(material):
    """Return only demonstrable contradictions or reviewable warnings.

    Unknown words/tags are *not* treated as verified. Passing this audit
    never indicates the morphology itself is correct.
    """
    issues = []
    for sentence in material.get("sentences", []):
        if not isinstance(sentence, dict):
            continue
        sid = sentence.get("id")
        text = sentence.get("text", "")
        stress_text = sentence.get("stressedText") or ""
        tts_text = sentence.get("ttsText") or ""
        if CYRILLIC.search(text) and tts_text and not CYRILLIC.search(tts_text):
            issues.append(_issue("warning", "tts_not_cyrillic", sid, None,
                                 "ロシア語TTS用の文がローマ字だけです。原文のキリル文字を使ってください。"))

        for word in sentence.get("words", []):
            if not isinstance(word, dict):
                continue
            wid = word.get("id")
            surface = word.get("surface") or ""
            lemma = (word.get("lemma") or "").lower()
            gender = GENDER_ALIASES.get(str(word.get("gender") or "").lower())
            if lemma in KNOWN_NOUN_GENDER and gender and gender != KNOWN_NOUN_GENDER[lemma]:
                issues.append(_issue(
                    "error", "known_noun_gender", sid, wid,
                    f"「{surface}」の辞書形「{lemma}」は女性名詞です。"
                    f"出力の性「{word.get('gender')}」と矛盾しています。"
                ))

            pos = word.get("partOfSpeech") or {}
            english_pos = (pos.get("en", "") if isinstance(pos, dict) else str(pos)).lower()
            russian_pos = (pos.get("ru", "") if isinstance(pos, dict) else "").lower()
            tense = str(word.get("tense") or "").strip().lower()
            person = str(word.get("person") or "").strip().lower()
            is_verb = "verb" in english_pos or "глагол" in russian_pos
            if (is_verb and tense in ("present", "future")
                    and len(surface) > 2 and surface.lower().endswith(("ю", "у"))
                    and (person in THIRD_SINGULAR or person.startswith(("3rd ", "third ")))):
                issues.append(_issue(
                    "error", "verb_1sg_person_conflict", sid, wid,
                    f"「{surface}」は1人称単数の動詞語形ですが、"
                    f"解析は「{word.get('person')}」としています。"
                ))

            stressed = word.get("stressed") or ""
            if ("\u0301" in stressed and stress_text
                    and stressed not in stress_text):
                issues.append(_issue(
                    "warning", "stress_not_propagated", sid, wid,
                    f"単語「{stressed}」のアクセントが文全体のstressedTextに反映されていません。"
                ))

        tree = (sentence.get("structure") or {}).get("tree")
        if (isinstance(tree, dict) and not tree.get("children")
                and len(sentence.get("words", [])) >= 3):
            issues.append(_issue("warning", "shallow_syntax_tree", sid, None,
                                 "文に複数の語がありますが、構文ツリーに主語・述語・目的語などの子要素がありません。"))
    return {"status": "review_required", "linguisticallyVerified": False, "issues": issues}
