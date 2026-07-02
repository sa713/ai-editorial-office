# Rollback Notes

## Rollback Scope

Rollback this step by removing these Step 2 additions from the `visual_illustration_brief` section:

- `Visual meaning extraction guidance`;
- `Visual anti-patterns`.

File:

- `editorial_knowledge/20_editorial_modes.md`

Also remove the Step 2 retrospective folder if the implementation record itself is rolled back:

- `retrospectives/system-maintenance-retrospective-0011/step-002/`

## Expected Effect Of Rollback

Rollback would keep the Step 1 mode but remove the more explicit guidance for extracting:

- main meaning;
- viewer takeaway;
- emotional tone;
- visual metaphor;
- distortion risks;
- visual anti-patterns.

## Safe Rollback Command Shape

Use a normal VCS revert if these files are tracked in the target environment.

If working without tracked history, manually remove only the Step 2 guidance sections and the Step 2 retrospective folder. Do not edit agents, pipelines, templates, image workflows, review-system files, or prompt artifacts during rollback.

## Post-Rollback Check

After rollback, verify:

- `visual_illustration_brief` still exists from Step 1;
- `Visual meaning extraction guidance` is gone;
- `Visual anti-patterns` is gone;
- no Artist Agent, Visual Editor Agent, workflow, prompt, template, or review heuristic remains.
