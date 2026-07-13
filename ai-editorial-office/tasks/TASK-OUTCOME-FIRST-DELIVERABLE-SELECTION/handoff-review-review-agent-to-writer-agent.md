# Handoff: Review Agent To Writer

- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
- From: Review Agent
- To: Writer / implementation function
- Review outcome: `changes_requested`
- Source: `review.md`, finding `OFD-001`

## Required Repair

- Fold outcome-first deliverable criteria and blockers into the existing Task
  Need Recognition gate row in `pipelines/review_pipeline.md`.
- Remove the standalone `Outcome-first deliverable gate` label and replace the
  completion wording with criteria inside the existing review gate.
- Resynchronize `about/review_pipeline.md`.
- Add a negative assertion to
  `tests/test_outcome_first_deliverable_selection.sh` that rejects the
  standalone gate label.

## Bounded Re-review Scope

- `pipelines/review_pipeline.md`
- `about/review_pipeline.md`
- `tests/test_outcome_first_deliverable_selection.sh`
- validation rerun and truthfulness of the no-new-gate statement in
  `implementation-report.md`

Do not change the approved deliverable model, role ownership, template ordering,
synthetic case expectations, or unrelated files.
