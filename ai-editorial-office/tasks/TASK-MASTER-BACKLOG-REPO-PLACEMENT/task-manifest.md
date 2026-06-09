# Task Manifest

## task identity

- Task ID: `TASK-MASTER-BACKLOG-REPO-PLACEMENT`
- Task title: Place master backlog in repo ideas folder
- Task type: system planning artifact placement
- Owner/current role: `chief_editor`
- Created: 2026-06-09
- Last updated: 2026-06-09

## current state

- Current status: `finalized`
- Selected pipeline: `compact_maintenance_mode`
- Risk mode: `low`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `../../ideas/master_backlog.md`
- Latest relevant handoff: none.
- Next required action: none.

## freshness

- Last verified: 2026-06-09
- Verified by: `chief_editor`
- Stale if: source backlog changes outside the repo or the user changes the target placement.

## current version pointers

- Canonical pointer owner: this manifest.
- Current active artifact or artifact set: `../../ideas/master_backlog.md`
- Replaces: root-side local source copy at `/ideas/master_backlog.md` for repo-contained planning use.
- Deprecated/previous versions: none inside `ai-editorial-office/ideas`.
- Versions no longer working artifacts: none.
- Version conflict state: none known.
- What to read on restart: `orchestration_plan.md`, `status.md`, `../../ideas/master_backlog.md`.
- Old versions read only for: source comparison if needed.
- Do not use latest modified as source of truth: yes.

## governance state

- Review required: no.
- Review artifact/current version: not applicable.
- Review outcome: not applicable.
- Compact finalization shape allowed: yes.
- Human approval required: no for requested placement.
- Human approval evidence: user explicitly requested repo placement.
- Final decision artifact: not created; compact maintenance task records decision in status and manifest.

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `task-manifest.md` | yes | required | Compact task state |
| `orchestration_plan.md` | yes | required | Route and boundaries |
| `status.md` | yes | required | State history |
| `../../ideas/master_backlog.md` | yes | required | Requested repo artifact |

## active constraints

- User constraints: add `master_backlog.md` to `ai-editorial-office/ideas`.
- User constraints: update document status to `active draft / placed in repo`.
- User constraints: do not change production files: `AGENTS.md`, agents, pipelines, templates, scripts, tests.
- User constraints: do not move backlog to `/about`.
- Pipeline constraints: use compact maintenance mode; do not expand into content production.
- Client-profile constraints: none.
- Governance constraints: `AGENTS.md` remains higher authority than backlog.

## open questions

- None.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- `orchestration_plan.md`;
- `status.md`;
- `../../ideas/master_backlog.md`.

Next action:

- Role: none.
- Action: task complete.
- Expected output: not applicable.
- Stop conditions: not applicable.
