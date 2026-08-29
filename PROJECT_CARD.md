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
2. ✅ Unify the legacy and new material engines.
3. 🟡 Integrate A1–C2 selection into the main Learn UI — implemented; browser/device verification pending.
4. ⏳ Run Educational Validity Gate on the A1 50-sentence calibration set.
5. ⏳ Add automated validation.
6. ⏳ Expand A1 from 50 to 500 validated sentences.
7. ⏳ Expand A2 → B1 → B2 → C1 → C2.

## 🟢 CONFIRMED
Repository evidence exists for these items.

- Main GitHub Pages app exists in `index.html`.
- The previous full Learn implementation is preserved as `legacy-index.html` before the canonical Learn migration.
- Existing legacy lesson corpus exists in `materials.js` and is preserved unchanged.
- CEFR curriculum definition exists in `curriculum.js`.
- A1 calibration corpus exists in `materials-a1-calibration.js`.
- One canonical compatibility layer exists in `material-engine.js`.
- Both legacy and A1 calibration materials pass through the same Material Engine API.
- Legacy materials remain `UNCLASSIFIED`; they are not assigned a CEFR level without evidence.
- Curriculum status is tracked in `CURRICULUM_STATUS.md`.
- A1–C2 curriculum browser exists in `level-browser.html`.
- My Material exploratory reader exists in `my-material.html`.

## 🟡 IMPLEMENTED / NOT FULLY VERIFIED
Code exists, but the project must not describe these as fully validated yet.

- A1–C2 selector inside canonical `index.html`.
- Category filtering inside canonical Learn.
- Empty A2–C2 levels remain selectable and show explicit 0/500 state rather than disappearing.
- Canonical Learn consumes `material-engine.js` rather than directly defining curriculum logic.
- 🎧 Audio behavior across all supported browsers/devices.
- 📐 Case labels and full paradigms across all material entries.
- 🔄 Imperfective/perfective pairing across all verbs.
- 🧬 Morphological decomposition accuracy beyond explicitly curated entries.
- 📱 Mobile navigation and layout across current iPhone/Safari versions.
- A1 calibration-set linguistic and pedagogical quality.

## 🔵 DECIDED
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
- Legacy material is preserved during migration and never silently promoted into a CEFR level.

## ⚪ PLANNED
- Educational Validity Gate results stored as repository data.
- Automated curriculum schema validation, duplicate checks, ID checks, coverage checks, and selected pedagogical checks.
- 500 validated sentences per CEFR level.
- Personal Encounter Graph / Map connected to general language nodes.
- Robust 🇯🇵 / 🇬🇧 explanation toggle or pathway system.
- Feature parity review between `legacy-index.html` and canonical Learn before retiring legacy UI.

## 🔴 KNOWN ISSUES
1. A1 calibration corpus has not passed Educational Validity Gate.
2. A2–C2 curriculum slots exist but their calibration corpora are not yet populated.
3. My Material is still largely Japanese-pathway oriented.
4. Some morphology is heuristic/local estimation and must not be treated as linguistically verified.
5. Automated repository validation is not yet installed.
6. Canonical Learn integration requires real browser/device verification before Step 3 can be marked PASS.
7. Legacy Learn has features not yet migrated to canonical Learn; `legacy-index.html` remains available during migration.

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
- **PASS** — required evidence exists and the gate passed.
- **FAIL** — evidence shows a requirement is not met.
- **NOT VERIFIED** — implementation or claim has not yet been tested sufficiently.
- **IMPLEMENTED / NOT VERIFIED** — code exists, but verification is incomplete.

Never use “complete”, “working”, “correct”, or equivalent for a major feature without repository evidence.

## ➡️ NEXT EVIDENCE STEP
**Finish Step 3 verification, then begin Step 4: Educational Validity Gate on A1 50.**

Step 3 PASS requires evidence that canonical `index.html` in a real browser:
- opens A1 and displays the calibration corpus;
- allows A1 category filtering;
- allows A2, B1, B2, C1, C2 selection without dead navigation;
- shows 0/500 clearly for empty levels;
- returns to A1 without stale-index errors;
- plays word and sentence audio where browser TTS is available;
- keeps legacy corpus accessible as Legacy without CEFR misclassification.

Step 4 then audits all 50 A1 sentences for naturalness, CEFR fit, pedagogical framing, case labels, aspect, morphology, duplication, and 🇯🇵/🇬🇧 pathway quality.
