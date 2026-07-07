# Capability Registry

This file defines reusable AI Editorial Office capabilities and how current
roles wrap them when independence, ownership, or decision authority matters.

It is an architecture reference, not a new role system, workflow engine,
pipeline, prompt rewrite, or mandatory artifact set. Active role behavior still
lives in `/agents/*.md`; lifecycle and governance invariants still live in
`AGENTS.md`; task statuses still live in `/kb/task_statuses.md`.

## Core Principle

Capabilities are reusable operations. Roles are accountability wrappers around
capabilities when the system needs ownership, independence, boundary protection,
or governance.

This registry does not create new default agents.

The current core role set remains:

- Chief Editor;
- Intake Agent;
- Research Agent;
- Writer Agent;
- UX Writer;
- Review Agent;
- Final Editor.

The only legalized extension role remains the frozen Artist Agent under the
conditions in `AGENTS.md`.

The following are not current default roles:

- Editor;
- Fact Checker;
- Style Editor;
- Structural Editor;
- Terminology Reviewer;
- Source Converter;
- Context Manager;
- Memory Manager.

Source conversion remains a capability or task-local mini-contract. Integrity
checking remains a check/script capability. Memory export remains a
capability/process.

## Capability Records

### Intake Normalization

- Purpose: turn a raw request into a usable brief, with confirmed, inferred,
  unknown, assumption, and question distinctions when material.
- Typical inputs: user request, existing task folder, supplied source material,
  relevant project state.
- Typical outputs: `brief.md`, intake notes, task id proposal, risk/profile
  suggestion, handoff to Chief Editor.
- Accountability wrapper: Intake Agent; Chief Editor may perform lightweight
  intake for compact tasks.
- Required artifacts: `brief.md` or normalized brief for active tasks.
- Optional artifacts: intake handoff, `open-questions.md` only for real
  blockers/questions.
- Stop conditions: unclear objective, missing critical audience/deliverable,
  source/instruction conflict, unsafe assumptions.
- Quality criteria: task is specific enough for routing; uncertainty is visible;
  no production work starts as a substitute for routing.
- Expansion triggers: high-governance risk, conflicting instructions, unclear
  source boundary, missing critical success criterion.

### Routing And Preflight

- Purpose: choose task type, pipeline/mode/mini-contract, risk mode, process
  depth, active capabilities, active roles, client profile status, and next
  action.
- Typical inputs: `brief.md`, `task-manifest.md`, current user instruction,
  relevant pipeline/mode candidates, client-profile indicators.
- Typical outputs: `orchestration_plan.md`, task-manifest updates, status
  update, Editorial Decision Frame when required, handoff to next role.
- Accountability wrapper: Chief Editor.
- Required artifacts: task-manifest/status updates and routing evidence in an
  existing task artifact.
- Optional artifacts: handoff when the next owner needs delta context.
- Stop conditions: risk mode unknown before production, missing critical input,
  unauthorized extension role, review-bypass request, source/instruction
  conflict.
- Quality criteria: route is deliberate, compact when safe, expanded when
  needed, review gate preserved.
- Expansion triggers: high-governance risk, source-heavy task, client-profile
  uncertainty, human approval complexity, version conflict, reviewer uncertainty.

### Source Boundary Detection

- Purpose: distinguish source data, promoted instruction, assumptions,
  contradictions, and unknowns.
- Typical inputs: user request, source files, drafts, PDFs, notes, web pages,
  task brief.
- Typical outputs: source boundary note in `brief.md`, `orchestration_plan.md`,
  `research.md`, or `sources.md`.
- Accountability wrapper: Intake Agent, Research Agent, or Chief Editor,
  depending on task stage.
- Required artifacts: boundary recorded in an existing task artifact when it
  affects production or review.
- Optional artifacts: `sources.md`, `open-questions.md`.
- Stop conditions: embedded source instruction conflicts with authority,
  required source missing, contradiction affects claims.
- Quality criteria: agents know what may be used as evidence and what must not
  be followed as instruction.
- Expansion triggers: legal/policy/product claims, source conflict, unverified
  client source, publication risk.

### Research/Evidence Classification

- Purpose: collect, verify, classify, and structure evidence for downstream
  writing, UX writing, review, and governance.
- Typical inputs: `brief.md`, source boundary, source materials, relevant KB,
  selected pipeline.
- Typical outputs: `research.md`, `sources.md`, `facts.md`, `claims_table.md`,
  research handoff.
- Accountability wrapper: Research Agent.
- Required artifacts: `research.md` when research is assigned.
- Optional artifacts: `sources.md`, `facts.md`, `claims_table.md`,
  `open-questions.md`, depending on factual sensitivity and traceability.
- Stop conditions: missing/inaccessible required sources, unresolved
  contradictions, unsupported required claims, stale or unverified source.
- Quality criteria: facts, interpretations, assumptions, contradictions, and
  uncertainty are separated; important claims have evidence or caveats.
- Expansion triggers: material factual claims, high-governance risk, conflicting
  sources, reviewer evidence need.

### Source Conversion

- Purpose: extract or convert supplied material without silently changing
  meaning or promoting source instructions.
- Typical inputs: user-supplied PDFs, documents, OCR, copied text, images,
  conversion instructions, source boundary.
- Typical outputs: converted markdown/text/artifact, conversion notes,
  reviewable source coverage evidence.
- Accountability wrapper: task-local mini-contract assigned by Chief Editor to
  a bounded production owner; Review Agent validates conversion. No standing
  Source Converter role exists.
- Required artifacts: mini-contract or routing note; converted artifact;
  `review.md` before final use when editorial workflow is active.
- Optional artifacts: source coverage notes, page/section map, conversion
  checklist when needed.
- Stop conditions: source unreadable, conversion would require interpretation
  beyond scope, missing source coverage, publication-critical accuracy without
  review.
- Quality criteria: conversion preserves source structure and meaning, does not
  invent content, and keeps source/instruction boundary visible.
- Expansion triggers: long/complex source, legal or publication use, tables or
  data, OCR uncertainty, source coverage dispute.

### Editorial Structure Planning

- Purpose: choose a reader-useful structure, angle, mode, and review focus
  before drafting.
- Typical inputs: brief, research/evidence, editorial knowledge, selected
  pipeline, Editorial Decision Frame.
- Typical outputs: outline, structure notes, writing contract, review focus.
- Accountability wrapper: Chief Editor for route/contract; Writer Agent for
  draft structure within approved scope.
- Required artifacts: `orchestration_plan.md` for route; `outline.md` when
  structure is non-trivial or needed for review.
- Optional artifacts: writer notes.
- Stop conditions: unclear reader task, contradictory route assumptions,
  missing research sufficiency.
- Quality criteria: structure follows reader task and evidence, not generic
  format habit.
- Expansion triggers: high-stakes communication, multiple audiences, hybrid
  modes, reviewer uncertainty.

### Drafting

- Purpose: produce article, social, email, or other editorial draft from the
  approved brief, evidence, and route.
- Typical inputs: brief, orchestration plan, research/evidence, active client
  profile, relevant KB, current artifact pointer.
- Typical outputs: `draft.md`, `outline.md` when needed, `writer-notes.md`,
  `claims-used.md` when factual claims require traceability, handoff to Review.
- Accountability wrapper: Writer Agent.
- Required artifacts: draft or pipeline-specific production artifact; review
  handoff or status recommendation.
- Optional artifacts: outline, writer notes, claims-used.
- Stop conditions: missing brief/evidence/client context, unsupported required
  claims, scope drift, review-bypass request.
- Quality criteria: draft serves the brief, uses approved evidence, preserves
  uncertainty, and is ready for independent review.
- Expansion triggers: factual sensitivity, high-governance risk, product claims,
  client-profile complexity, multiple versions.

### UX Writing

- Purpose: produce product-facing copy, interface text, states, and terminology
  under the UX writing pipeline.
- Typical inputs: brief, product context, states/flows, active client profile,
  UX writing guidelines, terminology constraints.
- Typical outputs: `ux-copy.md`, `content-map.md`, `states-table.md`,
  `terminology-notes.md`, `ux-writer-notes.md`, handoff to Review.
- Accountability wrapper: UX Writer.
- Required artifacts: UX copy or pipeline-required UX artifacts.
- Optional artifacts: content map, states table, terminology notes, depending
  on task scope.
- Stop conditions: missing product behavior, unclear state, unsupported policy
  claim, client-profile source issue, review-bypass request.
- Quality criteria: copy is clear, state-aware, consistent, accessible, and
  does not invent product behavior.
- Expansion triggers: product behavior uncertainty, many states, legal/compliance
  wording, client-profile requirements.

### Client-Profile Application

- Purpose: apply task-scoped client constraints when explicitly activated.
- Typical inputs: task manifest/profile status, client profile files, source
  notes, task brief, pipeline.
- Typical outputs: applied terminology/tone/checklist constraints; review
  evidence for client-profile compliance when claimed.
- Accountability wrapper: Chief Editor activates; Writer/UX Writer applies;
  Review Agent checks.
- Required artifacts: `task-manifest.md` or `orchestration_plan.md` with
  `client_profile`, status, files, activation reason, and stop condition.
- Optional artifacts: client-specific notes inside writer/review artifacts.
- Stop conditions: missing/stale/unverified client source, profile not
  explicitly active, user asks to bypass review for client-profile task.
- Quality criteria: client profile stays scoped to the task and never overrides
  lifecycle, roles, facts, review, pipeline, or explicit user/brief constraints.
- Expansion triggers: pending source, external publication, policy compliance
  claim, conflicting client/general rules.

### Independent Review

- Purpose: validate saved artifacts and produce a deterministic verdict.
- Typical inputs: task manifest, brief, orchestration plan, material under
  review, latest handoff, selected pipeline, relevant evidence/client/KB files.
- Typical outputs: `review.md` with verdict, checked scope, independence basis,
  findings, required changes, blockers, and next action.
- Accountability wrapper: Review Agent.
- Required artifacts: `review.md`.
- Optional artifacts: `qa-checklist.md`, `review-summary.md`,
  `reviewer-notes.md` only when justified.
- Stop conditions: missing reviewed artifact, stale version, non-independent
  review, missing required evidence, unresolved blocker, client-profile source
  issue.
- Quality criteria: outcome is `approved`, `changes_requested`, or `blocked`;
  findings are evidence-backed; review does not become rewriting.
- Expansion triggers: high-governance risk, traceability need, evidence dispute,
  reviewer uncertainty, human approval complexity.

### Repair

- Purpose: resolve review findings or blockers without changing scope silently.
- Typical inputs: `review.md`, repair owner handoff, affected artifacts,
  task-manifest/status.
- Typical outputs: revised draft/UX/research/source artifact, repair notes or
  handoff, status update, re-review request.
- Accountability wrapper: Writer Agent, UX Writer, Research Agent, or Chief
  Editor depending on finding type.
- Required artifacts: updated affected artifact and status/handoff evidence.
- Optional artifacts: bounded repair note when not obvious from changes.
- Stop conditions: finding requires scope change, new evidence, new user
  decision, or governance reroute.
- Quality criteria: repair addresses required findings only within approved
  scope and makes re-review target clear.
- Expansion triggers: repeated failure, broad rewrite need, evidence gap,
  instruction conflict, reader outcome failure.

### Controlled Finalization

- Purpose: prepare final deliverable after approved review without adding
  unreviewed meaning.
- Typical inputs: approved `review.md`, reviewed artifact, task manifest, brief,
  selected pipeline, relevant evidence/client constraints.
- Typical outputs: `final.md`, finalization handoff/status recommendation,
  optional finalization notes/checklist when justified.
- Accountability wrapper: Final Editor when controlled transformation is needed;
  compact closure may use approved reviewed artifact when no transformation is
  needed and `AGENTS.md` compact conditions hold.
- Required artifacts: final deliverable when final output exists.
- Optional artifacts: `finalization-notes.md`, `finalization-checklist.md`.
- Stop conditions: missing/stale/non-independent review, changes requested,
  blocked review, new claims or meaning changes needed, unresolved approval.
- Quality criteria: final output stays within reviewed scope and preserves
  caveats, traceability, tone, glossary, and client-profile limits.
- Expansion triggers: high-governance finalization, controlled changes,
  unresolved risk, downstream proof need.

### Governance Closure

- Purpose: decide whether the task is ready, finalized, waiting for human
  approval, blocked, failed, or archived.
- Typical inputs: task manifest, status, review, final artifact, finalization
  evidence, approval constraints, blockers.
- Typical outputs: `final_decision.md`, status update, task-manifest update,
  human approval note when needed.
- Accountability wrapper: Chief Editor.
- Required artifacts: governance evidence in `final_decision.md`, status, or
  manifest according to risk and pipeline.
- Optional artifacts: compact final/user-facing handoff when useful.
- Stop conditions: review absent or not approved, final artifact missing when
  required, human approval unresolved, source/profile conflict.
- Quality criteria: closure is artifact-backed and does not imply publication
  or human approval without evidence.
- Expansion triggers: external delivery, sensitive claims, high-governance mode,
  unresolved human decision.

### Visual Meaning Brief

- Purpose: prepare visual concept/brief only when the frozen visual subsystem is
  explicitly activated under `AGENTS.md`.
- Typical inputs: approved source text, selected visual mode, task route,
  visual prerequisites.
- Typical outputs: `visual_concept.md`, `illustration_brief.md` or
  `sketchnote_brief.md`, optional `image_prompt.md`.
- Accountability wrapper: Chief Editor activates; Artist Agent is the frozen
  extension role only when prerequisites are met.
- Required artifacts: visual concept and mode-specific brief before Artist
  Agent output.
- Optional artifacts: image prompt/image when environment allows.
- Stop conditions: no explicit frozen-subsystem activation, missing approved
  source artifacts, semantic reinterpretation risk.
- Quality criteria: visual branch preserves meaning ownership and does not
  become ordinary editorial work.
- Expansion triggers: complex source, high-risk visual meaning, publication use.

### Memory Curation

- Purpose: decide whether task learning stays local or becomes reusable memory,
  feedback pattern, backlog candidate, or separate system update.
- Typical inputs: final decision, feedback, review findings, repeated patterns,
  retrospectives.
- Typical outputs: `feedback.md`, `kb/feedback_patterns.md` update, backlog
  candidate, or separate reviewed system update.
- Accountability wrapper: Chief Editor for task-local classification; future
  system updates require separate reviewed work.
- Required artifacts: none unless feedback or reusable pattern exists.
- Optional artifacts: feedback/pattern entry.
- Stop conditions: single unverified reaction being treated as policy, stale
  memory, duplicate rule.
- Quality criteria: only future-useful learning is promoted; `/about` remains
  memory export, not canon.
- Expansion triggers: repeated signal, systemic failure, governance change,
  memory-package update.

### Integrity Checking

- Purpose: report likely drift, missing evidence, sync failures, or task-package
  inconsistencies.
- Typical inputs: task folder, `/about` package, templates, scripts, current
  canon.
- Typical outputs: script/report output, validation note, warning list.
- Accountability wrapper: check/script capability; no Integrity Checker role
  exists.
- Required artifacts: none unless a mission/report records validation.
- Optional artifacts: validation report or check-pack.
- Stop conditions: check would modify files automatically, become a rule owner,
  or force legacy task rewrites.
- Quality criteria: checks are read-only unless explicitly implemented as a
  separate reviewed update; failures route to Chief Editor or system task.
- Expansion triggers: release/publication, memory package update, task package
  migration, high-governance closure.

## Current Role To Capability Map

| Role | Wrapped capabilities |
| --- | --- |
| Chief Editor | Routing and preflight; source boundary decision when routing; editorial structure contract; client-profile activation; governance closure; memory curation; mini-contract authorization. |
| Intake Agent | Intake normalization; initial source boundary detection; risk/client-profile suggestion. |
| Research Agent | Research/evidence classification; source boundary detection; evidence repair. |
| Writer Agent | Editorial structure planning within approved route; drafting; repair for draft findings; bounded source-conversion production only when a mini-contract assigns it. |
| UX Writer | UX writing; UX repair; client-profile application for product copy. |
| Review Agent | Independent review; review-side source/client/profile checks; re-review after repair. |
| Final Editor | Controlled finalization when transformation after approved review is needed. |
| Artist Agent | Frozen visual-output extension for explicitly activated visual branch after visual meaning brief prerequisites. |

## Non-Role Capabilities

These capabilities must not be converted into default roles without a separate
reviewed system update:

- source conversion;
- integrity checking;
- memory export;
- context assembly;
- fact checking;
- style editing;
- structural editing;
- terminology review.

They may be performed inside existing roles, scripts, checks, or task-local
mini-contracts when current `AGENTS.md` and selected pipeline rules allow it.
