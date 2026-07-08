# AI Editorial Office Roadmap

Status: strategic roadmap
Last updated: 2026-07-08
Scope: long-term evolution of `ai-editorial-office/`
Source basis: the consolidated roadmap/backlog content in
`ideas/master_backlog.md` v0.3, plus the project lead direction that the
roadmap is now the primary strategic document for project evolution.

## Role of This Document

This roadmap is the strategic document for AI Editorial Office evolution. It
guides long-term direction, prioritization, sequencing, and architectural
direction.

It is not a canonical owner of operational rules. It does not replace
`AGENTS.md`, role specs, pipelines, lifecycle rules, the capability registry,
review-gate rules, framework boundaries, templates, or task-local artifacts.

If this roadmap conflicts with canonical architecture or operational rules, the
canonical files win. The roadmap should then be updated later to match the
canonical system.

## Strategic Context

The project has reached architectural stability. Future evolution should no
longer be driven by ad hoc ideas. The strategic shift is:

```text
from "add more roles and documents"
to "minimal task pack -> compact execution -> reviewable diff -> mandatory review"
```

The active system should become more compact, verifiable, reproducible, and
resistant to scope drift while preserving quality, traceability, review, and
restartability.

## Stable Foundation

The safe core already includes:

- the core role set: `chief_editor`, `intake_agent`, `research_agent`,
  `writer_agent`, `ux_writer`, `review_agent`, and `final_editor`;
- task lifecycle, task manifest, orchestration, handoff, review, finalization,
  and final governance patterns;
- the review gate as a mandatory quality boundary;
- compact execution guidance;
- the `/about` ChatGPT project memory package;
- safe-core publication discipline for GitHub;
- task-scoped client profile support, including `sber` mode;
- lifecycle validation;
- preflight examples and manual trials;
- source/provenance workflow;
- research pipeline hardening;
- task pack generator MVP;
- first sanitized end-to-end cases.

## Progress Snapshot

### Completed

Completed roadmap releases:

- Analytical Reasoning;
- Architecture Review;
- Engineering Review.

Engineering Review is implemented as one shared capability with optional review
lenses. The release preserved the existing architecture and added no new roles
or pipelines.

Completed roadmap phases:

- P0 - Consolidated Planning Baseline;
- P1 - Compare the First Three End-to-End Case Reports;
- P1.5 - Raw Brief Normalization;
- P2 - Codex Task Standard and Check Pack;
- P5 - Task Pack Generator Tuning;
- P5.5 - Customer Feedback Loop.

### Current

Current roadmap block:

- P3 - Lifecycle Validator Growth.

This is the next existing incomplete roadmap block after the Engineering Review
release. It should remain focused on structural safety checks around actual
lifecycle failures.

### Future

Future roadmap blocks remain:

- P4 - Real Low-Risk Compact Execution Trial;
- P6 - Capability Governance Skeleton;
- P7 - Artifact Quality Gates Capability;
- P8 - Reader-Testing Capability;
- P9 - Review-Gate Linter and Source Traceability Checks;
- P10 - Future Roles and Visual Subsystem.

## Evolution Principles

### Do Not Add Layers for Their Own Sake

The next useful path is shorter and more reliable:

```text
normal task definition
-> minimal task pack
-> compact execution
-> reviewable diff
-> review without reading the whole project
```

### Capabilities, Not New Default Roles

Capability ideas should be adopted as narrow, explicitly activated helpers with
clear boundaries, risks, evals, and review. They should not become default
roles, new governance layers, or shortcuts around the selected pipeline.

Useful capability adoption properties:

- narrow purpose;
- explicit activation;
- when-to-use and when-not-to-use boundaries;
- forbidden actions;
- progressive disclosure;
- activation contract;
- eval scenarios;
- review before controlled adoption.

### Markdown Remains Canonical

Scripts, validators, and capabilities may help the system work, but canonical
rules remain in the markdown files named by `AGENTS.md` and the canonical
ownership map.

### External Artifacts Require QA

DOCX, PDF, PPTX, XLSX, and other external artifacts are not ready until they
have passed visual or structural checks appropriate to the artifact type. This
is a future candidate for a practical capability, not a default behavior for
ordinary markdown tasks.

### Token Economy Is Task Discipline

The main context loss risk is vague task definition. Future Codex work should
remain shaped around:

```text
goal -> boundaries -> source of truth -> files -> prohibitions
-> acceptance criteria -> check pack
```

## Strategic Non-Goals

For the current roadmap horizon, do not pursue:

- new default roles;
- large pipeline refactors;
- mandatory capability packs;
- automated preflight checking unless repeated routing failures justify it;
- the visual subsystem as a production default;
- external artifact generation as default editorial behavior;
- wholesale transfer of ideas from skills repositories;
- new mandatory artifacts for architectural tidiness alone;
- rewriting the whole safe core for one local problem.

This roadmap also must not be used as:

- an architecture specification;
- governance;
- lifecycle owner;
- capability owner;
- workflow owner;
- implementation checklist;
- source of operational truth.

## Roadmap Phases

The `P*` labels below are the roadmap phases to use for strategic fit checks.
They preserve the priority sequence from the consolidated project roadmap.

### P0 - Consolidated Planning Baseline

Status: completed / strategic role updated by this document.

Strategic capability strengthened: planning continuity and backlog discipline.

The earlier development roadmap, skills roadmap, and token economy improvement
notes were consolidated into `ideas/master_backlog.md`. That file remains the
active backlog and retrospective planning artifact. This `ROADMAP.md` now
serves as the long-term strategic document, while the backlog remains useful
for implementation history and candidate work.

Boundary: the backlog and this roadmap do not override production files.

### P1 - Compare the First Three End-to-End Case Reports

Status: implemented / fix identified.

Strategic capability strengthened: real-case validation of compact execution,
source/provenance handling, evidence modes, routing, and review-gate behavior.

The first sanitized cases showed that:

- security-adjacent work should use `constrain`, not automatic `proceed`;
- clear internal feedback can use `proceed` when the raw brief is sufficient;
- source-bound tasks can use compact evidence when task-local source summaries
  are explicit;
- missing handoff warnings in compact task packs are not currently blockers;
- no large refactor, new role, new mandatory artifact, review-gate change, or
  validator change is required from this phase.

The identified follow-up was to improve task pack generation for declared
task-local evidence summaries. That follow-up is covered in P5.

### P1.5 - Raw Brief Normalization

Status: implemented / validated.

Strategic capability strengthened: converting natural-language user requests
into usable task definitions without manual prompt translation.

The system now distinguishes task signal, background context, noise, facts,
assumptions, questions, and unknowns. Source status must be made explicit
before source-dependent production. Manual validation covered noisy,
incomplete, external-source, source-bound, and management-request scenarios.

Boundary: normalization must not invent goals, sources, requirements, or client
profile activation.

### P2 - Codex Task Standard and Check Pack

Status: implemented.

Strategic capability strengthened: repository-aware implementation readiness
and reviewability for future Codex work.

The system has a compact standard for turning normalized briefs into Codex
tasks and check packs. The intended chain is:

```text
raw request -> normalized brief -> Codex task
-> implementation -> check pack -> review
```

The standard is meant to reduce unnecessary repo reading, prevent scope drift,
make validation explicit, and make review easier.

Boundary: the task standard must not invent requirements, files,
implementation strategy, roles, pipelines, validators, capabilities, or review
outcomes.

### P3 - Lifecycle Validator Growth

Status: current / in progress.

Strategic capability strengthened: structural safety checks around actual
lifecycle failures.

Candidate directions:

- handoff validator;
- deeper finalization-gate checks;
- `client_profile` consistency;
- `final_decision.md` ownership and stage checks;
- source metadata checker;
- forbidden pattern scanner;
- claim coverage checker;
- retrospective metrics collector.

Boundary: validators should catch structural errors without turning low-risk
tasks into bureaucracy.

### P4 - Real Low-Risk Compact Execution Trial

Status: planned.

Strategic capability strengthened: proof that compact execution works on real
low-risk work, not only synthetic examples.

The trial should check whether compact execution:

- avoids unnecessary files;
- preserves restartability;
- keeps the review gate intact;
- remains easy for ChatGPT or another reviewer to inspect;
- can rely on `task-manifest.md`, `status.md`, the working artifact, and
  `review.md` without a separate handoff when compact conditions justify it.

### P5 - Task Pack Generator Tuning

Status: implemented.

Strategic capability strengthened: compact, explicit context assembly for
writer and review roles.

The generator now includes declared task-local source/evidence artifacts such
as `source_summary.md`, `source_notes.md`, or equivalents in writer and review
read sets for source-based compact-evidence tasks. It also shows source status
explicitly, avoids adding source files for no-research tasks, preserves the
client-profile guard, and does not use latest modified time as source of truth.

### P5.5 - Customer Feedback Loop

Status: implemented.

Strategic capability strengthened: controlled handling of post-result feedback
without turning every reaction into a system rule.

Feedback is classified as:

- `task_local`;
- `preference`;
- `observation`;
- `confirmed_pattern`;
- `system_change_candidate`.

Boundary:

- one feedback item does not automatically change the system;
- preferences remain task/customer-scoped unless later promoted through the
  proper reviewed path;
- watchlist and backlog entries are decision-gated;
- feedback does not bypass review or governance.

### P6 - Capability Governance Skeleton

Status: proposal / planned after P1-P5.

Strategic capability strengthened: controlled adoption of optional capability
helpers without new roles.

Minimum proposed shape:

```text
kb/capability_governance.md
templates/capability-card.md
```

Candidate governance properties:

- no capability may override `AGENTS.md`, the selected pipeline, role
  separation, or review-gate rules;
- activation must be explicit;
- each capability has an owner from existing roles;
- each capability has when-to-use and when-not-to-use boundaries;
- each capability has an activation contract;
- progressive disclosure prevents unused details from loading by default;
- risks, forbidden actions, and eval scenarios are visible;
- capabilities remain optional helpers.

### P7 - Artifact Quality Gates Capability

Status: proposal.

Strategic capability strengthened: practical QA for external artifacts.

This is the proposed first real capability because DOCX, PDF, PPTX, XLSX, and
similar outputs carry high layout and structure risk that reasoning alone does
not reliably catch.

Initial candidate shape:

```text
capabilities/artifact-quality-gates/SKILL.md
capabilities/artifact-quality-gates/evals/activation_positive.jsonl
capabilities/artifact-quality-gates/evals/activation_negative.jsonl
```

Boundary: do not make this mandatory for ordinary markdown tasks.

### P8 - Reader-Testing Capability

Status: proposal.

Strategic capability strengthened: independent usability check by a fresh
reader without the conversation context.

Use for:

- important articles;
- strategic documents;
- UX-writing specs;
- client reports;
- decision memos;
- texts where reader misunderstanding is expensive.

The capability should check whether a fresh reader can understand the document
on its own, what it assumes but does not say, where ambiguity remains, where
context is missing, and what feels generic or unsupported.

Boundary: do not make this mandatory for every small task.

### P9 - Review-Gate Linter and Source Traceability Checks

Status: proposal.

Strategic capability strengthened: assistance for Review Agent without
replacing editorial judgment.

Candidate helpers:

- `review-gate-linter`;
- `source-traceability-check`;
- claim coverage checker;
- forbidden pattern scanner.

The preferred direction is to script stable checks while leaving editorial
judgment with Review Agent.

### P10 - Future Roles and Visual Subsystem

Status: defer.

Strategic capability strengthened: preserving experimental knowledge without
turning it into default production behavior.

Decision:

- future roles are not developed yet;
- the visual subsystem is not enabled by default;
- visual tasks remain experimental or isolated;
- return to this area after validators, compact execution, and task pack
  generation are more stable.

Known visual-subsystem problems:

- short requests like "visual notes" did not always trigger the right
  sketchnote pipeline;
- Codex sometimes produced SVG or infographic output instead of a living
  hand-drawn sketchnote;
- the expected final result should be PNG without extra HTML or service files
  unless the user asks otherwise;
- Russian text inside images must be checked for invented content, readability,
  and article fit;
- the visual pipeline must distinguish sketchnote, infographic, meme, comic,
  and presentation visual;
- visual tasks require a visual brief and image prompt, but must not break the
  ordinary editorial task lifecycle.

## Future Work Strategic Fit Check

Before proposing future implementation work, use this roadmap as a strategic
screen:

1. Which roadmap phase does the work belong to?
2. Which roadmap capability does it strengthen?
3. Does it fit the current strategic priorities?
4. Does it violate any roadmap non-goals?

If a proposed task clearly falls outside the roadmap, surface the mismatch
instead of silently implementing it.

This check is a planning aid. It does not make the roadmap an operational rule
owner.

## Maintenance

Update this roadmap when the project lead changes strategy, when roadmap phase
status changes materially, or when completed system work changes the long-term
evolution path.

Keep implementation history, candidates, and retrospective details in
`ideas/master_backlog.md` unless they need to change the strategic roadmap.

Do not sync `/about` only because this roadmap changed unless a separate memory
package update is requested.
