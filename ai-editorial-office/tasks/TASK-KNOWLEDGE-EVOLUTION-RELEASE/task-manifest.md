# Task Manifest

## task identity

- Task ID: `TASK-KNOWLEDGE-EVOLUTION-RELEASE`
- Task title: Knowledge Evolution Release
- Task type: system capability release
- Owner/current role: `chief_editor`
- Created: 2026-07-09
- Last updated: 2026-07-09

## current state

- Current status: `finalized`
- Selected pipeline: `research`
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final_decision.md`
- Latest relevant handoff:
  `handoff-release-writer-agent-to-review-agent.md`
- Next required action: run final validation, commit, and deliver release
  summary

## freshness

- Last verified: 2026-07-09
- Verified by: `chief_editor`
- Stale if: governing documents, current release status, capability registry,
  `/about` package shape, validation scripts, or release mission constraints
  change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `brief.md`
  - `orchestration_plan.md`
  - `status.md`
  - `../../research/knowledge_evolution_landscape.md`
  - `../../research/knowledge_evolution_architecture_synthesis.md`
  - implemented canonical integration files listed after synthesis
  - `../../research/knowledge_evolution_release_report.md`
  - `../../releases/S3-R6/release-pack.md`
  - `review.md`
  - `final.md`
  - `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart:
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - latest relevant handoff if present
  - `review.md` if review has started
  - current working artifact
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no before local release candidate commit
- Human approval evidence: user requested autonomous release-candidate work
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Mission scope |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Status history |
| `../../research/knowledge_evolution_landscape.md` | yes | required | Research |
| `../../research/knowledge_evolution_architecture_synthesis.md` | yes | required | Architecture synthesis |
| implemented canonical integration files | yes | conditional | Canonical owner and integration references updated |
| `../../research/knowledge_evolution_release_report.md` | yes | required | Release report |
| `../../releases/S3-R6/release-pack.md` | yes | required | Release pack |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Review handoff |
| `review.md` | yes | required | Independent review |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Governance closure |

## stale or conflicting state

- None known.

## active constraints

- User constraints: complete the full release; do not stop at intermediate
  milestones; do not touch `/Users/sa/Documents/codex/redaction`.
- Architecture constraints: no role, pipeline, lifecycle, review-gate,
  capability-registry, task-object, existing framework-ownership, or `/about`
  memory-boundary redesign.
- Pipeline constraints: source-backed research precedes synthesis and
  implementation; independent review required before final governance.
- Learning constraints: do not turn every task-local observation into system
  policy; canon promotion must stay deliberate, owned, evidenced, and reviewed.
- Client-profile constraints: none.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../BACKLOG.md`;
- `../../project-state.md`;
- `brief.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`.

Next action:

- Role: `chief_editor`
- Action: run final validation, commit, and deliver release summary
- Expected output: final commit hash and user-facing release summary
- Stop conditions: validation fails, staging fails, or release pack becomes
  incomplete.

## lifecycle notes

- Legacy task folders consulted: yes, S3.R4 and S3.R5 release tasks for current
  release-candidate pattern.
- Old artifact versions consulted: no.
- Safe-to-ignore material: none identified.
