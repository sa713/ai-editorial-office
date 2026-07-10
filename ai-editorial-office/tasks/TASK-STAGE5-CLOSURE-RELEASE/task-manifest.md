# Task Manifest

## task identity

- Task ID: `TASK-STAGE5-CLOSURE-RELEASE`
- Task title: Stage 5 strategic acceptance closure
- Task type: project governance and accepted-state synchronization
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research_pipeline.md`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: final validation, explicit staging, staged-diff check, and local commit

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: production scope, Project Lead decision, Stage 5 release state, S3.R4 state, or validation result changes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: yes
- Human approval evidence: current user statement `stage 5 accepted`
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Project Lead decision and scope |
| `task-manifest.md` | yes | required | current task state |
| `orchestration_plan.md` | yes | required | execution contract |
| `status.md` | yes | required | transition history |
| `research.md` | yes | required | repository evidence synthesis |
| `sources.md` | yes | required | source register |
| `facts.md` | yes | required | accepted-state facts |
| `claims_table.md` | yes | required | downstream claim controls |
| `handoff-research-research-agent-to-writer-agent.md` | yes | required | research delta |
| `handoff-writing-writer-agent-to-review-agent.md` | yes | required | patch delta |
| `review.md` | yes | required | independent verdict `approved` |
| `final.md` | yes | required | accepted closure summary |
| `handoff-finalization-final-editor-to-chief-editor.md` | yes | required | finalization delta |
| `final_decision.md` | yes | required | final governance decision |

## stale or conflicting state

- Before the patch, state files correctly recorded Stage 5 closure as pending;
  the current Project Lead decision supersedes that pending state.

## active constraints

- User constraints: record Stage 5 acceptance only.
- Pipeline constraints: repository evidence only; no external research needed.
- Client-profile constraints: not applicable.
- Governance constraints: preserve architecture, S3.R4 state, future-stage
  non-activation, review independence, and Project Lead authority.

## open questions

- None for Stage 5 closure. Project v1.0 and S3.R4 remain separate decisions.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `handoff-finalization-final-editor-to-chief-editor.md`;
- `review.md`;
- `final.md`;
- production diff.

Next action:

- Role: `chief_editor`
- Action: validate final state, stage authorized scope, check staged diff, commit
- Expected output: local commit and user handback
- Stop conditions: unauthorized staged path, future-stage activation, S3.R4
  disposition, memory mismatch, or validation failure

## lifecycle notes

- Legacy task folders consulted: yes; `TASK-STAGE4-CLOSURE-RELEASE` only as
  evidence of the established stage-closure pattern.
- Old artifact versions consulted: no.
- Safe-to-ignore material: unrelated `diff_intake.md` and legacy archive.
