# Handoff semantic decisions

## Decisions implemented

- `handoff-*` means role-to-role delta transfer.
- `handoff-*` should use one receiving role in the filename.
- Route ambiguity belongs inside the handoff body, not in filename variants.
- `compact-handoff.md` means final/user-facing transfer summary.
- `compact-handoff.md` must not be used for role routing.
- `context-summary.md` means optional recovery artifact after context fragmentation, long-running work, or handoff failure.
- `context-summary.md` is not a routine status update.
- Handoff must reference manifest instead of repeating full manifest state.
- Handoff must not repeat full status history, orchestration plan, KB list, restart checklist, or full artifact inventory.

## Decisions intentionally not implemented

- No new handoff workflow.
- No new artifact type.
- No required `context-summary.md`.
- No restart automation.
- No lifecycle state changes.
- No review ergonomics changes.
