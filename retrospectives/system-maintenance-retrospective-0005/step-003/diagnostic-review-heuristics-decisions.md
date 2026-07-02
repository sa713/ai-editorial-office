# Diagnostic review heuristics decisions

## Placement

The heuristics were added to `editorial_knowledge/40_editorial_review_system.md`, inside the existing mode-specific review behavior section.

No second file was needed.

## Shape

The implementation uses:

- one compact `Diagnostic analysis` line in the mode-specific list;
- one bounded optional diagnostic pass immediately after that list.

This avoids creating a new review stage, workflow, checklist artifact, or template.

## Heuristics included

- Distinction integrity: observed, implied, inferred, and hypothetical points stay visibly separated.
- Artificial completion check: review asks whether the text analyzes the idea or quietly designs it.
- Uncertainty preservation: gaps and ambiguity remain visible instead of being automatically fixed.
- Hypothesis discipline: suggested development is marked as a hypothesis or clarification direction.
- Rawness preservation: the result still shows the real state of the materials and does not become too mature.

## Boundary

The heuristics apply only when the task asks for diagnostic analysis of raw or incomplete materials. They are not universal review requirements, scoring criteria, tone policing, a confidence matrix, or a formal evidence audit.
