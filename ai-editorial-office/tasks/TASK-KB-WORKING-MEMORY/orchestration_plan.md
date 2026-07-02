# Orchestration Plan

Task ID: `TASK-KB-WORKING-MEMORY`
Owner: `chief_editor`
Date: 2026-07-02

## task summary

- User goal: turn the Knowledge Base into working memory by recording how knowledge is applied inside AI Software Studio.
- Deliverable: updated KB schema/model/navigation plus representative record updates and recommendations.
- Audience/channel: internal AI Software Studio roles.
- Current active version: v1 KB working-memory extension.

## task classification

- Task type: system KB architecture/documentation update.
- Risk mode: `high-governance`
- Factual sensitivity: medium-high for internal governance consistency.
- Human approval likely required: no for local documentation changes; yes for future binding adoption as Studio policy.
- Rationale: schema/lifecycle changes affect future role behavior and must preserve governance boundaries.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: user requested schema, lifecycle, coverage, representative record updates, recommendations, and consistency verification.
- Forbidden depth shortcuts: no direct finalization without review; no undocumented schema changes; no invented BRD/Historian policy.
- Expanded profile trigger: KB governance and future role usage.

## selected pipeline

- Pipeline: `/pipelines/research_pipeline.md` as source/context study plus custom KB update mini-contract, then writing, review, finalization, and Chief Editor governance.
- Why this pipeline: task depends on local source/context study and then produces reusable documentation.
- Pipeline exceptions or local constraints: no web research; no external factual source expansion; no all-record migration requirement.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Rationale: required local context is available enough to proceed; missing BRD/Historian files are a documented gap, not a blocker.
- Production may start: yes.
- If `constrain`: do not invent BRD Governance or Historian policy; model references those objects generically until canonical owners exist.

## editorial decision frame

- Chosen editorial route: extend the existing KB with an application layer, lifecycle, object-link model, coverage model, and representative record examples.
- Why this route serves the task: it preserves the current KB structure while adding working-memory capability.
- Alternatives considered:
  - Rewrite all 55 records now.
    - Why rejected: high churn and lower readability; user allowed representative updates.
  - Create a separate implementation-history log inside KB.
    - Why rejected: violates user constraint; history belongs to Historian/status/handoff.
  - Add only fields to schema without a register.
    - Why rejected: would not answer coverage questions across the KB.
- Writer/UX Writer contract:
  - Result type: KB model documentation and representative record updates.
  - Angle or reader path: "how knowledge moves from accepted idea to Studio working memory."
  - Scope boundary: KB application memory only, not Studio audit or process redesign.
  - Must include: lifecycle, application fields, object links, coverage, applied/not-applied/rejected support, recommendations.
  - Must not include: implementation history journal, invented BRD/Historian policy, mandatory all-record rewrite.
  - Source boundary and confidence: local repository sources only; missing files explicitly caveated.
- Review focus: schema consistency, no contradictions, no journal drift, representative examples, coverage model, user criteria.
- Reroute triggers: missing canonical source causes conflict; application model duplicates status/handoff; schema becomes unreadable.

## custom workflow mini-contract

- Deviation: KB docs and representative records are edited directly after local context study rather than producing a publishable `draft.md`.
- Reason: the deliverable is the KB itself, plus task-local documentation for review.
- Owner: `chief_editor` for routing; `writer_agent` for implementation/reporting; `review_agent` for independent review.
- Review gate preserved: yes.
- Governance model unchanged: yes.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/orchestration | `chief_editor` | yes | Route and constraints. |
| Research/context study | `chief_editor` / `research_agent` function | yes | Local source/context study only. |
| Writing/KB update | `writer_agent` | yes | Update KB docs and representative records. |
| Review | `review_agent` | yes | `review.md` required. |
| Finalization | `final_editor` | yes | `final.md` after approved review. |
| Final governance | `chief_editor` | yes | `final_decision.md`. |

## required knowledge and evidence

- Required KB:
  - KB `index.md`, `schema.md`, `navigation.md`, `source-register.md`.
  - Representative records across existing types.
  - `AGENTS.md`, `project-state.md`, artifact templates, task status model.
- Required source/evidence files:
  - `context-study.md`
  - changed KB files and records
  - `implementation-report.md`
- Evidence gaps:
  - No dedicated BRD Governance file found.
  - No dedicated Historian file found.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Current state pointer. |
| `status.md` | required | all roles | State/history. |
| `orchestration_plan.md` | required | all roles | Route and local mini-contract. |
| `context-study.md` | required | review_agent | Shows required local context was studied. |
| `implementation-report.md` | required | review_agent, user | Explains changes without bloating KB files. |
| `review.md` | required | final_editor/chief_editor | Independent check. |
| `final.md` | required after review | user/chief_editor | Delivery summary. |
| `qa-checklist.md` | omitted | n/a | Embedded review checklist is sufficient. |
| `open-questions.md` | omitted | n/a | No blocking questions. |

## structure-before-writing plan

- Reader path:
  1. KB `index.md`.
  2. `schema.md`.
  3. `application-model.md`.
  4. `lifecycle.md`.
  5. `application-register.md`.
  6. `coverage-model.md`.
  7. representative records.
- Section roles:
  - schema defines required/optional fields;
  - application model defines object linking;
  - lifecycle defines status governance;
  - register maps all records to application status;
  - coverage model aggregates.
- Duplication risks: avoid repeating full lifecycle in every record.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User brief, AGENTS, project-state, KB files | Task artifacts | Route recorded |
| 2 | writer_agent | Context study, KB files | KB application model docs | Schema/model complete |
| 3 | writer_agent | Existing records | Representative record updates | Applied/not-applied/rejected examples present |
| 4 | writer_agent | KB changes | `implementation-report.md` | Review-ready package |
| 5 | review_agent | Full package | `review.md` | Approved or bounded changes |
| 6 | final_editor | Approved package | `final.md` | Ready for governance |
| 7 | chief_editor | `review.md`, `final.md` | `final_decision.md` | Finalized |

## status transitions

- Starting status: `planning`
- Next expected status: `writing`
- Status owner: `chief_editor`
- Status update trigger: model implementation starts, handoff created, review outcome, finalization, final decision.

## review requirements

- Review artifact: `review.md`
- Review depth: full
- Reviewer independence requirement: reviewer did not create KB changes.
- Claims/evidence checks required: local-source claims and missing-source caveats.
- Optional review artifacts justified: no separate checklist unless review finds complexity.

## human approval requirements

- Required: no for this local KB update.
- Approval owner: user only for later policy adoption/publication.
- Evidence needed: not applicable.
- Cannot proceed past: not applicable.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| KB becomes implementation journal | Violates user constraint | writer_agent/review_agent | Use current application state, not history. |
| Schema becomes too heavy | Record readability drops | writer_agent | Add compact Application Profile and external register. |
| Missing BRD/Historian files lead to invented rules | Governance drift | chief_editor/review_agent | Record as source gap; support generic links only. |
| Representative updates seem incomplete | User may expect all records migrated | writer_agent | Application register covers all records; representative records show inline model. |

## completion criteria

- Required artifacts complete: yes after finalization.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

