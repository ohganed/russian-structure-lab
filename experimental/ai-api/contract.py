"""Schema 1.0 contract shared by the experimental AI API.

Indices use JavaScript UTF-16 code units, because the existing AI Material
reader uses String.prototype.slice(start, end).
"""
import unicodedata


class ContractError(ValueError):
    """Reject generated material instead of silently saving corrupted data."""


def remove_stress(text):
    # Remove only combining acute accents; retain ё and all original letters.
    return unicodedata.normalize(
        "NFC", unicodedata.normalize("NFD", text).replace("\u0301", "")
    )


def js_slice(text, start, end):
    raw = text.encode("utf-16-le")
    if not (0 <= start < end <= len(raw) // 2):
        raise ContractError("Offset is outside sentence")
    try:
        return raw[2 * start : 2 * end].decode("utf-16-le")
    except UnicodeDecodeError as exc:
        raise ContractError("Offset splits a Unicode surrogate pair") from exc


def _offset_span(text, entry, field):
    if not isinstance(entry, dict):
        raise ContractError(field + " must be an object")
    start, end, surface = entry.get("start"), entry.get("end"), entry.get(field)
    if type(start) is not int or type(end) is not int or not isinstance(surface, str) or not surface:
        raise ContractError(field + " requires start/end integer offsets and nonempty text")
    if js_slice(text, start, end) != surface:
        raise ContractError(f"{field} offset mismatch: {surface!r}")
    stressed = entry.get("stressed")
    if isinstance(stressed, str) and remove_stress(stressed) != surface:
        raise ContractError(f"{field} stressed form changes original spelling: {surface!r}")
    return start, end


def validate_material(material, original):
    """Return validated object; raise ContractError on any structural mismatch."""
    if not isinstance(original, str) or not original.strip() or len(original) > 4000:
        raise ContractError("Input must contain 1..4000 characters")
    if not isinstance(material, dict):
        raise ContractError("Generated material must be a JSON object")
    if material.get("schemaVersion") != "1.0" or material.get("language") != "ru":
        raise ContractError("schemaVersion=1.0 and language=ru are mandatory")
    if material.get("originalText") != original:
        raise ContractError("originalText differs from the submitted text")
    sentences = material.get("sentences")
    if not isinstance(sentences, list) or not (1 <= len(sentences) <= 150):
        raise ContractError("sentences must be a nonempty array of at most 150 items")

    cursor = 0
    sentence_ids = set()
    for si, sentence in enumerate(sentences):
        if not isinstance(sentence, dict):
            raise ContractError("sentence must be an object")
        sid, text = sentence.get("id"), sentence.get("text")
        if not isinstance(sid, str) or not sid or sid in sentence_ids:
            raise ContractError("sentence IDs must be unique nonempty strings")
        sentence_ids.add(sid)
        if not isinstance(text, str) or not text:
            raise ContractError(f"{sid}: text missing")
        pos = original.find(text, cursor)
        if pos < 0 or original[cursor:pos].strip():
            raise ContractError(f"{sid}: sentence changed, reordered, or omitted")
        cursor = pos + len(text)
        stressed_text = sentence.get("stressedText")
        if isinstance(stressed_text, str) and remove_stress(stressed_text) != text:
            raise ContractError(f"{sid}: stressedText changes original spelling")

        words, chunks = sentence.get("words"), sentence.get("chunks")
        if not isinstance(words, list) or not words:
            raise ContractError(f"{sid}: words must be a nonempty array")
        if not isinstance(chunks, list) or not chunks:
            raise ContractError(f"{sid}: chunks must be a nonempty array")
        ids, last, covered = set(), 0, []
        for word in words:
            wid = word.get("id") if isinstance(word, dict) else None
            if not isinstance(wid, str) or not wid or wid in ids:
                raise ContractError(f"{sid}: duplicate/missing word id")
            ids.add(wid)
            start, end = _offset_span(text, word, "surface")
            if start < last:
                raise ContractError(f"{sid}: word spans overlap/out of order")
            last = end
            covered.append((start, end))
        # Prevent missing entire words while tolerating punctuation between tokens.
        units = text.encode("utf-16-le")
        for i in range(0, len(units), 2):
            # Uncovered UTF-16 units are checked only at complete code points below.
            pass
        uncovered = []
        prev = 0
        for start, end in covered:
            uncovered.append(units[2 * prev : 2 * start].decode("utf-16-le"))
            prev = end
        uncovered.append(units[2 * prev :].decode("utf-16-le"))
        if any(c.isalpha() or c.isdigit() for gap in uncovered for c in gap):
            raise ContractError(f"{sid}: words omit lexical text")

        chunk_ids = set()
        for chunk in chunks:
            cid = chunk.get("id") if isinstance(chunk, dict) else None
            if not isinstance(cid, str) or not cid or cid in chunk_ids:
                raise ContractError(f"{sid}: duplicate/missing chunk id")
            chunk_ids.add(cid)
            _offset_span(text, chunk, "text")
            if any(wid not in ids for wid in chunk.get("wordIds", [])):
                raise ContractError(f"{sid}: unknown wordIds in chunk")
        tree = (sentence.get("structure") or {}).get("tree")
        if tree is not None:
            def visit(node):
                if not isinstance(node, dict):
                    raise ContractError(f"{sid}: invalid structure node")
                for ref in node.get("refIds", []):
                    if ref not in ids:
                        raise ContractError(f"{sid}: structure has unknown word ref")
                for child in node.get("children", []):
                    visit(child)
            visit(tree)
    if original[cursor:].strip():
        raise ContractError("Input has unprocessed sentences")
    return material
