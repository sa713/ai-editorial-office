# Orchestration Plan

Pipeline: research

## task summary

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP6`
- User goal: evaluate Product Intent Review end to end and calibrate product judgment without feature growth.
- Requested deliverable: 30+ case suite, rubric, runner, coverage/baseline/defect/repair reports, regressions, independent review, and full task pack.
- Format authority: `explicit`
- Selected deliverable: end-to-end Product Intent Review evaluation suite
- Selected deliverable set: ordered evaluation and governance set
- Audience/channel: AI Editorial Office maintainers; test fixtures, runner, task-local decision evidence

## classification and depth

- Task type: evaluation-system design and bounded test implementation.
- Risk mode: `standard`.
- Process depth: `full`.
- Execution profile: `expanded`.
- Human approval required: no.
- Rationale: the task evaluates a cross-cutting analytical capability and may expose production defects, but does not authorize release or architecture changes.

## task need recognition

- Signals: explicit Step 6 authorization, six evaluation levels, 30+ cases, hybrid judgment, mandatory coverage and calibration metrics, repair-loop gate.
- Requested deliverable: explicit multi-artifact evaluation pack.
- One-artifact sufficiency: no.
- Likely capabilities: Analytical Reasoning, Professional Analysis, Professional Communication, Architecture Review, Engineering Review, Integrity Checking.
- Domain Packs: none; cases are sanitized or synthetic.
- Evidence basis: finalized Step 1–5 contracts/tests and repository fixtures.
- Chief Editor decision: evaluate current behavior first; production changes require a confirmed contract defect.

## product intent review activation

- Task-local Product Intent Review mode: `not_needed`.
- Basis: the task evaluates an already authorized capability; it does not ask whether a proposed product/intervention should exist.
- Production consequence: `Proceed`.
- Reroute trigger: evaluation finds a reproducible Step 1–5 contract violation.

## outcome-first deliverable decision

| Order | Deliverable | Purpose | Dependency |
| --- | --- | --- | --- |
| 1 | baseline, design, rubric | Define fair evaluation before observing results. | finalized Step 1–5 |
| 2 | case fixture, catalogue, runner, runner tests | Execute structural/coverage checks and preserve manual judgment fields. | design/rubric |
| 3 | coverage, baseline comparison, evaluation report | Interpret current behavior without one pseudo-score. | suite run |
| 4 | defect log, repair-loop report, canonical diff | Gate any production change. | evaluated failures |
| 5 | review, final, final decision | Independent acceptance and closure. | all prior evidence |

- Removal check: each member has a distinct downstream evaluation or governance consumer.
- Missing companion: none.
- Deliverable boundary: no new user-facing deliverable profile.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Selected deliverable set | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Constraint: where an old runtime output is unavailable, use a documented historical contract baseline rather than inventing an old response.

## editorial decision frame

- Chosen route: build a hybrid evaluation suite inside existing test architecture; use deterministic runner checks for structure/coverage/invariants and saved independent manual judgment for product quality.
- Alternatives rejected:
  - String-matched gold answers — reject because product judgment permits multiple correct formulations.
  - Fully manual suite — reject because metadata, coverage, duplicate IDs, routing agreement, and forbidden behavior are deterministic.
  - New evaluation pipeline or reviewer role — reject because tests and existing Review Agent cover the task.
- Implementation contract:
  - minimum 30 cases, 8 classes, 8 pairs, 10 adversarial, required mode/finding/validation distributions;
  - every case includes input, hidden evaluator structure, required properties, forbidden errors, accepted variability, expected behavior, observed structured result, and manual evaluation;
  - runner validates but does not manufacture product judgment;
  - no production edits without defect evidence.
- Review focus: case difficulty, anti-overfit, negative cases, expected variability, separation of automation/judgment, hidden failures, repair evidence, regressions, and Step 7 readiness.

## roles

| Stage | Role | Responsibility |
| --- | --- | --- |
| Intake/orchestration | `chief_editor` | Scope, evaluation-first gate, deliverables, and governance. |
| Research/design | `research_agent` | Baseline, rubric, case design, expected behavior boundaries. |
| Evaluation implementation | `writer_agent` with implementation capabilities | Fixtures, runner, tests, catalogue, and reports; no production repair without defect handoff. |
| Manual judgment | independent `review_agent` role instance | Score product judgment without editing results. |
| Final review | independent `review_agent` role instance | Review design, evidence, repairs, regression, and readiness. |
| Finalization | `final_editor` | Preserve approved findings and limitations. |
| Closure | `chief_editor` | Final governance; Step 7 remains unauthorized. |

## required validation

- case metadata and unique IDs;
- class, pair, adversarial, mode, finding, validation-method and disposition coverage;
- evaluation runner tests;
- Step 1–5 routing, decision/review, output, validation regressions;
- lifecycle, state, restart, compact path, generator, deliverable selection,
  Professional Analysis, reader-centered quality, canonical links, `/about`,
  forbidden surfaces, scoped diff, and `git diff --check`.

## exit criteria

- Research: design/rubric precede result calibration.
- Implementation: suite meets coverage and runner produces manifest/metrics.
- Evaluation: failures are visible; production defects and repairs are explicit.
- Review: all 34 criteria and evaluation-design checks pass.
- Closure: Step 6 finalized; Step 7 unstarted.
