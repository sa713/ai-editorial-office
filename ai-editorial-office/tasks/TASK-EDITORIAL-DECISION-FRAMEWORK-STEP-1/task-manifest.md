# Task Manifest

## task identity

- Task ID: `TASK-EDITORIAL-DECISION-FRAMEWORK-STEP-1`
- Task title: Editorial Decision Framework, step 1
- Task type: system implementation
- Owner/current role: `chief_editor`
- Created: 2026-06-30
- Last updated: 2026-06-30

## current state

- Current status: `review`
- Selected pipeline: custom system-update mode under Chief Editor orchestration
- Risk mode: `high-governance`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: production architecture files named by the user
- Latest relevant handoff: none
- Next required action: review the production diff.

## governance state

- Review required: after production architecture changes, yes
- Review artifact/current version: pending
- Review outcome: pending
- Compact finalization shape allowed: not applicable
- Human approval required: yes, before implementation
- Human approval evidence: user requested implementation on 2026-06-30
- Final decision artifact: not created in step 1

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized user request |
| `task-manifest.md` | yes | required | Current task state |
| `status.md` | yes | required | Planning status |
| `orchestration_plan.md` | yes | required | Design-only execution contract |
| `system_change_proposal.md` | yes | conditional | Approved proposal basis |

## active constraints

- User constraints: implement only minimal production changes in named files.
- Pipeline constraints: no production work before Chief Editor routing.
- Governance constraints: do not create new production files; preserve lifecycle
  and review-gate.

## open questions

- None.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `system_change_proposal.md`.

Next action:

- Role: user / Review Agent
- Action: review the named production-file diff.
- Expected output: approval or requested changes.
- Stop conditions: do not create new roles, pipelines, statuses, or production
  artifacts.
