# Curriculum Rollout Status

Target: **3,000 sentences** = 500 per CEFR level × 6 levels.

## Current status

| Level | Calibration | Target | Status |
|---|---:|---:|---|
| A1 | 50 / 50 | 500 | 🟡 Calibration set created; Educational Validity Gate next |
| A2 | 0 / 50 | 500 | ⚪ Not started |
| B1 | 0 / 50 | 500 | ⚪ Not started |
| B2 | 0 / 50 | 500 | ⚪ Not started |
| C1 | 0 / 50 | 500 | ⚪ Not started |
| C2 | 0 / 50 | 500 | ⚪ Not started |

## Application integration status
- ✅ GitHub `main` is Source of Truth via `PROJECT_CARD.md`.
- ✅ Legacy and modern data are exposed through `material-engine.js`.
- 🟡 Canonical `index.html` now includes A1–C2 selection and category filtering; real-browser/device verification is pending.
- ✅ Previous full Learn UI is preserved as `legacy-index.html` during migration.
- ⏳ A1 Educational Validity Gate has not yet run.
- ⏳ Automated validation has not yet been installed.

## Data architecture in repo
- `PROJECT_CARD.md` — canonical project state and next evidence step.
- `EVIDENCE_GATE.md` — PASS/FAIL/NOT VERIFIED rules and gate definitions.
- `MATERIAL_CURRICULUM_3000.md` — curriculum specification and quality gate.
- `curriculum.js` — CEFR/category taxonomy, dataset rules, validation helper.
- `material-engine.js` — canonical compatibility layer for legacy and modern material data.
- `materials-a1-calibration.js` — first A1 50-sentence calibration corpus.
- `materials.js` — legacy corpus, preserved and currently `UNCLASSIFIED`.
- `index.html` — canonical Learn surface.
- `legacy-index.html` — preserved previous Learn implementation.

## Next implementation gate
Before A1 expands from 50 to 500:
- [ ] Russian naturalness audit
- [ ] CEFR A1 difficulty audit
- [ ] case-label audit
- [ ] verb aspect audit
- [ ] word-anatomy audit
- [ ] duplicate/near-duplicate audit
- [ ] Japanese pathway audit 🇯🇵
- [ ] English pathway audit 🇬🇧
- [ ] category balance check (10 × 5)
- [ ] decide how existing `materials.js` items map into new stable IDs through evidence, not guesswork

## Non-negotiable learning rules
- 🎧 Every Russian word/chunk/sentence should remain tappable for sound.
- 🧩 Prefer word → meaning chunk → sentence progression.
- 📐 Case view shows all six cases when a full paradigm is available, with current form marked 📍.
- 🔄 Verb entries expose imperfective/perfective pair when relevant.
- 🧬 Long Russian words preserve original spelling and also expose meaningful decomposition.
- 🪆 Deep information is optional and discovered progressively.
- 🇯🇵 and 🇬🇧 explanation pathways remain separate, not literal translations of each other.
