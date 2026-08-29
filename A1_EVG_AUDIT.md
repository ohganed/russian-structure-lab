# A1 Educational Validity Gate Audit

Scope: `materials-a1-calibration.js` — 50 sentences, 10 categories × 5.

Gate dimensions:
- Russian naturalness
- CEFR A1 fit
- pedagogical framing
- case labeling
- verb aspect
- morphology
- duplicate / near-duplicate risk
- 🇯🇵 Japanese pathway quality
- 🇬🇧 English pathway quality

## Overall result
**🟡 PARTIAL PASS — audit completed, corrections required before Step 4 can be marked PASS.**

The set is broadly usable as an A1 calibration corpus, but several entries need either correction or explicit pedagogical notes. No sentence should be expanded into the 500-sentence production corpus until the revisions below are resolved.

## Required revisions
| ID | Finding | Required action |
|---|---|---|
| A1-PR-002 | 🇯🇵 `兄弟` is broader/less precise than EN `brother` and RU `брат`. | Change JP to `これは私の兄／弟です。` or equivalent note that Russian does not encode older/younger here. |
| A1-PR-004 | 🇯🇵 `姉妹` is broader/less precise than RU `сестра`. | Change JP to `私には姉／妹がいます。` or equivalent note. |
| A1-TM-005 | 🧬 `приехал` decomposition `при- + ех + -ал` is too coarse and may imply `-ал` is one simple ending. | Prefer curated decomposition such as `при- + ех + -а- + -л` with an uncertainty/analysis note if shown to beginners. |
| A1-SI-004 | 🇯🇵 `インターネットが動きません` is unnatural Japanese. | Prefer `今日はインターネットが使えません。` or `今日はインターネットがつながりません。` depending intended nuance. |
| A1-CE-005 | 🇷🇺 `Мы идём в музей сегодня.` is possible but less neutral than the default A1 information order. | Prefer `Сегодня мы идём в музей.` for calibration unless marked as contrastive/focus word order. |

## Pedagogical-note required
These are not necessarily linguistically wrong, but the label alone can mislead an A1 learner.

| ID | Finding | Pedagogical note needed |
|---|---|---|
| A1-DL-004 | `Вечером` is an instrumental-form temporal expression. | Teach as a time expression first; case depth should be optional. |
| A1-PR-001 | `Меня` is syncretic genitive/accusative in form; syntax here is accusative. | Distinguish form ambiguity from sentence function. |
| A1-PR-005 | `в кафе` uses an indeclinable noun, so the prepositional relationship is not visible in the noun ending. | Explain construction without implying an observable case ending. |
| A1-FS-001 | `утром` is an instrumental-form temporal expression. | Teach as a high-frequency time chunk before abstract case explanation. |
| A1-BE-001 | `Я устал.` is masculine speaker agreement. | Mark masculine; provide `Я устала.` as the feminine counterpart in deeper view. |
| A1-NE-003 | `Зимой` is an instrumental-form temporal expression. | Teach as a lexicalized/high-frequency time pattern first. |
| A1-NE-004 | `в саду` is the special locative/prepositional form in `-у`. | Avoid presenting it as a fully regular prepositional ending pattern. |
| A1-SI-001 | `утром` again uses temporal instrumental. | Same framing rule as A1-FS-001. |
| A1-TO-001 | `Я думаю, что это хорошо.` contains a `что` subordinate clause and is borderline for strict A1 grammar sequencing. | If retained at A1, teach the whole `Я думаю, что ...` expression as a reusable chunk and defer clause theory. |

## Sentence-by-sentence gate status
Legend: ✅ PASS · 🟨 PASS WITH NOTE · 🔧 REVISE

### 🏠 Daily Life
- A1-DL-001 ✅
- A1-DL-002 ✅
- A1-DL-003 ✅
- A1-DL-004 🟨 temporal instrumental framing
- A1-DL-005 ✅

### 👥 People & Relationships
- A1-PR-001 🟨 syncretic form/function note
- A1-PR-002 🔧 JP precision
- A1-PR-003 ✅
- A1-PR-004 🔧 JP precision
- A1-PR-005 🟨 indeclinable `кафе`

### 💼 Work & Study
- A1-WS-001 ✅
- A1-WS-002 ✅
- A1-WS-003 ✅
- A1-WS-004 ✅
- A1-WS-005 ✅

### 🚆 Travel & Movement
- A1-TM-001 ✅
- A1-TM-002 ✅
- A1-TM-003 ✅
- A1-TM-004 ✅
- A1-TM-005 🔧 morphology decomposition

### 🍽️ Food & Shopping
- A1-FS-001 🟨 temporal instrumental framing
- A1-FS-002 ✅
- A1-FS-003 ✅
- A1-FS-004 ✅
- A1-FS-005 ✅ — natural elliptical restaurant request; treat as a situation chunk

### ❤️ Body & Emotion
- A1-BE-001 🟨 gender agreement note
- A1-BE-002 ✅
- A1-BE-003 ✅
- A1-BE-004 ✅
- A1-BE-005 ✅

### 🌦️ Nature & Environment
- A1-NE-001 ✅
- A1-NE-002 ✅
- A1-NE-003 🟨 temporal instrumental framing
- A1-NE-004 🟨 special locative form
- A1-NE-005 ✅

### 📰 Society & Information
- A1-SI-001 🟨 temporal instrumental framing
- A1-SI-002 ✅
- A1-SI-003 ✅
- A1-SI-004 🔧 JP naturalness
- A1-SI-005 ✅

### 🧠 Thought & Opinion
- A1-TO-001 🟨 CEFR sequencing / teach as chunk
- A1-TO-002 ✅
- A1-TO-003 ✅
- A1-TO-004 ✅
- A1-TO-005 ✅

### 🎭 Culture & Expression
- A1-CE-001 ✅
- A1-CE-002 ✅
- A1-CE-003 ✅
- A1-CE-004 ✅
- A1-CE-005 🔧 neutral word order for calibration

## Duplicate / coverage review
- Exact sentence duplicates: none observed in the 50-sentence calibration set.
- Category balance: PASS — 10 categories × 5 sentences.
- Controlled repetition exists in useful patterns (`У меня ...`, `Мне ...`, time expressions, motion verbs), but production expansion should track near-duplicate templates automatically.

## 🇯🇵 / 🇬🇧 pathway review
- Both fields exist for all 50 calibration entries.
- They are currently mostly short translations rather than fully distinct pedagogical pathways.
- Gate requirement for production corpus: 🇯🇵 explanations should exploit Japanese particles/structure where useful; 🇬🇧 explanations should exploit preposition/word-order/aspect comparisons where useful.

## Step 4 completion condition
Step 4 becomes **PASS** only after:
1. the 5 required revisions are applied to canonical data;
2. the note-required entries carry explicit pedagogical metadata or equivalent UI treatment;
3. the corrected 50 are re-audited;
4. automated validation in Step 5 can consume the review state.
