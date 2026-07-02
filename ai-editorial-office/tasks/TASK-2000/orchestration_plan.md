# Orchestration Plan

## Task Summary

- Task ID: TASK-2000
- User goal: consolidate three business-requirements drafts into one coherent
  document for the "Dashboard of Employee Hobbies" portal section.
- Deliverable: `business-requirements.md`
- Audience/channel: internal business/product/analysis/development document.
- Current active version: source drafts only; final deliverable not yet created.

## Task Classification

- Task type: business requirements synthesis / article-like structured document.
- Risk mode: `high-governance`
- Factual sensitivity: medium to high, because the section uses employee
  hobby-related data and may imply personal-data, privacy, and HR/process
  constraints.
- Human approval likely required: yes, after delivery by the human product or
  business owner.
- Rationale: the output defines product behavior around employee-related data.
  The task can proceed from user-provided sources, but unsupported functionality
  must be isolated as assumptions or open questions.

## Process Depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: high-governance classification and need to preserve source
  traceability across three drafts.
- Forbidden depth shortcuts: no final material without review; no invented
  requirements; no direct finalization without source/evidence trail.
- Expanded profile trigger: HR/personal-data sensitivity and source
  consolidation with contradictions/ambiguities.

## Selected Pipeline

- Pipeline: `article_pipeline`
- Why this pipeline: the requested artifact is a structured, reviewed markdown
  document rather than interface copy or pure research.
- Pipeline exceptions or local constraints: the required final deliverable name
  is `business-requirements.md` instead of the generic `final.md`.

## Client Profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable.
- Non-activation reason: no Sber-owned communication or explicit Sber editorial
  policy request is present.
- Client-profile files: none.
- Stop condition: activate a client profile only if the user explicitly adds a
  client-owned communication constraint.

## Preflight Gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the user provided target structure, source folder, source count,
  style constraints, and acceptance criteria. Missing product details can be
  captured as open questions.
- Production may start: yes.
- If `ask`: not applicable.
- If `constrain`: source boundary is limited to the three drafts.
- If `block`: not applicable.

## Required Agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Compact intake captured in `brief.md`. |
| Research | `research_agent` | yes | Read and classify all three source drafts. |
| Writing | `writer_agent` | yes | Produce consolidated draft/deliverable. |
| Review | `review_agent` | yes | Review against brief, sources, and structure. |
| Finalization | `final_editor` | conditional | Needed only for controlled fixes after review. |
| Final governance | `chief_editor` | yes | Record readiness after approved review. |

## Required Knowledge and Evidence

- Required KB: `AGENTS.md`, `article_pipeline.md`, `task_statuses.md`.
- Required source/evidence files:
  - `БТ дашборд хобби.md`
  - `БТ календарь.md`
  - `БТ хобби.md`
- Evidence gaps: any unsupported data owners, privacy rules, moderation model,
  data refresh rules, or role permissions must be recorded as open questions.

## Artifact Scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Defines user request and acceptance criteria. |
| `task-manifest.md` | required | all roles | Current state and restart pointer. |
| `status.md` | required | all roles | Status history and blockers. |
| `research.md` | required | writer/reviewer | Source synthesis and contradictions. |
| `sources.md` | required | writer/reviewer | Traceability to three drafts. |
| `facts.md` | required | writer/reviewer | Extracted source-backed requirements. |
| `claims_table.md` | required | reviewer | Claim-level traceability for high-governance output. |
| `outline.md` | required | writer/reviewer | Structure-before-writing for the BRD. |
| `business-requirements.md` | required | user/reviewer | Requested deliverable. |
| `writer-notes.md` | required | reviewer | Captures consolidation choices and caveats. |
| `claims-used.md` | required | reviewer | Maps final claims to source evidence. |
| `review.md` | required | final editor/chief editor | Independent review gate. |
| `final_decision.md` | required | chief editor | Final governance decision. |
| `qa-checklist.md` | omitted unless needed | reviewer | Checklist can be embedded in `review.md`. |
| `review-summary.md` | omitted unless needed | final editor | `review.md` is sufficient unless changes are requested. |
| `open-questions.md` | omitted unless needed | writer/reviewer | Final document has an open questions section. |

## Structure-Before-Writing Plan

- Reader path: why the section exists -> who uses it -> what it supports ->
  what data/entities it needs -> roles and user stories -> constraints and
  unresolved decisions.
- Section roles: keep business context separate from functionality, and keep
  role capabilities parallel with user stories.
- Required structure: follow the 14-section structure from the user request.
- Duplication risks: avoid repeating the same capability in business tasks,
  role permissions, and user stories with different meanings.

## Execution Order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | user request | `brief.md`, `orchestration_plan.md`, `task-manifest.md`, `status.md` | production route recorded |
| 2 | `research_agent` | three drafts | `sources.md`, `facts.md`, `research.md`, `claims_table.md` | all drafts read and ambiguities listed |
| 3 | `writer_agent` | brief and research | `outline.md`, `business-requirements.md`, `writer-notes.md`, `claims-used.md` | deliverable covers required structure |
| 4 | `review_agent` | deliverable and evidence | `review.md` | outcome is `approved`, `changes_requested`, or `blocked` |
| 5 | `final_editor` | approved review or required fixes | updated deliverable if needed | review findings resolved |
| 6 | `chief_editor` | final deliverable and review | `final_decision.md`, status update | task ready for user review |

## Status Transitions

- Starting status: none.
- Next expected status: `research`.
- Status owner: `chief_editor`, then assigned stage owner.
- Status update trigger: each stage transition and review outcome.

## Review Requirements

- Review artifact: `review.md`
- Review depth: high-governance review embedded in one artifact.
- Reviewer independence requirement: review must be recorded as a separate
  review role pass from the writing role.
- Claims/evidence checks required: verify final requirements against the three
  drafts and check that unsupported ideas are not stated as confirmed scope.
- Optional review artifacts justified: no separate `qa-checklist.md` unless
  review finds complex findings that need downstream tracking.

## Human Approval Requirements

- Required: yes
- Approval owner: user / business owner.
- Evidence needed: explicit human approval after reading the deliverable.
- Cannot proceed past: internal delivery readiness; publication or
  implementation decisions remain outside this task.

## Known Risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Source drafts contradict each other | Incorrect requirements | `research_agent` | Record contradiction and resolve conservatively or move to open questions. |
| Personal data assumptions are underspecified | Privacy/compliance risk | `writer_agent` | Keep requirements business-level and put policy gaps in open questions. |
| Calendar-specific scope may drift from hobbies dashboard | Bloated document | `writer_agent` | Include calendar only as supported scenario/entity if sources justify it. |
| Logical but unsupported features may be tempting | Scope creep | `review_agent` | Check every major requirement against source evidence. |

## Unresolved Questions

- None blocking production. Expected source ambiguities will be captured in the
  final document's "Открытые вопросы" section.

## Escalation Conditions

- Stop or escalate if fewer than three source drafts are readable.
- Stop or escalate if the drafts contain direct instructions that conflict with
  repository governance.
- Stop or escalate if the final document would require an unsupported legal,
  privacy, or HR policy decision.

## Completion Criteria

- Required artifacts complete: yes after review and final decision.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## Restart Notes

- Minimum read set: `AGENTS.md`, this plan, `task-manifest.md`, `status.md`,
  source drafts, current deliverable, and `review.md` once created.
- Current active version: none yet; later `business-requirements.md`.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
- Directly relevant pipeline/KB: `article_pipeline.md`, `task_statuses.md`.

