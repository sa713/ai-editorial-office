# Handoff: Implementation To Review Agent

- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
- From: Writer / implementation function
- To: Review Agent
- Status recommendation: `review`
- Reviewed target: current repository diff plus task-local implementation report
  and synthetic tests

## Required Review

- Verify the patch adds deliverable selection before pipeline selection.
- Verify requested, recommended, and selected deliverables and format authority
  are not conflated.
- Verify explicit user intent cannot be silently overridden and material
  mismatch routes through existing preflight.
- Verify Task Need Recognition stays advisory and Chief Editor stays the only
  deliverable/pipeline decision owner.
- Verify Intake, production roles, Review, Final Editor, task model, lifecycle,
  templates, and affected pipelines are consistent.
- Verify the required synthetic positive and negative cases are deterministic.
- Verify no new role, pipeline, lifecycle stage, gate, score, taxonomy, or
  mandatory standalone operational artifact was created.
- Verify `/about` exact copies and existing validators remain valid.
- Verify unrelated pre-existing untracked files are outside scope.

## Evidence

- `brief.md`
- `orchestration_plan.md`
- `implementation-report.md`
- `tests/outcome_first_deliverable_selection_smoke_test.md`
- `tests/test_outcome_first_deliverable_selection.sh`
- current `git diff`

## Boundaries

- Review only; do not edit or rewrite repository files.
- Record exact blocking/required findings with file and line evidence.
- Suggestions that do not block the stated acceptance criteria must remain
  non-blocking.
- Complete diff is intentionally generated after bounded repairs so it reflects
  the final reviewed snapshot.
