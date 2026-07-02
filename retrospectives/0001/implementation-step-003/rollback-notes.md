# Rollback notes

## Full rollback

To fully rollback Step 3:

1. Remove `freshness` section from `task_manifest_template.md`.
2. Remove governance visibility clarification lines from `task_manifest_template.md`.
3. Remove `stale or conflicting state` section from `task_manifest_template.md`.
4. Restore the previous manifest sentence in `AGENTS.md`.
5. Restore the previous Chief Editor manifest update sentence.
6. Remove the Step 3 normalization note from `project-state.md`.

## Partial rollback

If manifest becomes too long:

- keep only `Last updated by` and `Known stale risk`;
- remove `Latest artifact changes`;
- keep stale/conflict response in `AGENTS.md` only.

If governance fields are mistaken for statuses:

- keep the fields but strengthen the note that `/kb/task_statuses.md` owns operational statuses.

If approval workflow confusion appears:

- remove any approval-like detail from manifest guidance;
- keep publication/delivery approval distinction in final decision docs.

## Rollback safety

Rollback does not require changing pipelines, task statuses, review model, agent set, or existing task folders.
