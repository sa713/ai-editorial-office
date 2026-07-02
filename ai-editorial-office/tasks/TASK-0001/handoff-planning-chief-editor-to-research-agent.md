# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-planning-chief-editor-to-research-agent.md`

Handoff type: `stage-specific`

Stage: `planning`

Created by: `chief_editor`

Created for: `research_agent`

Created at: `2026-05-15 23:27:14 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Related orchestration plan: `/tasks/TASK-0001/orchestration_plan.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `chief_editor`

Agent spec: `/agents/chief_editor.md`

Work completed by this role:

- Confirmed Article Pipeline for the task;
- Determined that Research Pipeline is required before writing;
- Created `orchestration_plan.md`;
- Updated `status.md` from `intake` to `research`;
- Assigned next ownership to `research_agent`.

Decision boundaries reached:

- Chief Editor orchestration for this step is complete.
- Chief Editor did not write the article, create draft artifacts, start review, create final artifacts, or grant approval.

## receiving role

Role: `research_agent`

Agent spec: `/agents/research_agent.md`

Expected responsibility:

- Execute the research scope in `/tasks/TASK-0001/orchestration_plan.md`;
- Create research traceability artifacts;
- Update open questions if research changes them;
- Hand off to `chief_editor` or `writer_agent` according to sufficiency and pipeline rules.

The receiving role must not assume any work is complete unless it is listed in this handoff or present in the referenced artifacts.

## current status

Current task status: `research`

Previous task status: `intake`

Status transition reason:

- Article Pipeline is confirmed, and separate research is required before writing because factual claims are expected and factual sensitivity is medium.

Next expected status: `planning`

Status source of truth: `/tasks/TASK-0001/status.md`

If this handoff conflicts with `status.md`, the receiving role must stop and escalate.

## completed work

Summary of completed work:

- Loaded required governance, KB, pipeline, role, and task files for Chief Editor orchestration;
- Confirmed current status `intake` and intake handoff consistency;
- Confirmed no blockers at orchestration;
- Created a plan requiring Research Pipeline before writing;
- Updated the operational status to `research`;
- Created this planning handoff to Research Agent.

Completed checklist:

| Item | Status | Evidence |
| --- | --- | --- |
| Article Pipeline confirmed | `done` | `/tasks/TASK-0001/orchestration_plan.md` |
| Research requirement decided | `done` | `/tasks/TASK-0001/orchestration_plan.md` |
| Status updated | `done` | `/tasks/TASK-0001/status.md` |
| Next agent assigned | `done` | `/tasks/TASK-0001/status.md` |
| Writing started | `not_done` | Writing is blocked until research artifacts exist. |
| Review started | `not_done` | Review cannot start before draft artifacts exist. |
| Finalization/governance artifacts created | `not_done` | Not allowed at this stage. |

## artifacts created

| Artifact | Owner | Purpose | Ready for next role |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/orchestration_plan.md` | `chief_editor` | Governs Article Pipeline execution and required research scope. | `yes` |
| `/tasks/TASK-0001/handoff-planning-chief-editor-to-research-agent.md` | `chief_editor` | Transfers orchestration context to Research Agent. | `yes` |

## artifacts updated

| Artifact | Updated by | What changed | Reason |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/status.md` | `chief_editor` | Status changed from `intake` to `research`; owner changed to `research_agent`; required research artifacts listed. | Route task to Research Pipeline before writing. |

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Upstream research pipeline: `/pipelines/research_pipeline.md`

Pipeline stage completed: `chief_editor orchestration`

Next pipeline stage: `research`

Pipeline constraints relevant to next role:

- Research Agent must not write the article draft.
- Research must produce `research.md`, `sources.md`, `facts.md`, and `claims_table.md`.
- Research must separate facts, interpretations, assumptions, contradictions, and open questions.
- Model memory is not verified evidence.
- Unsupported or contradicted claims cannot be used as facts.
- Writer Agent cannot begin until research sufficiency is established or Chief Editor records a later valid change.

Pipeline conflicts:

- None identified.

If a pipeline conflict exists, the next role must not proceed until it is resolved.

## required KB

KB already used:

| KB file | Used for | Notes |
| --- | --- | --- |
| `/kb/task_statuses.md` | Operational transition from `intake` to `research`. | Transition is allowed. |
| `/kb/editorial_policy.md` | Factual discipline and quality bar. | Requires evidence over plausibility and review before finalization. |
| `/kb/tone_of_voice.md` | Tone requirements for downstream writing. | Calm, practical, non-hype. |

KB required before next action:

| KB file | Required for | Must be loaded by |
| --- | --- | --- |
| `/kb/task_statuses.md` | Status and handoff governance. | `research_agent` |
| `/kb/editorial_policy.md` | Evidence discipline and claim handling. | `research_agent` |
| `/kb/tone_of_voice.md` | Draft-use guidance aligned with requested tone. | `research_agent` |
| `/kb/forbidden_patterns.md` | Flagging claims and patterns that should not be used downstream. | `research_agent` |
| `/kb/ux_writing_guidelines.md` | Understanding UX-writer/product-team context. | `research_agent` |
| `/kb/glossary.md` | Terminology consistency if needed. | `research_agent` |

The receiving role must not rely on remembered KB content. Required KB must be read from disk.

## required next inputs

The receiving role must load:

- `AGENTS.md`;
- `/project-state.md`;
- `/kb/task_statuses.md`;
- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/forbidden_patterns.md`;
- `/kb/ux_writing_guidelines.md`;
- `/pipelines/article_pipeline.md`;
- `/pipelines/research_pipeline.md`;
- `/agents/research_agent.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/open-questions.md`;
- `/tasks/TASK-0001/orchestration_plan.md`;
- this handoff file.

Optional but useful inputs:

- `/kb/glossary.md`.

## research scope

Research Agent should:

- gather source-backed context for how AI can support editors and UX writers in product teams;
- identify claims safe to use about drafting, structure checking, adaptation, and weak-spot detection;
- mark replacement claims and exaggerated productivity claims as unsafe unless strongly supported and caveated;
- distinguish evidence-backed facts from practical editorial interpretation;
- identify whether internal examples are unavailable and how that limits the article;
- produce concise draft-use guidance for Writer Agent.

Research Agent should not:

- write the article;
- create `outline.md` or `draft.md`;
- create `review.md`;
- create `final.md` or `final_decision.md`;
- approve the material.

## assumptions

| Assumption | Reason | Risk | Needs verification |
| --- | --- | --- | --- |
| The article can use generic examples if no internal examples are supplied. | No internal materials were supplied in intake. | Medium: examples may feel less specific. | `yes` |
| The draft should avoid vendor-specific claims unless research supports them and Chief Editor allows them. | Brief asks for calm, practical, non-hype framing. | Low. | `no` |
| Human approval is not required during research. | No current human decision blocks evidence collection. | Low. | Reassess before finalization or delivery. |

Assumptions must not be treated as facts by the receiving role.

## next required action

Next action owner: `research_agent`

Next action:

```text
Create a research evidence base for TASK-0001, including research.md, sources.md, facts.md, claims_table.md, updated open-questions.md if needed, and a research handoff.
```

Required before action:

- Verify current status is still `research`;
- Verify Article Pipeline and Research Pipeline are still selected;
- Load required KB and task artifacts;
- Confirm no draft, review, final, approval, or final governance artifacts are being created during research.

Expected output:

- `/tasks/TASK-0001/research.md`;
- `/tasks/TASK-0001/sources.md`;
- `/tasks/TASK-0001/facts.md`;
- `/tasks/TASK-0001/claims_table.md`;
- updated `/tasks/TASK-0001/open-questions.md`, if needed;
- `/tasks/TASK-0001/handoff-research-research-agent-to-chief-editor.md` or `/tasks/TASK-0001/handoff-research-research-agent-to-writer-agent.md`.

Expected status after action: `planning`

If the research scope cannot be completed safely, expected status after action: `research` with documented gaps or `blocked` with blocker details.

## success criteria for next role

The next role succeeds when:

- all assigned research artifacts are present and current;
- every material claim proposed for the article is classified in `claims_table.md`;
- sources are listed with class, freshness, reliability, use, and limitations;
- assumptions and open questions are not promoted to facts;
- unsupported, contradicted, or overhyped claims are marked unsafe for draft use;
- status transition or recommendation is recorded;
- a research handoff is created for the next valid MVP role.

The next role must not mark the stage complete if any blocking research question remains open.

## escalation notes

Escalate if:

- required KB, pipeline, or agent specs are unavailable;
- no adequate evidence can be found for material claims needed by the brief;
- internal examples are mandatory but unavailable;
- source reliability or freshness is too weak for safe drafting;
- the task is redirected toward writing, review, or finalization before research is complete.

Escalation target: `chief_editor`

Smallest decision needed:

```text
Decide whether to narrow the article to clearly supportable general guidance, request internal examples, or block writing until stronger evidence is available.
```

Risk of proceeding without escalation:

```text
Writer Agent may create a plausible but unsupported article about AI-assisted editorial work.
```

Recommended status if escalation is needed: `blocked`

## restart notes

Minimum restart checklist for the receiving role:

- read `AGENTS.md`;
- read `/project-state.md`;
- read `/kb/task_statuses.md`;
- read `/tasks/TASK-0001/status.md`;
- read `/tasks/TASK-0001/brief.md`;
- read `/tasks/TASK-0001/orchestration_plan.md`;
- read this handoff file;
- read `/pipelines/article_pipeline.md`;
- read `/pipelines/research_pipeline.md`;
- read `/agents/research_agent.md`;
- read required KB listed above;
- verify current status still matches this handoff;
- continue only from `next required action`.

Last known reliable state:

- Current status: `research`
- Completed stage: `chief_editor orchestration`
- Last completed artifact: `/tasks/TASK-0001/handoff-planning-chief-editor-to-research-agent.md`
- Next role: `research_agent`
- Next action: create research traceability artifacts
- Blocking issue, if any: `none`
