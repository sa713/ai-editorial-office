# Task Manifest

## task identity

- Task ID: `TASK-PROFESSIONAL-COMMUNICATION-RELEASE`
- Task title: Professional Communication Release
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
- Current working artifact: `../../releases/S3-R5/release-pack.md`
- Latest relevant handoff:
  `handoff-release-writer-agent-to-review-agent.md`
- Next required action: commit release candidate and deliver final summary

## freshness

- Last verified: 2026-07-09
- Verified by: `chief_editor`
- Stale if: governing documents, capability registry, `/about` package shape,
  validation results, or release mission constraints change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `brief.md`
  - `orchestration_plan.md`
  - `status.md`
  - `../../research/professional_communication_landscape.md`
  - `../../research/professional_communication_architecture_synthesis.md`
  - `../../kb/professional_communication.md`
  - `../../research/professional_communication_release_report.md`
  - `../../releases/S3-R5/release-pack.md`
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
  - `handoff-release-writer-agent-to-review-agent.md`
  - `review.md`
  - `final_decision.md`
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
| `../../research/professional_communication_landscape.md` | yes | required | Research |
| `../../research/professional_communication_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `../../kb/professional_communication.md` | yes | conditional | Canonical capability doc |
| `../../research/professional_communication_release_report.md` | yes | required | Release report |
| `../../releases/S3-R5/release-pack.md` | yes | required | Release pack |
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
  capability-registry, task-object, or framework-ownership redesign.
- Pipeline constraints: source-backed research precedes synthesis and
  implementation; independent review required before final governance.
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
- `status.md`;
- `review.md`;
- `final_decision.md`;
- `../../releases/S3-R5/release-pack.md`.

Next action:

- Role: `chief_editor`
- Action: commit release candidate and deliver final summary
- Expected output: committed release candidate and final commit hash
- Stop conditions: failed validation, staging conflict, or architecture
  conflict appears.

## lifecycle notes

- Legacy task folders consulted: yes, `TASK-PROFESSIONAL-ANALYSIS-RELEASE` for
  current release-candidate pattern.
- Old artifact versions consulted: no.
- Safe-to-ignore material: untracked `diff_intake.md`.
