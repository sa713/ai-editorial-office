# Rollback Notes

## Rollback Scope

Rollback this step by removing the bounded meaning-preservation chain check from:

- `editorial_knowledge/40_editorial_review_system.md`

Also remove the Step 7 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-007/`

## Expected Effect Of Rollback

Rollback would remove explicit review guidance for checking semantic continuity across:

- `visual_concept.md`;
- `illustration_brief.md`;
- `image_prompt.md`.

Earlier visual branch artifacts and roles would remain if Steps 1-6 remain.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the Step 7 meaning-preservation review block and the Step 7 retrospective folder. Do not edit agents, pipelines, templates, image artifacts, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- the meaning-preservation chain check no longer appears in `40_editorial_review_system.md`;
- the prior `visual_illustration_brief` review pass remains if Step 4 remains;
- no image quality review, Artist QA pipeline, art direction, comic workflow, or presentation workflow remains.
