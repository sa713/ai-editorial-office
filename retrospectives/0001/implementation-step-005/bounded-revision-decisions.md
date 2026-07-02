# Bounded revision decisions

## Decisions implemented

- `changes_requested` defaults to bounded revision.
- Review must identify:
  - issue;
  - why it blocks approval;
  - repair owner;
  - repair scope;
  - do-not-change area;
  - re-review scope.
- Re-review focuses on the stated repair scope unless the repair introduces a new blocker.
- Full rewrite, new research, or orchestration escalation requires a blocker, evidence gap, instruction conflict, scope problem, reader outcome failure, or repeated failed repair.

## Decisions intentionally not implemented

- No new lifecycle state for bounded revision.
- No separate bounded-revision artifact required.
- No automatic re-review workflow.
- No permission for reviewer to rewrite.
- No change to review verdict model.

## Boundary

Bounded revision limits repair scope. It does not hide deeper problems. If the root issue exceeds the repair scope, Review Agent should escalate through existing `blocked`, `research`, `writing`, or Chief Editor routing rules.
