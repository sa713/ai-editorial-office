# Rollback Notes

## rollback scope

Step 3 changed one production file:

```text
ai-editorial-office/agents/chief_editor.md
```

Step 3 also updated or created task-local artifacts in:

```text
ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0016/
```

## production rollback

To roll back the production behavior, remove the `Normalized Brief Contract` section from `chief_editor.md`.

The section begins with:

```text
## Normalized Brief Contract
```

and ends immediately before:

```text
## Outputs
```

## task-local rollback

To roll back only Step 3 task-local records, restore the Step 2 versions of:

- `task-manifest.md`;
- `orchestration_plan.md`;
- `status.md`;
- `implementation-plan.md`;
- `changed-files.md`;
- `safety-check.md`;
- `rollback-notes.md`;
- `diff.md`.

Also remove:

- `normalized-brief-contract-decisions.md`.

## protected files

No rollback is needed for:

- `/ai-editorial-office/agents/intake_agent.md`;
- `/ai-editorial-office/pipelines/`;
- review files;
- visual subsystem files;
- role model definitions;
- task status model files.

