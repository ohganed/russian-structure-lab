# Russian Structure Lab — Evidence Gate

This file defines how the project decides whether a feature or curriculum stage is actually complete.

## Core rule
A claim is not accepted because it was discussed in chat, appears in a screenshot, or was intended in a design note. It must have repository evidence on `main`.

## Gate states
- **PASS** — implementation/data exists and all required checks for the gate passed.
- **FAIL** — a required check is known to fail.
- **NOT VERIFIED** — required verification has not been executed or evidence is missing.
- **IMPLEMENTED / NOT VERIFIED** — code exists but gate evidence is incomplete.

## Standard feature gate
Before a feature is marked PASS, record evidence for:

1. **Correctness** — implementation matches its stated behavior.
2. **User path** — a learner can enter, use, and leave the feature without a dead end.
3. **Data integrity** — existing learner/material data is not silently lost or corrupted.
4. **Failure behavior** — unavailable/incomplete data is shown honestly rather than hidden or fabricated.
5. **Mobile behavior** — relevant mobile layout/navigation is verified when the feature is mobile-facing.
6. **Accessibility of core action** — the main learning action remains obvious and usable.
7. **Documentation** — `PROJECT_CARD.md` reflects the real state.

## Educational Validity Gate (EVG)
Curriculum material must not be expanded from a calibration set until the calibration set passes these checks:

### A. Linguistic correctness
- Natural Russian.
- Correct morphology.
- Correct case analysis.
- Correct verb aspect pairing where relevant.
- Correct stress/audio text when curated.
- No misleading decomposition.

### B. CEFR validity
- Vocabulary and syntax match the intended level.
- Sentence length and abstraction are appropriate.
- The item does not rely on unexplained advanced structures unless intentionally marked as an encounter.

### C. Pedagogical validity
- The learner can understand why the sentence is present.
- Chunks are meaningful units, not arbitrary word splits.
- Grammar metadata does not overload the surface UI.
- JP and EN pathways explain from their own linguistic perspective.
- Potential misconceptions are identified.

### D. Corpus quality
- Category balance matches the curriculum matrix.
- Duplicate and near-duplicate items are controlled.
- IDs are stable and unique.
- Required fields are present.
- Coverage is intentional rather than accidental.

### E. Interaction validity
- Russian sentence is playable.
- Russian chunks are intended to be playable.
- Russian words are intended to be playable.
- Progressive disclosure remains intact.

## Curriculum expansion gates

### Gate A1-50 → A1-500
Status: **NOT VERIFIED**

Requires:
- EVG for all 50 calibration items;
- correction of all FAIL items;
- automated schema/ID/duplicate/coverage validator installed;
- normalized Material Engine in use;
- A1 level accessible from the main Learn UI.

### Gate A1-500 → A2
Status: **NOT VERIFIED**

Requires:
- 500 A1 items pass automated validation;
- representative manual EVG review after expansion;
- Learn filtering/navigation remains usable at 500 items;
- no regression in audio/chunk/structure interactions.

The same gate pattern applies to A2 → B1 → B2 → C1 → C2.

## Evidence record format
For any major gate, record:

```md
### Gate: <name>
Date: YYYY-MM-DD
Commit: <sha>
State: PASS | FAIL | NOT VERIFIED | IMPLEMENTED / NOT VERIFIED

Evidence:
- ...

Known limitations:
- ...

Next action:
- ...
```

## Current evidence record
### Gate: Source of Truth foundation
Date: 2026-08-29
State: PASS

Evidence:
- `PROJECT_CARD.md` defines canonical status and implementation order.
- `EVIDENCE_GATE.md` defines completion language and required gates.
- Repository `main` is explicitly designated as Source of Truth.

Known limitations:
- Material engine is still split between legacy and new curriculum paths.
- Automated validation is not yet installed.

Next action:
- Step 2: unify legacy and new material engines.
