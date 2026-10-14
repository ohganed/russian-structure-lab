# Case Explorer pilot verification
Run from the repository root with Node.js 18+:

```sh
node --test tests/case-explorer.test.cjs
```

This suite checks curated data shape, unique examples, answer indices, expected form agreement, navigation, and that explanations are not revealed before a correct answer. It does not replace a real Safari/iPhone browser test.

The GitHub Actions workflow also runs Playwright checks in Chromium and WebKit. These cover all six examples, answer feedback, retry/reset, wraparound navigation, mobile-width touch interaction, and return navigation. WebKit on Linux approximates Safari engine behavior; it is not a substitute for testing on a physical iPhone or checking Russian speech voices on the device.
