# Handoff

## handoff metadata

Task ID: `TASK-0001`

Handoff file: `handoff-review-review-agent-to-final-editor.md`

Handoff type: `stage-specific`

Stage: `review`

Created by: `review_agent`

Created for: `final_editor`

Created at: `2026-05-16 00:01:30 MSK`

Related status file: `/tasks/TASK-0001/status.md`

Related review file: `/tasks/TASK-0001/review.md`

Authority source: `AGENTS.md`

State model source: `/kb/task_statuses.md`

## sending role

Role: `review_agent`

Agent spec: `/agents/review_agent.md`

Work completed by this role:

- Performed independent review;
- Created `review.md`;
- Created `qa-checklist.md`;
- Created `review-summary.md`;
- Created `reviewer-notes.md`;
- Updated `status.md` to `approved`;
- Routed the task to `final_editor`.

Decision boundaries observed:

- Review Agent did not rewrite the article.
- Review Agent did not create `final.md`, `final_decision.md`, `approval.md`, or publication artifacts.
- Review Agent did not make final governance or human approval decisions.

## receiving role

Role: `final_editor`

Agent spec: `/agents/final_editor.md`

Expected responsibility:

- Create controlled finalization artifacts after approved review;
- Preserve approved meaning, caveats, and claim boundaries;
- Avoid introducing new facts, sources, statistics, internal examples, or approval language;
- Hand off to `chief_editor` for final governance decision.

## review outcome

Review outcome: `approved`

Mapped operational status: `approved`

Recommended next status during finalization: remain `approved` until Chief Editor final governance decides next status.

## reviewed artifacts

Final Editor should read:

- `AGENTS.md`;
- `/kb/task_statuses.md`;
- `/kb/editorial_policy.md`;
- `/kb/tone_of_voice.md`;
- `/kb/forbidden_patterns.md`;
- `/kb/ux_writing_guidelines.md`;
- `/kb/glossary.md`;
- `/pipelines/article_pipeline.md`;
- `/agents/final_editor.md`;
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
- `/tasks/TASK-0001/claims-used.md`;
- `/tasks/TASK-0001/writer-notes.md`;
- `/tasks/TASK-0001/review.md`;
- `/tasks/TASK-0001/qa-checklist.md`;
- `/tasks/TASK-0001/review-summary.md`;
- `/tasks/TASK-0001/reviewer-notes.md`;
- this handoff.

## blockers

None.

## required changes

No required changes from review.

## finalization constraints

Final Editor must:

- preserve no-hype, practical tone;
- preserve the central distinction between AI assistance and human editorial responsibility;
- preserve caveats for C1, C3, C4, and C7;
- preserve exclusion of blocked claims C8, C9, C10, and C11;
- avoid numeric productivity claims;
- avoid invented internal practices or policies;
- avoid vendor-specific superiority claims;
- avoid publication, approval, or governance language;
- not create `final_decision.md` or `approval.md`.

## factual risks

| Risk | Handling |
| --- | --- |
| Internal examples unavailable. | Keep generic examples unless user/Chief Editor supplies source material. |
| Human approval unknown. | Leave for Chief Editor governance after finalization. |
| Statistics unsupported. | Do not add statistics. |

## first action for receiving role

Create:

- `/tasks/TASK-0001/final.md`;
- `/tasks/TASK-0001/finalization-notes.md`;
- `/tasks/TASK-0001/finalization-checklist.md`;
- handoff to `chief_editor`.

Then leave Chief Editor to create `final_decision.md` and update governance status.
