# Orchestration Plan

## task summary

- Task ID: `TASK-PROFESSIONAL-COMMUNICATION-RELEASE`
- User goal: complete backlog release `S3.R5 - Professional Communication`.
- Deliverable: research, architecture synthesis, implemented capability docs,
  validation, `/about` sync if required, release report, and release pack.
- Audience/channel: Project Lead architectural review.
- Current active version: release candidate artifacts listed in manifest.

## task classification

- Task type: system capability release
- Risk mode: `standard`
- Factual sensitivity: medium; professional communication claims need
  authoritative source grounding.
- Human approval likely required: after delivery, for architectural acceptance.
- Rationale: canonical documentation may change, but architecture is frozen and
  changes must remain bounded.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: mission spans research, synthesis, canonical docs, validation,
  `/about`, release report, and release pack.
- Forbidden depth shortcuts: no direct implementation without research and
  synthesis; no review bypass; no new roles/pipelines/stages; no duplicate
  framework ownership.

## selected pipeline

- Pipeline: `research`
- Why this pipeline: release requires source-backed research before capability
  documentation and independent review.
- Pipeline exceptions or local constraints: implementation and final
  governance are included as release steps under the existing lifecycle; no new
  pipeline is created.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable.
- Non-activation reason: no client-owned content.
- Stop condition: any attempt to apply client-specific policy.

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

- Rationale: mission defines repository, governing documents, phases,
  deliverables, constraints, validation, and deliver-back requirements.
- Production may start: yes

## editorial decision frame

- Chosen editorial route: research and synthesize one bounded Professional
  Communication shared capability; implement only if it can complement existing
  capabilities without overlap.
- Why this route serves the task: communication skill can improve executive,
  technical, recommendation, explanation, and action-oriented artifacts while
  preserving current roles and lifecycle.
- Alternatives considered:
  - Alternative route, one line: create a Professional Communicator role.
    - Why rejected, one line: role architecture is frozen and communication is
      shared across existing roles.
  - Alternative route, one line: expand Writer Agent or UX Writer only.
    - Why rejected, one line: professional communication also affects routing,
      research handoff, review, finalization, and decision artifacts.
  - Alternative route, one line: fold all communication into Audience Alignment
      or Quality Attributes.
    - Why rejected, one line: those frameworks name reader/outcome and quality
      priorities but do not own message architecture, explanation, density, or
      recommendation presentation.
- Writer/implementation contract:
  - Result type: research, synthesis, canonical capability docs, tests, memory
    sync, release report, release pack.
  - Scope boundary: Professional Communication release only.
  - Must include: boundaries with Writer, UX Writer, Audience Alignment,
    Quality Attributes, Analytical Reasoning, and Professional Analysis;
    activation rules; review challenge; validation.
  - Must not include: grammar/style ownership, new roles, pipelines, lifecycle
    stages, mandatory artifacts, framework redesign, redaction-path edits.
  - Source boundary and confidence: use primary or authoritative sources for
    professional communication practice.
- Review focus: architecture preservation, non-overlap with existing
  capabilities, source support, correct `/about` sync, validation completeness,
  and release-pack standard.
- Reroute triggers: research shows Professional Communication duplicates an
  existing canonical owner completely, requires role-model change, or cannot be
  bounded.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Mission routing |
| Research | `research_agent` | yes | Professional communication research |
| Planning/synthesis | `chief_editor` | yes | Architecture decisions |
| Writing/implementation | `writer_agent` | yes | Documentation update production |
| Review | `review_agent` | yes | Independent release review |
| Finalization | `final_editor` | no | Final artifact is release packet; no transformation expected |
| Final governance | `chief_editor` | yes | Final decision |

## required knowledge and evidence

- Required project files:
  - `../../AGENTS.md`
  - `../../ROADMAP.md`
  - `../../BACKLOG.md`
  - `../../project-state.md`
  - `../../kb/capability_registry.md`
  - `../../kb/audience_outcome_alignment.md`
  - `../../kb/editorial_quality_attributes.md`
  - `../../kb/professional_analysis.md`
  - `../../agents/chief_editor.md`
  - `../../agents/review_agent.md`
  - `../../pipelines/review_pipeline.md`
- Required external evidence: authoritative sources for executive
  communication, technical writing, engineering communication, policy memo
  writing, scientific communication, documentation practice, plain language,
  recommendation presentation, explanation, and decision-oriented writing.
- Evidence gaps: none known before research.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Mission scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../research/professional_communication_landscape.md` | required | synthesis/review | Research |
| `../../research/professional_communication_architecture_synthesis.md` | required | implementation/review | Decisions |
| `../../kb/professional_communication.md` | conditional | canonical users | Capability doc if synthesis approves |
| canonical integration patches | conditional | active roles | Needed for discoverability and review |
| `/about` files | conditional | memory package | Sync copied files if changed |
| `../../tests/professional_communication_smoke_test.md` | conditional | review/release | Activation and non-overlap validation |
| `../../research/professional_communication_release_report.md` | required | Project Lead | Release report |
| `../../releases/S3-R5/release-pack.md` | required | Project Lead | Release readiness standard |
| `review.md` | required | Chief Editor | Independent review |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Mission and governing docs | Task trace | Route established |
| 2 | `research_agent` | External and internal sources | Research landscape | Research complete |
| 3 | `chief_editor` | Research and roadmap/backlog | Architecture synthesis | Capability decisions made |
| 4 | `writer_agent` | Synthesis | Canonical docs, tests, memory sync | Release candidate implemented |
| 5 | `review_agent` | Release candidate | `review.md` | Verdict recorded |
| 6 | `chief_editor` | Review and validation | `final_decision.md` | Release candidate ready |

## review requirements

- Review artifact: `review.md`
- Review depth: full release review
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: source-backed research, non-overlap with
  existing capabilities, architecture boundary, validation evidence, release
  pack completeness.
- Optional review artifacts justified: no; release report, release pack, and
  review are sufficient.

## human approval requirements

- Required: no before local release candidate commit.
- Approval owner: Project Lead after delivery.
- Evidence needed: completed release pack, validation results, final commit.
- Cannot proceed past: Project Lead acceptance without user decision.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Capability duplicates Audience Alignment | architecture drift | `chief_editor` | Make audience identification/outcome fit stay in existing framework |
| Capability duplicates Writer or UX Writer | role confusion | `chief_editor` | Define Professional Communication as shared message architecture, not drafting ownership |
| Capability becomes grammar/style checklist | scope dilution | `review_agent` | Explicit non-goal and activation boundaries |
| Capability overlaps Professional Analysis | duplicate recommendation ownership | `chief_editor` | Separate analytical product shape from presentation and reader transfer |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if Professional Communication cannot be implemented without
  a new role, pipeline, lifecycle stage, review gate, mandatory artifact, or
  duplicate canonical owner.

## completion criteria

- Required artifacts complete.
- Capability integrated without architecture redesign.
- Review outcome approved.
- Validation passed.
- `/about` synchronized if required.
- Release pack complete.
- Final commit created.

## finalization conditions

- Finalization may start when independent review approves the release
  candidate and validation passes.
- Finalization must stop when review blocks or validation exposes incoherence.
- Compact finalization shape allowed: no, because this is a full release.
- Conditional finalization artifacts needed: `final.md` and
  `final_decision.md`; no separate checklist unless review requires one.

## restart notes

- Minimum read set: `brief.md`, `task-manifest.md`, `orchestration_plan.md`,
  `status.md`, latest handoff if present, current working artifact.
- Current active version: manifest-listed release artifacts.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
