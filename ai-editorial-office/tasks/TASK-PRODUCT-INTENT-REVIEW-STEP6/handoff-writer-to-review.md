# Handoff — Writer Agent to Review Agent

- From: `writer_agent`
- To: independent `review_agent` role instance
- Reason: evaluation fixture, runner, runner tests, manifest metrics, reports,
  and full regression evidence are complete.
- Review first: `brief.md`, `evaluation-design.md`, `evaluation-rubric.md`,
  `case-catalogue.md`, `coverage-report.md`, `evaluation-report.md`,
  `defect-log.md`, `repair-loop-report.md`, and the fixture/runner.
- Challenge: case difficulty, expected-result independence, real negative
  cases, acceptable variability, automation/manual separation, hidden failures,
  overfit, repair evidence, limitations, and readiness.
- Verify: no production diff, one review gate, existing outcomes, unchanged
  Professional Analysis status, and no Step 7 surface.
- Do not edit: observed case results during judgment.
- Escalate if: any case is too weak, self-approving, hidden, or unsupported.
