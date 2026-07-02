# Rollback Notes

## Rollback Scope

Rollback this step by deleting:

- `ai-editorial-office/templates/artifacts/visual_concept_template.md`

Also remove the Step 3 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-003/`

## Expected Effect Of Rollback

Rollback would remove the `visual_concept.md` artifact type and its template.

The `visual_illustration_brief` mode from Steps 1-2 would remain, but the system would no longer have a standalone output document for visual editorial meaning.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the visual concept template and the Step 3 retrospective folder. Do not edit agents, pipelines, task templates, review-system files, prompt artifacts, storyboard files, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- `visual_concept_template.md` no longer exists;
- `visual_illustration_brief` still exists if Steps 1-2 remain;
- no Artist Agent, Visual Editor Agent, `image_prompt.md`, image workflow, review heuristic, storyboard, comic artifact, or presentation artifact remains.
