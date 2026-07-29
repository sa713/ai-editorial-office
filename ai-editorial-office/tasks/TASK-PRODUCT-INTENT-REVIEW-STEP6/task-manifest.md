# Task Manifest

Selected pipeline: research

## task identity

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP6`
- Task title: Product Intent Review — Step 6 Evaluation Suite and Calibration
- Task type: bounded end-to-end evaluation design and implementation
- Owner/current role: `chief_editor`
- Created: 2026-07-29
- Last updated: 2026-07-29

## current state

- Current status: `finalized`
- Selected deliverable: Product Intent Review end-to-end evaluation suite
- Selected deliverable set: evaluation design, rubric, 30+ case suite, hybrid runner, coverage/baseline/defect/repair reports, review, and closure
- Selected primary pipeline or mode: `research_pipeline`
- Companion mini-contracts: bounded evaluation implementation with Architecture and Engineering Review
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-final-editor-to-chief-editor.md`
- Next required action: await separate explicit authority; do not start Step 7

## freshness

- Last verified: 2026-07-29
- Verified by: `chief_editor`
- Stale if: Product Intent Review Step 1–5 contracts, fixtures, routing, decision/review, output, or validation checkers change

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `final.md`; `review.md`; `final_decision.md`; `brief.md`; `baseline-report.md`; `evaluation-design.md`; `evaluation-rubric.md`; `case-catalogue.md`; `coverage-report.md`; `baseline-comparison.md`; `evaluation-report.md`; `defect-log.md`; `repair-loop-report.md`; `implementation-report.md`; `canonical-diff.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: this manifest, `brief.md`, `orchestration_plan.md`, `status.md`, latest handoff, current evaluation artifacts, and the suite fixture/runner
- Old versions read only for: finalized Step 0–5 contracts and documented historical baseline
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Human approval required: no
- Human approval evidence: Step 6 brief status is `Authorized`
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Requirement | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Authorized Step 6 scope. |
| `task-manifest.md` | yes | required | Restart anchor. |
| `orchestration_plan.md` | yes | required | Evaluation-first execution contract. |
| `status.md` | yes | required | Lifecycle history. |
| `baseline-report.md` | yes | required | Step 1–5 test and runtime baseline. |
| `evaluation-design.md` | yes | required | Hybrid architecture and schema. |
| `evaluation-rubric.md` | yes | required | Product-judgment scale and failure conditions. |
| `case-catalogue.md` | yes | required | Human-readable suite index. |
| `coverage-report.md` | yes | required | Coverage and mandatory metrics. |
| `baseline-comparison.md` | yes | required | Historical/current/expected comparison. |
| `evaluation-report.md` | yes | required | Evaluation outcomes and interpretation. |
| `defect-log.md` | yes | required | Zero confirmed production defects. |
| `repair-loop-report.md` | yes | required | Zero production repair loops. |
| `implementation-report.md` | yes | required | Evaluation assets and checks. |
| `canonical-diff.md` | yes | required | Explicit no-production-diff record. |
| `review.md` | yes | required | Independent review; 34/34 pass. |
| `final.md` | yes | required | Approved summary/index. |
| `final_decision.md` | yes | required | Governance closure. |

## active constraints

- Evaluate current behavior before production changes.
- Do not change expected behavior to hide a failing case.
- Keep automated contract checks separate from manual product judgment.
- Do not reduce judgment to string matching or one aggregate score.
- Production repair requires reproducible defect evidence and the minimum owner-local change.
- Preserve Step 1–5 contracts, unrelated worktree changes, Professional Analysis status, and release state.
- Do not create a role, pipeline, stage, gate, status, outcome, deliverable, mode, or Step 7 surface.

## next action packet

- Role: none
- Action: await separate explicit authority for later work.
- Expected output: none.
- Stop conditions: do not start Step 7 or alter production without new authority.
