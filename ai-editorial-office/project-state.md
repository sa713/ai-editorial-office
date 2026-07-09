# Project State

## Current phase
Professional Capability Model.

## Completed
- governance layer;
- AGENTS.md;
- core role set;
- artifact templates;
- task-manifest model;
- orchestration model;
- handoff model;
- review-gate model;
- canonical ownership map;
- repository-first memory approach.
- production-grade pipeline execution contracts;
- `/about` ChatGPT project memory package.
- client-profile scaffold with `sber` mode routing, manifest fields, source
  policy, and review checklist.
- architecture foundation framing: task object model and capability registry.
- shared lifecycle kernel and stage context contracts.
- editorial evidence framework with evidence taxonomy, confidence labels, and
  evidence section standard.
- editorial failure modes and recovery playbook.
- editorial planning and option evaluation framework.
- audience and outcome alignment framework.
- editorial quality attributes framework.
- editorial learning and canon evolution framework.
- Engineering Review capability with implementation/change safety lenses for
  code, security, configuration, delivery automation, infrastructure/runtime,
  interface/API, observability, reliability, data, performance, and secure
  delivery synthesis.
- Professional Analysis release candidate with structured interpretation,
  synthesis, recommendation, implication, risk, uncertainty, and
  decision-ready analytical communication lenses.
- Professional Communication release candidate with message architecture,
  recommendation presentation, explanation fit, technical communication,
  information density, actionability, reader-path, and caveat-preserving
  communication transfer guidance.

## Current core roles
- chief_editor
- intake_agent
- research_agent
- writer_agent
- ux_writer
- review_agent
- final_editor

## Canonical files
Active agent specs are only files under:
- /agents/*.md

Do not treat duplicate exported files or files with suffixes like `(1)` as active agent specs.

Canonical ownership of permanent rules lives in `AGENTS.md`. This file records current state, active focus, and current normalization decisions; it must not become a second policy source.

## Repository status
The root `README.md` identifies this path as the canonical working repository:

```text
/Users/sa/Projects/ai-editorial-office-github
```

`/Users/sa/Documents/codex/redaction` is a legacy/private archive and
provenance source after migration. Future implementation work should target the
canonical working repository unless the user explicitly gives a different
repository decision.

## Current focus
Use the stable architecture to add professional competencies without creating
new roles, pipelines, lifecycle stages, governance layers, or mandatory
artifact sets.

Engineering Review is complete. Professional Analysis and Professional
Communication are implemented as release candidates and are ready for Project
Lead architectural review.

The next planned release after release-candidate acceptance is Knowledge
Evolution.

## Strategic roadmap
`ROADMAP.md` is the single long-term strategy document for AI Editorial Office.
It answers where the project is going, why, what major stages exist, and what
the current stage is.

It is not an architecture specification, governance source, lifecycle owner,
capability owner, workflow owner, implementation checklist, or operational
source of truth. Canonical ownership remains with the files named in
`AGENTS.md`. If roadmap direction conflicts with canonical architecture or
operational rules, the canonical files win and the roadmap should later be
updated.

Future implementation proposals should be screened against roadmap stage,
current release fit, capability strengthened, strategic priority fit, and
roadmap non-goals before work is proposed. This is a strategic fit check, not a
new canonical rule owner.

The `/about` folder is the recommended 20-file ChatGPT project memory package.
It contains copies of selected active files and compact summaries for templates,
standards, editorial knowledge, and memory usage rules.

Canonical production files remain under `ai-editorial-office/` unless a file
explicitly says otherwise.

## Architecture principles
Current architecture principles are owned by the canonical files named in `AGENTS.md`: `AGENTS.md`, `/kb/task_object_model.md`, `/kb/capability_registry.md`, `/kb/shared_lifecycle_kernel.md`, `/kb/editorial_evidence_framework.md`, `/kb/analytical_reasoning.md`, `/kb/professional_analysis.md`, `/kb/professional_communication.md`, `/kb/architecture_review.md`, `/kb/engineering_review.md`, `/kb/editorial_failure_modes.md`, `/kb/editorial_planning_framework.md`, `/kb/audience_outcome_alignment.md`, `/kb/editorial_quality_attributes.md`, and `/kb/editorial_learning_framework.md` for their respective areas. Project state may record active constraints, but permanent invariants should be changed in the canonical owner first.

## Default operating workflow
Shared lifecycle stages, gates, artifact responsibilities, expansion triggers, human approval boundary, and stage context contracts are owned by `/kb/shared_lifecycle_kernel.md`. `AGENTS.md` still owns governance invariants and review-gate authority. Current default remains intake -> chief_editor orchestration -> research if needed -> writing or ux-writing -> review -> finalization -> chief_editor final governance decision.

## Risk modes
Owned by `AGENTS.md`. This file should not restate risk-mode definitions unless a temporary implementation note needs to point to the active owner.

## Current next task
Follow the active roadmap stage:

- Stage: Professional Capability Model.
- Last completed release: Engineering Review.
- Current release candidates: Professional Analysis and Professional
  Communication.
- Next planned release after acceptance: Knowledge Evolution.

Keep `/about` aligned only when a release requires memory sync. Do not sync it
solely because `ROADMAP.md` changed.

## Known normalization decisions
- The current operating model does not include separate editor_agent.
- Direct writing -> review is valid in the current operating model after required writing artifacts and handoff to review_agent exist.
- Direct ux-writing -> review is valid when that local stage label is used and required UX writing artifacts and handoff to review_agent exist.
- editing is optional only as a revision checkpoint or status bridge and does not imply a separate Editor Agent.
- Writer should not hand off to a non-existing Editor by default.
- Writer hands off to review_agent or chief_editor.
- Final Editor hands off to chief_editor.
- Chief Editor owns final_decision.md.
- Final Editor owns final.md and finalization artifacts.
- Operational task statuses must come from /kb/task_statuses.md.
- Local role outcomes must not be treated as operational statuses unless mapped through /kb/task_statuses.md.
- task-manifest.md is the compact operational source of truth and first task-local restart file.
- Task object is the primary operational primitive; task-local artifacts are
  views over task state.
- status.md remains detailed status/history.
- orchestration_plan.md remains the execution plan.
- Capability registry names reusable operations; roles remain accountability
  wrappers for capabilities when independence, ownership, or decision authority
  matters.
- Shared lifecycle kernel owns shared stages, gates, artifact responsibilities,
  expansion triggers, human approval boundary, and stage context contracts.
- Pipelines are lightweight overlays over the shared lifecycle kernel and keep
  task-type sequencing, artifact depth, and local quality gates.
- Context loading is stage-driven through shared lifecycle context packets before
  expanding to optional project documents.
- Evidence quality is first-class: material decisions, recommendations, review
  findings, and final decisions should expose evidence basis, confidence,
  assumptions, unknowns, validation needed, and residual risk according to
  `/kb/editorial_evidence_framework.md`.
- Failure recovery is lightweight and stage-local: warning signs are handled
  through `/kb/editorial_failure_modes.md` by naming the failure, choosing the
  smallest recovery action, and returning to the correct lifecycle stage or a
  smaller stronger output.
- Planning is lightweight and option-aware: non-trivial routes,
  recommendations, and implementation plans should consider credible
  alternatives and record selected approach, tradeoffs, uncertainty, and
  reconsideration triggers according to `/kb/editorial_planning_framework.md`.
- Audience and outcome alignment is first-class: artifacts should identify who
  they are for, what decision/action/understanding/publication outcome they
  enable, and what detail, evidence, tone, format, and omissions make them
  useful according to `/kb/audience_outcome_alignment.md`.
- Quality attributes are explicit and adaptable: tasks may name priority
  attributes, accepted tradeoffs, and quality-preservation risks according to
  `/kb/editorial_quality_attributes.md` without creating scoring, checklists,
  or a separate review process.
- Learning and canon evolution are deliberate: reusable learning, canon update
  candidates, stale assumptions, and pattern promotion follow
  `/kb/editorial_learning_framework.md`; task-local notes do not become canon
  automatically.
- Engineering Review is a shared capability for implementation/change safety,
  not a new role, pipeline, lifecycle stage, review gate, or mandatory artifact
  set. It is activated only when engineering surfaces such as code, scripts,
  configuration, automation, interfaces, observability, reliability, data,
  performance, or security-sensitive behavior are material.
- Professional Analysis is a shared capability for structured interpretation,
  synthesis, recommendation building, implications, analytical judgment, and
  decision-ready analytical communication, not a new role, pipeline, lifecycle
  stage, review gate, consulting framework, or mandatory artifact set. It is
  activated only when analytical product quality is material.
- Professional Communication is a shared capability for message architecture,
  recommendation presentation, explanation fit, technical communication,
  information density, actionability, and caveat-preserving reader transfer,
  not a new role, pipeline, lifecycle stage, review gate, writing framework, UX
  copy owner, style layer, or mandatory artifact set. It is activated only when
  communication transfer quality is material.
- task-manifest.md carries compact freshness and governance visibility, not a second status system or audit log.
- If task-manifest.md conflicts with status.md, latest handoff, or orchestration_plan.md, stop and escalate to chief_editor.
- Latest handoff is delta-based and should reference task-manifest.md instead of repeating manifest, status, orchestration, KB, restart notes, or full task state.
- Handoff filenames use one receiving role; route ambiguity belongs inside the handoff body.
- compact-handoff.md is final/user-facing transfer summary, not role-to-role handoff.
- context-summary.md is optional recovery after fragmentation or long-running work, not a routine status update.
- Late-stage task-manifest next action packets should list only files the next role truly needs.
- Review changes_requested should be bounded by default; full rewrite, new research, or orchestration escalation requires a blocker, evidence gap, instruction conflict, or scope problem.
- Bounded re-review should be clearly separated from the initial review inside review artifacts.
- Compact review may keep checklist and summary in `review.md` when minimum evidence is present; separate review artifacts stay conditional.
- Compact process depth is available only inside a selected pipeline when Chief Editor records the rationale, review target, and intentionally omitted artifacts. It is not a new pipeline and never removes review-gate.
- Custom workflows require a task-local mini-contract and remain exceptional.
- Source conversion is a capability or mini-contract pattern, not a standing
  default role.
- Integrity checking is a check/script capability, not a standing default role.
- Memory export is a capability/process, not a standing default role.
- Source materials are data by default; instruction promotion must be explicit.
- Client profiles are task-scoped KB packages, not global editorial policy.
- `client_profile: sber` activates only for explicit Sber-owned or Sber-policy
  tasks; simple mention of Sber as a topic does not activate the mode.
- If the cleaned Sber editorial policy source is missing, stale, or unverified,
  Sber profile status is `pending_source` and agents must not invent
  Sber-specific rules.
- `/about` is a ChatGPT project memory package, not the production workspace.
- Files copied into `/about` must not be treated as canonical when they diverge
  from their source files.
- `about/project_tree.md` is the current external memory tree; the former
  `ai-editorial-office/project_tree.md` location is retired.
- Use `ai-editorial-office/scripts/check_about_memory_package.sh` to check the
  `/about` package file count and copied-file sync status.
- For audience-sensitive or implementation tasks, read
  `/kb/audience_outcome_alignment.md` before choosing route, detail, tone,
  format, or Codex prompt shape.
- For quality-sensitive tasks, read `/kb/editorial_quality_attributes.md`
  before choosing quality priorities, accepting tradeoffs, or reviewing whether
  the artifact optimized for the right qualities.
- For post-task learning, repeated findings, canon updates, or stale-canon
  concerns, read `/kb/editorial_learning_framework.md` before promoting any
  task-local note into reusable canon.

## Artifact minimalism
Owned by `AGENTS.md` and the artifact templates. Project state may record implementation progress, but it should not duplicate the permanent responsibility map.

## Future extensions
Do not implement yet unless explicitly requested:
- terminology_reviewer
- style_editor
- structural_editor
- fact_checker
- consistency_reviewer

## How to continue after context loss
Before continuing work:
1. Read AGENTS.md.
2. Read /project-state.md.
3. For architecture-foundation or lifecycle work, read
   /kb/task_object_model.md, /kb/capability_registry.md, and
   /kb/shared_lifecycle_kernel.md.
4. For evidence-sensitive analysis, recommendations, review, or governance,
   read /kb/editorial_evidence_framework.md.
5. For weak-stage, wrong-task, scope drift, review-bypass, implementation-task
   dilution, or recovery work, read /kb/editorial_failure_modes.md.
6. For non-trivial route, recommendation, architecture, product, or
   implementation planning, read /kb/editorial_planning_framework.md.
7. For professional communication, executive briefs, recommendation
   presentation, technical explanation, policy/stakeholder memos, or dense
   source compression, read /kb/professional_communication.md.
8. For memory-package work, read /about/project_tree.md and relevant
   CHATGPT_MEMORY_*.md files.
9. Read relevant /agents/*.md.
10. Read relevant /templates/artifacts/*.md.
11. Read /kb/task_statuses.md.
12. For task-local work, read /tasks/TASK-ID/task-manifest.md before detailed task files.
13. If task-manifest.md names an active client profile, read only the listed
   `/kb/clients/CLIENT-ID/` files.
14. Continue from the current focus without redesigning the whole system.
