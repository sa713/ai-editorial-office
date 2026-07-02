# Task Manifest

## task identity

- Task ID: `TASK-EDITORIAL-DECISION-FRAMEWORK-COMPACTNESS`
- Task title: Editorial Decision Frame compactness normalization
- Task type: production instruction normalization
- Owner/current role: `chief_editor`
- Created: 2026-06-30
- Last updated: 2026-06-30

## current state

- Current status: `review_ready`
- Selected pipeline: compact system-instruction update
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `production-diff.md`
- Latest relevant handoff: none
- Next required action: user review.

## governance state

- Review required: compact self-check.
- Review artifact/current version: this manifest plus `production-diff.md`.
- Review outcome: ready for user review.
- Compact finalization shape allowed: yes.
- Human approval required: no.
- Final decision artifact: not applicable.

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized request |
| `orchestration_plan.md` | yes | required | Route and decision frame |
| `task-manifest.md` | yes | required | Current state |
| `status.md` | yes | required | Change summary |
| `production-diff.md` | yes | required by user | Full requested diff |

## active constraints

- No new production files.
- No Writer Agent or UX Writer edits unless strictly necessary.
- No architecture, role, lifecycle, or review-gate changes.
- Keep the change focused on frame compactness.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `orchestration_plan.md`;
- `production-diff.md`.

Next action:

- Role: user
- Action: review the patch.
- Expected output: approval, requested adjustment, or instruction to commit.
