# Step 6 Implementation Plan

## Scope

Perform only Step 6: add current-version discipline for version-heavy tasks with
refinement loops, multiple artifact generations, and v2/v3/v4 materials.

## Plan

1. Inspect existing current-version, restart, old-version, and navigation rules.
2. Strengthen `AGENTS.md` with a global current-version discipline that requires
   one explicit task-local pointer and forbids guessing from recency.
3. Expand `task_manifest_template.md` current-version pointer fields without
   creating a registry or database.
4. Add navigation guidance to `project_tree.md`.
5. Patch only pipeline restart checks where broad old-version reading could
   otherwise create restart noise or guessing.
6. Record changed files, decisions, safety checks, rollback notes, and semantic
   diff.

## Completion

Completed. Current-version discipline is manifest-centered, explicit, and
bounded. No versioning system, registry, automation, database logic, or
document-management framework was added.
