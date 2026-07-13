# Research Pipeline

## pipeline purpose

This pipeline creates a verified, traceable evidence base for a task before downstream writing, UX writing, review, finalization, or editorial decision-making.

The pipeline is production research only. It does not create publishable copy, final wording, review approval, finalization artifacts, or governance decisions.

The pipeline must produce task-local markdown artifacts that let Writer Agent, UX Writer, Review Agent, Final Editor, or Chief Editor continue without relying on chat history or model memory.

Use `/kb/research_evidence.md` to choose the evidence mode:
`no-research`, `compact-evidence`, or `full-evidence`. Evidence depth is
conditional and claim-driven, not automatic.

## when to use

Chief Editor selects this evidence pipeline only after the intended outcome and
selected deliverable are known enough to define what evidence that deliverable
needs. Research need does not decide the final artifact format retroactively.

Use this pipeline when any of these are true:

- the task needs factual claims, dates, names, numbers, quotes, product behavior, policy details, market context, or source-backed reasoning;
- the task has medium, high, or critical factual sensitivity;
- downstream `writer_agent` or `ux_writer` needs an evidence base before drafting;
- `review_agent` needs additional factual evidence before review can pass;
- `final_editor` or `chief_editor` needs verified facts before finalization or governance decision;
- existing sources conflict, are outdated, or have unknown freshness;
- user-provided material must be checked, summarized, classified, or separated from assumptions.

## when not to use

Do not use this pipeline when:

- the task is pure formatting, file organization, or non-factual cleanup;
- the task can be completed from an already approved `review.md` and existing source-backed artifacts;
- the user asks only for finalization after valid review approval;
- the task is intake normalization without research scope;
- the request is to write, rewrite, polish, or publish copy and required research already exists;
- using the pipeline would bypass a required writing, review, finalization, or governance stage.

If evidence is already sufficient, Chief Editor may skip this pipeline and document the reason in `/tasks/TASK-ID/orchestration_plan.md`.

For low-risk tasks with no factual, product, policy, numeric, legal, HR,
security, regulatory, medical, financial, or reputational claims, Chief Editor
may record a `no-research` rationale instead of creating research artifacts.

## required agents

Role legality and extension-role bounds are governed by `AGENTS.md`. This table
only maps Research Pipeline responsibilities to current roles.

| Stage responsibility | Required role | Agent spec |
| --- | --- | --- |
| Intake package, if not already complete | `intake_agent` | `/agents/intake_agent.md` |
| Deliverable-first pipeline selection and status governance | `chief_editor` | `/agents/chief_editor.md` |
| Research execution | `research_agent` | `/agents/research_agent.md` |
| Downstream drafting, if research is sufficient for article or editorial copy | `writer_agent` | `/agents/writer_agent.md` |
| Downstream UX copy, if research is sufficient for product-language work | `ux_writer` | `/agents/ux_writer.md` |
| Downstream independent verification of drafted material | `review_agent` | `/agents/review_agent.md` |
| Downstream controlled finalization after approved review | `final_editor` | `/agents/final_editor.md` |

This pipeline does not change role authority. It only routes research evidence
to the current owner of the next valid stage.

## required inputs

Research execution follows `/kb/shared_lifecycle_kernel.md` stage context contracts and `AGENTS.md` short context loading policy. Use these inputs only when they are relevant to the current stage or required by the selected depth:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/tasks/TASK-ID/brief.md`;
- `/tasks/TASK-ID/task-manifest.md`;
- `/tasks/TASK-ID/status.md`;
- `/tasks/TASK-ID/orchestration_plan.md`;
- the latest relevant handoff file, if present;
- this file: `/pipelines/research_pipeline.md`;
- `/agents/research_agent.md`;
- relevant KB files named in `orchestration_plan.md` or required by the task;
- user-provided sources, files, links, notes, or source material, if any.

If a required input is missing, `research_agent` must stop, record the missing input in `/tasks/TASK-ID/open-questions.md` or a failure note, and recommend `blocked` or `research` according to `/kb/task_statuses.md`. If the missing input requires a human decision, record that decision need inside the blocker.

`task-manifest.md` must be updated at every stage transition, status transition, owner change, blocker change, research artifact state change, and handoff creation. The research stage cannot be considered complete if `task-manifest.md` is stale. If `task-manifest.md`, `status.md`, latest handoff, and `orchestration_plan.md` conflict, stop and escalate to `chief_editor`.

## artifact set

The research stage may create or update these artifacts inside `/tasks/TASK-ID/`, subject to the artifact creation policy below:

- `/tasks/TASK-ID/task-manifest.md`;
- `/tasks/TASK-ID/research.md`;
- `/tasks/TASK-ID/sources.md`, when source traceability is required;
- `/tasks/TASK-ID/facts.md`, when fact-level extraction is required;
- `/tasks/TASK-ID/claims_table.md`, when claim-level validation is required;
- `/tasks/TASK-ID/open-questions.md`, when questions exist or are deferred;
- `/tasks/TASK-ID/handoff-research-research-agent-to-TO.md`.

`TO` must be replaced with the receiving core role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug. These slugs are not separate agent names:

- `writer-agent` for `writer_agent`;
- `ux-writer` for `ux_writer`;
- `review-agent` for `review_agent`;
- `final-editor` for `final_editor`;
- `chief-editor` for `chief_editor`.

Examples:

- `/tasks/TASK-ID/handoff-research-research-agent-to-writer-agent.md`;
- `/tasks/TASK-ID/handoff-research-research-agent-to-ux-writer.md`;
- `/tasks/TASK-ID/handoff-research-research-agent-to-chief-editor.md`.

The handoff is a navigation artifact only. It must not replace required research artifacts.

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

Use `/kb/research_evidence.md` when choosing whether the task needs
`no-research`, `compact-evidence`, or `full-evidence`. Research artifacts must
have a consumer, traceability purpose, review purpose, governance need, or
explicit task requirement.

Low-risk no-claim tasks can use a recorded no-research rationale instead of
`research.md`, `sources.md`, `facts.md`, or `claims_table.md`. High-governance
material claims require the full evidence set.

### required artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `task-manifest.md` | Compact current research state and artifact inventory | all roles | never for active tasks |
| `research.md` | Research summary, scope, contradictions, gaps, downstream guidance | writer_agent, ux_writer, review_agent, chief_editor | only when Chief Editor records that a compact evidence note elsewhere is enough for low-risk work |
| research handoff | Delta-transfer to next valid role | receiving role | only when no role transition occurs |

### conditional artifacts

| Artifact | Required when | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `sources.md` | source traceability is needed, factual sensitivity is material, or high-governance | writer_agent, review_agent, chief_editor | low-risk claims are absent or compact evidence note is explicitly sufficient |
| `facts.md` | fact-level extraction is needed, factual sensitivity is material, or high-governance | writer_agent, review_agent | low-risk task has no reusable factual base |
| `claims_table.md` | claim-level validation is needed, claims will be reused downstream, or high-governance | writer_agent, review_agent | no material claims need downstream validation |
| `open-questions.md` | real blocking or deferred questions, source gaps, unresolved decisions, or traceability needs exist | chief_editor, downstream owner | no questions, blockers, deferred decisions, or traceability gaps exist |
| `research-notes.md` | methodology, caveats, or source limitations do not fit compactly in `research.md` | chief_editor, review_agent | `research.md` already captures the needed operational detail |

### optional artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| versioned evidence notes | comparison matters across retries | review_agent, chief_editor | normal update history is enough |
| `failure.md` | research cannot complete under constraints | chief_editor | task is not failed |

## allowed stages

This pipeline may operate only across these stages:

- `intake`, only to confirm that the research scope exists;
- `research`, for evidence collection, classification, verification, and handoff;
- `planning`, when research is complete and Chief Editor must route the next stage;
- `writing`, only as the recommended downstream stage after Chief Editor routing;
- `review`, only as the recommended downstream stage when research is being supplied to support independent review;
- `human_approval_required`, only when reached through a valid transition in `/kb/task_statuses.md`;
- `blocked`, when safe continuation is impossible;
- `failed`, when research cannot be completed under current constraints.

Research stage work must not produce `outline.md`, `draft.md`, `ux-copy.md`, `review.md`, `final.md`, `finalization-notes.md`, or `final_decision.md`.

## stage sequence

| Step | Status before | Role | Action | Required outputs | Status after |
| --- | --- | --- | --- | --- | --- |
| 1 | `intake` or `planning` | `chief_editor` | Confirm research is required and record scope in `orchestration_plan.md` | `orchestration_plan.md`, `status.md`, optional handoff | `research` or `blocked` |
| 2 | `research` | `research_agent` | Load required context and define research scope | updated `research.md` or notes in `open-questions.md` | `research` or `blocked` |
| 3 | `research` | `research_agent` | Collect and classify sources | `sources.md` | `research` or `blocked` |
| 4 | `research` | `research_agent` | Extract facts, interpretations, assumptions, contradictions, and gaps | `research.md`, `facts.md`, `open-questions.md` | `research` |
| 5 | `research` | `research_agent` | Build claim-level traceability and draft-use guidance | `claims_table.md` | `research` or `blocked` |
| 6 | `research` | `research_agent` | Check sufficiency and create handoff to the next valid role | `handoff-research-research-agent-to-TO.md` | `planning`, `blocked`, or `failed` |

The receiving role depends on the orchestration plan:

- hand off to `writer_agent` for article, social, or editorial drafting;
- hand off to `ux_writer` for UX writing;
- hand off to `review_agent` when research fills evidence gaps for review;
- hand off to `final_editor` only when finalization needs source-backed clarification after review approval;
- hand off to `chief_editor` when sufficiency, scope, contradiction, or approval decisions are needed.

## status transitions

Operational statuses and direct transitions must come from `/kb/task_statuses.md`.

Allowed transitions for this pipeline:

| From | To | Trigger | Responsible role | Required evidence |
| --- | --- | --- | --- | --- |
| `intake` | `research` | Chief Editor selects this pipeline after intake | `chief_editor` | `orchestration_plan.md`, `status.md` |
| `planning` | `research` | Chief Editor assigns research stage | `chief_editor` | `orchestration_plan.md`, handoff |
| `research` | `planning` | Research is complete but editorial direction or downstream role must be chosen | `research_agent` recommends, `chief_editor` records | handoff to `chief_editor` |
| `research` | `blocked` | Missing input, source contradiction, role conflict, or insufficient evidence blocks safe continuation | current role | `status.md`, `open-questions.md` or failure note |
| `research` | `failed` | Research cannot be completed under current constraints after retry policy is exhausted | `chief_editor` | failure artifact |
| `changes_requested` | `research` | Review or revision found evidence gaps | `review_agent`, `writer_agent`, `ux_writer`, or `chief_editor` recommends | `review.md`, `qa-checklist.md`, handoff |
| `blocked` | `research` | Blocker is resolved and research can continue | current owner or `chief_editor` | updated `status.md` |

Research local outcomes must be recorded as recommendations, then converted through a transition valid under `/kb/task_statuses.md`.

| Research local outcome | Operational status |
| --- | --- |
| `research_ready_for_writing` | recommend `planning`, then Chief Editor routes to `writing` |
| `research_ready_for_ux_writing` | recommend `planning`, then Chief Editor routes to `writing` |
| `research_ready_for_review` | recommend `planning`, then Chief Editor routes through the next valid status toward `review` |
| `needs_more_research` | `research` |
| `blocked` | `blocked` |
| `human_approval_required` | recommend `blocked` with escalation details unless the current status model allows direct `human_approval_required` |

Local outcomes must not be written as operational task statuses.

## handoff requirements

Every research handoff must follow `/templates/artifacts/handoff_template.md` as a compact delta-handoff. It must reference `task-manifest.md`, summarize only what changed, list only artifacts created or updated, name active constraints for the next role, identify blockers or open questions that affect the next step, and state next role, next action, expected outputs, forbidden outputs, and escalation conditions.

The handoff must not repeat the full source list, claim table, KB list, manifest, status history, orchestration plan, restart checklist, or all research findings.

If research is insufficient, the handoff must not say or imply that drafting is ready. It must hand off to `chief_editor`, `research_agent`, or the appropriate blocker owner with a concrete next decision.

## risk mode behavior

Risk mode classification follows `AGENTS.md` and `/project-state.md`.

`low-risk` research may be a compact evidence note when factual claims are low-sensitivity and the Chief Editor records why separate `sources.md`, `facts.md`, and `claims_table.md` are not required.

`standard` research uses normal Research Pipeline artifacts when factual claims are present or material.

`high-governance` research requires separate `sources.md`, `facts.md`, and `claims_table.md`. High-governance research must preserve source freshness, reliability, claim status, caveats, contradictions, and downstream-use guidance as separate traceable artifacts.

## source requirements

All factual claims must trace back to `sources.md`, `facts.md`, or
`claims_table.md`.

Source type and proximity labels describe the origin and distance of a source
from the claim. They are not evidence classes. Canonical evidence classes and
confidence labels are owned by `/kb/editorial_evidence_framework.md`.

`sources.md` must use the structure defined in `/agents/research_agent.md` and include:

- source title;
- source type;
- source proximity/type label;
- link or local path;
- publication or update date;
- evidence freshness;
- reliability assessment;
- what the source was used for;
- limitations.

Allowed source proximity/type labels:

- `primary`;
- `secondary`;
- `tertiary`;
- `user-provided`;
- `inferred`;
- `model-memory`.

Evidence freshness must be:

- `current`;
- `recent`;
- `outdated`;
- `unknown`.

Model memory is not verified evidence. It may be recorded only as `model-memory` and must not support a claim marked `confirmed`.

Outdated or unknown-freshness sources must be marked. They cannot support high-risk or critical claims unless another current or independently verifiable source supports the claim.

## claims requirements

`claims_table.md` is a claim-level evidence and traceability view over task
state for downstream factual use.

Each claim must include:

- claim text;
- status;
- source evidence;
- confidence;
- factual sensitivity;
- whether it can be used in draft;
- notes for Writer or UX Writer;
- notes for Reviewer.

Allowed claim statuses:

- `confirmed`;
- `likely`;
- `uncertain`;
- `contradicted`;
- `unsupported`.

Allowed draft-use values:

- `yes`;
- `no`;
- `with caveat`.

Rules:

- unsupported claims cannot be used as facts;
- contradicted claims cannot be used as facts;
- uncertain claims can be used only with caveat;
- likely claims can be used only when the task risk allows it and the caveat need is recorded;
- confirmed claims must have traceable source evidence;
- critical factual sensitivity requires independently verifiable evidence;
- facts, interpretations, assumptions, and open questions must remain separate;
- assumptions must not be promoted to facts by downstream roles.

## sufficiency criteria

Research is sufficient only when all required conditions are met:

- all required artifacts exist and are current for the assigned scope;
- `research.md` separates confirmed facts, interpretations, assumptions, contradictions, gaps, and implications;
- `sources.md` lists checked sources with proximity/type label, freshness,
  reliability, use, and limitations;
- `facts.md` lists usable facts with source and confidence;
- `claims_table.md` marks every key claim with status, evidence, confidence, factual sensitivity, and draft-use guidance;
- `open-questions.md` marks which questions block downstream work, when real questions exist;
- unsupported and contradicted claims are marked `Can be used in draft: no`;
- uncertain claims are marked `Can be used in draft: with caveat` or `no`;
- critical factual sensitivity claims have independently verifiable evidence or are blocked for use;
- outdated or unknown-freshness evidence is not used to support high-risk claims without additional verification;
- contradictions that affect the task are documented and either resolved or escalated;
- downstream Writer or UX Writer can proceed without inventing missing core facts;
- Reviewer can trace factual claims back to sources without relying on chat history.

If any criterion fails, the pipeline is not ready for drafting. The next status must remain `research` or become `blocked`. If a human decision is required, document it as an escalation inside the blocker unless the current status model permits a direct transition to `human_approval_required`.

## escalation rules

Escalate to `chief_editor` or the user when:

- instructions conflict;
- required inputs or source materials are missing;
- source access is unavailable and the missing source is necessary;
- source reliability is too weak for the task risk level;
- sources contradict each other on a material point;
- facts required by the brief are unavailable or unverifiable;
- freshness is unknown for a source needed for a high-risk claim;
- a critical factual sensitivity claim lacks independently verifiable evidence;
- the research scope is too broad or ambiguous to complete deterministically;
- a downstream role asks `research_agent` to write publishable copy, approve review, or finalize;
- the retry policy is exhausted;
- human editorial, legal, reputational, or strategic judgment is required.

Escalation must state:

- blocking issue;
- affected files, sources, or instructions;
- why safe continuation is impossible;
- smallest decision needed;
- recommended operational status;
- recommended next role.

## blocked conditions

Set or recommend `blocked` when any of these prevent safe continuation:

- missing `TASK-ID`;
- missing `/tasks/TASK-ID/brief.md`;
- missing or stale `/tasks/TASK-ID/status.md`;
- missing `/tasks/TASK-ID/orchestration_plan.md`;
- selected pipeline conflicts with `AGENTS.md`;
- requested work would mix research with writing or review;
- required source material is unavailable;
- checked sources materially contradict each other and the contradiction affects downstream output;
- required facts are unverifiable;
- high or critical factual sensitivity cannot be supported by adequate evidence;
- required KB, agent spec, or template is unavailable;
- handoff cannot identify a valid core receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
- downstream work would require inventing facts;
- context is too fragmented to continue and cannot be repaired with `context-summary.md`.

Blocked status must be documented in `/tasks/TASK-ID/status.md` using the format from `/kb/task_statuses.md`.

## retry policy

Follow `/kb/task_statuses.md`.

Research retries are allowed when the issue is recoverable:

- missing handoff;
- incomplete source table;
- incomplete claim classification;
- formatting error;
- recoverable source gap;
- context fragmentation that can be repaired with `context-summary.md`.

Research retries are not allowed without escalation when:

- instructions conflict;
- required evidence does not exist or cannot be accessed;
- the task requires bypassing review;
- a human decision is missing;
- the same evidence gap has failed twice;
- the brief is too ambiguous to define research scope.

Retry rules:

- after the first failed attempt, document the issue and retry once;
- after the second failed attempt on the same issue, set or recommend `blocked`;
- after three failed attempts on the research stage, recommend `failed` unless the user or Chief Editor changes constraints;
- each retry must preserve previous meaningful artifacts or create versioned notes when comparison matters.

## completion conditions

Research pipeline completion requires:

- `task-manifest.md` is current and reflects research artifact states;
- required research artifacts are present in `/tasks/TASK-ID/`;
- each required artifact follows the structure required by `/agents/research_agent.md` or this pipeline;
- `claims_table.md` clearly states which claims are safe, unsafe, or caveated for drafting;
- `open-questions.md` clearly marks whether each question blocks downstream work, when real questions exist;
- `handoff-research-research-agent-to-TO.md` exists with `TO` replaced by a valid core receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
- `status.md` records the current status, previous status, responsible role, next action, key artifacts, and blockers;
- the recommended next status is valid under `/kb/task_statuses.md`;
- if the recommended downstream stage is `writing` or `review`, all sufficiency criteria are met;
- if sufficiency criteria are not met, the task is left in `research` or `blocked`, not handed off as ready for drafting.

Completion does not mean factual truth is approved for publication. It means the assigned research scope has been made traceable enough for the next valid stage.

## restart protocol

After context loss, the next agent must restart from files, not chat memory.

Receiving or restarting agents use the short context path from `/kb/shared_lifecycle_kernel.md` and `AGENTS.md`:

1. `AGENTS.md` or a short reference to its active invariants.
2. `/tasks/TASK-ID/task-manifest.md`.
3. The latest relevant handoff file.
4. The current working artifact.
5. Only `/pipelines/research_pipeline.md`, source material, KB, or editorial knowledge directly needed for the next action.

Do not read all pipelines, all agent specs, all old task folders, all retrospectives, all versions, or the full project tree by default.

Expanded reading is allowed for high-governance, conflict, source/evidence uncertainty, or restart uncertainty. In that case read the exact source/evidence files, `status.md`, review trail, governance artifacts, old versions, or legacy decision evidence needed to resolve the risk.

Then perform this restart check:

- confirm `TASK-ID`;
- confirm the current-version pointer names the active artifact when multiple versions exist;
- do not use latest modified time as the current-version source;
- stop and ask Chief Editor if current version state is unclear;
- confirm current status is valid under `/kb/task_statuses.md`;
- confirm the selected pipeline is still this pipeline or research is still the active upstream stage;
- confirm the current owner role and next required role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
- compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and the latest handoff for conflicts;
- check whether required research artifacts are present and current;
- identify missing, stale, or contradictory artifacts;
- continue the next incomplete stage or set/recommend `blocked` if safe continuation is impossible.

Model memory, prior chat, or unsaved notes must not be used as verified evidence during restart.
