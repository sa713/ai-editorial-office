# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-research-research-agent-to-chief-editor.md`

Handoff type: `stage-specific`

Stage: `research`

Created by: `research_agent`

Created for: `chief_editor`

Created at: `2026-05-15 23:38:48 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Related orchestration plan: `/tasks/TASK-0001/orchestration_plan.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `research_agent`

Agent spec: `/agents/research_agent.md`

Work completed by this role:

- Loaded required task, pipeline, role, and KB inputs;
- Collected and classified checked sources;
- Created research evidence base;
- Created facts table and claims table;
- Updated open questions;
- Updated status from `research` to `planning` for Chief Editor routing.

Decision boundaries reached:

- Research local outcome is `research_ready_for_writing`;
- Research Agent recommends Chief Editor route to Writer Agent;
- Research Agent did not write the article, create outline/draft, review, finalization, approval, or governance artifacts.

## receiving role

Role: `chief_editor`

Agent spec: `/agents/chief_editor.md`

Expected responsibility:

- Validate research sufficiency;
- Decide whether to route to `writer_agent` or request more research;
- Update `status.md`;
- Create next handoff if routing to another role.

The receiving role must not assume any work is complete unless it is listed in this handoff or present in the referenced artifacts.

## current status

Current task status: `planning`

Previous task status: `research`

Status transition reason:

- Research artifacts are complete for the assigned scope and require Chief Editor routing before writing.

Next expected status: `writing`

Status source of truth: `/tasks/TASK-0001/status.md`

If this handoff conflicts with `status.md`, the receiving role must stop and escalate.

## completed work

Summary of completed work:

- Created `/tasks/TASK-0001/sources.md` with checked source classes, freshness, reliability, use, and limitations;
- Created `/tasks/TASK-0001/facts.md` with usable facts and confidence;
- Created `/tasks/TASK-0001/claims_table.md` with safe, caveated, and unsafe claims;
- Created `/tasks/TASK-0001/research.md` with findings, assumptions, gaps, implications, and do-not-say list;
- Updated `/tasks/TASK-0001/open-questions.md`;
- Updated `/tasks/TASK-0001/status.md`.

Completed checklist:

| Item | Status | Evidence |
| --- | --- | --- |
| Sources classified | `done` | `/tasks/TASK-0001/sources.md` |
| Facts extracted | `done` | `/tasks/TASK-0001/facts.md` |
| Claims classified | `done` | `/tasks/TASK-0001/claims_table.md` |
| Research summary created | `done` | `/tasks/TASK-0001/research.md` |
| Open questions updated | `done` | `/tasks/TASK-0001/open-questions.md` |
| Status updated | `done` | `/tasks/TASK-0001/status.md` |
| Draft created | `not_done` | Not allowed for Research Agent. |
| Review created | `not_done` | Not allowed at research stage. |
| Final artifacts created | `not_done` | Not allowed at research stage. |

## artifacts created

| Artifact | Owner | Purpose | Ready for next role |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/research.md` | `research_agent` | Research summary, findings, implications, gaps, and do-not-say list. | `yes` |
| `/tasks/TASK-0001/sources.md` | `research_agent` | Checked source inventory and limitations. | `yes` |
| `/tasks/TASK-0001/facts.md` | `research_agent` | Usable facts with confidence and source references. | `yes` |
| `/tasks/TASK-0001/claims_table.md` | `research_agent` | Claim-level draft-use guidance. | `yes` |
| `/tasks/TASK-0001/handoff-research-research-agent-to-chief-editor.md` | `research_agent` | Transfer research context to Chief Editor. | `yes` |

## artifacts updated

| Artifact | Updated by | What changed | Reason |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/open-questions.md` | `research_agent` | Converted intake questions into research-stage table and added guidance on numeric claims. | Carry unresolved questions forward safely. |
| `/tasks/TASK-0001/status.md` | `research_agent` | Current status changed from `research` to `planning`; owner changed to `chief_editor`; research artifacts marked present. | Research complete; Chief Editor routing required. |

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Upstream research pipeline: `/pipelines/research_pipeline.md`

Pipeline stage completed: `research`

Next pipeline stage: `planning`

Pipeline constraints relevant to next role:

- Chief Editor must route before writing begins.
- Writer Agent must use `claims_table.md` and must not use claims marked `no`.
- Review remains mandatory before finalization.
- No non-MVP Editor Agent exists.

Pipeline conflicts:

- None identified.

## sources checked

| Source ID | Title | Use |
| --- | --- | --- |
| S1 | OpenAI - Content creation for everyone in your company | Content creation, writing, editing, rewriting, structure improvement. |
| S2 | OpenAI Help Center - ChatGPT Capabilities Overview | General drafting, rewriting, summarizing, creative suggestions, and co-writing/editing support. |
| S3 | NN/g - Common Tasks Performed by UX Professionals with the Help of Generative AI | UX-specific task examples. |
| S4 | OpenAI Academy - Writing with ChatGPT | Plan-draft-revise workflow, tone adaptation, constraints, and fact verification guidance. |
| S5 | Microsoft Work Trend Index 2024 | Broad workplace AI context and governance caution. |
| S6 | NIST AI Risk Management Framework Core | Governance/risk framing. |
| S7 | OpenAI Help Center - ChatGPT can make mistakes | Limitation and verification caution. |
| S8 | NN/g - AI: First New UI Paradigm in 60 Years | Broad UX framing. |

## facts safe to use

- AI can support drafting, rewriting, summarizing, and repurposing when framed as assistance, not autonomous final writing.
- UX writers can use AI for text variants, tone changes, shortening, expanding, rewording, proofreading, and microcopy support.
- AI can help surface possible gaps or alternative structures, but human review remains responsible for judging relevance and quality.
- AI-generated outputs can contain mistakes, so important claims and product facts require verification.
- AI use benefits from governance, clear ownership, and risk management.

## claims not safe to use

- AI replaces editors or UX writers.
- AI always saves time.
- AI automatically improves editorial quality.
- AI catches every weak spot.
- Organization-specific examples or policies exist.
- Numeric productivity claims for editors or UX writers.

## claims usable only with caveat

- AI can speed up drafting: use only as a task-specific possibility, not a guarantee.
- AI can help check structure: frame as generating options or questions for human review.
- AI can detect weak spots: frame as surfacing possible issues, not validating the final text.
- Teams benefit from shared AI rules: use as a governance recommendation, not a proven universal outcome.

## contradictions and impact

| Contradiction | Impact | Handling |
| --- | --- | --- |
| No material contradiction found for narrow assistance claims. | No blocker. | Use cautious wording and trace claims. |
| Replacement rhetoric conflicts with the brief and governance model. | High if introduced in draft. | Treat replacement claims as unsafe except as a rejected misconception. |

## assumptions and risk

| Assumption | Risk | Handling |
| --- | --- | --- |
| Generic examples are acceptable. | Article may be less specific. | Chief Editor can still request internal examples before writing. |
| Vendor-specific comparison is unnecessary. | Low. | Keep article tool-agnostic unless Chief Editor changes scope. |

Assumptions must not be treated as facts by downstream roles.

## open questions

| Question | Blocks next action | Note |
| --- | --- | --- |
| Are internal policies or examples available? | `no` | Blocks only organization-specific claims. |
| Is human approval required before internal publication? | `no` | Reassess later, not a research blocker. |
| Should numeric productivity claims be included? | `yes, if desired` | Current recommendation: avoid them. |

## blockers

None.

## required next inputs

The receiving role must load:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/pipelines/article_pipeline.md`;
- `/pipelines/research_pipeline.md`;
- `/agents/chief_editor.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/orchestration_plan.md`;
- `/tasks/TASK-0001/research.md`;
- `/tasks/TASK-0001/sources.md`;
- `/tasks/TASK-0001/facts.md`;
- `/tasks/TASK-0001/claims_table.md`;
- `/tasks/TASK-0001/open-questions.md`;
- this handoff file.

## next required action

Next action owner: `chief_editor`

Next action:

```text
Validate research sufficiency and either route TASK-0001 to Writer Agent for outline/draft creation or send it back to research with a narrower evidence request.
```

Recommended next status: `writing`

Expected output if routing to writing:

- updated `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md`.

## success criteria for next role

The next role succeeds when:

- Chief Editor records a routing decision;
- unsafe claims remain blocked;
- Writer Agent receives clear constraints and source-backed claim guidance;
- status transition is valid under `/kb/task_statuses.md`;
- no draft, review, or finalization gate is bypassed.

## escalation notes

Escalate if:

- Chief Editor requires organization-specific examples before writing;
- numeric productivity claims are required;
- source reliability is judged insufficient for the intended article angle;
- human approval is required before writing.

Escalation target: `chief_editor`

Smallest decision needed:

```text
Decide whether the article may proceed with generic examples and no numeric productivity claims.
```

Risk of proceeding without escalation:

```text
The draft could sound generic or introduce unsupported internal/productivity claims.
```

Recommended status if escalation is needed: `blocked`

## restart notes

Minimum restart checklist for Chief Editor:

- read `AGENTS.md`;
- read `/kb/task_statuses.md`;
- read `/tasks/TASK-0001/status.md`;
- read `/tasks/TASK-0001/orchestration_plan.md`;
- read this handoff file;
- read research artifacts;
- verify current status is still `planning`;
- route only through valid Article Pipeline transitions.

Last known reliable state:

- Current status: `planning`
- Completed stage: `research`
- Last completed artifact: `/tasks/TASK-0001/handoff-research-research-agent-to-chief-editor.md`
- Next role: `chief_editor`
- Next action: route to writing or request more research
- Blocking issue, if any: `none`
