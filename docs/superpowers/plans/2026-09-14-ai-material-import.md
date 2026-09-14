# Russian Structure Lab AI Material Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a copy-to-AI / paste-JSON learning workflow for arbitrary Russian text without requiring an API key.

**Architecture:** Keep the canonical Situation-first Learn intact. Add one standalone `ai-material.html` surface that owns prompt generation, JSON import/validation, local library storage, progressive Russian analysis UI, and TTS; add only one navigation link to `index.html`.

**Tech Stack:** Static HTML/CSS/JavaScript, Web Speech API, Clipboard API, localStorage.

**Spec:** `docs/superpowers/specs/2026-09-14-ai-material-import-design.md`

## Global Constraints
- Preserve input Russian text exactly in `originalText` and sentence `text`.
- No paid or external AI API is required by the app.
- AI uncertainty must remain visible.
- Existing curriculum flow must not be replaced.
- Imported data must pass offset validation before becoming study material.

---

### Task 1: AI Material study surface

**Files:**
- Create: `ai-material.html`

**Interfaces:**
- Consumes: JSON contract from the design spec.
- Produces: `PROMPT`, `validate(data)`, `loadLesson(data)`, Reader/Chunk/Structure/Aspect/Library UI.

- [ ] Create an import modal with Russian source text and generated JSON fields.
- [ ] Implement `copyPrompt` and `copyCombined` using the Clipboard API.
- [ ] Implement JSON cleanup and strict sentence/word/chunk offset validation.
- [ ] Add a valid built-in sample used through the same loader as external JSON.
- [ ] Render sentence words as tappable units with Russian TTS and stress toggle.
- [ ] Add progressive Word Anatomy details: lemma, POS, case/ending, morphology, aspect pair, morphemes, agreement, conjugation, confidence, alternatives, word family.
- [ ] Add Meaning Chunks, Sentence Architecture, and Aspect/Morphology navigation.
- [ ] Save and reopen up to 30 imported materials from localStorage.

### Task 2: Canonical navigation

**Files:**
- Modify: `index.html`

**Interfaces:**
- Produces: navigation entry to `ai-material.html`.

- [ ] Add one `🤖 AI Material` link in the existing top navigation without changing the canonical learning engine.

### Task 3: Verification

**Files:**
- Read-only verification: `ai-material.html`, `index.html`

- [ ] Fetch `ai-material.html` from the feature branch and confirm the prompt, validator, sample, TTS, localStorage library, Chunk, Structure, and Aspect surfaces exist.
- [ ] Fetch `index.html` and confirm `ai-material.html` is linked once.
- [ ] Confirm main-branch canonical Learn remains unchanged until review/merge.
- [ ] Mark real browser/device interaction UNVERIFIED unless actually exercised in a browser.
