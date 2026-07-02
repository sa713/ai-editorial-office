# Diff

```diff
diff --git a/editorial_knowledge/50_editorial_failure_patterns.md b/editorial_knowledge/50_editorial_failure_patterns.md
@@
 #### Do not over-correct
 
 Do not ban all interpretation or recommendations. Keep bounded hypotheses and material-level recommendations when they are clearly marked and do not become a finished project.
+
+### Pattern: Defensive Diagnostic Drift
+
+#### What it is
+
+After correcting for Artificial Concept Completion, diagnostic analysis starts weakening supported conclusions and becomes defensive analysis.
+
+#### How it appears
+
+Repeated disclaimers; "requires clarification" in nearly every section; supported conclusions framed as weak hypotheses; uncertainty repeated instead of grouped; the text protects itself from error more than it helps the reader understand the situation; conclusions are weaker than the materials justify.
+
+#### Why it hurts usefulness
+
+The diagnosis loses operational value. Readers get caution without enough clarity to decide, prioritize, or take the next step.
+
+#### Typical source
+
+Overcorrection after Artificial Concept Completion, fear of unsupported inference, confusion between uncertainty and usefulness, defensive review behavior, or pressure to avoid hallucination at any cost.
+
+#### Repair move
+
+Match confidence to evidence strength. Keep strong conclusions strong when the materials support them. Consolidate uncertainty into focused limitation blocks. Remove repeated caveats. Distinguish weak inference from supported inference. Restore operational conclusions.
+
+Detection questions: does caution improve honesty or reduce usefulness? Is the conclusion weaker than the materials justify? Is uncertainty repeated instead of localized? Would a reader still know what to do or conclude? Is the text analyzing or self-protecting?
+
+#### Do not over-correct
+
+Do not ban uncertainty or hypotheses. Keep previous diagnostic guardrails: do not invent governance, roadmap, lifecycle, process structure, or completion behavior without support from the materials.
```
