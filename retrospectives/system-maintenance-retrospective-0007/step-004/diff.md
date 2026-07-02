# Diff

```diff
diff --git a/editorial_knowledge/40_editorial_review_system.md b/editorial_knowledge/40_editorial_review_system.md
--- a/editorial_knowledge/40_editorial_review_system.md
+++ b/editorial_knowledge/40_editorial_review_system.md
@@
 Use these heuristics only when the task asks for diagnostic analysis of raw or incomplete materials. Do not turn them into a universal checklist, scoring system, confidence matrix, or formal evidence audit. They must not ban uncertainty, demand aggressive confidence, encourage speculative conclusions, or weaken Artificial Concept Completion safeguards.
 
+For `author_concept_diagnosis` tasks, review may add a bounded conceptual pass:
+- **Central thought clarity**: does the idea have a central thought, or does it fall into separate observations, wishes, or concerns?
+- **Problem vs solution confusion**: are the problem, solution, tool, and desired effect distinct, or are they mixed together?
+- **Mechanism visibility**: is it clear why or how the idea is expected to work?
+- **Audience definition**: is it clear who the idea is for and whose behavior, state, or understanding should change?
+- **Expected change**: is it clear what should change if the idea works?
+- **Success criterion**: is it clear how the author would know the idea is working?
+- **Boundary clarity**: does the idea have scope, limits, or constraints, or is it trying to explain or solve everything at once?
+- **Conceptual mixing**: are diagnosis, goals, processes, values, and implementation details kept distinct?
+
+Use these heuristics only to help the author see what is undefined, mixed, absent, disconnected, or not yet distinguished in the idea. Do not turn them into a mandatory checklist, consulting canvas, maturity model, taxonomy system, scoring tool, or artificial sophistication exercise. They should support author-facing diagnosis, not ideation consulting.
+
 ## Structure review
```
