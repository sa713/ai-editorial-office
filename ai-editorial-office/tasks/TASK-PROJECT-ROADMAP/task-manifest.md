# Task Manifest

## task identity

- Task ID: `TASK-PROJECT-ROADMAP`
- Task title: Introduce Project Roadmap
- Task type: documentation-only system strategy update
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
- Latest relevant handoff: `review.md`
- Next required action: validate requested commands, commit, and report result

## freshness

- Last verified: 2026-07-08
- Verified by: `chief_editor`
- Stale if: roadmap source, project lead constraints, canonical ownership map,
  or edited files change before finalization.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `../../ROADMAP.md`
  - `../../../README.md`
  - `../../project-state.md`
- Replaces: no production roadmap file in this repository
- Deprecated/previous versions: old roadmap files folded into
  `../../ideas/master_backlog.md`
- Versions no longer working artifacts: old development roadmap filenames named
  in root `README.md`
- Version conflict state: none
- What to read on restart:
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - `../../ROADMAP.md`
  - root `../../../README.md`
  - `../../project-state.md`
  - `review.md`
  - `final.md`
  - `final_decision.md`
- Old versions read only for: reviewer-governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no for local documentation commit; user requested
  the change explicitly
- Human approval evidence: current user task
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User goal and constraints |
| `task-manifest.md` | yes | required | Current task pointer |
| `orchestration_plan.md` | yes | required | Compact routing contract |
| `status.md` | yes | required | Status and transition history |
| `../../ROADMAP.md` | yes | required | Roadmap candidate under review |
| `../../../README.md` | yes | conditional | Lightweight navigation |
| `../../project-state.md` | yes | conditional | Lightweight state/navigation note |
| `handoff-writing-writer-agent-to-review-agent.md` | yes | conditional | Direct writing-to-review transfer |
| `review.md` | yes | required before finalization | Independent review approved |
| `final.md` | yes | required for compact finalization | Final deliverable pointer |
| `final_decision.md` | yes | required for governance closure | Chief Editor final decision |

## stale or conflicting state

- None known.

## active constraints

- User constraints: documentation only; no redesign; no architecture,
  behavior, lifecycle, role, pipeline, capability registry, review-gate, or
  framework-boundary changes; do not touch `/about`, `diff_intake.md`, legacy
  repository, or `/Users/sa/Documents/codex/redaction`.
- Pipeline constraints: independent review before finalization.
- Client-profile constraints: none.
- Governance constraints: roadmap must remain strategy, not canonical owner.

## open questions

- None.

## next action packet

Minimum restart read set:

- `ai-editorial-office/AGENTS.md` invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- `../../ROADMAP.md`;
- `../../../README.md`;
- `../../project-state.md`;
- `handoff-writing-writer-agent-to-review-agent.md`.

Next action:

- Role: `chief_editor`
- Action: validate requested commands, commit, and deliver results
- Expected output: final response with changed files, validation results, and
  commit hash
- Stop conditions: roadmap becomes operational canon, invents roadmap items,
  drops roadmap items, changes architecture, or touches prohibited files.

## lifecycle notes

- Legacy task folders consulted: no.
- Old artifact versions consulted: no; only consolidated backlog/source note
  was used.
- Safe-to-ignore material: unrelated task folders and untracked `diff_intake.md`.
