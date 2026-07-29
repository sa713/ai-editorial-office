# Orchestration Plan

Pipeline: research

## task summary

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP3`
- User goal: integrate Product Intent Review analysis and findings into the existing Editorial Decision Frame, production boundaries, and independent Review Pipeline.
- Requested deliverable: bounded Step 3 implementation, full task pack, canonical diff, regression checks, and independent review.
- Format authority: `explicit`
- Selected deliverable: Product Intent Review decision and review integration
- Selected deliverable set: ordered set
- Audience/channel: AI Editorial Office maintainers; repository canon, roles, pipelines, templates, tests, and task-local reports
- Current active version: baseline and integration designs

## task classification

- Task type: canonical role/pipeline/template and executable test integration.
- Risk mode: `standard`
- Factual sensitivity: authority, ordering, finding/verdict separation, and regressions must be repository-verifiable.
- Human approval likely required: no.
- Rationale: changes cross operational role and review contracts but are bounded, reversible, and testable.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: Step 3 spans analytical collection, Chief Editor decision transfer, two production roles, independent review, finalization preservation, and regressions.
- Forbidden depth shortcuts: documentation-only review claims, mandatory seven-field form in `limited`, product verdict enum, or implicit pipeline/gate/status expansion.

## task need recognition

- Observed request signals: explicit Step 3 authorization, thirty acceptance criteria, ten scenario tests, named role/pipeline/template surfaces, and strict forbidden surfaces.
- Requested deliverable: implementation plus named reports and independent review.
- Format authority: `explicit`
- Recommended deliverable set and outcome-fit reason: respect the named implementation/test/report set; each member supplies distinct design, behavior, or governance evidence.
- One-artifact sufficiency signal: no.
- Likely primary task type: bounded system implementation.
- Material secondary aspects: Architecture Review, Engineering Review, Analytical Reasoning, review contract design, compatibility.
- Likely capabilities and why: Analytical Reasoning, Architecture Review, Engineering Review, Integrity Checking; Professional Analysis remains an open release candidate and is not released by this task.
- Likely Domain Packs and why: none.
- Research/evidence recommendation: repository baseline plus executable scenario and regression checks.
- Risk/consequence recommendation: standard; a defect could either hide a weak product behind polished copy or burden ordinary editing.
- Review recommendation: full scoped independent review inside the existing single gate.
- Ambiguity or missing information: none blocking.
- Decomposition recommendation: baseline/design -> canonical integration -> executable scenarios -> independent review -> closure.
- Confidence and negative evidence: `verified`; explicit prohibitions rule out new roles, pipelines, statuses, gates, outcomes, standalone default artifact, or evidence taxonomy.
- Explicit non-decision: advisory recognition does not activate Product Intent Review.
- Chief Editor decision: proceed with the minimum Step 3 surface.

## product intent review activation

- Task-local Product Intent Review mode: `not_needed`
- Activation basis: this task implements an already explicitly authorized system contract; it does not ask whether an unapproved product/intervention should exist.
- Negative evidence: owner intent, required outcome, scope, boundaries, and acceptance criteria are already explicit; recursive self-review would not change the implementation decision.
- Limited focus: not applicable.
- Evidence depth: repository-verifiable implementation evidence.
- Production consequence: proceed with the authorized bounded implementation.
- Reroute trigger: implementation evidence reveals a conflict with the existing single review gate, role authority, or Step 1/2 canon.

## outcome-first deliverable decision

- Decision: `respect_requested`
- Selected deliverable set:

| Order | Deliverable | Purpose | Dependency | Production priority |
| --- | --- | --- | --- | --- |
| 1 | `baseline-report.md` | Establish current behavior and exact gaps. | independent | 1 |
| 2 | `decision-integration-design.md` | Define analysis-to-production decision semantics. | baseline | 2 |
| 3 | `review-integration-design.md` | Define independent challenge and outcome separation. | baseline and decision design | 3 |
| 4 | canonical role/pipeline/template/test changes | Implement Step 3. | both designs | 4 |
| 5 | `implementation-report.md` and `change-summary.md` | Prove behavior, validation, and scope. | implementation | 5 |

- Member removal check: removing any member loses baseline, decision semantics, independent-review semantics, executable behavior, or closure evidence.
- Missing companion check: none.
- Explicit-intent preservation note: no Step 4 or default standalone Product Intent Review report is added.

## selected pipeline

- Primary pipeline or mode: `research_pipeline`.
- Companion mini-contract: `writer_agent` with implementation capabilities updates the authorized canon/roles/pipelines/templates/tests and cannot review its own work.
- Review target: `review_agent` with Architecture and Engineering Review checks semantics, executable behavior, compatibility, and forbidden surfaces.
- Pipeline exception: code/test implementation is a bounded companion after research/design; no new pipeline is created.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Selected deliverable set | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Production may start: yes, after both designs.
- Scope boundary: only files with observed contract gaps plus exact `/about` mirrors when mapped surfaces change.

## editorial decision frame

- Chosen editorial route: extend existing roles, research/review pipelines, planning frame, and conditional templates; use `/kb/product_intent_review.md` as sole semantic owner.
- Why this route serves the outcome: it makes `limited/full` executable and independently reviewable without adding architecture.
- Alternatives considered:
  - New Product Reviewer or pipeline — rejected because it violates authority and duplicates the existing gate.
  - Mandatory task-local Product Intent Review report — rejected because adaptive output and compact-path semantics already exist.
  - Review-only documentation update — rejected because production and scenario behavior must be executable and regression-protected.
- Writer/UX Writer contract for implementation:
  - Result type: bounded canonical/test diff and reports.
  - Scope boundary: Step 3 only.
  - Must include: analysis ownership, consequence, compact product-intent frame block, production boundary, independent review, minimum validation, reroute.
  - Must not include: new role/pipeline/stage/gate/status/outcome/artifact default or Step 4.
- Review focus: finding/verdict separation, product-first ordering, owner authority, `limited` proportionality, `full` completeness, no-build approval case, and regressions.
- Reroute triggers: any need to alter lifecycle/state/outcome architecture or to release Professional Analysis.

## required roles

| Stage | Role | Responsibility |
| --- | --- | --- |
| Intake/routing | `chief_editor` | Scope, mode decision, route, and governance. |
| Research/design | `research_agent` | Baseline and integration designs. |
| Implementation | `writer_agent` with implementation capabilities | Canon, roles, pipelines, templates, tests, reports. |
| Review | `review_agent` with Architecture/Engineering Review | Independent acceptance and negative-scope check. |
| Finalization | `final_editor` | Preserve approved result and build final index only after approval. |
| Closure | `chief_editor` | Finalize Step 3 without starting Step 4. |

## required evidence and checks

- Step 1 canonical owner and Step 2 final routing behavior.
- Current role, pipeline, planning, challenge, template, and test contracts.
- Lifecycle validation and validator smoke suite.
- New decision/review scenarios plus routing, Task Need Recognition, generator, Professional Analysis, challenge, reader quality, outcome-first selection, review outcome, restart, compact path, canonical link, `/about` parity, forbidden-surface, and scoped-diff checks.

## stage exit criteria

- Research: current contract and exact gaps are explicit.
- Planning: decision and review integration designs preserve all forbidden surfaces.
- Implementation: observable contracts and ten executable scenarios are complete.
- Review: all thirty Step 3 criteria pass or bounded repairs are requested.
- Closure: approved Step 3 is finalized; Step 4 remains unstarted.
