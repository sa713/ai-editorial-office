# Brief

## Task Identity

- Task ID: `TASK-ENGINEERING-REVIEW-RELEASE`
- Task title: Engineering Review Release
- Task type: system capability release

## User Goal

Complete the Engineering Review roadmap stage as one coherent release that is
ready for Project Lead architectural review.

## Source Of Truth

Priority order:

1. `../../AGENTS.md`
2. `../../ROADMAP.md`
3. `../../project-state.md`
4. `../../research/engineering_review_execution_plan.md`

## Required Outcome

The release must include:

- research for remaining engineering review competencies;
- architecture synthesis;
- implemented capability documentation where approved;
- validation;
- `/about` synchronization;
- release report at
  `../../research/engineering_review_release_report.md`.

## Constraints

- Preserve existing architecture.
- Do not redesign Task Object, Capability Registry, Shared Lifecycle,
  Review Gate, Role Model, or framework structure.
- Do not introduce new default roles, pipelines, lifecycle stages, mandatory
  artifacts, or duplicate framework owners.
- Merge, split, postpone, or reject competencies when that improves
  architectural quality.
- Do not touch `/Users/sa/Documents/codex/redaction`.

## Acceptance Criteria

- Engineering Review is represented as a coherent capability or justified
  smaller set of capabilities.
- Candidate competencies have final decisions: implemented, merged, postponed,
  or rejected.
- Canonical files are updated only where required.
- `/about` remains exactly 20 files and synced where source-copy files changed.
- Validation scripts pass.
- Final release report exists and records decisions, validation, risks, and
  next-stage recommendations.
