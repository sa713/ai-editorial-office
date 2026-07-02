# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-planning-chief-editor-to-writer-agent.md`

Handoff type: `stage-specific`

Stage: `planning`

Created by: `chief_editor`

Created for: `writer_agent`

Created at: `2026-05-15 23:47:30 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Related orchestration plan: `/tasks/TASK-0001/orchestration_plan.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `chief_editor`

Agent spec: `/agents/chief_editor.md`

Work completed by this role:

- Reviewed research stage artifacts;
- Confirmed research sufficiency for writing;
- Confirmed Article Pipeline remains valid;
- Confirmed unsafe claims remain blocked and caveated claims remain caveated;
- Updated `status.md` from `planning` to `writing`;
- Assigned next ownership to `writer_agent`.

Decision boundaries reached:

- Chief Editor routing to Writer Agent is complete.
- Chief Editor did not write `outline.md` or `draft.md`.
- Chief Editor did not create review, finalization, approval, or governance artifacts.

## receiving role

Role: `writer_agent`

Agent spec: `/agents/writer_agent.md`

Expected responsibility:

- Create `outline.md`;
- Create `draft.md`;
- Create `writer-notes.md`;
- Create `claims-used.md`;
- Create writing handoff to the next valid MVP role.

The receiving role must not assume any work is complete unless it is listed in this handoff or present in the referenced artifacts.

## current status

Current task status: `writing`

Previous task status: `planning`

Status transition reason:

- Research sufficiency is confirmed and Writer Agent can draft within the constraints recorded below.

Next expected status: `editing` or `review`

Status source of truth: `/tasks/TASK-0001/status.md`

If this handoff conflicts with `status.md`, the receiving role must stop and escalate.

## completed work

Summary of completed work:

- Read required Chief Editor inputs;
- Validated that research artifacts exist and are sufficient for cautious drafting;
- Confirmed open questions do not block writing if the draft uses generic examples and avoids numeric productivity claims;
- Recorded explicit writing constraints;
- Updated status to `writing`;
- Created this handoff to Writer Agent.

Completed checklist:

| Item | Status | Evidence |
| --- | --- | --- |
| Research sufficiency checked | `done` | `/tasks/TASK-0001/research.md`; `/tasks/TASK-0001/claims_table.md` |
| Route to writing approved | `done` | `/tasks/TASK-0001/status.md` |
| Writer Agent assigned | `done` | `/tasks/TASK-0001/status.md` |
| Unsafe claims kept blocked | `done` | `/tasks/TASK-0001/claims_table.md`; this handoff |
| Caveated claims kept caveated | `done` | `/tasks/TASK-0001/claims_table.md`; this handoff |
| Outline written | `not_done` | Not allowed for Chief Editor. |
| Draft written | `not_done` | Not allowed for Chief Editor. |
| Review started | `not_done` | Review requires draft artifacts first. |
| Final artifacts created | `not_done` | Not allowed at this stage. |

## artifacts created

| Artifact | Owner | Purpose | Ready for next role |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md` | `chief_editor` | Transfer writing constraints and routing decision to Writer Agent. | `yes` |

## artifacts updated

| Artifact | Updated by | What changed | Reason |
| --- | --- | --- | --- |
| `/tasks/TASK-0001/status.md` | `chief_editor` | Status changed from `planning` to `writing`; current owner changed to `writer_agent`; writing constraints recorded. | Route to Writer Agent after sufficient research. |

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Upstream research pipeline: `/pipelines/research_pipeline.md`

Pipeline stage completed: `planning`

Next pipeline stage: `writing`

Pipeline constraints relevant to next role:

- Writing must be based on `brief.md`, `orchestration_plan.md`, research artifacts, required KB, and this handoff.
- Writer Agent must create `outline.md`, `draft.md`, `writer-notes.md`, and `claims-used.md`.
- Writer Agent must not create `review.md`, `final.md`, `final_decision.md`, or `approval.md`.
- Review is mandatory after draft creation.
- No separate Editor Agent exists in MVP.

Pipeline conflicts:

- None identified.

If a pipeline conflict exists, the next role must not proceed until it is resolved.

## research sufficiency

Sufficiency decision: `sufficient_for_writing`

Basis:

- `sources.md` lists checked sources with class, freshness, reliability, use, and limitations.
- `facts.md` lists usable facts with confidence and relevance.
- `claims_table.md` identifies claims safe to use, claims usable only with caveat, and claims blocked from draft use.
- `research.md` gives implications for writing and a do-not-say list.
- `open-questions.md` marks unresolved questions as non-blocking for generic drafting.

No additional research is required before writing if Writer Agent follows this handoff.

## writing constraints

Writer Agent must follow these constraints exactly:

- no AI hype;
- no replacement rhetoric;
- no unsupported productivity claims;
- no invented internal practices;
- generic examples only;
- practical tone;
- claims must follow `claims_table.md`;
- claims marked `Can be used in draft: no` must remain blocked;
- claims marked `Can be used in draft: with caveat` must remain caveated;
- no numeric productivity claims;
- no organization-specific examples, policies, adoption claims, or team practices;
- no vendor-specific superiority claims;
- no claim that AI can approve, finalize, publish, or replace review;
- no generic AI intro such as `в современном мире` or "AI changes everything";
- no statement that the draft is final, reviewed, approved, or ready for publication.

Expected article shape:

- approximately 4000 characters;
- internal portal draft;
- clear thesis that AI assists but does not replace editors or UX writers;
- practical sections around drafting, structure checks, adaptation, and weak-spot detection;
- concise conclusion that returns responsibility to human editorial judgment and review.

## claim-use rules

Safe claims may be used:

- C2: AI can help adapt existing text for audience, channel, length, or tone.
- C5: AI does not replace editorial responsibility for meaning, factual accuracy, tone, risk, and final decisions.
- C6: AI outputs can contain errors or unsupported information, so important claims should be checked.
- C12: AI can be useful for UX microcopy and content design tasks such as rewriting, shortening, expanding, and tone adjustment.

Caveated claims may be used only with caution:

- C1: drafting support can be framed as help with first drafts or draft fragments, not guaranteed speed.
- C3: structure checks can be framed as generating alternatives or questions, not validating the best structure.
- C4: weak-spot detection can be framed as surfacing possible issues, not catching every issue.
- C7: shared AI rules can be framed as a governance recommendation, not a proven universal benefit.

Blocked claims must not be used as factual claims:

- C8: AI improves editorial quality by itself.
- C9: AI can replace editors or UX writers in product teams.
- C10: AI always saves time for editorial teams.
- C11: organization-specific examples or policies exist for this article.

## required KB

KB already used by Chief Editor:

| KB file | Used for | Notes |
| --- | --- | --- |
| `/kb/task_statuses.md` | Validating `planning` to `writing` transition. | Transition is allowed. |
| `/kb/editorial_policy.md` | Maintaining factual discipline and role separation. | Unsupported claims must remain blocked. |
| `/kb/tone_of_voice.md` | Writing tone constraints. | Calm, practical, non-hype. |
| `/kb/forbidden_patterns.md` | Anti-hype and anti-filler constraints. | Must be loaded before drafting. |

KB required before next action:

| KB file | Required for | Must be loaded by |
| --- | --- | --- |
| `/kb/task_statuses.md` | Status and handoff governance. | `writer_agent` |
| `/kb/editorial_policy.md` | Factual discipline, quality bar, review-gate integrity. | `writer_agent` |
| `/kb/tone_of_voice.md` | Draft tone. | `writer_agent` |
| `/kb/forbidden_patterns.md` | Avoiding hype, filler, and unsupported confidence. | `writer_agent` |
| `/kb/ux_writing_guidelines.md` | Handling UX writing examples without inventing product behavior. | `writer_agent` |

The receiving role must not rely on remembered KB content. Required KB must be read from disk.

## required next inputs

The receiving role must load:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/forbidden_patterns.md`;
- `/kb/ux_writing_guidelines.md`;
- `/pipelines/article_pipeline.md`;
- `/agents/writer_agent.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/orchestration_plan.md`;
- `/tasks/TASK-0001/research.md`;
- `/tasks/TASK-0001/sources.md`;
- `/tasks/TASK-0001/facts.md`;
- `/tasks/TASK-0001/claims_table.md`;
- `/tasks/TASK-0001/open-questions.md`;
- this handoff file.

Optional but useful inputs:

- `/kb/glossary.md`.

## open questions

| Question | Blocks writing | Chief Editor decision |
| --- | --- | --- |
| Are internal AI/editorial policies, examples, or product-team practices available? | `no` | Proceed without them; do not invent internal practices. |
| Should workflow examples be organization-specific or generic? | `no` | Generic examples only. |
| Is human approval required before internal publication or delivery? | `no` | Reassess after review/finalization; does not block writing. |
| Should the draft include numeric productivity claims? | `yes, if desired` | Do not include numeric productivity claims. |

## assumptions

| Assumption | Reason | Risk | Handling |
| --- | --- | --- | --- |
| Generic examples are sufficient for the draft. | No internal examples were supplied. | Draft may feel less specific. | Keep examples clearly generic and practical. |
| A tool-agnostic article is preferred. | Brief does not ask for vendor comparison. | Low. | Avoid vendor-specific recommendations. |

Assumptions must not be treated as facts by Writer Agent.

## blockers

None.

## next required action

Next action owner: `writer_agent`

Next action:

```text
Create outline.md, draft.md, writer-notes.md, and claims-used.md for TASK-0001 using only supported or properly caveated claims from the research artifacts and this handoff.
```

Expected status after action: `editing` or `review`

If Writer Agent finds missing evidence or a necessary unsafe claim, expected status after action: `research` or `blocked` with documented reason.

## success criteria for next role

The next role succeeds when:

- `outline.md` exists and matches the brief and writing constraints;
- `draft.md` exists and is a draft article, not a final artifact;
- `claims-used.md` traces all factual claims to `claims_table.md`, `facts.md`, or `sources.md`;
- `writer-notes.md` records assumptions, caveats, risks, and any excluded unsafe claims;
- no unsafe claim is used as fact;
- caveated claims remain caveated;
- a writing handoff is created for the next valid MVP role.

The next role must not mark the stage complete if any blocking evidence gap remains open.

## escalation notes

Escalate if:

- the draft would require numeric productivity claims;
- the draft would require internal examples or policies;
- a necessary claim is marked `no` in `claims_table.md`;
- source evidence is insufficient for a factual claim needed by the article;
- the task is redirected toward review, finalization, or publication before writing artifacts exist.

Escalation target: `chief_editor`

Smallest decision needed:

```text
Decide whether to remove the unsafe claim, return to research, or ask the user for internal source material.
```

Risk of proceeding without escalation:

```text
The draft may contain unsupported governance, productivity, or internal-practice claims.
```

Recommended status if escalation is needed: `blocked` or `research`

## restart notes

Minimum restart checklist for Writer Agent:

- read `AGENTS.md`;
- read `/kb/task_statuses.md`;
- read `/tasks/TASK-0001/status.md`;
- read `/tasks/TASK-0001/brief.md`;
- read `/tasks/TASK-0001/orchestration_plan.md`;
- read this handoff file;
- read research artifacts;
- verify current status is still `writing`;
- continue only from `next required action`.

Last known reliable state:

- Current status: `writing`
- Completed stage: `planning`
- Last completed artifact: `/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md`
- Next role: `writer_agent`
- Next action: create outline, draft, writer notes, and claims-used
- Blocking issue, if any: `none`
