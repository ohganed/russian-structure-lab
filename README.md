# Russian Structure Lab

Touch Russian, hear it, and open its structure.

## Source of Truth
The repository on `main` is canonical. Start with:
- `PROJECT_CARD.md` — current project state, evidence status, and next step.
- `EVIDENCE_GATE.md` — PASS / FAIL / NOT VERIFIED rules.
- `CURRICULUM_STATUS.md` — curriculum rollout state.

## App surfaces
- `index.html` — canonical Learn surface using the Material Engine and A1–C2 selection.
- `legacy-index.html` — preserved previous Learn surface during migration.
- `level-browser.html` — curriculum status browser.
- `my-material.html` — exploratory My Material reader.
- `ai-material.html` — AI-assisted reading/material surface on the AI-material feature branch.

## AI Material workflow

Russian text → copy the built-in analysis prompt → analyze in ChatGPT or another capable AI → paste the generated JSON → validate → save locally → study.

The app does **not** call a paid/external AI API. Imported AI material is stored separately in `russianStructureLab.aiLibrary.v1` and is **not CEFR-certified curriculum material**.

AI material progressively exposes:
- Word Anatomy / lemma / meaning
- case, gender, number, agreement, declension
- verb conjugation and imperfective/perfective aspect
- Meaning Chunks
- Sentence Architecture
- Russian TTS where the browser provides `ru-RU`
- confidence and alternative analysis for uncertain AI output

A hand-checked import fixture is available at `ai-material-sample.json`.

## Learning architecture
- 🎧 Words → 🧩 Meaning Chunks → 🧱 Sentence Architecture
- 📐 Russian cases and inflection
- 🔄 Aspect as perspective
- 🧬 Original spelling plus meaningful morphology
- 🪆 Progressive disclosure rather than grammar overload

Do not infer completion from chat history. Use repository evidence and the gates above.
