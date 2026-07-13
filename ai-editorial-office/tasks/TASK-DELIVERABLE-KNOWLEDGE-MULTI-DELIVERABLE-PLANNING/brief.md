# Brief

## Task identity

- Task ID: `TASK-DELIVERABLE-KNOWLEDGE-MULTI-DELIVERABLE-PLANNING`
- Task type: canonical system extension
- Date: 2026-07-13

## Goal

Extend Outcome-First Deliverable Selection so deliverables are reusable
knowledge objects and Chief Editor can select a single deliverable or a minimal
ordered deliverable set when one artifact cannot satisfy the user outcome.

## Required result

- create canonical deliverable knowledge under `kb/deliverables/`;
- describe purpose, use cases, structure, strengths, weaknesses, failure modes,
  companions, and nearby-type boundaries for each catalogue entry;
- introduce `selected_deliverable_set` as the current multi-deliverable view;
- keep explicit user intent authoritative and prevent automatic bundle growth;
- preserve current roles, pipelines, lifecycle, review gate, and artifact
  minimalism;
- add deterministic synthetic tests for single and coordinated selections.

## Architecture constraints

- no Deliverable, Catalogue, Package, or Bundle Agent;
- no new pipeline, lifecycle stage, review gate, score, classifier, generator,
  or mandatory standalone task artifact;
- deliverable knowledge belongs to Knowledge Base;
- selection belongs to Chief Editor;
- review belongs to Review Agent;
- production belongs to existing Writer/UX Writer roles;
- catalogue profiles guide judgment and are not templates.

## Requested and selected output

- Requested deliverable: repository implementation with tests.
- Format authority: `explicit` for implementation and constraints;
  implementation-report format is safely inferred for traceable delivery.
- Selected deliverable set:
  1. canonical repository update — primary implementation;
  2. synthetic regression suite — validation evidence, depends on the canon;
  3. compact implementation report — delivery explanation, depends on the
     final reviewed patch.

## Success criteria

- catalogue profiles are discoverable and follow one stable knowledge schema;
- the task model supports a single item or ordered set with purpose, dependency,
  and production priority per member;
- Chief Editor explicitly decides whether one artifact is sufficient;
- the chosen set is minimal, outcome-based, and not produced automatically;
- Review Agent can remove redundant members or identify a missing necessary
  companion using deterministic evidence;
- explicit requested format remains preserved unless the user agrees to change;
- synthetic cases cover longread-only, AI education, presentation, interview
  publication, and short-answer behavior;
- repository validators and `/about` exact-copy checks pass.

## Out of scope

- real content production from catalogue profiles;
- automatic deliverable classification or package generation;
- new permanent roles, pipelines, statuses, or gates;
- publication to GitHub without a separate user request.
