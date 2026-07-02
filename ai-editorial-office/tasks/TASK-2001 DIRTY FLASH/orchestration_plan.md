# Orchestration Plan

## task summary

- Task ID: `TASK-2001 DIRTY FLASH`
- User goal: turn raw consultant notes into a usable photoshoot concept pack.
- Deliverable: `photo_concept.md`, `model_brief.md`, `photographer_cheatsheet.md`, `editorial_decision.md`.
- Audience/channel: photographer preparing and running an adult fashion/portrait/editorial-style photoshoot; model receives a separate human-readable brief.
- Current active version: first complete artifact set.

## task classification

- Task type: creative editorial normalization.
- Risk mode: standard.
- Factual sensitivity: low; references are treated as mood references from source, not researched claims.
- Human approval likely required: no.
- Rationale: the task is interpretive and creative, but contains sexualized and dark imagery that needs boundary control.

## process depth

- Depth: compact.
- Execution profile: compact.
- Rationale: source material is sufficient, deliverables are clear, no external research is required.
- Forbidden depth shortcuts: no direct production before routing; no bypass of review; no activation of frozen visual subsystem.
- Expanded profile trigger, if any: conflicting source direction or request for factual reference verification.

## selected pipeline

- Pipeline: `article_pipeline`.
- Why this pipeline: the deliverables are article-like editorial texts that need structure, source-aware rewriting, and review before delivery.
- Pipeline exceptions or local constraints: requested artifact names replace generic `draft.md` / `final.md` outputs; `photo_concept.md`, `model_brief.md`, and `photographer_cheatsheet.md` are the reviewed deliverable set.

## client profile

- Client profile: none.
- Client profile status: not_applicable.
- Activation reason: none.
- Non-activation reason, if considered and rejected: task is not Sber-owned and does not request a client policy.
- Client-profile files: none.
- Stop condition: any later user request to adapt for a specific client must be routed separately.

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

- Rationale: the user provided source file, deliverables, lengths, exclusions, and success criteria.
- Production may start: yes.
- If `constrain`: keep interpretation inside `Dirty Flash.md`; no new concept invention.

## custom workflow mini-contract

- Deviation: use named photoshoot pack artifacts instead of generic article draft/final files.
- Reason: user explicitly requested specific files.
- Owner: Chief Editor for routing; Writer Agent for artifact production; Review Agent for independent check; Chief Editor for final decision.
- Review gate preserved: yes.
- Governance model unchanged: yes.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | Chief Editor | yes | Normalize source boundary and route task |
| Research | omitted | no | No external factual claims required |
| Writing | Writer Agent | yes | Produce four requested artifacts |
| Review | Review Agent | yes | `review.md` required |
| Finalization | omitted | no | Artifacts are already named final working files after approval |
| Final governance | Chief Editor | yes | `final_decision.md` |

## required knowledge and evidence

- Required KB: task statuses only for lifecycle naming.
- Required source/evidence files: `Dirty Flash.md`, user request.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Normalized local source of task scope |
| `task-manifest.md` | required | all roles | Restart pointer |
| `orchestration_plan.md` | required | all roles | Routing and custom workflow |
| `status.md` | required | all roles | Lifecycle trace |
| `photo_concept.md` | required | photographer | Main concept |
| `model_brief.md` | required | model / photographer | Pre-shoot explanation |
| `photographer_cheatsheet.md` | required | photographer | On-set practical tool |
| `editorial_decision.md` | required | user / Chief Editor | Rationale and risk record |
| `review.md` | required | Chief Editor | Review gate |
| `final_decision.md` | required | Chief Editor / user | Governance closure |

## structure-before-writing plan

- Reader path: concept first, model-facing explanation second, on-set checklist third, editorial rationale last.
- Section roles: keep concept atmospheric; keep model brief inviting and non-technical; keep cheat sheet operational; keep decision concise.
- Required structure: follow user-provided headings for the cheat sheet exactly.
- Duplication risks: raw source repeats the same ideas in several phrasings; final artifacts should repeat only what each audience needs.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user request, `Dirty Flash.md` | manifest, plan, status routing | production may start |
| 2 | Writer Agent | brief, source, plan | four requested artifacts | files complete |
| 3 | Review Agent | brief, source, produced artifacts | `review.md` | verdict recorded |
| 4 | Chief Editor | review, artifacts | `final_decision.md`, finalized status | task complete |

## review requirements

- Review artifact: `review.md`
- Review depth: compact standard review.
- Reviewer independence requirement: Review Agent is separate from Writer Agent in role record.
- Claims/evidence checks required: check that concept is source-bound and not newly invented.
- Optional review artifacts justified: no.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Concept drifts into victimhood | Breaks source idea | Writer / Review | Keep heroine in control |
| Concept becomes cheap explicitness | Reduces taste and usability | Writer / Review | Use “trace”, “after”, “tension”, not literal shock |
| Too much reference dumping | Makes pack hard to use | Writer | Keep references out of core artifacts unless useful |
| Model brief feels coercive or objectifying | Bad working atmosphere | Writer / Review | Emphasize adult consent, agency, and emotional control |

## completion criteria

- Required artifacts complete: yes.
- Review outcome acceptable: approved.
- Blockers resolved: yes.
- Governance fields complete: yes.

## restart notes

- Minimum read set: `brief.md`, this plan, `Dirty Flash.md`, current active artifact set, `review.md`, `final_decision.md`.
- Current active version: first complete artifact set.
- Deprecated/previous versions: none.
- Latest relevant handoff: not applicable.
- Directly relevant pipeline/KB: `AGENTS.md` invariants and `kb/task_statuses.md`.
