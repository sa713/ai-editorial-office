# Task Manifest

## task identity

- Task ID: `TASK-EDITORIAL-CHALLENGE-FRAMEWORK`
- Task title: Editorial Challenge Framework implementation
- Task type: production instruction update
- Owner/current role: `chief_editor`
- Created: 2026-06-30
- Last updated: 2026-06-30

## current state

- Current status: `review_ready`
- Selected pipeline: compact production instruction update
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `production-diff.md`
- Latest relevant handoff: none
- Next required action: user review of production diff.

## governance state

- Review required: compact implementation self-check.
- Review artifact/current version: `production-diff.md`.
- Review outcome: ready for user review.
- Compact finalization shape allowed: yes.
- Human approval required: no; user requested implementation.
- Final decision artifact: not applicable.

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized design request |
| `orchestration_plan.md` | yes | required | Route and design-local frames |
| `task-manifest.md` | yes | required | Current state |
| `status.md` | yes | required | Work summary |
| `system_change_proposal.md` | yes | required | Design proposal |
| `production-diff.md` | yes | required by user | Full requested production diff |

## active constraints

- Production edits limited to the four requested files.
- No new roles.
- No mandatory standalone challenge artifact.
- Challenge must test route-validity assumptions and be evidence-backed, not
  preference-backed.
- Reviewer must not rewrite, re-route, finalize, or govern.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `orchestration_plan.md`;
- `system_change_proposal.md`.
- `production-diff.md`.

Next action:

- Role: user
- Action: review implementation diff.
