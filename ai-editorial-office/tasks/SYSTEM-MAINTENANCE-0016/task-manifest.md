# Task Manifest

## task identity

- Task ID: `SYSTEM-MAINTENANCE-0016`
- Task title: Normalized Brief Contract
- Task type: `governance/system-improvement`
- Owner/current role: `chief_editor`
- Created: 2026-06-02
- Last updated: 2026-06-02

## current state

- Current status: `step-3-complete`
- Selected pipeline: `not_applicable`
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Current working artifact: `ai-editorial-office/agents/chief_editor.md`
- Latest relevant handoff: none
- Next required action: none for Step 3

## routing decision

- Activated role: `chief_editor`
- Task type determined: governance/system-improvement for editorial entry behavior.
- Pipeline/mode chosen: no production pipeline; compact governance update implementation.
- Step 1 canonical owner decision preserved: `/ai-editorial-office/agents/intake_agent.md` for Raw Brief Normalization.
- Step 2 production owner preserved: `intake_agent`.
- Step 3 production owner selected: `chief_editor`.

## implemented behavior

`chief_editor.md` now has a `Normalized Brief Contract` section.

The added contract tells Chief Editor to use a normalized brief as a working routing basis while distinguishing confirmed, inferred, and unknown context.

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `task-manifest.md` | yes | required | Current task state and routing pointer. |
| `orchestration_plan.md` | yes | required | Step 3 execution contract. |
| `status.md` | yes | required | State transition and completion note. |
| `implementation-plan.md` | yes | required by user | Step 3 implementation plan. |
| `changed-files.md` | yes | required by user | Records production and task-local changes. |
| `normalized-brief-contract-decisions.md` | yes | required by user | Step 3 contract decisions. |
| `raw-brief-normalization-decisions.md` | historical | optional | Step 2 mechanism decisions. |
| `raw-brief-decisions.md` | historical | optional | Step 1 canonical owner decision. |
| `safety-check.md` | yes | required by user | Confirms protected areas were not changed. |
| `rollback-notes.md` | yes | required by user | Rollback scope for Step 3. |
| `diff.md` | yes | required by user | Contains diff section for `chief_editor.md`. |

## active constraints

- Execute only Step 3 of `SYSTEM-MAINTENANCE-0016`.
- Change only the selected owner file for production behavior: `ai-editorial-office/agents/chief_editor.md`.
- Do not change Intake Agent.
- Do not change pipelines.
- Do not change review.
- Do not change visual subsystem.
- Do not change role model.
- Do not change task status model.

## open questions

- None for Step 3.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `ai-editorial-office/agents/chief_editor.md`;
- `normalized-brief-contract-decisions.md`;
- `safety-check.md`.

Next action:

- Role: none unless the user requests a later step.
- Action: no further Step 3 action required.
- Expected output: not applicable.
- Stop conditions: any requested change to Intake Agent, pipelines, review, visual subsystem, role model, or task status model.
