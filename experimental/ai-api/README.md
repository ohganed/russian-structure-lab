# Russian Structure Lab — AI API experiment (v0)

**Status: IMPLEMENTED / NOT VERIFIED ON USER'S MAC.** Experimental branch only.
This is a contract-first local API inspired by the UI/API separation in
Digital Agency's 源内. It is **not** an installation of 源内 or an official
government service. No existing HTML pages, lessons, learner history, local
storage or main-branch deployment are modified.

## Scope
- POST /v1/analyze receives JSON: {"originalText": "Я читаю."}.
- A **local** Ollama instance generates the same schemaVersion 1.0 JSON
  consumed by ai-material.html.
- contract.py rejects results that change originalText, reorder/omit
  sentences, misplace word/chunk offsets, change stress-free spelling,
  duplicate IDs, omit lexical tokens, or break word references.
- Response is the lesson JSON directly; it can be pasted into AI Material's
  **Generated JSON** field (no new UI is required for this pilot).
- **Fail closed:** provider problems return an error; invalid lessons never
  report success or enter the user's existing localStorage.
- Authentication: bearer token in environment, loopback bind only, CORS
  disallowed by default. Do **not** embed API tokens in GitHub Pages JavaScript.

## Architecture

    AI Material (existing: paste-and-import JSON)
           ↑ user pastes response after local verification
    local POST /v1/analyze (stdlib Python, 127.0.0.1)
           ↓
    Ollama /api/chat (127.0.0.1:11434)
           ↓
    schemaVersion 1.0 contract checks → lesson JSON or 422

The existing ai-material.html remains the source of truth for rendering and
the v1 prompt shape. The API output contract is intentionally a subset of its
rich material fields; future adapters should reuse the existing reader's
conventions rather than redefine curriculum or AI Material.

## Local smoke test (Mac, Ollama running)
Requirements: Python 3.10+, an installed local Ollama model. No pip packages.

    cd experimental/ai-api
    python3 -m unittest discover -s tests -v
    export RSL_API_TOKEN="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
    export RSL_OLLAMA_MODEL="qwen2.5:3b"
    python3 server.py

In a second terminal, supply the **same token securely** (not from the browser
or a public repository), then:

    curl -sS -X POST http://127.0.0.1:8766/v1/analyze \
      -H 'Content-Type: application/json' \
      -H "Authorization: Bearer $RSL_API_TOKEN" \
      --data '{"originalText":"Я читаю."}'

A 200 response is a JSON lesson. A 422 is not an acceptable lesson: inspect
the detail field, adjust the model/prompt or retry after correction. The target
qwen2.5:3b may fail complex multi-sentence analyses; passing structural
validation alone does **not** establish Russian linguistic accuracy.

## Security / operational limits
- No user input or generated lesson is saved on the server by this prototype.
- Only local HTTP, no remote bind and no browser CORS by default.
- Do not expose Ollama or this API to the Internet without a separately
  designed authentication proxy, rate limits, TLS, logging policy and abuse
  controls.
- Avoid uploading student data, personal information or confidential texts.
- Browser-to-loopback from GitHub Pages is **not** the supported deployment
  path. Modern browser private-network/CORS rules and token handling make it
  unsuitable as a drop-in iPhone solution.
- API response is not yet integrated into ai-material.html; copying JSON is
  deliberately retained as a safe fallback.
- Generated morphology, aspect, case, etymology and stress still require an
  independent Educational Validity Gate (EVG).
- Original indexes use JavaScript UTF-16 units, not Python code points.

## Evidence / next gate
- Source code and tests added to an experimental PR only.
- GitHub CI may run unit tests when the PR is opened.
- Before merging: verify CI, Mac + actual Ollama, several sentences including
  ё/combining accents, iPhone access architecture, accessibility, credentials,
  and the existing EVIDENCE_GATE.md curriculum requirements.
- Do not change PROJECT_CARD.md or declare an EVG PASS from this experiment.


## Mac-only UI pilot (new, separate from public Pages)

**Mac and Ollama only.** The experimental PR holds a Mac-local analysis
screen; the main branch and its GitHub Pages UI remain untouched.

Start from the repository root after switching to the experiment branch:

    python3 experimental/ai-api/start_mac.py

Requirements: macOS, Python 3.10+, Ollama running on this Mac, with
the requested model installed. Default model is qwen2.5:3b.
Use RSL_OLLAMA_MODEL if you have installed another model, e.g.:

    RSL_OLLAMA_MODEL=gemma3:4b python3 experimental/ai-api/start_mac.py

The launcher:
1. Checks the local Ollama service and installed model.
2. Creates a random **in-memory-only, per-run** bearer token.
3. Serves the screen at http://127.0.0.1:8766/pilot and opens it on Mac.
4. Accepts JSON analysis requests only on loopback with a valid token.
5. Stops with Control+C in Terminal. No Mac/iPhone cross-device access.

On screen: enter text → MacのOllamaで解析 → review preview →
JSONをコピー → open existing AI Material and paste into Generated JSON.
Nothing is automatically imported into the existing learner database.
ChatGPT remains available via the existing manual AI Material prompt flow.

**Security details:** The HTML is stored in a .template resource, not a
direct GitHub Pages .html entry point. The local server injects the ephemeral
bearer token into the page served **only** from 127.0.0.1, not into URLs, git,
localStorage or the clipboard. It enforces Host and Origin restrictions, CSP,
no-store, no-referrer and fail-closed JSON validation. A static browser page
(including the public GitHub Pages deployment) cannot call the API using a
hard-coded credential. Never port-forward or expose port 8766 on a network.

**Verification boundary:** HTTP security and contract unit tests in GitHub
Actions do not confirm that the user's Mac, Ollama model or Russian-language
analysis passes. The schema/position checks do not judge grammar correctness.
Do not describe the experimental PR as a production release until user-device
and Educational Validity Gate checks pass.


## Troubleshooting: AI provider unavailable (502)

The local /pilot screen and /health returning HTTP 200 means the pilot server
is running. A 502 from POST /v1/analyze is a model/provider stage failure,
not proof the Mac UI is broken. The old pilot reported every failure as the
same "AI provider unavailable" string. This branch now adds:
- timeout → Ollama did not respond within RSL_OLLAMA_TIMEOUT (default 240s).
- ollama_http → Ollama returned HTTP status 4xx/5xx. The exact status is shown.
- connection → Ollama could not be reached or the connection was interrupted.
- bad_response → Ollama returned an unexpected message format.
- unexpected → unexpected internal/provider failure.

The terminal prints only error class, elapsed time, and input length. It
deliberately does NOT log the Russian source text or generated lesson.

After pulling new commits: Stop the old server with Control+C, then run:

    cd ~/Downloads/russian-structure-lab-ollama-pilot
    git pull --ff-only origin experiment/ai-api-v0
    python3 experimental/ai-api/start_mac.py

First test the short sentence: Я читаю книгу.
For a 10-sentence news article, try one or two sentences at a time. A small
3B model producing high-detail structured JSON for ten sentences can be slow
or exceed its practical generation capacity. If the model is slow even with
short sentences, you may configure a longer maximum wait time:

    RSL_OLLAMA_TIMEOUT=360 python3 experimental/ai-api/start_mac.py

Allowable range is 30..600 seconds. A longer timeout does NOT guarantee
correct grammar or syntactically valid JSON. HTTP 422 means an AI output was
rejected by the contract validator, not that Ollama is inaccessible.
Do not blindly save invalid JSON; the UI should continue to show an error.


## Fix: surface offset mismatch (example: читаю)

For a source such as Я читаю книгу., the correct JS slice offsets are:
Я [0,1), читаю [2,7), книгу [8,13). A small LLM may return wrong
start/end positions even when it analyzes the text correctly.

The API now asks Ollama **not** to count positions. alignment.py derives
word and chunk offsets deterministically from the **exact** sentence.text
using UTF-16 indexing, and then runs the original strict validator.
Exact original text, source order, accents, word spelling and cross-references
are never silently changed. Unknown, missing or ambiguous text is still
rejected rather than fabricated; grammar accuracy remains a separate review.

After this change run:

    cd ~/Downloads/russian-structure-lab-ollama-pilot
    git pull --ff-only origin experiment/ai-api-v0
    python3 experimental/ai-api/start_mac.py

Stop the currently running local server using Control+C first.
Retest Я читаю книгу. If that passes, try the longer news text 1–2
sentences at a time to assess latency and substantive analysis quality.


## Fix: structure has unknown word ref

Ollama sometimes invents references such as S1.node.refIds=["word1"]
while the actual sentence.words[].id values are ["w1","w2",...].
The Mac pilot now safely reconstructs unknown structure refIds from
node.text only when that literal substring identifies the intended
source words unambiguously. Existing correct references are preserved;
ambiguous repeated text, modified wording, missing node text and
unresolvable references are still rejected.

The system prompt also requires the model to cite existing exact word
IDs in every structure tree node. This is a structural repair only,
not evidence that a grammar analysis is linguistically correct.

The AI Radio application, if running on port 4180, is a separate process;
updating or restarting this pilot on port 8766 must not affect it.

## Russian linguistic quality: expert prompt v1.1 (7B comparison)

The existing public `ai-material.html` has a detailed Japanese JSON prompt v1.0.
The early Mac-only API used a separate, *much shorter* prompt focused on JSON
structure, and did not carry over explicit Russian case/infinitive/aspect/ending
instructions. This likely contributed to substantive errors such as
`книгу` incorrectly tagged "possessive" and `читаю` with lemma `читаю`.

The experimental Mac pilot now uses a **revised linguistic v1.1 prompt**
in `server.py`, drawing on the existing v1.0 teaching requirements:
Russian case names, real lemma, verbal aspect, person and tense,
Russian endings, bilingual grammar reasoning, stress, and cautious
confidence. It retains exact-source/no-invented-IDs constraints and the
deterministic offset/structure validation already in place.

**Comparison protocol:** finish any already-running 7B test with the old
prompt first, and save that JSON as the baseline. Pushing a GitHub update
does not change a Python server process already running on the Mac.
To test the new prompt, stop only that Mac pilot and run:

    cd ~/Downloads/russian-structure-lab-ollama-pilot
    git pull --ff-only origin experiment/ai-api-v0
    RSL_OLLAMA_MODEL=qwen2.5:7b RSL_PORT=8768 python3 experimental/ai-api/start_mac.py

Compare identical input and model before/after the update. Passing JSON
validation **does not** prove grammatical accuracy; review specific gold
analyses of lemma, case, aspect, accent and explanations.
