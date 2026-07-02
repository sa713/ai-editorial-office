# Defensive review heuristics decisions

## Placement

The heuristics were added to the existing bounded diagnostic pass in `editorial_knowledge/40_editorial_review_system.md`.

This keeps the change mode-specific and avoids creating a new review stage, workflow, or audit process.

## Heuristic decision

The added checks cover:

- confidence proportionality;
- disclaimer inflation;
- usefulness preservation;
- defensive weakening.

They help review notice when diagnostic analysis becomes self-protective and less useful.

## Boundary decision

The guidance explicitly says these heuristics must not ban uncertainty, demand aggressive confidence, encourage speculative conclusions, or weaken Artificial Concept Completion safeguards.

## Anti-bureaucracy decision

No scoring, matrix, formal evidence logic, checklist expansion, or reviewer workflow was introduced.
