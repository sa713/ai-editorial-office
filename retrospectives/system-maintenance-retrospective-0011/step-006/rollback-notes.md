# Rollback Notes

## Rollback Scope

Rollback this step by deleting:

- `ai-editorial-office/agents/artist_agent.md`;
- `ai-editorial-office/templates/artifacts/image_prompt_template.md`.

Also remove the Step 6 retrospective folder if the implementation record itself
is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-006/`

## Expected Effect Of Rollback

Rollback would remove the execution role and `image_prompt.md` artifact type.

The previous visual branch layers would remain if Steps 1-5 remain:

- `visual_illustration_brief`;
- visual meaning extraction;
- `visual_concept.md`;
- visual concept review;
- `illustration_brief.md`.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the Artist Agent file,
the image prompt template, and the Step 6 retrospective folder. Do not edit
pipelines, review-system files, visual concept template, illustration brief
template, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- `artist_agent.md` no longer exists;
- `image_prompt_template.md` no longer exists;
- pipelines are unchanged;
- review system is unchanged;
- `visual_concept_template.md` remains unchanged if Step 3 remains;
- `illustration_brief_template.md` remains unchanged if Step 5 remains.
