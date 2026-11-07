"""Deterministic source alignment for Ollama-generated Russian lesson JSON.

The language model proposes lexical surfaces and chunk text, but must not
calculate character offsets. We calculate JS UTF-16 offsets from exact source
substrings; any text change, missing word or ambiguous chunk is rejected by
the final contract validator. No grammatical claims are corrected here.
"""
from copy import deepcopy
import unicodedata

from contract import ContractError


def _stable_id(value, prefix, index, existing):
    """Coerce the model's loose ID to a unique string owned by the server."""
    proposed = str(value) if type(value) is int else value
    if not isinstance(proposed, str) or not proposed.strip() or proposed in existing:
        proposed = f"{prefix}{index}"
        while proposed in existing:
            proposed += "_"
    existing.add(proposed)
    return proposed


def _utf16_index(text, index):
    return len(text[:index].encode("utf-16-le")) // 2


def _is_word_char(char):
    return char.isalnum() or char == "_" or unicodedata.category(char).startswith("M")


def _whole_token(text, start, end):
    """Prevent slicing through an original word; allow punctuation boundaries."""
    left_safe = start == 0 or not (
        _is_word_char(text[start - 1]) and _is_word_char(text[start])
    )
    right_safe = end == len(text) or not (
        _is_word_char(text[end - 1]) and _is_word_char(text[end])
    )
    return left_safe and right_safe


def _find_word(text, surface, start):
    at = text.find(surface, start)
    while at >= 0:
        after = at + len(surface)
        if _whole_token(text, at, after):
            return at, after
        at = text.find(surface, at + 1)
    raise ContractError("Cannot locate exact word in original sentence: " + repr(surface))


def _valid_anchors(word_ids, spans):
    """Model-provided IDs are hints for repeated text, never source authority."""
    if not isinstance(word_ids, list):
        return []
    out = []
    for value in word_ids:
        if type(value) is int:
            value = str(value)
        if isinstance(value, str) and value in spans and value not in out:
            out.append(value)
    return out


def _find_chunk(text, value, word_spans, word_ids):
    """Find exact source occurrence, preferring literal text over unreliable IDs.

    An exact single match wins even when AI references are wrong. For repeated
    phrases only, already-valid IDs can disambiguate. Every recovered span
    must contain complete original words, never partial Cyrillic tokens.
    """
    if value == text and word_spans:
        return 0, len(text)

    candidates = []
    at = text.find(value)
    while at >= 0:
        end = at + len(value)
        if _whole_token(text, at, end):
            contained = [wid for wid, (a, b) in word_spans.items()
                         if at <= a and b <= end]
            partial = any(
                a < end and b > at and not (at <= a and b <= end)
                for a, b in word_spans.values()
            )
            if contained and not partial:
                candidates.append((at, end, contained))
        at = text.find(value, at + 1)

    if len(candidates) == 1:
        return candidates[0][:2]
    if len(candidates) > 1:
        anchors = _valid_anchors(word_ids, word_spans)
        if anchors:
            anchored = [candidate for candidate in candidates
                        if all(ref in candidate[2] for ref in anchors)]
            if len(anchored) == 1:
                return anchored[0][:2]
    raise ContractError(
        "Chunk text cannot be aligned unambiguously to complete source words: "
        + repr(value)
    )


def _repair_structure_refs(node, text, word_spans):
    """Repair unknown word references only when node.text identifies words exactly.

    Do not reinterpret grammar or guess referents. A repeated or nonliteral
    phrase without a unique anchor remains a hard error.
    """
    if not isinstance(node, dict):
        raise ContractError("Structure tree node must be an object")
    refs = node.get("refIds", [])
    if not isinstance(refs, list):
        refs = [refs] if refs is not None else []
    refs = [str(ref) if type(ref) is int else ref for ref in refs]
    if any(not isinstance(ref, str) for ref in refs):
        # Non-string refs cannot identify source words, but literal node.text
        # may still be enough to reconstruct a precise mapping.
        refs = ["__invalid_ref__"]
    node["refIds"] = refs
    missing = any(ref not in word_spans for ref in refs)
    if missing:
        value = node.get("text")
        if not isinstance(value, str) or not value:
            raise ContractError("Structure has unknown word ref and no literal node text")

        candidates = []
        at = text.find(value)
        while at >= 0:
            end = at + len(value)
            if _whole_token(text, at, end):
                matched = [wid for wid, (a, b) in word_spans.items()
                           if at <= a and b <= end]
                partial = any(
                    (a < end and b > at) and not (at <= a and b <= end)
                    for a, b in word_spans.values()
                )
                # Keep every existing valid reference anchored in the candidate.
                known = [ref for ref in refs if ref in word_spans]
                if matched and not partial and all(ref in matched for ref in known):
                    candidates.append(matched)
            at = text.find(value, at + 1)

        if len(candidates) != 1:
            raise ContractError(
                "Structure has unknown word ref; node text is missing or ambiguous"
            )
        node["refIds"] = candidates[0]

    children = node.get("children", [])
    if not isinstance(children, list):
        raise ContractError("Structure children must be an array")
    for child in children:
        _repair_structure_refs(child, text, word_spans)


def align_generated_offsets(material, original):
    """Return a copy with deterministic offsets; never change original text.

    The final validate_material() step remains mandatory to detect missed
    lexical words, altered accents, invalid references, and omitted sentences.
    """
    if not isinstance(material, dict) or material.get("originalText") != original:
        raise ContractError("originalText differs from the submitted text")

    repaired = deepcopy(material)
    sentence_ids = set()
    for si, sentence in enumerate(repaired.get("sentences", []), start=1):
        if not isinstance(sentence, dict) or not isinstance(sentence.get("text"), str):
            raise ContractError("Missing sentence text")
        sentence["id"] = _stable_id(sentence.get("id"), "s", si, sentence_ids)
        text = sentence["text"]
        cursor = 0
        spans = {}
        word_ids = set()
        words = sentence.get("words") or []
        for wi, word in enumerate(words, start=1):
            if not isinstance(word, dict) or not isinstance(word.get("surface"), str) or not word["surface"]:
                raise ContractError("Word surface is missing")
            start, end = _find_word(text, word["surface"], cursor)
            word["start"] = _utf16_index(text, start)
            word["end"] = _utf16_index(text, end)
            cursor = end
            wid = _stable_id(word.get("id"), "w", wi, word_ids)
            word["id"] = wid
            spans[wid] = (start, end)

        chunk_ids = set()
        for ci, chunk in enumerate(sentence.get("chunks") or [], start=1):
            if not isinstance(chunk, dict) or not isinstance(chunk.get("text"), str) or not chunk["text"]:
                raise ContractError("Chunk text is missing")
            chunk["id"] = _stable_id(chunk.get("id"), "c", ci, chunk_ids)
            # All chunk references and positions come from literal source spans.
            # Ollama's wordIds (including missing, wrong and numeric IDs) are
            # only optional disambiguation hints for repeated identical text.
            start, end = _find_chunk(text, chunk["text"], spans, chunk.get("wordIds"))
            matched = [wid for wid, (a, b) in spans.items()
                       if start <= a and b <= end]
            if not matched:
                raise ContractError("Chunk cannot identify any complete source word")
            chunk["wordIds"] = matched
            chunk["start"] = _utf16_index(text, start)
            chunk["end"] = _utf16_index(text, end)

        tree = (sentence.get("structure") or {}).get("tree")
        if tree is not None:
            _repair_structure_refs(tree, text, spans)

    return repaired
