# Task Manifest

## task identity

- Task ID: `SYSTEM-MAINTENANCE-UPDATE-0021`
- Task title: Preflight Gate before production
- Task type: `editorial system update / process maintenance`
- Owner/current role: none; task finalized
- Created: 2026-06-04
- Last updated: 2026-06-04

## current state

- Current status: `finalized`
- Selected pipeline: `custom workflow mini-contract`
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Current working artifact: `final_decision.md`
- Latest relevant handoff: none
- Next required action: none

## freshness

- Last verified: 2026-06-04
- Verified by: `chief_editor`
- Stale if: system files are changed without updating `changed-files.md`, `diff.md`, `review.md`, and `final_decision.md`

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: task-local maintenance package plus changed system files recorded in `changed-files.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `task-manifest.md`, `orchestration_plan.md`, `design-note.md`, `changed-files.md`, `diff.md` if present, `review.md` if present
- Old versions read only for: pilot examples and review/governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: user explicitly requested the system update in the current task
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `task-manifest.md` | yes | required | Current state pointer |
| `orchestration_plan.md` | yes | required | Compact maintenance contract |
| `status.md` | yes | required | State history |
| `design-note.md` | yes | required | Must precede system-file changes |
| `changed-files.md` | yes | required | System and task-local change trace |
| `diff.md` | yes | required by user | Diff of changed system files |
| `pilot-preflight-examples.md` | yes | required | Demonstrates ASK/CONSTRAIN/PROCEED/BLOCK |
| `review.md` | yes | required | Independent compatibility review approved |
| `final_decision.md` | yes | required | Chief Editor governance decision |

## stale or conflicting state

- None.

## active constraints

- Do not create a new pipeline.
- Do not create a new role.
- Do not create a new mandatory artifact for every task.
- Do not force clarifying questions when safe inference or constraints are enough.
- Do not rewrite roles or pipelines wholesale.
- Do not change review-gate, governance, task status model, or visual subsystem.
- Create `diff.md` for changed system files.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `orchestration_plan.md`;
- `design-note.md`;
- `changed-files.md` and `diff.md` after implementation.

Next action:

- Role: none
- Action: none
- Expected output: none
- Stop conditions: the gate becomes a new status, new role, new pipeline, mandatory new artifact, or question-generation routine

## lifecycle notes

- Legacy task folders consulted: yes, only for TASK-0024 source signal and pilot examples
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated old task content outside pilot examples
