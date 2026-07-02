# Orchestration Plan

## task summary

- Task ID: TASK-P15-05-MANAGEMENT-RAW-BRIEF
- User goal: test P1.5 Raw Brief Normalization on a short management request.
- Deliverable: task-local `brief.md` and `normalization-check.md`.
- Audience/channel: user / ChatGPT review.
- Current active version: initial normalization result.

## task classification

- Task type: intake normalization test
- Risk mode: low-risk
- Factual sensitivity: low for this no-design test
- Human approval likely required: no
- Rationale: no plan, roadmap, architecture, change list, or production system
  change is performed.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: narrow test of Intake Agent behavior on management requests.
- Forbidden depth shortcuts: do not turn normalization into Sber-mode design.
- Expanded profile trigger, if any: accidental plan, roadmap, architecture, or
  Sber requirement claim.

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
| Deliverable | `defined` |
| Source boundary | `unclear` |
| Success criterion | `unclear` |
| Approval boundary | `unknown` |
| Missing data strategy | `ask` |

- Rationale: future planning would require scope, problem statement, source
  boundary, and approval boundary.
- Production may start: no
- If `ask`: ask for problem statement, intended reader, source policy/examples,
  scope, and expected depth before planning.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize raw request |
| Orchestration | chief_editor | yes | Route as compact test |
| Planning/design | chief_editor | no | Future planning is explicitly forbidden in this test |
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
- No plan, roadmap, architecture, change list, or Sber-mode design is created.
- No production files are changed.
