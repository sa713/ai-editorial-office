# Handoff — Writer Agent to Review Agent

- From: `writer_agent` with bounded implementation capabilities
- To: `review_agent`
- Reason: Step 4 implementation and pre-review regressions are complete.
- Review first: both designs, `implementation-report.md`, `canonical-diff.md`,
  `change-summary.md`, changed owners/profiles/roles/templates, output checker,
  fixtures, and regression evidence.
- Required challenge: all twenty-nine acceptance criteria, twelve scenarios,
  existing-profile fit, order/directness/uncertainty/leakage, `not_needed`,
  source-size independence, Step 2/3 regressions, forbidden surfaces, and
  `/about` parity.
- Expected output: independent `review.md` with one existing outcome.
