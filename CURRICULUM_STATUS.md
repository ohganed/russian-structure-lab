# Curriculum Rollout Status

Target: **3,000 sentences** = 500 per CEFR level × 6 levels.

## Current status

| Level | Calibration | Target | Status |
|---|---:|---:|---|
| A1 | 50 / 50 | 500 | 🟡 Calibration set created; quality gate next |
| A2 | 0 / 50 | 500 | ⚪ Not started |
| B1 | 0 / 50 | 500 | ⚪ Not started |
| B2 | 0 / 50 | 500 | ⚪ Not started |
| C1 | 0 / 50 | 500 | ⚪ Not started |
| C2 | 0 / 50 | 500 | ⚪ Not started |

## Data architecture in repo
- `MATERIAL_CURRICULUM_3000.md` — curriculum specification and quality gate.
- `curriculum.js` — CEFR/category taxonomy, dataset rules, validation helper.
- `materials-a1-calibration.js` — first A1 50-sentence calibration corpus.
- `materials.js` — existing corpus to be migrated into the 3,000-sentence matrix.

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
- [ ] decide how existing `materials.js` items map into the new stable IDs

## Non-negotiable learning rules
- 🎧 Every Russian word/chunk/sentence should remain tappable for sound.
- 🧩 Prefer word → meaning chunk → sentence progression.
- 📐 Case view shows all six cases when a full paradigm is available, with current form marked 📍.
- 🔄 Verb entries expose imperfective/perfective pair when relevant.
- 🧬 Long Russian words preserve original spelling and also expose meaningful decomposition.
- 🪆 Deep information is optional and discovered progressively.
- 🇯🇵 and 🇬🇧 explanation pathways remain separate, not literal translations of each other.
