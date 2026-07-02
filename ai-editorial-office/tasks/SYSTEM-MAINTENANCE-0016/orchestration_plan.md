# Orchestration Plan

## task summary

- Task ID: `SYSTEM-MAINTENANCE-0016`
- User goal: complete only Step 3 for Normalized Brief Contract.
- Deliverable: production rule in `chief_editor.md` plus required task-local governance artifacts.
- Audience/channel: internal editorial system governance.
- Current active version: Step 3 implementation in `ai-editorial-office/agents/chief_editor.md`.

## task classification

- Task type: `governance/system-improvement`
- Risk mode: `standard`
- Factual sensitivity: low; this is repository governance and role behavior.
- Human approval likely required: no additional approval requested for Step 3.
- Rationale: the change affects Chief Editor routing behavior but does not alter Intake, pipeline sequence, review, visual subsystem, role model, or task status model.

## selected mode

- Pipeline: `not_applicable`
- Mode: compact governance update implementation.
- Why: the user requested a bounded system mechanism update, not a production content task.
- Forbidden changes: Intake Agent, pipelines, review, visual subsystem, role model, and task status model.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Entry routing | `chief_editor` | yes | Activated to classify the update and preserve boundaries. |
| Production owner | `chief_editor` | yes | Owns how normalized briefs are accepted for routing. |
| Intake | `intake_agent` | no | Explicitly not changed in Step 3. |
| Review | `review_agent` | no | No review behavior changed; user requested only Step 3. |

## Step 3 implementation contract

Implement a new `Normalized Brief Contract` section in:

```text
ai-editorial-office/agents/chief_editor.md
```

The section must:

- state that normalized brief is a working basis, not automatically confirmed facts;
- distinguish `Confirmed`, `Inferred`, and `Unknown`;
- allow Chief Editor to use inferred context for pipeline, mode, role, and risk-mode choices when confidence is sufficient;
- require clarification when inferred context materially affects the result, changes audience, changes task meaning, or could cause the wrong result;
- include the requested email-after-meeting and employee-announcement examples.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 3 | `chief_editor` | Step 1 and Step 2 artifacts and user request | updated execution contract | Scope remains bounded to Step 3. |
| 3 | `chief_editor` | owner file | `Normalized Brief Contract` section | Section contains labels, allowed use, escalation rule, and examples. |
| 3 | `chief_editor` | changed files | updated task-local artifacts | Protected areas confirmed unchanged. |

## completion criteria

- `chief_editor.md` contains the new section.
- `Confirmed`, `Inferred`, and `Unknown` are defined.
- Inferred context can support routing decisions when safe.
- Escalation rule is present.
- Required examples are present.
- Required Step 3 artifacts are updated or created.
- Intake Agent, pipelines, review, visual subsystem, role model, and task status model remain unchanged.

