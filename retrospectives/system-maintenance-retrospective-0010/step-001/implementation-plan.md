# Step 1 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0010 / step-001`

Focus: artifact depth normalization for low-risk and simple standard tasks.

Goal: reduce unnecessary support artifacts without weakening review, governance, or traceability.

## Discovery

Rules and creation pressure were found in these canonical or scaffold areas:

- `ai-editorial-office/AGENTS.md`:
  - global artifact minimalism;
  - process depth;
  - review-gate;
  - task folder example;
  - `compact-handoff.md` semantics.
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`:
  - artifact scope table;
  - compact process depth fields.
- `ai-editorial-office/pipelines/*.md`:
  - pipeline artifact sets;
  - review/finalization requirements;
  - completion checks.
- `ai-editorial-office/agents/*.md`:
  - role-local output lists that made some support artifacts appear mandatory.
- `ai-editorial-office/templates/tasks/*.md`:
  - task scaffolds that instructed agents to create `open-questions.md` even when empty and to expect full review/finalization support sets.

Historical task folders were intentionally not edited.

## Implementation Steps

1. Clarify the global artifact rule in `AGENTS.md`.
2. Make `review.md` the primary review artifact for low-risk and simple standard tasks.
3. Make `review-summary.md`, `qa-checklist.md`, `finalization-checklist.md`, `open-questions.md`, and `finalization-notes.md` conditional.
4. Clarify that `compact-handoff.md` is not automatic.
5. Clarify that legacy task folders are history, not templates.
6. Update only direct mandatory language in relevant pipelines, role specs, and task scaffolds.
7. Run search checks for stale mandatory wording.

## Non-Goals

- No role set changes.
- No pipeline replacement.
- No governance model changes.
- No new workflow.
- No new production artifacts.
- No automation.
- No Step 2-6 work.

## Status

Completed.
