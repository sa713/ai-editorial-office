# Rollback Notes

To roll back Step 3:

1. Open `editorial_knowledge/50_editorial_failure_patterns.md`.
2. Remove the section:
   `### Pattern: Sketchnote → Infographic Drift`
3. Leave all other failure patterns unchanged.
4. Optionally keep or remove this retrospective folder depending on whether the
   rollback should preserve historical context.

Rollback impact: the system will lose the named failure pattern for detecting
sketchnote-to-infographic drift, but no execution, review, pipeline, or agent
behavior will change.
