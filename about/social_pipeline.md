# Social Pipeline

## pipeline purpose

This pipeline governs creation of short-form editorial and promotional materials:

- social posts;
- short announcements;
- platform-adapted content;
- promotional editorial copy;
- announcement copy;
- short-form editorial materials.

The pipeline supports fast iteration without governance collapse. Brevity, platform adaptation, and engagement goals must not weaken factual traceability, tone consistency, review-gate integrity, or final governance ownership.

The pipeline is markdown-first, artifact-backed, deterministic, and restartable from `/tasks/TASK-ID/` without chat history.

## when to use

Use this pipeline when the requested output is short-form editorial or promotional copy adapted to one or more platforms.

Use it when:

- the deliverable is a social post, announcement, caption, thread starter, short promotional text, or platform-adapted editorial snippet;
- platform constraints, audience expectations, and brevity materially affect the copy;
- tone consistency and reduced context size create drift risk;
- factual claims may be used and need traceability;
- the material still needs review before finalization, publication, delivery, release, or archival.

## when not to use

Do not use this pipeline when:

- the task is a long-form article, explainer, analysis, or knowledge content;
- the task is product-facing interface copy or UX writing;
- the task is only research and no short-form copy is required;
- the task is only review of existing material;
- the task is finalization after an already approved review, unless Chief Editor selects this pipeline as governing context;
- the request would require bypassing research, review, finalization, governance, or human approval rules.

If the task mixes social copy with long-form, UX, or review work, Chief Editor must record the selected pipeline and scope boundaries in `/tasks/TASK-ID/orchestration_plan.md`.

## required agents

By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.

| Stage | Required role | Agent spec | Responsibility |
| --- | --- | --- | --- |
| Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, platform target, audience, constraints, and missing information |
| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
| Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
| Writing | `writer_agent` | `/agents/writer_agent.md` | Create platform-adapted short-form draft and claim usage notes |
| Review | `review_agent` | `/agents/review_agent.md` | Independently validate copy, artifacts, tone, traceability, and governance compliance |
| Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |

This pipeline must not assign work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in the current operating model is handled by `writer_agent` for copy changes or `research_agent` for evidence gaps, not by a separate editing role.

## required inputs

Pipeline execution follows `/kb/shared_lifecycle_kernel.md` stage context contracts and `AGENTS.md` short context loading policy. Use these inputs only when they are relevant to the current stage or required by the selected depth:

- `AGENTS.md`;
- `/project-state.md`, when continuing after context loss;
- `/kb/task_statuses.md`;
- `/tasks/TASK-ID/brief.md`;
- `/tasks/TASK-ID/task-manifest.md`;
- `/tasks/TASK-ID/status.md`;
- `/tasks/TASK-ID/orchestration_plan.md`;
- the selected pipeline: `/pipelines/social_pipeline.md`;
- `/pipelines/research_pipeline.md`, when research or factual claims are used;
- latest relevant handoff file;
- `/agents/writer_agent.md`;
- relevant KB files named in `orchestration_plan.md`;
- active client-profile files named in `task-manifest.md` or
  `orchestration_plan.md`, only when `client_profile` is set;
- `/kb/tone_of_voice.md`, when tone matters;
- `/kb/editorial_policy.md`, when editorial or promotional risk matters;
- target platform, channel, audience, format, length, and publishing constraints when applicable.

If `TASK-ID`, `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, or required platform constraints are missing, production must not continue until Chief Editor creates or repairs the missing artifact, or the task is set to `blocked`.

## required artifacts

These artifacts define the Social Pipeline artifact set. Required/conditional/optional depth is governed by the artifact creation policy below.

| Artifact | Required when | Owner |
| --- | --- | --- |
| `/tasks/TASK-ID/brief.md` | always | `intake_agent` or `chief_editor` |
| `/tasks/TASK-ID/task-manifest.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/status.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/orchestration_plan.md` | always | `chief_editor` |
| `/tasks/TASK-ID/research.md` | research is required | `research_agent` |
| `/tasks/TASK-ID/sources.md` | factual claims are used | `research_agent` |
| `/tasks/TASK-ID/facts.md` | factual claims are used | `research_agent` |
| `/tasks/TASK-ID/claims_table.md` | factual claims are used | `research_agent` |
| `/tasks/TASK-ID/draft.md` | always | `writer_agent` |
| `/tasks/TASK-ID/claims-used.md` | factual claims are used | `writer_agent` |
| `/tasks/TASK-ID/writer-notes.md` | when needed by `writer_agent` or when platform/tone decisions matter | `writer_agent` |
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
| `brief.md` | Defines platform, audience, scope, acceptance criteria | all roles | never for active tasks |
| `task-manifest.md` | Compact current state and restart anchor | all roles | never for new tasks |
| `status.md` | Detailed status/history and transition rationale | all roles, Chief Editor | never for active tasks |
| `orchestration_plan.md` | Execution contract, roles, gates, artifact scope | all roles | never after orchestration starts |
| `draft.md` | Social copy or variants under review | review_agent, final_editor | never for social production |
| `review.md` | Independent review verdict and findings | final_editor, chief_editor | never before finalization |
| role handoff | Delta-transfer between roles | receiving role | only when no role transition occurs, or compact finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md` |

### conditional artifacts

| Artifact | Required when | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `research.md` | research is required or claims need evidence context | writer_agent, review_agent | low-risk task has no factual claims and no-research rationale is recorded |
| `sources.md` | factual claims need source traceability, or high-governance | review_agent, chief_editor | no factual claims, or low-risk evidence is intentionally compact |
| `facts.md` | factual claims need fact-level traceability, or high-governance | writer_agent, review_agent | no factual claims, or low-risk evidence is intentionally compact |
| `claims_table.md` | material claims require claim-level validation, or high-governance | writer_agent, review_agent | no material claims, or low-risk evidence is intentionally compact |
| `claims-used.md` | factual claims appear in draft, required for high-governance | review_agent | no factual claims are used |
| `qa-checklist.md` | high-governance review, downstream consumer, task-specific requirement, detailed traceability need, or Chief Editor requires separate checklist | chief_editor, final_editor | low-risk or simple standard checklist is embedded in `review.md` |
| `review-summary.md` | review outcome needs separate concise transfer to finalization/governance | final_editor, chief_editor | review handoff and `review.md` already provide an equivalent concise next action |
| `finalization-checklist.md` | high-governance or downstream governance needs finalization proof, or task-specific requirement demands it | chief_editor | compact finalization is evident from `review.md`, `final.md`, current `task-manifest.md`, and optional handoff if needed |
| `approval.md` | explicit human approval is required | chief_editor | approval not required or approval is documented in `status.md` |

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
- `research`, when required;
- `writing`;
- `editing`, only as an optional Writer Agent revision checkpoint or status bridge; it is not required and does not introduce a separate editing role;
- `review`;
- `changes_requested`;
- `approved`;
- `human_approval_required`;
- `finalization`;
- `finalized`;
- `blocked`;
- `failed`;
- `archived`.

No stage may merge writing and review. No stage may merge finalization and Chief Editor governance decision. Short-form speed must not bypass governance.

## stage sequence

Default production sequence:

```text
intake -> chief_editor orchestration -> research if needed -> writing -> review -> finalization -> chief_editor final governance decision
```

Operational sequence:

| Step | Status before | Role | Action | Required outputs | Status after |
| --- | --- | --- | --- | --- | --- |
| 1 | none or `intake` | `intake_agent` | Normalize request, platform target, audience, constraints, and missing inputs | `brief.md`, `status.md`, intake handoff | `intake` or `blocked` |
| 2 | `intake` | `chief_editor` | Select Social Pipeline, classify factual/tone risk, assign next role | `orchestration_plan.md`, `status.md`, orchestration handoff | `research`, `planning`, or `blocked` |
| 3 | `research` | `research_agent` | Create evidence base when required | `research.md`, `sources.md`, `facts.md`, `claims_table.md`, research handoff | `planning`, `blocked`, or `failed` |
| 4 | `planning` | `chief_editor` | Confirm research sufficiency or no-research rationale; route to writing | updated `orchestration_plan.md`, `status.md`, handoff | `writing`, `research`, or `blocked` |
| 5 | `writing` | `writer_agent` | Create short-form draft from approved inputs and platform constraints | `draft.md`, `claims-used.md` when needed, `writer-notes.md` when needed, writer handoff | `review`, or optional `editing` only for revision checkpoint |
| 6 | `review` | `review_agent` | Validate factual traceability, tone, editorial relevance, replaceability risk, platform adaptation, brevity, and artifacts | `review.md`, `qa-checklist.md` when separate checklist is required, `review-summary.md` when concise transfer is needed, review handoff | `approved`, `changes_requested`, `blocked`, or `human_approval_required` |
| 7 | `changes_requested` | `writer_agent` or `research_agent` | Resolve review findings or evidence gaps | updated draft or research artifacts, handoff | `review`, `writing`, `research`, or `blocked` |
| 8 | `approved` | `final_editor` | Produce controlled final deliverable | `final.md`, conditional finalization notes/checklist, finalization handoff | `approved` |
| 9 | `approved` | `chief_editor` | Validate finalization and make governance decision | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |

Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate editing role.

## status transitions

Operational statuses must come from `/kb/task_statuses.md`.

Allowed critical transitions:

| From | To | Trigger | Responsible role | Required artifact evidence |
| --- | --- | --- | --- | --- |
| `intake` | `research` | Social copy needs evidence before writing | `chief_editor` | `orchestration_plan.md`, `status.md` |
| `intake` | `planning` | Research is not required before social writing | `chief_editor` | `orchestration_plan.md`, `status.md` |
| `research` | `planning` | Research scope complete or needs Chief Editor routing | `research_agent` recommends, `chief_editor` records | research artifacts, research handoff |
| `planning` | `writing` | Chief Editor confirms platform, tone, and evidence inputs are sufficient | `chief_editor` | `orchestration_plan.md`, status update, handoff |
| `writing` | `review` | Required writing artifacts are complete and review is required | `writer_agent` | `draft.md`, `writer-notes.md`, `claims-used.md` when needed, handoff to `review_agent` |
| `writing` | `editing` | Status model bridge or Writer Agent revision checkpoint | `writer_agent` | `draft.md`, writer handoff |
| `editing` | `review` | Draft is ready for independent review | `writer_agent` or `chief_editor` | `draft.md`, `claims-used.md` when needed, handoff |
| `writing` | `research` | Writer finds missing evidence | `writer_agent` recommends | `writer-notes.md`, handoff or status note |
| `writing` | `blocked` | Writer cannot continue safely | `writer_agent` | `status.md`, failure note or handoff |
| `review` | `approved` | Review outcome is `approved` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `changes_requested` | Review outcome is `changes_requested` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `blocked` | Review outcome is `blocked` | `review_agent` | `review.md`, blocker evidence |
| `review` | `human_approval_required` | Review requires human decision | `review_agent` or `chief_editor` | `review.md`, `status.md` escalation |
| `changes_requested` | `writing` | Copy changes are required | `review_agent` recommends, `chief_editor` or owner records | `review.md`, handoff to `writer_agent` |
| `changes_requested` | `research` | Evidence gaps are required | `review_agent` recommends, `chief_editor` or owner records | `review.md`, handoff to `research_agent` |
| `changes_requested` | `review` | Required changes are complete and ready for re-review | responsible production role | updated artifacts, handoff |
| `approved` | `human_approval_required` | Human approval is required before finalization, publication, delivery, or release | `chief_editor` | `status.md`, `review.md` or brief requirement |
| `approved` | `finalized` | Chief Editor validates finalization and no human approval blocks closure | `chief_editor` | `final.md`, conditional finalization notes, `task-manifest.md`, `final_decision.md` |
| `blocked` | valid recovery status under `/kb/task_statuses.md` | Blocker resolved | current owner or `chief_editor` | updated `status.md`, resolution evidence |

If a desired transition is not allowed by `/kb/task_statuses.md`, use the nearest valid transition and document the reason in `status.md`.

## risk mode behavior

Risk mode classification follows `AGENTS.md` and `/project-state.md`.

`low-risk`:

- research may be skipped with a no-research rationale;
- evidence artifacts may be combined or omitted when no factual claims are used;
- review is still required, but checklist may be compact inside `review.md`;
- compact execution may be used when `AGENTS.md` safety conditions hold;
- finalization may use compact shape: `review.md`, `final.md`, current `task-manifest.md`, and optional short handoff only if needed.

`standard`:

- use normal Social Pipeline requirements;
- research is required when factual claims are present;
- claims traceability is required when claims are material;
- simple source-light standard tasks may keep checklist and summary content inside `review.md` when no downstream consumer, high-governance need, task-specific requirement, blocker/open-question state, or traceability need requires separate files.

`high-governance`:

- research is required;
- `sources.md`, `facts.md`, and `claims_table.md` are required;
- `claims-used.md` is required;
- review must be full;
- `finalization-checklist.md` is required;
- human approval must be assessed explicitly;
- Chief Editor must not finalize governance without an explicit decision on approval.

## platform adaptation requirements

Platform adaptation must be explicit and artifact-backed.

`brief.md`, `orchestration_plan.md`, `draft.md`, `writer-notes.md`, or handoff must record:

- target platform or channel;
- intended audience;
- format constraints;
- length or character constraints, if known;
- call-to-action requirements, if any;
- link, hashtag, mention, or media constraints, if any;
- required variants, if more than one platform is targeted.

Platform optimization must not:

- change factual meaning;
- remove required caveats;
- exaggerate claims for engagement;
- create clickbait drift;
- violate tone of voice or editorial policy;
- imply human approval, release, publication, or delivery.

If platform constraints are missing but materially affect the copy, Writer Agent must stop and recommend `blocked` or Chief Editor clarification.

## tone requirements

Tone consistency is mandatory.

Writer Agent and Review Agent must apply:

- `/kb/tone_of_voice.md`;
- `/kb/editorial_policy.md`, when editorial or promotional risk matters;
- `/kb/forbidden_patterns.md`, when clickbait, exaggeration, manipulative framing, or risky claims matter;
- task-local tone constraints from `brief.md` and `orchestration_plan.md`.

Tone drift risks must be documented in `writer-notes.md`, `review.md`, or `finalization-notes.md`.

High-risk tone drift includes:

- clickbait framing;
- overpromising;
- unsupported urgency;
- excessive simplification;
- misleading certainty;
- brand or editorial voice mismatch;
- emotional pressure that conflicts with editorial policy.

Social adaptation must not break tone consistency. If engagement goals conflict with tone or factual accuracy, the task must be routed to `blocked`, `changes_requested`, or Chief Editor escalation.

## factual requirements

Brevity does not cancel factual traceability.

Research is required when:

- factual claims are material to the post;
- the copy mentions dates, numbers, names, quotes, external events, policies, product behavior, or source-backed claims;
- factual sensitivity is medium, high, or critical;
- source freshness matters;
- review or Chief Editor requests more evidence.

If factual claims are used, traceability artifacts are required unless the confirmed low-risk or simple source-light standard mode and Chief Editor rationale allow compact evidence:

- `sources.md`;
- `facts.md`;
- `claims_table.md`;
- `claims-used.md`.

Rules:

- Writer Agent must not invent facts for engagement;
- unsupported claims cannot be used as facts;
- contradicted claims cannot be used as facts;
- uncertain claims can be used only with caveat;
- short-form compression must not remove a caveat that is needed for accuracy;
- `claims-used.md` must show how each factual claim was used in the draft when claims traceability is required.

If evidence is insufficient, route back to `research`, set `blocked`, or escalate.

## brevity requirements

Brevity is required only within the platform and task constraints. It must not reduce accuracy, clarity, or governance.

Writer Agent must:

- keep the draft concise for the selected platform;
- avoid unnecessary background when task context is intentionally reduced;
- preserve the core claim, caveats, and CTA constraints;
- avoid oversimplification that changes meaning;
- record removed context when removal creates risk;
- document unresolved compression risks in `writer-notes.md`.

Review Agent must check whether short-form compression has created ambiguity, factual distortion, clickbait drift, missing caveats, or tone drift.

## review requirements

Review is mandatory before finalization.

Review Agent must validate:

- compliance with `brief.md`;
- compliance with `AGENTS.md`;
- compliance with `orchestration_plan.md`;
- Social Pipeline compliance;
- review-gate integrity;
- reviewer independence from Writer Agent;
- required artifact completeness;
- factual traceability, if factual claims are used;
- correct use of `claims_table.md` and `claims-used.md`, when present;
- tone consistency;
- platform adaptation;
- brevity without factual distortion;
- absence of clickbait drift;
- absence of unsupported or contradicted claims presented as facts;
- caveats for uncertain claims;
- editorial relevance to the current material, issue, release, campaign, hero, topic, or change named in the brief;
- release-specific information value: what the reader learns about this material that would not be true of the format in general;
- replaceability risk as `low`, `medium`, or `high`;
- absence of inherited-purpose substitution, where the text uses the general purpose of a magazine, rubric, event, or format as the hook for a specific issue;
- absence of dead closing phrases unless the closing line contains a concrete action, location, deadline, or useful meaning;
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

The task must not enter `approved` if `review.md` is missing, review is not independent, checked artifacts are not listed, platform adaptation breaks factual meaning, tone drift is unresolved, unsupported claims are used as facts, or critical issues remain open.

For announcements, issue notes, release notes, and other short-form materials tied to a specific current item, `review.md` must include a compact editorial relevance block:

- what is unique to this material;
- where the actual editorial angle appears;
- whether the text speaks about the current material or about the format, rubric, or product in general;
- whether there is release-specific information value;
- whether the stated topic is developed;
- whether the draft substitutes the topic with the inherited purpose of the format.

The Review Agent must run a replaceability test when the brief names a specific topic, issue, hero, release, or campaign:

- replace the topic with a plausible alternative;
- estimate how much text still works;
- mark replaceability risk `low`, `medium`, or `high`;
- request changes if high replaceability risk means the current angle is missing.

When selecting among variants, Review Agent must prefer the version with the strongest release-specific angle and lowest inherited-purpose substitution, not merely the calmest, warmest, least HR-like, or most editorially polished version.

When a separate `qa-checklist.md` is created for these tasks, it must include:

- text reveals the specific material's topic, not only the general purpose of the format;
- at least one release-specific reason to read is present;
- replaceability risk is assessed;
- the final phrase is not a dead closing phrase;
- the base function of the magazine, rubric, format, event, or product is not used as the main hook unless it changed;
- accurate, calm, and human copy is still flagged when it is generic.

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
- finalization must not introduce new claims, new tone direction, new platform strategy, or changed meaning;
- finalization must not remove required caveats;
- unresolved risks must remain visible in `finalization-notes.md`;
- finalization does not grant publication, delivery, release, or governance approval.

If finalization needs new facts, strategy changes, platform changes, or unresolved review decisions, stop and route back to `research`, `writing`, `review`, `blocked`, or `human_approval_required` as allowed by `/kb/task_statuses.md`.

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
- finalization did not bypass review or introduce unsupported changes;
- tone, platform, factual, and caveat blockers are resolved or explicitly carried as approved caveats;
- editorial relevance and replaceability checks are present in review when the brief names a specific current material, release, issue, hero, campaign, or topic;
- human approval requirements from `brief.md`, `status.md`, `review.md`, or `finalization-notes.md` are satisfied or the task is moved to `human_approval_required`;
- no unresolved blocker prevents closure.

Publication, delivery, or release requires human approval when required by `brief.md`, `status.md`, `review.md`, `finalization-notes.md`, or `final_decision.md`. Human approval must be artifact-backed in `status.md` or `approval.md`; it must not be inferred from chat memory.

## handoff requirements

Every role transition normally creates a handoff file following `/templates/artifacts/handoff_template.md`. Compact execution may omit the finalization-to-Chief-Editor handoff only when `task-manifest.md` is current and no blocker, traceability need, governance escalation, contradiction, version conflict, evidence dispute, reviewer uncertainty, or human approval complexity exists.

Expected handoffs:

- `handoff-intake-intake-agent-to-chief-editor.md`;
- `handoff-planning-chief-editor-to-research-agent.md`, when research is required;
- `handoff-planning-chief-editor-to-writer-agent.md`, when writing can begin;
- `handoff-research-research-agent-to-chief-editor.md` or `handoff-research-research-agent-to-writer-agent.md`;
- `handoff-writing-writer-agent-to-review-agent.md`;
- `handoff-review-review-agent-to-chief-editor.md`;
- `handoff-review-review-agent-to-writer-agent.md`, when changes are requested from Writer Agent;
- `handoff-review-review-agent-to-research-agent.md`, when more research is required;
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
| Intake gate | `brief.md` and `status.md` exist with task goal, audience, platform, constraints, and `TASK-ID` | missing or ambiguous brief |
| Orchestration gate | `orchestration_plan.md` selects Social Pipeline, assigns roles, and records research/platform/tone needs | missing plan, invalid role, unclear constraints |
| Platform gate | target platform and constraints are known or explicitly documented as not applicable | missing platform constraints that affect copy |
| Tone gate | tone sources are loaded and tone drift risks are documented | missing tone source, clickbait drift, voice mismatch |
| Research gate | research artifacts exist when factual claims are used | unsupported, contradicted, stale, or missing evidence |
| Brevity gate | draft is concise without distorting facts, caveats, or tone | oversimplification, missing caveat, misleading compression |
| Writing gate | `draft.md` and `claims-used.md` when needed exist and avoid unsafe claims | invented facts or missing claim traceability |
| Editorial relevance gate | the text carries the specific material's topic, angle, change, issue, release, or hero rather than only the inherited purpose of the format | generic copy, high replaceability risk, missing release-specific value, inherited-purpose hook |
| Review gate | `review.md` outcome is `approved` with checked artifacts listed and editorial relevance checks completed | missing review, non-independent review, unresolved critical issues, missing replaceability test |
| Finalization gate | `final.md` and required finalization evidence exist after approved review | finalization before review, missing current manifest state, or new unsupported claims |
| Governance gate | `final_decision.md` validates finalization and human approval requirements | missing approval, unresolved blocker, missing final decision |

Failure at any gate must keep the task in the current valid status, move it to `changes_requested`, `research`, `blocked`, or `human_approval_required`, or follow retry policy.

## escalation rules

Escalate to Chief Editor or user when:

- instructions conflict;
- required task artifacts are missing and cannot be safely created by the current role;
- selected pipeline conflicts with `AGENTS.md`;
- target platform, audience, CTA, or length constraints are unclear;
- platform optimization would require factual distortion or clickbait drift;
- tone requirements conflict with engagement goals;
- factual claims are unavailable, unsupported, contradicted, or too uncertain;
- source freshness or reliability is insufficient for task risk;
- Writer Agent is asked to invent facts, approve, review, finalize, publish, or deliver;
- Review Agent independence cannot be established;
- review blocks finalization;
- finalization would require new facts, new platform strategy, or review override;
- human approval is required;
- retry policy is exhausted.

Escalation must include:

- blocking issue;
- affected files, platform constraints, claims, sources, or instructions;
- why safe continuation is impossible;
- smallest decision needed;
- recommended operational status;
- recommended next role.

## blocked conditions

Set or recommend `blocked` when any of these prevent safe continuation:

- missing or invalid `TASK-ID`;
- missing `brief.md`, `status.md`, or `orchestration_plan.md`;
- selected pipeline conflicts with `AGENTS.md`;
- required agent spec, KB file, tone file, or pipeline file is unavailable;
- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
- platform constraints are missing and materially affect copy;
- tone requirements conflict and cannot be resolved by the current role;
- platform adaptation would create clickbait drift, factual distortion, or misleading compression;
- research is required but research artifacts are missing or insufficient;
- factual claims are required but `sources.md`, `facts.md`, or `claims_table.md` is missing;
- Writer Agent would need to invent facts for engagement;
- unsupported or contradicted claims are required by the brief and cannot be removed or caveated;
- review is missing, non-independent, or blocked;
- finalization is requested before approved review;
- human approval is required but absent;
- status transition cannot be reconciled with `/kb/task_statuses.md`;
- context fragmentation prevents reliable continuation and cannot be repaired with `context-summary.md`.

Blocked status must be recorded in `status.md` using the format from `/kb/task_statuses.md`.

## retry policy

Follow `/kb/task_statuses.md`.

Retryable cases:

- incomplete handoff;
- missing optional stage note;
- formatting error;
- draft too long for known platform constraints;
- incomplete claim usage table;
- recoverable tone drift;
- recoverable platform adaptation issue;
- recoverable source gap;
- review changes that can be addressed by Writer Agent or Research Agent;
- context fragmentation repairable through `context-summary.md`.

Non-retryable without escalation:

- instruction conflict;
- impossible factual requirement;
- missing human decision;
- request to bypass review;
- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
- repeated failure caused by unclear platform constraints;
- review-gate failure that requires a governance decision.

Retry rules:

- after the first failed attempt, document the issue and retry once;
- after the second failed attempt on the same issue, set or recommend `blocked`;
- after three failed attempts on the same production stage, set or recommend `failed` unless the user or Chief Editor changes constraints;
- each retry must preserve previous meaningful artifacts or use versioned filenames when comparison matters.

## completion conditions

Social Pipeline is complete only when:

- required task artifacts exist in `/tasks/TASK-ID/`;
- `brief.md`, `task-manifest.md`, `status.md`, and `orchestration_plan.md` are current;
- research artifacts exist if research was required;
- source, fact, claim, and claims-used artifacts exist if factual claims were used;
- `draft.md` exists;
- independent `review.md` exists and outcome is `approved`;
- `qa-checklist.md` exists when separate checklist depth is required, otherwise checks are embedded in `review.md`;
- `review-summary.md` exists when needed for concise governance transfer;
- `final.md` exists and was created by `final_editor` after approved review;
- `finalization-notes.md` exists when controlled changes or unresolved risks need to be recorded;
- `finalization-checklist.md` exists when high-governance depth, downstream governance, traceability proof, task-specific requirement, or Chief Editor requires it;
- `final_decision.md` exists and was created by `chief_editor`;
- `status.md` records a valid final state under `/kb/task_statuses.md`;
- human approval is documented if required by brief, status, review, finalization notes, or final decision;
- no unresolved blocker prevents closure.

Completion means the social workflow is artifact-complete and governance-closed. It does not imply publication, delivery, or release unless required human approval is explicitly documented.

## restart protocol

After context loss, continue from artifacts, not chat history.

Receiving or restarting agents use the short context path from `/kb/shared_lifecycle_kernel.md` and `AGENTS.md`:

1. `AGENTS.md` or a short reference to its active invariants.
2. `/tasks/TASK-ID/task-manifest.md`.
3. The latest relevant handoff file.
4. The current working artifact.
5. Only `/pipelines/social_pipeline.md`, `/pipelines/research_pipeline.md`, KB, or editorial knowledge directly needed for the next action.

Do not read all pipelines, all agent specs, all old task folders, all retrospectives, all versions, or the full project tree by default.

Expanded reading is allowed for high-governance, conflict, or restart uncertainty. In that case read the exact source/evidence files, `status.md`, review trail, governance artifacts, or old versions needed to resolve the risk.

Then perform this restart check:

- confirm `TASK-ID`;
- confirm the current-version pointer names the active artifact when multiple versions exist;
- do not use latest modified time as the current-version source;
- stop and ask Chief Editor if current version state is unclear;
- confirm current status is valid under `/kb/task_statuses.md`;
- confirm the selected pipeline is Social Pipeline;
- confirm current owner role and next role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
- compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
- identify the last completed quality gate;
- verify required artifacts for that gate;
- identify missing, stale, unsupported, or contradicted factual claims;
- identify unresolved tone drift, platform adaptation, or brevity risks;
- continue from the next incomplete stage or set/recommend `blocked`.

Model memory, prior chat, or unsaved notes must not be used as evidence, approval, review outcome, platform constraint, tone authority, or workflow state.
