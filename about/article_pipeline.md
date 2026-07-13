# Article Pipeline

## pipeline purpose

This pipeline governs creation of article-style editorial materials:

- articles;
- longreads;
- explainers;
- analytical texts;
- editorial content;
- knowledge content.

The pipeline turns a task brief into a reviewed and finalized article
deliverable through controlled intake, orchestration, optional research,
writing, review, finalization, and Chief Editor governance. When teaching,
understanding, or complex explanation is material, it also preserves the
approved Reader Model transition and Learning Design without adding a role or
artifact.

The pipeline is markdown-first, artifact-backed, and restartable from `/tasks/TASK-ID/` without chat history.

## when to use

Use this pipeline when the requested output is an article-like text that needs editorial structure, source-aware writing, and review before finalization.

Use it when:

- the deliverable is a publishable or deliverable editorial text;
- the output needs a clear argument, explanation, narrative, or knowledge structure;
- factual claims may be used and must remain traceable;
- research may be required before drafting;
- the task needs Writer Agent drafting and independent Review Agent validation;
- the task needs Final Editor controlled finalization and Chief Editor final governance decision.

## when not to use

Do not use this pipeline when:

- the task is only research and does not require a draft article;
- the task is only UX writing, interface copy, product microcopy, or content design;
- the task is only review of an existing material;
- the task is only finalization after an already approved review, unless Chief Editor selects this pipeline as governing context;
- the task is social-only short-form content governed by `/pipelines/social_pipeline.md`;
- the task can be completed as non-factual formatting or file cleanup;
- the request would require bypassing research, review, finalization, or governance rules.

If the task is ambiguous, Chief Editor must record the pipeline choice and rationale in `/tasks/TASK-ID/orchestration_plan.md`.

## required agents

Role legality and extension-role bounds are governed by `AGENTS.md`. This table
only maps Article Pipeline responsibilities to current roles.

| Stage | Required role | Agent spec | Responsibility |
| --- | --- | --- | --- |
| Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize raw request into task artifacts |
| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
| Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
| Writing | `writer_agent` | `/agents/writer_agent.md` | Create outline, draft, writer notes, and claims-used |
| Review | `review_agent` | `/agents/review_agent.md` | Independently validate draft and artifacts |
| Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |

Revision in the current operating model is handled by `writer_agent`, not by a
separate Editor role.

## required inputs

Pipeline execution follows `/kb/shared_lifecycle_kernel.md` stage context
contracts and `AGENTS.md` short context loading policy. Load the shared task
packet from those owners, then add only article-specific context:

- this pipeline file;
- `/pipelines/research_pipeline.md`, when research is required or factual claims
  are used;
- `/agents/writer_agent.md` and other assigned role specs when needed by the
  active stage;
- relevant KB, client-profile, handoff, and source files named by the task
  artifacts.
- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
  Transformation, and approved Learning Design sequence when material.

If `TASK-ID`, `brief.md`, `task-manifest.md`, `status.md`, or `orchestration_plan.md` is missing, production must not continue until Chief Editor creates or repairs the missing artifact, or sets the task to `blocked`.

## required artifacts

Shared task artifacts and ownership are defined in `AGENTS.md`,
`/kb/task_object_model.md`, and `/kb/shared_lifecycle_kernel.md`. Article
Pipeline adds these task-type views when the selected depth requires them:

- `outline.md`;
- `draft.md`;
- `writer-notes.md`, when assumptions, caveats, or decisions affect review;
- `claims-used.md`, when factual claims require traceability;
- article research artifacts when research or factual claims require them.

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

For low-risk and simple source-light standard tasks, use
`/kb/compact_execution.md` to apply compact execution without weakening
review-gate. Chief Editor must record the compact rationale; `review.md`
remains required before finalization; optional artifacts are not created
automatically. Review Agent should not require optional artifacts when core
traceability, restartability, and governance evidence are sufficient.

Use `/kb/research_evidence.md` when deciding whether an article task is
`no-research`, `compact-evidence`, or `full-evidence`. Do not create
`sources.md`, `facts.md`, or `claims_table.md` automatically for low-risk
no-claim tasks. Material claims that enter the draft should be reflected in
`claims-used.md` or equivalent compact evidence.

### required artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `brief.md` | Defines task goal, audience, scope, acceptance criteria | all roles | never for active tasks |
| `task-manifest.md` | Compact current state and restart anchor | all roles | never for new tasks |
| `status.md` | Detailed status/history and transition rationale | all roles, Chief Editor | never for active tasks |
| `orchestration_plan.md` | Execution contract, roles, gates, artifact scope | all roles | never after orchestration starts |
| `draft.md` | Material under review | review_agent, final_editor | never for article production |
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

Use only statuses from `/kb/task_statuses.md`. For article work, the
task-specific production status is `writing`; `editing` remains only the
optional revision/status bridge defined by the status owner.

No stage may merge writing with review or finalization with Chief Editor
governance.

## stage sequence

Default production sequence:

```text
intake -> chief_editor orchestration -> research if needed -> writing -> review -> finalization -> chief_editor final governance decision
```

Article-specific route:

1. Chief Editor selects Article Pipeline and confirms research need.
2. Research runs only when evidence or factual claims require it.
3. Chief Editor confirms research sufficiency or no-research rationale.
4. Writer Agent creates article writing artifacts.
5. Review Agent independently reviews the current draft package.
6. Final Editor finalizes only after approved review.
7. Chief Editor records the final governance decision.

Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate Editor role.

## status transitions

Operational statuses and transitions are owned by `/kb/task_statuses.md`.
Article-specific transition notes:

- route to `research` when article evidence is required, otherwise to
  `planning`;
- route from `planning` to `writing` only after article inputs are sufficient;
- route from `writing` to `review` after required article writing artifacts and
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
- compact execution may be used when Chief Editor records the profile, rationale, review target, and intentionally omitted artifacts;
- review is still required, but checklist may be compact inside `review.md`;
- Reader Review is `compact` for a simple reader transfer; a complex teaching
  outcome may require `normal` despite low factual risk;
- finalization may use compact shape: `review.md`, `final.md`, current `task-manifest.md`, and optional short handoff only if needed.

`standard`:

- use normal Article Pipeline requirements;
- research is required when factual claims are present;
- claims traceability is required when claims are material;
- simple source-light standard tasks may keep checklist and summary content inside `review.md` when no downstream consumer, high-governance need, task-specific requirement, blocker/open-question state, or traceability need requires separate files.
- Reader Review is normally `normal` when reader change is material and
  `not applicable` when it is not.

`high-governance`:

- research is required;
- `sources.md`, `facts.md`, and `claims_table.md` are required;
- `claims-used.md` is required;
- review must be full;
- Reader Review is `full` when the article teaches, updates a mental model, or
  justifies a Bounded Utility Tradeoff; otherwise record the applicable depth.
- `finalization-checklist.md` is required;
- human approval must be assessed explicitly;
- Chief Editor must not finalize governance without an explicit decision on approval.

## research requirements

Research is required when:

- factual claims are material to the article;
- factual sensitivity is medium, high, or critical;
- the brief names sources, data, people, dates, numbers, policies, product behavior, or external events;
- source freshness matters;
- the draft would otherwise require Writer Agent to invent facts;
- review or Chief Editor requests additional evidence.

Use `/kb/research_evidence.md` to choose the smallest reviewable evidence mode.
Low-risk no-claim article tasks can record a no-research rationale instead of
creating research artifacts. Source-light tasks may use compact evidence when
Review Agent can trace material claims without a full research dump.

When research is required, Article Pipeline must use `/pipelines/research_pipeline.md` as upstream context.

Required research outputs:

- `research.md`;
- `sources.md`, if factual claims are used;
- `facts.md`, if factual claims are used;
- `claims_table.md`, if factual claims are used;
- `open-questions.md`, when questions remain;
- research handoff.

Research must separate facts, interpretations, assumptions, contradictions, and open questions. Model memory is not verified evidence. Unsupported or contradicted claims cannot be used as facts. Uncertain claims can be used only with caveat.

If research is insufficient, the task must not move to writing as ready for drafting.

## writing requirements

Writer Agent must write only from:

- `brief.md`;
- `orchestration_plan.md`;
- approved KB context;
- research artifacts when factual claims are used;
- the latest relevant handoff.

Writer Agent creates only the writing artifacts required by risk mode and downstream review:

- `outline.md`;
- `draft.md`;
- `writer-notes.md`, when assumptions, caveats, or decisions affect review;
- `claims-used.md`, if factual claims are used or high-governance traceability is required;
- writing handoff.

Writing rules:

- writing does not replace research;
- Writer Agent must not invent facts, sources, examples, dates, links, names, or statistics;
- unsupported and contradicted claims must not be used as facts;
- uncertain claims may be used only with explicit caveat;
- the draft must not claim to be approved, final, published, or ready for delivery;
- factual claims used in the draft must be traceable through `claims-used.md`, `claims_table.md`, `facts.md`, or `sources.md`;
- teaching/explanation must realize the approved reader transition and use only
  supported or clearly labeled illustrative examples;
- if a needed claim is unsafe, Writer Agent must stop and recommend `research`, `blocked`, or escalation.

## review requirements

Review is mandatory before finalization.

Review Agent must validate:

- compliance with `brief.md`;
- compliance with `AGENTS.md`;
- compliance with `orchestration_plan.md`;
- Article Pipeline compliance;
- review-gate integrity;
- reviewer independence from Writer Agent;
- required artifact completeness;
- factual traceability;
- correct use of `claims_table.md` and `claims-used.md`, when factual claims are used;
- absence of unsupported or contradicted claims presented as facts;
- caveats for uncertain claims;
- approved Reader Model transition and Learning Design when material;
- tone, structure, glossary, and editorial policy compliance;
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

The task must not enter `approved` if `review.md` is missing, review is not independent, checked artifacts are not listed, critical issues remain open, or factual traceability is insufficient.

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
- finalization must not introduce new claims, change meaning, remove required caveats, or override review;
- unresolved risks must remain visible in `finalization-notes.md`;
- finalization does not grant publication approval or governance approval.

If finalization needs new facts, strategy changes, or unresolved review decisions, stop and route back to `research`, `writing`, `review`, `blocked`, or `human_approval_required` as allowed by `/kb/task_statuses.md`.

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
- human approval requirements from `brief.md`, `status.md`, `review.md`, or `finalization-notes.md` are satisfied or the task is moved to `human_approval_required`;
- no unresolved blocker prevents closure.

Publication or delivery requires human approval when required by `brief.md`, `status.md`, `review.md`, `finalization-notes.md`, or `final_decision.md`. Human approval must be artifact-backed in `status.md` or `approval.md`; it must not be inferred from chat memory.

## handoff requirements

Handoff behavior is owned by `AGENTS.md`,
`/kb/shared_lifecycle_kernel.md`, and
`/templates/artifacts/handoff_template.md`. Article handoffs normally connect
Chief Editor, Research Agent when used, Writer Agent, Review Agent, Final
Editor, and Chief Editor governance. Handoffs must point to current article
artifacts and never replace them.

## quality gates

Quality gates are mandatory and artifact-backed.

| Gate | Passed only when | Blocking evidence |
| --- | --- | --- |
| Intake gate | `brief.md` and `status.md` exist with task goal, audience, output, constraints, and `TASK-ID` | missing or ambiguous brief |
| Orchestration gate | `orchestration_plan.md` selects Article Pipeline, assigns roles, records research need, and includes the reader transition when material | missing plan, invalid role, or missing material Reader Model contract |
| Research gate | required research artifacts exist and claims are safe, unsafe, or caveated | unsupported, contradicted, stale, or missing evidence |
| Writing gate | `outline.md`, `draft.md`, and `claims-used.md` when needed exist, avoid unsafe claims, and realize the approved reader transition when material | invented facts, missing claim traceability, or broken material Cognitive Bridge |
| Review gate | `review.md` outcome is `approved` with checked artifacts listed | missing review, non-independent review, unresolved critical issues |
| Finalization gate | `final.md` and required finalization evidence exist after approved review | finalization before review, missing current manifest state, or new unsupported claims |
| Governance gate | `final_decision.md` validates finalization and human approval requirements | missing approval, unresolved blocker, missing final decision |

Failure at any gate must keep the task in the current valid status, move it to `changes_requested`, `research`, `blocked`, or `human_approval_required`, or follow retry policy.

## escalation rules

Escalate to Chief Editor or user when:

- instructions conflict;
- required task artifacts are missing and cannot be safely created by the current role;
- the pipeline conflicts with `AGENTS.md`;
- a role is asked to exceed its decision boundary;
- factual claims are unavailable, unsupported, contradicted, or too uncertain for the requested output;
- source freshness or reliability is insufficient for task risk;
- Writer Agent is asked to invent facts, approve, review, finalize, publish, or deliver;
- Review Agent independence cannot be established;
- review blocks finalization;
- finalization would require new facts, new strategy, or review override;
- human approval is required;
- retry policy is exhausted.

Escalation must include:

- blocking issue;
- affected files, claims, sources, or instructions;
- why safe continuation is impossible;
- smallest decision needed;
- recommended operational status;
- recommended next role.

## blocked conditions

Set or recommend `blocked` when any of these prevent safe continuation:

- missing or invalid `TASK-ID`;
- missing `brief.md`, `status.md`, or `orchestration_plan.md`;
- selected pipeline conflicts with `AGENTS.md`;
- required agent spec, KB file, or pipeline file is unavailable;
- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
- research is required but research artifacts are missing or insufficient;
- factual claims are required but `sources.md`, `facts.md`, or `claims_table.md` is missing;
- Writer Agent would need to invent facts to continue;
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
- incomplete outline or draft;
- recoverable source gap;
- review changes that can be addressed by Writer Agent or Research Agent;
- context fragmentation repairable through `context-summary.md`.

Non-retryable without escalation:

- instruction conflict;
- impossible factual requirement;
- missing human decision;
- request to bypass review;
- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
- repeated failure caused by unclear brief;
- review-gate failure that requires a governance decision.

Retry rules:

- after the first failed attempt, document the issue and retry once;
- after the second failed attempt on the same issue, set or recommend `blocked`;
- after three failed attempts on the same production stage, set or recommend `failed` unless the user or Chief Editor changes constraints;
- each retry must preserve previous meaningful artifacts or use versioned filenames when comparison matters.

## completion conditions

Article Pipeline is complete only when the shared lifecycle and status owners
allow closure, and the article-specific packet is current:

- required article writing artifacts exist;
- required research/claim artifacts exist when research or factual claims were
  used;
- independent `review.md` approves the current draft package;
- finalization and Chief Editor governance artifacts exist when required;
- human approval and blockers are resolved or explicitly carried by the
  governing status.

Completion means the article workflow is artifact-complete and governance-closed. It does not imply publication or delivery unless required human approval is explicitly documented.

## restart protocol

Restart behavior is owned by `AGENTS.md` and
`/kb/shared_lifecycle_kernel.md`. For Article Pipeline restarts, add only these
checks to the shared restart packet:

- selected pipeline is Article Pipeline;
- current article draft, outline, and claim-use artifacts are identified when
  applicable;
- required article research artifacts are present when research was required;
- the last completed article quality gate is clear.
