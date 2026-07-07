# Review Pipeline

## pipeline purpose

This pipeline governs independent review before:

- finalization;
- publication;
- delivery;
- governance decision;
- release;
- archival.

The pipeline protects review-gate integrity, factual traceability, KB compliance, artifact completeness, governance compliance, and deterministic review outcomes.

For instructional and operational materials, the pipeline also protects information architecture: reading path, section role clarity, selective reading usability, and structural duplication.

Review is a gate, not a writing, editing, finalization, or governance role. It produces evidence-backed findings and one of three allowed outcomes: `approved`, `changes_requested`, or `blocked`.

When reviewed work contains material claims, recommendations, route decisions,
or final-decision support, review applies `/kb/editorial_evidence_framework.md`
to check evidence basis, confidence, assumptions, unknowns, validation needed,
and residual risk.

When a task was governed by a Problem Hypothesis and/or Editorial Decision
Frame, review also includes an assumptions-based Editorial Challenge Lens inside
`review.md`. This lens tests whether the assumptions that made the chosen route
valid still hold. It is part of review, not a new pipeline, role, review gate,
artifact, or mandatory extra review cycle.

## when to use

Use this pipeline when a draft, UX copy, edited material, finalization candidate, or task package needs independent validation before moving forward.

Use it when:

- a material is ready for review after writing or UX writing;
- the task is already in `review` status;
- the latest handoff is directly from `writer_agent` or `ux_writer` to `review_agent` and required writing artifacts exist;
- review is required before finalization;
- review is requested before publication, delivery, release, governance decision, or archival;
- a previous review requested changes and the updated artifacts need re-review;
- factual traceability, KB compliance, artifact completeness, or governance integrity must be checked;
- Chief Editor needs an independent review outcome before assigning finalization.

## when not to use

Do not use this pipeline when:

- there is no material or artifact set to review;
- the task is still intake, research, or writing and not ready for independent review;
- the request is to write, rewrite, edit, finalize, publish, deliver, or approve instead of review;
- review would be performed by the same role instance that wrote the material;
- required inputs are missing and cannot be checked;
- the user asks to bypass review-gate.

If review scope is ambiguous, Chief Editor or Review Agent must document the ambiguity in `status.md`, `reviewer-notes.md`, or a handoff before continuing.

## required agents

By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.

| Responsibility | Required role | Agent spec |
| --- | --- | --- |
| Review execution | `review_agent` | `/agents/review_agent.md` |
| Governance routing and final decision | `chief_editor` | `/agents/chief_editor.md` |
| Writing changes, when review requests text changes | `writer_agent` | `/agents/writer_agent.md` |
| UX writing changes, when review requests UX copy changes | `ux_writer` | `/agents/ux_writer.md` |
| Evidence repair, when review finds factual or product evidence gaps | `research_agent` | `/agents/research_agent.md` |
| Finalization after approved review | `final_editor` | `/agents/final_editor.md` |

This pipeline must not assign review, editing, writing, finalization, or governance work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.

## required inputs

Review execution follows `/kb/shared_lifecycle_kernel.md` review context contract and `AGENTS.md` short context loading policy. Use these inputs only when they are relevant to the current review scope or required by the selected depth:

- `AGENTS.md`;
- `/project-state.md`, when continuing after context loss;
- `/kb/task_statuses.md`;
- `/tasks/TASK-ID/task-manifest.md`;
- `/tasks/TASK-ID/status.md`;
- `/tasks/TASK-ID/brief.md`;
- `/tasks/TASK-ID/orchestration_plan.md`;
- the selected production pipeline from `/pipelines/*.md`;
- `/pipelines/review_pipeline.md`;
- latest relevant handoff file;
- `/agents/review_agent.md`;
- material under review: `/tasks/TASK-ID/draft.md` or UX artifacts;
- relevant KB files named in `orchestration_plan.md`;
- active client-profile files and checklist named in `task-manifest.md` or
  `orchestration_plan.md`, only when `client_profile` is set;
- research and claim artifacts, if applicable.
- evidence-confidence notes when material conclusions depend on evidence
  quality.

When present, Problem Hypothesis and Editorial Decision Frame in
`orchestration_plan.md` are required inputs for the Editorial Challenge Lens.

For article-style review, the material under review is usually:

- `/tasks/TASK-ID/draft.md`;
- `/tasks/TASK-ID/claims-used.md`, if factual claims are used.

For UX writing review, the material under review is usually:

- `/tasks/TASK-ID/ux-copy.md`;
- `/tasks/TASK-ID/content-map.md`;
- `/tasks/TASK-ID/states-table.md`;
- `/tasks/TASK-ID/terminology-notes.md`;
- `/tasks/TASK-ID/ux-writer-notes.md`.

If required inputs are missing, including an active client-profile checklist
named by the manifest or orchestration plan, Review Agent must stop, record the
missing input, and recommend `blocked` or `changes_requested` according to
`/kb/task_statuses.md`.

Review may start from `review` status or from a direct handoff by `writer_agent` or `ux_writer` when the required artifacts exist and review is required. Missing `editing` status is not a blocker in the current operating model.

`task-manifest.md` must be updated at every stage transition, status transition, owner change, blocker change, review outcome change, review artifact state change, and handoff creation. Review cannot be considered complete if `task-manifest.md` is stale. If `task-manifest.md`, `status.md`, latest handoff, and `orchestration_plan.md` conflict, stop and escalate to `chief_editor`.

## required artifacts

Review uses this artifact set. Required/conditional/optional depth is governed by the artifact creation policy below.

| Artifact | Required when | Owner |
| --- | --- | --- |
| `/tasks/TASK-ID/task-manifest.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/status.md` | always | current owner or `chief_editor` |
| `/tasks/TASK-ID/brief.md` | always | `intake_agent` or `chief_editor` |
| `/tasks/TASK-ID/orchestration_plan.md` | always | `chief_editor` |
| `/tasks/TASK-ID/draft.md` | article, social, or editorial draft review | `writer_agent` |
| UX artifacts | UX writing review | `ux_writer` |
| `/tasks/TASK-ID/research.md` | research was required or factual/product claims are used | `research_agent` |
| `/tasks/TASK-ID/sources.md` | applicable factual/product claims need source traceability | `research_agent` |
| `/tasks/TASK-ID/facts.md` | applicable factual/product claims need fact traceability | `research_agent` |
| `/tasks/TASK-ID/claims_table.md` | applicable factual/product claims need claim validation | `research_agent` |
| `/tasks/TASK-ID/claims-used.md` | factual claims are used in draft | `writer_agent` |
| `/tasks/TASK-ID/review.md` | always | `review_agent` |
| `/tasks/TASK-ID/qa-checklist.md` | separate checklist required by downstream consumer, high-governance, task requirement, blocker/open-question state, or traceability need | `review_agent` |
| `/tasks/TASK-ID/review-summary.md` | separate concise transfer is consumed downstream | `review_agent` |
| `/tasks/TASK-ID/reviewer-notes.md` | extra reviewer reasoning or caveats needed | `review_agent` |
| `/tasks/TASK-ID/handoff-review-review-agent-to-TO.md` | always when handing off | `review_agent` |

`TO` must be replaced with the receiving core role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug, for example `chief-editor`, `writer-agent`, `ux-writer`, `research-agent`, or `artist-agent` when visual-extension conditions apply. These slugs are not separate agent names.

## artifact creation policy

Artifact creation must be intentional, conditional, risk-based, and downstream-driven. Do not create placeholder files for future use.

For low-risk and simple source-light standard tasks, use
`/kb/compact_execution.md` to review compact execution without expanding the
artifact package by default. `review.md` remains required before finalization;
Review Agent should not require optional artifacts when core traceability,
restartability, and governance evidence are sufficient.

Use `/kb/research_evidence.md` to review evidence mode without turning
research artifacts into defaults. Review Agent should not require research
artifacts for no-claim low-risk tasks when a no-research rationale is visible.
When material claims exist, Review Agent should verify them through
`claims-used.md`, `facts.md`, `sources.md`, `claims_table.md`, or equivalent
compact evidence. Missing evidence for material claims should produce
`changes_requested` or `blocked`.

### required artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `task-manifest.md` | Compact current state and review outcome fields | all roles | never for active tasks |
| `status.md` | Detailed status/history and blockers | all roles | never for active tasks |
| `brief.md` | Review scope and acceptance criteria | review_agent, chief_editor | never for review |
| `orchestration_plan.md` | Selected production pipeline and review gates | review_agent, chief_editor | never after orchestration starts |
| reviewed material | The artifact being independently reviewed | review_agent, final_editor | never for review |
| `review.md` | Deterministic verdict, evidence-confidence challenge, findings, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
| review handoff | Delta-transfer to next valid role | receiving role | only when no role transition occurs |

### conditional artifacts

| Artifact | Required when | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| `qa-checklist.md` | high-governance review, downstream consumer, task-specific requirement, detailed traceability need, or Chief Editor requires separate checklist | final_editor, chief_editor | low-risk or simple standard checklist is embedded in `review.md` |
| `review-summary.md` | next role needs separate concise outcome and next action | final_editor, chief_editor | `review.md` and handoff already provide equivalent concise routing |
| `reviewer-notes.md` | caveats, borderline decisions, or human-attention concerns exceed `review.md` | chief_editor, next production role | no extra reasoning is needed beyond `review.md` |
| research/claim artifacts | factual or product claims require traceability | review_agent | no factual/product claims are used |

### optional artifacts

| Artifact | Why it exists | Downstream consumer | May be omitted when |
| --- | --- | --- | --- |
| versioned review notes | comparison across re-review matters | chief_editor | current `review.md` supersedes prior review |
| `failure.md` | review cannot complete under constraints | chief_editor | task is not failed |

## allowed stages

Allowed stages:

- `review`;
- `changes_requested`;
- `approved`;
- `blocked`;
- `human_approval_required`;
- `research`, only as a recommended return path for evidence gaps;
- `writing`, only as a recommended return path for Writer Agent or UX Writer changes;
- `editing`, only as an optional status bridge or revision checkpoint; it is not required and does not introduce a separate Editor role;
- `finalization`, only after approved review and assignment to `final_editor`;
- `finalized`, only after Chief Editor governance decision;
- `failed`;
- `archived`.

Review Agent must not create `draft.md`, `ux-copy.md`, `final.md`, `final_decision.md`, or publication/delivery artifacts.

Reviewer may flag unnecessary artifact creation as operational inefficiency. Artifact bloat is a governance issue if it reduces maintainability, restartability, or reviewer clarity.

## stage sequence

Default review sequence:

```text
writing or ux-writing -> review -> changes if needed -> review -> finalization -> chief_editor governance decision
```

Operational sequence:

| Step | Status before | Role | Action | Required outputs | Status after |
| --- | --- | --- | --- | --- | --- |
| 1 | `writing`, `editing`, or `changes_requested` | `writer_agent` or `ux_writer` | Hand off material ready for independent review | writing or UX artifacts, handoff | `review` |
| 2 | `review` | `review_agent` | Load required artifacts, verify independence, validate scope | review notes or blocker evidence | `review` or `blocked` |
| 3 | `review` | `review_agent` | Validate factual traceability, evidence confidence, KB compliance, artifact completeness, governance compliance, and Editorial Challenge Lens when applicable | `review.md`, `qa-checklist.md` when separate checklist is required, `review-summary.md` when concise transfer is needed, `reviewer-notes.md` when extra notes are needed | `approved`, `changes_requested`, or `blocked` |
| 4 | `changes_requested` | `writer_agent`, `ux_writer`, or `research_agent` | Resolve required changes or evidence gaps | updated artifacts, handoff | `review`, `writing`, `research`, or `blocked` |
| 5 | `review` | `review_agent` | Re-review changed artifacts | updated review artifacts and handoff | `approved`, `changes_requested`, or `blocked` |
| 6 | `approved` | `final_editor` | Finalize only after approved review | `final.md`, conditional finalization notes/checklist, finalization handoff unless compact finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md` | `approved` |
| 7 | `approved` | `chief_editor` | Make governance decision after finalization | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |

Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` or `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. Review Agent must not treat a missing `editing` stage as a blocker in the current operating model. `editing` may be used only as a ready-for-review or revision bridge owned by the production role. It must not assign work to a separate Editor role.

## status transitions

Operational statuses must come from `/kb/task_statuses.md`.

Allowed critical transitions:

| From | To | Trigger | Responsible role | Required artifact evidence |
| --- | --- | --- | --- | --- |
| `writing` | `review` | Writer Agent or UX Writer completed required artifacts and review is required | `writer_agent`, `ux_writer`, or `chief_editor` | draft or UX artifacts, handoff to `review_agent` |
| `ux-writing` | `review` | Local UX writing stage label was used and required UX artifacts are complete | `ux_writer` or `chief_editor` | UX artifacts, handoff to `review_agent` |
| `editing` | `review` | Material is handed off for independent review | production role or `chief_editor` | draft or UX artifacts, handoff |
| `changes_requested` | `review` | Required changes were made and need re-review | production role or `chief_editor` | updated artifacts, handoff |
| `review` | `approved` | Review outcome is `approved` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `changes_requested` | Review outcome is `changes_requested` | `review_agent` | `review.md`, conditional checklist/summary, handoff |
| `review` | `blocked` | Review outcome is `blocked` | `review_agent` | `review.md`, blocker evidence |
| `review` | `human_approval_required` | Review identifies required human decision | `review_agent` or `chief_editor` | `review.md`, `status.md` escalation |
| `changes_requested` | `writing` | Text or UX copy changes are required | `review_agent` recommends, owner records | review artifacts, handoff to `writer_agent` or `ux_writer` |
| `changes_requested` | `research` | Evidence gaps are required | `review_agent` recommends, owner records | review artifacts, handoff to `research_agent` |
| `approved` | `human_approval_required` | Human approval is required before finalization, release, publication, delivery, or archival | `chief_editor` | `status.md`, `review.md`, brief requirement |
| `approved` | `finalized` | Chief Editor validates finalization and no human approval blocks closure | `chief_editor` | `final.md`, conditional finalization notes, `task-manifest.md`, `final_decision.md` |
| `blocked` | valid recovery status under `/kb/task_statuses.md` | Blocker resolved | current owner or `chief_editor` | updated `status.md`, resolution evidence |

No transition to `approved` is valid without a `review.md` outcome `approved` and checked artifacts listed in review outputs.

No transition to finalization is valid while review outcome is `changes_requested`, `blocked`, missing, or non-independent.

## risk mode behavior

Risk mode classification follows `AGENTS.md` and `/project-state.md`.

`low-risk` and simple source-light `standard` review use `review.md` as the primary review artifact and may keep checklist and summary content inside it. Review is still required before finalization.

`standard` review may use separate `qa-checklist.md` only when downstream routing, task-specific requirements, blockers/open questions, or traceability needs make the separate file useful.

`high-governance` review must use full review depth and must not approve if source traceability, required research artifacts, claim coverage, reviewer independence, human approval assessment, or governance-sensitive caveats are incomplete.

Evidence depth follows `/kb/research_evidence.md`: `no-research` is acceptable
only when no material claims need evidence; `compact-evidence` is acceptable
when material claims are source-light and traceable; `full-evidence` is
required for high-governance material claims.

Compact review minimum:

- verdict;
- reviewed artifact or artifact set;
- lightweight independence check;
- compact Editorial Challenge Lens when the task was governed by Problem
  Hypothesis and/or Editorial Decision Frame;
- compact evidence-confidence check when the reviewed conclusion depends on
  material evidence;
- usefulness/pass rationale or blocking issues;
- governance note when relevant;
- one next action.

Normal review uses separate checklist or summary only when downstream review, routing, or risk needs them. Full review is required for high-governance and source-heavy work.

For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope.

## review rule ownership

This pipeline owns review-stage sequencing, review status transitions, review artifact depth, and review quality gates. Shared lifecycle concepts and stage context contracts are owned by `/kb/shared_lifecycle_kernel.md`.

It does not restate detailed review logic. Review Agent owns:

- reviewer independence checks;
- factual, source, and claim validation;
- editorial relevance and replaceability pressure;
- assumptions-based Editorial Challenge Lens;
- instructional architecture pressure;
- allowed review outcomes and approval blockers;
- escalation content;
- deterministic review artifact content.

Templates own only fillable scaffolds. `AGENTS.md` owns governance invariants.

Pipeline-level retry behavior follows `/kb/task_statuses.md`; review-specific retry and escalation decisions are recorded by `review_agent` in review artifacts and handoff.

## quality gates

Quality gates are mandatory and artifact-backed.

| Gate | Passed only when | Blocking evidence |
| --- | --- | --- |
| Review readiness gate | Reviewed material and latest handoff exist | missing draft, UX artifacts, or handoff |
| Independence gate | Reviewer is independent from the material creator | same role instance or unknown independence |
| Artifact completeness gate | Required artifacts for selected pipeline are present | missing required task artifact |
| Factual traceability gate | Factual claims trace to source, fact, claim, or research artifacts | unsupported, contradicted, stale, or missing evidence |
| KB compliance gate | Relevant KB files were checked and findings cite artifacts | missing KB, tone, glossary, or policy check |
| Instructional architecture gate | Instructional or operational material can be followed through a clear reading path, with distinct section roles and bounded rereading cost | unclear route to action, mixed section roles, useless duplication, missing navigation, forced linear reading where reference use is needed |
| Outcome gate | Outcome is exactly `approved`, `changes_requested`, or `blocked` | ambiguous verdict |
| Finalization gate | Finalization allowed only after review outcome `approved` | missing review, blocked review, changes requested |

Failure at any gate prevents `approved`.

## completion conditions

Review Pipeline is complete only when:

- `task-manifest.md` is current and reflects review outcome and review artifact states;
- required review inputs were checked or missing inputs were documented;
- reviewer independence was checked;
- `review.md` exists and includes reviewed artifacts, findings, blockers, required changes, and outcome;
- when the reviewed work was governed by Problem Hypothesis and/or Editorial
  Decision Frame, `review.md` includes Editorial Challenge Lens or a compact
  statement that route-validity assumptions still hold;
- `qa-checklist.md` exists with pass, fail, or not_applicable statuses when separate checklist depth is required;
- `review-summary.md` exists with operational outcome and next action when concise transfer is not already covered by `review.md` and handoff;
- `reviewer-notes.md` exists when extra caveats or borderline reasoning do not fit in `review.md`;
- review outcome is exactly `approved`, `changes_requested`, or `blocked`;
- review outcome maps to a valid operational status under `/kb/task_statuses.md`;
- handoff exists to the correct next core role or explicitly legalized extension role whose `AGENTS.md` conditions apply;
- all review-critical decisions cite artifacts;
- if outcome is `approved`, finalization can proceed without bypassing review-gate;
- if outcome is not `approved`, the task is not handed off as ready for finalization.

Completion means independent review is artifact-complete. It does not mean finalization, publication, delivery, release, archival, or governance approval has occurred.

## restart protocol

After context loss, continue from artifacts, not chat history.

Receiving or restarting agents use the short context path from `/kb/shared_lifecycle_kernel.md` and `AGENTS.md`:

1. `AGENTS.md` or a short reference to its active invariants.
2. `/tasks/TASK-ID/task-manifest.md`.
3. The latest relevant handoff file.
4. The material under review or current `review.md`.
5. Only `/pipelines/review_pipeline.md`, the selected production pipeline, KB, or editorial knowledge directly needed for the next action.

Do not read all pipelines, all agent specs, all old task folders, all retrospectives, all versions, or the full project tree by default.

Expanded reading is allowed for high-governance, conflict, unsupported claims, review uncertainty, or restart uncertainty. In that case read the exact source/evidence files, `status.md`, prior review trail, governance artifacts, or old versions needed to resolve the risk.

Then perform this restart check:

- confirm `TASK-ID`;
- confirm the current-version pointer names the reviewed/current artifact when multiple versions exist;
- do not use latest modified time as the current-version source;
- stop and ask Chief Editor if current version state is unclear;
- confirm current status is valid under `/kb/task_statuses.md`;
- confirm review is the active stage or review is required before the next stage;
- confirm Review Agent is independent from the material creator;
- compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
- identify reviewed material and selected production pipeline;
- verify required artifacts for review readiness;
- identify unsupported, contradicted, missing, stale, or untraceable claims;
- continue review from the next incomplete validation step or set/recommend `blocked`.

Model memory, prior chat, or unsaved notes must not be used as evidence, approval, review outcome, reviewer independence proof, or workflow state.
