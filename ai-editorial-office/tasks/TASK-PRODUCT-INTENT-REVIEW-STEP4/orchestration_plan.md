# Orchestration Plan

Pipeline: research

## task summary

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP4`
- User goal: make Product Intent Review results compact, decision-ready, prioritized, adaptive to `limited/full`, and integrated into existing deliverables.
- Requested deliverable: bounded Step 4 implementation, full task pack, canonical diff, deliverable-fit analysis, regressions, and independent review.
- Format authority: `explicit`
- Selected deliverable: Product Intent Review adaptive output integration
- Selected deliverable set: ordered set
- Audience/channel: AI Editorial Office maintainers; repository canon, deliverable profiles, roles, templates, tests, and task-local reports
- Current active version: baseline and output/deliverable designs

## task classification

- Task type: canonical communication/deliverable-profile and executable output-contract integration.
- Risk mode: `standard`
- Factual sensitivity: reader order, directness, uncertainty, profile choice, negative-scope, and regressions must be repository-verifiable.
- Human approval likely required: no.
- Rationale: changes affect user-facing result shape but not routing, analysis authority, lifecycle, or release state.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: Step 4 crosses the Product Intent owner, three deliverable profiles, Professional Communication, four roles, conditional templates, and twelve output scenarios.
- Forbidden shortcuts: a universal fixed report, output length based on source size, new profile by naming symmetry, or internal architecture exposed as user-facing content.

## task need recognition

- Observed request signals: explicit Step 4 authorization, four reader jobs, outcome-first profile rules, `limited/full` output semantics, twelve cases, and strict forbidden surfaces.
- Requested deliverable: implementation plus named designs/reports and independent review.
- Format authority: `explicit`
- Recommended deliverable set and outcome-fit reason: respect the named design/implementation/test/report set; each member has a distinct governance or regression role.
- One-artifact sufficiency signal: no.
- Likely primary task type: bounded system implementation.
- Material secondary aspects: Professional Communication, Deliverable Knowledge, Reader-Centered Quality, Architecture Review, Engineering Review.
- Likely capabilities and why: Professional Communication, Analytical Reasoning, Architecture Review, Engineering Review, Integrity Checking; Professional Analysis stays unreleased.
- Likely Domain Packs and why: none.
- Research/evidence recommendation: repository baseline, profile comparison, and executable output-shape regressions.
- Risk/consequence recommendation: standard; poor output can bury the product decision or create unnecessary artifact/profile growth.
- Review recommendation: full scoped review inside the existing gate.
- Ambiguity or missing information: no blocker; existing profiles are sufficient unless tests disconfirm.
- Decomposition recommendation: baseline/profile fit -> adaptive contract -> canonical integration -> executable scenarios -> independent review -> closure.
- Confidence and negative evidence: `verified`; report/research-report/decision-memo cover the reader jobs and no stable fourth job requires a new profile.
- Explicit non-decision: deliverable recommendation does not select or produce an artifact.
- Chief Editor decision: reuse existing profiles and implement Step 4 without a new profile.

## product intent review activation

- Task-local Product Intent Review mode: `not_needed`
- Activation basis: this task implements an explicitly authorized output contract; it does not ask whether an unapproved product/intervention should exist.
- Negative evidence: intent, reader jobs, scope, constraints, and acceptance criteria are explicit; recursive self-review cannot change the authorized implementation.
- Production consequence: `Proceed`.
- Reconsideration trigger: profile tests reveal a stable reader job that report, research report, decision memo, or embedded block cannot express without distortion.

## outcome-first deliverable decision

- Decision: `respect_requested`
- Selected deliverable set:

| Order | Deliverable | Purpose | Dependency | Production priority |
| --- | --- | --- | --- | --- |
| 1 | `baseline-report.md` | Establish current output/profile gaps. | independent | 1 |
| 2 | `deliverable-fit-analysis.md` | Decide whether existing profiles suffice. | baseline | 2 |
| 3 | `output-contract-design.md` | Define adaptive reader-facing semantics. | baseline and fit decision | 3 |
| 4 | canonical/profile/role/template/test changes | Implement Step 4. | both designs | 4 |
| 5 | `implementation-report.md`, `canonical-diff.md`, `change-summary.md` | Prove behavior, validation, and scope. | implementation | 5 |

- Member removal check: removing any member loses baseline, anti-proliferation evidence, output semantics, executable behavior, or closure evidence.
- Missing companion check: none.
- Explicit-intent preservation note: no Product Intent Review profile/report default or Step 5 artifact is added.

## selected pipeline

- Primary pipeline or mode: `research_pipeline`.
- Companion mini-contract: `writer_agent` with implementation capabilities updates only authorized canon/profiles/roles/templates/tests and cannot review its own work.
- Review target: `review_agent` with Architecture/Engineering Review checks output semantics, profile reuse, reader applicability, regressions, and forbidden surfaces.
- Pipeline exception: code/test implementation is a bounded companion after research/design; no output pipeline is created.

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

- Production may start: yes, after fit analysis and output design.
- Scope boundary: only files with observed Step 4 contract gaps plus exact `/about` mirrors when mapped surfaces change.

## editorial decision frame

- Chosen editorial route: extend the sole Product Intent owner, existing profiles, Professional Communication, current roles, and conditional templates; add executable output-format fixtures.
- Why this route serves the outcome: it makes analysis usable without duplicating deliverable knowledge or adding architecture.
- Alternatives considered:
  - New Product Intent Review profile — rejected because existing profiles and embedded blocks cover all reader jobs.
  - Universal Product Intent Review template — rejected because mode, reader need, evidence, stakes, and selected deliverable require adaptation.
  - Canon-only prose — rejected because ordering, leakage, directness, and conditionality need executable protection.
- Writer contract:
  - Result type: bounded canonical/test diff and reports.
  - Scope boundary: Step 4 only.
  - Must include: verdict-first order, one main gap, next decision, evidence boundary, practical validation, production consequence, editorial notes last, adaptive `limited/full`, direct no-build, no internal leakage.
  - Must not include: new profile/pipeline/role/stage/gate/status/outcome/template default, routing/ownership change, or Step 5.
- Review focus: reader job/profile fit, order, priority, directness, uncertainty density, internal architecture leakage, source-size independence, and regressions.
- Reroute triggers: any need to change modes/routing/ownership or introduce a new profile.

## required roles

| Stage | Role | Responsibility |
| --- | --- | --- |
| Intake/routing | `chief_editor` | Scope, route, selected deliverable/profile decision, and governance. |
| Research/design | `research_agent` | Baseline, deliverable-fit analysis, and output design evidence. |
| Implementation | `writer_agent` with implementation capabilities | Canon, profiles, roles, conditional templates, checker, fixtures, tests, reports. |
| Review | `review_agent` with Architecture/Engineering Review | Independent acceptance and negative-scope check. |
| Finalization | `final_editor` | Preserve approved priority/directness and create final index only after approval. |
| Closure | `chief_editor` | Finalize Step 4 without starting Step 5. |

## required evidence and checks

- Step 1–3 owner, routing, analysis, review, and final decisions.
- Current report/research-report/decision-memo profiles and catalogue.
- Professional Communication, roles, templates, deliverable tests, reader-quality tests.
- Lifecycle validation/smoke, output tests, routing, analysis/review, outcome-first/profile, generator, restart, compact path, canonical link, `/about`, forbidden-surface, and scoped-diff checks.

## stage exit criteria

- Research: current gaps and profile fit are explicit.
- Planning: adaptive contract and no-new-profile decision are reviewable.
- Implementation: observable contracts and twelve scenarios are complete.
- Review: all twenty-nine criteria pass or bounded repairs are requested.
- Closure: approved Step 4 is finalized; Step 5 remains unstarted.
