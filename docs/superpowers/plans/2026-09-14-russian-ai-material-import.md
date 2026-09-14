# Russian AI Material Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Russian AI-material workflow that lets the user copy a built-in analysis prompt, analyze Russian text externally, paste the returned JSON, validate it, save it locally, and study it through Reader, Words, Meaning Chunks, Sentence Architecture, Audio, Aspect, and Morphology views.

**Architecture:** Preserve the canonical Situation-first curriculum in `index.html`. Extend the existing `my-material.html` concept into a dedicated AI-import reading surface, while extracting the Russian prompt and import/validation logic into focused JavaScript files. Imported AI material uses its own localStorage namespace and never enters CEFR curriculum data.

**Tech Stack:** Static HTML/CSS/JavaScript, browser `localStorage`, Web Speech API (`ru-RU`), GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-14-russian-ai-material-import-design.md`

## Global Constraints

- No paid/external AI API is required by the app.
- Preserve existing A1–C2, Legacy, Material Engine, and Aspect Lab behavior.
- Imported AI material is separate from CEFR-certified curriculum data.
- `originalText` and every `sentence.text` must remain unchanged by analysis metadata.
- Uncertain morphology/aspect/syntax must be displayed as uncertain rather than invented.
- Japanese and English explanations remain available as separate learning aids.
- Russian audio uses browser `ru-RU` TTS when available, but TTS failure must not block study.
- Use PASS / FAIL / UNVERIFIED / IMPLEMENTED-NOT-VERIFIED reporting.

---

### Task 1: Russian AI Prompt Module

**Files:**
- Create: `ai-material-prompt.js`
- Create: `tests/ai-material-prompt.test.mjs`

**Interfaces:**
- Produces: `window.RSL_AI_PROMPT.buildPrompt(text)` returning one complete prompt string.
- Produces: `window.RSL_AI_PROMPT.template` for copying the prompt without text.
- Produces: `window.RSL_AI_PROMPT.schemaVersion === "1.0"`.

- [ ] **Step 1: Write the failing prompt contract test**

Create a Node test that loads `ai-material-prompt.js` in a VM-like browser shim and asserts that the generated prompt contains all of these requirements: JSON-only output, `language:"ru"`, original-text preservation, offsets, stress in separate fields, case/gender/number, adjective agreement, verb aspect/aspectPair, conjugation, morphemes, chunks, sentence architecture, field-level confidence, uncertainty/alternative analysis, Japanese + English explanations, and `{{RUSSIAN_TEXT}}` replacement.

- [ ] **Step 2: Run the test and verify failure**

Run:

```bash
node --test tests/ai-material-prompt.test.mjs
```

Expected: FAIL because `ai-material-prompt.js` does not yet exist.

- [ ] **Step 3: Implement `ai-material-prompt.js`**

Expose a browser global:

```js
window.RSL_AI_PROMPT = {
  schemaVersion: '1.0',
  template: '...',
  buildPrompt(text) {
    return this.template.replace('{{RUSSIAN_TEXT}}', String(text ?? '').trim());
  }
};
```

The prompt must explicitly require this analysis order:

```text
1) Word Anatomy
2) Meaning Chunks
3) Sentence Architecture
```

It must require exact substring-compatible `start`/`end` offsets and must prohibit invented aspect pairs, declension classes, conjugation classes, morphemes, or etymology.

- [ ] **Step 4: Run the prompt test**

Run:

```bash
node --test tests/ai-material-prompt.test.mjs
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add ai-material-prompt.js tests/ai-material-prompt.test.mjs
git commit -m "feat: add Russian AI material prompt"
```

---

### Task 2: JSON Validation and Normalization

**Files:**
- Create: `ai-material-engine.js`
- Create: `tests/ai-material-engine.test.mjs`

**Interfaces:**
- Produces: `window.RSL_AI_MATERIAL_ENGINE.cleanJson(raw)`.
- Produces: `window.RSL_AI_MATERIAL_ENGINE.validate(data)` returning `{ ok: true, data }` or throwing an `Error` with a useful location message.
- Produces: `window.RSL_AI_MATERIAL_ENGINE.saveLesson(data)`.
- Produces: `window.RSL_AI_MATERIAL_ENGINE.listLessons()`.
- Produces: `window.RSL_AI_MATERIAL_ENGINE.deleteLesson(key)`.
- Storage key: `russianStructureLab.aiLibrary.v1`.

- [ ] **Step 1: Write failing validation tests**

Cover at minimum:

```js
// valid Russian lesson passes
// invalid JSON fences are cleaned before parsing
// language other than ru fails
// empty sentences fails
// word offset mismatch fails with sentence + word identification
// chunk offset mismatch fails with sentence + chunk identification
// duplicate IDs inside one sentence fail
// broken chunk.wordIds fail
// unsupported schemaVersion fails
// optional fields may be absent
// save/list preserves lesson across storage reload simulation
```

- [ ] **Step 2: Run tests and verify failure**

```bash
node --test tests/ai-material-engine.test.mjs
```

Expected: FAIL because engine does not yet exist.

- [ ] **Step 3: Implement clean/validate/storage functions**

Validation must accept progressive/incomplete optional analysis but reject structural corruption. Error messages must include identifiers such as:

```text
Sentence s2 / word w4: offset mismatch for "книгу"
```

Use a 50-item library cap, newest first, deduplicated by `originalText` when available.

- [ ] **Step 4: Run tests**

```bash
node --test tests/ai-material-engine.test.mjs
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add ai-material-engine.js tests/ai-material-engine.test.mjs
git commit -m "feat: validate and store AI Russian materials"
```

---

### Task 3: AI Material Import and Reader Surface

**Files:**
- Modify: `my-material.html`
- Consume: `ai-material-prompt.js`
- Consume: `ai-material-engine.js`

**Interfaces:**
- Consumes `RSL_AI_PROMPT.buildPrompt(text)`.
- Consumes `RSL_AI_MATERIAL_ENGINE.cleanJson/validate/saveLesson/listLessons/deleteLesson`.
- Produces a study surface with tabs/actions: `Text`, `Chunks`, `Structure`, `Library`.

- [ ] **Step 1: Add an import panel without removing existing reading behavior**

The panel must contain:

```text
1 · Russian text
[textarea]
[Copy analysis prompt] [Copy text + prompt]

2 · Generated JSON
[textarea]
[Load analysis]
```

Do not call any external API from the page.

- [ ] **Step 2: Wire prompt-copy actions**

`Copy analysis prompt` copies `RSL_AI_PROMPT.template`.

`Copy text + prompt` copies `RSL_AI_PROMPT.buildPrompt(sourceText)`.

Both actions show a short in-app status message after `navigator.clipboard.writeText()` succeeds or fails.

- [ ] **Step 3: Wire JSON import**

On `Load analysis`:

```js
const cleaned = RSL_AI_MATERIAL_ENGINE.cleanJson(raw);
const parsed = JSON.parse(cleaned);
const { data } = RSL_AI_MATERIAL_ENGINE.validate(parsed);
RSL_AI_MATERIAL_ENGINE.saveLesson(data);
openLesson(data);
```

No invalid material may be stored.

- [ ] **Step 4: Render the source text as the primary surface**

For each sentence, render untouched `sentence.text`. Replace only ranges covered by word offsets with tappable spans while preserving punctuation and spacing exactly.

Tapping a word must play Russian TTS and open its detail panel.

- [ ] **Step 5: Implement progressive word disclosure**

Default view:

```text
surface / stressed
meaning ja + en
lemma
part of speech
```

Expanded view:

```text
case / gender / number / animacy
ending / stem / agreement
morphemes
conjugation or declension
aspect
syntactic role
```

Deep view:

```text
aspect pair
word family
confidence by field
alternative analysis
```

Missing optional fields render as absent, never as fabricated values.

- [ ] **Step 6: Implement Meaning Chunks view**

Show each chunk's Russian text/stress, Russian-order meaning, natural meaning, and function. Selecting a chunk highlights its `wordIds` in the reader.

- [ ] **Step 7: Implement Sentence Architecture view**

Render `structure.tree` recursively. Selecting a node highlights `refIds` in the reader. Labels prefer Japanese, then English, then Russian/type.

- [ ] **Step 8: Implement Library view**

List saved AI materials from `russianStructureLab.aiLibrary.v1` with title/date/open/delete. Clearly label the collection `AI Material · not CEFR certified`.

- [ ] **Step 9: Preserve mobile usability**

At <=720px, the reader and analysis panel must remain reachable without horizontal overflow. Reuse the current Text/Dive mobile navigation pattern rather than adding a new layout system.

- [ ] **Step 10: Commit**

```bash
git add my-material.html
git commit -m "feat: add AI material import reader"
```

---

### Task 4: Navigation Integration

**Files:**
- Modify: `index.html`
- Modify: `README.md`

**Interfaces:**
- `index.html` links to the AI import reader without changing curriculum state/data.

- [ ] **Step 1: Add one clear navigation entry**

Change the existing My Material navigation wording to make the new purpose obvious, for example:

```text
🪆 AI Material
```

Keep the target as `my-material.html`.

- [ ] **Step 2: Document the workflow in README**

Add a concise section:

```text
Russian text → copy built-in prompt → analyze externally → paste JSON → validate → save → study
```

State explicitly that imported material is local and is not CEFR-certified curriculum.

- [ ] **Step 3: Commit**

```bash
git add index.html README.md
git commit -m "docs: expose AI material workflow"
```

---

### Task 5: Automated Regression Checks

**Files:**
- Create: `tests/ai-material-page.test.mjs`
- Optionally modify: `package.json` only if one already exists and adding a test script does not change the deployment model.

**Interfaces:**
- Tests static integration contracts without requiring network access.

- [ ] **Step 1: Add static integration tests**

Assert that `my-material.html` includes:

```text
ai-material-prompt.js
ai-material-engine.js
Copy analysis prompt
Copy text + prompt
Generated JSON
Load analysis
Meaning Chunks
Sentence Architecture
AI Material · not CEFR certified
```

Assert that `index.html` still contains curriculum scripts:

```text
curriculum.js
materials.js
materials-a1-calibration.js
material-engine.js
```

and still links `aspect-lab.html`, `level-browser.html`, and `legacy-index.html`.

- [ ] **Step 2: Run all Node tests**

```bash
node --test tests/*.test.mjs
```

Expected: all PASS.

- [ ] **Step 3: Commit**

```bash
git add tests/ai-material-page.test.mjs package.json
git commit -m "test: cover AI material integration"
```

---

### Task 6: Browser Verification and Repair

**Files:**
- Create or update: `AI_MATERIAL_VERIFICATION.md`
- Modify implementation files only if verification exposes defects.

**Interfaces:**
- Produces repository evidence for PASS / FAIL / UNVERIFIED.

- [ ] **Step 1: Serve the GitHub Pages-compatible app locally**

Use the project's existing static-server method. If none exists, use:

```bash
python3 -m http.server 8000
```

- [ ] **Step 2: Verify canonical curriculum regression**

In a real browser confirm:

```text
index.html loads
A1 opens
A2–C2 selection still works
Legacy still works
Aspect Lab link still works
AI Material link opens my-material.html
```

- [ ] **Step 3: Verify prompt workflow**

Paste a short Russian sample such as:

```text
Я боялся, что опоздаю.
```

Confirm both copy buttons produce non-empty Russian-specific prompts and the combined prompt includes the text exactly.

- [ ] **Step 4: Verify valid JSON import**

Use a hand-checked fixture conforming to schema 1.0. Confirm it loads, saves, survives reload, and reopens from Library.

- [ ] **Step 5: Verify learning interactions**

Confirm:

```text
word tap highlights/opens detail
Russian TTS attempts playback
expanded/deep analysis opens
chunk selection highlights source words
structure-node selection highlights source words
aspect/confidence/alternative analysis render when present
```

- [ ] **Step 6: Verify rejection behavior**

Confirm useful errors for malformed JSON, wrong language, word offset mismatch, chunk offset mismatch, duplicate IDs, and broken references.

- [ ] **Step 7: Verify mobile layout**

At a narrow viewport confirm Text/Dive navigation remains usable, import fields fit the screen, and no essential control is clipped.

- [ ] **Step 8: Repair any discovered defects and rerun automated tests**

```bash
node --test tests/*.test.mjs
```

Expected: PASS after fixes.

- [ ] **Step 9: Record evidence**

`AI_MATERIAL_VERIFICATION.md` must list each acceptance criterion with `PASS`, `FAIL`, or `UNVERIFIED` and concrete evidence.

- [ ] **Step 10: Final commit**

```bash
git add AI_MATERIAL_VERIFICATION.md my-material.html ai-material-prompt.js ai-material-engine.js tests
git commit -m "verify: AI Russian material workflow"
```

---

## Plan Self-Review

- Spec coverage: prompt, external AI workflow, JSON validation, local storage, reader, chunks, architecture, audio, confidence, uncertainty, CEFR separation, mobile behavior, and browser verification are all mapped to tasks.
- Placeholder scan: no TBD/TODO/"implement later" instructions remain.
- Interface consistency: prompt globals and engine globals are defined once in Tasks 1–2 and consumed consistently in Task 3.
- Scope control: direct API calls, cloud sync, CEFR auto-classification, spaced repetition, grading, and server-side storage remain out of scope.
