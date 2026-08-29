# Step 3 Browser Verification Checklist

This file is repository evidence for the canonical Learn migration. It separates implementation from device verification.

## Canonical surface
`index.html`

## Preserved fallback
`legacy-index.html`

## Verification cases
- [ ] A1 opens and displays calibration material.
- [ ] A1 category filter changes the active material set without console/runtime errors.
- [ ] A2 opens and clearly displays 0 / 500 rather than failing silently.
- [ ] B1 opens and clearly displays 0 / 500 rather than failing silently.
- [ ] B2 opens and clearly displays 0 / 500 rather than failing silently.
- [ ] C1 opens and clearly displays 0 / 500 rather than failing silently.
- [ ] C2 opens and clearly displays 0 / 500 rather than failing silently.
- [ ] Returning from an empty level to A1 resets the material index safely.
- [ ] Legacy selector exposes existing legacy materials as `UNCLASSIFIED`.
- [ ] No legacy item is presented as A1–C2 without explicit classification evidence.
- [ ] Word tap triggers Russian TTS where browser speech synthesis is available.
- [ ] Sentence tap triggers Russian TTS where browser speech synthesis is available.
- [ ] Mobile layout remains usable on iPhone Safari.

## Gate status
**IMPLEMENTED / NOT VERIFIED** until the checks above are performed in the deployed app.
