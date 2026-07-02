# Ownership decisions

## Decisions actually implemented

- `AGENTS.md` owns the canonical ownership map.
- `AGENTS.md` owns system invariants, role separation, review-gate, authority hierarchy, artifact minimalism, and governance boundaries.
- `project-state.md` owns current phase, active focus, and current normalization decisions only.
- `/kb/task_statuses.md` owns operational task statuses and transitions.
- `/pipelines/*.md` own pipeline sequence and task-type artifact depth.
- `/agents/*.md` own role behavior and decision boundaries.
- `/templates/artifacts/*.md` own artifact fields and fillable shapes.
- `/templates/tasks/*.md` own task setup scaffolds, not policy restatement.
- `editorial_knowledge/*.md` owns editorial quality, usefulness, modes, and failure patterns.
- Task-local artifacts keep their existing ownership:
  - `task-manifest.md`: compact current state and next action.
  - `status.md`: transition history and blockers.
  - `orchestration_plan.md`: task-specific execution contract.
  - `handoff-*.md`: role-to-role delta transfer.
  - `review.md`: verdict, findings, checked scope, required changes.
  - `final_decision.md`: Chief Editor final governance decision.

## Decisions intentionally not made

- No decision on compact path.
- No decision on manifest freshness or governance block.
- No decision on review depth changes.
- No decision on new templates or artifacts.
- No decision on status model changes.
