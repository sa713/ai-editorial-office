# Orchestration Plan

## task summary

- Task ID: `TASK-2003 DIRTY FLASH BOUNDED REVISION`
- User goal: revise Dirty Flash materials using approved feedback without changing the concept's visual language.
- Deliverable: `photo_concept_v2.md`, `model_brief_v2.md`, `photographer_cheatsheet_v2.md`, `revision_notes.md`.
- Audience/channel: photographer and model preparation materials.
- Current active version: v2 artifact set.

## task classification

- Task type: bounded creative editorial revision.
- Risk mode: standard.
- Factual sensitivity: low.
- Human approval likely required: no.
- Rationale: revision is interpretive and source-bound, with moderate creative/sexualized concept risk.

## process depth

- Depth: compact.
- Execution profile: compact.
- Rationale: inputs are clear and prior feedback defines a bounded repair scope.
- Forbidden depth shortcuts: do not rewrite into a new concept; do not alter system rules; do not omit review.
- Expanded profile trigger, if any: user asks for broader repositioning or new moodboard/research.

## selected pipeline

- Pipeline: `article_pipeline`.
- Why this pipeline: v2 artifacts are editorial texts requiring structured rewriting and review.
- Pipeline exceptions or local constraints: user-requested v2 filenames are the deliverable set instead of generic `draft.md` / `final.md`.

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

- Rationale: TASK-2001 and TASK-2002 provide sufficient scope and feedback.
- Production may start: yes.
- If `constrain`: preserve Dirty Flash atmosphere and visual markers; revise hierarchy and emotional framing only.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Routing | Chief Editor | yes | Define bounded scope |
| Revision writing | Writer Agent | yes | Produce v2 artifacts and notes |
| Review | Review Agent | yes | Validate bounded scope and feedback application |
| Final governance | Chief Editor | yes | Record final decision |

## required knowledge and evidence

- Required source/evidence files: TASK-2001 v1 artifacts and TASK-2002 feedback/final decision.
- Evidence gaps: none.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Normalized revision scope |
| `task-manifest.md` | required | all roles | Version pointer |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `status.md` | required | all roles | Lifecycle trace |
| `photo_concept_v2.md` | required | photographer | Revised concept |
| `model_brief_v2.md` | required | model / photographer | Revised pre-shoot explanation |
| `photographer_cheatsheet_v2.md` | required | photographer | Revised on-set tool |
| `revision_notes.md` | required | user / reviewer | Explain bounded revision |
| `review.md` | required | Chief Editor | Review gate |
| `final_decision.md` | required | Chief Editor / user | Governance closure |

## structure-before-writing plan

- Reader path: v2 concept must lead with loss of propriety without loss of control; model brief must convert that into playable state; cheat sheet must make the conflict operational.
- Section roles: concept explains meaning; model brief invites embodiment; cheat sheet gives on-set controls; revision notes explain delta.
- Required structure: keep cheat sheet practical and include archetype distinction.
- Duplication risks: avoid replacing “after night” overuse with abstract moral language only; keep visual markers concrete.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user request, TASK-2002 feedback | routing artifacts | revision may start |
| 2 | Writer Agent | v1 artifacts, feedback | v2 artifacts and notes | files complete |
| 3 | Review Agent | v2 artifacts, brief, feedback | `review.md` | verdict recorded |
| 4 | Chief Editor | approved review | `final_decision.md`, status update | task complete |

## review requirements

- Review artifact: `review.md`
- Review depth: compact standard review.
- Reviewer independence requirement: Review Agent separate from Writer Agent.
- Claims/evidence checks required: verify v2 applies TASK-2002 feedback and does not drift into a new concept.
- Optional review artifacts justified: no.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Overcorrecting into abstraction | Loses shoot usability | Writer / Review | Keep concrete bathroom/flash/body markers |
| Losing the “after” atmosphere entirely | Breaks original Dirty Flash language | Writer / Review | Keep “after” as trace, not center |
| Archetype map becomes academic | Hurts on-set use | Writer | Keep distinctions short and practical |

## completion criteria

- Required artifacts complete: yes.
- Feedback applied: yes.
- Atmosphere preserved: yes.
- Review outcome acceptable: yes.
- Governance fields complete: yes.

## restart notes

- Minimum read set: `brief.md`, TASK-2002 `feedback.md`, v2 artifacts, `revision_notes.md`, `review.md`.
- Current active version: v2 artifact set.
- Deprecated/previous versions: TASK-2001 v1 artifacts for comparison only.
- Latest relevant handoff: not applicable.
