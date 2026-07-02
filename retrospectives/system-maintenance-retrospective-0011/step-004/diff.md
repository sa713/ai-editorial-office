# Step 4 Diff Summary

The local repository state exposes these project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 4.

## Requested File Diff: `editorial_knowledge/40_editorial_review_system.md`

```diff
diff --git a/editorial_knowledge/40_editorial_review_system.md b/editorial_knowledge/40_editorial_review_system.md
--- a/editorial_knowledge/40_editorial_review_system.md
+++ b/editorial_knowledge/40_editorial_review_system.md
@@
 This check must not ban development suggestions, hypotheses, or next-step recommendations. It should catch editorial takeover and hidden consulting drift while keeping review compact, editorial-first, and specific to `author_concept_diagnosis`; it must not become a workflow, scoring model, maturity review, coaching session, or ideation methodology.
+
+For `visual_illustration_brief` outputs, especially `visual_concept.md`, review may add a bounded semantic visual-concept pass:
+- **Meaning integrity**: does the concept preserve the text's main meaning, avoid adding a new meaning, and keep the main conclusion visible?
+- **Viewer takeaway integrity**: does the 3-5 second viewer takeaway match what the text actually wants to say?
+- **Metaphor quality**: does the metaphor carry the meaning, avoid first-obvious banality, and avoid reducing the text to caricature?
+- **Distortion check**: did the concept introduce extra meanings, false emphasis, tone distortion, or visual completion of the author's idea?
+- **Misreading risk**: does the review identify what the viewer may misunderstand and where the strongest misreading risks are?
+- **Visual usefulness**: would the concept help someone understand, become interested in, or retain the text's meaning rather than merely produce a beautiful picture?
+- **Boundary protection**: does the review stay away from style, composition, color, drawing technique, artist skill, and artistic taste?
+
+Use this pass only to review the meaning layer before artist or prompt work. It must not review a finished image, judge an artist, become art direction, become design review, teach visual design, create a generation workflow, or prepare prompt wording. If revision is needed, request correction of the semantic concept, not image execution details.
 
 ## Structure review
```

## Step Artifacts Added

```diff
+ retrospectives/system-maintenance-retrospective-0011/step-004/implementation-plan.md
+ retrospectives/system-maintenance-retrospective-0011/step-004/changed-files.md
+ retrospectives/system-maintenance-retrospective-0011/step-004/visual-review-decisions.md
+ retrospectives/system-maintenance-retrospective-0011/step-004/safety-check.md
+ retrospectives/system-maintenance-retrospective-0011/step-004/rollback-notes.md
+ retrospectives/system-maintenance-retrospective-0011/step-004/diff.md
```

## Boundary Confirmation

```diff
+ Added bounded semantic review guidance for `visual_concept.md`.
- Added no Artist Agent.
- Added no `image_prompt.md`.
- Added no image generation workflow.
- Added no image review.
- Added no artist review.
- Added no art direction.
- Added no design methodology.
- Started no Step 5+ work.
```
