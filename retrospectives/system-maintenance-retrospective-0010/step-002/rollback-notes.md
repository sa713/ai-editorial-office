# Rollback Notes

## Rollback Scope

Rollback this step by reverting changes in:

- `ai-editorial-office/AGENTS.md`;
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`;
- `about/project_tree.md`;
- touched pipeline files;
- touched role spec files;
- touched task/agent scaffold files.

Also remove the Step 2 retrospective folder if the implementation itself is rolled back.

## Expected Effect Of Rollback

Rollback would restore broader context loading behavior:

- ordinary restart would again point agents toward longer file lists;
- task scaffolds would again load `/project-state.md`, status, brief, orchestration, pipeline, role spec, and stage artifacts by default;
- role specs would again preload more files before acting;
- version-heavy tasks would lack an explicit current-version pointer requirement.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, restore from the pre-step project snapshot. Do not delete task history folders or task artifacts during rollback.

## Post-Rollback Check

After rollback, verify:

- review is still mandatory;
- high-governance traceability is still available;
- no partial current-version pointer wording remains without template support;
- legacy tasks are not accidentally promoted into templates.
