# Task Manifest

Selected pipeline: research

## task identity

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP1`
- Task title: Product Intent Review — Step 1 Capability Specification
- Task type: bounded canonical capability specification
- Owner/current role: `chief_editor`
- Created: 2026-07-29
- Last updated: 2026-07-29

## current state

- Current status: `finalized`
- Selected deliverable: `../../kb/product_intent_review.md`
- Selected deliverable set: ordered set
- Selected primary pipeline or mode: `research_pipeline` with a bounded canonical-specification mini-contract
- Companion mini-contracts: `baseline-report.md`, `specification-report.md`, `implementation-report.md`, and `change-summary.md`
- Risk mode: `standard`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-final-editor-to-chief-editor.md`
- Next required action: await separate explicit authority for any later operationalization; do not start Step 2

## reader outcome state

- Reader outcome material: yes
- Reader Outcome Contract pointer: `orchestration_plan.md`
- Reader Review required: `normal`
- Companion Pass required: yes

## freshness

- Last verified: 2026-07-29
- Verified by: `chief_editor`
- Stale if: Product Intent Review, Professional Analysis, capability-registry, or canonical-ownership contracts change before review

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `brief.md`; `baseline-report.md`; `../../kb/product_intent_review.md`; `specification-report.md`; `implementation-report.md`; `change-summary.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, `status.md`, latest handoff, current task reports, and changed canonical files
- Old versions read only for: Step 0 architecture decision and historical Problem Hypothesis provenance
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
| `brief.md` | yes | required | Exact authorized Step 1 source supplied by the user. |
| `task-manifest.md` | yes | required | Current-state and version pointer. |
| `orchestration_plan.md` | yes | required | Bounded Step 1 execution contract. |
| `status.md` | yes | required | Lifecycle state and history. |
| `handoff-chief-editor-to-research-agent.md` | yes | required | Routing transfer. |
| `research.md` | yes | required | Compact evidence and source-boundary record. |
| `baseline-report.md` | yes | required | Step 1 starting state and scope baseline. |
| `../../kb/product_intent_review.md` | yes | required | Sole full canonical owner of the capability specification. |
| `specification-report.md` | yes | required | Requirement-to-contract traceability. |
| `implementation-report.md` | yes | required | Canonical change and non-change record. |
| `change-summary.md` | yes | required | Scoped diff summary. |
| `review.md` | yes | required | Independent review outcome `approved`. |
| `final_decision.md` | yes | required | Chief Editor closure; Step 2 remains unstarted. |
| `final.md` | yes | required | Compact approved artifact index. |

## stale or conflicting state

- None.

## active constraints

- Perform only authorized Step 1 specification work.
- Do not implement routing, task-object fields, role specs, pipelines, templates, runtime behavior, production behavior, or Step 2.
- Keep `project-state.md` and the Professional Analysis release-candidate status unchanged.
- Use `kb/product_intent_review.md` as the only full owner; other files receive only minimal relationship, registry, or ownership pointers.
- Preserve all unrelated dirty and untracked files.

## open questions

- None blocking. Historical Problem Hypothesis disposition must be decided inside Step 1 without changing its historical task files or current production references.

## next action packet

- Role: `research_agent`
- Action: establish the current canonical baseline, evidence boundary, and exact authorized change surface.
- Expected output: `research.md`, `baseline-report.md`, and a handoff to `writer_agent`.
- Stop conditions: need for a new role, pipeline, lifecycle stage, task status, review outcome, mandatory task artifact, production behavior, or Professional Analysis release decision.

## lifecycle notes

- Step 0 consulted: yes, as the approved architecture decision and baseline.
- Historical Problem Hypothesis proposal consulted: only for explicit disposition; it remains non-canonical evidence.
- Safe-to-ignore material: unrelated task folders, legacy repository content, and every implementation surface reserved for later steps.
