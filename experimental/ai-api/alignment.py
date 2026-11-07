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
    """Find an exact chunk source span without trusting invented word IDs.

    Known IDs can disambiguate repeated phrases. Unknown IDs may be repaired
    later ONLY if the literal text determines a unique, whole-word span.
    """
    if not isinstance(word_ids, list):
        raise ContractError("Chunk wordIds must be an array")
    # An LLM sometimes writes JSON numbers (1) rather than string IDs ("1"),
    # or uses null placeholders. These values are never authoritative:
    # convert integral labels only for locating known anchors, and otherwise
    # infer references solely from an exact, unambiguous source-text span.
    if any(type(wid) not in (str, int) and wid is not None for wid in word_ids):
        raise ContractError("Chunk wordIds contains unsupported values")
    normalized = [str(wid) if type(wid) is int else wid for wid in word_ids]
    known = [wid for wid in normalized if wid is not None and wid in word_spans]

    if known and len(known) == len(normalized):
        first = min(word_spans[wid][0] for wid in known)
        last = max(word_spans[wid][1] for wid in known)
        if text[first:last] == value:
            return first, last

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
            if contained and not partial and all(wid in contained for wid in known):
                candidates.append((at, end))
        at = text.find(value, at + 1)
    if len(candidates) != 1:
        raise ContractError("Chunk text cannot be aligned unambiguously: " + repr(value))
    return candidates[0]



def _repair_structure_refs(node, text, word_spans):
    """Repair unknown word references only when node.text identifies words exactly.

    Do not reinterpret grammar or guess referents. A repeated or nonliteral
    phrase without a unique anchor remains a hard error.
    """
    if not isinstance(node, dict):
        raise ContractError("Structure tree node must be an object")
    refs = node.get("refIds", [])
    if not isinstance(refs, list) or any(not isinstance(ref, str) for ref in refs):
        raise ContractError("Structure refIds must be an array of word IDs")

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
            if any(type(wid) is not str or wid not in spans for wid in ids):
                # Reconstruct references from source text, not the model's
                # integer/null labels. The strict validator still runs afterward.
                # Exact source text and existing IDs are the sole authorities.
                matched = [wid for wid, (a, b) in spans.items()
                           if start <= a and b <= end]
                if not matched:
                    raise ContractError("Chunk cannot identify any source words")
                chunk["wordIds"] = matched
            chunk["start"] = _utf16_index(text, start)
            chunk["end"] = _utf16_index(text, end)

        tree = (sentence.get("structure") or {}).get("tree")
        if tree is not None:
            _repair_structure_refs(tree, text, spans)

    return repaired
