# Overlap reduction notes

## Reduced overlap

- Handoff remains role-to-role delta, not restart encyclopedia.
- `compact-handoff.md` is separated from role routing.
- `context-summary.md` is separated from normal handoff and status update.
- Manifest remains compact current state.
- Status remains detailed transition history.
- Orchestration remains execution contract.

## Anti-duplication guidance added

- Handoff should reference `task-manifest.md`.
- Handoff should list only changed artifacts, not the whole task folder.
- Handoff should not repeat full manifest, status history, orchestration plan, KB list, restart checklist, or artifact inventory.
- Context summary should only exist when ordinary restart files are insufficient.

## Left unchanged

- Existing task templates already contain handoff lists; they were not rewritten.
- Existing task folders were not migrated.
- Existing `compact-handoff.md` files in old tasks were not renamed.
- Existing lifecycle and status rules were not changed.

## Remaining risk

Legacy task folders still contain mixed examples. Future agents should follow the canonical semantics in `AGENTS.md` and `handoff_template.md`, not infer semantics from old tasks.
