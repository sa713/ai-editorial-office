# Diff

Git currently sees `editorial_knowledge/01_principles.md` as an untracked file in this workspace, so `git diff -- editorial_knowledge/01_principles.md` does not produce a tracked diff.

The effective change made in this step is:

```diff
diff --git a/editorial_knowledge/01_principles.md b/editorial_knowledge/01_principles.md
--- a/editorial_knowledge/01_principles.md
+++ b/editorial_knowledge/01_principles.md
@@
 ## Russian editorial clarity
+
+## Reader-state boundaries
+
+Reader-state awareness is a small editorial sensitivity, not a behavioral layer.
+
+Use it only when a task asks the reader to enter, try, join, respond, use a workspace, or take a first step that may feel heavier than it needs to be.
+
+The purpose is limited:
+
+- make the honest first step clear;
+- reduce unnecessary pressure;
+- allow observation before commitment when that is factually available;
+- keep the language human, operational, and specific.
+
+It must not become:
+
+- persuasion;
+- emotional editing;
+- engagement or adoption optimization;
+- tone policing;
+- a new workflow, stage, role, score, or review requirement.
+
+### Honesty rule
+
+Mandatory stays mandatory.
+Optional stays optional.
+Unknown stays unknown.
+
+Reader-state edits must not hide rules, soften real obligations into suggestions, make optional actions sound required, or imply activity and social proof without evidence.
```
