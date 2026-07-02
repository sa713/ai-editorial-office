# Rollback notes

## Full rollback

To fully rollback Step 1:

1. Remove `Canonical ownership map` from `ai-editorial-office/AGENTS.md`.
2. Restore the removed repeated sections in `ai-editorial-office/project-state.md` if a previous version is needed.
3. Clear `ai-editorial-office/kb/00_index.md` back to its prior empty state.
4. Keep or remove this retrospective folder as historical implementation notes.

## Partial rollback

If the new ownership map creates confusion:

- keep the `project-state.md` anti-duplication cleanup;
- shorten the `AGENTS.md` ownership map to only system-level owners;
- keep `kb/00_index.md` because it only clarifies KB scope.

If `project-state.md` becomes too sparse for restart:

- add back only temporary current-state summaries;
- do not restore full permanent policy duplication unless no canonical owner can carry the rule.

## Drift response

If new drift appears:

- first identify the canonical owner from `AGENTS.md`;
- move the rule to that owner;
- replace duplicates with a short reference;
- if no owner fits, stop and route to `chief_editor` instead of adding more prose.

## Rollback safety

Rollback does not require changing pipelines, templates, agents, statuses, or task folders. The Step 1 changes are documentation-level and reversible by removing or restoring short markdown sections.
