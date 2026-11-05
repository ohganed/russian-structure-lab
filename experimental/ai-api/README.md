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
