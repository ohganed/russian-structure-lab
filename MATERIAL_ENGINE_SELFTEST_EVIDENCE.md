# Material Engine Self-Test Evidence

The browser self-test page is `material-engine-selftest.html`.

Expected assertions:
1. Material Engine loads.
2. Legacy material rows normalize to canonical objects.
3. A1 calibration objects normalize through the same engine.
4. Legacy items remain `UNCLASSIFIED`.
5. `getByLevel('A1')` returns the A1 calibration set.
6. `getByLevel('B1')` returns an empty array until B1 data is added.
7. IDs remain stable and unique inside the collected dataset.

This document does not substitute for browser execution. Runtime status remains NOT VERIFIED until deployed self-test behavior is observed.
