# Task Manifest

Selected pipeline: research

## task identity

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP5`
- Task title: Product Intent Review — Step 5 Minimum Product Validation
- Task type: bounded canonical and executable validation-contract integration
- Owner/current role: `chief_editor`
- Created: 2026-07-29
- Last updated: 2026-07-29

## current state

- Current status: `finalized`
- Selected deliverable: reliable Minimum Product Validation inside Product Intent Review
- Selected deliverable set: validation contract, method map, bounded canonical/role/profile integration, executable regressions, and required closure reports
- Selected primary pipeline or mode: `research_pipeline`
- Companion mini-contracts: bounded system implementation with Architecture and Engineering Review
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-final-editor-to-chief-editor.md`
- Next required action: await separate explicit authority; do not start Step 6

## freshness

- Last verified: 2026-07-29
- Verified by: `chief_editor`
- Stale if: Product Intent Review Step 1–4 canon, validation checker, roles, or deliverable profiles change

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `brief.md`; `baseline-report.md`; `validation-contract-design.md`; `validation-method-map.md`; `implementation-report.md`; `canonical-diff.md`; `change-summary.md`; `review.md`; `final.md`; `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: this manifest, `brief.md`, `orchestration_plan.md`, `status.md`, latest handoff, both design artifacts, current scoped diff, and `/kb/product_intent_review.md`
- Old versions read only for: finalized Step 0–4 architecture, routing, analysis, output, and acceptance evidence
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Human approval required: no
- Human approval evidence: Step 5 brief status is `Authorized`
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Requirement | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Authorized Step 5 scope and constraints. |
| `task-manifest.md` | yes | required | Restart anchor. |
| `orchestration_plan.md` | yes | required | Bounded execution contract. |
| `status.md` | yes | required | Lifecycle history. |
| `baseline-report.md` | yes | required | Step 4 validation baseline and observed gaps. |
| `validation-contract-design.md` | yes | required | Decision and field semantics. |
| `validation-method-map.md` | yes | required | Bounded hypothesis/method/signal map. |
| `implementation-report.md` | yes | required | Implemented behavior and check evidence. |
| `canonical-diff.md` | yes | requested | Semantic diff over finalized Step 4. |
| `change-summary.md` | yes | required | Scoped surface and explicit non-changes. |
| `review.md` | yes | required | Independent review; 32/32 pass. |
| `final.md` | yes | required | Approved user-facing index. |
| `final_decision.md` | yes | required | Governance closure; Step 6 remains unstarted. |

## active constraints

- Strengthen the existing minimum hypothesis validation; do not add a second capability.
- Preserve routing, modes, finding/verdict separation, role ownership, lifecycle, deliverable selection, and release state.
- Keep examples bounded in fixtures unless a distinct canonical consumer is proven.
- Do not create a role, pipeline, stage, gate, status, outcome, required report, evidence taxonomy, metric library, automatic pilot/A/B test, or Step 6 surface.
- Preserve unrelated dirty and untracked files, including finalized Step 0–4 work.

## next action packet

- Role: none
- Action: await separate explicit authority.
- Expected output: none.
- Stop conditions: do not start Step 6 or alter release status without a new authorized task.
- Stop conditions: any need to change routing/modes, create architecture, or alter release status.
