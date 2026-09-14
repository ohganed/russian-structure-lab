# Russian Structure Lab — AI Material Import Design

Date: 2026-09-14
Status: Approved in chat; awaiting spec review before implementation

## 1. Goal

Add an AI-assisted material-import workflow to Russian Structure Lab, modeled on the existing Arabic Structure Lab workflow:

Russian text → copy built-in analysis prompt → analyze in ChatGPT/another AI → copy generated JSON → paste into Russian Structure Lab → validate → save locally → study as structured material.

The app must not require a paid external AI API. The app owns the prompt, schema, importer, validation, rendering, and local storage. The user performs the AI analysis outside the app and pastes the result back in.

## 2. Preserve the Existing Learning Model

The current canonical Russian Structure Lab remains situation-first for curated curriculum material:

Situation → Words → Sentence → Audio → Re-encounter

AI-imported reading material gets a dedicated reading/analysis surface rather than being forced into the same flow:

Text → Words → Meaning Chunks → Sentence Architecture → Audio → Aspect / Morphology

Existing A1–C2 curriculum behavior, legacy material, Material Engine usage, and Aspect Lab must remain intact.

## 3. User Flow

1. User opens `AI Material` / `My Material` import.
2. User pastes Russian text.
3. App offers:
   - `Copy analysis prompt`
   - `Copy text + prompt`
4. User runs the prompt in ChatGPT or another capable AI.
5. AI returns one valid JSON object only.
6. User pastes JSON into the app.
7. App validates the JSON before accepting it.
8. If valid, the material is saved locally and immediately opened as a lesson.
9. Saved AI materials appear in a local library and can be reopened later.

## 4. Russian Analysis Schema

Top-level fields:

- `schemaVersion`
- `title`
- `language: "ru"`
- `originalText`
- `sentences[]`
- optional `sourceNote`
- optional `analysisMeta`

Each sentence should support:

- `id`
- `text` — exact original sentence text
- `ttsText`
- `overallMeaning { ja, en }`
- `sentenceType { ru, en, ja }`
- `words[]`
- `chunks[]`
- `structure`
- optional `grammarNotes[]`
- optional `alternativeAnalysis[]`

Each word should support, where linguistically applicable:

- `id`
- `surface`
- `stressed`
- `start`, `end`
- `meaning { ja, en }`
- `lemma`
- `partOfSpeech { ru, en, ja }`
- `morphemes[]`
- `morphology`
- `grammar`
- `declension`
- `conjugation`
- `aspect`
- `aspectPair`
- `wordFamily[]`
- `relations`
- `confidence`
- `confidenceReason`
- `alternativeAnalysis`

### 4.1 Nouns / adjectives / pronouns

Where applicable expose:

- case
- gender
- number
- animacy
- declension type
- ending
- stem
- agreement
- syntactic role

For adjective-noun relationships, connect the words through relation IDs so the UI can highlight agreement.

### 4.2 Verbs

Where applicable expose:

- lemma
- imperfective/perfective aspect
- aspect pair
- tense
- person
- number
- gender for past forms
- mood
- reflexive status
- conjugation class if confidently known
- prefix / stem / suffix / ending decomposition when useful

Aspect analysis must distinguish lexical aspect information from pedagogical interpretation. If the aspect pair is uncertain or irregular, mark it as uncertain rather than inventing one.

### 4.3 Stress

Do not modify `originalText` or `sentence.text` by inserting stress marks.

Use a separate `stressed` field for words and optional `stressedText` for sentences.

## 5. Meaning Chunks

Chunks represent useful semantic/syntactic groups rather than mechanical token groups.

Each chunk should support:

- `id`
- `text`
- `stressed`
- `start`, `end`
- `wordIds[]`
- `type`
- `meaningOrder { ja, en }`
- `naturalMeaning { ja, en }`
- `function { ru, en, ja }`
- `headWordId`
- `structureNodeId`
- optional `note`

The app should distinguish Russian-order comprehension from natural translation.

## 6. Sentence Architecture

The analysis prompt must not force every sentence into an English-only SVOC model.

The structure layer should represent Russian syntax using concepts such as:

- subject
- predicate
- verb
- object
- indirect object
- predicative
- attribute/modifier
- prepositional phrase
- adverbial phrase
- subordinate clause
- relative clause
- infinitive construction
- impersonal construction
- omitted / implicit elements

Each structure tree node should support:

- `id`
- `type`
- `labelRu`
- `labelEn`
- `labelJa`
- `text`
- `refIds[]`
- `children[]`

Word → chunk → structure references must be navigable in both directions where possible.

## 7. Progressive Disclosure UI

The Arabic Structure Lab is the visual/interaction reference.

### 7.1 Reader

The Russian text is the main surface. Tapping a word opens a bottom sheet / detail panel.

Default word view shows only:

- surface/stressed form
- meaning
- lemma
- part of speech

Expanded view reveals:

- case / gender / number / ending
- morphology
- declension or conjugation
- aspect
- morphemes
- syntactic role

Deep view may reveal:

- aspect pair
- word family
- alternative analysis
- confidence details

### 7.2 Meaning Chunks

A dedicated Chunks view lists chunk text, Russian-order meaning, natural meaning, and function. Selecting a chunk highlights its words in the reader.

### 7.3 Sentence Architecture

A dedicated Structure view renders the analysis tree. Selecting a node highlights the linked words in the source sentence.

### 7.4 Audio

Sentence, chunk, and word playback use Russian TTS (`ru-RU`) when available.

The imported material must remain usable even if TTS is unavailable.

## 8. Prompt Design

The app contains a Russian-specific prompt inspired by Arabic Structure Lab v1.2.

The prompt must require:

- valid JSON only
- no Markdown fences or commentary
- exact preservation of original text
- complete processing of all sentences
- offset validation compatibility (`sentence.text.slice(start,end) === surface`)
- field-level confidence
- no invented morphology, aspect pairs, conjugation classes, or etymology
- explicit uncertainty / alternative analysis
- Word Anatomy → Meaning Chunks → Sentence Architecture ordering
- Japanese + English learning explanations
- audio-ready text fields
- progressive-disclosure-compatible JSON

The prompt should favor modern, natural Russian and educational usefulness over exhaustive linguistic detail.

## 9. Import Validation

Before saving an imported lesson, validate at minimum:

1. JSON parses successfully.
2. Top-level object exists.
3. `language === "ru"`.
4. `sentences` is non-empty.
5. Every sentence has `text`.
6. Every word with integer `start/end` satisfies exact substring matching.
7. Every chunk with integer `start/end` satisfies exact substring matching.
8. Duplicate IDs inside the same sentence are rejected or reported.
9. Broken `wordIds` / `refIds` are reported.
10. Unsupported schema versions produce a clear error instead of silent corruption.

Validation errors must identify the sentence/word/chunk involved where practical.

## 10. Storage

Use a separate local-storage namespace for imported AI material so curriculum data remains canonical and untouched.

Suggested key:

`russianStructureLab.aiLibrary.v1`

Store at least:

- stable lesson key
- title
- saved timestamp
- full imported JSON

Keep a reasonable cap (for example 30–50 local items) for the first implementation.

No imported material should silently become CEFR-certified curriculum content.

## 11. Files / Components

Preferred implementation shape:

- add a dedicated AI-material reader/import page or focused module rather than overloading canonical `index.html`
- keep the built-in prompt in a separate JS file where practical
- keep schema validation/import logic separate from rendering logic where practical
- link the new surface from canonical navigation and/or `my-material.html`

Exact file names may be adjusted after implementation planning, but isolation is preferred over growing `index.html` further.

## 12. Error Handling

- Invalid JSON: do not save; show parsing error.
- Offset mismatch: do not silently repair; identify the mismatch.
- Unsupported fields: ignore safely when possible.
- Missing optional analysis: render what exists; do not fail the entire lesson.
- Missing TTS: keep reading/analysis fully available.
- Low-confidence AI analysis: display confidence rather than hiding uncertainty.

## 13. Acceptance Criteria

PASS requires repository evidence for all of the following:

1. Existing canonical curriculum view still loads.
2. Existing A1/A2–C2/Legacy navigation behavior is not broken.
3. User can open AI Material import UI.
4. User can paste Russian text.
5. User can copy the Russian analysis prompt.
6. User can copy text + prompt in one action.
7. User can paste a valid generated JSON object.
8. App validates and loads it as a lesson.
9. Imported lesson persists after reload.
10. User can reopen it from a local library.
11. Word tapping shows progressively disclosed Russian analysis.
12. Meaning Chunks view works and highlights linked words.
13. Sentence Architecture view works and highlights linked words.
14. Sentence/word Russian TTS works where browser TTS is available.
15. Invalid JSON and offset mismatches are rejected with useful messages.
16. Imported AI material is clearly separate from CEFR-certified curriculum data.
17. Browser verification is performed on the resulting GitHub Pages-compatible surface.

## 14. Non-goals for First Implementation

Not required for the first version:

- calling OpenAI or another AI API directly from the app
- automatic cloud sync
- server-side database
- CEFR auto-classification
- automatic correction of AI JSON
- spaced repetition scheduling
- grading / right-wrong scoring
- full dependency-tree linguistics

## 15. Verification Language

Use:

- PASS — directly verified
- FAIL — direct evidence of failure
- UNVERIFIED — not sufficiently tested
- IMPLEMENTED / NOT VERIFIED — code exists but real verification is incomplete

Do not call the feature complete merely because the UI or code exists.
