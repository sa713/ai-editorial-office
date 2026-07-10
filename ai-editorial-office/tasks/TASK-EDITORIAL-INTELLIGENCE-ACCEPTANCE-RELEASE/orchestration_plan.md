# Orchestration Plan

## task summary

- Task ID: `TASK-EDITORIAL-INTELLIGENCE-ACCEPTANCE-RELEASE`
- User goal: complete `S5.R5 - Editorial Intelligence Acceptance` through
  Release Candidate.
- Deliverable: researched, synthesized, implemented, scenario-tested,
  independently reviewed, documented, state/memory-aligned if required, and
  locally committed RC.
- Audience/channel: Project Lead architectural review through repository
  artifacts and final handback.

## task classification

- Task type: system governance integration release.
- Risk mode: `high-governance`.
- Factual sensitivity: high; the contract governs evidence and decision support
  for future self-improvement releases.
- Human approval likely required: yes, after RC delivery.
- Rationale: a weak contract could legitimize bureaucracy, hidden governance,
  unsupported improvement claims, or automation that displaces human judgment.

## process depth

- Depth: `full`.
- Execution profile: `expanded`.
- Rationale: authoritative cross-domain research, existing-owner synthesis,
  canonical release-standard change, twelve scenarios, independent review,
  state sync, possible memory sync, and release packaging require full traceability.
- Forbidden shortcuts: no score, checklist-only proof, synthetic-as-operational
  claim, automatic disposition, second acceptance gate, or duplicate owner.

## selected pipeline

- Pipeline: `research_pipeline.md`.
- Why this pipeline: claims about evaluation, assurance, human authority,
  architecture cost, and operational evidence must precede owner selection and
  implementation.
- Local contract: apply the Roadmap evolution sequence—Research -> Architecture
  Synthesis -> bounded release -> Validation -> conditional Memory Sync—inside
  the existing lifecycle and Project Lead acceptance boundary.

## client and domain context

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Active Domain Knowledge Pack: `none`.
- Non-activation reason: accepted packs may supply adjacent context, but the
  release governs Stage 5 intelligence packages rather than a domain task.

## active capabilities

- Research and Evidence Classification.
- Evidence Confidence Assessment.
- Analytical Reasoning.
- Professional Analysis.
- Professional Communication.
- Architecture Review.
- Engineering Review for repository change and validation evidence.
- Evaluation Signals.
- Knowledge Evolution and Memory Curation.
- Integrity Checking.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the mission names the scope, evidence topics, contract dimensions,
  prohibited architecture, scenarios, artifacts, state boundary, and validators.
- Production may start: yes.

## editorial decision frame

- Chosen route: research authoritative evidence and accepted Stage 5 owners;
  extend the existing Release Pack/Project Lead decision-support boundary with
  one conditional intelligence-acceptance contract if the owner fit is proven.
- Why this route serves the task: it can make value, restraint, uncertainty,
  cost, automation, and disposition inspectable without creating a second
  acceptance workflow.
- Alternatives considered:
  - Create a new acceptance pipeline, board, gate, or role.
    - Rejected: authority and workflow already exist and the mission forbids it.
  - Add a universal weighted acceptance score or maturity model.
    - Rejected: incompatible evidence cannot be collapsed safely and the
      mission forbids governance scoring.
  - Put the contract entirely in Evaluation Signals or Knowledge Evolution.
    - Rejected provisionally: both provide evidence or learning disposition but
      neither owns Project Lead release acceptance; research will test precise reuse.
- Writer/implementation contract:
  - Result type: bounded Release Pack integration, supporting guidance only if
    an owner gap is proven, scenario test, release report, state/memory sync,
    and review packet.
  - Must include: improvement claim, intended/observed value, evidence and
    baseline, real/synthetic distinction, architecture/governance cost, human
    authority, automation, reversibility/containment, maintenance, uncertainty,
    non-claims, cross-effects, and recommended human disposition.
  - Must not include: automatic decision/action, scores, maturity levels,
    dashboards, boards, gates, new roles/pipelines/stages, or generic expansion
    to ordinary releases without evidence.
  - Source boundary: authoritative external practice plus repository canon;
    repository-specific architecture choices remain explicit synthesis.
- Review focus: evidence/claim separation, operational proof, value and
  restraint, human authority, owner fit, automation risk, uncertainty,
  contradictory effects, scenario coverage, non-scoring, state, memory, and
  protected paths.
- Reroute triggers: the contract cannot be expressed inside the existing
  Release Pack boundary, requires a forbidden governance structure, or cannot
  distinguish proof from assertion without a new evidence owner.

## required roles

| Stage | Role | Required? | Responsibility |
| --- | --- | --- | --- |
| Intake/orchestration | `chief_editor` | yes | Route and acceptance-owner boundary |
| Research | `research_agent` | yes | Authoritative evidence base |
| Synthesis | `chief_editor` | yes | Minimal architecture decision |
| Writing/implementation | `writer_agent` | yes | Bounded repository patch |
| Review | `review_agent` | yes | Independent deterministic challenge |
| Finalization | `final_editor` | yes | Controlled final pointer |
| Governance | `chief_editor` | yes | RC decision only |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| Task control artifacts | required | all roles | Governance/restartability |
| Source/fact/claim trace | required | synthesis/review | High-governance evidence |
| Three mission research/release artifacts | required | Project Lead/review | Explicit deliverables |
| Existing-owner contract patch | required if owner fit holds | future Stage 5 releases | Smallest mechanism |
| New owner file | conditional and disfavored | future Stage 5 releases | Only if current standard cannot own contract |
| Twelve-scenario validation | required | review/Project Lead | Demonstrate disposition behavior |
| `/about` updates | conditional | external memory | Only when current checker/memory contract requires |
| Release Pack | required | Project Lead | Existing readiness owner |
| Review/final/governance files | required | governance | Release closure |

## execution order

| Step | Role | Output | Exit condition |
| --- | --- | --- | --- |
| 1 | `research_agent` | landscape and evidence artifacts | Evidence sufficient |
| 2 | `chief_editor` | architecture synthesis | Owner route selected |
| 3 | `writer_agent` | contract, scenarios, report, pack, state/memory | RC implementation complete |
| 4 | `review_agent` | `review.md` | Approved or bounded repair |
| 5 | `final_editor` | `final.md` | Approved package finalized |
| 6 | `chief_editor` | `final_decision.md`, S5.R5 `Review`, commit | RC ready |

## review requirements

- Review artifact: `review.md`.
- Depth: full high-governance review with embedded checklist.
- Independence: reviewer role instance distinct from the Writer Agent instance.
- Checks: sources, claims, owner boundaries, value/restraint, real-use proof,
  authority, automation, architecture/maintenance cost, uncertainty, all
  dispositions and scenarios, state, memory, validators, and protected paths.

## human approval requirements

- Required: yes.
- Approval owner: Project Lead.
- Evidence needed: completed Release Pack and final local RC commit.
- Cannot proceed past: S5.R5 `Review` to `Done`.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Checklist compliance substitutes for proof | False improvement claim | Review Agent / Project Lead | Require claim-evidence link and gaps/non-claims |
| Synthetic cases masquerade as operations | False confidence | Research / Review | Label evidence origin and cap claim strength |
| Acceptance becomes scoring | Hidden governance | Chief Editor / Review | Qualitative two-principle judgment and no aggregation |
| Existing owners are duplicated | Architecture drift | Chief Editor | Owner map and reference-first integration |
| Human review is weakened | Authority loss | Project Lead / Review | Explicit decision authority, override, automation boundary |
| Cost is ignored | Bureaucracy and decay | Architecture Review | Architecture and maintenance burden with proportionality |

## escalation conditions

- Stop if the mechanism requires automatic governance, a new gate or decision
  owner, or evidence cannot support a truthful Release Candidate claim.

## completion criteria

- Required artifacts complete; all twelve scenarios pass; independent review
  approved; validators pass; memory aligned if required; S5.R4 accepted is
  normalized; S5.R5 is `Review`; Stage 5 remains active; Project Lead
  acceptance remains pending; no push occurs.

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, manifest, latest handoff, current
  artifact, and the directly relevant owner/pipeline.
- Current active version: manifest artifact set.
- Deprecated versions: none.
