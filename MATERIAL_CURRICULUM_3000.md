# Russian Structure Lab — 3,000 Sentence Curriculum

## Goal
Russian Structure Lab will contain **3,000 core sentences**: **500 sentences for each CEFR level A1, A2, B1, B2, C1, C2**.

The corpus is not a flat example-sentence list. Each sentence is an entrance into the Russian language network: sound, chunks, case, aspect, morphology, syntax, meaning, situation, examples, and personal encounters.

## Core principle
**Same worlds, deeper language.** Learners revisit the same semantic/situational categories from A1 through C2. Complexity grows spirally rather than by abandoning earlier topics.

## Matrix
Each CEFR level has 10 categories × 50 sentences = 500.

| Category | A1 | A2 | B1 | B2 | C1 | C2 |
|---|---:|---:|---:|---:|---:|---:|
| 🏠 Daily Life | 50 | 50 | 50 | 50 | 50 | 50 |
| 👥 People & Relationships | 50 | 50 | 50 | 50 | 50 | 50 |
| 💼 Work & Study | 50 | 50 | 50 | 50 | 50 | 50 |
| 🚆 Travel & Movement | 50 | 50 | 50 | 50 | 50 | 50 |
| 🍽️ Food & Shopping | 50 | 50 | 50 | 50 | 50 | 50 |
| ❤️ Body & Emotion | 50 | 50 | 50 | 50 | 50 | 50 |
| 🌦️ Nature & Environment | 50 | 50 | 50 | 50 | 50 | 50 |
| 📰 Society & Information | 50 | 50 | 50 | 50 | 50 | 50 |
| 🧠 Thought & Opinion | 50 | 50 | 50 | 50 | 50 | 50 |
| 🎭 Culture & Expression | 50 | 50 | 50 | 50 | 50 | 50 |
| **TOTAL** | **500** | **500** | **500** | **500** | **500** | **500** |

Grand total: **3,000 sentences**.

## Level character
- 🌱 **A1** — concrete survival language; short clauses; high-frequency vocabulary; basic present/past/future; first encounters with cases in meaningful contexts.
- 🌿 **A2** — routine life, simple narration, requests, plans, comparisons; broader case/preposition patterns and aspect contrasts.
- 🌳 **B1** — connected narration, reasons, experiences, opinions, conditions; productive aspect choice and more complex syntax.
- 🌲 **B2** — argument, explanation, negotiation, news, abstract relations; flexible syntax, register awareness, denser morphology.
- 🏛️ **C1** — precise abstract expression, social/academic discourse, stance, qualification, implication, stylistic choice.
- 🌌 **C2** — highly nuanced expression, rhetoric, literature, irony, ambiguity, idiomatic and stylistically marked language.

## Required sentence metadata
Every sentence should eventually carry:
- `id`
- `level` (A1–C2)
- `category`
- `subCategory`
- Russian original
- Japanese pathway explanation 🇯🇵
- English pathway explanation 🇬🇧
- 🎧 sound / stress data
- 🧩 meaning chunks
- 🧱 sentence architecture
- 📐 case focus
- 🔄 aspect focus (verbs should expose imperfective/perfective pair where relevant)
- 🧬 word anatomy focus
- 🌳 word-family links
- 🧠 semantic/concept links
- 🎭 situation/register
- 📖 related examples
- 🗺️ encounter-network hooks

## Word-display rule
Russian spelling can be visually long. A target word must preserve the **original spelling** and, where linguistically meaningful, also expose a decomposition such as prefix + root/stem + suffix + ending/postfix. Decomposition is an optional deeper layer and must never replace the original word.

## Case-display rule
When a declinable target is examined, show the complete six-case paradigm appropriate to masculine, feminine, neuter, or plural form when available. Highlight the case used in the current sentence with 📍 rather than hiding the other cases.

## Learning architecture
Surface: calm Russian text.

Tap → 🎧 sound → meaning → 🧩 chunk → 🧱 structure → 📐/🔄/🧬 analysis → 🌳/🧠/🎭 network → 🗺️ personal encounters.

The learner may stop at any depth. Deep information is discovered, not presented all at once.

## Production quality gate
Do **not** bulk-generate all 3,000 sentences without validation.

For each CEFR level:
1. Design category/grammar/lexical coverage.
2. Produce a 50-sentence calibration set (5 per category).
3. Review CEFR authenticity, natural Russian, pedagogical progression, duplicate concepts, morphology/aspect/case accuracy, and JP/EN explanation quality.
4. Correct the generation rules.
5. Expand each category toward 50 sentences.
6. Run duplicate and coverage audits.
7. Approve the 500-sentence level only after the quality gate passes.

## Existing corpus migration
The existing `materials.js` corpus is seed material, not a separate legacy course. Existing sentences should be assigned CEFR level + category + metadata and absorbed into this 3,000-sentence matrix. Gaps are then filled systematically.

## Dataset IDs
Recommended stable IDs:
`A1-DL-001` … `A1-DL-050`
`A1-PR-001` … etc.

Category codes:
- DL Daily Life
- PR People & Relationships
- WS Work & Study
- TM Travel & Movement
- FS Food & Shopping
- BE Body & Emotion
- NE Nature & Environment
- SI Society & Information
- TO Thought & Opinion
- CE Culture & Expression

Repeat the same scheme for A2, B1, B2, C1, C2.
