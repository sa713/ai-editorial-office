# Orchestration Plan

Pipeline: research

## task summary

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP1`
- User goal: specify Product Intent Review as a narrow, conditional, evidence-bounded capability inside the current Professional Analysis family.
- Requested deliverable: canonical capability specification plus the named Step 1 reports and governed closure artifacts.
- Format authority: `explicit`
- Selected deliverable: `../../kb/product_intent_review.md`
- Selected deliverable set: ordered set
- Audience/channel: repository owner and later implementation steps; canonical English KB plus Russian task-local reports
- Current active version: initial Step 1 packet

## task classification

- Task type: canonical capability specification, not operational implementation.
- Risk mode: `standard`
- Factual sensitivity: canonical ownership, capability boundaries, and release-state claims must be repository-traceable.
- Human approval likely required: no for this authorized Step 1; future operational implementation remains outside scope.
- Rationale: the task changes canon but expressly forbids behavior, routing, role, pipeline, template, runtime, and release-state changes.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: the specification crosses multiple existing capability boundaries and has twenty explicit acceptance criteria.
- Forbidden depth shortcuts: keyword activation, universal checklist, copied evidence taxonomy, hidden role changes, hidden workflow changes, or premature Step 2 implementation.

## task need recognition

- Observed request signals: explicit Step 1 authorization, named canonical owner, bounded canonical change surface, mandatory independent review, and detailed acceptance contract.
- Requested deliverable: full Product Intent Review capability specification and named governance reports.
- Format authority: `explicit`
- Recommended deliverable set and outcome-fit reason: respect the requested canonical spec plus task-local traceability reports; no additional product deliverables.
- One-artifact sufficiency signal: no; the canonical spec owns reusable semantics while reports prove implementation scope and requirement coverage.
- Likely primary task type: system capability specification.
- Material secondary aspects: evidence discipline, professional analysis, professional communication, architecture boundary review, and regression safety.
- Likely capabilities and why: Task Need Recognition for bounded routing; Analytical Reasoning for distinctions and gap prioritization; Professional Analysis for decision-ready specification; Architecture Review for non-duplication; Professional Communication for readable canon.
- Likely Domain Packs and why: none.
- Research / evidence recommendation: use the authorized brief, approved Step 0 decision, current canonical owners, project state, and historical proposal only as provenance.
- Risk / consequence recommendation: full review, minimal canonical diff, no operational checks disguised as implementation.
- Review recommendation: independent acceptance review against every Step 1 criterion plus explicit negative-scope checks.
- Ambiguity, contradiction, or missing information: none blocking; parent capability use is explicitly authorized without accepting or releasing Professional Analysis.
- Decomposition recommendation: baseline -> sole-owner spec -> minimal registry/ownership/relationship pointers -> traceability reports -> independent review -> closure.
- Confidence and negative evidence: high; there is no authorization for Step 2 or production behavior.
- Explicit non-decision: this plan does not activate Product Intent Review in live task routing.
- Chief Editor decision: proceed with the bounded Step 1 route.

## outcome-first deliverable decision

- User problem to solve: establish a reusable, reviewable Product Intent Review contract before operational integration.
- Requested deliverable: named canonical and task-local artifacts.
- Format authority: `explicit`
- Recommended deliverable set: same set.
- One artifact sufficient: no.
- Decision: `respect_requested`

| Order | Deliverable | Purpose | Dependency |
| --- | --- | --- | --- |
| 1 | `baseline-report.md` | Confirm starting state, authority, scope, and non-goals. | authorized brief and Step 0 |
| 2 | `../../kb/product_intent_review.md` | Own the complete reusable capability contract. | baseline |
| 3 | `specification-report.md` | Map explicit requirements to canonical sections. | canonical spec |
| 4 | `implementation-report.md` | Record exact canonical edits and preserved surfaces. | completed diff |
| 5 | `change-summary.md` | Give the reviewer a bounded scope summary. | completed diff |

- Member removal check: each named member supports a distinct explicit acceptance or governance need.
- Missing companion check: none; review and closure files are process artifacts.
- Explicit-intent preservation note: no templates, runtime tests, or implementation companions will be generated.

## selected pipeline

- Primary pipeline or mode: `research_pipeline` with a bounded canonical-specification mini-contract.
- Why this route fits: the baseline and boundary work are evidence-led; a Writer Agent then expresses the approved specification in canon; Review Agent remains independent.
- Pipeline exception: canonical-system specification is produced by `writer_agent` after the research packet, then reviewed as one scoped change set.
- Governance model unchanged: yes.

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

- Production may start: yes.
- Constraint: only the capability specification, capability-registry record, ownership pointer, necessary parent relationship note, required task pack, and exact `/about` sync if a mapped canonical source changes.

## editorial decision frame

- Chosen route: keep one full owner and make every neighboring capability boundary explicit.
- Reader journey: purpose and activation -> depth -> seven-element model -> checks -> incomplete-data behavior -> main gap and alternatives -> minimum validation -> adaptive output -> authority boundaries and failure modes.
- Practical transformation: a later implementer can add routing or task-local behavior without inventing semantics, while Step 1 itself changes no behavior.
- Alternatives rejected:
  - Expand `professional_analysis.md` with the full contract: rejected because it would blur the general parent capability and violate single narrow ownership.
  - Make Product Intent Review a new role or pipeline: rejected because no new accountability or lifecycle is needed.
  - Reuse the historical Problem Hypothesis proposal as canon: rejected because it is unaccepted, narrower in some places and broader in workflow implications in others.
- Writer contract:
  - Must include all required semantics and boundaries.
  - Must keep evidence classification delegated to the Editorial Evidence Framework.
  - Must distinguish product finding from operational review verdict.
  - Must not implement activation, output fields, role responsibilities, templates, or automation.
- Review focus: semantic completeness, sole ownership, evidence bounds, overlap control, negative-scope compliance, release-state preservation, and historical proposal disposition.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | `chief_editor` | yes | Authorize the bounded route and selected set. |
| Research | `research_agent` | yes | Establish baseline and evidence boundary. |
| Writing | `writer_agent` | yes | Produce the canonical specification and reports. |
| UX writing | none | no | No product copy is produced. |
| Review | `review_agent` | yes | Independently review the complete change set. |
| Finalization | `final_editor` | conditional | Create only the approved artifact index; do not transform canon. |
| Final governance | `chief_editor` | yes | Close Step 1 without starting Step 2. |

## required knowledge and evidence

- Primary authority: `brief.md`.
- Approved prior decision: `../TASK-PRODUCT-INTENT-REVIEW-STEP0/final_decision.md` and `architecture-decision.md`.
- Canonical boundaries: `AGENTS.md`, `project-state.md`, `kb/capability_registry.md`, `kb/professional_analysis.md`, `kb/analytical_reasoning.md`, `kb/editorial_evidence_framework.md`, `kb/task_need_recognition.md`, `kb/audience_outcome_alignment.md`, `kb/editorial_quality_attributes.md`, `kb/editorial_planning_framework.md`, `kb/architecture_review.md`, `kb/editorial_challenge_lens.md`, and role/pipeline contracts named in the brief.
- Historical evidence only: `../TASK-PROBLEM-FRAMING-FRAMEWORK/system_change_proposal.md`.
- Evidence gap: real-world PIR behavior cannot be validated in Step 1 because behavior implementation is forbidden.

## quality priorities

- Primary: complete but bounded semantics, one owner, evidence calibration, non-duplication, future implementability.
- Guardrails: no invented evidence, no release-state change, no new role/pipeline/stage/gate/status/verdict, no rigid universal artifact.
- Accepted tradeoff: specification-level completeness is preferred over operational examples or fixtures in this step.

## stage exit criteria

- Research exit: authority, current state, change surface, historical-proposal disposition options, and negative scope are explicit.
- Writing exit: required canonical and task-local artifacts exist and the diff stays inside the authorized surface.
- Review exit: all acceptance criteria and negative checks pass, or bounded repairs are requested.
- Governance exit: approved Step 1 is finalized with Step 2 explicitly unstarted.
