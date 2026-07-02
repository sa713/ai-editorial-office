# Diff

```diff
diff --git a/editorial_knowledge/10_operational_rules.md b/editorial_knowledge/10_operational_rules.md
--- a/editorial_knowledge/10_operational_rules.md
+++ b/editorial_knowledge/10_operational_rules.md
@@
 ### Anti-pattern
 Scoring confidence, mandatory tagging, evidence matrices, full traceability systems, confidence protocols, or labeling every phrase.
 
 ## Rule
 
+### Principle
+Separate editorial diagnosis, author concept diagnosis, and solution design before choosing the output shape.
+
+### Why it exists
+Prevents the editorial system from mixing material analysis, the author's idea state, and solution architecture in one response.
+
+### Reader impact
+The reader receives the type of help they asked for and can see when a different type of work would be a separate next step.
+
+### Writing implication
+Use the working question to keep the response inside the right boundary:
+
+- Editorial diagnosis asks: "What is happening with the material as an object of editorial work?" Focus on clarity, completeness, structure, gaps, and readiness for further editorial work.
+- Author concept diagnosis asks: "What is happening with the author's idea?" Focus on the central thought, problem, intention, mechanism, audience, expected change, success criterion, and what is mixed or not distinguished.
+- Solution design asks: "How should the solution be arranged?" Focus on model, process, roles, scenarios, roadmap, metrics, governance, and implementation.
+
+Move from one type of work to another only when the task explicitly asks for it or records it. If the task is diagnosis, do not turn it into solution design. If design is needed, name it as a separate next step first.
+
+### Repair implication
+If the response mixes types, return it to the requested type of work; name what is analysis, interpretation, and proposed development; remove ready-made solutions that were not requested.
+
+### Anti-pattern
+Diagnosing a weak material by inventing a program, treating an author's unresolved idea as a design brief, or hiding solution design inside diagnostic recommendations.
+
+## Rule
+
 ### Principle
 If a term or distinction does not affect reader action, remove it or demote it.
```
