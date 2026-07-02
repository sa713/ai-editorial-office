# Task Manifest

## task identity

- Task ID: `TASK-CARE-PR-EDF-CHECK`
- Task title: CARE PR Editorial Decision Frame check
- Task type: review / mechanism test-run
- Owner/current role: `review_agent`
- Created: 2026-06-30
- Last updated: 2026-06-30

## current state

- Current status: `human_approval_required`
- Selected pipeline: review / mechanism test-run
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `review-addendum.md`
- Latest relevant handoff: none
- Next required action: user decides whether this task-local check should be
  copied into the external CARE PR task folder.

## governance state

- Review required: yes.
- Review artifact/current version: `review-addendum.md`
- Review outcome: `works_partially`
- Compact finalization shape allowed: yes.
- Human approval required: yes, only for writing into the external CARE PR
  folder outside the current workspace.
- Human approval evidence: external CARE PR folder was provided by the user, but
  no explicit write approval for that external path was requested or granted.
- Final decision artifact: not applicable.

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized check request |
| `task-manifest.md` | yes | required | Current test-run state |
| `status.md` | yes | required | Progress and external-write boundary |
| `orchestration_plan.md` | yes | required | Contains CARE PR Editorial Decision Frame |
| `search-report.md` | yes | conditional | Records source discovery |
| `review-addendum.md` | yes | required | Review Agent assessment of the frame |

## active constraints

- User constraints: test CARE PR without architecture changes or production
  edits.
- Pipeline constraints: do not rewrite `final.md` merely to exercise the new
  mechanism.
- Governance constraints: production files unchanged by this test-run.
- Filesystem constraint: external CARE PR folder is read-only unless explicit
  write approval is granted.

## open questions

- Should the task-local Editorial Decision Frame and review addendum be copied
  into `/Users/sa/Documents/codex/Care/PR/TASK-CARE-PR-STRATEGY`?

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `orchestration_plan.md`;
- `review-addendum.md`;
- external CARE PR `final.md` and `review.md`.

Next action:

- Role: user / Chief Editor
- Action: decide whether to apply the task-local check to the external CARE PR
  folder.
- Expected output: either no further action, or an explicit instruction to write
  the addendum into the external folder.
