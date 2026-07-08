# Task Manifest

## task identity

- Task ID: `TASK-PROFESSIONAL-ANALYSIS-RELEASE`
- Task title: Professional Analysis Release
- Task type: system capability release
- Owner/current role: `chief_editor`
- Created: 2026-07-08
- Last updated: 2026-07-08

## current state

- Current status: `finalized`
- Selected pipeline: `research`
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `../../research/professional_analysis_release_report.md`
- Latest relevant handoff: `handoff-release-writer-agent-to-review-agent.md`
- Next required action: commit and deliver release summary

## freshness

- Last verified: 2026-07-08
- Verified by: `chief_editor`
- Stale if: governing documents, capability registry, `/about` package shape,
  or mission constraints change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `../../research/professional_analysis_competency_landscape.md`
  - `../../research/professional_analysis_architecture_synthesis.md`
  - `../../kb/professional_analysis.md`
  - `../../research/professional_analysis_release_report.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart:
  - `brief.md`
  - this manifest
  - `orchestration_plan.md`
  - `status.md`
  - current working artifacts listed above
  - `review.md`
  - `final.md`
  - `final_decision.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no before local release candidate commit
- Human approval evidence: user requested complete release candidate
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Mission scope |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Status history |
| `../../research/professional_analysis_competency_landscape.md` | yes | required | Research |
| `../../research/professional_analysis_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `../../kb/professional_analysis.md` | yes | conditional | Canonical capability doc |
| `../../research/professional_analysis_release_report.md` | yes | required | Release report |
| `handoff-release-writer-agent-to-review-agent.md` | yes | conditional | Release handoff |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Final deliverable pointer |
| `final_decision.md` | yes | required | Governance closure |

## stale or conflicting state

- None known.

## active constraints

- User constraints: complete release; no architecture redesign; no new default
  roles, pipelines, lifecycle stages, mandatory artifacts, duplicate framework
  owners, or redaction-path edits.
- Pipeline constraints: research and writing separated where factual support is
  material; independent review required before final governance.
- Client-profile constraints: none.
- Governance constraints: canonical ownership must stay with current owners.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `../../AGENTS.md`;
- `../../ROADMAP.md`;
- `../../BACKLOG.md`;
- `../../project-state.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- current working artifact.

Next action:

- Role: `chief_editor`
- Action: commit and deliver release summary
- Expected output: committed release candidate and final response
- Stop conditions: architecture redesign pressure, unsupported canonical
  changes, or conflict with governing documents.

## lifecycle notes

- Legacy task folders consulted: no.
- Old artifact versions consulted: no.
- Safe-to-ignore material: untracked `diff_intake.md`.
