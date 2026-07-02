# Task Manifest

## task identity

- Task ID: `TASK-P5-5-CUSTOMER-FEEDBACK-LOOP`
- Task title: P5.5 Customer Feedback Loop
- Task type: system update / editorial workflow refinement
- Owner/current role: `chief_editor`
- Created: 2026-06-11
- Last updated: 2026-06-11

## current state

- Current status: `review`
- Selected pipeline: compact governed system-update mode
- Risk mode: standard
- Process depth: compact
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: production patch for P5.5
- Latest relevant handoff: none
- Next required action: user review of diff and check-pack

## governance state

- Review required: yes, by user review of diff
- Review artifact/current version: check-pack for user review
- Review outcome: pending
- Compact finalization shape allowed: yes
- Human approval required: yes
- Human approval evidence: pending user review
- Final decision artifact: not created for this local system-update packet

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Local execution brief. |
| `task-manifest.md` | yes | required | Current state pointer. |
| `orchestration_plan.md` | yes | required | Routing and role contract. |
| `status.md` | yes | required | State history. |
| `implementation-notes.md` | yes | required | Records existing feedback points and integration rationale. |
| `check-pack.md` | yes | required | Manual/smoke check evidence for review. |

## active constraints

- User constraints: no new agents, no review-gate changes, no mandatory
  `feedback.md`, no automatic watchlist/backlog updates.
- Pipeline constraints: preserve role separation and task-local artifacts.
- Client-profile constraints: none.
- Governance constraints: production changes require user review.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- `ai-editorial-office/AGENTS.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `ideas/master_backlog.md`;
- `ideas/engineering_watchlist.md`;
- existing feedback KB/template and role files.

Next action:

- Role: `chief_editor`
- Action: review compact P5.5 workflow patch.
- Expected output: approval, requested changes, or stop decision.
- Stop conditions: any requested change would add a role, weaken review-gate, or
  make feedback artifacts mandatory.

## lifecycle notes

- Legacy task folders consulted: no.
- Old artifact versions consulted: existing tests/templates only.
- Safe-to-ignore material: unrelated task folders and untracked user materials.
