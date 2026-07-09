# Orchestration Plan

## task summary

- Task ID: `TASK-SOFTWARE-ARCHITECTURE-DOMAIN-PACK-RELEASE`
- User goal: complete backlog release `S4.R2 - Software Architecture Domain
  Pack` and reach release-candidate state.
- Deliverable: research, architecture synthesis, canonical candidate domain
  pack, validation, `/about` sync if required, release report, release pack,
  independent review, final governance decision.
- Audience/channel: Project Lead architectural review.
- Current active version: release artifacts listed in `task-manifest.md`.

## task classification

- Task type: domain knowledge pack release
- Risk mode: `high-governance`
- Factual sensitivity: high for external research, source interpretation, and
  canonical knowledge-pack boundaries.
- Human approval likely required: after delivery, for Project Lead acceptance.
- Rationale: the release creates the first concrete Domain Knowledge Pack and
  must prove the S4.R1 standard works without architecture drift.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: source-backed domain pack work requires research, synthesis,
  pack writing, validation, review, and release packaging.
- Forbidden depth shortcuts: no direct pack without research and synthesis; no
  review bypass; no role/capability/pipeline creation.
- Expanded profile trigger: canonical high-governance release work.

## selected pipeline

- Pipeline: `research` with task-local release mini-contract
- Why this pipeline: the release starts with source-backed domain research and
  then produces a knowledge artifact.
- Pipeline exceptions or local constraints: implementation, validation, release
  packaging, and governance occur under the existing lifecycle; no new release
  or domain-pack pipeline is created.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable.
- Non-activation reason: no client-owned communication or Sber policy task.

## domain pack handling

- Active pack before production: none.
- Candidate pack: `Software Architecture`.
- Candidate pack status: in development until review approves it as release
  candidate.
- Use rule: the candidate pack may be validated inside this release but must
  not be treated as accepted active canon outside the release before Project
  Lead review.

## active capabilities

- Research/Evidence Classification
- Evidence Confidence Assessment
- Analytical Reasoning
- Professional Analysis
- Professional Communication
- Architecture Review
- Engineering Review for repository documentation, validation, scripts, and
  changed canonical surfaces
- Knowledge Evolution and stale-knowledge challenge
- Domain Knowledge Pack Standard

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

- Rationale: mission defines repository, governing documents, release goal,
  research source expectations, deliverables, constraints, validation, and
  success criteria.
- Production may start: yes

## editorial decision frame

- Chosen editorial route: research authoritative architecture practice,
  synthesize a bounded domain-context shape, implement one canonical Software
  Architecture Domain Knowledge Pack, validate against representative
  scenarios, and package the release for Project Lead review.
- Why this route serves the task: it creates the first real domain pack while
  preserving S4.R1 boundaries and reusing Architecture Review and Engineering
  Review instead of duplicating them.
- Alternatives considered:
  - Alternative route, one line: create an Architecture Expert role or
    architecture pipeline.
    - Why rejected, one line: forbidden by release constraints and unnecessary
      because packs are context packages.
  - Alternative route, one line: expand `kb/architecture_review.md` with all
    software architecture domain content.
    - Why rejected, one line: Architecture Review owns review moves; the pack
      owns source-backed domain context consumed by existing capabilities.
  - Alternative route, one line: create a broad software engineering knowledge
    pack.
    - Why rejected, one line: too broad for activation boundaries and would
      blur Engineering Review, DevSecOps, AI Engineering, and Cybersecurity.
  - Alternative route, one line: make only a source register with no practical
    guidance.
    - Why rejected, one line: the release goal requires practical architectural
      judgment, not a bibliography.
- Writer contract:
  - Result type: canonical candidate Domain Knowledge Pack plus release
    research, synthesis, validation, report, and release pack.
  - Angle or reader path: help future agents know when software architecture
    context matters, what questions to ask first, what sources support durable
    guidance, and where the pack stops.
  - Scope boundary: software architecture domain context for
    architecture-sensitive tasks; no policy, capability, role, pipeline, or
    mandatory artifact rules.
  - Must include: required pack sections from the Domain Knowledge Pack
    Standard plus user-required sections.
  - Must not include: unsourced best-practice commands, universal architecture
    prescriptions, cloud-provider-specific mandates, or lifecycle/governance
    instructions.
  - Source boundary and confidence: use authoritative sources; mark claims as
    high, medium, or limited confidence based on source class and freshness.
- Review focus: pack-standard completeness, source support, activation
  boundaries, relation to Architecture Review and Engineering Review,
  forbidden architecture drift, scenario validation, `/about` disposition, and
  release-pack readiness.
- Reroute triggers: evidence shows the pack cannot be useful without a new role
  or capability; source support is too weak; scenario validation fails
  activation or non-activation boundaries.

## custom workflow mini-contract

- Deviation: use a release mini-contract over the research pipeline because the
  repository has no separate release pipeline.
- Reason: releases combine research, synthesis, canonical writing, validation,
  review, and governance.
- Owner: `chief_editor`
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | `chief_editor` | yes | Mission routing and constraints |
| Research | `research_agent` | yes | Source landscape |
| Architecture synthesis | `chief_editor` | yes | Pack placement and boundaries |
| Writing/implementation | `writer_agent` | yes | Pack and release docs |
| Review | `review_agent` | yes | Independent release review |
| Finalization | `final_editor` | yes | Final deliverable pointer |
| Final governance | `chief_editor` | yes | Release candidate decision |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Mission scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../research/software_architecture_pack_landscape.md` | required | synthesis/review | Research evidence |
| `../../research/software_architecture_pack_architecture_synthesis.md` | required | writing/review | Architecture decisions |
| `../../kb/software_architecture_domain_pack.md` | required | future pack activation | Candidate canonical pack |
| `/about` files | conditional | external memory | Sync if canonical changes require |
| `../../research/software_architecture_pack_release_report.md` | required | Project Lead | Release report and validation |
| `../../releases/S4-R2/release-pack.md` | required | Project Lead | Release readiness |
| `review.md` | required | Chief Editor | Independent review |
| `final.md` | required | User/Project Lead | Deliverable pointer |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Mission and governing docs | Task trace | Route established |
| 2 | `research_agent` | External and internal sources | Research landscape | Research sufficiency |
| 3 | `chief_editor` | Research and standards | Architecture synthesis | Pack shape approved |
| 4 | `writer_agent` | Synthesis | Candidate pack and integration docs | Release candidate drafted |
| 5 | `writer_agent` | Candidate pack and scenarios | Validation, release report, release pack | Review-ready packet |
| 6 | `review_agent` | Release packet | `review.md` | Verdict recorded |
| 7 | `final_editor` | Approved review | `final.md` | Final pointer complete |
| 8 | `chief_editor` | Review/final/validation | `final_decision.md` | Release candidate ready |

## review requirements

- Review artifact: `review.md`
- Review depth: full release review
- Reviewer independence requirement: reviewer separate from `writer_agent`
  production role.
- Claims/evidence checks required: source-backed pack, pack-standard
  completeness, activation and non-activation boundaries, architecture
  preservation, scenario validation, canonical owner placement, `/about` sync,
  validation scripts, release pack completeness.

## human approval requirements

- Required: no before local release candidate.
- Approval owner: Project Lead after delivery.
- Evidence needed: completed release pack, validation results, final
  governance decision.
- Cannot proceed past: Project Lead acceptance without user decision.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Pack becomes Architecture Review replacement | capability drift | `chief_editor` | Explicit relation to `kb/architecture_review.md` |
| Pack becomes Engineering Review replacement | capability drift | `chief_editor` | Boundary against implementation/change safety ownership |
| Source-backed guidance becomes universal prescription | quality risk | `research_agent` | Confidence limits and source register |
| Cloud frameworks dominate general architecture guidance | scope distortion | `writer_agent` | Separate cloud-specific guidance from general principles |
| Pack over-activates on incidental architecture terms | process bloat | `review_agent` | Scenario validation and activation boundaries |

## escalation conditions

- Stop or escalate if the pack cannot satisfy success criteria without a new
  role, capability, framework, pipeline, lifecycle stage, review gate,
  mandatory ordinary artifact, policy owner, or capability owner.

## completion criteria

- Required artifacts complete.
- Pack follows Domain Knowledge Pack Standard.
- Pack implemented without forbidden architecture changes.
- Validation passes against representative scenarios.
- Independent review outcome is approved.
- Repository validation passes.
- `/about` synchronized if required.
- Release pack complete.
- Final governance decision says ready for Project Lead review.
