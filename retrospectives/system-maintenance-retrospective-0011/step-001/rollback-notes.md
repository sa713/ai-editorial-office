# Rollback Notes

## Rollback Scope

Rollback this step by removing the `visual_illustration_brief` section from:

- `editorial_knowledge/20_editorial_modes.md`

Also remove the Step 1 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-001/`

## Expected Effect Of Rollback

Rollback would remove the editorial mode for meaning-based illustration briefs.

The system would no longer have a dedicated mode for turning a text's meaning into an illustration task, viewer takeaway, mood, metaphor, required elements, constraints, and non-distortion rules.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the `visual_illustration_brief` section and the Step 1 retrospective folder. Do not edit pipelines, templates, agents, comics, presentations, or review-system files during rollback.

## Post-Rollback Check

After rollback, verify:

- `visual_illustration_brief` no longer appears in `editorial_knowledge/20_editorial_modes.md`;
- no pipeline, template, or agent files were changed;
- no comic or presentation behavior was introduced.
