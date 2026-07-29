# Handoff — Writer Agent to Review Agent

- From: `writer_agent` with bounded implementation capabilities
- To: `review_agent`
- Reason: Step 3 implementation and pre-review regressions are complete.
- Review first: `implementation-report.md`, `change-summary.md`,
  `canonical-diff.md`, both integration designs, changed canonical surfaces,
  executable checker/tests, and current scoped status.
- Required challenge: all thirty acceptance criteria, ten scenarios,
  finding/verdict separation, owner authority, single-gate architecture,
  compact path, restart, forbidden surfaces, and `/about` parity.
- Do not rewrite: implementation; request bounded repair for findings.
- Expected output: independent `review.md` with exactly one existing outcome.
