# Russian Structure Lab — 3,000 Sentence Curriculum

## Goal
Russian Structure Lab will contain **3,000 core sentences**: **500 sentences for each CEFR level A1, A2, B1, B2, C1, C2**.

The corpus is not a flat example-sentence list. Each sentence is an entrance into the Russian language network: sound, chunks, case, aspect, morphology, syntax, meaning, situation, examples, and personal encounters.

## Core principle
**Same worlds, deeper language.** Learners revisit the same semantic/situational categories from A1 through C2. Complexity grows spirally rather than by abandoning earlier topics.

## Primary learning loop
The learner-facing default path is:

**🎭 Situation → 🔤 Words → 🏗️ Sentence → 🎧 Audio → 🗺️ Re-encounter**

This is the surface learning loop. Grammar is not the starting screen. The learner first enters a meaningful scene, notices a small set of useful words, meets them as a sentence, hears the whole utterance naturally, and later meets the same language again in another context.

### 🎭 1. Situation
Start from a concrete communicative or human scene: ordering tea, meeting a friend, feeling cold, finding a station, reading a message. Situation supplies meaning before explanation.

### 🔤 2. Words
Expose only the few words needed to enter the sentence. Every Russian word remains tappable for sound. Do not turn this step into a vocabulary-list memorization screen.

### 🏗️ 3. Sentence
Recombine the words into a natural Russian utterance. Preserve the sequence **Words → Meaning Chunks → Sentence** where it helps comprehension. The sentence is an entry point into the deeper language network, not an isolated item to memorize.

### 🎧 4. Audio
The whole sentence is heard as natural connected Russian. Word/chunk/sentence audio should all be reachable by touch. Slower study audio may be offered as a deeper option, but natural rhythm remains the reference.

### 🗺️ 5. Re-encounter
Learning continues when a known word, chunk, case relation, aspect pair, or construction appears again in a new situation. Re-encounter is preferred over repetitive quiz-style recall.

Example network:
`без сахара` ☕ → `без молока` 🥛 → `без машины` 🚶 → `без друга` 👤

A re-encounter should preserve both the current situation and the earlier encounter link when possible, gradually building a personal map of Russian rather than a scorecard.

## Surface and underground architecture
The app has two complementary layers.

**Surface — experience Russian**

`🎭 Situation → 🔤 Words → 🏗️ Sentence → 🎧 Audio → 🗺️ Re-encounter`

**Underground — investigate Russian**

`🧩 Chunk → 🧱 Syntax → 📐 Case → 🔄 Aspect → 🧬 Word Anatomy → 🌳 Word Family → 🧠 Meaning / Contrast → 🎭 Register → 📖 Examples → 🗺️ Encounters`

The surface must remain calm. The underground may be deep. Complexity is discovered by tapping, not presented all at once. 📍 Current Focus remains visible while moving through deeper branches.

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
- 🎭 `situation` — scene/communicative intent before grammar
- 🔤 `words` — minimal entry vocabulary, with audio hooks
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
- 🗺️ `reEncounters` — links to earlier/later sentences, chunks, structures, and personal encounters

## Re-encounter design rules
1. Reuse should be meaningful, not accidental duplication.
2. A familiar item should appear in a changed situation, collocation, grammatical relation, or register.
3. Prefer a small number of repeated high-value structures across many worlds over one-off vocabulary density.
4. Re-encounter links may connect sentence ↔ sentence, word ↔ word, chunk ↔ chunk, case relation ↔ example, aspect pair ↔ event type, and general graph ↔ personal encounter graph.
5. Do not force a quiz after every encounter. Recognition, prediction, listening, reconstruction, and optional production can all count as learning contact.
6. The backend may count encounters and spacing quietly; the learner-facing surface should emphasize the Russian world, not scores.

## Word-display rule
Russian spelling can be visually long. A target word must preserve the **original spelling** and, where linguistically meaningful, also expose a decomposition such as prefix + root/stem + suffix + ending/postfix. Decomposition is an optional deeper layer and must never replace the original word.

## Case-display rule
When a declinable target is examined, show the complete six-case paradigm appropriate to masculine, feminine, neuter, or plural form when available. Highlight the case used in the current sentence with 📍 rather than hiding the other cases.

## Learning architecture
Default surface journey:

`🎭 Situation → 🔤 Words → 🏗️ Sentence → 🎧 Audio → 🗺️ Re-encounter`

Optional Matryoshka deep dive:

`tap → 🎧 sound → meaning → 🧩 chunk → 🧱 structure → 📐/🔄/🧬 analysis → 🌳/🧠/🎭 network → 📖 examples → 🗺️ encounters`

The learner may stop at any depth. Deep information is discovered, not presented all at once.

## Production quality gate
Do **not** bulk-generate all 3,000 sentences without validation.

For each CEFR level:
1. Design category/grammar/lexical **and re-encounter** coverage.
2. Produce a 50-sentence calibration set (5 per category).
3. Review CEFR authenticity, natural Russian, pedagogical progression, duplicate concepts, morphology/aspect/case accuracy, JP/EN explanation quality, situation clarity, and usefulness of planned re-encounters.
4. Correct the generation rules.
5. Expand each category toward 50 sentences by selecting **Situation first**, then language that fills real coverage gaps.
6. Run duplicate, structure, vocabulary, and re-encounter-network audits.
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
