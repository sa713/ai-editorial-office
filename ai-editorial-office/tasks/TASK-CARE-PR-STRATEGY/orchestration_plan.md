# Orchestration Plan

## Task Summary

- Task ID: `TASK-CARE-PR-STRATEGY`
- User goal: inspect Care PR brainstorm and independently decide the editorial
  route for further work.
- Deliverable: reviewed strategic memo/action plan.
- Audience/channel: inferred internal strategy document for user, Care lead, or
  Care working group.
- Current active version: `final.md`

## Task Classification

- Task type: article-style strategic action plan
- Risk mode: `high-governance`
- Factual sensitivity: high for claims about team reputation, employee needs,
  internal process quality, and stakeholder perception.
- Human approval likely required: yes before external rollout, no for local task
  artifact delivery.
- Rationale: source contains subjective perceptions and organizational
  implications. The output must preserve uncertainty and avoid turning
  brainstorm observations into official facts.

## Process Depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: internal reputation and operating-model claims require explicit
  source traceability, review, finalization checklist, and approval boundary.
- Forbidden depth shortcuts: no direct source-to-final path, no skipped review,
  no unsupported PR campaign recommendations.
- Expanded profile trigger, if any: high-governance risk.

## Selected Pipeline

- Pipeline: `article_pipeline.md` with `research_pipeline.md` upstream.
- Why this pipeline: requested work needs a structured, source-aware editorial
  deliverable with argument, plan, review, and final governance.
- Pipeline exceptions or local constraints: final output is a strategy memo, not
  a public article. Article Pipeline still governs because it is the closest
  current production path for analytical editorial material.

## Client Profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: none.
- Non-activation reason, if considered and rejected: no Sber-owned or
  Sber-policy communication requested.
- Client-profile files: none.
- Stop condition: activate no client profile unless user later supplies one.

## Preflight Gate

| Field | Decision |
| --- | --- |
| Audience | `inferred` |
| Channel or context | `inferred` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Rationale: the source and user goal are enough to create a constrained
  strategy artifact. Missing stakeholder data is handled as validation work in
  the plan, not invented as evidence.
- Production may start: yes.
- If `ask`: not applicable.
- If `constrain`: final output must frame reputation and needs as hypotheses
  from the brainstorm until validated.
- If `block`: not applicable.

## Editorial Decision Frame

- Chosen editorial route: convert the brainstorm into a service-positioning and
  90-day action strategy for Care.
- Why this route serves the task: the source problem is not only publicity; it
  combines unclear value, unclear interaction model, weak visibility, content
  quality risk, and internal operating friction.
- Alternatives considered:
  - Immediate PR campaign:
    - Rejected because it would amplify unclear positioning before needs,
      roles, and service promises are validated.
  - Portfolio-only route:
    - Rejected because it improves visibility but does not solve interaction,
      need discovery, or internal process issues.
  - Internal process cleanup only:
    - Rejected because it may improve Care internally while leaving UEC without
      a clear answer to what Care does and how to work with it.
- Writer contract:
  - Result type: strategic memo with prioritized workstreams and phased action
    plan.
  - Angle or reader path: from source diagnosis to editorial decision, then to
    concrete operating moves.
  - Scope boundary: do not invent survey results, leadership decisions,
    staffing, budgets, KPIs, or official mandates.
  - Must include: caveat about source limits; problem reframing; recommended
    workstreams; 30/60/90-day plan; approval and validation boundary.
  - Must not include: claims that Care reputation is objectively low; polished
    PR copy; public announcements; visual concepts.
  - Source boundary and confidence: one brainstorm source, high confidence for
    what the source says, low confidence for organization-wide truth.
- Review focus: evidence caveats, route validity, role separation, traceability,
  and whether recommendations are appropriately constrained.
- Reroute triggers: new stakeholder data contradicts the source, user requests
  public campaign copy, official approval becomes mandatory before finalization,
  or client-specific policy is introduced.

## Required Agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `intake_agent` | yes | Normalize source and user request |
| Orchestration | `chief_editor` | yes | Route and governance |
| Research | `research_agent` | yes | High-governance source analysis |
| Writing | `writer_agent` | yes | Draft strategy memo |
| Review | `review_agent` | yes | `review.md` and `qa-checklist.md` required |
| Finalization | `final_editor` | yes | `final.md` and high-governance checklist |
| Final governance | `chief_editor` | yes | `final_decision.md` |

## Required Knowledge And Evidence

- Required KB: `research_evidence.md`, `editorial_policy.md`,
  `tone_of_voice.md`, `glossary.md`, `task_statuses.md`
- Required source/evidence files: `/Users/sa/Documents/codex/Care/PR/pr care.md`
- Evidence gaps: no validated survey, leadership mandate, official Care service
  catalog, or external stakeholder data.

## Artifact Scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart and governance |
| `brief.md` | required | all roles | Source boundary and task goal |
| `status.md` | required | all roles | Lifecycle state |
| `research.md` | required | writer/reviewer | High-governance source analysis |
| `sources.md` | required | reviewer/governance | Source traceability |
| `facts.md` | required | writer/reviewer | Fact/interpretation split |
| `claims_table.md` | required | writer/reviewer | Claim-level traceability |
| `outline.md` | required | reviewer | Structure before drafting |
| `draft.md` | required | reviewer/finalizer | Draft under review |
| `writer-notes.md` | conditional | reviewer | Assumptions and caveats affect review |
| `claims-used.md` | required | reviewer | Claims used in output |
| `review.md` | required | finalizer/Chief Editor | Review gate |
| `qa-checklist.md` | required | Chief Editor | High-governance review evidence |
| `review-summary.md` | omitted | n/a | `review.md` and handoff are sufficient |
| `final.md` | required | user | Final deliverable |
| `finalization-notes.md` | conditional | Chief Editor | Controlled finalization notes |
| `finalization-checklist.md` | required | Chief Editor | High-governance finalization evidence |
| `final_decision.md` | required | user/governance | Closure decision |

## Structure-Before-Writing Plan

- Reader path: source caveat -> reframed diagnosis -> strategic choice -> workstreams -> phased plan -> decisions needed.
- Section roles: decision, evidence limits, diagnosis, action plan, governance.
- Required structure: prioritized, actionable, not promotional.
- Duplication risks: avoid repeating the brainstorm list; synthesize it into
  workstreams.

## Execution Order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `intake_agent` | user request/source path | `brief.md`, intake handoff | task routable |
| 2 | `chief_editor` | brief and rules | `orchestration_plan.md`, planning handoff | research assigned |
| 3 | `research_agent` | source file | `research.md`, `sources.md`, `facts.md`, `claims_table.md` | evidence sufficient |
| 4 | `chief_editor` | research | writer handoff | route confirmed |
| 5 | `writer_agent` | brief/research/plan | `outline.md`, `draft.md`, `writer-notes.md`, `claims-used.md` | ready for review |
| 6 | `review_agent` | draft/evidence | `review.md`, `qa-checklist.md` | approved or repair routed |
| 7 | `final_editor` | approved draft/review | `final.md`, finalization artifacts | final ready for governance |
| 8 | `chief_editor` | final/review | `final_decision.md`, status update | task closed locally |

## Status Transitions

- Starting status: `intake`
- Next expected status: `finalized`
- Status owner: `chief_editor`
- Status update trigger: each role transition and final governance decision.

## Review Requirements

- Review artifact: `review.md`
- Review depth: full
- Reviewer independence requirement: `review_agent` must be separate from
  `writer_agent`.
- Claims/evidence checks required: yes, through `claims_table.md` and
  `claims-used.md`.
- Optional review artifacts justified: yes, `qa-checklist.md` required by
  high-governance mode.

## Human Approval Requirements

- Required: no for local completion; yes before external use.
- Approval owner: user / Care leadership.
- Evidence needed: explicit approval if the plan becomes official.
- Cannot proceed past: external announcement, mandate, or rollout.

## Known Risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Source perceptions treated as facts | Misleading plan | writer/reviewer | Use caveats and validation workstream |
| PR before service clarity | Reputation work becomes cosmetic | chief_editor/writer | Route as service-positioning strategy |
| Internal process issues ignored | Communications remain low quality | writer | Include operating workstream |
| Overbroad plan | Hard to execute | writer/final_editor | Use phased 30/60/90-day plan |

## Completion Criteria

- Required artifacts complete: yes.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## Finalization Conditions

- Finalization may start when: `review.md` outcome is `approved`.
- Finalization must stop when: finalization would introduce new claims or remove
  source caveats.
- Compact finalization shape allowed: no, because high-governance mode requires
  separate checklist.
- Conditional finalization artifacts needed: yes, `finalization-notes.md` and
  `finalization-checklist.md`.

## Restart Notes

- Minimum read set: `task-manifest.md`, `brief.md`, `orchestration_plan.md`,
  `research.md`, `claims_table.md`, `claims-used.md`, `review.md`, `final.md`.
- Current active version: `final.md`.
- Deprecated/previous versions: `draft.md` is the reviewed draft.
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`.
- Directly relevant pipeline/KB: `article_pipeline.md`, `research_evidence.md`.
