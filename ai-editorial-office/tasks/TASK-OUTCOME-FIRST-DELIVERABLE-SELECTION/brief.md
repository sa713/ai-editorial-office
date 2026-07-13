# Brief

## Task

- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
- Goal: add outcome-first deliverable selection before pipeline selection while
  preserving evidence discipline, governance, traceability, review, and the
  existing architecture.
- Source instruction: user-provided Codex task dated 2026-07-13.

## User Objective

Make AI Editorial Office determine whether the initially mentioned artifact is
the best way to solve the user's real problem before it chooses how to produce
that artifact.

## Deliverable

- Requested deliverables: canonical implementation, implementation report,
  complete diff, modified-canonical-files summary, architectural decision
  explanation, and synthetic tests.
- Format authority: `explicit`.
- Advisory recommended deliverable: the requested bounded patch and evidence
  package are already sufficient.
- Selected deliverable: same as requested; no alternative format needed.

## Constraints

- Do not redesign the system.
- Do not add a permanent role, pipeline, lifecycle stage, gate, score, or
  mandatory standalone artifact.
- Do not silently weaken explicit user format authority.
- Do not modify unrelated systems or pre-existing untracked task material.
- Keep Task Need Recognition advisory and Chief Editor authoritative.
- Keep independent review mandatory.

## Acceptance Criteria

- Requested, recommended, and selected deliverables are distinct in canon.
- Format authority is explicit and silent override is forbidden.
- Chief Editor selects the deliverable before the pipeline.
- Intake captures request evidence without selecting the deliverable.
- Review verifies artifact suitability, explicit-intent preservation,
  explanation of alternatives, and pipeline ordering.
- Synthetic cases cover the five required examples and material negative cases.
- `/about` exact-copy package remains synchronized.
- Existing validators and smoke tests pass.
