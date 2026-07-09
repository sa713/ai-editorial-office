# Task Manifest

## task identity

- Task ID: `TASK-DEVSECOPS-DOMAIN-PACK-RELEASE`
- Task title: DevSecOps Domain Pack Release
- Task type: domain knowledge pack release
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Candidate domain pack: `DevSecOps`
- Candidate pack status: `release candidate`
- Current working artifact: `final_decision.md`
- Latest relevant handoff:
  `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: commit and hand back to user.

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: `AGENTS.md`, `ROADMAP.md`, `BACKLOG.md`, `project-state.md`,
  `kb/domain_knowledge_pack_standard.md`, `kb/engineering_review.md`,
  `kb/software_architecture_domain_pack.md`, release-pack standard,
  validation scripts, or `/about` memory rules change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `brief.md`
  - `task-manifest.md`
  - `orchestration_plan.md`
  - `status.md`
  - `../../research/devsecops_pack_landscape.md`
  - `../../research/devsecops_pack_architecture_synthesis.md`
  - `../../kb/devsecops_domain_pack.md`
  - `../../research/devsecops_pack_release_report.md`
  - `../../releases/S4-R3/release-pack.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart:
  - `../../AGENTS.md`
  - `../../ROADMAP.md`
  - `../../BACKLOG.md`
  - `../../project-state.md`
  - `../../kb/domain_knowledge_pack_standard.md`
  - `../../kb/engineering_review.md`
  - `../../kb/software_architecture_domain_pack.md`
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - latest relevant handoff if present
  - current working artifact
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: pending `review.md`
- Review outcome: pending
- Compact finalization shape allowed: no
- Human approval required: no before local release-candidate preparation
- Human approval evidence: user requested autonomous work until release
  candidate; Project Lead review remains post-delivery.
- Final decision artifact: pending `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Release mission scope |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Status history |
| `../../research/devsecops_pack_landscape.md` | yes | required | Research |
| `../../research/devsecops_pack_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `../../kb/devsecops_domain_pack.md` | yes | required | Canonical candidate pack |
| `../../research/devsecops_pack_release_report.md` | yes | required | Release report and scenario validation |
| `../../releases/S4-R3/release-pack.md` | yes | required | Release pack |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Chief Editor governance closure |

## active constraints

- User constraints: complete the whole release; do not stop at intermediate
  milestones; do not touch `/Users/sa/Documents/codex/redaction`.
- Architecture constraints: no new roles, capabilities, frameworks, pipelines,
  lifecycle stages, review gates, policy owners, capability owners, client
  profiles, task status models, or mandatory ordinary task artifacts.
- Pack constraints: follow `kb/domain_knowledge_pack_standard.md`; pack is
  source-backed context only.
- Integration constraint: support Engineering Review without duplicating
  Engineering Review ownership.
- Source constraints: prefer primary or authoritative sources; mark confidence
  limits and stale-if triggers.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../BACKLOG.md`;
- `../../project-state.md`;
- `../../kb/domain_knowledge_pack_standard.md`;
- `../../kb/engineering_review.md`;
- `brief.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- current working artifact.

Next action:

- Role: `chief_editor`
- Action: commit and hand back to user.
- Expected output: final command validation results, final release commit hash,
  and user-facing delivery summary.
- Stop conditions: source evidence too weak for durable pack guidance,
  architecture conflict requiring a forbidden system change, or inability to
  keep the pack bounded as context.

## lifecycle notes

- Legacy task folders consulted: yes, S4.R2 release for release-candidate
  artifact pattern only.
- Safe-to-ignore material: pre-existing untracked `diff_intake.md`.
