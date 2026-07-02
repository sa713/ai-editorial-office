# Orchestration Plan

## task summary

Task ID: `TASK-0001`

Task title: `AI support for editors and UX writers in product teams`

Requested output: `draft article`

Audience: `editors, UX writers, product teams`

Primary goal: Create a draft article for an internal portal explaining how AI can help editors and UX writers in product teams without replacing editorial judgment.

Quality bar: calm, practical, source-aware article draft; no hype, no replacement rhetoric, no unsupported claims presented as facts, mandatory independent review before finalization.

Current task status: `research`

Brief source: `/tasks/TASK-0001/brief.md`

Current status source: `/tasks/TASK-0001/status.md`

Last updated by: `chief_editor`

Last updated at: `2026-05-15 23:27:14 MSK`

## task classification

Task type: `article`

Complexity: `medium`

Risk level: `medium`

Factual sensitivity: `medium`

Requires research: `yes`

Requires writing: `yes`

Requires optional revision: `yes`

Requires independent review: `yes`

Requires human approval: `unknown`

Classification rationale:

- The requested deliverable is an article-style draft for an internal portal, so Article Pipeline is the governing pipeline.
- The brief expects factual claims and marks factual sensitivity as `medium`; under Article Pipeline and Research Pipeline this requires a separate research stage before writing.
- The article topic touches AI use in product/editorial work, where unsupported claims could create misleading operational guidance.
- The requested output is a draft, not a final publishable artifact; review and finalization remain mandatory later stages.

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Upstream research pipeline: `/pipelines/research_pipeline.md`

Pipeline version or date, if known: `unknown`

Reason selected:

- User explicitly requested Article Pipeline.
- The deliverable is an article/explainer with a thesis, audience, tone, and target length.
- The task requires writing, independent review, finalization, and Chief Editor governance rather than a one-step answer.

Pipeline constraints:

- Research, writing, review, finalization, and governance must remain separate stages.
- Only MVP roles may be used: `intake_agent`, `chief_editor`, `research_agent`, `writer_agent`, `review_agent`, `final_editor`.
- There is no separate active Editor Agent in MVP.
- Writer Agent must not invent facts, sources, product behavior, examples, dates, statistics, or quotes.
- Review is mandatory before finalization.
- Finalization may begin only after valid `review.md` with outcome `approved`.
- Chief Editor final governance decision requires `final_decision.md`, but that artifact must not be created now.

Pipeline conflicts:

- None identified.

## research decision

Research required: `yes`

Research rationale:

- `brief.md` says factual claims are expected.
- `brief.md` sets factual sensitivity to `medium`.
- Article Pipeline requires research when factual claims are material or factual sensitivity is medium, high, or critical.
- Research Pipeline applies because downstream writing needs an evidence base before claims about AI-assisted editorial workflows can be safely drafted.

Research scope:

- Collect a concise evidence base for practical, non-hype claims about how AI can support editors and UX writers.
- Separate confirmed facts, interpretations, assumptions, and open questions.
- Identify safe claims for the draft about AI helping with draft generation, structure checks, adaptation, and finding weak spots.
- Identify claims that must not be used, especially replacement rhetoric, unsupported productivity claims, or vendor-specific claims.
- Record source freshness and reliability.
- Provide draft-use guidance for `writer_agent`.
- Mark whether organization-specific examples are unavailable; if unavailable, recommend generic examples with caveats.

Research outputs required:

- `/tasks/TASK-0001/research.md`;
- `/tasks/TASK-0001/sources.md`;
- `/tasks/TASK-0001/facts.md`;
- `/tasks/TASK-0001/claims_table.md`;
- updated `/tasks/TASK-0001/open-questions.md`;
- `/tasks/TASK-0001/handoff-research-research-agent-to-chief-editor.md` or `/tasks/TASK-0001/handoff-research-research-agent-to-writer-agent.md`, depending on sufficiency.

Research completion rule:

- If research is sufficient for drafting, `research_agent` should recommend routing to `writer_agent`; operationally, Research Pipeline recommends returning to `planning` for Chief Editor routing or handing off according to the orchestration plan if sufficiency is clear.
- If research finds unresolved evidence gaps that affect safe drafting, leave the task in `research` or recommend `blocked` with specific blocker details.

## required agents

| Stage | Required agent | Agent spec | Responsibility | Handoff required |
| --- | --- | --- | --- | --- |
| intake | `intake_agent` | `/agents/intake_agent.md` | normalize raw task package | `yes` |
| orchestration/planning | `chief_editor` | `/agents/chief_editor.md` | select pipeline, plan execution, assign roles, maintain governance | `yes` |
| research | `research_agent` | `/agents/research_agent.md` | create evidence base and claim traceability | `yes` |
| writing | `writer_agent` | `/agents/writer_agent.md` | create outline, draft, writer notes, and claims-used | `yes` |
| review | `review_agent` | `/agents/review_agent.md` | independent review | `yes` |
| finalization | `final_editor` | `/agents/final_editor.md` | controlled finalization after approved review | `yes` |
| final governance decision | `chief_editor` | `/agents/chief_editor.md` | validate finalization and create `final_decision.md` | `yes` |

Role separation rules:

- Writer Agent and Review Agent must be independent role instances.
- Chief Editor must not write the article.
- Chief Editor must not perform independent review.
- Research Agent must not write the draft.
- No non-MVP agents may be introduced.
- `editing` may appear only as a status-model bridge or Writer Agent revision checkpoint; it does not introduce an Editor Agent.

## required KB

| KB file | Required for | Loaded before stage | Notes |
| --- | --- | --- | --- |
| `/kb/task_statuses.md` | status governance | all stages | Required for every transition. |
| `/kb/editorial_policy.md` | factual discipline, quality bar, review-gate integrity | planning, research, writing, review | Required. |
| `/kb/tone_of_voice.md` | calm, practical, non-hype article tone | writing, review, finalization | Required. |
| `/kb/forbidden_patterns.md` | avoiding hype, filler, and weak editorial patterns | writing, review | Required before drafting or review. |
| `/kb/ux_writing_guidelines.md` | context on UX writers and product-language work | research, writing | Required because the audience and topic include UX writers. |
| `/kb/glossary.md` | terminology consistency | research, writing, review | Useful and required if terminology questions appear. |

KB loading rule:

- Do not assume KB content from memory.
- Required KB must be read from disk by the assigned role before using it.
- If a required KB file is unavailable, record the issue in `status.md` and decide whether it blocks the current stage.

## required artifacts

| Artifact | Required | Owner | Created or updated at stage | Status |
| --- | --- | --- | --- | --- |
| `/tasks/TASK-0001/brief.md` | yes | `intake_agent` | intake | `present` |
| `/tasks/TASK-0001/status.md` | yes | `chief_editor` | all stages | `present` |
| `/tasks/TASK-0001/open-questions.md` | yes | current owner | intake onward | `present` |
| `/tasks/TASK-0001/orchestration_plan.md` | yes | `chief_editor` | planning | `present` |
| `/tasks/TASK-0001/research.md` | yes | `research_agent` | research | `missing` |
| `/tasks/TASK-0001/sources.md` | yes | `research_agent` | research | `missing` |
| `/tasks/TASK-0001/facts.md` | yes | `research_agent` | research | `missing` |
| `/tasks/TASK-0001/claims_table.md` | yes | `research_agent` | research | `missing` |
| `/tasks/TASK-0001/outline.md` | yes | `writer_agent` | writing | `not_applicable_yet` |
| `/tasks/TASK-0001/draft.md` | yes | `writer_agent` | writing | `not_applicable_yet` |
| `/tasks/TASK-0001/claims-used.md` | yes | `writer_agent` | writing | `not_applicable_yet` |
| `/tasks/TASK-0001/writer-notes.md` | yes | `writer_agent` | writing | `not_applicable_yet` |
| `/tasks/TASK-0001/review.md` | yes | `review_agent` | review | `not_applicable_yet` |
| `/tasks/TASK-0001/qa-checklist.md` | yes | `review_agent` | review | `not_applicable_yet` |
| `/tasks/TASK-0001/review-summary.md` | yes | `review_agent` | review | `not_applicable_yet` |
| `/tasks/TASK-0001/reviewer-notes.md` | yes | `review_agent` | review | `not_applicable_yet` |
| `/tasks/TASK-0001/final.md` | yes | `final_editor` | finalization | `not_applicable_yet` |
| `/tasks/TASK-0001/finalization-notes.md` | yes | `final_editor` | finalization | `not_applicable_yet` |
| `/tasks/TASK-0001/finalization-checklist.md` | yes | `final_editor` | finalization | `not_applicable_yet` |
| `/tasks/TASK-0001/final_decision.md` | yes | `chief_editor` | final governance decision | `not_applicable_yet` |
| `/tasks/TASK-0001/approval.md` | conditional | `user` or `chief_editor` | human approval | `not_applicable_yet` |

Optional future artifacts such as `edited.md`, `editor-notes.md`, and `revision-requests.md` are not required and must not introduce a non-MVP editing role.

## execution order

| Step | Status before | Agent | Action | Required inputs | Expected outputs | Status after |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `none` | `intake_agent` | normalize raw request | raw user request | `brief.md`, `status.md`, `open-questions.md`, intake handoff | `intake` |
| 2 | `intake` | `chief_editor` | validate brief, confirm Article Pipeline, require research | intake artifacts, pipelines, KB | `orchestration_plan.md`, updated `status.md`, planning handoff | `research` |
| 3 | `research` | `research_agent` | create evidence base and claim traceability | `brief.md`, `status.md`, `orchestration_plan.md`, planning handoff, required KB | `research.md`, `sources.md`, `facts.md`, `claims_table.md`, updated `open-questions.md`, research handoff | `planning`, `research`, or `blocked` |
| 4 | `planning` | `chief_editor` | confirm research sufficiency and route to writing | research artifacts, research handoff | updated `status.md`, handoff to `writer_agent` | `writing` |
| 5 | `writing` | `writer_agent` | create article outline and draft | brief, orchestration plan, research artifacts, KB, handoff | `outline.md`, `draft.md`, `writer-notes.md`, `claims-used.md`, writing handoff | `editing` or `review` according to status model and handoff |
| 6 | `editing` or `review` | `review_agent` | perform independent review after draft is ready | draft artifacts, research artifacts, brief, plan | `review.md`, `qa-checklist.md`, `review-summary.md`, `reviewer-notes.md`, review handoff | `approved`, `changes_requested`, `blocked`, or `human_approval_required` |
| 7 | `approved` | `final_editor` | controlled finalization | approved review artifacts and draft | `final.md`, `finalization-notes.md`, `finalization-checklist.md`, finalization handoff | `approved` |
| 8 | `approved` | `chief_editor` | validate finalization and make governance decision | finalization and review artifacts | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |

Execution rules:

- Do not skip research for this task.
- Do not start writing until research artifacts exist or Chief Editor records a later justified change.
- Do not create `draft.md`, `review.md`, `final.md`, `final_decision.md`, or `approval.md` during this orchestration step.
- Do not merge writing and review.
- Do not merge finalization and governance.

## status transitions

Planned transitions:

| From | To | Trigger | Responsible role | Required artifact |
| --- | --- | --- | --- | --- |
| `intake` | `research` | Chief Editor confirms Article Pipeline and requires research before writing | `chief_editor` | `orchestration_plan.md`, `status.md`, `handoff-planning-chief-editor-to-research-agent.md` |
| `research` | `planning` | Research Agent completes assigned research and needs Chief Editor routing | `research_agent` recommends; `chief_editor` records | research artifacts and research handoff |
| `planning` | `writing` | Chief Editor confirms research sufficiency and routes to Writer Agent | `chief_editor` | updated `status.md`, handoff to `writer_agent` |
| `writing` | `editing` | Writer Agent uses optional status bridge or revision checkpoint | `writer_agent` | `outline.md`, `draft.md`, `writer-notes.md`, `claims-used.md` |
| `editing` | `review` | Draft is ready for independent review | `writer_agent` or `chief_editor` | draft artifacts and handoff |
| `review` | `approved` | review verdict approved | `review_agent` | `review.md`, `qa-checklist.md`, `review-summary.md` |
| `review` | `changes_requested` | review requires changes | `review_agent` | `review.md`, `qa-checklist.md`, `review-summary.md` |
| `review` | `blocked` | review finds blocker | `review_agent` | `review.md`, blocker evidence |
| `approved` | `approved` | Final Editor completes controlled finalization | `final_editor` | `final.md`, `finalization-notes.md`, `finalization-checklist.md` |
| `approved` | `finalized` | Chief Editor validates finalization | `chief_editor` | `final_decision.md`, `final.md` |

Status source of truth: `/tasks/TASK-0001/status.md`

State model source of truth: `/kb/task_statuses.md`

Any unplanned transition must be documented in `status.md` with reason, responsible role, and affected artifacts.

## review requirements

Independent review required: `yes`

Reviewer: `review_agent`

Reviewer spec: `/agents/review_agent.md`

Review artifact: `/tasks/TASK-0001/review.md`

Review must check:

- compliance with `brief.md`;
- compliance with `orchestration_plan.md`;
- factual traceability through `research.md`, `sources.md`, `facts.md`, `claims_table.md`, and `claims-used.md`;
- source usage and caveats;
- separation of research and writing;
- Writer Agent and Review Agent independence;
- required artifact completeness;
- unresolved blockers;
- tone: calm, practical, non-hype;
- absence of replacement rhetoric or generic AI cheerleading.

Valid review outcomes:

- `approved`;
- `changes_requested`;
- `blocked`.

The task cannot move to `approved` without a valid `review.md`.

## human approval requirements

Human approval required: `unknown`

Required approver: `user`, if later required for internal publication or strategic sign-off

Approval artifact: `/tasks/TASK-0001/approval.md` or documented approval in `status.md`

Human approval is required when:

- review, finalization notes, or Chief Editor governance identifies a strategic, reputational, policy, or publishing decision;
- internal publication requires explicit user approval;
- the material contains high-risk claims not suitable for finalization without human decision.

If approval remains unknown at final governance, Chief Editor must decide whether to set `human_approval_required` before closure.

## known risks

| Risk | Severity | Stage affected | Mitigation | Owner |
| --- | --- | --- | --- | --- |
| Draft may make generic or unsupported claims about AI productivity or editorial quality. | `medium` | research/writing/review | Research Agent must classify safe, caveated, and unsafe claims before writing. | `research_agent` |
| Article may drift into AI hype or replacement rhetoric. | `medium` | writing/review | Use `/kb/tone_of_voice.md`, `/kb/editorial_policy.md`, and `/kb/forbidden_patterns.md`; review must check this explicitly. | `writer_agent`, `review_agent` |
| Internal examples are unavailable. | `low` | research/writing | Use generic examples only if marked as illustrative, not organization-specific facts. | `research_agent`, `writer_agent` |
| Human publication approval may be required later. | `low` | finalization/governance | Reassess after review and before final governance. | `chief_editor` |

## unresolved questions

| Question | Blocks progress | Needed from | Target stage | Status |
| --- | --- | --- | --- | --- |
| Should separate research be required before writing? | `no` | `chief_editor` | planning | `answered: yes` |
| Are internal AI/editorial policies, examples, or product-team practices available? | `no` | `user` or `chief_editor` | research/writing | `open` |
| Should examples be organization-specific or generic? | `no` | `chief_editor` | research/writing | `deferred: use generic examples unless internal material is supplied` |

Questions do not block research. They may affect writing specificity and should be carried forward.

## blockers

Current blockers:

- None.

Blocked status required: `no`

## escalation conditions

Escalate when:

- required KB, pipeline, or agent specs are unavailable;
- research cannot identify safe claims for the requested article;
- internal examples are required but no source material is supplied;
- the task is redirected toward finalization or publication before independent review;
- a non-MVP role is requested;
- a human approval decision becomes necessary.

Recommended escalation status:

- Use `blocked` for missing required inputs or unresolved evidence risk.
- Use `human_approval_required` only when the next action is specifically a human editorial, strategic, legal, reputational, or publishing decision.

## next role assignment

Next required role: `research_agent`

Next agent spec: `/agents/research_agent.md`

Next operational status: `research`

First action for next role:

```text
Load the required inputs, execute the research scope in this orchestration plan, create research traceability artifacts, update open questions, and hand off according to sufficiency.
```

Required next inputs:

- `AGENTS.md`;
- `/project-state.md`;
- `/kb/task_statuses.md`;
- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/forbidden_patterns.md`;
- `/kb/ux_writing_guidelines.md`;
- `/kb/glossary.md`, if terminology needs normalization;
- `/pipelines/article_pipeline.md`;
- `/pipelines/research_pipeline.md`;
- `/agents/research_agent.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/open-questions.md`;
- `/tasks/TASK-0001/orchestration_plan.md`;
- `/tasks/TASK-0001/handoff-planning-chief-editor-to-research-agent.md`.

## restart notes

Last reliable state:

- Intake complete.
- Chief Editor orchestration complete.
- Article Pipeline confirmed.
- Research Pipeline required before writing.
- Current operational status: `research`.
- Current owner: `research_agent`.
- No blockers.
- No draft, review, final, approval, or final governance artifacts have been created.

To restart, load `status.md`, this plan, and the latest handoff before acting.
