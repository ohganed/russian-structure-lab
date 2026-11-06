"""Deterministic source alignment for Ollama-generated Russian lesson JSON.

The language model proposes lexical surfaces and chunk text, but must not
calculate character offsets. We calculate JS UTF-16 offsets from exact source
substrings; any text change, missing word or ambiguous chunk is rejected by
the final contract validator. No grammatical claims are corrected here.
"""
from copy import deepcopy
import unicodedata

from contract import ContractError


def _utf16_index(text, index):
    return len(text[:index].encode("utf-16-le")) // 2


def _is_word_char(char):
    return char.isalnum() or char == "_" or unicodedata.category(char).startswith("M")


def _whole_token(text, start, end):
    return ((start == 0 or not _is_word_char(text[start - 1]))
            and (end == len(text) or not _is_word_char(text[end])))


def _find_word(text, surface, start):
    at = text.find(surface, start)
    while at >= 0:
        after = at + len(surface)
        if _whole_token(text, at, after):
            return at, after
        at = text.find(surface, at + 1)
    raise ContractError("Cannot locate exact word in original sentence: " + repr(surface))


def _find_chunk(text, value, word_spans, word_ids):
    # Word IDs provide an unambiguous anchor even for repeated expressions.
    if word_ids:
        if not isinstance(word_ids, list) or any(
            not isinstance(wid, str) or wid not in word_spans for wid in word_ids
        ):
            raise ContractError("Chunk refers to unknown word IDs")
        first = min(word_spans[wid][0] for wid in word_ids)
        last = max(word_spans[wid][1] for wid in word_ids)
        if text[first:last] == value:
            return first, last

    candidates = []
    at = text.find(value)
    while at >= 0:
        end = at + len(value)
        if _whole_token(text, at, end):
            if not word_ids or all(
                at <= word_spans[wid][0] and word_spans[wid][1] <= end
                for wid in word_ids
            ):
                candidates.append((at, end))
        at = text.find(value, at + 1)
    if len(candidates) != 1:
        raise ContractError("Chunk text cannot be aligned unambiguously: " + repr(value))
    return candidates[0]


def align_generated_offsets(material, original):
    """Return a copy with deterministic offsets; never change original text.

    The final validate_material() step remains mandatory to detect missed
    lexical words, altered accents, invalid references, and omitted sentences.
    """
    if not isinstance(material, dict) or material.get("originalText") != original:
        raise ContractError("originalText differs from the submitted text")

    repaired = deepcopy(material)
    for sentence in repaired.get("sentences", []):
        if not isinstance(sentence, dict) or not isinstance(sentence.get("text"), str):
            raise ContractError("Missing sentence text")
        text = sentence["text"]
        cursor = 0
        spans = {}
        words = sentence.get("words") or []
        for word in words:
            if not isinstance(word, dict) or not isinstance(word.get("surface"), str) or not word["surface"]:
                raise ContractError("Word surface is missing")
            start, end = _find_word(text, word["surface"], cursor)
            word["start"] = _utf16_index(text, start)
            word["end"] = _utf16_index(text, end)
            cursor = end
            wid = word.get("id")
            if isinstance(wid, str):
                spans[wid] = (start, end)

        for chunk in sentence.get("chunks") or []:
            if not isinstance(chunk, dict) or not isinstance(chunk.get("text"), str) or not chunk["text"]:
                raise ContractError("Chunk text is missing")
            ids = chunk.get("wordIds", [])
            if not isinstance(ids, list):
                raise ContractError("Chunk wordIds must be an array")
            start, end = _find_chunk(text, chunk["text"], spans, ids)
            chunk["start"] = _utf16_index(text, start)
            chunk["end"] = _utf16_index(text, end)

    return repaired
