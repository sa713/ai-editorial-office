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

When reviewed work depends on complex analysis, competing explanations,
disconfirmation, contradiction handling, sufficiency judgment, or uncertainty
communication, review applies `/kb/analytical_reasoning.md` to challenge the
reasoning path without creating a new review gate.

When reviewed work depends on structured interpretation, synthesis,
recommendation building, implications, analytical judgment, or decision-ready
analytical communication, review applies `/kb/professional_analysis.md` to
challenge the analytical product without creating a new review gate.

When reviewed work depends on message architecture, recommendation
presentation, explanation fit, technical communication, information density,
actionability, or caveat-preserving reader transfer, review applies
`/kb/professional_communication.md` to challenge communication transfer without
creating a new review gate.

When reviewed work is architecture-sensitive, review applies
`/kb/architecture_review.md` to challenge architectural drivers,
quality-attribute scenarios, architectural tradeoffs, assumptions, architecture
risks, accepted risks, and decision rationale without creating a new review
gate. Architecture Review is distinct from instructional architecture review:
it checks system design fitness rather than only reading path or section
structure.

When reviewed work is engineering-sensitive, review applies
`/kb/engineering_review.md` to challenge the changed surface, selected
engineering lenses, validation evidence, findings, and residual risk without
creating a new review gate. Engineering Review is distinct from Architecture
Review: it checks implementation/change safety rather than overall design
fitness.

When reviewed work shows wrong-task drift, weak evidence, hidden assumptions,
scope drift, role confusion, over-polishing, under-execution, implementation
task dilution, premature finalization, or review-gate bypass, review applies
`/kb/editorial_failure_modes.md` to name the failure and request bounded repair,
return to the right lifecycle stage, or block.

When reviewed work commits to a non-trivial route, recommendation, or
implementation plan, review applies `/kb/editorial_planning_framework.md` to
challenge whether credible alternatives, relevant evaluation dimensions, the
selected approach, accepted tradeoffs, and reconsideration triggers are visible.

When reviewed work depends on reader usefulness, actionability, implementation
clarity, publication fit, or stakeholder alignment, review applies
`/kb/audience_outcome_alignment.md` to challenge audience, intended outcome,
detail level, tone, format, evidence depth, omissions, and success criteria.

When reviewed work depends on selected quality priorities or visible tradeoffs,
review applies `/kb/editorial_quality_attributes.md` to challenge whether the
artifact optimized for the right qualities and preserved them through handoff.

When reviewed work proposes reusable learning, Knowledge Evolution disposition,
canon updates, pattern reuse, stale/conflicting knowledge findings,
correction/retirement, or `/about` sync, review applies
`/kb/editorial_learning_framework.md` to check evidence chain, owner, scope,
duplication, privacy, maintenance cost, and whether the item should remain
task-local.

When a task was governed by a Problem Hypothesis and/or Editorial Decision
Frame, review also includes an assumptions-based Editorial Challenge Lens inside
`review.md`. This lens tests whether the assumptions that made the chosen route
valid still hold. Its boundaries are governed by `AGENTS.md` and the selected
review scope.

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

Role legality and extension-role bounds are governed by `AGENTS.md`. This table
only maps Review Pipeline responsibilities to current roles.

| Responsibility | Required role | Agent spec |
| --- | --- | --- |
| Review execution | `review_agent` | `/agents/review_agent.md` |
| Governance routing and final decision | `chief_editor` | `/agents/chief_editor.md` |
| Writing changes, when review requests text changes | `writer_agent` | `/agents/writer_agent.md` |
| UX writing changes, when review requests UX copy changes | `ux_writer` | `/agents/ux_writer.md` |
| Evidence repair, when review finds factual or product evidence gaps | `research_agent` | `/agents/research_agent.md` |
| Finalization after approved review | `final_editor` | `/agents/final_editor.md` |

This pipeline does not change role authority. It only routes review findings to
the current owner of the affected work.

## required inputs

Review execution follows `/kb/shared_lifecycle_kernel.md` review context
contract and `AGENTS.md` short context loading policy. Load the shared review
packet from those owners, then add only review-specific context:

- this pipeline file;
- `/agents/review_agent.md`;
- the selected production pipeline;
- the material under review;
- latest handoff and assigned client-profile files when named by task
  artifacts;
- research, claim, source, and evidence-confidence artifacts when material
  claims or evidence-dependent conclusions are present;
- analytical-reasoning notes when reasoning complexity, evidence ambiguity,
  contradictions, or sufficiency judgments are material;
- professional-analysis notes when structured interpretation, synthesis,
  recommendation building, implications, analytical judgment, or
  decision-ready analytical communication is material;
- professional-communication notes when message architecture, recommendation
  presentation, explanation fit, technical communication, information density,
  actionability, or evidence/caveat-preserving reader transfer is material;
- architecture-review notes when architectural significance, drivers,
  quality-attribute scenarios, tradeoffs, assumptions, risks, or decision
  rationale are material;
- engineering-review notes when implementation/change safety, validation
  evidence, security/configuration/interface/data/reliability/performance
  risk, or engineering residual risk is material;
- the relevant editorial KB guidance only when its materiality trigger applies
  to the reviewed work.

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

Shared task artifacts and ownership are defined in `AGENTS.md`,
`/kb/task_object_model.md`, and `/kb/shared_lifecycle_kernel.md`. Review
Pipeline adds these review-stage views when the selected depth requires them:

- the material under review from the selected production pipeline;
- applicable research, source, fact, claim, and claim-use artifacts;
- `review.md`;
- `qa-checklist.md`, when separate checklist depth is required;
- `review-summary.md`, when separate concise transfer is needed;
- `reviewer-notes.md`, when extra caveats or borderline reasoning are needed;
- review handoff when handing off to the next role.

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
| `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Architecture Review challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
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

Use only statuses from `/kb/task_statuses.md`. Review Pipeline normally operates
in `review`, `changes_requested`, `approved`, `blocked`, or
`human_approval_required`, and may recommend valid returns to `research`,
`writing`, or optional `editing` according to the repair owner.

Review Agent must not create `draft.md`, `ux-copy.md`, `final.md`, `final_decision.md`, or publication/delivery artifacts.

Reviewer may flag unnecessary artifact creation as operational inefficiency. Artifact bloat is a governance issue if it reduces maintainability, restartability, or reviewer clarity.

## stage sequence

Default review sequence:

```text
writing or ux-writing -> review -> changes if needed -> review -> finalization -> chief_editor governance decision
```

Review-specific route:

1. Production owner hands off material ready for independent review.
2. Review Agent loads required artifacts, verifies independence, and validates
   scope.
3. Review Agent applies the material frameworks and review checks, then records
   exactly one valid outcome.
4. `changes_requested` findings return to the repair owner and then to
   re-review.
5. `approved` findings allow finalization, followed by Chief Editor governance.

Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` or `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. Review Agent must not treat a missing `editing` stage as a blocker in the current operating model. `editing` may be used only as a ready-for-review or revision bridge owned by the production role. It must not assign work to a separate Editor role.

## status transitions

Operational statuses and transitions are owned by `/kb/task_statuses.md`.
Review-specific transition notes:

- route from production or `changes_requested` to `review` only when reviewed
  material and handoff exist;
- route from `review` only to `approved`, `changes_requested`, `blocked`, or a
  valid human-approval escalation;
- route `changes_requested` findings back to `writing`, `research`, or
  `review` according to the repair owner and re-review scope;
- route from `approved` toward finalization/governance only under the shared
  review-gate and human-approval rules.

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
- compact analytical-reasoning check when the reviewed conclusion depends on
  problem framing, competing explanations, hidden assumptions, contradiction
  handling, diagnostic evidence, or sufficiency judgment;
- compact Professional Analysis check when the reviewed work depends on
  structured interpretation, synthesis, recommendation, implications,
  analytical judgment, or decision-ready communication;
- compact Professional Communication check when the reviewed work depends on
  message architecture, recommendation or ask presentation, explanation fit,
  technical communication, information density, actionability, or
  caveat-preserving reader transfer;
- compact Architecture Review check when the reviewed work is
  architecture-sensitive or depends on drivers, quality-attribute scenarios,
  architectural tradeoffs, assumptions, accepted risks, or decision rationale;
- compact failure-mode check when warning signs are visible;
- compact option-evaluation check when the reviewed work depends on a
  non-trivial selected approach;
- compact audience/outcome check when reviewed work depends on reader fit,
  actionability, implementation clarity, publication fit, or stakeholder
  alignment;
- compact quality-attribute check when reviewed work depends on selected
  quality priorities or accepted tradeoffs;
- compact Knowledge Evolution check when reviewed work proposes reusable
  learning, canon updates, pattern reuse, stale/conflicting knowledge,
  correction/retirement, or memory disposition;
- usefulness/pass rationale or blocking issues;
- governance note when relevant;
- one next action.

Normal review uses separate checklist or summary only when downstream review, routing, or risk needs them. Full review is required for high-governance and source-heavy work.

For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope.

## review rule ownership

This pipeline owns review-stage sequencing, review status transitions, review artifact depth, and review quality gates. Shared lifecycle concepts and stage context contracts are owned by `/kb/shared_lifecycle_kernel.md`.

It does not restate detailed review logic. Review Agent owns:

- reviewer independence checks;
- analytical-reasoning challenge, including wrong question, premature closure,
  confirmation bias, unsupported recommendation, hidden assumption,
  contradiction smoothing, false precision, unbounded research, and weak
  sufficiency judgment;
- Professional Analysis challenge, including unclear analytical product,
  missing decision context, weak synthesis, hidden options or implications,
  unsupported recommendation, missing risk/uncertainty, and unclear next
  decision/action;
- Professional Communication challenge, including missing or buried main point,
  weak message architecture, wrong density, unclear recommendation or ask,
  hidden caveats, misleading compression, weak explanation fit, technical
  ambiguity, missing next action, and unreviewable reader transfer;
- Architecture Review challenge, including missing drivers, vague quality
  attributes, missing scenarios, hidden architectural assumptions,
  architecture/implementation confusion, missing rejected alternatives,
  undocumented accepted risks, and decisions without rationale;
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
| Audience/outcome gate | Artifact fits the intended reader, outcome, action, detail, tone, format, and evidence depth | wrong reader, no actionability, wrong depth, generic output, or unusable implementation prompt |
| Professional-communication gate | Communication transfer is sufficient when message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, or caveat-preserving reader transfer is material | buried main point, wrong density, unclear ask or next action, hidden caveat, misleading compression, weak explanation, technical ambiguity, or unreviewable reader path |
| Quality-attribute gate | Priority quality attributes are sufficient for task risk and outcome | optimized for wrong quality, unresolved tradeoff, lost precision/actionability/traceability, or unreviewable artifact |
| Knowledge Evolution gate | Learning, pattern, canon, stale-knowledge, correction/retirement, and memory-disposition claims are evidenced, scoped, owned, non-duplicative, and reviewable when material | task-local note promoted without evidence, no owner, duplicate rule, privacy risk, `/about` treated as canon, or stale guidance handled by silent deletion |
| Outcome gate | Outcome is exactly `approved`, `changes_requested`, or `blocked` | ambiguous verdict |
| Finalization gate | Finalization allowed only after review outcome `approved` | missing review, blocked review, changes requested |

Failure at any gate prevents `approved`.

## completion conditions

Review Pipeline is complete only when the shared lifecycle and status owners
allow the review stage to close, and the review-specific packet is current:

- required review inputs were checked or missing inputs were documented;
- reviewer independence was checked;
- `review.md` exists and includes reviewed artifacts, findings, blockers,
  required changes, and exactly one valid outcome;
- when the reviewed work was governed by Problem Hypothesis and/or Editorial
  Decision Frame, `review.md` includes Editorial Challenge Lens or a compact
  statement that route-validity assumptions still hold;
- conditional review artifacts exist when their depth triggers apply;
- handoff exists to the correct next role when a role transition occurs;
- review-critical decisions cite artifacts;
- if outcome is `approved`, finalization can proceed without bypassing review-gate;
- if outcome is not `approved`, the task is not handed off as ready for finalization.

Completion means independent review is artifact-complete. It does not mean finalization, publication, delivery, release, archival, or governance approval has occurred.

## restart protocol

Restart behavior is owned by `AGENTS.md` and
`/kb/shared_lifecycle_kernel.md`. For Review Pipeline restarts, add only these
checks to the shared restart packet:

- review is the active stage or review is required before the next stage;
- reviewed material, selected production pipeline, and latest handoff are
  identified;
- Review Agent independence from the material creator is clear;
- unsupported, contradicted, missing, stale, or untraceable claims are visible;
- the next incomplete validation step is clear.
