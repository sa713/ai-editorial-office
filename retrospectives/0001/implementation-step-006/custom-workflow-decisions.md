# Custom workflow decisions

## Decisions implemented

- Custom workflow remains exceptional.
- Custom workflow is task-local and belongs in `orchestration_plan.md`.
- Mini-contract includes:
  - why no existing pipeline fits;
  - custom stages;
  - required artifacts;
  - review target;
  - stop conditions;
  - human approval implications.
- Custom workflow must not bypass `AGENTS.md`, review-gate, role separation, task statuses, or artifact minimalism.
- Repeated custom workflow patterns should be routed to Chief Editor for later promotion, not expanded inside one task.

## Decisions intentionally not implemented

- No workflow engine.
- No dynamic orchestration system.
- No new lifecycle.
- No new artifact type.
- No automation.
- No new agents.

## Boundary

Mini-contract is a visible constraint for an exception. It is not a new reusable pipeline unless explicitly promoted in a future decision.
