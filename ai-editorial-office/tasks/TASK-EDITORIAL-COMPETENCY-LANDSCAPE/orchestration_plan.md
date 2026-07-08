# Orchestration Plan

## task summary

- Task ID: TASK-EDITORIAL-COMPETENCY-LANDSCAPE
- User goal: produce a research report on competencies for a best-in-class AI
  Editorial Office.
- Deliverable: `ai-editorial-office/research/editorial_competency_landscape.md`
- Audience/channel: project lead, repository-local research artifact.
- Current active version: `ai-editorial-office/research/editorial_competency_landscape.md`

## task classification

- Task type: research
- Risk mode: standard
- Factual sensitivity: medium
- Human approval likely required: no
- Rationale: the report is design research, not canon or implementation work,
  but it relies on professional-source claims and will influence future system
  design.

## process depth

- Depth: full
- Execution profile: expanded
- Rationale: broad cross-domain scope, source-backed synthesis, and later
  architecture relevance require explicit source notes and independent review.
- Forbidden depth shortcuts: no direct canon edits; no role, pipeline, or
  project-state changes; no implementation tasks.
- Expanded profile trigger: wide source landscape and required competency,
  artifact, failure-mode, and architecture-note coverage.

## selected pipeline

- Pipeline: `research_pipeline.md`
- Why this pipeline: the task asks for evidence gathering and synthesis, not
  drafting publishable copy or implementation.
- Pipeline exceptions or local constraints: main report is saved at the
  user-requested research path; task-local process artifacts stay in this task
  folder.

## client profile

- Client profile: none
- Client profile status: not_applicable
- Activation reason: not applicable
- Non-activation reason: independent research task, not Sber-owned or
  Sber-style communication.
- Client-profile files: none
- Stop condition: any attempt to apply client policy or change canon.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | confirmed |
| Channel or context | confirmed |
| Deliverable | defined |
| Source boundary | defined |
| Success criterion | defined |
| Approval boundary | defined |
| Missing data strategy | proceed |

- Rationale: the user supplied detailed structure, constraints, validation, and
  deliver-back requirements.
- Production may start: yes
- If `ask`: not applicable
- If `constrain`: research only; preliminary architecture notes are explicitly
  not final decisions.
- If `block`: not applicable

## editorial decision frame

- Chosen editorial route: broad comparative research synthesis organized by
  competency, domain, heuristic, artifact, failure mode, and preliminary
  architecture note.
- Why this route serves the task: the next modernization stage is
  competency-based, so the artifact must make competencies and their supporting
  practices explicit before any architecture design.
- Alternatives considered:
  - Domain-by-domain literature review only.
    - Rejected because it would bury the competency map needed for later design.
  - Immediate architecture proposal.
    - Rejected because the user explicitly forbids canon changes and asks for
      research only.
  - Short benchmark memo.
    - Rejected because the requested report needs concrete artifacts, failure
      modes, and source notes across many domains.
- Writer/UX Writer contract: not assigned; this is a research deliverable.
- Review focus: structure compliance, source quality, concrete usefulness,
  forbidden-change compliance, and preliminary-note boundary.
- Reroute triggers: source gaps that prevent reliable synthesis; accidental
  canon modification; unsupported implementation recommendation.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | chief_editor | yes | Route task and set boundaries. |
| Research | research_agent | yes | Collect and synthesize evidence. |
| Writing/UX writing | none | no | Research artifact only. |
| Review | review_agent | yes | Independent check before delivery. |
| Finalization | none | no | No publication copy or canon finalization. |
| Final governance | chief_editor | no | Not changing system canon. |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `research_pipeline.md`,
  `research_evidence.md`, `task_statuses.md`.
- Required source/evidence files: external source notes embedded in the report.
- Evidence gaps: consulting methods include some book/proprietary practice
  references; report labels them as practice synthesis and prioritizes public
  authoritative sources where possible.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Captures user scope and constraints. |
| `task-manifest.md` | required | all roles | Restart pointer and artifact inventory. |
| `status.md` | required | all roles | State and validation trail. |
| `orchestration_plan.md` | required | all roles | Routing and boundary contract. |
| `editorial_competency_landscape.md` | required | project lead | Main research report at requested path. |
| `review.md` | required before delivery | chief_editor / user | Independent review trail. |
| `sources.md` | omitted | review_agent | Source notes are embedded in the report. |
| `facts.md` | omitted | review_agent | The report is synthesis, not claim-by-claim factual reuse. |
| `claims_table.md` | omitted | review_agent | Major claims are tied to source notes in the report. |
| `open-questions.md` | omitted | chief_editor | No blocking questions. |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user request, AGENTS, pipeline | brief, manifest, plan, status | research may start |
| 2 | research_agent | authoritative sources | research report | requested structure complete |
| 3 | review_agent | report and task constraints | review.md | approved or changes requested |
| 4 | chief_editor | diff and validation | status update and commit | only allowed files committed |

## status transitions

- Starting status: intake
- Next expected status: research, then review, then approved
- Status owner: chief_editor for transitions; research_agent and review_agent
  for stage outcomes.
- Status update trigger: artifact creation, review completion, validation.

## review requirements

- Review artifact: `review.md`
- Review depth: standard, with constraint and source-quality checks.
- Reviewer independence requirement: review_agent distinct from research_agent
  in recorded role boundary.
- Claims/evidence checks required: source notes sufficient for major domain
  claims; unsupported implementation decisions must be absent.
- Optional review artifacts justified: no.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Accidentally designing canon changes | Violates user scope | chief_editor | Keep architecture section preliminary. |
| Generic competency labels | Low usefulness | research_agent | Include artifacts, heuristics, failure modes, and domain practices. |
| Weak source quality | Poor design basis | research_agent | Prefer standards, handbooks, official docs, and recognized professional bodies. |
| Dirty pre-existing files included in commit | Scope contamination | chief_editor | Stage only this task's files and verify diff scope. |

## unresolved questions

- None.

## escalation conditions

- Stop or escalate if a required source cannot be accessed and no authoritative
  substitute exists for a required domain.
- Stop if any task step requires modifying canon, agents, pipelines,
  project-state, `/about`, `diff_intake.md`, or the legacy repository.

## completion criteria

- Required artifacts complete: yes after report and review.
- Review outcome acceptable: approved.
- Blockers resolved: yes.
- Governance fields complete: yes for research delivery.

## restart notes

- Minimum read set: this plan, `task-manifest.md`, `status.md`,
  `ai-editorial-office/research/editorial_competency_landscape.md`, `review.md`.
- Current active version: `ai-editorial-office/research/editorial_competency_landscape.md`
- Deprecated/previous versions: none.
- Latest relevant handoff: none.
