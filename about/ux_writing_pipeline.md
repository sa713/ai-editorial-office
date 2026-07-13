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

Use this pipeline when the primary or assigned member of the selected
deliverable set, recorded after the outcome-first decision, is product-facing
copy that appears in or
around an interface, product flow, onboarding path, notification, validation
state, or user guidance surface. A UX example alone does not select this
pipeline when format choice was delegated or only illustrative.

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

Role legality and extension-role bounds are governed by `AGENTS.md`. This table
only maps UX Writing Pipeline responsibilities to current roles.

| Stage | Required role | Agent spec | Responsibility |
| --- | --- | --- | --- |
| Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, supplied UI context, and missing information |
| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select minimal deliverable set, then primary pipeline and bounded UX member contracts; assign roles, maintain status, make final decision |
| Research, when facts or product context need verification | `research_agent` | `/agents/research_agent.md` | Create evidence base for factual or product claims |
| UX writing | `ux_writer` | `/agents/ux_writer.md` | Create product-facing copy and UX writing artifacts |
| Review | `review_agent` | `/agents/review_agent.md` | Independently validate UX copy and artifacts |
| Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |

Revision in the current operating model is handled by `ux_writer` for UX copy or
`research_agent` for evidence gaps, not by a separate Editor role.

## required inputs

Pipeline execution follows `/kb/shared_lifecycle_kernel.md` stage context
contracts and `AGENTS.md` short context loading policy. Load the shared task
packet from those owners, then add only UX-specific context:

- this pipeline file;
- `/pipelines/research_pipeline.md`, when research, factual claims, or product
  claims are used;
- `/agents/ux_writer.md` and other assigned role specs when needed by the
  active stage;
- UX guidance, glossary, tone, product context, client-profile, handoff, and
  source files named by task artifacts.

If `TASK-ID`, `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, required product context, or required terminology source is missing, production must not continue until Chief Editor creates or repairs the missing artifact, or the task is set to `blocked`.

## required artifacts

Shared task artifacts and ownership are defined in `AGENTS.md`,
`/kb/task_object_model.md`, and `/kb/shared_lifecycle_kernel.md`. UX Writing
Pipeline adds these task-type views when the selected depth requires them:

- `ux-copy.md`;
- `content-map.md`, when flow or screen relationships affect review or restart;
- `states-table.md`, when UI states, triggers, errors, or fallbacks affect copy;
- `terminology-notes.md`, when terminology source or conflicts matter;
- `ux-writer-notes.md`, when assumptions, caveats, or product questions affect
  review;
- UX research artifacts when factual or product claims require them.

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

For low-risk and simple source-light standard tasks, use
`/kb/compact_execution.md` to apply compact execution without weakening
review-gate. Chief Editor must record the compact rationale; `review.md`
remains required before finalization; optional artifacts are not created
automatically. Review Agent should not require optional artifacts when core
traceability, restartability, and governance evidence are sufficient.

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

Use only statuses from `/kb/task_statuses.md`. For UX work, the production
status may be `writing` or the optional explicit `ux-writing` status defined by
the status owner; `editing` remains only the optional revision/status bridge.

No stage may merge UX writing with review or finalization with Chief Editor
governance. No stage may use UX Writer to make product ownership decisions.

## stage sequence

Default production sequence:

```text
intake -> chief_editor orchestration -> research if needed -> ux-writing -> review -> finalization -> chief_editor final governance decision
```

UX-specific route:

1. Chief Editor selects UX Writing Pipeline and confirms product/factual risk.
2. Research runs only when product context or factual/product claims require
   verification.
3. Chief Editor confirms product context and terminology sufficiency.
4. UX Writer creates UX copy and required UX support artifacts.
5. Review Agent independently reviews the current UX package.
6. Final Editor finalizes only after approved review.
7. Chief Editor records the final governance decision.

Direct `writing` -> `review` handoff is valid in the current operating model after required UX writing artifacts exist and the latest handoff from `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. `editing` may be used only as an optional UX Writer revision or ready-for-review bridge. It must not assign work to a separate Editor role.

## status transitions

Operational statuses and transitions are owned by `/kb/task_statuses.md`.
UX-specific transition notes:

- route to `research` when product context or factual/product claims need
  verification, otherwise to `planning`;
- route from `planning` to UX production only after product context and
  terminology are sufficient;
- route from UX production to `review` after required UX artifacts and handoff
  exist;
- route `changes_requested` findings back to UX production, `research`, or
  `review` according to the repair owner and re-review scope;
- route from `approved` toward finalization/governance only under the shared
  review-gate and human-approval rules.

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

Handoff behavior is owned by `AGENTS.md`,
`/kb/shared_lifecycle_kernel.md`, and
`/templates/artifacts/handoff_template.md`. UX writing handoffs normally
connect Chief Editor, Research Agent when used, UX Writer, Review Agent, Final
Editor, and Chief Editor governance. Handoffs must point to current UX copy,
state coverage, terminology decisions, product-context gaps, and blockers when
material.

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

UX Writing Pipeline is complete only when the shared lifecycle and status
owners allow closure, and the UX-specific packet is current:

- required UX copy and support artifacts exist for the selected flow/state
  complexity;
- required research, source, fact, and claim artifacts exist when factual or
  product claims were used;
- independent `review.md` approves the current UX package;
- finalization and Chief Editor governance artifacts exist when required;
- human or product approval and blockers are resolved or explicitly carried by
  the governing status.

Completion means the UX writing workflow is artifact-complete and governance-closed. It does not imply release, publication, or delivery unless required human approval is explicitly documented.

## restart protocol

Restart behavior is owned by `AGENTS.md` and
`/kb/shared_lifecycle_kernel.md`. For UX Writing Pipeline restarts, add only
these checks to the shared restart packet:

- selected pipeline is UX Writing Pipeline;
- current UX copy/version and relevant state tables are identified;
- product context, feature availability, and terminology sources are current;
- unresolved terminology conflicts, missing UI states, or unsupported product
  behavior are visible;
- required UX research artifacts are present when research was required;
- the last completed UX quality gate is clear.
