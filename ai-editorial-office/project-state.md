# Project State

## Current phase
Stage 4 - Domain Expertise is complete. Stage 5 - Editorial Intelligence is
active. S5.R1 - Feedback and Learning Intelligence, S5.R2 - Evaluation
Signals, S5.R3 - Memory Hygiene Intelligence, and S5.R4 - Task Need
Recognition are accepted. S5.R5 - Editorial Intelligence Acceptance is a
Release Candidate in Project Lead review.

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
- Knowledge Evolution release candidate with deliberate learning disposition,
  source-evidence chains, pattern confirmation, stale/conflicting knowledge
  challenge, canon correction/retirement, and `/about` memory disposition
  guidance.
- Accepted Feedback and Learning Intelligence release with a bounded bridge
  from existing customer-feedback classification to existing Knowledge
  Evolution disposition, evidence/applicability checks, owner-scoped action,
  rejection/deferral, and actual Domain Pack use-effect capture.
- Accepted Evaluation Signals release with an optional advisory view over
  saved capability activation, Domain Pack effect, review, architecture,
  evidence, learning, stale-knowledge, release, and maintenance observations;
  it preserves comparison context, contradictions, confidence, current owners,
  and explicit non-decision without scores, KPIs, rankings, dashboards, or
  automatic governance.
- Accepted Memory Hygiene Intelligence release with a source-first manual
  disposition flow for external memory; exact-copy and compact-summary
  branches; sync/no-sync, correction, compression, omission, deferral, and
  retirement; stale/contradictory memory repair; bounded growth; independent
  review; and advisory-only checks without automatic writes or canonical
  override.
- Accepted Task Need Recognition release with an evidence-first advisory view
  of likely task type, capabilities, Domain Packs, research/evidence and review
  needs, architecture/engineering/communication significance, ambiguity,
  decomposition, uncertainty, and negative evidence; Chief Editor retains all
  routing, activation, depth, and governance decisions.
- Editorial Intelligence Acceptance implementation in progress with a conditional
  Release Pack contract that requires both value and restraint, distinguishes
  synthetic from real-use evidence, tests human authority, automation,
  architecture and maintenance cost, reversibility, hidden governance,
  uncertainty, and cross-effects, and supplies human dispositions without
  scores or automatic decisions.
- Accepted Domain Knowledge Pack Standard with pack purpose,
  structure, activation, source/evidence requirements, boundaries, forbidden
  content, review, update, retirement, and `/about` boundary guidance.
- Accepted Software Architecture Domain Pack with source-backed
  architecture decision, driver, quality-attribute, style, pattern, boundary,
  coupling, tradeoff, risk, evidence, activation, update, and retirement
  guidance.
- Accepted DevSecOps Domain Pack with source-backed secure delivery,
  CI/CD, automation, configuration, supply-chain risk, deployment-boundary,
  validation-evidence, and operational-security guidance.
- Accepted Cybersecurity Domain Pack with source-backed
  cybersecurity context for security-sensitive analysis, threat understanding,
  defensive recommendations, secure design, control and mitigation framing,
  assurance evidence, residual-risk interpretation, and safety-aware review
  context.
- Accepted AI Engineering Domain Pack with source-backed context for
  AI-enabled system boundaries, model/provider fit, prompts and instructions,
  structured outputs, RAG, data quality, evaluation, reliability and
  monitoring, human oversight, defensive safety, tool/agentic workflows, and
  AI-assisted engineering.

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
Stage 4 is fully closed after Project Lead acceptance. Preserve its stable,
source-backed domain knowledge layer while Stage 5 continues with S5.R1
through S5.R4 accepted and the S5.R5 Release Candidate in review.

Engineering Review and Professional Communication are complete. Professional
Analysis remains an open release candidate. Knowledge Evolution is complete.

S4.R1 through S4.R5 are accepted and complete. Stage 4 is complete. Stage 5 is
active. S5.R1 through S5.R4 are accepted and `Done`; S5.R5 is the current
release in `Review`. Stage 5 is not closed.

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
Current architecture principles are owned by the canonical files named in `AGENTS.md`: `AGENTS.md`, `/kb/task_object_model.md`, `/kb/capability_registry.md`, `/kb/shared_lifecycle_kernel.md`, `/kb/editorial_evidence_framework.md`, `/kb/analytical_reasoning.md`, `/kb/professional_analysis.md`, `/kb/professional_communication.md`, `/kb/architecture_review.md`, `/kb/engineering_review.md`, `/kb/task_need_recognition.md`, `/kb/editorial_failure_modes.md`, `/kb/editorial_planning_framework.md`, `/kb/audience_outcome_alignment.md`, `/kb/editorial_quality_attributes.md`, `/kb/editorial_learning_framework.md`, `/kb/domain_knowledge_pack_standard.md`, and the accepted Domain Knowledge Packs for their respective areas. Project state may record active constraints, but permanent invariants should be changed in the canonical owner first.

## Default operating workflow
Shared lifecycle stages, gates, artifact responsibilities, expansion triggers, human approval boundary, and stage context contracts are owned by `/kb/shared_lifecycle_kernel.md`. `AGENTS.md` still owns governance invariants and review-gate authority. Current default remains intake -> chief_editor orchestration -> research if needed -> writing or ux-writing -> review -> finalization -> chief_editor final governance decision.

## Risk modes
Owned by `AGENTS.md`. This file should not restate risk-mode definitions unless a temporary implementation note needs to point to the active owner.

## Current next task
Follow the active roadmap stage:

- Stage: Stage 5 - Editorial Intelligence, active.
- Last completed stage: Stage 4 - Domain Expertise.
- Last completed release: S5.R4 - Task Need Recognition.
- Open release candidates: Professional Analysis and S5.R5 Editorial
  Intelligence Acceptance.
- Current next action: Project Lead reviews the S5.R5 Release Candidate; do not
  record acceptance, close Stage 5, or start a future stage automatically.
- Stage 5 status: active; S5.R1 through S5.R4 `Done`; S5.R5 `Review`.

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
- Task Need Recognition is an evidence-first advisory capability that may
  recommend likely task type, capabilities, Domain Packs, evidence/research and
  review needs, significance, ambiguity, decomposition, and uncertainty. It
  does not route, activate, select depth, plan, or replace Chief Editor.
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
- Learning and Knowledge Evolution are deliberate: reusable learning, pattern
  candidates, canon-update candidates, stale/conflicting knowledge,
  correction/retirement, and `/about` memory disposition follow
  `/kb/editorial_learning_framework.md`; task-local notes do not become canon
  automatically.
- Feedback and Learning Intelligence reuses two existing owners: actual post-
  delivery feedback classification stays in `/kb/customer_feedback_loop.md`,
  while reusable learning disposition stays in
  `/kb/editorial_learning_framework.md`. Feedback classification and learning
  disposition are linked but distinct; future-use claims need saved evidence,
  affected area, applicability, contradictions, an existing owner, bounded
  action, review, and explicit non-promotion.
- Domain Pack activation is not proof of value. When actual use materially
  affects a result, existing task artifacts may record sections/sources used,
  observed benefit or burden, evidence/confidence, unnecessary complexity, and
  learning disposition. Effect capture is conditional and never changes a pack
  automatically.
- Evaluation Signals are optional advisory views over saved evidence, not a new
  capability, framework, store, dashboard, telemetry layer, role, pipeline,
  lifecycle stage, review gate, status, score, KPI, ranking, target, maturity
  level, or mandatory artifact. Chief Editor may assemble a material view;
  Review Agent challenges evidence, comparison, missing cases, contradictions,
  confidence, proportionality, and non-decision; Project Lead or the existing
  canonical owner remains the decision authority. Counts never prove value,
  acceptance, priority, retirement, or system improvement.
- Editorial Intelligence Acceptance is a conditional section of the existing
  Release Pack standard for Stage 5 intelligence and explicitly scoped future
  self-improvement releases. An accept recommendation requires evidence for
  both value and restraint; synthetic evidence cannot prove operational
  improvement; Project Lead remains the only acceptance authority. The
  contract adds no new owner, workflow, role, pipeline, lifecycle stage, review
  gate, status, board, dashboard, score, threshold, or automatic disposition.
- Memory Hygiene Intelligence is a bounded refinement of existing Knowledge
  Evolution, Memory Curation, stale-knowledge, and Integrity Checking behavior.
  A canonical change or saved drift signal receives a source/materiality/
  purpose/sensitivity/value check and one of `exact-copy`, `compact-summary`,
  `correct`, `compress`, `retire`, `omit`, `defer`, or `no-sync`. Exact copies
  use byte validation; summaries use independent semantic review. Repository
  canon remains authoritative, `/about` remains a derived 20-file package, and
  no checker, Evaluation Signal, or other automation writes memory, changes
  canon, selects disposition, or records acceptance.
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
- Domain Knowledge Packs are source-backed context packages, not roles,
  pipelines, lifecycle stages, review gates, policy owners, capability owners,
  task status models, client profiles, mandatory ordinary task artifacts, or
  automatic canon-promotion paths. They activate only when domain context
  materially affects evidence depth, terminology, risk, review focus, or output
  quality.
- Software Architecture Domain Pack is an accepted, active Domain Knowledge
  Pack for architecture-sensitive tasks. It provides source-backed context for
  architectural decisions, drivers, quality attributes, styles, patterns,
  boundaries, coupling, tradeoffs, risks, evidence, and review questions. It
  does not own Architecture Review, Engineering Review, roles, pipelines,
  policies, review outcomes, task statuses, or mandatory artifacts.
- DevSecOps Domain Pack is an accepted, active Domain Knowledge Pack for
  secure delivery, CI/CD, automation, configuration, supply-chain risk,
  deployment boundaries, validation evidence, and operational-security
  assumptions. It provides source-backed context and review questions while
  supporting Engineering Review without owning Engineering Review, roles,
  pipelines, policies, review outcomes, task statuses, or mandatory artifacts.
- Cybersecurity Domain Pack is an accepted, active Domain Knowledge Pack for
  security-sensitive analysis, threat understanding, defensive
  recommendations, secure design, control and mitigation framing, assurance
  evidence, residual-risk interpretation, and safety-aware review context. It
  provides source-backed context and review questions while supporting
  Engineering Review, Architecture Review, Professional Analysis, and
  Professional Communication without owning those capabilities, cybersecurity
  policy, security approval, incident response, roles, pipelines, review
  outcomes, task statuses, or mandatory artifacts.
- AI Engineering Domain Pack is an accepted, active Domain Knowledge Pack for
  AI-enabled system boundaries, model/provider fit, prompts and instructions,
  structured outputs, RAG, data quality, evaluation, reliability and
  monitoring, human oversight, defensive safety, tool/agentic workflows, and
  AI-assisted engineering. It supplies source-backed context and review
  questions without owning Engineering Review, Cybersecurity, DevSecOps,
  Software Architecture, Professional Analysis, roles, pipelines, policies,
  approval, review outcomes, task statuses, or mandatory artifacts.
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
- For post-task learning, repeated findings, canon updates, or stale-knowledge
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
