# Orchestration Plan

## task summary

- Task ID: `TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE`
- User goal: complete `S5.R3 - Memory Hygiene Intelligence` through Release
  Candidate
- Deliverable: researched, implemented, scenario-tested, independently
  reviewed, documented, state-aligned, memory-aligned, and locally committed RC
- Audience/channel: Project Lead architectural review through repository
  artifacts and final handback
- Current active version: task-manifest active artifact set

## task classification

- Task type: system capability integration release
- Risk mode: `high-governance`
- Factual sensitivity: high; professional claims and memory/canonical
  boundaries must be traceable
- Human approval likely required: yes, after RC delivery for acceptance
- Rationale: external memory can mislead future work if wrong, stale, bloated,
  sensitive, or treated as authority

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: authoritative research, cross-owner architecture synthesis,
  canonical changes, ten scenarios, memory sync, independent review, and
  release packaging require full traceability
- Forbidden shortcuts: no direct `/about` rewrite before disposition, no
  automatic propagation, no canon from memory, no review bypass
- Expanded profile trigger: high-governance system release with external-memory
  and state consequences

## selected pipeline

- Pipeline: `research_pipeline.md`
- Why this pipeline: professional evidence and current owner analysis must
  precede architecture and implementation
- Local contract: after research, use the existing lifecycle for synthesis,
  writing/implementation, review, finalization, and Chief Editor RC governance

## client and domain context

- Client profile: `none`
- Client profile status: `not_applicable`
- Active Domain Knowledge Pack: `none`
- Non-activation reason: memory hygiene is a shared repository-governance
  concern; pack content is considered only for inclusion/omission examples
- Stop condition: a pack or memory summary is treated as canonical policy

## active capabilities

- Research and Evidence Classification
- Evidence Confidence Assessment
- Analytical Reasoning
- Professional Analysis
- Professional Communication
- Architecture Review
- Knowledge Evolution and Memory Curation
- Pattern Reuse and Stale Knowledge Detection
- Integrity Checking
- Engineering Review only for changed validation behavior

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

- Rationale: mission, sources, scenarios, prohibited changes, validations,
  repository, and Project Lead boundary are explicit.
- Production may start: yes

## editorial decision frame

- Chosen route: research memory, knowledge, records, synchronization,
  provenance, compression, freshness, and human-review practice; map it to
  existing Knowledge Evolution, Memory Curation, Integrity Checking, Chief
  Editor, Review Agent, and `/about` contracts; implement one compact manual
  disposition flow with exact-copy and summary branches.
- Why this route serves the task: it makes memory decisions reproducible while
  preserving repository authority and a bounded 20-file package.
- Alternatives considered:
  - Create a Memory Manager role or separate memory-governance framework.
    - Rejected: existing owners already cover classification, challenge, and
      validation.
  - Automatically mirror every changed canonical file or commit.
    - Rejected: materiality, sensitivity, compactness, and human review require
      selective disposition.
  - Store full repository detail in external memory.
    - Rejected: it creates bloat, duplication, and a second source of truth.
- Writer/implementation contract:
  - Result type: bounded canonical guidance, existing role/review consequences,
    ten-scenario test, release documentation, state sync, and reviewed `/about`
    synchronization.
  - Reader path: signal -> canonical source/evidence -> materiality ->
    disposition -> validation -> review -> manual memory update or recorded
    no-sync.
  - Must include: sync/no-sync, exact-copy/summary, stale/contradiction,
    omission/compression/correction/retirement, duplicate consolidation,
    ownership/evidence/validation, temporary-state replacement, and privacy.
  - Must not include: automatic writes, completeness scores, mandatory commit
    sync, new stores/owners/roles/pipelines/stages/gates, silent deletion, or
    memory override.
  - Source boundary: authoritative external practice plus current repository
    canon; repository-specific choices remain explicit synthesis.
- Review focus: authority, provenance, exact-copy fidelity, summary semantic
  preservation, bounded growth, no-sync evidence, omission/privacy, stale and
  contradiction repair, non-automation, state, checker, and scenarios.
- Reroute triggers: safe behavior requires automatic authority, destructive
  cleanup without trace, or a new owner/governance layer.

## required roles

| Stage | Role | Required? | Responsibility |
| --- | --- | --- | --- |
| Intake/orchestration | `chief_editor` | yes | Route, authority, owner selection |
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
| Existing-owner patches | required | future releases/tasks | Smallest usable mechanism |
| Ten-scenario validation | required | review/Project Lead | Prove disposition behavior |
| `/about` exact-copy/summary updates | required if material | external memory | RC must be represented accurately |
| New runtime sync engine/store | omitted | none | Forbidden and unsupported |
| Release Pack | required | Project Lead | Readiness rule |
| Review/final/governance files | required | governance | Release closure |

## execution order

| Step | Role | Output | Exit condition |
| --- | --- | --- | --- |
| 1 | `research_agent` | landscape/evidence artifacts | Evidence sufficient |
| 2 | `chief_editor` | architecture synthesis | Existing-owner route selected |
| 3 | `writer_agent` | canon, scenarios, report, pack, state/memory | RC implementation complete |
| 4 | `review_agent` | `review.md` | Approved or bounded repair |
| 5 | `final_editor` | `final.md` | Approved package finalized |
| 6 | `chief_editor` | `final_decision.md`, S5.R3 `Review`, commit | RC ready |

## review requirements

- Review artifact: `review.md`
- Depth: full high-governance review with embedded checklist
- Independence: reviewer role instance distinct from research, synthesis, and
  writing instances
- Checks: sources, owner boundaries, disposition determinism, semantic
  preservation, privacy/omission, non-automation, scenarios, state, `/about`,
  validators, and protected paths
- Optional support artifacts: none; one complete `review.md` is sufficient

## human approval requirements

- Required: yes
- Approval owner: Project Lead
- Evidence needed: completed Release Pack and final local commit
- Cannot proceed past: S5.R3 `Review` to `Done`

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Memory becomes parallel canon | Authority drift | Chief Editor / Review | Source-first disposition and conflict rule |
| Every change triggers growth | Bloat/noise | Chief Editor | Materiality and no-sync/omit defaults |
| Compression drops caveats | Misleading summary | Writer / Review | Semantic preservation validation |
| Cleanup deletes meaning | Lost context | Review Agent | Consolidate/retire with preserved rationale |
| Temporary RC state persists | Stale future context | Chief Editor | Supersession trigger after acceptance |
| Advisory checker becomes writer | Automation drift | Chief Editor | Read-only reporting only |

## escalation conditions

- Stop if no canonical source can support a memory fact, a contradiction cannot
  be resolved from repository evidence, or implementation requires forbidden
  autonomous authority.

## completion criteria

- Required artifacts complete; all ten scenarios pass; review approved;
  validators pass; `/about` is aligned; S5.R3 is `Review`; S5.R4 remains not
  started; Project Lead acceptance remains pending.

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, manifest, latest handoff, current
  artifact, and directly relevant owner/pipeline.
- Current active version: manifest artifact set.
- Deprecated versions: none.
