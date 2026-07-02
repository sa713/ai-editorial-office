# Rollback Notes

## Rollback Scope

Rollback this step by deleting:

- `ai-editorial-office/templates/artifacts/illustration_brief_template.md`

Also remove the Step 5 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-005/`

## Expected Effect Of Rollback

Rollback would remove the `illustration_brief.md` artifact type and its template.

The previous visual branch layers would remain if Steps 1-4 remain:

- `visual_illustration_brief`;
- visual meaning extraction;
- `visual_concept.md`;
- visual concept review.

The system would no longer have the editorial handoff artifact from `visual_concept.md` to an illustrator.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the illustration brief template and the Step 5 retrospective folder. Do not edit agents, pipelines, task templates, review-system files, image prompts, image workflows, storyboard files, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- `illustration_brief_template.md` no longer exists;
- `visual_concept_template.md` remains if Step 3 remains;
- no Artist Agent, `image_prompt.md`, image workflow, storyboard, comic artifact, presentation artifact, composition methodology, drawing rules, or design methodology remains.
