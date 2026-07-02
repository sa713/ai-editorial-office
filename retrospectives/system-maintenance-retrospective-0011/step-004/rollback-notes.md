# Rollback Notes

## Rollback Scope

Rollback this step by removing the bounded semantic visual-concept pass for `visual_illustration_brief` from:

- `editorial_knowledge/40_editorial_review_system.md`

Also remove the Step 4 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-004/`

## Expected Effect Of Rollback

Rollback would keep the `visual_illustration_brief` mode and `visual_concept.md` template from earlier steps, but remove the dedicated review guidance for checking visual concepts.

The system would no longer explicitly check:

- meaning integrity;
- viewer takeaway integrity;
- metaphor quality;
- distortion;
- misreading risk;
- visual usefulness;
- boundary protection.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the Step 4 review pass and the Step 4 retrospective folder. Do not edit agents, pipelines, templates, image prompts, image workflows, storyboard files, comic files, or presentation files during rollback.

## Post-Rollback Check

After rollback, verify:

- the `visual_illustration_brief` review pass no longer appears in `40_editorial_review_system.md`;
- `visual_illustration_brief` itself remains if Steps 1-2 remain;
- `visual_concept_template.md` remains if Step 3 remains;
- no Artist Agent, `image_prompt.md`, image workflow, art direction, or design methodology remains.
