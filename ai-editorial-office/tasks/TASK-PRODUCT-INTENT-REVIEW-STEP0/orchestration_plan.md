# Orchestration Plan

Pipeline: research

## task summary

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP0`
- User goal: audit the current AI Editorial Office architecture and decide the smallest correct integration point for Product Intent Review.
- Requested deliverable: `baseline-report.md`, `product-intent-responsibility-map.md`, and `architecture-decision.md`
- Format authority: `explicit`
- Selected deliverable: `baseline-report.md`
- Selected deliverable set: ordered set
- Audience/channel: repository owner and future implementer; task-local Markdown
- Current active version: the three named Step 0 reports

## task classification

- Task type: architecture audit / research / decision support
- Risk mode: `standard`
- Factual sensitivity: repository architecture and governance claims must be file-traceable
- Human approval likely required: no for Step 0 completion; later implementation remains outside scope
- Rationale: the task affects future canon but currently authorizes only read-only analysis plus task-local reports.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: the requested audit spans several canonical owners and must distinguish existing coverage, gaps, duplication risk, and later change surface.
- Forbidden depth shortcuts: keyword-only audit, one universal checklist, hidden implementation, role creation by default, or extrapolation from legacy tasks.
- Expanded profile trigger: architectural significance and cross-owner consequences.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable
- Non-activation reason: this is an internal repository architecture task.
- Stop condition: none.

## task need recognition

- Observed request signals: new system capability, explicit architecture audit, cross-canonical-owner scan, staged initiative, no implementation at Step 0.
- Requested deliverable: three named architecture-audit reports.
- Format authority: `explicit`
- Recommended deliverable set and outcome-fit reason: the requested ordered set is already minimum sufficient because it separates evidence baseline, ownership/gap mapping, and the actual architecture decision.
- One-artifact sufficiency signal: no; merging would weaken audit traceability and violate explicit output names.
- Likely primary task type: repository architecture research.
- Material secondary aspects: evidence discipline, professional analysis, professional communication, architecture review, regression planning.
- Likely capabilities and why: Task Need Recognition for routing evidence; Analytical Reasoning for gap diagnosis; Professional Analysis for synthesis; Professional Communication for decision-ready reports; Architecture Review for design-fit judgment.
- Likely Domain Packs and why: none; the subject is the Editorial Office architecture itself.
- Research / evidence recommendation: inspect current canonical owners and cite file paths and sections.
- Risk / consequence recommendation: standard risk, expanded evidence, no production mutations.
- Review recommendation: independent review of the complete three-report set against `brief.md`.
- Architecture / engineering / communication significance: architecture significance is material; engineering significance is not yet material because implementation is forbidden.
- Ambiguity, contradiction, or missing information: exact later file changes are recommendations only until Step 1+; no blocker.
- Decomposition recommendation: baseline -> responsibility map -> architecture decision -> independent review.
- Confidence and negative evidence: high confidence in task classification; no evidence that a new role or lifecycle is authorized.
- Explicit non-decision: this advisory view does not select implementation design beyond Step 0.
- Chief Editor decision or next question: proceed with the requested three-report set and bounded research route.

## outcome-first deliverable decision

- User problem to solve: identify the correct minimal architectural home for Product Intent Review before implementation.
- Requested deliverable: three named Markdown reports.
- Format authority: `explicit`
- Recommended deliverable set: same ordered set.
- One artifact sufficient: no; each report serves a distinct acceptance need.
- Why this is the minimum sufficient outcome-fit artifact family: evidence, ownership, and decision remain separately reviewable without extra companion artifacts.
- Alternative value or mismatch, if any: a single combined report would be shorter but would erase the requested separation.
- Decision: `respect_requested`
- Selected deliverable: `baseline-report.md`
- Selected deliverable set mode: `ordered set`
- Selected deliverable set:

| Order | Deliverable | Purpose in this task | Dependency | Production priority |
| --- | --- | --- | --- | --- |
| 1 | `baseline-report.md` | Establish current mechanisms and their observed coverage. | independent evidence base | 1 |
| 2 | `product-intent-responsibility-map.md` | Map owners, partial coverage, exact gaps, and duplication risks. | depends on baseline | 2 |
| 3 | `architecture-decision.md` | Recommend the minimal extension and later change surface. | depends on baseline and map | 3 |

- Member removal check: removing any member drops one explicit acceptance layer: baseline evidence, ownership analysis, or decision.
- Missing companion check: none; review and governance files are process artifacts, not deliverable companions.
- Explicit-intent preservation note: no additional product output or implementation artifact will be generated.

## selected pipeline

- Primary pipeline or mode: `research_pipeline`
- Why this route fits the primary selected deliverable: Step 0 is an evidence-backed repository study with recommendations, not production implementation.
- Companion mini-contracts:
  - Deliverable: `product-intent-responsibility-map.md`
  - Existing production owner: `research_agent`
  - Dependency and shared evidence: canonical architecture scan summarized in the baseline.
  - Review target: responsibility boundaries, overlap, and exact functional gap.
  - Deliverable: `architecture-decision.md`
  - Existing production owner: `research_agent` using Architecture Review capability.
  - Dependency and shared evidence: baseline plus responsibility map.
  - Review target: minimality, owner fit, alternatives, role/gate preservation, later change surface, and regression risks.
- Pipeline exceptions or local constraints: no Writer stage; the Research Agent owns the analytical reports, Review Agent reviews them, and Chief Editor closes Step 0. This does not weaken review independence.

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

- Rationale: the attached canonical brief fully defines scope, outputs, prohibitions, and acceptance criteria.
- Production may start: yes
- If `constrain`: work is limited to task-local reports and governance artifacts; no production-logic or canon changes.

## editorial decision frame

- Chosen editorial route: evidence-first repository audit followed by an ownership map and an architecture decision.
- Why this route serves the selected deliverable set and task outcome: it exposes what already exists before proposing a minimal extension.
- Reader journey rationale: scattered knowledge of current mechanisms -> explicit coverage/gap map -> decision-ready minimal integration recommendation.
- Cognitive Bridge:
  - What the reader already knows: AI Editorial Office has task routing, capabilities, lifecycle, challenge, evidence, and review mechanisms.
  - Old or incomplete model to update: partial mechanisms may appear sufficient even if none owns product-intent reconstruction and causal viability.
  - Required transition: distinguish reusable foundations from the exact missing responsibility and from future implementation.
- Moments of Insight:
  - Existing audience/outcome checks assess artifact usefulness but do not establish whether the proposed intervention itself is worth creating.
  - The Editorial Challenge Lens can pressure-test route assumptions but is review-bound and does not own pre-production product-intent analysis.
  - Task Need Recognition can detect relevant signals but intentionally cannot activate or execute the review.
  - The minimal extension should attach to existing lifecycle and roles rather than create a parallel process.
- Practical Transformation: the repository owner can approve, revise, or reject a bounded Step 1 direction without authorizing implementation in Step 0.
- Alternatives considered:
  - Reuse Architecture Review unchanged.
    - Rejected because its canonical scope is architecture fitness, not general product intent across courses, services, campaigns, events, and processes.
  - Expand the Editorial Challenge Lens only.
    - Rejected provisionally because it is review-bound and too late for the required pre-production behavior.
  - Create a Product Strategist role and pipeline.
    - Rejected because no unique accountability or lifecycle need has been established.
- Writer/UX Writer contract:
  - Result type: not applicable; Research Agent produces the requested analytical reports.
  - Scope boundary: Step 0 evidence and recommendation only.
  - Must include: studied documents, current coverage, exact gap, minimal extension, alternatives, later canonical change surface, risks, tests, open questions, readiness recommendation.
  - Must not include: implemented capability, canon modifications, runtime changes, new role, new gate, or Step 1 work.
  - Source boundary and confidence: current canonical repository files plus the user-supplied `brief.md`; distinguish confirmed repository behavior from recommendation.
- Review focus: completeness against Step 0 acceptance criteria, canonical-owner accuracy, minimality, non-duplication, role/gate preservation, and absence of implementation.
- Reroute triggers: a discovered existing canonical owner fully covering Product Intent Review, a material canon conflict, or any need to modify production logic.

## custom workflow mini-contract

- Deviation: analytical report production remains with `research_agent`; no Writer/Final Editor stage is used.
- Reason: the requested outputs are research and architecture-decision artifacts, not editorial copy; named deliverables remain unchanged after approved review.
- Owner: `chief_editor`
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | `chief_editor` | yes | Normalize source, select set, and constrain Step 0. |
| Research | `research_agent` | yes | Produce the three reports from repository evidence. |
| Writing/UX writing | none | no | Not applicable to architecture-audit reports. |
| Review | `review_agent` | yes | Independently review the full report set. |
| Finalization | none | no | Approved named reports are the final deliverable set. |
| Final governance | `chief_editor` | yes | Close Step 0 without authorizing Step 1. |

## required knowledge and evidence

- Required KB: `task_object_model.md`, `capability_registry.md`, `task_need_recognition.md`, `shared_lifecycle_kernel.md`, `editorial_evidence_framework.md`, `analytical_reasoning.md`, `professional_analysis.md`, `professional_communication.md`, `architecture_review.md`, `editorial_planning_framework.md`, `audience_outcome_alignment.md`, `editorial_quality_attributes.md`, `editorial_failure_modes.md`, relevant deliverable profiles.
- Required source/evidence files: `AGENTS.md`, `project-state.md`, relevant role specs, pipelines, templates, tests, and reader-centered implementation evidence.
- Evidence gaps: none blocking; non-canonical idea/backlog files may be used only as historical implementation evidence, not authority.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Canonical initiative requirements. |
| `research.md` | required | reviewer, Chief Editor | Compact evidence index satisfying the selected Research Pipeline contract without duplicating the requested reports. |
| Three named reports | required | repository owner, reviewer, future implementer | Explicit user deliverables. |
| `review.md` | required | Chief Editor | Review gate. |
| `final_decision.md` | required | repository owner | Step 0 governance closure. |
| `final.md` | omitted | none | The explicit three-file set is the final artifact set. |
| Implementation files/tests | omitted | none | Forbidden at Step 0. |

## quality priorities

- Primary: architectural correctness, traceability, minimality, non-duplication, decision usefulness.
- Guardrails: no invented current behavior; no implementation; no role/gate proliferation; preserve uncertainty.
- Accepted tradeoff: breadth is limited to architecture mechanisms material to Product Intent Review, not every repository file.

## stage exit criteria

- Research exit: canonical source list complete, coverage claims traceable, exact gap stated, and three reports ready together.
- Review exit: `review.md` returns `approved`, `changes_requested`, or `blocked` with checked files and independence recorded.
- Governance exit: Step 0 is closed with readiness recommendation for Step 1, while Step 1 remains unstarted.
