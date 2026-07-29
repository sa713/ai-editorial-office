# Task Manifest

Selected pipeline: research

## task identity

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP0`
- Task title: Product Intent Review — Step 0 Architecture Audit
- Task type: repository architecture research and decision support
- Owner/current role: `chief_editor`
- Created: 2026-07-29
- Last updated: 2026-07-29

## current state

- Current status: `finalized`
- Selected deliverable: `baseline-report.md`
- Selected deliverable set: ordered set
- Selected primary pipeline or mode: `research_pipeline` with Architecture Review capability and a bounded three-report output contract
- Companion mini-contracts: `product-intent-responsibility-map.md` and `architecture-decision.md`
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: final.md
- Latest relevant handoff: `handoff-review-agent-to-chief-editor.md`
- Next required action: await an explicit user/Project Lead decision before any Step 1 work

## reader outcome state

- Reader outcome material: yes
- Reader Outcome Contract pointer: `orchestration_plan.md`
- Reader Review required: `normal`
- Companion Pass required: yes

## freshness

- Last verified: 2026-07-29
- Verified by: `chief_editor`
- Stale if: relevant canonical architecture changes before review

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `brief.md`; `baseline-report.md`; `product-intent-responsibility-map.md`; `architecture-decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, `status.md`, latest handoff, and the current report set
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: no
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Exact canonical source of requirements supplied by the user. |
| `task-manifest.md` | yes | required | Current-state and version pointer. |
| `orchestration_plan.md` | yes | required | Step 0 execution contract. |
| `status.md` | yes | required | Lifecycle state and history. |
| `handoff-chief-editor-to-research-agent.md` | yes | required | Routing transfer. |
| `research.md` | yes | required | Compact evidence index for Research Pipeline compliance. |
| `baseline-report.md` | yes | required | Current architecture baseline and partial coverage. |
| `product-intent-responsibility-map.md` | yes | required | Existing, partial, gap, conflict, and ownership map. |
| `architecture-decision.md` | yes | required | Minimal extension decision; no implementation. |
| `review.md` | yes | required | Current outcome `approved` after bounded F1/F2 re-review. |
| `final.md` | yes | required | Compact index of the three approved requested deliverables; no new analysis. |
| `final_decision.md` | yes | required | Step 0 governance closure; no Step 1 authority. |

## stale or conflicting state

- None.

## active constraints

- User constraints: perform only Step 0; create exactly the three requested reports; do not implement Product Intent Review; do not proceed to Step 1; do not change production logic; do not touch the legacy repository.
- Pipeline constraints: preserve research/production/review separation and mandatory independent review.
- Client-profile constraints: none.
- Governance constraints: treat `brief.md` as the initiative source of truth; use existing canonical owners; avoid new roles, stages, gates, or duplicated policy.

## open questions

- None blocking Step 0. Any uncertainty about later implementation must be recorded as a Step 0 open question, not resolved by implementation.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `handoff-chief-editor-to-research-agent.md`;
- current report set;
- directly relevant canonical KB, role, pipeline, template, test, and project-state files named in the plan.

Next action:

- Role: user / initiative owner
- Action: decide whether and how to authorize Step 1, including the Professional Analysis governance dependency.
- Expected output: explicit future instruction or no action.
- Stop conditions: any instruction conflict, pressure to implement the capability, or missing canonical owner that makes a recommendation unsafe.

## lifecycle notes

- Legacy task folders consulted: no; legacy folders are excluded and not needed.
- Old artifact versions consulted: no; no version comparison is required.
- Safe-to-ignore material: unrelated untracked task folders and all implementation work outside Product Intent Review Step 0.
