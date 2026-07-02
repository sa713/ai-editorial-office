# Orchestration Plan

## task summary

- Task ID: TASK-P15-03-EXTERNAL-SOURCE-RAW-BRIEF
- User goal: test P1.5 Raw Brief Normalization on an external-source request.
- Deliverable: task-local `brief.md` and `normalization-check.md`.
- Audience/channel: user / ChatGPT review.
- Current active version: initial normalization result.

## task classification

- Task type: intake normalization test
- Risk mode: low-risk
- Factual sensitivity: standard for future task, low for this no-research test
- Human approval likely required: no
- Rationale: no source access, no research, no explanation, and no production
  system changes are performed.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: narrow test of Intake Agent source-status behavior.
- Forbidden depth shortcuts: do not open source, research, summarize, or infer
  source content.
- Expanded profile trigger, if any: accidental source claim or source access.

## selected pipeline

- Pipeline: compact intake normalization test
- Why this pipeline: output is only a normalized brief/task definition.
- Pipeline exceptions or local constraints: no new production pipeline is
  created.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `inferred` |
| Channel or context | `unknown` |
| Deliverable | `defined` |
| Source boundary | `unclear` |
| Success criterion | `defined` |
| Approval boundary | `unknown` |
| Missing data strategy | `constrain` |

- Rationale: the test can proceed only by constraining output to intake
  normalization and marking source status as not opened/reviewed.
- Production may start: no
- If `constrain`: create only normalization artifacts; do not research.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize raw request |
| Orchestration | chief_editor | yes | Route as compact test |
| Research | research_agent | no | Research is explicitly forbidden in this test |
| Writing | writer_agent | no | Explanation/summary is explicitly forbidden |
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
- No source is opened.
- No explanation, summary, outline, or source content claim is created.
- No production files are changed.
