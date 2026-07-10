# Task Manifest

## task identity

- Task ID: `TASK-STAGE4-CLOSURE-RELEASE`
- Task title: Stage 4 Closure Release
- Task type: project-state synchronization release
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research_pipeline.md`
- Pipeline mini-contract: state synchronization rules in `orchestration_plan.md`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: finalized closure packet and approved repository diff
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: stage the authorized scope, run cached validation, commit, and push to GitHub

## freshness

- Last verified: 2026-07-10
- Verified by: `chief_editor`
- Stale if: repository state changes, Project Lead opens Stage 5, or any Stage 4 acceptance verdict changes

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact set: `brief.md`, `orchestration_plan.md`, `status.md`, `research.md`, `review.md`, `final.md`, `final_decision.md`, and current handoffs
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, `status.md`, latest handoff, current diff
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved` after bounded repair and re-review
- Compact finalization shape allowed: no
- Human approval required: yes, already supplied by the Project Lead in the user mission for closure, commit, and push
- Human approval evidence: current user mission
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Closure scope and constraints |
| `task-manifest.md` | yes | required | Current task state |
| `orchestration_plan.md` | yes | required | State-only execution contract |
| `status.md` | yes | required | Lifecycle history |
| `research.md` | yes | required | Current-state inventory |
| `review.md` | yes | required | Approved after bounded repair and re-review |
| `final.md` | yes | required | Compact closure summary after approved review |
| `final_decision.md` | yes | required | Chief Editor closure decision |

## stale or conflicting state

- None. The accepted Stage 4 state has been synchronized and independently
  reviewed.

## active constraints

- User constraints: state wording only; no functionality or architecture change; do not open Stage 5; push final commit
- Pipeline constraints: independent review required before governance closure
- Client-profile constraints: not applicable
- Governance constraints: preserve historical RC evidence and modify only current state-bearing surfaces

## open questions

- None. The source boundary and accepted target state are explicit.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- `brief.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- current `research.md` or latest handoff;
- current diff.

Next action:

- Role: `chief_editor`
- Action: stage only the authorized scope, validate, commit, and push
- Expected output: final commit hash and successful GitHub push
- Stop conditions: any requested edit would change technical content, architecture, roles, capabilities, pipelines, lifecycle, or historical evidence

## lifecycle notes

- Legacy task folders consulted: yes, only as evidence of historical RC and acceptance boundaries
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated untracked `diff_intake.md`; historical release-task narratives after state classification
