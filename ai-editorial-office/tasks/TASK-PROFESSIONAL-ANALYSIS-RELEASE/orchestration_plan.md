# Orchestration Plan

## task summary

- Task ID: `TASK-PROFESSIONAL-ANALYSIS-RELEASE`
- User goal: complete backlog release `S3.R4 - Professional Analysis`.
- Deliverable: research, synthesis, implemented capability docs, validation,
  `/about` sync, and release report.
- Audience/channel: Project Lead architectural review.
- Current active version: release candidate artifacts listed in manifest.

## task classification

- Task type: system capability release
- Risk mode: `standard`
- Factual sensitivity: medium; professional analysis claims need authoritative
  source grounding.
- Human approval likely required: after delivery, for architectural acceptance.
- Rationale: canonical documentation may change, but architecture is frozen and
  changes must remain bounded.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: mission spans research, synthesis, canonical docs, `/about`, and
  release report.
- Forbidden depth shortcuts: no direct implementation without research and
  synthesis; no review bypass; no new roles/pipelines/stages.

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

- Chosen editorial route: one Professional Analysis capability with optional
  analysis lenses.
- Why this route serves the task: it improves analytical products while
  preserving the current task-object, capability, role, lifecycle, and review
  architecture.
- Alternatives considered:
  - Alternative route, one line: implement one capability per analysis domain.
    - Why rejected, one line: risks capability sprawl and duplicate owners.
  - Alternative route, one line: add an Analyst or Consultant role.
    - Why rejected, one line: role architecture is frozen.
  - Alternative route, one line: fold the release into Analytical Reasoning.
    - Why rejected, one line: Analytical Reasoning owns reasoning moves, not
      analytical product shape.
- Writer/implementation contract:
  - Result type: research, synthesis, canonical capability docs, synced memory,
    release report.
  - Scope boundary: Professional Analysis release only.
  - Must include: capability boundaries, relationship to existing capabilities,
    activation rules, review challenge, validation, release report.
  - Must not include: new roles, pipelines, lifecycle stages, mandatory
    artifacts, framework redesign, roadmap rewrite, redaction-path edits.
  - Source boundary and confidence: use primary or authoritative sources for
    professional analytical practice.
- Review focus: architecture preservation, non-overlap with existing
  capabilities, source support, correct `/about` sync, validation completeness.
- Reroute triggers: research shows Professional Analysis duplicates Analytical
  Reasoning completely, requires role-model change, or cannot be bounded.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Mission routing |
| Research | `research_agent` | yes | Professional analysis research |
| Planning/synthesis | `chief_editor` | yes | Architecture decisions |
| Writing/implementation | `writer_agent` | yes | Documentation update production |
| Review | `review_agent` | yes | Independent release review |
| Finalization | `final_editor` | no | Final artifact is release report; no transformation expected |
| Final governance | `chief_editor` | yes | Final decision |

## required knowledge and evidence

- Required project files:
  - `../../AGENTS.md`
  - `../../ROADMAP.md`
  - `../../BACKLOG.md`
  - `../../project-state.md`
  - `../../kb/capability_registry.md`
  - `../../kb/analytical_reasoning.md`
  - `../../kb/architecture_review.md`
  - `../../kb/engineering_review.md`
  - `../../agents/chief_editor.md`
  - `../../agents/review_agent.md`
- Required external evidence: authoritative sources for business analysis,
  policy appraisal, analytical quality assurance, intelligence analysis,
  decision analysis, product discovery, and technology assessment.
- Evidence gaps: none known after research.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Mission scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../research/professional_analysis_competency_landscape.md` | required | synthesis/review | Research |
| `../../research/professional_analysis_architecture_synthesis.md` | required | implementation/review | Decisions |
| `../../kb/professional_analysis.md` | conditional | canonical users | Capability doc |
| canonical integration patches | conditional | active roles | Needed for discoverability and review |
| `/about` files | conditional | memory package | Sync copied files |
| `../../research/professional_analysis_release_report.md` | required | Project Lead | Release report |
| `review.md` | required | Chief Editor | Independent review |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Mission and governing docs | Task trace | Route established |
| 2 | `research_agent` | External and internal sources | Research landscape | Research complete |
| 3 | `chief_editor` | Research and roadmap/backlog | Architecture synthesis | Capability decisions made |
| 4 | `writer_agent` | Synthesis | Canonical docs and memory sync | Release candidate implemented |
| 5 | `review_agent` | Release candidate | `review.md` | Verdict recorded |
| 6 | `chief_editor` | Review and validation | `final_decision.md` | Release candidate ready |

## review requirements

- Review artifact: `review.md`
- Review depth: full release review
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: source-backed research, non-overlap with
  existing capabilities, architecture boundary, validation evidence.
- Optional review artifacts justified: no; release report and review are
  sufficient.
