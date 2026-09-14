# Russian Structure Lab — AI Material Verification

Date: 2026-09-14
Branch: `feature/ai-material-import`

## Evidence summary

### PASS — local executable checks

A local Node test harness was run against the prompt/engine implementation and an equivalent AI-material page contract.

Command:

```bash
node --test /tmp/rsl-ai/tests/*.test.mjs
```

Fresh result:

```text
5 tests
5 pass
0 fail
```

Covered:

- Russian AI prompt contract contains JSON-only, Russian language, offset, morphology, aspect, chunk, structure, confidence, and alternative-analysis requirements.
- Prompt inserts supplied Russian text.
- JSON engine accepts a valid Russian lesson.
- JSON engine rejects an offset mismatch.
- Local-storage save/list roundtrip works in the test shim.
- Markdown JSON fences are cleaned.
- AI material page contract includes prompt-copy, text+prompt copy, generated JSON import, Meaning Chunks, Sentence Architecture, TTS, and progressive analysis controls.

### PASS — repository evidence

The feature branch contains:

- `ai-material-prompt.js`
- `ai-material-engine.js`
- `ai-material.html`
- `ai-material-sample.json`
- design spec and implementation plan
- README documentation for the AI Material workflow

`ai-material.html` visibly includes:

- `Copy analysis prompt`
- `Copy text + prompt`
- `Generated JSON`
- `Load analysis`
- `Meaning Chunks`
- `Sentence Architecture`
- `AI Material · not CEFR certified`
- Russian TTS language `ru-RU`
- progressive `Case / Aspect / Morphology` disclosure

The engine uses the isolated storage namespace:

```text
russianStructureLab.aiLibrary.v1
```

and validates schema version, language, sentence presence, word/chunk offsets, duplicate IDs, chunk word references, and structure refs.

## Acceptance criteria

| Criterion | State | Evidence |
|---|---|---|
| Existing canonical curriculum remains untouched on feature branch | PASS | New AI files are isolated; no curriculum data files changed |
| AI Material import UI exists | PASS | `ai-material.html` |
| Paste Russian source text | PASS | `#sourceText` UI present |
| Copy analysis prompt | PASS | prompt module + button contract |
| Copy text + prompt | PASS | `buildPrompt(text)` + button contract |
| Paste generated JSON | PASS | `#jsonInput` UI present |
| Validate imported JSON | PASS | local engine tests |
| Save/reopen local lesson | PASS for engine | localStorage shim test; real browser persistence UNVERIFIED |
| Word progressive analysis | IMPLEMENTED / NOT VERIFIED | repository UI evidence; browser interaction not run |
| Meaning Chunks interaction | IMPLEMENTED / NOT VERIFIED | repository UI evidence; browser interaction not run |
| Sentence Architecture interaction | IMPLEMENTED / NOT VERIFIED | repository UI evidence; browser interaction not run |
| Russian browser TTS | IMPLEMENTED / NOT VERIFIED | `ru-RU` code present; target browser/voice not run |
| Invalid JSON/offset errors | PASS for engine | local executable tests include mismatch rejection |
| CEFR separation | PASS | separate page + storage namespace + UI label |
| Mobile layout | IMPLEMENTED / NOT VERIFIED | responsive CSS present; device/browser not run |
| Canonical navigation includes AI Material entry | UNVERIFIED / NOT IMPLEMENTED | README documents the surface; canonical `index.html` navigation was intentionally not rewritten in this environment |
| Real GitHub Pages/browser verification | UNVERIFIED | current environment cannot clone/serve the GitHub repository due network/DNS restriction |

## Known limitation

The current feature is reachable as `ai-material.html` on the feature branch, but the canonical `index.html` navigation has not yet been modified. The existing canonical index is a very large single-file surface; rewriting it through the current connector without a real checkout would create unnecessary regression risk. Navigation integration should be the first small follow-up once the branch is available in a normal Git workspace or browser-capable development environment.

## Current result

**IMPLEMENTED / NOT FULLY VERIFIED**

The prompt, validator/storage engine, AI reading surface, sample fixture, and documentation exist with local executable coverage. Browser behavior, persistence in a real browser, TTS availability, mobile interaction, and canonical navigation integration remain to be verified before this feature may be called complete.
