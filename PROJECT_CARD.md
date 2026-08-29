# Russian Structure Lab — Project Card

> **Source of Truth:** this repository on `main`.
>
> Chat conversations, screenshots, local notes, and design discussions are context only. A feature is considered real only when its state is represented here and supported by repository evidence.

## 🎯 Purpose
Russian Structure Lab is a calm, exploratory Russian-learning environment where learners touch Russian, hear it, notice structure, and progressively open deeper linguistic relationships without being forced through a dense grammar-first interface.

Core learning loop:

**🎧 hear → notice → 🧩 chunk → 🧱 structure → 📐 case / 🔄 aspect / 🧬 morphology → 🌳 word family / 🧠 meaning network → use**

The curriculum target is **3,000 core sentences**: 500 sentences at each CEFR level A1, A2, B1, B2, C1, C2.

## 🧭 Canonical implementation order
Work proceeds in this order unless this file is explicitly changed:

1. ✅ Introduce `PROJECT_CARD.md` and GitHub Source-of-Truth rules.
2. 🟡 Unify the legacy and new material engines — compatibility engine implemented; runtime self-test created; final verification/promotion into Learn pending.
3. ⏳ Integrate A1–C2 selection into the main Learn UI.
4. ⏳ Run Educational Validity Gate on the A1 50-sentence calibration set.
5. ⏳ Add automated validation.
6. ⏳ Expand A1 from 50 to 500 validated sentences.
7. ⏳ Expand A2 → B1 → B2 → C1 → C2.

## 🟢 CONFIRMED
Repository evidence exists for these items.

- Main GitHub Pages app exists in `index.html`.
- Existing legacy lesson corpus exists in `materials.js`.
- CEFR curriculum definition exists in `curriculum.js`.
- A1 calibration corpus exists in `materials-a1-calibration.js`.
- Curriculum status is tracked in `CURRICULUM_STATUS.md`.
- A1–C2 curriculum browser exists in `level-browser.html`.
- My Material exploratory reader exists in `my-material.html`.
- `material-engine.js` defines a canonical normalized material shape and adapters for legacy and modern material records.
- `level-browser.html` now reads curriculum counts through `RSL_MATERIAL_ENGINE` rather than directly reading only the A1 array.
- `MATERIAL_ENGINE_MIGRATION.md` documents the non-destructive migration path.
- `material-engine-selftest.html` exists as a runtime verification surface.

## 🟡 IMPLEMENTED / NOT FULLY VERIFIED
Code exists, but the project must not describe these as fully validated yet.

- Canonical Material Engine runtime behavior across the deployed GitHub Pages surface.
- 🎧 Audio behavior across all supported browsers/devices.
- 📐 Case labels and full paradigms across all material entries.
- 🔄 Imperfective/perfective pairing across all verbs.
- 🧬 Morphological decomposition accuracy beyond explicitly curated entries.
- 📱 Mobile navigation and layout across current iPhone/Safari versions.
- A1 calibration-set linguistic and pedagogical quality.
- Navigation between all app surfaces.

## 🔵 DECIDED
These are active design decisions even when implementation is incomplete.

- GitHub `main` is the project Source of Truth.
- Surface complexity must stay low; deep complexity is progressively disclosed.
- Every displayed Russian word/chunk/sentence should be tappable for sound where technically possible.
- No katakana pronunciation. Use Russian orthography and IPA where pronunciation explanation is needed.
- Verb learning should expose imperfective/perfective pairs where relevant.
- Russian word decomposition must preserve the original spelling.
- Unknown/heuristic morphology must be marked as uncertain rather than presented as verified fact.
- 🇯🇵 Japanese and 🇬🇧 English explanation paths are separate pedagogical paths, not literal translations of each other.
- 📍 Current Focus should remain visible while the learner explores deeper relationships.
- Emoji are Concept Anchors, not decoration.
- Curriculum is spiral: the same worlds recur from A1 to C2 with progressively deeper language.
- Legacy material receives `UNCLASSIFIED`, not an automatically guessed CEFR level.

## ⚪ PLANNED
- Main Learn consumer migrated to the canonical Material Engine.
- A1–C2 level selector inside the main Learn UI.
- Category filtering within each CEFR level.
- Educational Validity Gate results stored as repository data.
- Automated curriculum schema validation, duplicate checks, ID checks, coverage checks, and selected pedagogical checks.
- 500 validated sentences per CEFR level.
- Personal Encounter Graph / Map connected to general language nodes.
- Robust 🇯🇵 / 🇬🇧 explanation toggle or pathway system.

## 🔴 KNOWN ISSUES
1. `index.html` still reads the legacy `materials.js` path and is not yet driven by the canonical Material Engine.
2. Step 2 has repository implementation evidence but its deployed runtime self-test has not yet been independently verified in this record.
3. The A1 calibration corpus has not passed Educational Validity Gate.
4. A2–C2 curriculum slots exist but their calibration corpora are not yet populated.
5. My Material is still largely Japanese-pathway oriented.
6. Some morphology is heuristic/local estimation and must not be treated as linguistically verified.
7. Automated repository validation is not yet installed.

## ⚫ DEPRECATED / DO NOT ASSUME
- Do not treat the old `materials.js` structure as the final curriculum schema.
- Do not claim 3,000 sentences exist until repository data actually contains and validates them.
- Do not claim A1 is complete while only the 50-sentence calibration set exists.
- Do not claim Encounter Map is a complete persistent personal-language graph.
- Do not infer implementation from chat discussion alone.

## 📊 Current curriculum evidence
| Level | Calibration data | Final target | Evidence state |
|---|---:|---:|---|
| A1 | 50 | 500 | 🟡 calibration exists; EVG pending |
| A2 | 0 | 500 | ⚪ not started |
| B1 | 0 | 500 | ⚪ not started |
| B2 | 0 | 500 | ⚪ not started |
| C1 | 0 | 500 | ⚪ not started |
| C2 | 0 | 500 | ⚪ not started |

## ✅ Completion language
Use these terms consistently:

- **PASS** — required evidence exists and the gate passed.
- **FAIL** — evidence shows a requirement is not met.
- **NOT VERIFIED** — implementation or claim has not yet been tested sufficiently.
- **IMPLEMENTED / NOT VERIFIED** — code exists, but verification is incomplete.

Never use “complete”, “working”, “correct”, or equivalent for a major feature without repository evidence.

## ➡️ NEXT EVIDENCE STEP
**Finish Step 2 verification, then Step 3: integrate A1–C2 selection into the main Learn UI through the canonical Material Engine.**

Step 2 PASS requires:

- canonical normalized material shape — ✅ implemented;
- legacy compatibility adapter — ✅ implemented;
- A1 calibration accepted through same engine — ✅ implemented in engine path;
- no destructive deletion — ✅ confirmed;
- documented migration path — ✅ implemented;
- runtime self-test — 🟡 page created, verification record pending.

Step 3 will not silently reclassify legacy material. Empty levels must remain visible as `0 / 500` rather than disappearing.

See `EVIDENCE_GATE.md` for release/gate rules.
