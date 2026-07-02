# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-writing-writer-agent-to-review-agent.md`

Handoff type: `stage-specific`

Stage: `writing`

Created by: `writer_agent`

Created for: `review_agent`

Created at: `2026-05-15 23:54:48 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `writer_agent`

Agent spec: `/agents/writer_agent.md`

Work completed by this role:

- Created `outline.md`;
- Created `draft.md`;
- Created `writer-notes.md`;
- Created `claims-used.md`;
- Created this handoff to `review_agent`;
- Updated `status.md` from `writing` to `review`.

Decision boundaries observed:

- Writer Agent did not perform review.
- Writer Agent did not create `review.md`, `qa-checklist.md`, `review-summary.md`, or `reviewer-notes.md`.
- Writer Agent did not create `final.md`, `final_decision.md`, or `approval.md`.
- Writer Agent did not add sources, statistics, internal examples, or final approval language.

## receiving role

Role: `review_agent`

Expected responsibility:

- Independently review the draft and writing artifacts;
- Check compliance with brief, orchestration plan, KB, research artifacts, and claims traceability;
- Create review-stage artifacts according to Article Pipeline and the Review Agent spec.

The receiving role must not rely on chat history.

## current status

Current task status: `review`

Previous task status: `writing`

Status transition reason:

- Writing artifacts now exist and the draft is ready for independent review.

Review gate status: `not_started_by_review_agent`

## artifacts created by Writer Agent

| Artifact | Purpose | Ready for review |
| --- | --- | --- |
| `/tasks/TASK-0001/outline.md` | Planned structure and evidence dependencies. | `yes` |
| `/tasks/TASK-0001/draft.md` | Draft article, not final copy. | `yes` |
| `/tasks/TASK-0001/writer-notes.md` | Assumptions, exclusions, caveats, weak spots, review attention points. | `yes` |
| `/tasks/TASK-0001/claims-used.md` | Traceability from draft claims to `claims_table.md`. | `yes` |
| `/tasks/TASK-0001/handoff-writing-writer-agent-to-review-agent.md` | Transfer context to Review Agent. | `yes` |

## required review inputs

Review Agent should read:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/forbidden_patterns.md`;
- `/kb/ux_writing_guidelines.md`;
- `/kb/glossary.md`;
- `/pipelines/article_pipeline.md`;
- `/agents/review_agent.md`;
- `/tasks/TASK-0001/brief.md`;
- `/tasks/TASK-0001/status.md`;
- `/tasks/TASK-0001/orchestration_plan.md`;
- `/tasks/TASK-0001/research.md`;
- `/tasks/TASK-0001/sources.md`;
- `/tasks/TASK-0001/facts.md`;
- `/tasks/TASK-0001/claims_table.md`;
- `/tasks/TASK-0001/open-questions.md`;
- `/tasks/TASK-0001/outline.md`;
- `/tasks/TASK-0001/draft.md`;
- `/tasks/TASK-0001/writer-notes.md`;
- `/tasks/TASK-0001/claims-used.md`;
- this handoff.

## review focus

Review Agent should check:

- Draft matches the brief: internal portal article, calm practical tone, about 4000 characters.
- Draft remains a draft and does not claim final approval.
- No AI hype or replacement rhetoric.
- No unsupported productivity claims, numeric claims, or "always saves time" language.
- No organization-specific practices, examples, or policies are invented.
- Generic examples do not read as internal facts.
- All factual claims used in the draft are traceable through `claims-used.md`.
- Caveated claims C1, C3, C4, and C7 remain caveated.
- Blocked claims C8, C9, C10, and C11 are not used as factual claims.
- UX examples do not invent product behavior or hide user-facing constraints.

## known limitations

| Limitation | Blocks review | Notes |
| --- | --- | --- |
| No internal examples or policies were supplied. | `no` | Draft uses generic examples only. |
| No numeric productivity evidence exists. | `no` | Draft contains no numeric productivity claims. |
| Human approval requirement is unknown. | `no` | Should be reassessed later by Chief Editor/final governance. |

## recommended next action

Review Agent should perform independent review and create the required review artifacts. Valid review outcomes remain `approved`, `changes_requested`, or `blocked` according to the local system.
