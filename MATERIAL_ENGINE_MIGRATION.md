# Material Engine Migration

## Goal
Unify the legacy corpus and CEFR curriculum corpus without deleting or silently reclassifying existing material.

## Canonical runtime interface
`material-engine.js` exposes `window.RSL_MATERIAL_ENGINE`.

The engine normalizes two currently supported source shapes:

1. `window.RSL_MATERIALS` — legacy array-based records from `materials.js`.
2. `window.RSL_A1_CALIBRATION` — object-based CEFR records from `materials-a1-calibration.js`.

## Safety rule
Legacy items are normalized with:

```text
level: UNCLASSIFIED
verification: NOT VERIFIED
```

They are **not** automatically assigned to A1–C2. CEFR classification is an educational decision and must be made through the curriculum migration/EVG process.

## Canonical normalized fields
- `id`
- `level`
- `category`
- `subCategory`
- `context`
- `ru`
- `jp`
- `en`
- `scene`
- `sound`
- `words`
- `chunks`
- `architecture`
- `caseFocus`
- `aspectFocus`
- `anatomyFocus`
- `grammarFocus`
- `register`
- `source`
- `sourceShape`
- `verification`

## Public engine operations
- `getAll()`
- `getByLevel(level)`
- `getByCategory(level, category)`
- `getById(id)`
- `stats()`
- `normalizeLegacy(row)`
- `normalizeModern(item)`

## Migration sequence
1. Keep `materials.js` intact.
2. Keep CEFR calibration files intact.
3. Load source datasets before `material-engine.js`.
4. Move consumers to `RSL_MATERIAL_ENGINE` one at a time.
5. Verify behavior after each consumer migration.
6. Only after all legacy items are intentionally classified and verified should the old array schema be considered for retirement.

## Current state
- Canonical compatibility engine: **IMPLEMENTED / NOT VERIFIED**.
- Legacy corpus deletion: **not performed**.
- Automatic CEFR guessing: **not performed**.
- Main Learn UI migration: **pending Step 3 after engine verification**.
