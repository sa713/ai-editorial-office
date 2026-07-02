# Orchestration Plan

## task summary

- Task ID: VIBE-CODING-COMMUNITY
- User goal: разобрать `Roadmap.md` на понятный пакет markdown-идей для руководства сообщества
- Deliverable: `leadership_ideas_pack.md`, `community_entities_map.md`, `portal_content_ideas.md`
- Audience/channel: письмо или вложение к письму инициаторам и менеджерам `Vibe Coding Community`
- Current active version: main artifact set listed above

## task classification

- Task type: article-style editorial package / structured knowledge artifacts
- Risk mode: `low-risk`
- Factual sensitivity: low; external facts are not required
- Human approval likely required: no
- Rationale: задача требует редакционной структуризации исходного материала и соблюдения ограничений, но не требует внешнего research, технической спецификации или governance changes.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: source material and acceptance criteria are supplied; review-gate remains mandatory.
- Forbidden depth shortcuts: no bypass of review, no production outside task folder, no changes to `AGENTS.md`, roles, review-gate, pipelines, production files.
- Expanded profile trigger, if any: conflict between source and user constraints, request for implementation roadmap, KPI, UI design, technical architecture, or system-rule changes.

## selected pipeline

- Pipeline: `article_pipeline`
- Why this pipeline: existing system has no separate pipeline for idea packs; `article_pipeline` is the closest markdown-first editorial flow for structured text deliverables requiring writing and independent review.
- Pipeline exceptions or local constraints: no `final.md`; the final deliverable is the approved set of named markdown files, recorded in `final_decision.md`.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: n/a
- Non-activation reason, if considered and rejected: task is about a community idea package and not a Sber-owned or explicit Sber-policy task.
- Client-profile files: none
- Stop condition: if the user later explicitly requires a specific client editorial policy.

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

- Rationale: user supplied source file, task folder, audience, expected deliverables, exclusions, terms to preserve, tone and readiness criteria.
- Production may start: yes
- If `ask`: n/a
- If `constrain`: use only `Roadmap.md` and user brief; remove implementation-roadmap, resource, KPI, UI and governance layers from deliverables.
- If `block`: n/a

## custom workflow mini-contract

- Deviation: the reviewed final deliverable is a set of named markdown files, not a single `final.md`.
- Reason: user explicitly asked not to create `final.md` if final deliverable can be fixed through the main markdown files and `final_decision.md`.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | chief_editor | yes | Compact normalization from user prompt |
| Research | research_agent | no | Source is provided; no external research |
| Writing | writer_agent | yes | Prepare main artifact set |
| Review | review_agent | yes | `review.md` required |
| Finalization | final_editor | no | No separate `final.md`; main files are reviewed deliverables |
| Final governance | chief_editor | yes | `final_decision.md` after approved review |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `kb/task_statuses.md`, `pipelines/article_pipeline.md`, relevant templates.
- Required source/evidence files: `Roadmap.md`, user request captured in `brief.md`.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Normalize task goal and constraints |
| `task-manifest.md` | required | all roles | Restart anchor |
| `status.md` | required | all roles | State and transition evidence |
| `orchestration_plan.md` | required | all roles | Editorial routing and scope |
| `leadership_ideas_pack.md` | required | user / community leadership | Main ideas package |
| `community_entities_map.md` | required | user / community managers | Structured map of activities, artifacts, mechanics and functions |
| `portal_content_ideas.md` | required | user / community managers | Content logic for portal page |
| `draft.md` | required by selected pipeline | review_agent | Pointer to the main reviewed artifact set |
| `writer-notes.md` | conditional | review_agent | Records structure decisions and exclusions |
| `review.md` | required | chief_editor | Review-gate evidence |
| `final_decision.md` | conditional | user / chief_editor | Governance closure after approved review |
| `final.md` | omitted | n/a | Would duplicate the three named deliverables and contradict user preference |

## structure-before-writing plan

- Reader path: concept summary -> why portal/chat are insufficient -> practical workshop model -> operational loop -> broad formats -> small artifacts -> participant scenarios -> leadership discussion points.
- Section roles: main pack explains value; entities map structures components; portal ideas translate the loop into page content.
- Required structure: follow user-provided recommended structures while smoothing rough draft tone.
- Duplication risks: avoid repeating full definitions in every document; use tables in the map and narrative in the leadership pack.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | `AGENTS.md`, user prompt, source file | `brief.md`, `orchestration_plan.md`, initial status/manifest | preflight allows proceed |
| 2 | writer_agent | `brief.md`, `Roadmap.md`, plan | main markdown artifact set, `draft.md`, `writer-notes.md` | documents cover source ideas and constraints |
| 3 | review_agent | brief, plan, main files | `review.md` | deterministic outcome recorded |
| 4 | chief_editor | approved review | `final_decision.md`, updated manifest/status | task ready for user review |

## status transitions

- Starting status: `intake`
- Next expected status: `finalized`
- Status owner: chief_editor
- Status update trigger: artifact creation, review outcome, final decision

## review requirements

- Review artifact: `review.md`
- Review depth: compact deterministic review against user criteria, source coverage and exclusions.
- Reviewer independence requirement: review role is separate from writer role.
- Claims/evidence checks required: validate against `Roadmap.md` and `brief.md`; no external source claims.
- Optional review artifacts justified: no; embedded checklist in `review.md` is sufficient.

## human approval requirements

- Required: no
- Approval owner: n/a
- Evidence needed: n/a
- Cannot proceed past: n/a

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Source roadmap leaks into deliverables | User constraint violation | writer_agent / review_agent | Convert timing/resources into neutral ideas or omit |
| Documents become technical specification | Wrong audience and scope | writer_agent / review_agent | Keep content at idea, format and artifact level |
| Portal document becomes UI design | User constraint violation | writer_agent / review_agent | Describe content blocks and logic only |
| Ideas are over-compressed | Loss of source coverage | writer_agent / review_agent | Preserve all major activities, artifacts, mechanics and light functions |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if user asks to change system rules, roles, review-gate, pipelines, production files, or to add prohibited roadmap/KPI/technical/UI materials.

## completion criteria

- Required artifacts complete: yes when listed artifacts exist.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## finalization conditions

- Finalization may start when: `review.md` outcome is approved.
- Finalization must stop when: review is missing, blocked, or changes requested.
- Compact finalization shape allowed: yes; final deliverable is the approved set of named markdown files.
- Conditional finalization artifacts needed: `final_decision.md` only.

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, `Roadmap.md`, main artifact set, `review.md`.
- Current active version: `leadership_ideas_pack.md`, `community_entities_map.md`, `portal_content_ideas.md`.
- Deprecated/previous versions: none.
- Latest relevant handoff: not created under compact execution.
- Directly relevant pipeline/KB: `article_pipeline.md`, `kb/task_statuses.md`.
