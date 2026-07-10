# Task Manifest

## task identity

- Task ID: `TASK-EVALUATION-SIGNALS-RELEASE`
- Task title: Evaluation Signals Release
- Task type: system capability integration release
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research_pipeline.md`
- Pipeline mini-contract: evaluation-signal system release contract in
  `orchestration_plan.md`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Active Domain Knowledge Pack: `none`
- Domain Pack activation reason: no pack is active as task authority; accepted
  packs and their saved use evidence are repository research inputs
- Current working artifact: `final_decision.md`
- Latest relevant handoff:
  `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: re-stage final governance updates, re-run final closure
  checks, create the local Release Candidate commit, and deliver the hash

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: governing documents, S5.R2 mission, S5.R1 acceptance evidence,
  release-pack standard, relevant owners, or validation scripts change.

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
  - `../../research/evaluation_signals_landscape.md`
  - `handoff-research-research-agent-to-chief-editor.md`
  - `../../research/evaluation_signals_architecture_synthesis.md`
  - `handoff-architecture-chief-editor-to-writer-agent.md`
  - canonical implementation named in the architecture synthesis
  - `../../tests/evaluation_signals_smoke_test.md`
  - `../../research/evaluation_signals_release_report.md`
  - `../../releases/S5-R2/release-pack.md`
  - `handoff-release-writer-agent-to-review-agent.md`
  - `review.md`
  - `handoff-review-review-agent-to-final-editor.md`
  - `final.md`
  - `handoff-finalization-final-editor-to-chief-editor.md`
  - `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none; the prior state lag is resolved by the explicit
  Project Lead mission and S5.R1 acceptance commit `fb3b932`
- What to read on restart: `brief.md`, this manifest,
  `orchestration_plan.md`, `status.md`, latest handoff, and current working
  artifact
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: yes, after Release Candidate delivery
- Human approval evidence: S5.R1 accepted and S5.R2 explicitly opened; S5.R2
  acceptance remains pending
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
| `claims_table.md` | yes | required | Claim traceability |
| `../../research/evaluation_signals_landscape.md` | yes | required | Professional landscape |
| `handoff-research-research-agent-to-chief-editor.md` | yes | required | Research delta |
| `../../research/evaluation_signals_architecture_synthesis.md` | yes | required | Architecture decision |
| `handoff-architecture-chief-editor-to-writer-agent.md` | yes | required | Implementation contract |
| canonical implementation | yes | required | Existing-owner changes only |
| `../../tests/evaluation_signals_smoke_test.md` | yes | required | Eight mission scenarios pass |
| `../../research/evaluation_signals_release_report.md` | yes | required | Release evidence |
| `../../releases/S5-R2/release-pack.md` | yes | required | Project Lead review packet |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Complete review delta |
| `review.md` | yes | required | Independent review approved |
| `handoff-review-review-agent-to-final-editor.md` | yes | required | Approved finalization scope |
| `final.md` | yes | required | Controlled final deliverable pointer |
| `handoff-finalization-final-editor-to-chief-editor.md` | yes | required | Finalization delta |
| `final_decision.md` | yes | required | Chief Editor RC governance |

## stale or conflicting state

- `ROADMAP.md` and `project-state.md` still describe S5.R1 in review, while
  `BACKLOG.md`, S5.R1 Release Verdict, commit `fb3b932`, and this explicit
  Project Lead mission establish S5.R1 accepted and S5.R2 open. The user
  instruction resolves authorization; this release must normalize the stale
  state surfaces before review.

## active constraints

- User constraints: finish through Release Candidate without pausing; preserve
  `diff_intake.md`; do not touch the legacy archive.
- Architecture constraints: advisory signals only; no scores, KPIs, rankings,
  dashboards, governance automation, autonomous optimization, automatic state
  changes, new roles, pipelines, lifecycle states, or review gates.
- Evidence constraints: every reusable signal needs evidence pointer, scope,
  interpretation limits, contradiction handling, and a human decision owner.
- State constraints: S5.R2 may move to `Review`, never `Done`, in this mission.

## open questions

- None blocking.

## next action packet

- Role: `chief_editor`
- Action: re-stage governance updates, run final closure validation, create the
  local RC commit, and deliver the hash
- Expected output: validated Release Candidate commit and handback
- Stop conditions: evidence supports only score-based governance or a bounded
  existing-owner mechanism cannot be justified

## lifecycle notes

- Legacy task folders consulted: yes, only S5.R1 and current release artifacts
  for active Stage 5 integration and release standards
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated root `diff_intake.md`
