# Task Manifest

## task identity

- Task ID: `TASK-BUILD-PROJECT-BACKLOG`
- Task title: Build Project Backlog
- Task type: operational planning
- Owner/current role: `chief_editor`
- Created: 2026-07-08
- Last updated: 2026-07-08

## current state

- Current status: `finalized`
- Selected pipeline: `review`
- Risk mode: `low`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `../../BACKLOG.md`
- Latest relevant handoff: none
- Next required action: final validation, commit, and delivery report

## freshness

- Last verified: 2026-07-08
- Verified by: `chief_editor`
- Stale if: roadmap stages, release order, completed release status, or current
  active release changes.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `../../BACKLOG.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart:
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - `review.md`
  - `final.md`
  - `final_decision.md`
  - `../../BACKLOG.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: user requested final commit hash
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User scope and constraints |
| `task-manifest.md` | yes | required | Current task state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | State history |
| `../../BACKLOG.md` | yes | required | Operational backlog |
| `review.md` | yes | required | Independent review |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Governance closure |

## stale or conflicting state

- None known.

## active constraints

- User constraints: only create the backlog; no architecture, capability,
  pipeline, role, lifecycle, `AGENTS.md`, or redaction-path edits.
- Pipeline constraints: review required before finalization.
- Client-profile constraints: none.
- Governance constraints: backlog is operational planning and does not override
  roadmap or canonical files.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- `../../BACKLOG.md`.

Next action:

- Role: `chief_editor`
- Action: run validation, commit, and deliver summary
- Expected output: committed `BACKLOG.md`
- Stop conditions: validation failure or accidental excluded-file change.

## lifecycle notes

- Safe-to-ignore material: pre-existing untracked `diff_intake.md`.
