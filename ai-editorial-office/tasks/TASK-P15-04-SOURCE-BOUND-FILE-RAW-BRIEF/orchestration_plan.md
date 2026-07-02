# Orchestration Plan

## task summary

- Task ID: TASK-P15-04-SOURCE-BOUND-FILE-RAW-BRIEF
- User goal: test P1.5 Raw Brief Normalization on a file-dependent rewrite
  request.
- Deliverable: task-local `brief.md` and `normalization-check.md`.
- Audience/channel: user / ChatGPT review.
- Current active version: initial normalization result.

## task classification

- Task type: intake normalization test
- Risk mode: low-risk
- Factual sensitivity: standard for future rewrite, low for this no-source test
- Human approval likely required: no
- Rationale: no source processing, rewrite, draft, answer structure, or
  production system change is performed.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: narrow test of Intake Agent source-status behavior.
- Forbidden depth shortcuts: do not inspect source, invent source content, or
  create an answer/structure.
- Expanded profile trigger, if any: accidental source claim or rewrite output.

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
| Success criterion | `defined` |
| Approval boundary | `unknown` |
| Missing data strategy | `block` |

- Rationale: source file is required before any rewrite can start.
- Production may start: no
- If `block`: wait for `task.md` to be provided or verified.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize raw request |
| Orchestration | chief_editor | yes | Route as compact test |
| Writing | writer_agent | no | Rewrite is explicitly forbidden in this test |
| Review | review_agent | no | No production material or system change |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User test request | Compact route | Scope constrained |
| 2 | intake_agent | Raw request | `brief.md` | Source status marked |
| 3 | intake_agent | Brief and raw request | `normalization-check.md` | Fantasy check complete |
| 4 | chief_editor | Task-local artifacts | Final status | Passed/failed conclusion recorded |

## completion criteria

- `brief.md` exists.
- `normalization-check.md` exists.
- Required normalization categories are shown.
- No source content is invented.
- No answer, draft, or answer structure is created.
- No production files are changed.
