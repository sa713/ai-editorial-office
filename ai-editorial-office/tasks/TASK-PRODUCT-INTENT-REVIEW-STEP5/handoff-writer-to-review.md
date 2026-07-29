# Handoff — Writer Agent to Review Agent

- From: `writer_agent`
- To: `review_agent`
- Reason: bounded Step 5 implementation and pre-review regressions are complete.
- Changed: canonical validation semantics, short role/profile consequences,
  derived method-fit checker, 15 authorized scenarios, 3 bounded class-coverage
  scenarios, and compact output fields.
- Review first: `brief.md`, `validation-contract-design.md`,
  `validation-method-map.md`, `implementation-report.md`, `canonical-diff.md`,
  `change-summary.md`, and the exact scoped diff.
- Required decision: evaluate all 32 acceptance criteria with
  `pass`/`fail`/`not applicable`/`needs clarification` and issue only an
  existing operational outcome.
- Verify negative scope: no new role, pipeline, stage, gate, status, outcome,
  required report, evidence taxonomy, automatic method, release change, or
  Step 6.
- Independence: reviewer role instance did not perform the Writer Agent
  implementation.
- Escalate if: evidence is insufficient for deterministic approval or a
  material defect requires a bounded repair.
