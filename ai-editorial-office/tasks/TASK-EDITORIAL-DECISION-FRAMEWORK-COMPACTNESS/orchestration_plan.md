# Orchestration Plan

## task summary

- Task ID: `TASK-EDITORIAL-DECISION-FRAMEWORK-COMPACTNESS`
- User goal: compact the Editorial Decision Frame format after the CARE PR
  test-run.
- Deliverable: minimal production instruction patch and saved diff.
- Current active version: `production-diff.md`

## task classification

- Task type: production instruction normalization.
- Risk mode: `standard`
- Factual sensitivity: low.
- Human approval likely required: no.
- Rationale: changes affect production operating instructions, but only format
  guardrails for an existing mechanism.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the target is a narrow format clarification.
- Forbidden depth shortcuts: do not alter roles, lifecycle, review-gate, or
  Writer/UX behavior unless required.
- Expanded profile trigger, if any: contradictions with the existing lifecycle.

## selected pipeline

- Pipeline: compact system-instruction update.
- Why this pipeline: the task is a local production-doc patch with reviewable
  diff, not a content production task.
- Pipeline exceptions or local constraints: no new production files.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the user gave exact files, behavior, and acceptance criteria.
- Production may start: yes.

## editorial decision frame

- Chosen editorial route: compact the existing frame instructions in place.
- Why this route serves the task: it fixes the CARE PR test-run weakness without
  adding roles, artifacts, or lifecycle steps.
- Alternatives considered, usually 2-3 compact options:
  - Add a new decision artifact:
    - Why rejected: violates the minimal-entity constraint and duplicates the
      orchestration plan.
  - Expand Writer/UX instructions:
    - Why rejected: current Writer/UX contract already covers use of the frame.
  - Add only template wording:
    - Why rejected: reviewer enforcement also needs to catch bloated frames.
- Writer/UX Writer contract: not applicable; no writing assignment.
- Review focus: check compactness guardrails, handoff brevity, reviewer
  enforcement, and no unnecessary Writer/UX changes.
- Reroute triggers: if compactness requires architecture changes, stop and
  return to Chief Editor.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Scope and route production-doc patch |
| Implementation | Chief Editor / Codex | yes | Apply minimal instruction updates |
| Review | Review Agent | compact self-check | Verify acceptance criteria and diff |

## completion criteria

- Production instructions protect the frame from expansion.
- Template gives short alternative format.
- Handoff remains a short summary.
- Review Agent can flag formal or bloated frames.
- Writer Agent and UX Writer are not changed by this compactness pass.
- Full requested diff is saved task-locally.
