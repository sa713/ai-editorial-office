# Orchestration Plan

## task summary

- Task ID: `TASK-ENGINEERING-REVIEW-RELEASE`
- User goal: complete Engineering Review roadmap stage as one coherent release.
- Deliverable: research, synthesis, implemented capability docs, validation,
  `/about` sync, and release report.
- Audience/channel: Project Lead architectural review.
- Current active version: release candidate artifacts listed in manifest.

## task classification

- Task type: system capability release
- Risk mode: `standard`
- Factual sensitivity: medium; engineering review claims need source-backed
  professional framing.
- Human approval likely required: after delivery, for architectural acceptance.
- Rationale: canonical documentation may change, but architecture is frozen and
  changes must be bounded.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: mission spans research, synthesis, canonical docs, `/about`, and
  release report.
- Forbidden depth shortcuts: no direct implementation without research and
  synthesis; no review bypass; no new roles/pipelines/stages.
- Expanded profile trigger, if any: already active due release scope.

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
- Activation reason: not applicable
- Non-activation reason: no client-owned content.
- Client-profile files: none
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
- If `constrain`: constrain to Engineering Review only; ignore later roadmap
  stages.

## editorial decision frame

- Chosen editorial route: one Engineering Review capability with internal
  lenses, unless research proves separate capabilities are necessary.
- Why this route serves the task: it optimizes for architectural quality,
  minimum complexity, and existing role/capability architecture.
- Alternatives considered:
  - Alternative route, one line: implement one capability per competency.
    - Why rejected, one line: risks capability sprawl and duplicates review
      ownership.
  - Alternative route, one line: only create research and postpone all
      implementation.
    - Why rejected, one line: user requested complete release candidate with
      implemented capability documentation.
  - Alternative route, one line: change role or pipeline architecture.
    - Why rejected, one line: architecture is frozen.
- Writer/implementation contract:
  - Result type: research, synthesis, canonical capability docs, synced memory,
    release report.
  - Scope boundary: Engineering Review stage only.
  - Must include: competency decisions, merged/postponed/rejected rationale,
    activation boundaries, validation, release report.
  - Must not include: new roles, pipelines, lifecycle stages, mandatory
    artifacts, framework redesign, redaction-path edits.
  - Source boundary and confidence: use existing research plus primary
    professional sources for engineering review areas.
- Review focus: architecture preservation, capability minimalism, source
  support, correct `/about` sync, validation completeness.
- Reroute triggers: research shows Engineering Review duplicates Architecture
  Review completely, requires role-model change, or cannot be bounded.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Mission routing |
| Research | `research_agent` | yes | Professional competency research |
| Planning/synthesis | `chief_editor` | yes | Architecture decisions |
| Writing/implementation | `writer_agent` | yes | Documentation update production |
| Review | `review_agent` | yes | Independent release review |
| Finalization | `final_editor` | no | Final artifact is release report; no transformation expected |
| Final governance | `chief_editor` | yes | Final decision |

## required knowledge and evidence

- Required project files:
  - `../../AGENTS.md`
  - `../../ROADMAP.md`
  - `../../project-state.md`
  - `../../research/engineering_review_execution_plan.md`
  - `../../kb/capability_registry.md`
  - `../../kb/codex_task_standard.md`
  - `../../kb/architecture_review.md`
  - `../../agents/chief_editor.md`
  - `../../agents/review_agent.md`
- Required external evidence: primary professional sources for code review,
  security, configuration, CI/CD, infrastructure, API, observability,
  reliability, database, performance, and DevSecOps.
- Evidence gaps: none known before research.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Mission scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../research/engineering_review_competency_landscape.md` | required | synthesis/review | Research |
| `../../research/engineering_review_architecture_synthesis.md` | required | implementation/review | Decisions |
| `../../kb/engineering_review.md` | conditional | canonical users | Capability doc if approved |
| canonical integration patches | conditional | active roles | Needed only where capability must be discoverable |
| `/about` files | conditional | memory package | Sync copied files and summaries |
| `../../research/engineering_review_release_report.md` | required | Project Lead | Release report |
| `review.md` | required | Chief Editor | Independent review |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Mission and governing docs | Task trace | Route established |
| 2 | `research_agent` | Existing and external sources | Research landscape | Competencies covered |
| 3 | `chief_editor` | Research and execution plan | Architecture synthesis | Capability decisions made |
| 4 | `writer_agent` | Synthesis | Canonical docs and memory sync | Release candidate implemented |
| 5 | `review_agent` | Release candidate | `review.md` | Verdict recorded |
| 6 | `chief_editor` | Review and validation | `final_decision.md` | Release candidate ready |

## review requirements

- Review artifact: `review.md`
- Review depth: full release review
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: source-backed research, competency decision
  rationale, architecture boundary, validation evidence.
- Optional review artifacts justified: no; release report and review are
  sufficient.
