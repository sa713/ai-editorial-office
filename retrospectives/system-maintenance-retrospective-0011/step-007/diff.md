# Step 7 Diff Summary

The local repository state exposes these project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 7.

## Requested File Diff: `editorial_knowledge/40_editorial_review_system.md`

```diff
diff --git a/editorial_knowledge/40_editorial_review_system.md b/editorial_knowledge/40_editorial_review_system.md
--- a/editorial_knowledge/40_editorial_review_system.md
+++ b/editorial_knowledge/40_editorial_review_system.md
@@
 Use this pass only to review the meaning layer before artist or prompt work. It must not review a finished image, judge an artist, become art direction, become design review, teach visual design, create a generation workflow, or prepare prompt wording. If revision is needed, request correction of the semantic concept, not image execution details.
+
+When `visual_concept.md`, `illustration_brief.md`, and `image_prompt.md` all exist, review may add a bounded meaning-preservation chain check:
+- **Meaning continuity**: does the main meaning remain stable from `visual_concept.md` to `illustration_brief.md` to `image_prompt.md`?
+- **Viewer takeaway continuity**: does the intended viewer understanding stay the same across all three artifacts?
+- **Metaphor continuity**: does the selected visual metaphor remain intact, or was it replaced by another metaphor?
+- **Distortion introduction**: did `illustration_brief.md` or `image_prompt.md` introduce meanings that were absent from `visual_concept.md`?
+- **Constraint preservation**: are required elements, forbidden distortions, and misreading protections preserved downstream?
+- **Prompt drift**: does `image_prompt.md` amplify secondary ideas, lose the main conclusion, or visually complete material beyond the approved concept?
+- **Boundary protection**: does the review stay focused on meaning rather than image quality, style, composition, color, drawing technique, or artistic taste?
+
+Use this check only to verify semantic continuity across the artifact chain. It must not become image quality review, art direction, Artist QA, artistic critique, composition review, color review, style review, drawing review, comic work, or presentation work. If a problem appears after `visual_concept.md`, fix `illustration_brief.md` or `image_prompt.md` at the point where the meaning drift was introduced; do not change `visual_concept.md` to accommodate later drift.
 
 ## Structure review
```

## Step Artifacts Added

```diff
+ retrospectives/system-maintenance-retrospective-0011/step-007/implementation-plan.md
+ retrospectives/system-maintenance-retrospective-0011/step-007/changed-files.md
+ retrospectives/system-maintenance-retrospective-0011/step-007/meaning-preservation-decisions.md
+ retrospectives/system-maintenance-retrospective-0011/step-007/safety-check.md
+ retrospectives/system-maintenance-retrospective-0011/step-007/rollback-notes.md
+ retrospectives/system-maintenance-retrospective-0011/step-007/diff.md
```

## Boundary Confirmation

```diff
+ Added meaning-preservation review across `visual_concept.md` -> `illustration_brief.md` -> `image_prompt.md`.
- Added no image review.
- Added no image quality review.
- Added no art direction.
- Added no Artist QA pipeline.
- Added no composition, color, style, technique, or drawing-quality review.
- Added no comics.
- Added no presentations.
```
