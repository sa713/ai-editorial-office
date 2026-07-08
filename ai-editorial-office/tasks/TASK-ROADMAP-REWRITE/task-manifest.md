# Task Manifest

## task identity

- Task ID: `TASK-ROADMAP-REWRITE`
- Task title: Rewrite Project Roadmap
- Task type: roadmap strategy rewrite
- Owner/current role: `chief_editor`
- Created: 2026-07-08
- Last updated: 2026-07-08

## current state

- Current status: `finalized`
- Selected pipeline: `review`
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `../../ROADMAP.md`
- Latest relevant handoff: none
- Next required action: final validation, commit, and delivery report

## freshness

- Last verified: 2026-07-08
- Verified by: `chief_editor`
- Stale if: project lead changes strategic stages, current stage, or next
  planned release.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `../../ROADMAP.md`
  - `../../../README.md`
  - `../../project-state.md`
- Replaces: obsolete roadmap structure in `../../ROADMAP.md`
- Deprecated/previous versions: previous P0-P10 roadmap content
- Versions no longer working artifacts: previous P0-P10 roadmap content
- Version conflict state: none
- What to read on restart:
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - `review.md`
  - `final.md`
  - `final_decision.md`
  - `../../ROADMAP.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: user requested rewrite, validation, and final commit
  hash
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User scope and constraints |
| `task-manifest.md` | yes | required | Current task state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | State history |
| `../../ROADMAP.md` | yes | required | Rewritten roadmap |
| `../../../README.md` | yes | conditional | Lightweight navigation |
| `../../project-state.md` | yes | conditional | Current strategic state |
| `review.md` | yes | required | Independent review |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Governance closure |

## stale or conflicting state

- None known.

## active constraints

- User constraints: no architecture changes, no `AGENTS.md` changes, no
  capability-definition changes, no `/about` sync, no redaction-path edits.
- Pipeline constraints: review required before finalization.
- Client-profile constraints: none.
- Governance constraints: roadmap remains strategic and non-canonical.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../project-state.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`.

Next action:

- Role: `chief_editor`
- Action: run validation, commit, and deliver summary
- Expected output: committed roadmap replacement and final response
- Stop conditions: validation failure, accidental architecture change, or
  conflict with canonical owners.

## lifecycle notes

- Safe-to-ignore material: pre-existing untracked `diff_intake.md`.
