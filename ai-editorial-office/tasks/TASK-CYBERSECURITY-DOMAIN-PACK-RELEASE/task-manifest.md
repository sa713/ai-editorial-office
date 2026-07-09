# Task Manifest

## task identity

- Task ID: `TASK-CYBERSECURITY-DOMAIN-PACK-RELEASE`
- Task title: Cybersecurity Domain Pack Release
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
- Current working artifact:
  `../../releases/S4-R4/release-pack.md`
- Latest relevant handoff:
  `handoff-release-writer-agent-to-review-agent.md`
- Next required action: deliver release candidate summary and commit hash

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: governing documents, active release state, Domain Knowledge Pack
  Standard, adjacent domain packs, source register evidence, validation
  results, or release mission constraints change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `brief.md`
  - `orchestration_plan.md`
  - `status.md`
  - `../../research/cybersecurity_pack_landscape.md`
  - `../../research/cybersecurity_pack_architecture_synthesis.md`
  - `../../kb/cybersecurity_domain_pack.md`
  - `../../research/cybersecurity_pack_release_report.md`
  - `../../releases/S4-R4/release-pack.md`
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
  - latest relevant handoff
  - current working artifact
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no before local release-candidate commit; Project
  Lead review required for accepted release
- Human approval evidence: user requested autonomous release-candidate work
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Mission scope |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Status history |
| `../../research/cybersecurity_pack_landscape.md` | yes | required | Research |
| `../../research/cybersecurity_pack_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `../../kb/cybersecurity_domain_pack.md` | yes | required | Canonical domain context pack |
| `../../research/cybersecurity_pack_release_report.md` | yes | required | Release report and validation |
| `../../releases/S4-R4/release-pack.md` | yes | required | Release readiness |
| `handoff-research-research-agent-to-writer-agent.md` | yes | required | Research-to-production transfer |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Review handoff |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Chief Editor governance closure |

## stale or conflicting state

- None known.

## active constraints

- User constraints: complete the full release; do not stop at intermediate
  milestones; do not touch `/Users/sa/Documents/codex/redaction`.
- Architecture constraints: no new capabilities, roles, frameworks, pipelines,
  lifecycle stages, governance layers, review gates, policy owners, approval
  workflows, or mandatory ordinary task artifacts.
- Domain-pack constraints: follow `kb/domain_knowledge_pack_standard.md` and
  keep the cybersecurity pack as source-backed context.
- Safety constraints: defensive and review-oriented only; no exploit,
  weaponization, bypass, malware, credential theft, stealth, persistence, or
  unauthorized-access instructions.
- Client-profile constraints: none.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../BACKLOG.md`;
- `../../project-state.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- `../../kb/domain_knowledge_pack_standard.md`;
- `../../kb/engineering_review.md`;
- `../../kb/devsecops_domain_pack.md`;
- `../../kb/software_architecture_domain_pack.md`;
- current working artifact.

Next action:

- Role: `chief_editor`
- Action: deliver release-candidate handback and commit hash
- Expected output: S4.R4 release candidate available for Project Lead review
- Stop conditions: source access is insufficient for material claims, safety
  boundary cannot be preserved, adjacent-pack boundary conflict appears, or
  canonical instructions conflict.

## lifecycle notes

- Legacy task folders consulted: yes, release-candidate task pattern from
  prior Stage 3/4 release tasks.
- Old artifact versions consulted: no.
- Safe-to-ignore material: untracked `diff_intake.md`.
