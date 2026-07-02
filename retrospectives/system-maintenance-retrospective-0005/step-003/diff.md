# Diff

```diff
diff --git a/editorial_knowledge/40_editorial_review_system.md b/editorial_knowledge/40_editorial_review_system.md
@@
 - **Educational scaffolding**: judge prerequisites, mental model size, example quality, transfer to use, and whether the reader can apply the concept.
 - **Exploration**: judge boundaries, useful dimensions, distinct paths, narrowing logic, and whether curiosity becomes navigable.
 - **Opinion framing**: judge clarity of lens, separation of fact and interpretation, limits of the frame, and whether the frame can be tested against the case.
+- **Diagnostic analysis**: judge whether the text preserves the raw state of the idea, separates observed, implied, inferred, and hypothetical material, and avoids hidden solutioning.
 
 Mode-specific criteria should override generic review habits. Do not review an instruction for narrative richness or a decision-support text for encyclopedic coverage.
+
+For `diagnostic_analysis` tasks, review may add a bounded diagnostic pass:
+- **Distinction integrity**: are observed, implied, inferred, and hypothetical points visibly separated?
+- **Artificial completion check**: is the editorial system analyzing the idea, or quietly designing it?
+- **Uncertainty preservation**: did uncertainty remain visible, or were gaps automatically fixed?
+- **Hypothesis discipline**: if development is suggested, is it marked as a hypothesis or clarification direction rather than a ready solution?
+- **Rawness preservation**: does the result still show the real state of the materials, or has it become too mature?
+
+Use these heuristics only when the task asks for diagnostic analysis of raw or incomplete materials. Do not turn them into a universal checklist, scoring system, confidence matrix, or formal evidence audit.
```
