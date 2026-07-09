# Knowledge Evolution Architecture Synthesis

Date: 2026-07-09

## Decision

Implement Knowledge Evolution as an explicit bounded capability inside the
existing canonical owner, `kb/editorial_learning_framework.md`, with concise
integration references in existing role, lifecycle, registry, review, and
state documents.

Do not create a new role, pipeline, lifecycle stage, mandatory artifact,
database, release state, canon owner, or `/about` authority.

## Why This Shape Fits The Architecture

The current architecture already has the right home:

- `AGENTS.md` names "Editorial learning and Knowledge Evolution" as a
  canonical ownership area.
- `kb/editorial_learning_framework.md` already owns reusable learning,
  canonization criteria, learning extraction, Knowledge Evolution, canon
  evolution, stale-knowledge challenge, and canon retirement.
- `kb/capability_registry.md` already treats learning extraction, canon
  evolution, pattern reuse, and stale-knowledge detection as shared
  capabilities, not standing roles.
- `kb/shared_lifecycle_kernel.md` already has a memory curation stage and
  memory disposition gate.
- `kb/task_object_model.md` already has optional fields for learning
  candidates, canon updates, reusable patterns, deprecated assumptions,
  post-task learning, and memory disposition.
- `review_pipeline.md` and `review_agent.md` already require review challenge
  for learning, canon, stale-knowledge, correction/retirement, and memory-sync
  claims.

Creating a new Knowledge Evolution owner would duplicate existing learning
canon. The better architecture-compatible move is to clarify that Knowledge
Evolution is the deliberate evolution layer of the Learning Framework.

## What Belongs Inside Knowledge Evolution

Knowledge Evolution owns:

- learning disposition from completed tasks, releases, reviews, feedback, and
  repository inspection;
- distinction between task-local observation, candidate, pattern,
  canon-update candidate, accepted canon, superseded/retired guidance, and
  rejected learning;
- criteria for moving temporary observations toward confirmed patterns;
- evidence and traceability expectations for learning promotion;
- owner-first canon update, correction, deprecation, and retirement;
- stale knowledge challenge triggers and recovery paths;
- reuse-driven and review-driven detection of stale or conflicting guidance;
- `/about` synchronization disposition when canonical changes need memory
  export updates, while keeping `/about` non-canonical.

## What Is Already Covered Elsewhere

### Existing Learning Framework

The Learning Framework is the owner. Knowledge Evolution should not replace it.
S3.R6 should update the framework with clearer evolution states, evidence
traceability, stale-knowledge triage, correction/retirement outcomes, and
review integration.

### Project State

`project-state.md` records current phase, completed releases, current focus,
normalization decisions, and active system state. It should mention the release
candidate and compact normalization decision after implementation. It must not
own permanent Knowledge Evolution rules.

### `/about`

`/about` is a ChatGPT project memory package and copied/compact export. It
should be synchronized when canonical docs or compact summaries change. It must
not become a source of canon, promotion, or review authority.

### ROADMAP And BACKLOG

`ROADMAP.md` owns strategic direction. `BACKLOG.md` owns release management.
They should be updated for release status only, not turned into Knowledge
Evolution instruction files.

### Task-Local Retrospectives And Feedback

Task-local notes, `feedback.md`, `final_decision.md`, review findings, and
release reports can carry learning signals. They do not become canon
automatically. They remain evidence or candidates until reviewed against
criteria and owner fit.

### Canonical Ownership Rules

`AGENTS.md` owns rule placement and canonical ownership. Knowledge Evolution
may consume the ownership map but must not create a second ownership map.

## Postponed

- Automated stale-document detection.
- Knowledge health dashboards or scoring.
- New metadata fields in every task artifact.
- A separate decision-record system.
- A dedicated lessons-learned database.
- Domain-specific knowledge packs.
- `/about` automation beyond existing sync validation.
- Machine-assisted trend analysis across all task folders.

These may become future work only if evidence shows the current lightweight
approach is insufficient.

## Rejected Options

| Option | Reason rejected |
| --- | --- |
| New `knowledge_evolution.md` canonical file | Would duplicate the current Learning Framework owner. |
| New role such as Historian, Canon Manager, or Knowledge Curator | Role model is frozen; current roles already wrap learning capabilities. |
| New Knowledge Evolution pipeline | Shared lifecycle and memory curation already provide the stage shape. |
| Mandatory `lessons.md` for every task | Would violate artifact minimalism and create noise. |
| Automatic canon promotion from feedback or release reports | Violates reviewed, owner-first canon evolution. |
| Treat `/about` as a knowledge base | Contradicts the non-canonical memory package boundary. |
| Delete stale guidance by default | Loses traceability and replacement rationale. |

## Implementation Shape

Canonical updates:

- `kb/editorial_learning_framework.md`: add explicit Knowledge Evolution
  capability, disposition states, source-evidence chain, pattern confirmation,
  stale/conflicting knowledge triage, correction/retirement outcomes, and
  `/about` sync disposition.
- `AGENTS.md`: clarify the ownership-map name and entry-discipline selection
  language so Knowledge Evolution is discoverable through the existing owner.
- `kb/capability_registry.md`: name Knowledge Evolution as the shared
  capability cluster and clarify activation/output boundaries.
- `kb/shared_lifecycle_kernel.md`: clarify memory curation as the Knowledge
  Evolution touchpoint without adding a lifecycle stage.
- `kb/task_object_model.md`: clarify existing learning fields as Knowledge
  Evolution views, without adding new required fields.
- Role specs: update Chief Editor, Research Agent, Review Agent, and Final
  Editor references where needed; avoid changing role authority.
- `pipelines/review_pipeline.md`: clarify review challenge for Knowledge
  Evolution disposition and stale/canon claims.
- `kb/00_index.md`: add discoverability if needed.
- `project-state.md`, `ROADMAP.md`, `BACKLOG.md`: update release state after
  implementation.

Non-canonical updates:

- release research artifacts;
- release report;
- release pack;
- task-local release artifacts;
- optional smoke test for Knowledge Evolution activation and non-activation;
- `/about` sync if copied canonical files or compact summaries change.

## Architecture Preservation

This release preserves:

- Task Object shape;
- Capability Registry shape;
- Shared Lifecycle stages;
- Review Gate;
- Role Model;
- existing framework ownership;
- `/about` memory package boundary;
- artifact minimalism;
- deliberate reviewed canon evolution.

## Validation Focus

Review and validation should check:

- no duplicate canonical owner was introduced;
- no new mandatory artifact was introduced;
- canon promotion remains reviewed and owner-first;
- stale knowledge handling includes correction, retirement, and deferral
  without silent deletion;
- task-local learning remains task-local by default;
- `/about` remains non-canonical and is synchronized if required;
- validation scripts pass.
