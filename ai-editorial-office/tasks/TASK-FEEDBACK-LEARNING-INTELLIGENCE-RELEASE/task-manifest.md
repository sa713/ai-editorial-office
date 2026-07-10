# Task Manifest

## task identity

- Task ID: `TASK-FEEDBACK-LEARNING-INTELLIGENCE-RELEASE`
- Task title: Feedback and Learning Intelligence Release
- Task type: system capability integration release
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research_pipeline.md`
- Pipeline mini-contract: system release integration contract in
  `orchestration_plan.md`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Active Domain Knowledge Pack: `none`
- Domain Pack activation reason: no domain pack is needed to govern this
  repository-documentation release; historical pack-use evidence is research
  input, not task activation
- Current working artifact: `final_decision.md`
- Latest relevant handoff:
  `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: create the local Release Candidate commit and deliver
  the package and commit hash for Project Lead review

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: governing documents, S5.R1 mission constraints, feedback or
  learning owners, Domain Pack standard, release-pack standard, or validation
  scripts change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact set:
  - `brief.md`
  - `task-manifest.md`
  - `orchestration_plan.md`
  - `status.md`
  - `sources.md`
  - `facts.md`
  - `claims_table.md`
  - `../../research/feedback_learning_intelligence_landscape.md`
  - `../../research/feedback_learning_intelligence_architecture_synthesis.md`
  - `handoff-research-research-agent-to-chief-editor.md`
  - `handoff-architecture-chief-editor-to-writer-agent.md`
  - canonical integration patches named in the architecture synthesis
  - `../../tests/feedback_learning_intelligence_smoke_test.md`
  - `../../research/feedback_learning_intelligence_release_report.md`
  - `../../releases/S5-R1/release-pack.md`
  - `handoff-release-writer-agent-to-review-agent.md`
  - `review.md`
  - `final.md`
  - `handoff-finalization-final-editor-to-chief-editor.md`
  - `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest,
  `orchestration_plan.md`, `status.md`, latest handoff if present, and current
  working artifact
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: yes, after release-candidate delivery
- Human approval evidence: pending Project Lead architectural review
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Mission contract |
| `task-manifest.md` | yes | required | Current state |
| `orchestration_plan.md` | yes | required | Execution contract |
| `status.md` | yes | required | Lifecycle history |
| `sources.md` | yes | required | High-governance source register |
| `facts.md` | yes | required | Research findings |
| `claims_table.md` | yes | required | Claim-level traceability |
| `../../research/feedback_learning_intelligence_landscape.md` | yes | required | Research landscape |
| `../../research/feedback_learning_intelligence_architecture_synthesis.md` | yes | required | Architecture decision |
| `handoff-research-research-agent-to-chief-editor.md` | yes | required | Research delta |
| `handoff-architecture-chief-editor-to-writer-agent.md` | yes | required | Implementation contract |
| canonical integration patches | yes | conditional | Existing owners only |
| `../../tests/feedback_learning_intelligence_smoke_test.md` | yes | required | All nine mission cases pass |
| `../../research/feedback_learning_intelligence_release_report.md` | yes | required | Release evidence |
| `../../releases/S5-R1/release-pack.md` | yes | required | Project Lead review packet |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Review delta and scope |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Final deliverable pointer |
| `handoff-finalization-final-editor-to-chief-editor.md` | yes | required | Finalization delta |
| `final_decision.md` | yes | required | Chief Editor RC governance |

## stale or conflicting state

- None known. The current mission is the explicit Project Lead instruction
  required to open Stage 5 and S5.R1.

## active constraints

- User constraints: finish the release candidate, do not stop at intermediate
  milestones, do not push or record acceptance, do not start S5.R2, do not
  touch the excluded archive or `diff_intake.md`.
- Architecture constraints: no new roles, pipelines, lifecycle stages, review
  gates, learning stores, feedback taxonomies, automatic promotion, or
  mandatory retrospectives.
- Evidence constraints: reusable learning must be traceable, scoped, reviewed,
  owner-routed, and rejectable or deferrable.
- State constraints: S5.R1 moves to `Review` only after the complete release
  candidate exists; never to `Done` in this mission.

## open questions

- None blocking.

## next action packet

- Role: `chief_editor`
- Action: create one local commit from the validated authorized stage and
  deliver the Release Candidate package and commit hash
- Expected output: one local commit and user-facing handback
- Stop conditions: authoritative evidence contradicts the mission boundaries,
  or a bounded integration cannot be made through existing owners

## lifecycle notes

- Legacy task folders consulted: yes, only S3.R6 and recent release tasks for
  the current release-candidate and release-pack contract
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated root `diff_intake.md`
