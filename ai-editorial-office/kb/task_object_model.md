# Task Object Model

This file defines the architectural model for an AI Editorial Office task.

It is a canonical architecture reference for task-object fields and for how
task-local artifacts act as views over task state. It does not change runtime
behavior, task statuses, review-gate rules, compact execution, pipeline
requirements, shared lifecycle rules, or role responsibilities. Shared
lifecycle stages, gates, artifact responsibilities, expansion triggers, human
approval boundary, and stage context contracts live in
`/kb/shared_lifecycle_kernel.md`; evidence taxonomy, confidence labels, and
evidence section standards live in `/kb/editorial_evidence_framework.md`;
analytical reasoning moves, hypothesis comparison, disconfirmation,
contradiction handling, and sufficiency judgment live in
`/kb/analytical_reasoning.md`;
Professional Analysis moves, analytical product shape, structured
interpretation, synthesis, recommendation building, implications, and
decision-ready analytical communication live in `/kb/professional_analysis.md`;
Professional Communication moves, message architecture, recommendation
presentation, explanation fit, technical communication, information density,
actionability, and preservation of evidence and caveats during reader transfer
live in `/kb/professional_communication.md`;
Architecture Review moves, architecture drivers, quality-attribute scenarios,
architectural tradeoffs, architecture risks, and decision-rationale challenge
live in `/kb/architecture_review.md`;
Engineering Review moves, implementation/change safety lenses, engineering
validation expectations, and engineering residual-risk handling live in
`/kb/engineering_review.md`;
planning levels, option evaluation, and recommendation formation live in
`/kb/editorial_planning_framework.md`; audience and outcome alignment fields,
reader fit, and usefulness criteria live in
`/kb/audience_outcome_alignment.md`; quality attributes, quality tradeoffs, and
quality preservation guidance live in `/kb/editorial_quality_attributes.md`;
learning extraction, Knowledge Evolution, canon evolution, stale-knowledge
challenge, canon retirement, and memory disposition live in
`/kb/editorial_learning_framework.md`;
Domain Knowledge Pack purpose, structure, activation, source/evidence
requirements, boundaries, review, update, retirement, and relation to existing
roles and capabilities live in `/kb/domain_knowledge_pack_standard.md`;
runtime authority still remains with `AGENTS.md`, `/kb/task_statuses.md`, the
selected pipeline, role specs, and task-local artifacts.

## Core Principle

The task object is the primary operational primitive of AI Editorial Office.

The system should be understood in this order:

```text
task object first;
capability map second;
roles as accountability wrappers;
workflows and pipelines as execution guidance;
artifacts as views over task state.
```

This is an architecture framing, not a workflow engine. The task object is
represented by markdown artifacts inside `/tasks/TASK-ID/`; it is not a hidden
database, runtime service, automation layer, or replacement for Chief Editor
governance.

## Required Task Object Fields

Every active task should be describable by these fields. A compact task may
record several fields in one artifact, and not every field requires a standalone
file.

| Field | Meaning | Typical owner/view |
| --- | --- | --- |
| `task_id` | Stable task identifier. | `brief.md`, `task-manifest.md`, `status.md` |
| `objective` | What the task must achieve. | `brief.md`, `task-manifest.md` |
| `user_request_summary` | Compact summary of the user's request and any later accepted scope changes. | `brief.md`, `task-manifest.md`, `status.md` |
| `audience` | Intended reader or user. Mark confirmed, inferred, or unknown when material. | `brief.md`, preflight section, `orchestration_plan.md` |
| `intended_outcome` | What the artifact must enable: decision, approval, implementation, review, understanding, alignment, publication, teaching, persuasion, or canon documentation. | `brief.md`, `orchestration_plan.md`, production notes |
| `reader_context` | What the audience already knows, needs, fears, lacks, or must not be burdened with. | `brief.md`, `orchestration_plan.md`, writer/UX notes |
| `required_action_or_decision` | Specific action, decision, approval, challenge, implementation, or next step the reader must be able to take. Optional when the outcome is pure understanding. | `brief.md`, `orchestration_plan.md`, final artifact |
| `format_constraints` | Length, language, medium, structure, copyability, accessibility, or channel constraints that shape usefulness. | `brief.md`, `orchestration_plan.md`, production notes |
| `detail_level` | Compact, standard, deep, or task-specific depth needed by the audience and outcome. | `orchestration_plan.md`, production notes, review artifacts |
| `tone_requirements` | Tone, formality, sensitivity, and vocabulary constraints required by reader context and evidence quality. | `brief.md`, relevant KB, production notes |
| `channel_context` | Publication channel, product context, internal/external use, or task environment. | `brief.md`, `orchestration_plan.md` |
| `deliverable` | Expected output or artifact set. | `brief.md`, `task-manifest.md` |
| `quality_priorities` | Selected quality attributes that matter most for this task, such as correctness, actionability, traceability, audience fit, implementation readiness, or reviewability. | `brief.md`, `orchestration_plan.md`, production/review notes |
| `quality_tradeoffs` | Accepted quality tradeoffs, such as completeness vs brevity or elegance vs implementation value. | `orchestration_plan.md`, Editorial Decision Frame, `review.md` |
| `source_boundary` | What is source data, instruction, assumption, contradiction, or unknown. | `brief.md`, `orchestration_plan.md`, `research.md`, `sources.md` |
| `evidence_basis` | Evidence classes and artifact/source pointers that support material claims, routes, recommendations, review findings, or final decisions. | `orchestration_plan.md`, `research.md`, `sources.md`, `claims_table.md`, `review.md`, `final_decision.md` |
| `confidence_level` | Evidence-quality label for material conclusions: `verified`, `supported`, `plausible`, `speculative`, or `unsupported`. | research/review artifacts, decision frame, final decision |
| `assumptions` | Working assumptions that are not facts and must remain visible when they affect decisions or output. | `brief.md`, `orchestration_plan.md`, writer/UX notes, `review.md` |
| `unknowns` | Missing, stale, contradicted, or uninspected information that may affect safety, quality, or confidence. | `brief.md`, `status.md`, `open-questions.md`, review artifacts |
| `validation_needed` | Evidence that would most reduce uncertainty or unblock a stronger conclusion. | `orchestration_plan.md`, `research.md`, `review.md`, handoff |
| `residual_risk` | Remaining risk after available evidence, assumptions, and validation are considered. | `review.md`, finalization notes, `final_decision.md` |
| `analytical_question` | Optional question the analysis must answer when reasoning complexity, ambiguity, or decision impact is material. | `orchestration_plan.md`, `research.md`, `review.md` |
| `hypotheses_considered` | Optional competing explanations, routes, or causal accounts considered before conclusion. | `orchestration_plan.md`, `research.md`, `review.md` |
| `key_assumptions` | Optional linchpin assumptions that must hold for the conclusion, recommendation, or route to remain valid. | `orchestration_plan.md`, `research.md`, production notes, `review.md` |
| `contradictions` | Optional material source, scope, timing, definition, method, or incentive conflicts that affect analysis. | `research.md`, `status.md`, `review.md` |
| `disconfirmation_checks` | Optional evidence or tests that could weaken or invalidate a conclusion. | `orchestration_plan.md`, `research.md`, `review.md` |
| `sufficiency_judgment` | Optional statement that evidence is enough, not enough, or enough-with-caveat for the current decision risk. | `research.md`, `review.md`, `final_decision.md` |
| `architecture_review_scope` | Optional scope of an architecture-sensitive review: decision, affected boundary, and materiality trigger. | `orchestration_plan.md`, `review.md` |
| `architecture_drivers` | Optional business, user, quality, constraint, lifecycle, integration, risk, or governance drivers shaping an architecture decision. | `orchestration_plan.md`, `research.md`, `review.md` |
| `quality_attribute_scenarios` | Optional scenarios that make material architecture qualities reviewable. | `orchestration_plan.md`, `research.md`, `review.md` |
| `architectural_tradeoffs` | Optional accepted tradeoffs between architecture options, qualities, owners, risks, or future change paths. | `orchestration_plan.md`, production notes, `review.md`, `final_decision.md` |
| `architecture_risks` | Optional architecture-specific risks such as driver mismatch, hidden assumption, weak operability, governance drift, or accepted residual risk. | `research.md`, `review.md`, `final_decision.md` |
| `architectural_assumptions` | Optional assumptions about system shape, owners, interfaces, canon, workload, lifecycle, or future evolution that affect architecture fitness. | `orchestration_plan.md`, `research.md`, `review.md` |
| `success_criterion` | How readiness and audience usefulness will be judged for this task. | `brief.md`, `orchestration_plan.md`, `review.md` |
| `risk_mode` | `low-risk`, `standard`, `high-governance`, or unresolved/blocked until determined. | `task-manifest.md`, `orchestration_plan.md`, `status.md` |
| `process_depth` | `compact`, `normal`, or `full`. | `task-manifest.md`, `orchestration_plan.md` |
| `selected_workflow` | Selected pipeline overlay, editorial mode, or task-local mini-contract. | `orchestration_plan.md`, `task-manifest.md` |
| `planning_level` | `trivial`, `standard`, or `strategic` planning depth selected for meaningful decisions. | `orchestration_plan.md`, `task-manifest.md` |
| `options_considered` | Credible alternatives considered before selecting route, recommendation, or implementation plan. | `orchestration_plan.md`, Editorial Decision Frame, review artifacts |
| `selected_option` | Chosen approach and why it best serves the task now. | `orchestration_plan.md`, Editorial Decision Frame, final decision |
| `tradeoffs_accepted` | Costs, risks, or constraints accepted by choosing the selected option. | `orchestration_plan.md`, review/final decision |
| `reconsideration_triggers` | Conditions that would make a rejected option stronger or require reroute. | Editorial Decision Frame, `review.md`, `final_decision.md` |
| `active_capabilities` | Capabilities selected for the task, from `/kb/capability_registry.md`. | `orchestration_plan.md`, `task-manifest.md` |
| `active_domain_packs` | Optional Domain Knowledge Packs activated because domain context materially affects evidence depth, terminology, risk, review focus, or output quality. | `orchestration_plan.md`, `task-manifest.md`, `research.md`, `review.md`, `final_decision.md` |
| `active_roles` | Current core roles or explicitly legalized extension roles assigned to wrap capabilities. | `orchestration_plan.md`, handoffs, `status.md` |
| `client_profile_status` | Client profile id, status, files, activation reason, and stop condition when applicable. | `task-manifest.md`, `orchestration_plan.md`, review artifacts |
| `current_owner` | Role currently responsible for the next action. | `task-manifest.md`, `status.md`, handoff |
| `current_status` | Operational task status from `/kb/task_statuses.md`. | `status.md`, summarized in `task-manifest.md` |
| `current_artifact_pointer` | Current active artifact or artifact set, especially when versions exist. | `task-manifest.md` or named task-local owner |
| `required_gates` | Gates required by risk, workflow, evidence, review, finalization, governance, or human approval. | `orchestration_plan.md`, `task-manifest.md` |
| `completed_gates` | Gates already passed and where the evidence is stored. | `task-manifest.md`, `status.md`, `review.md`, `final_decision.md` |
| `open_blockers` | Missing data, conflicts, source gaps, approval gaps, or governance blockers. | `status.md`, `task-manifest.md`, `open-questions.md` when justified |
| `review_outcome` | `approved`, `changes_requested`, `blocked`, or not yet reviewed. | `review.md`, `status.md`, `task-manifest.md` |
| `finalization_mode` | No finalization yet, controlled finalization required, compact finalization, or final artifact already reviewed. | `orchestration_plan.md`, `review.md`, `final_decision.md` |
| `human_approval_requirement` | Whether a human decision is required before continuation, publication, delivery, or closure. | `orchestration_plan.md`, `status.md`, `final_decision.md` |
| `next_action` | Smallest safe next action and owner. | `task-manifest.md`, handoff, `status.md` |
| `learning_candidates` | Potential reusable learning discovered during task execution, review, feedback, release work, repository inspection, or governance. Optional and task-local until validated. | `review.md`, `feedback.md`, `final_decision.md`, implementation report |
| `canon_updates_needed` | Candidate canonical changes that require a separate reviewed update or direct owner-file patch. Optional. | `final_decision.md`, `feedback.md`, system task notes |
| `reusable_patterns` | Validated or candidate patterns that may help future similar tasks. Optional. | `feedback.md`, `kb/feedback_patterns.md`, system update artifacts |
| `deprecated_assumptions` | Assumptions, paths, source statuses, patterns, or guidance found stale, superseded, retired, or unsafe. Optional. | `status.md`, `review.md`, `final_decision.md` |
| `post_task_learning` | Compact Knowledge Evolution closure note deciding whether learning stays task-local, becomes feedback/pattern, needs canon update, is stale/conflicting, or is rejected/deferred. Optional. | `final_decision.md`, `feedback.md` |
| `memory_disposition` | Whether task learning stays local, becomes feedback, becomes a pattern, needs `/about` sync, or needs a separate system update. | `feedback.md`, `final_decision.md`, `kb/feedback_patterns.md` |

## Artifact Views Over The Task Object

Artifacts are views over task state. They should not duplicate each other unless
the selected workflow, risk mode, review, restartability, or governance need
requires it.

| Artifact | Task-object responsibility |
| --- | --- |
| `brief.md` | Defines objective, user request summary, audience, intended outcome, reader context when known, channel/context, deliverable, source boundary, constraints, quality cues when material, and success criterion. |
| `task-manifest.md` | Compact current-state view: task id, selected workflow, active capabilities/roles, active Domain Knowledge Packs when material, current owner/status, artifact inventory, current pointer, constraints, gates, review/finalization state, and next action. |
| `status.md` | Transition history, blocker history, rationale for state changes, approvals, and recovery path. It must not become a duplicate manifest. |
| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit when material, quality priorities/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame when required, evidence basis/confidence for material route decisions, and expansion triggers. |
| `research.md` | Research scope, verified facts, interpretations, assumptions, hypotheses, contradictions, diagnostic evidence, source confidence, evidence class, sufficiency judgment, and evidence limits. |
| `sources.md` | Source inventory, provenance, freshness, reliability, relevance, and evidence class. |
| `facts.md` | Fact-level evidence when needed by factual sensitivity, downstream review, or high-governance scope. |
| `claims_table.md` | Claim-level traceability for material claims, high-governance tasks, evidence disputes, or review needs. |
| `outline.md` | Planned structure when structure is non-trivial or needed for review. |
| `draft.md`, `ux-copy.md`, or equivalent production artifact | Current material under production or review, shaped to the recorded audience, outcome, detail, tone, and format constraints. |
| `claims-used.md` | Claims actually used in production artifacts when factual traceability matters. |
| `writer-notes.md` / `ux-writer-notes.md` | Production assumptions, caveats, audience/outcome choices, quality-preservation notes, and review focus that are not already obvious from the draft. |
| `review.md` | Independent confidence gate: reviewed artifacts, independence basis, analytical reasoning challenge when material, Professional Analysis challenge when material, Professional Communication challenge when material, Architecture Review challenge when material, Engineering Review challenge when material, active Domain Knowledge Pack activation/boundary/source challenge when material, audience/outcome fit, quality-attribute fit when material, evidence/confidence challenge, assumptions and unknowns, findings, verdict, required changes, blockers, learning/canon candidates when material, and next action. |
| `qa-checklist.md` | Separate review evidence only when a downstream consumer, high-governance mode, task requirement, blocker, or traceability need justifies it. |
| `review-summary.md` | Separate concise review transfer only when `review.md` and handoff are not enough for the next owner. |
| `final.md` | Final deliverable after approved review or reviewed-final compact closure. |
| `finalization-notes.md` | Controlled finalization decisions only when finalization changes, risks, high governance, or traceability justify it. |
| `finalization-checklist.md` | Finalization proof only when a downstream/governance consumer needs separate evidence. |
| `final_decision.md` | Chief Editor governance closure, final readiness, evidence basis for closure, residual risk, human approval caveat, memory disposition, learning decision when material, or reason for non-closure. |
| `feedback.md` | Optional post-delivery user reaction, task-local feedback signal, or learning candidate. It does not automatically change canon. |
| `handoff-*.md` | Delta transfer between roles: what changed, what the next owner needs, and when to stop. |
| `compact-handoff.md` | Optional final/user-facing transfer summary, not an internal role-to-role handoff. |
| `context-summary.md` | Optional recovery artifact after fragmentation or long-running work, not routine status. |

## Compact And Expanded Use

The task object does not require every artifact to exist.

Compact execution remains valid when current `AGENTS.md` compact conditions hold:

- risk is low or simple standard;
- source and evidence needs are limited;
- review can validate from the compact packet;
- no high-governance or unresolved human approval complexity is present.

Expanded execution remains required when risk, evidence, review, governance,
client-profile source status, contradiction, version conflict, human approval,
or restartability requires more explicit evidence.

The correct question is not "which files can be created?" but "which task
object fields and gates must be visible for the next owner, reviewer, or Chief
Editor to move safely?"

## Gates

Task gates are confidence decisions recorded in existing artifacts. Shared gate
semantics and stage order are owned by `/kb/shared_lifecycle_kernel.md`;
evidence taxonomy and confidence labels are owned by
`/kb/editorial_evidence_framework.md`; planning levels and option evaluation
are owned by `/kb/editorial_planning_framework.md`; analytical reasoning moves
are owned by `/kb/analytical_reasoning.md`; Professional Analysis moves are
owned by `/kb/professional_analysis.md`; Professional Communication moves are
owned by `/kb/professional_communication.md`; Architecture Review moves are owned
by `/kb/architecture_review.md`; Engineering Review moves are owned by
`/kb/engineering_review.md`; audience/outcome alignment is owned by
`/kb/audience_outcome_alignment.md`; quality attributes and tradeoffs are owned
by `/kb/editorial_quality_attributes.md`; Knowledge Evolution, learning, and
canon evolution are owned by `/kb/editorial_learning_framework.md`; Domain
Knowledge Pack activation, boundaries, source/evidence requirements, review,
update, and retirement are owned by `/kb/domain_knowledge_pack_standard.md`;
this file maps those gates to task-object fields and artifact views.

| Gate | Question | Default evidence |
| --- | --- | --- |
| Entry/preflight | Is the task understood enough to ask, constrain, proceed, or block? | `orchestration_plan.md`, `task-manifest.md`, or `status.md` |
| Source boundary | What is source data, instruction, assumption, contradiction, or unknown? | `brief.md`, `research.md`, `sources.md`, plan |
| Research sufficiency | Are material claims supported, caveated, or blocked? | `research.md`, `sources.md`, `facts.md`, `claims_table.md` |
| Draft readiness | Is production within approved scope and evidence? | production artifact, writer/UX notes, handoff |
| Review | Is the artifact approved, changes requested, or blocked? | `review.md` |
| Finalization | Is final output within reviewed scope? | `final.md`, optional finalization notes/checklist |
| Governance closure | Can the task be finalized, archived, or moved to human approval? | `final_decision.md`, `status.md`, `task-manifest.md` |
| Memory disposition | Should learning stay task-local or be promoted through feedback/pattern/system update? | `feedback.md`, final decision, feedback patterns |

## Non-Goals

This model does not:

- add a workflow engine;
- add new default agents;
- make every field a mandatory standalone section;
- make every artifact mandatory;
- change allowed task statuses;
- weaken review;
- remove compact execution;
- promote `/about` to canon;
- treat old task folders as templates;
- create mandatory domain pack artifacts for ordinary tasks;
- treat Domain Knowledge Packs as roles, pipelines, lifecycle stages, policy
  owners, capability owners, review gates, or task status models;
- replace role specs or selected pipelines.
