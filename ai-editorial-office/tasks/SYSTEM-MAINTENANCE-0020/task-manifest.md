# Task Manifest

## task identity

- Task ID: `SYSTEM-MAINTENANCE-0020`
- Task title: User Feedback Loop for AI editorial office
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
- Stale if: system files are changed without updating `changed-files.md`, `review.md`, and `final_decision.md`

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: task-local maintenance package plus explicitly listed system-file changes in `changed-files.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `task-manifest.md`, `orchestration_plan.md`, `design-note.md`, `changed-files.md`, `review.md` if present
- Old versions read only for: pilot examples and reviewer-governance traceability
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
| `orchestration_plan.md` | yes | required | Compact execution contract |
| `design-note.md` | yes | required | Must precede system-file changes |
| `changed-files.md` | yes | required | Records system files created or updated |
| `diff.md` | yes | optional/user-requested | Diff for selected system files |
| `pilot-feedback-examples.md` | yes | required | Demonstrates old-task handling without mutating old tasks |
| `review.md` | yes | required | Independent review approved |
| `final_decision.md` | yes | required | Chief Editor governance decision |

## stale or conflicting state

- None.

## active constraints

- Feedback capture must remain optional.
- Do not create new roles.
- Do not create a heavy new pipeline.
- Do not activate visual subsystem.
- Do not change review-gate, governance, or task status model unless strictly necessary.
- Do not rewrite old tasks or add `feedback.md` into old `TASK-*` folders.
- Keep `AGENTS.md` changes minimal and targeted if used.

## open questions

- None blocking. Preferred feedback pattern log location will be decided in `design-note.md`.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `orchestration_plan.md`;
- `design-note.md`;
- `changed-files.md` if present.

Next action:

- Role: none
- Action: none
- Expected output: none
- Stop conditions: any change would make feedback mandatory, create a new role, reopen old tasks automatically, or alter governance/status model

## lifecycle notes

- Legacy task folders consulted: yes, only for pilot examples and maintenance pattern comparison
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated historical task content outside explicit pilot examples
