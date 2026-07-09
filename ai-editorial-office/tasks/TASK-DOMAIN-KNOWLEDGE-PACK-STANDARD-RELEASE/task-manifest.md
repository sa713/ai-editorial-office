# Task Manifest

## task identity

- Task ID: `TASK-DOMAIN-KNOWLEDGE-PACK-STANDARD-RELEASE`
- Task title: Domain Knowledge Pack Standard Release
- Task type: system standard release
- Owner/current role: `chief_editor`
- Created: 2026-07-09
- Last updated: 2026-07-09

## current state

- Current status: `finalized`
- Selected pipeline: `research`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final_decision.md`
- Latest relevant handoff:
  `handoff-release-writer-agent-to-review-agent.md`
- Next required action: final validation and deliver release summary

## freshness

- Last verified: 2026-07-09
- Verified by: `chief_editor`
- Stale if: `AGENTS.md`, `ROADMAP.md`, `BACKLOG.md`, `project-state.md`,
  `research/stage3_strategic_review.md`, release-pack standard, validation
  scripts, or `/about` memory package rules change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `brief.md`
  - `task-manifest.md`
  - `orchestration_plan.md`
  - `status.md`
  - `../../research/domain_knowledge_pack_standard_landscape.md`
  - `../../research/domain_knowledge_pack_standard_architecture_synthesis.md`
  - `../../kb/domain_knowledge_pack_standard.md`
  - `../../research/domain_knowledge_pack_standard_release_report.md`
  - `../../releases/S4-R1/release-pack.md`
  - `review.md`
  - `final.md`
  - `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart:
  - `../../AGENTS.md`
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
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no before local release-candidate preparation
- Human approval evidence: user requested autonomous work until release
  candidate; Project Lead review remains post-delivery.
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Release mission scope |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Status history |
| `../../research/domain_knowledge_pack_standard_landscape.md` | yes | required | Research |
| `../../research/domain_knowledge_pack_standard_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `../../kb/domain_knowledge_pack_standard.md` | yes | required | Canonical standard |
| canonical integration files | yes | conditional | Discoverability and review integration |
| `/about` files | yes | conditional | Synced because copied canonical files and compact summaries changed |
| `../../research/domain_knowledge_pack_standard_release_report.md` | yes | required | Release report |
| `../../releases/S4-R1/release-pack.md` | yes | required | Release pack |
| `../../tests/domain_knowledge_pack_standard_smoke_test.md` | yes | conditional | Manual scenario validation |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Writing-to-review transfer |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Chief Editor governance closure |

## stale or conflicting state

- Resolved during release implementation: `project-state.md`, `ROADMAP.md`,
  and `BACKLOG.md` now identify Stage 4 Domain Expertise and S4.R1 as the
  current release candidate for Project Lead review.

## active constraints

- User constraints: complete the entire release; do not stop at intermediate
  milestones; do not touch `/Users/sa/Documents/codex/redaction`.
- Architecture constraints: no new roles, pipelines, lifecycle stages, review
  gates, mandatory ordinary task artifacts, hidden policy owners, duplicate
  capability owners, or `/about` canon promotion.
- Source constraints: use primary or authoritative sources where possible and
  record evidence limits.
- Release constraints: release candidate requires research, synthesis,
  standard, validation, `/about` disposition, release report, release pack,
  independent review, final governance decision.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../BACKLOG.md`;
- `../../project-state.md`;
- `../../research/stage3_strategic_review.md`;
- `brief.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- `../../kb/domain_knowledge_pack_standard.md`;
- `../../research/domain_knowledge_pack_standard_release_report.md`;
- `../../releases/S4-R1/release-pack.md`;
- `handoff-release-writer-agent-to-review-agent.md`.

Next action:

- Role: `chief_editor`
- Action: run final validation and deliver release summary for Project Lead
  architectural review.
- Expected output: release candidate ready summary.
- Stop conditions: source conflict that would require forbidden architecture
  change, inability to cite evidence, or instruction conflict.

## lifecycle notes

- Legacy task folders consulted: yes, `TASK-KNOWLEDGE-EVOLUTION-RELEASE` for
  release-candidate artifact pattern only.
- Old artifact versions consulted: no.
- Safe-to-ignore material: pre-existing untracked `diff_intake.md`.
