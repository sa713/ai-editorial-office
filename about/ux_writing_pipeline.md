# UX Writing Pipeline

## pipeline purpose

This pipeline governs creation, validation, finalization, and governance of product-facing interface copy:

- UX/UI texts;
- microcopy;
- onboarding copy;
- labels;
- helper text;
- empty states;
- validation messages;
- error messages;
- notifications;
- product-facing interface copy.

The pipeline turns a product-language task into reviewed UX copy through controlled intake, Chief Editor orchestration, optional research, UX writing, independent review, finalization, and Chief Editor final governance decision.

The pipeline is markdown-first, artifact-backed, deterministic, and restartable from `/tasks/TASK-ID/` without chat history.

## when to use

Use this pipeline when the requested output is product-facing copy that appears in or around an interface, product flow, onboarding path, notification, validation state, or user guidance surface.

Use it when:

- UI states, flows, labels, helper text, errors, or notifications need to be created or revised;
- product terminology, tone, clarity, accessibility, or cognitive load matter;
- copy may imply product behavior or feature availability;
- missing states or unclear flows need to be documented;
- factual or product claims need source-backed product context;
- UX copy needs independent review before finalization, release, publication, or delivery.

## when not to use

Do not use this pipeline when:

- the task is a long-form article, explainer, analysis, or knowledge content;
- the task is only research and no UX copy is required;
- the task is only review of existing material without new UX writing;
- the task is social-only or marketing-only copy not tied to interface states;
- the task is finalization after an already approved review, unless Chief Editor selects this pipeline as governing context;
- the task can be completed as non-factual formatting or file cleanup;
- the request would require bypassing review, product clarification, finalization, or governance rules.

If the task mixes article copy and UX copy, Chief Editor must record the selected pipeline and scope boundaries in `/tasks/TASK-ID/orchestration_plan.md`.

## required agents

By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.

| Stage | Required role | Agent spec | Responsibility |
| --- | --- | --- | --- |
| Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, supplied UI context, and missing information |
| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
| Research, when facts or product context need verification | `research_agent` | `/agents/research_agent.md` | Create evidence base for factual or product claims |
| UX writing | `ux_writer` | `/agents/ux_writer.md` | Create product-facing copy and UX writing artifacts |
| Review | `review_agent` | `/agents/review_agent.md` | Independently validate UX copy and artifacts |
| Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |

This pipeline must not assign work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in the current operating model is handled by `ux_writer` for UX copy or `research_agent` for evidence gaps, not by a separate Editor role.

## required inputs

Pipeline execution follows `AGENTS.md` short context loading policy. Use these inputs only when they are relevant to the current stage or required by the selected depth:

- `AGENTS.md`;
- `/project-state.md`, when continuing pipeline materialization or after context loss;
- `/kb/task_statuses.md`;
- `/tasks/TASK-ID/brief.md`;
- `/tasks/TASK-ID/task-manifest.md`;
- `/tasks/TASK-ID/status.md`;
- `/tasks/TASK-ID/orchestration_plan.md`;
- the selected pipeline: `/pipelines/ux_writing_pipeline.md`;
- `/pipelines/research_pipeline.md`, when research, factual claims, or product claims are used;
- `/agents/ux_writer.md`;
- `/kb/ux_writing_guidelines.md`;
- `/kb/glossary.md`;
- `/kb/tone_of_voice.md`;
- active client-profile files named in `task-manifest.md` or
  `orchestration_plan.md`, only when `client_profile` is set;
- product context, UI fragments, screenshots, flows, existing copy, requirements, or product notes when applicable;
- the latest relevant handoff file for the current stage.

If `TASK-ID`, `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, required product context, or required terminology source is missing, production must not continue until Chief Editor creates or repairs the missing artifact, or the task is set to `blocked`.

## required artifacts

These artifacts define the UX Writing Pipeline artifact set. Required/conditional/optional depth is governed by the artifact creation policy below.

| Artifact | Required when | Owner |
| --- | --- | --- |
| `/tasks/TASK-ID/brief.md` | always | `intake_agent` or `chief_editor` |
| `/tasks/TASK-ID/task-manifest.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/status.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/orchestration_plan.md` | always | `chief_editor` |
| `/tasks/TASK-ID/research.md` | research is required | `research_agent` |
| `/tasks/TASK-ID/sources.md` | factual or product claims are used | `research_agent` |
| `/tasks/TASK-ID/facts.md` | factual or product claims are used | `research_agent` |
| `/tasks/TASK-ID/claims_table.md` | factual or product claims are used | `research_agent` |
| `/tasks/TASK-ID/ux-copy.md` | always | `ux_writer` |
| `/tasks/TASK-ID/content-map.md` | always | `ux_writer` |
| `/tasks/TASK-ID/states-table.md` | always | `ux_writer` |
| `/tasks/TASK-ID/terminology-notes.md` | always | `ux_writer` |
| `/tasks/TASK-ID/ux-writer-notes.md` | always | `ux_writer` |
| `/tasks/TASK-ID/review.md` | always before finalization | `review_agent` |
| `/tasks/TASK-ID/qa-checklist.md` | separate checklist required by downstream consumer, high-governance, task requirement, blocker/open-question state, or traceability need | `review_agent` |
| `/tasks/TASK-ID/review-summary.md` | separate concise transfer is consumed downstream | `review_agent` |
| `/tasks/TASK-ID/final.md` | after approved review | `final_editor` |
| `/tasks/TASK-ID/finalization-notes.md` | controlled changes, unresolved risks/blockers, downstream governance, high-governance, task requirement, or traceability need | `final_editor` |
| `/tasks/TASK-ID/final_decision.md` | after finalization | `chief_editor` |

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

### required artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `brief.md` | Defines product, surface, user intent, constraints | all roles | never for active tasks |
| `task-manifest.md` | Compact current state and restart anchor | all roles | never for new tasks |
| `status.md` | Detailed status/history and transition rationale | all roles, Chief Editor | never for active tasks |
| `orchestration_plan.md` | Execution contract, roles, gates, artifact scope | all roles | never after orchestration starts |
| `ux-copy.md` | UX copy under review | review_agent, final_editor | never for UX writing production |
| `review.md` | Independent review verdict and findings | final_editor, chief_editor | never before finalization |
| role handoff | Delta-transfer between roles | receiving role | only when no role transition occurs, or compact finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md` |

### conditional artifacts

| Artifact | Required when | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `content-map.md` | flow/screen relationships affect review or restart | review_agent, final_editor | low-risk single-surface copy is self-explanatory and rationale is recorded |
| `states-table.md` | UI states, triggers, errors, or fallbacks affect copy | review_agent | no state variation exists or state handling is not applicable |
| `terminology-notes.md` | terminology source, conflicts, or approved terms matter | review_agent, final_editor | no special terminology applies |
| `ux-writer-notes.md` | assumptions, caveats, or product questions affect review | review_agent | no assumptions or caveats exist and manifest/handoff are sufficient |
| `research.md` | research is required or factual/product claims need evidence context | ux_writer, review_agent | low-risk task has supplied product context and no sensitive claims |
| `sources.md` / `facts.md` / `claims_table.md` | factual/product claims need traceability, or high-governance | review_agent, chief_editor | no factual/product claims, or low-risk evidence is intentionally compact |
| `qa-checklist.md` | high-governance review, downstream consumer, task-specific requirement, detailed traceability need, or Chief Editor requires separate checklist | chief_editor, final_editor | low-risk or simple standard checklist is embedded in `review.md` |
| `review-summary.md` | review outcome needs separate concise transfer to finalization/governance | final_editor, chief_editor | review handoff and `review.md` already provide an equivalent concise next action |
| `finalization-checklist.md` | high-governance or downstream governance needs finalization proof, or task-specific requirement demands it | chief_editor | compact finalization is evident from `review.md`, `final.md`, current `task-manifest.md`, and optional handoff if needed |
| `approval.md` | product-owner or human approval is required | chief_editor | approval not required or approval is documented in `status.md` |

### optional artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `context-summary.md` | Restarts after severe context fragmentation | current owner | manifest/status/handoff are sufficient |
| `failure.md` | Records unrecoverable task failure | chief_editor | task is not failed |
| `archive.md` | Records archive rationale | chief_editor | task is still active |

Each role must also update `task-manifest.md` at every stage transition, status transition, owner change, blocker change, and handoff creation. Role handoffs remain the default transfer mechanism. In compact execution, finalization-to-Chief-Editor handoff may be omitted only when `review.md`, `final.md`, and current `task-manifest.md` give enough delta context. Handoff files do not replace the primary artifacts.

A stage cannot be considered complete if `task-manifest.md` is stale. If `task-manifest.md`, `status.md`, latest handoff, and `orchestration_plan.md` conflict, stop and escalate to `chief_editor`.

## allowed stages

Allowed production stages:

- `intake`;
- `planning`;
- `research`, when product context or factual/product claims require verification;
- `writing`, used for UX writing by `ux_writer`;
- `editing`, only as an optional UX Writer revision checkpoint or status bridge; it is not required and does not introduce a separate Editor role;
- `review`;
- `changes_requested`;
- `approved`;
- `human_approval_required`;
- `finalization`;
- `finalized`;
- `blocked`;
- `failed`;
- `archived`.

No stage may merge UX writing and review. No stage may merge finalization and Chief Editor governance decision. No stage may use UX Writer to make product ownership decisions.

## stage sequence

Default production sequence:

```text
intake -> chief_editor orchestration -> research if needed -> ux-writing -> review -> finalization -> chief_editor final governance decision
```

Operational sequence:

| Step | Status before | Role | Action | Required outputs | Status after |
| --- | --- | --- | --- | --- | --- |
| 1 | none or `intake` | `intake_agent` | Normalize request, target surface, available product context, and missing states | `brief.md`, `status.md`, intake handoff | `intake` or `blocked` |
| 2 | `intake` | `chief_editor` | Select UX Writing Pipeline, classify product/factual risk, assign next role | `orchestration_plan.md`, `status.md`, orchestration handoff | `research`, `planning`, or `blocked` |
| 3 | `research` | `research_agent` | Verify product context or factual/product claims when required | `research.md`, `sources.md`, `facts.md`, `claims_table.md`, research handoff | `planning`, `blocked`, or `failed` |
| 4 | `planning` | `chief_editor` | Confirm product context and terminology sufficiency; route to UX writing | updated `orchestration_plan.md`, `status.md`, handoff | `writing`, `research`, or `blocked` |
| 5 | `writing` | `ux_writer` | Create UX copy artifacts from approved inputs and KB | `ux-copy.md`, `content-map.md`, `states-table.md`, `terminology-notes.md`, `ux-writer-notes.md`, UX handoff | `review`, or optional `editing` only for revision checkpoint |
| 6 | `review` | `review_agent` | Independently validate UX copy, product traceability, terminology, clarity, and artifacts | `review.md`, `qa-checklist.md` when separate checklist is required, `review-summary.md` when concise transfer is needed, review handoff | `approved`, `changes_requested`, `blocked`, or `human_approval_required` |
| 7 | `changes_requested` | `ux_writer` or `research_agent` | Resolve review findings or evidence gaps | updated UX or research artifacts, handoff | `review`, `writing`, `research`, or `blocked` |
| 8 | `approved` | `final_editor` | Produce controlled final deliverable | `final.md`, conditional finalization notes/checklist, finalization handoff | `approved` |
| 9 | `approved` | `chief_editor` | Validate finalization and make governance decision | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |

Direct `writing` -> `review` handoff is valid in the current operating model after required UX writing artifacts exist and the latest handoff from `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. `editing` may be used only as an optional UX Writer revision or ready-for-review bridge. It must not assign work to a separate Editor role.

## status transitions

Operational statuses must come from `/kb/task_statuses.md`.

Allowed critical transitions:

| From | To | Trigger | Responsible role | Required artifact evidence |
| --- | --- | --- | --- | --- |
| `intake` | `research` | Product context or factual/product claims need verification | `chief_editor` | `orchestration_plan.md`, `status.md` |
| `intake` | `planning` | Product context is supplied and research is not required | `chief_editor` | `orchestration_plan.md`, `status.md` |
| `research` | `planning` | Product or factual research scope complete | `research_agent` recommends, `chief_editor` records | research artifacts, research handoff |
| `planning` | `writing` | Chief Editor confirms product context and terminology are sufficient | `chief_editor` | `orchestration_plan.md`, status update, handoff |
| `writing` | `review` | Required UX writing artifacts are complete and review is required | `ux_writer` | `ux-copy.md`, `content-map.md`, `states-table.md`, `terminology-notes.md`, `ux-writer-notes.md`, handoff to `review_agent` |
| `ux-writing` | `review` | Local stage label used for UX writing completion and review is required | `ux_writer` | `ux-copy.md`, `content-map.md`, `states-table.md`, `terminology-notes.md`, `ux-writer-notes.md`, handoff to `review_agent` |
| `writing` | `editing` | Status model bridge or UX Writer revision checkpoint | `ux_writer` | UX artifacts, UX handoff |
| `editing` | `review` | UX copy is ready for independent review | `ux_writer` or `chief_editor` | `ux-copy.md`, `content-map.md`, `states-table.md`, `terminology-notes.md`, handoff |
| `writing` | `research` | UX Writer finds missing product context or evidence | `ux_writer` recommends | `ux-writer-notes.md`, `states-table.md`, handoff or status note |
| `writing` | `blocked` | UX Writer cannot continue safely | `ux_writer` | `status.md`, failure note or handoff |
| `review` | `approved` | Review outcome is `approved` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `changes_requested` | Review outcome is `changes_requested` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `blocked` | Review outcome is `blocked` | `review_agent` | `review.md`, blocker evidence |
| `review` | `human_approval_required` | Review requires human or product decision | `review_agent` or `chief_editor` | `review.md`, `status.md` escalation |
| `changes_requested` | `writing` | UX copy changes are required | `review_agent` recommends, `chief_editor` or owner records | `review.md`, handoff to `ux_writer` |
| `changes_requested` | `research` | Product context or evidence gaps are required | `review_agent` recommends, `chief_editor` or owner records | `review.md`, handoff to `research_agent` |
| `changes_requested` | `review` | Required changes are complete and ready for re-review | responsible production role | updated artifacts, handoff |
| `approved` | `human_approval_required` | Human approval is required before release, publication, delivery, or closure | `chief_editor` | `status.md`, `review.md` or brief requirement |
| `approved` | `finalized` | Chief Editor validates finalization and no human approval blocks closure | `chief_editor` | `final.md`, conditional finalization notes, `task-manifest.md`, `final_decision.md` |
| `blocked` | any valid recovery status | Blocker resolved | current owner or `chief_editor` | updated `status.md`, resolution evidence |

If a desired transition is not allowed by `/kb/task_statuses.md`, use the nearest valid transition and document the reason in `status.md`.

## risk mode behavior

Risk mode classification follows `AGENTS.md` and `/project-state.md`.

`low-risk`:

- research may be skipped with a no-research rationale when no factual or product behavior claims are used;
- evidence artifacts may be combined or omitted if copy is based only on supplied product context and low-sensitivity language choices;
- review is still required, but checklist may be compact inside `review.md`;
- compact execution may be used when `AGENTS.md` safety conditions hold;
- finalization may use compact shape: `review.md`, `final.md`, current `task-manifest.md`, and optional short handoff only if needed.

`standard`:

- use normal UX Writing Pipeline requirements;
- research is required when factual or product claims are present;
- claims traceability is required when claims are material;
- simple source-light standard tasks may keep checklist and summary content inside `review.md` when no downstream consumer, high-governance need, task-specific requirement, blocker/open-question state, or traceability need requires separate files.

`high-governance`:

- research is required;
- `sources.md`, `facts.md`, and `claims_table.md` are required for factual or product claims;
- review must be full;
- `finalization-checklist.md` is required;
- human or product-owner approval must be assessed explicitly;
- Chief Editor must not finalize governance without an explicit decision on approval.

## product context requirements

UX writing requires explicit product context sufficient for the assigned surface.

Product context may include:

- product requirements;
- UI screenshots or fragments;
- flow diagrams;
- existing interface copy;
- state definitions;
- user intent and target audience;
- business rules;
- feature availability;
- validation rules;
- error conditions;
- notification triggers;
- constraints from product owner or user.

Product context must be recorded or referenced in task artifacts, usually in `brief.md`, `orchestration_plan.md`, `content-map.md`, `states-table.md`, `research.md`, or handoff files.

UX Writer must not:

- invent product behavior;
- invent unavailable features;
- change business logic;
- silently redefine product concepts;
- decide feature scope, release scope, or product policy.

Unclear product behavior, missing UI states, unknown feature availability, or conflicting product requirements block UX writing until clarified or explicitly documented as a non-blocking assumption by Chief Editor or the user.

## terminology requirements

Terminology consistency is mandatory.

UX Writer must load and apply:

- `/kb/glossary.md`;
- `/kb/tone_of_voice.md`;
- `/kb/ux_writing_guidelines.md`;
- domain-specific terminology sources named in `orchestration_plan.md`;
- task-local terminology or product naming artifacts, if present.

`terminology-notes.md` must document:

- approved terms;
- rejected variants;
- rationale;
- KB or product context source;
- unresolved terminology questions;
- terms needing product or Chief Editor decision.

If terminology sources conflict, UX Writer must stop, document the conflict, and recommend `blocked` or escalation. UX Writer must not silently choose a term when the choice changes product meaning, legal meaning, or user expectation.

## UX writing requirements

UX Writer must create copy only from:

- `brief.md`;
- `orchestration_plan.md`;
- product context artifacts;
- approved KB context;
- research artifacts when factual or product claims are used;
- latest relevant handoff.

UX Writer creates only the UX writing artifacts required by risk mode and downstream review:

- `ux-copy.md`;
- `content-map.md`, when flow or screen relationships affect review or restart;
- `states-table.md`, when UI states, triggers, or fallback behavior affect copy;
- `terminology-notes.md`, when terminology source or conflicts matter;
- `ux-writer-notes.md`, when assumptions, caveats, or product questions affect review;
- UX writing handoff.

UX writing rules:

- copy must minimize ambiguity and cognitive load;
- copy must preserve terminology and tone consistency;
- copy must be traceable to product context and KB;
- missing UI states must be documented in `states-table.md`;
- assumptions must be documented in `ux-writer-notes.md`;
- accessibility and clarity risks must be documented;
- risky wording must be documented and handed off for review;
- UX copy must not imply unavailable features or unsupported product behavior;
- factual or product claims must trace to `claims_table.md`, `facts.md`, `sources.md`, `research.md`, product context, or KB;
- if required product behavior is unclear, UX Writer must stop and recommend `blocked` or clarification.

## review requirements

Review is mandatory before finalization.

Review Agent must validate:

- compliance with `brief.md`;
- compliance with `AGENTS.md`;
- compliance with `orchestration_plan.md`;
- UX Writing Pipeline compliance;
- review-gate integrity;
- reviewer independence from UX Writer;
- product context traceability;
- terminology consistency;
- tone and glossary compliance;
- required artifact completeness;
- clarity and cognitive load;
- accessibility risks;
- missing or ambiguous UI states;
- unsupported product behavior or unavailable feature implications;
- correct use of `claims_table.md` when factual or product claims are used;
- status consistency under `/kb/task_statuses.md`.

Review Agent creates only the review artifacts required by risk mode and downstream governance:

- `review.md`;
- `qa-checklist.md`, when a separate checklist is required;
- `review-summary.md`, when concise transfer is needed;
- `reviewer-notes.md`, when needed by `/agents/review_agent.md`;
- review handoff.

Valid review outcomes:

- `approved`;
- `changes_requested`;
- `blocked`.

The task must not enter `approved` if `review.md` is missing, review is not independent, checked artifacts are not listed, product context traceability is insufficient, terminology conflicts remain, unclear product behavior affects copy, or critical accessibility or clarity issues remain open.

## finalization requirements

Finalization may begin only after valid review outcome `approved`.

Final Editor creates only finalization artifacts required by risk mode and downstream governance:

- `final.md`;
- `finalization-notes.md`, when controlled finalization changes or unresolved risks must be recorded;
- `finalization-checklist.md`, when high-governance depth, downstream governance, traceability proof, task-specific requirement, or Chief Editor requires it;
- `handoff-finalization-final-editor-to-chief-editor.md`, unless compact execution finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md`.

Finalization rules:

- `final_editor` owns `final.md`;
- `final.md` must contain the finalized deliverable only;
- finalization may apply approved review changes and controlled polishing only;
- finalization must not introduce new product behavior, new claims, new terminology, or changed meaning;
- finalization must not remove required caveats or unresolved risk visibility;
- unresolved risks must remain visible in `finalization-notes.md`;
- finalization does not grant release, publication, delivery, product, or governance approval.

If finalization needs product decisions, new facts, terminology decisions, strategy changes, or unresolved review decisions, stop and route back to `research`, `writing`, `review`, `blocked`, or `human_approval_required` as allowed by `/kb/task_statuses.md`.

## governance requirements

Chief Editor owns final governance decision.

Chief Editor must create:

- `/tasks/TASK-ID/final_decision.md`;
- updated `/tasks/TASK-ID/status.md`.

Chief Editor must verify before setting `finalized`:

- `review.md` exists and outcome is `approved`;
- `qa-checklist.md` exists when separate checklist depth is required, otherwise checks are embedded in `review.md`;
- `review-summary.md` exists when needed for concise governance transfer;
- `final.md` exists and was created by `final_editor`;
- `finalization-notes.md` exists when controlled changes or unresolved risks need to be recorded;
- compact finalization omissions, if any, are recorded in `task-manifest.md` or `final_decision.md`;
- finalization did not bypass review or introduce unsupported product behavior;
- terminology and product context blockers are resolved or explicitly carried as approved caveats;
- human approval requirements from `brief.md`, `status.md`, `review.md`, or `finalization-notes.md` are satisfied or the task is moved to `human_approval_required`;
- no unresolved blocker prevents closure.

Release, publication, or delivery requires human approval when required by `brief.md`, `status.md`, `review.md`, `finalization-notes.md`, or `final_decision.md`. Human approval must be artifact-backed in `status.md` or `approval.md`; it must not be inferred from chat memory.

## handoff requirements

Every role transition normally creates a handoff file following `/templates/artifacts/handoff_template.md`. Compact execution may omit the finalization-to-Chief-Editor handoff only when `task-manifest.md` is current and no blocker, traceability need, governance escalation, contradiction, version conflict, evidence dispute, reviewer uncertainty, or human approval complexity exists.

Expected handoffs:

- `handoff-intake-intake-agent-to-chief-editor.md`;
- `handoff-planning-chief-editor-to-research-agent.md`, when research is required;
- `handoff-planning-chief-editor-to-ux-writer.md`, when UX writing can begin;
- `handoff-research-research-agent-to-chief-editor.md` or `handoff-research-research-agent-to-ux-writer.md`;
- `handoff-ux-writing-ux-writer-to-review-agent.md`;
- `handoff-review-review-agent-to-chief-editor.md`;
- `handoff-review-review-agent-to-ux-writer.md`, when changes are requested from UX Writer;
- `handoff-review-review-agent-to-research-agent.md`, when more research or product evidence is required;
- `handoff-finalization-final-editor-to-chief-editor.md`, when compact omission is not justified.

Each handoff must include:

- sending role and receiving role;
- reference to `/tasks/TASK-ID/task-manifest.md`;
- what changed since the previous stage;
- artifacts created or updated;
- constraints changed, if any;
- blockers;
- next role;
- next action;
- expected outputs;
- forbidden outputs;
- escalation conditions.

Handoffs must not replace the primary artifacts for the completed stage.

## quality gates

Quality gates are mandatory and artifact-backed.

| Gate | Passed only when | Blocking evidence |
| --- | --- | --- |
| Intake gate | `brief.md` and `status.md` exist with task goal, surface, audience, product context, constraints, and `TASK-ID` | missing or ambiguous brief |
| Orchestration gate | `orchestration_plan.md` selects UX Writing Pipeline, assigns roles, and records research/product context need | missing plan, invalid role, unclear ownership |
| Product context gate | required product behavior, UI states, feature availability, and constraints are present or explicitly blocked | unclear behavior, missing state, unavailable feature ambiguity |
| Terminology gate | glossary, tone, UX guidelines, and task-local terminology are loaded and conflicts documented | missing terminology source or unresolved conflict |
| Research gate | required research artifacts exist when factual or product claims are used | unsupported, contradicted, stale, or missing evidence |
| UX writing gate | UX artifacts exist and copy avoids invented product logic, ambiguity, terminology drift, and hidden assumptions | invented behavior, missing state coverage, unclear copy |
| Review gate | `review.md` outcome is `approved` with checked artifacts listed | missing review, non-independent review, unresolved critical issues |
| Finalization gate | `final.md` and required finalization evidence exist after approved review | finalization before review, missing current manifest state, or new unsupported product behavior |
| Governance gate | `final_decision.md` validates finalization and human approval requirements | missing approval, unresolved blocker, missing final decision |

Failure at any gate must keep the task in the current valid status, move it to `changes_requested`, `research`, `blocked`, or `human_approval_required`, or follow retry policy.

## escalation rules

Escalate to Chief Editor or user when:

- instructions conflict;
- required task artifacts are missing and cannot be safely created by the current role;
- the pipeline conflicts with `AGENTS.md`;
- a role is asked to exceed its decision boundary;
- product behavior is unclear;
- UI states, triggers, errors, or fallback behavior are missing;
- terminology sources conflict;
- requested copy would imply unavailable features;
- requested copy would change product logic, business rules, or user expectations;
- factual or product claims are unavailable, unsupported, contradicted, or too uncertain;
- accessibility or clarity risk is high;
- Review Agent independence cannot be established;
- review blocks finalization;
- finalization would require new product decisions or review override;
- human or product approval is required;
- retry policy is exhausted.

Escalation must include:

- blocking issue;
- affected files, screens, states, terms, claims, sources, or instructions;
- why safe continuation is impossible;
- smallest decision needed;
- recommended operational status;
- recommended next role.

## blocked conditions

Set or recommend `blocked` when any of these prevent safe continuation:

- missing or invalid `TASK-ID`;
- missing `brief.md`, `status.md`, or `orchestration_plan.md`;
- selected pipeline conflicts with `AGENTS.md`;
- required agent spec, KB file, glossary, UX guidelines, or pipeline file is unavailable;
- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
- product context is missing or too ambiguous for safe UX writing;
- UI states, triggers, validation rules, or fallback behavior are missing and affect copy;
- terminology sources conflict on a product-critical term;
- UX Writer would need to invent product behavior or unavailable features;
- factual or product claims are required but `sources.md`, `facts.md`, or `claims_table.md` is missing;
- review is missing, non-independent, or blocked;
- finalization is requested before approved review;
- human or product approval is required but absent;
- status transition cannot be reconciled with `/kb/task_statuses.md`;
- context fragmentation prevents reliable continuation and cannot be repaired with `context-summary.md`.

Blocked status must be recorded in `status.md` using the format from `/kb/task_statuses.md`.

## retry policy

Follow `/kb/task_statuses.md`.

Retryable cases:

- incomplete handoff;
- missing optional stage note;
- formatting error;
- incomplete UX copy table;
- incomplete states table;
- terminology note omission;
- recoverable product context gap;
- review changes that can be addressed by UX Writer or Research Agent;
- context fragmentation repairable through `context-summary.md`.

Non-retryable without escalation:

- instruction conflict;
- impossible product requirement;
- missing product owner or human decision;
- request to bypass review;
- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
- repeated failure caused by unclear brief or missing product context;
- review-gate failure that requires a governance decision.

Retry rules:

- after the first failed attempt, document the issue and retry once;
- after the second failed attempt on the same issue, set or recommend `blocked`;
- after three failed attempts on the same production stage, set or recommend `failed` unless the user or Chief Editor changes constraints;
- each retry must preserve previous meaningful artifacts or use versioned filenames when comparison matters.

## completion conditions

UX Writing Pipeline is complete only when:

- required task artifacts exist in `/tasks/TASK-ID/`;
- `brief.md`, `task-manifest.md`, `status.md`, and `orchestration_plan.md` are current;
- research artifacts exist if research was required;
- source, fact, and claim artifacts exist if factual or product claims were used;
- `ux-copy.md` exists and conditional UX support artifacts exist when needed by flow complexity, terminology, state coverage, review, or risk mode;
- independent `review.md` exists and outcome is `approved`;
- `qa-checklist.md` exists when separate checklist depth is required, otherwise checks are embedded in `review.md`;
- `review-summary.md` exists when needed for concise governance transfer;
- `final.md` exists and was created by `final_editor` after approved review;
- `finalization-notes.md` exists when controlled changes or unresolved risks need to be recorded;
- `finalization-checklist.md` exists when high-governance depth, downstream governance, traceability proof, task-specific requirement, or Chief Editor requires it;
- `final_decision.md` exists and was created by `chief_editor`;
- `status.md` records a valid final state under `/kb/task_statuses.md`;
- human or product approval is documented if required by brief, status, review, finalization notes, or final decision;
- no unresolved blocker prevents closure.

Completion means the UX writing workflow is artifact-complete and governance-closed. It does not imply release, publication, or delivery unless required human approval is explicitly documented.

## restart protocol

After context loss, continue from artifacts, not chat history.

Receiving or restarting agents use the short context path from `AGENTS.md`:

1. `AGENTS.md` or a short reference to its active invariants.
2. `/tasks/TASK-ID/task-manifest.md`.
3. The latest relevant handoff file.
4. The current working artifact.
5. Only `/pipelines/ux_writing_pipeline.md`, `/pipelines/research_pipeline.md`, UX KB, terminology source, or editorial knowledge directly needed for the next action.

Do not read all pipelines, all agent specs, all old task folders, all retrospectives, all versions, or the full project tree by default.

Expanded reading is allowed for high-governance, conflict, product-context uncertainty, or restart uncertainty. In that case read the exact source/evidence files, `status.md`, review trail, governance artifacts, product context, terminology source, or old versions needed to resolve the risk.

Then perform this restart check:

- confirm `TASK-ID`;
- confirm the current-version pointer names the active artifact when multiple versions exist;
- do not use latest modified time as the current-version source;
- stop and ask Chief Editor if current version state is unclear;
- confirm current status is valid under `/kb/task_statuses.md`;
- confirm the selected pipeline is UX Writing Pipeline;
- confirm current owner role and next role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
- compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
- identify the last completed quality gate;
- verify required artifacts for that gate;
- identify missing, stale, contradictory, or unsupported product context;
- identify unresolved terminology conflicts or missing UI states;
- continue from the next incomplete stage or set/recommend `blocked`.

Model memory, prior chat, or unsaved notes must not be used as product context, terminology authority, evidence, approval, review outcome, or workflow state.
