# Orchestration Plan

## task summary

- Task ID: TASK-P15-02-INCOMPLETE-RAW-BRIEF
- User goal: test P1.5 Raw Brief Normalization on an incomplete request.
- Deliverable: task-local `brief.md` and `normalization-check.md`.
- Audience/channel: user / ChatGPT review.
- Current active version: initial normalization result.

## task classification

- Task type: intake normalization test
- Risk mode: low-risk
- Factual sensitivity: low
- Human approval likely required: no
- Rationale: no material, draft, structure, source claims, or production system
  changes.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: narrow test of Intake Agent behavior.
- Forbidden depth shortcuts: do not write material or create a future material
  plan; do not invent missing brief fields.
- Expanded profile trigger, if any: conflict with editorial entry rules.

## selected pipeline

- Pipeline: compact intake normalization test
- Why this pipeline: output is only a normalized brief/task definition.
- Pipeline exceptions or local constraints: no new production pipeline is
  created.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `unknown` |
| Channel or context | `unknown` |
| Deliverable | `unclear` |
| Source boundary | `unclear` |
| Success criterion | `unclear` |
| Approval boundary | `unknown` |
| Missing data strategy | `ask` |

- Rationale: production would require inventing multiple material facts.
- Production may start: no
- If `ask`: ask for update details, artifact type, audience, channel, goal,
  source, and acceptance criteria.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize raw request |
| Orchestration | chief_editor | yes | Route as compact test |
| Writing | writer_agent | no | Material writing is explicitly forbidden |
| Review | review_agent | no | No production material or system change |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User test request | Compact route | Scope constrained |
| 2 | intake_agent | Raw request | `brief.md` | Missing fields marked |
| 3 | intake_agent | Brief and raw request | `normalization-check.md` | Fantasy check complete |
| 4 | chief_editor | Task-local artifacts | Final status | Passed/failed conclusion recorded |

## completion criteria

- `brief.md` exists.
- `normalization-check.md` exists.
- Required normalization categories are shown.
- No material, draft, outline, structure, or material plan is created.
- No production files are changed.
