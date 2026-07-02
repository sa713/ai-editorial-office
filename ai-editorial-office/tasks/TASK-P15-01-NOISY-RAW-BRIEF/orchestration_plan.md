# Orchestration Plan

## task summary

- Task ID: TASK-P15-01-NOISY-RAW-BRIEF
- User goal: test P1.5 Raw Brief Normalization on a noisy raw request.
- Deliverable: task-local `brief.md` and `normalization-check.md`.
- Audience/channel: user / ChatGPT review.
- Current active version: initial normalization result.

## task classification

- Task type: intake normalization test
- Risk mode: low-risk
- Factual sensitivity: low
- Human approval likely required: no
- Rationale: no final post, no source claims, no production system changes.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: this is a narrow test of an intake rule.
- Forbidden depth shortcuts: do not write the post; do not invent missing
  audience, channel, source, or dashboard facts.
- Expanded profile trigger, if any: conflict with editorial entry rules.

## selected pipeline

- Pipeline: compact intake normalization test
- Why this pipeline: no production writing is requested; only Intake Agent
  normalization is needed.
- Pipeline exceptions or local constraints: no new production pipeline is
  created.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `unknown` |
| Channel or context | `unknown` |
| Deliverable | `defined` |
| Source boundary | `unclear` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Rationale: the test can proceed by constraining output to a brief/task
  definition and not writing the post.
- Production may start: no
- If `constrain`: create only normalization artifacts and mark unknowns.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize raw request |
| Orchestration | chief_editor | yes | Route as compact test |
| Writing | writer_agent | no | Post writing is explicitly forbidden |
| Review | review_agent | no | No production material or system change |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User test request | Compact route | Scope constrained |
| 2 | intake_agent | Raw request | `brief.md` | Brief created |
| 3 | intake_agent | Brief and raw request | `normalization-check.md` | Fantasy check complete |
| 4 | chief_editor | Task-local artifacts | Final status | Passed/failed conclusion recorded |

## completion criteria

- `brief.md` exists.
- `normalization-check.md` exists.
- Task signal, background context, noise, confirmed, inferred, unknown,
  assumptions, open questions, source status, and acceptance criteria are shown.
- No post is written.
- No production files are changed.
