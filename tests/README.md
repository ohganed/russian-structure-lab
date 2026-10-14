# Case Explorer pilot verification
Run from the repository root with Node.js 18+:

```sh
node --test tests/case-explorer.test.cjs
```

This suite checks curated data shape, unique examples, answer indices, expected form agreement, navigation, and that explanations are not revealed before a correct answer. It does not replace a real Safari/iPhone browser test.
