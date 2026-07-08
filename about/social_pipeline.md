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

Role legality and extension-role bounds are governed by `AGENTS.md`. This table
only maps Social Pipeline responsibilities to current roles.

| Stage | Required role | Agent spec | Responsibility |
| --- | --- | --- | --- |
| Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, platform target, audience, constraints, and missing information |
| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
| Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
| Writing | `writer_agent` | `/agents/writer_agent.md` | Create platform-adapted short-form draft and claim usage notes |
| Review | `review_agent` | `/agents/review_agent.md` | Independently validate copy, artifacts, tone, traceability, and governance compliance |
| Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |

Revision in the current operating model is handled by `writer_agent` for copy
changes or `research_agent` for evidence gaps, not by a separate editing role.

## required inputs

Pipeline execution follows `/kb/shared_lifecycle_kernel.md` stage context
contracts and `AGENTS.md` short context loading policy. Load the shared task
packet from those owners, then add only social-specific context:

- this pipeline file;
- `/pipelines/research_pipeline.md`, when research or factual claims are used;
- `/agents/writer_agent.md` and other assigned role specs when needed by the
  active stage;
- tone, policy, platform, client-profile, handoff, and source files named by
  task artifacts.

If `TASK-ID`, `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, or required platform constraints are missing, production must not continue until Chief Editor creates or repairs the missing artifact, or the task is set to `blocked`.

## required artifacts

Shared task artifacts and ownership are defined in `AGENTS.md`,
`/kb/task_object_model.md`, and `/kb/shared_lifecycle_kernel.md`. Social
Pipeline adds these task-type views when the selected depth requires them:

- `draft.md` for social copy or variants;
- `writer-notes.md`, when platform, tone, CTA, or compression decisions affect
  review;
- `claims-used.md`, when factual claims require traceability;
- social research artifacts when research or factual claims require them.

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

For low-risk and simple source-light standard tasks, use
`/kb/compact_execution.md` to apply compact execution without weakening
review-gate. Chief Editor must record the compact rationale; `review.md`
remains required before finalization; optional artifacts are not created
automatically. Review Agent should not require optional artifacts when core
traceability, restartability, and governance evidence are sufficient.

Use `/kb/research_evidence.md` when deciding whether a short-form task is
`no-research`, `compact-evidence`, or `full-evidence`. Do not create
`sources.md`, `facts.md`, or `claims_table.md` automatically for low-risk
no-claim tasks. Material claims that enter the draft should be reflected in
`claims-used.md` or equivalent compact evidence.

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

Use only statuses from `/kb/task_statuses.md`. For social work, the
task-specific production status is `writing`; `editing` remains only the
optional revision/status bridge defined by the status owner.

No stage may merge writing with review or finalization with Chief Editor
governance. Short-form speed must not bypass governance.

## stage sequence

Default production sequence:

```text
intake -> chief_editor orchestration -> research if needed -> writing -> review -> finalization -> chief_editor final governance decision
```

Social-specific route:

1. Chief Editor selects Social Pipeline and confirms platform, tone, and
   factual risk.
2. Research runs only when evidence or factual claims require it.
3. Chief Editor confirms research sufficiency or no-research rationale.
4. Writer Agent creates social copy or variants from approved constraints.
5. Review Agent independently reviews the current social package.
6. Final Editor finalizes only after approved review.
7. Chief Editor records the final governance decision.

Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate editing role.

## status transitions

Operational statuses and transitions are owned by `/kb/task_statuses.md`.
Social-specific transition notes:

- route to `research` when social copy needs evidence, otherwise to `planning`;
- route from `planning` to `writing` only after platform, tone, and evidence
  inputs are sufficient;
- route from `writing` to `review` after required social writing artifacts and
  handoff exist;
- route `changes_requested` findings back to `writing`, `research`, or
  `review` according to the repair owner and re-review scope;
- route from `approved` toward finalization/governance only under the shared
  review-gate and human-approval rules.

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

Use `/kb/research_evidence.md` to choose the smallest reviewable evidence mode.
Low-risk no-claim social tasks can record a no-research rationale instead of
creating research artifacts. Source-light tasks may use compact evidence when
Review Agent can trace material claims without a full research dump.

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

Handoff behavior is owned by `AGENTS.md`,
`/kb/shared_lifecycle_kernel.md`, and
`/templates/artifacts/handoff_template.md`. Social handoffs normally connect
Chief Editor, Research Agent when used, Writer Agent, Review Agent, Final
Editor, and Chief Editor governance. Handoffs must point to current social
variants, platform constraints, claim caveats, and blockers when material.

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

Social Pipeline is complete only when the shared lifecycle and status owners
allow closure, and the social-specific packet is current:

- required social draft or variant artifacts exist;
- required platform, tone, factual, and claim-use evidence exists when used;
- independent `review.md` approves the current social package, including
  relevance/replaceability checks when required;
- finalization and Chief Editor governance artifacts exist when required;
- human approval and blockers are resolved or explicitly carried by the
  governing status.

Completion means the social workflow is artifact-complete and governance-closed. It does not imply publication, delivery, or release unless required human approval is explicitly documented.

## restart protocol

Restart behavior is owned by `AGENTS.md` and
`/kb/shared_lifecycle_kernel.md`. For Social Pipeline restarts, add only these
checks to the shared restart packet:

- selected pipeline is Social Pipeline;
- current social variant/version and platform constraints are identified;
- unresolved tone, platform, brevity, relevance, or replaceability risks are
  visible;
- required social research artifacts are present when research was required;
- the last completed social quality gate is clear.
