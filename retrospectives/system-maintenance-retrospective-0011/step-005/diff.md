# Step 5 Diff Summary

The local repository state exposes these project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 5.

## Requested File Diff: `templates/artifacts/illustration_brief_template.md`

Requested logical path:

- `templates/artifacts/illustration_brief_template.md`

Actual workspace path:

- `ai-editorial-office/templates/artifacts/illustration_brief_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/illustration_brief_template.md b/ai-editorial-office/templates/artifacts/illustration_brief_template.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/templates/artifacts/illustration_brief_template.md
@@
+# Illustration Brief
+
+Purpose: translate `visual_concept.md` into an editorial assignment an
+illustrator can use to make an illustration that carries the intended meaning.
+
+Output artifact: `illustration_brief.md`
+
+Mode: `visual_illustration_brief`
+
+Source artifact: `visual_concept.md`
+
+Ownership: created by editorial work and used by an illustrator. This brief
+does not replace `visual_concept.md`; it is built from it. It is not a prompt,
+not a model instruction, not a design document, and not a drawing-method
+guide.
+
+Difference from `visual_concept.md`: `visual_concept.md` answers "What does
+the illustration mean?" `illustration_brief.md` answers "What should the
+illustrator draw to carry that meaning?"
+
+Do not specify composition, colors, technique, style, generation settings, or
+prompt wording in this artifact.
+
+### Illustration goal
+
+- Task the illustration should solve:
+
+### Main meaning
+
+- Meaning that must be preserved from `visual_concept.md`:
+
+### Viewer takeaway
+
+- What the viewer should understand within a few seconds:
+
+### Emotional tone
+
+- Feeling the illustration should create:
+- Text-grounded reason for this tone:
+
+### Visual metaphor
+
+- Visual metaphor chosen by editorial:
+- Why this metaphor carries the meaning:
+
+### Required elements
+
+- Elements that must be present:
+- Meaning or source constraint each element protects:
+
+### Forbidden distortions
+
+- What must not be changed:
+- What must not be intensified:
+- What must not be weakened:
+- What must not be added:
+
+### Misreading risks
+
+- Wrong interpretations to avoid:
+- What would create those interpretations:
+
+### Notes for illustrator
+
+- Short clarifications:
+- Meaning constraints to preserve:
+- Open questions before illustration work:
```

## Step Artifacts Added

```diff
+ retrospectives/system-maintenance-retrospective-0011/step-005/implementation-plan.md
+ retrospectives/system-maintenance-retrospective-0011/step-005/changed-files.md
+ retrospectives/system-maintenance-retrospective-0011/step-005/illustration-brief-decisions.md
+ retrospectives/system-maintenance-retrospective-0011/step-005/safety-check.md
+ retrospectives/system-maintenance-retrospective-0011/step-005/rollback-notes.md
+ retrospectives/system-maintenance-retrospective-0011/step-005/diff.md
```

## Boundary Confirmation

```diff
+ Added `illustration_brief.md` artifact template.
+ Built it on `visual_concept.md`.
+ Defined ownership: created by editorial, used by illustrator.
+ Distinguished it from `visual_concept.md`.
- Added no Artist Agent.
- Added no `image_prompt.md`.
- Added no image generation workflow.
- Added no composition methodology.
- Added no drawing rules.
- Added no storyboard, comic artifact, or presentation artifact.
- Started no Step 6+ work.
```
