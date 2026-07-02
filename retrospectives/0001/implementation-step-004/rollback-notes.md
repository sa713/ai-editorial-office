# Rollback notes

## Full rollback

To fully rollback Step 4:

1. Remove the new `compact-handoff.md` and `context-summary.md` paragraphs from `AGENTS.md`.
2. Remove `compact-handoff.md` and `context-summary.md` rows from the artifact responsibility table in `AGENTS.md`.
3. Restore the previous `context-summary.md` sentence in `AGENTS.md` context discipline.
4. Remove the `compact-handoff.md` / `context-summary.md` exclusion note from `handoff_template.md`.
5. Restore the previous Chief Editor handoff wording.
6. Remove the Step 4 current-state notes from `project-state.md`.

## Partial rollback

If `compact-handoff.md` causes confusion:

- keep only the AGENTS definition;
- remove mentions from Chief Editor guidance.

If `context-summary.md` is underused:

- keep it optional;
- add examples later only after real restart failures.

If task templates drift:

- do not rewrite all task templates at once;
- update only the template that caused the drift.

## Rollback safety

Rollback does not require changing lifecycle, statuses, governance state, compact path, review model, or existing task folders.
