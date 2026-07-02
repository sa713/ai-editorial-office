# Governance state decisions

## Decisions implemented

- Governance state stays in `task-manifest.md` as compact visibility.
- Governance fields are not operational task statuses.
- Operational task status remains owned by `status.md` and `/kb/task_statuses.md`.
- Review, finalization, final governance, human approval, and publication/delivery approval are distinct visibility fields.
- `finalized` does not mean published, delivered, or human-approved unless approval is explicitly recorded.
- Missing or unclear approval should remain visible without creating a new approval workflow.

## Decisions intentionally not implemented

- No approval matrix.
- No new lifecycle.
- No new status values.
- No review verdict changes.
- No automatic approval validation.
- No publication workflow.

## Boundary

The manifest may show governance state for restart and routing. It must not become the place for full review findings, finalization notes, human approval evidence, or publication decision details.
