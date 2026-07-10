# Orchestration Plan

## task summary

- Task ID: `TASK-EVALUATION-SIGNALS-RELEASE`
- User goal: complete `S5.R2 - Evaluation Signals` through Release Candidate
- Deliverable: researched, implemented, scenario-tested, independently
  reviewed, documented, state-aligned, memory-aligned if required, and
  committed release candidate
- Audience/channel: Project Lead architectural review through repository
  artifacts and final handback
- Current active version: task-manifest active artifact set

## task classification

- Task type: system capability integration release
- Risk mode: `high-governance`
- Factual sensitivity: high; professional claims and canonical behavior must be
  traceable
- Human approval likely required: yes, after delivery for acceptance
- Rationale: the release affects reusable governance-support behavior while
  being forbidden from making governance decisions

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: external research, multi-owner synthesis, canonical changes,
  representative validation, memory assessment, review, and release packaging
  need full traceability
- Forbidden depth shortcuts: no direct scoring design, no canon patch before
  synthesis, no review bypass, no dashboard or automation substitute
- Expanded profile trigger: high-governance cross-owner system release

## selected pipeline

- Pipeline: `research_pipeline.md`
- Why this pipeline: professional evidence and repository-owner analysis must
  precede architecture and implementation
- Pipeline exceptions or local constraints: after research, use the existing
  lifecycle to synthesize, write the bounded implementation, review,
  finalize, and record Chief Editor governance

## client and domain context

- Client profile: `none`
- Client profile status: `not_applicable`
- Active Domain Knowledge Pack: `none`
- Non-activation reason: this is repository governance-support work; packs are
  research subjects, not task authorities
- Stop condition: a pack is treated as policy or decision authority

## active capabilities

- Research and Evidence Classification
- Evidence Confidence Assessment
- Analytical Reasoning
- Professional Analysis
- Professional Communication
- Architecture Review
- Knowledge Evolution and stale-knowledge handling
- Engineering Review only if executable validation changes

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

- Rationale: the mission defines the repository, sources, boundaries,
  artifacts, cases, validation, exclusions, and Project Lead authority.
- Production may start: yes

## editorial decision frame

- Chosen editorial route: research professional practice, map useful signals to
  existing evidence, learning, review, architecture, Domain Pack, and release
  owners, implement one compact advisory signal contract, and prove through
  contradictory and noisy cases that the contract informs but never decides.
- Why this route serves the task: it exposes meaningful observations without
  creating a parallel evaluation system or score.
- Alternatives considered:
  - Build a dashboard or scorecard.
    - Rejected: it turns mixed evidence into false precision and adds an
      unnecessary product surface.
  - Add a new Evaluation role, pipeline, or review gate.
    - Rejected: existing roles and review/governance touchpoints already own
      evidence, challenge, and decisions.
  - Add automated trend scanning and governance actions.
    - Rejected: evidence volume and mission authority support only optional,
      human-reviewed observations.
- Writer/implementation contract:
  - Result type: bounded canonical guidance, optional record shape,
    representative cases, release documentation, and state/memory sync.
  - Angle or reader path: signal question -> evidence -> context and limits ->
    interpretation -> affected owner -> optional Project Lead consideration ->
    explicit non-decision.
  - Scope boundary: only signals material to a human decision; task-local by
    default and reusable only after comparable evidence.
  - Must include: activation/use, review recurrence, architecture drift,
    evidence quality, learning movement, stale knowledge, release observations,
    maintenance burden, noise rejection, contradiction handling.
  - Must not include: scores, KPIs, rankings, targets, gates, dashboards,
    automated acceptance/rejection, automatic canon/backlog/roadmap/memory
    change, capability retirement, or new operational structure.
  - Source boundary and confidence: primary/authoritative sources plus current
    repository evidence; synthesized recommendations remain bounded in scope.
- Review focus: advisory boundary, evidence traceability, qualitative versus
  countable signals, task-local versus reusable routing, noise and
  contradiction handling, owner reuse, scenario results, state and memory.
- Reroute triggers: signal design requires scalar scoring, automatic decisions,
  new authority, or mandatory task-wide telemetry.

## required roles

| Stage | Role | Required? | Responsibility |
| --- | --- | --- | --- |
| Intake/orchestration | `chief_editor` | yes | Route, authority, owner selection |
| Research | `research_agent` | yes | Authoritative evidence base |
| Synthesis | `chief_editor` | yes | Minimal architecture decision |
| Writing/implementation | `writer_agent` | yes | Bounded repository patch |
| Review | `review_agent` | yes | Independent deterministic challenge |
| Finalization | `final_editor` | yes | Final deliverable pointer |
| Governance | `chief_editor` | yes | Release Candidate decision only |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| Task control artifacts | required | all roles | Governance and restartability |
| `sources.md`, `facts.md`, `claims_table.md` | required | synthesis/review | High-governance traceability |
| Three mission research/release artifacts | required | Project Lead/review | Explicit deliverables |
| Existing canonical owner patches | required | future work | Smallest usable mechanism |
| Representative scenario validation | required | review/Project Lead | Prove non-decision behavior |
| `/about` updates | conditional | external memory | Only when checker or material canon/state change requires it |
| New runtime automation, score, or dashboard | omitted | none | Forbidden and unsupported |
| `release-pack.md` | required | Project Lead | Release readiness rule |
| `review.md`, `final.md`, `final_decision.md` | required | governance | Review and RC closure |

## execution order

| Step | Role | Output | Exit condition |
| --- | --- | --- | --- |
| 1 | `research_agent` | landscape and evidence artifacts | Evidence sufficient |
| 2 | `chief_editor` | architecture synthesis | Existing-owner design selected |
| 3 | `writer_agent` | canonical implementation and scenarios | Complete RC implemented |
| 4 | `review_agent` | `review.md` | Approved or bounded repair named |
| 5 | `final_editor` | `final.md` | Approved package summarized |
| 6 | `chief_editor` | `final_decision.md`, release state `Review`, commit | RC ready for Project Lead |

## status transitions

- Starting status: `intake`
- Current status: `research`
- Next expected status: `planning`
- Status owner: current lifecycle role, recorded by Chief Editor at transition
- Status update trigger: stage exit, owner handoff, review outcome, finalization

## review requirements

- Review artifact: `review.md`
- Review depth: full high-governance review with embedded checklist
- Reviewer independence requirement: reviewer role instance distinct from the
  research, synthesis, and writing role instances
- Claims/evidence checks required: authoritative-source traceability,
  inference marking, owner boundaries, optionality, advisory/non-decision
  behavior, case evidence, validation outputs
- Optional review artifacts justified: no; one complete `review.md` is enough

## human approval requirements

- Required: yes
- Approval owner: Project Lead
- Evidence needed: completed Release Pack and final commit
- Cannot proceed past: S5.R2 `Review` to `Done`

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Counts become targets | Gaming and vanity metrics | Chief Editor / Review | Context and non-decision fields; reject target use |
| Mixed signals collapse into a score | False precision | Chief Editor / Review | Preserve each signal and contradiction separately |
| Optional capture becomes telemetry | Process bloat | Chief Editor | Materiality trigger and existing-artifact default |
| Signal becomes governance automation | Authority drift | Project Lead / Review | Explicit prohibited actions and human decision boundary |
| Rare activation becomes automatic retirement | Capability loss | Review | Treat frequency as a question, not value proof |
| State lag persists | Misleading release context | Chief Editor | Normalize ROADMAP/project-state during implementation |

## escalation conditions

- Stop or escalate if an existing owner cannot hold the behavior without a new
  role, pipeline, status, review gate, score, or automated authority.

## completion criteria

- Required artifacts complete: all mission, task, validation, and release
  artifacts exist and are current
- Review outcome acceptable: `approved`
- Blockers resolved: yes
- Governance fields complete: S5.R2 in `Review`, Project Lead acceptance pending

## finalization conditions

- Finalization may start when: independent review is approved
- Finalization must stop when: meaning, evidence, boundaries, or release state
  would change outside approved scope
- Compact finalization shape allowed: no; high-governance release needs final
  pointer, handoff, and Chief Editor decision
- Conditional finalization artifacts needed: no separate checklist or notes;
  `review.md`, `final.md`, handoff, and `final_decision.md` are sufficient

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, `task-manifest.md`, latest handoff,
  current artifact, and directly relevant owner/pipeline
- Current active version: task-manifest artifact set
- Deprecated/previous versions: none
- Latest relevant handoff: none at research entry
