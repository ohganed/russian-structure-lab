# Russian Structure Lab — AI Material Import Design

## Goal
Add a safe, copy-based AI analysis workflow for arbitrary Russian text, modeled on Arabic Structure Lab, so analyzed JSON can be imported and studied as structured material without requiring an API key.

## User flow
1. Open **AI Material** from Russian Structure Lab.
2. Paste Russian text.
3. Copy either the analysis prompt alone or the prompt with the text embedded.
4. Run the prompt in ChatGPT or another capable AI.
5. Copy the returned JSON.
6. Paste JSON into Russian Structure Lab and load it.
7. Study the material through Reader, Word Anatomy, Meaning Chunks, Sentence Architecture, Aspect/Morphology, audio, and saved Library.

## Product principles
- Original Russian text is preserved exactly.
- The reading surface remains calm; analysis appears progressively.
- Russian-specific structure is first-class: stress, lemma, case, endings, agreement, verb aspect, conjugation, reflexivity, prefixes/suffixes, and word families.
- Meaning-order glosses and natural translations remain separate.
- AI uncertainty is visible through field-level confidence and alternative analysis.
- No external AI API is required. The app only copies a prompt and imports JSON.
- Existing curriculum and Situation-first Learn remain unchanged.

## Architecture
Implement the feature as a standalone `ai-material.html` page. It owns prompt generation, JSON validation/normalization, rendering, TTS, and localStorage-backed material library. The canonical `index.html` only receives a navigation link, minimizing regression risk.

## JSON contract
Top-level fields: `schemaVersion`, `language`, `title`, `originalText`, `sentences`.

Each sentence should support: `id`, `text`, `stressedText`, `ttsText`, `overallMeaning`, `words`, `chunks`, `structure`, `grammarNotes`, `alternativeAnalysis`.

Each word should support: `id`, `surface`, `stressed`, `start`, `end`, `meaning`, `lemma`, `partOfSpeech`, `morphemes`, `morphology`, `grammar`, `case`, `ending`, `agreement`, `aspect`, `aspectPair`, `conjugation`, `wordFamily`, `relations`, `confidence`, `alternativeAnalysis`.

Chunks should support Russian-order meaning and natural meaning separately and link back to word IDs. Structure nodes link to word IDs so selecting structure can highlight text.

## UI
- Header: back to Learn, title, `＋ 教材`.
- Reader: one sentence at a time, tappable Russian words, sentence audio, stress toggle, overall meaning.
- Bottom navigation: `本文`, `Chunk`, `Structure`, `Aspect`, `教材`.
- Word sheet: surface/stressed form, meaning, lemma, POS, case/ending, aspect pair, expandable morphology and word family.
- Import modal: Russian text, prompt-copy controls, generated JSON area, load button, sample.
- Library: up to 30 locally saved AI materials.

## Validation
Reject non-object JSON, missing sentences, sentence text that cannot map word/chunk offsets, and non-Russian language markers when present. Strip Markdown code fences around JSON on import. Do not silently rewrite source text.

## Verification
- Static fetch confirms page and nav link exist.
- Prompt includes required Russian analysis fields and JSON-only instruction.
- Sample JSON loads by the same validator used for imports.
- Offset checks pass for sample words/chunks.
- Existing canonical Learn file remains otherwise unchanged.
- Real browser/device behavior remains UNVERIFIED until opened in a browser.
