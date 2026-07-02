# Orchestration Plan

Task ID: `TASK-0003`

Owner: `chief_editor`

Created at: `2026-05-19 18:12:43 MSK`

## pipeline

Selected pipeline: `/pipelines/social_pipeline.md`

Pipeline rationale:

- deliverable is a short internal announcement;
- platform-specific brevity and tone constraints matter;
- no external research is required because the task facts are supplied by the user;
- independent review and finalization remain required.

## risk mode

Confirmed risk mode: `low-risk`

Risk rationale:

- internal short-form editorial copy;
- no sensitive factual claims beyond user-supplied context;
- no exact number of heroes, names, links, or contact details are invented;
- no publication approval requested inside the task.

## role sequence

1. `intake_agent`: normalize task and constraints.
2. `chief_editor`: confirm intent, structure, pipeline, risk mode.
3. `writer_agent`: create proposed structure and three announcement variants.
4. `review_agent`: independently review variants and select strongest direction.
5. `writer_agent`: apply bounded revision to selected version.
6. `review_agent`: bounded re-review.
7. `final_editor`: produce final announcement text.
8. `chief_editor`: final governance decision and compact handoff.

## artifact scope

Required:

- `brief.md`;
- `task-manifest.md`;
- `status.md`;
- `orchestration_plan.md`;
- `outline.md`;
- `draft.md`;
- `writer-notes.md`;
- `review.md`;
- `qa-checklist.md`;
- `review-summary.md`;
- `bounded-revision.md`;
- `final.md`;
- `finalization-notes.md`;
- `final_decision.md`;
- role handoffs.

Research artifacts intentionally omitted:

- no `research.md`, `sources.md`, `facts.md`, `claims_table.md`, or `claims-used.md` because the task relies only on user-supplied facts and avoids material factual claims beyond the brief.

## writing constraints

- Put the format change early.
- Keep the text short.
- Let interest come from the new editorial situation, not from encouragement.
- Do not overexplain the magazine.
- Avoid HR framing around young specialists.
- Avoid synthetic warmth and fake excitement.

## review criteria

Review each variant against:

- usefulness;
- reader-state;
- trust;
- failure patterns;
- synthetic tone.

Primary review question:

```text
Does this announcement make the changed issue feel worth opening because colleagues become a little more visible and human, without sounding like HR or a corporate mailing?
```
