# Complete Diff: Outcome-First Deliverable Selection

Дата: 2026-07-13

Baseline: `2b524c2726e402b9bc8b82546ee0883abe296b47` (`main` before this implementation).

Scope: all canonical modifications and all new files created for
`TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`, including canonical integration,
`/about` exact mirrors, templates, synthetic tests, implementation report,
independent review and repair history, finalization, and final governance.

Pre-existing unrelated untracked paths are excluded. This file excludes only
its own recursive self-diff.

Whitespace-only context lines in the embedded display diff are rendered as
empty lines so this Markdown artifact passes repository whitespace checks.

~~~~diff
diff --git a/AGENTS.md b/AGENTS.md
index d086680..c590061 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -10,6 +10,9 @@ Then start the editorial entry flow there:

 - activate `chief_editor`;
 - determine task type;
+- distinguish the requested deliverable from the outcome-first recommended
+  deliverable, then record the selected deliverable without silently
+  overriding explicit user intent;
 - choose the pipeline or mode;
 - create or update `task-manifest.md`;
 - create or update `orchestration_plan.md`;
diff --git a/about/AGENTS.md b/about/AGENTS.md
index 3c7e6d4..aecbd7b 100644
--- a/about/AGENTS.md
+++ b/about/AGENTS.md
@@ -42,7 +42,7 @@
 | Task status model and transitions | `/kb/task_statuses.md` | status references, not alternate state models |
 | Task object model and artifact view mapping | `/kb/task_object_model.md` | task-specific values, restart pointers, and local consequences |
 | Capability registry and role-capability mapping | `/kb/capability_registry.md` | selected capabilities and task-specific consequences |
-| Task Need Recognition signals, advisory recommendations, uncertainty, negative evidence, and decomposition cues before routing | `/kb/task_need_recognition.md` | compact task-specific recognition view and Chief Editor decision |
+| Task Need Recognition signals, outcome-first deliverable recommendation, uncertainty, negative evidence, and decomposition cues before routing | `/kb/task_need_recognition.md` | compact task-specific recognition view, requested/recommended/selected deliverable decision, and Chief Editor routing decision |
 | Shared lifecycle kernel and stage context contracts | `/kb/shared_lifecycle_kernel.md` | selected stage, task-specific gate evidence, and local pipeline consequences |
 | Editorial evidence taxonomy, confidence labels, and evidence section standard | `/kb/editorial_evidence_framework.md` | task-specific evidence notes, confidence labels, assumptions, and risks |
 | Analytical reasoning moves, hypothesis comparison, disconfirmation, contradiction handling, and sufficiency judgment | `/kb/analytical_reasoning.md` | task-specific analytical notes, assumptions, hypotheses, contradictions, and sufficiency judgments |
@@ -192,6 +192,11 @@ Before production starts, Chief Editor must route the task editorially:
   decomposition, or uncertainty is material; treat it as advisory evidence and
   record the Chief Editor decision separately;
 - determine the task type;
+- before selecting a pipeline, distinguish the requested deliverable from the
+  outcome-first recommended deliverable, identify whether format choice is
+  explicit or delegated, and record the selected deliverable and reason;
+- respect an explicit requested deliverable by default; an alternative format
+  may be recommended, but it must not replace explicit user intent silently;
 - choose the relevant pipeline or editorial mode;
 - determine whether a client profile must be activated;
 - determine whether a Domain Knowledge Pack should be activated when domain
@@ -277,10 +282,11 @@ Exception: direct-production execution is allowed when the user explicitly asks
 to do the work directly, skip the editorial process, bypass the process, not use
 the editorial system, or handle the request as an ordinary non-editorial task.

-After routing, the result must stay within the selected pipeline or mode. For
-example, when `visual_article_sketchnote` is selected, execution must not
-silently drift into an infographic, web page, SVG summary, corporate one-pager,
-or other output genre that contradicts the selected mode.
+After routing, the result must stay within the selected deliverable and the
+pipeline or mode chosen for it. For example, when
+`visual_article_sketchnote` is selected, execution must not silently drift into
+an infographic, web page, SVG summary, corporate one-pager, or other output
+genre that contradicts the selected deliverable and mode.

 ## Core roles and extension roles

@@ -826,12 +832,18 @@ final governance still happens and must be artifact-backed.

 2. Orchestration

-   `chief_editor` выбирает pipeline, назначает core roles или явно легализованные extension roles только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
+   `chief_editor` сначала фиксирует requested, recommended и selected
+   deliverable, затем выбирает подходящий для selected deliverable pipeline,
+   назначает core roles или явно легализованные extension roles только когда
+   их условия выполнены, фиксирует план в `orchestration_plan.md` и
+   поддерживает `task-manifest.md` и `status.md`. Это одна orchestration-stage,
+   а не новая lifecycle stage или gate.

    Before production starts, `chief_editor` records or confirms a compact
    Preflight Gate decision in an existing task artifact. The required fields are:
    Audience (`confirmed` / `inferred` / `unknown`), Channel or context
-   (`confirmed` / `inferred` / `unknown`), Deliverable (`defined` / `unclear`),
+   (`confirmed` / `inferred` / `unknown`), Selected deliverable
+   (`defined` / `unclear`),
    Source boundary (`defined` / `unclear`), Success criterion (`defined` /
    `unclear`), Approval boundary (`defined` / `unclear`), and Missing data
    strategy (`ask` / `constrain` / `proceed` / `block`).
diff --git a/about/article_pipeline.md b/about/article_pipeline.md
index 8c6117f..99ff7de 100644
--- a/about/article_pipeline.md
+++ b/about/article_pipeline.md
@@ -22,7 +22,11 @@ The pipeline is markdown-first, artifact-backed, and restartable from `/tasks/TA

 ## when to use

-Use this pipeline when the requested output is an article-like text that needs editorial structure, source-aware writing, and review before finalization.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is an article-like text that needs editorial
+structure, source-aware writing, and review before finalization. An article
+mention alone does not select this pipeline when format choice was delegated or
+only illustrative.

 Use it when:

@@ -55,7 +59,7 @@ only maps Article Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize raw request into task artifacts |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
 | Writing | `writer_agent` | `/agents/writer_agent.md` | Create outline, draft, writer notes, and claims-used |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate draft and artifacts |
diff --git a/about/chief_editor.md b/about/chief_editor.md
index 1d31a42..88bc52e 100644
--- a/about/chief_editor.md
+++ b/about/chief_editor.md
@@ -31,7 +31,10 @@ signals and advisory recommendations are owned by

 ## Primary Responsibilities

-- select or confirm the appropriate pipeline and process depth;
+- distinguish requested, recommended, and selected deliverables; select the
+  smallest sufficient outcome-fit deliverable without silently overriding
+  explicit user intent; then select or confirm the appropriate pipeline and
+  process depth for that deliverable;
 - inspect Task Need Recognition evidence when material; accept, reject, narrow,
   or override its recommendations; and keep the recorded Chief Editor decision
   separate from the advisory view, including risk/consequence advice that does
@@ -293,6 +296,10 @@ Required when applicable:
   artifact.
 - compact Task Need Recognition acceptance, rejection, narrowing, override, or
   next-question decision when the advisory view is material.
+- compact outcome-first deliverable decision in `orchestration_plan.md` when
+  deliverable choice is material: requested deliverable, format authority,
+  recommended deliverable and reason, decision, selected deliverable, and any
+  alternative offered without silent substitution.
 - compact audience/outcome alignment note when reader, outcome, detail, tone,
   format, or success criteria materially shape the artifact.
 - compact reader journey inside `orchestration_plan.md` when reader change is
@@ -392,6 +399,9 @@ Conditional:
 - treat Task Need Recognition as an automatic route, task classifier,
   capability/Domain Pack activation, risk/depth choice, decomposition command,
   score, threshold, gate, or planning authority;
+- silently merge requested and recommended deliverables, replace an explicit
+  requested format without user agreement, or choose a pipeline before the
+  selected deliverable is recorded;
 - start production when audience or intended outcome is unknown and could
   materially change route, detail, evidence, tone, or deliverable;
 - start production when quality priorities conflict and the tradeoff could
@@ -414,7 +424,9 @@ Conditional:

 The Chief Editor may decide:

-- pipeline, risk mode, process depth, and active client profile;
+- selected deliverable, whether an advisory alternative is useful, and the
+  pipeline chosen afterward for that deliverable;
+- risk mode, process depth, and active client profile;
 - whether Task Need Recognition is needed and whether each recommendation is
   accepted, rejected, narrowed, overridden, or returned for evidence;
 - role routing and next owner;
@@ -481,6 +493,9 @@ The Chief Editor must not decide:
 - publication or human approval unless approval evidence is explicitly recorded.
 - hidden runtime metadata, unavailable model/mode values, or session details
   that are not needed for task traceability.
+- replace an explicit user-requested deliverable without user agreement; when
+  the mismatch is material, use preflight to ask, constrain, or preserve the
+  request with an explained alternative.

 ## Stop Conditions

@@ -536,6 +551,10 @@ the actual execution row or provide the delta needed for Chief Editor to do so.
 - final readiness is based on saved artifacts, not chat memory;
 - preflight decisions are explicit before production but do not force a separate
   artifact or unnecessary user question;
+- requested, recommended, and selected deliverables remain distinct; format
+  authority is visible; the selected deliverable is sufficient for the actual
+  outcome; explicit user intent is preserved; and pipeline selection follows
+  rather than determines the deliverable decision;
 - Editorial Decision Frame is present before writing or UX writing, is compact,
   names real alternatives with short rejection reasons, does not duplicate
   research, outline, review, or analytical addenda, and gives the next
diff --git a/about/final_editor.md b/about/final_editor.md
index 8b96381..5954054 100644
--- a/about/final_editor.md
+++ b/about/final_editor.md
@@ -38,6 +38,8 @@ owned by `/kb/domain_knowledge_pack_standard.md`.
   active Domain Knowledge Pack caveats when material, and structure;
 - preserve intended audience, outcome, actionability, detail level, format, and
   tone constraints from the reviewed artifact;
+- preserve the reviewed selected deliverable and do not use finalization to
+  adopt a different requested or recommended format;
 - preserve approved quality attributes and accepted tradeoffs from the reviewed
   artifact;
 - preserve evidence confidence limits, assumptions, and residual risks recorded
@@ -133,6 +135,8 @@ Conditional:
 - add or preserve a claim of client-policy compliance unless review verified it
   against the active client-profile source;
 - silently change meaning, scope, audience, channel, or claims;
+- silently change the selected deliverable or resolve a deliverable/pipeline
+  conflict during finalization;
 - remove selected-approach rationale, accepted tradeoffs, or reconsideration
   triggers when they are still material to user understanding;
 - remove analytical uncertainty, contradiction notes, sufficiency limits, or
diff --git a/about/intake_agent.md b/about/intake_agent.md
index 1218e4d..d4b536e 100644
--- a/about/intake_agent.md
+++ b/about/intake_agent.md
@@ -28,9 +28,10 @@ Professional Communication guidance is owned by
 - normalize the raw request into task title, goal, audience, output, channel,
   and constraints;
 - surface preflight inputs for Chief Editor: audience, channel/context,
-  intended outcome, reader context, deliverable, required action or decision,
-  format/detail/tone constraints, source boundary, success criterion, approval
-  boundary, missing information, and safe assumptions;
+  intended outcome, reader context, requested deliverable, format authority,
+  required action or decision, format/detail/tone constraints, source boundary,
+  success criterion, approval boundary, missing information, and safe
+  assumptions;
 - capture or conservatively infer the reader starting state, old/incomplete
   model, and desired practical change when teaching, understanding, or complex
   explanation is material; mark uncertainty instead of inventing a persona;
@@ -43,6 +44,10 @@ Professional Communication guidance is owned by
   consequence, significance, ambiguity, decomposition, or uncertainty is
   material; separate observed request evidence from recommendations and
   explicit non-decision;
+- when deliverable choice is material, record the requested deliverable and
+  whether format authority is `explicit`, `delegated`, `inferred`, or
+  `unknown`; surface an outcome-first deliverable recommendation as advisory
+  evidence without selecting it;
 - identify task type and likely pipeline;
 - identify whether a client profile may apply and propose `client_profile` when
   the task is clearly client-scoped;
@@ -166,10 +171,12 @@ handoff. It follows the artifact-minimalism rule in `AGENTS.md`.
 - desired model or practice after use:
 - status: confirmed / inferred / unknown / assumption

-## expected artifact
-- confirmed:
-- inferred:
-- unknown:
+## deliverable
+- requested deliverable: confirmed / inferred / not specified
+- format authority: explicit / delegated / inferred / unknown
+- advisory recommended deliverable, when material:
+- recommendation basis: outcome, use context, sufficiency, and avoidable burden
+- Chief Editor selection: pending

 ## source status
 - supplied sources:
@@ -196,6 +203,12 @@ Expected artifacts and acceptance criteria may come from explicit user wording
 or from labeled, bounded assumptions. If they are not known, mark them
 `unknown` or ask a question; do not fill them with generic defaults.

+Do not turn a request such as `explain this` into a checklist, roadmap, matrix,
+or other compressed artifact solely because it is shorter. Do not turn a
+delegated format choice into an explicit user requirement. Deliverable
+recommendation belongs to Task Need Recognition; selection belongs to Chief
+Editor and must precede pipeline selection.
+
 ### Ask vs proceed

 Ask a clarifying question when missing or ambiguous information:
@@ -343,6 +356,8 @@ Conditional:
 - approve final pipeline choice or final client-profile activation;
 - invent missing requirements, product behavior, facts, or user intent;
 - silently redefine scope, audience, channel, or expected output;
+- select a recommended deliverable, silently replace an explicit requested
+  deliverable, or use pipeline choice to decide the deliverable retroactively;
 - create production, review, finalization, governance, or placeholder artifacts;
 - make optional artifacts appear mandatory;
 - treat legacy task folders as templates;
@@ -355,12 +370,15 @@ The Intake Agent may decide:
 - how to normalize the request into a task package;
 - initial classification, likely pipeline recommendation, and proposed
   `client_profile`;
+- requested deliverable, format-authority classification, and an advisory
+  outcome-first deliverable recommendation when material;
 - whether ambiguity must be surfaced before orchestration;
 - which input gaps are likely material for Chief Editor preflight.

 The Intake Agent must not decide:

 - final pipeline approval or final client-profile activation;
+- selected deliverable or permission to override an explicit requested format;
 - confirmed task type, active capability or Domain Pack, risk/depth,
   decomposition, preflight, route, or next-action decisions;
 - final Preflight Gate outcome;
@@ -384,16 +402,20 @@ Stop and surface ambiguity when:

 ## Handoff Expectations

-Intake handoff must be short and routing-focused: normalized goal, likely
-pipeline, proposed risk mode, proposed client profile if any, known constraints,
-supplied materials, open questions, blockers, and recommended next Chief Editor
-action. It should not include analysis or draft content.
+Intake handoff must be short and routing-focused: normalized goal, requested
+deliverable and format authority, advisory recommended deliverable when
+material, likely pipeline only after that distinction, proposed risk mode,
+proposed client profile if any, known constraints, supplied materials, open
+questions, blockers, and recommended next Chief Editor action. It should not
+include analysis or draft content.

 ## Role-Specific Quality Checks

 - task package can be understood without chat history;
 - material reader starting state and uncertainty are visible without invented
   demographic or psychological detail;
+- requested, recommended, and selected deliverable are not conflated; explicit
+  format intent and delegated choice remain distinguishable;
 - risk mode and client-profile proposals are conservative and justified;
 - open questions are real, not boilerplate;
 - only bootstrap artifacts were created;
diff --git a/about/research_pipeline.md b/about/research_pipeline.md
index 0b9af9a..c49f026 100644
--- a/about/research_pipeline.md
+++ b/about/research_pipeline.md
@@ -14,6 +14,10 @@ conditional and claim-driven, not automatic.

 ## when to use

+Chief Editor selects this evidence pipeline only after the intended outcome and
+selected deliverable are known enough to define what evidence that deliverable
+needs. Research need does not decide the final artifact format retroactively.
+
 Use this pipeline when any of these are true:

 - the task needs factual claims, dates, names, numbers, quotes, product behavior, policy details, market context, or source-backed reasoning;
@@ -49,7 +53,7 @@ only maps Research Pipeline responsibilities to current roles.
 | Stage responsibility | Required role | Agent spec |
 | --- | --- | --- |
 | Intake package, if not already complete | `intake_agent` | `/agents/intake_agent.md` |
-| Pipeline selection and status governance | `chief_editor` | `/agents/chief_editor.md` |
+| Deliverable-first pipeline selection and status governance | `chief_editor` | `/agents/chief_editor.md` |
 | Research execution | `research_agent` | `/agents/research_agent.md` |
 | Downstream drafting, if research is sufficient for article or editorial copy | `writer_agent` | `/agents/writer_agent.md` |
 | Downstream UX copy, if research is sufficient for product-language work | `ux_writer` | `/agents/ux_writer.md` |
diff --git a/about/review_agent.md b/about/review_agent.md
index 5d4cca0..a892199 100644
--- a/about/review_agent.md
+++ b/about/review_agent.md
@@ -78,6 +78,11 @@ boundaries are owned by `/kb/task_need_recognition.md`.
   keyword classification, negative evidence, risk/consequence,
   proportionality, ambiguity, uncertainty, decomposition basis, owner
   boundaries, and non-automation;
+- verify the outcome-first deliverable decision when material: requested,
+  recommended, and selected deliverables remain distinct; format authority is
+  visible; the selected artifact is sufficient for the user's real objective;
+  explicit format intent was respected; any alternative or override was
+  explained; and pipeline selection followed the selected deliverable;
 - challenge whether the artifact optimized for the right quality attributes and
   whether accepted tradeoffs are visible and safe;
 - challenge each Bounded Utility Tradeoff against its concrete reader need,
@@ -312,6 +317,9 @@ artifacts must never become silently mandatory.
   contradictory evidence, forces a single type, overstates confidence,
   creates unnecessary depth, omits the Chief Editor decision, or performs
   routing, activation, decomposition, scoring, or depth selection;
+- approve a hidden deliverable substitution, an unexplained divergence from an
+  explicit requested format, a smallest artifact that is insufficient for the
+  outcome, or a pipeline selected before the deliverable decision;
 - approve canon evolution based on a single unverified task note, raw feedback,
   duplicate owner, missing source-evidence chain, or `/about` mirror;
 - approve a memory change that lacks a current canonical source, independently
@@ -361,6 +369,9 @@ The Review Agent may decide:
 - whether Task Need Recognition evidence and recommendations are proportionate,
   uncertainty-aware, owner-safe, explicitly advisory, and separated from the
   Chief Editor decision;
+- whether requested, recommended, and selected deliverables are correctly
+  separated; explicit intent is respected; any alternative is justified; and
+  the selected deliverable and downstream pipeline fit the real outcome;
 - whether a failure mode requires bounded repair, return to an earlier stage,
   or blocker;
 - whether option exploration is sufficient for the planning level and risk;
@@ -399,6 +410,9 @@ Stop and mark blocked or escalate when:
 - the Editorial Decision Frame is missing for post-planning writing, or is too
   formal, bloated, or duplicative to validate the chosen route as a usable
   production contract;
+- the orchestration record does not permit the reviewer to determine the
+  requested deliverable, format authority, selected deliverable, or whether the
+  pipeline was chosen after that decision when the distinction is material;
 - reviewer independence cannot be established;
 - required evidence, claim traceability, or source files are missing;
 - evidence confidence is below the minimum needed for the material conclusion
@@ -456,6 +470,11 @@ short examples needed to clarify a finding.
   recommendations, negative evidence, ambiguity, uncertainty, decomposition
   basis, explicit non-decision, and Chief Editor decision remain distinct; no
   keyword, score, threshold, or recommendation performs routing or activation;
+- outcome-first deliverable selection is checked when material: requested,
+  recommended, and selected deliverables remain distinct; the recommendation
+  is outcome-fit and sufficient rather than merely shorter; explicit user
+  format intent is preserved; alternatives or unresolved mismatches are
+  explained; and the pipeline follows the selected deliverable;
 - analytical reasoning is checked when material: the work does not answer the
   wrong question, close prematurely, confirm only the preferred answer, hide
   assumptions, smooth contradictions, inflate precision, overrun research, or
diff --git a/about/review_pipeline.md b/about/review_pipeline.md
index 877ddbb..82dc4ce 100644
--- a/about/review_pipeline.md
+++ b/about/review_pipeline.md
@@ -57,8 +57,10 @@ When downstream scope materially depends on Task Need Recognition, review
 applies `/kb/task_need_recognition.md` to challenge observed evidence,
 recommendation-versus-Chief Editor decision separation, keyword-only or forced
 classification, negative evidence, risk/consequence, proportionality,
-ambiguity, uncertainty, decomposition basis, owner boundaries, and
-non-automation. This is part of the
+ambiguity, uncertainty, decomposition basis, requested/recommended/selected
+deliverable separation, format authority, explicit-intent preservation,
+outcome-fit sufficiency, pipeline-after-deliverable ordering, owner boundaries,
+and non-automation. This is part of the
 existing review gate, not a new routing or review gate.

 When reviewed work shows wrong-task drift, weak evidence, hidden assumptions,
@@ -271,7 +273,7 @@ compact evidence. Missing evidence for material claims should produce
 | `task-manifest.md` | Compact current state and review outcome fields | all roles | never for active tasks |
 | `status.md` | Detailed status/history and blockers | all roles | never for active tasks |
 | `brief.md` | Review scope and acceptance criteria | review_agent, chief_editor | never for review |
-| `orchestration_plan.md` | Selected production pipeline and review gates | review_agent, chief_editor | never after orchestration starts |
+| `orchestration_plan.md` | Requested/recommended/selected deliverable decision, selected production pipeline, and review gates | review_agent, chief_editor | never after orchestration starts |
 | reviewed material | The artifact being independently reviewed | review_agent, final_editor | never for review |
 | `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Reader Review Lens when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
 | review handoff | Delta-transfer to next valid role | receiving role | only when no role transition occurs |
@@ -450,7 +452,10 @@ It does not restate detailed review logic. Review Agent owns:
 - Task Need Recognition challenge, including hidden request evidence,
   keyword-only or forced classification, missing negative evidence,
   disproportionate depth, hidden ambiguity/uncertainty, unsupported
-  decomposition, owner override, and recommendations treated as decisions;
+  decomposition, requested/recommended/selected deliverable conflation, silent
+  explicit-format override, insufficient artifact recommendation, pipeline
+  selection before the deliverable decision, owner override, and
+  recommendations treated as decisions;
 - Domain Knowledge Pack challenge, including weak activation, unsupported
   source register use, boundary drift, stale-if trigger neglect, canonical
   owner override, and misuse as policy, capability ownership, role, pipeline,
@@ -483,7 +488,7 @@ Quality gates are mandatory and artifact-backed.
 | Reader Review gate | When material, understanding, retention, application, Cognitive Bridge, Learning Design sequence, and reader burden have deterministic statuses tied to the Reader Outcome Contract and exact artifact evidence | missing bridge, headings substituted for memorable ideas, vague Practical Transformation, academic or jargon overload that blocks the outcome, or a taste preference presented as a finding |
 | Companion Pass gate | Reader-facing work is natural and concrete enough for the intended reader while preserving precision, evidence, caveats, boundaries, and traceability | taxonomy dump, synthetic expert performance, avoidable academic distance, unsupported friendliness, precision loss, or substantive repair deferred to Final Editor |
 | Professional-communication gate | Communication transfer is sufficient when message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, or caveat-preserving reader transfer is material | buried main point, wrong density, unclear ask or next action, hidden caveat, misleading compression, weak explanation, technical ambiguity, or unreviewable reader path |
-| Task Need Recognition gate | When downstream scope materially depends on recognition, observed evidence, recommendations, negative evidence, uncertainty, decomposition basis, explicit non-decision, and Chief Editor decision are distinct, proportionate, and owner-safe | keyword-only or forced type, hidden ambiguity, missing negative evidence, unsupported split, score/threshold authority, automatic routing/activation/depth, or Chief Editor decision absent |
+| Task Need Recognition gate | When downstream scope materially depends on recognition, observed evidence, recommendations, negative evidence, uncertainty, decomposition basis, explicit non-decision, and Chief Editor decision are distinct, proportionate, and owner-safe; when deliverable choice is material, requested, recommended, and selected deliverables are distinct, format authority is visible, the selected artifact is sufficient for the actual outcome, explicit user intent is respected, any alternative or unresolved mismatch is explained, and the pipeline was chosen afterward for the selected deliverable | keyword-only or forced type, hidden ambiguity, missing negative evidence, unsupported split, score/threshold authority, automatic routing/activation/depth, Chief Editor decision absent, silent format substitution, requested/recommended conflation, unjustified alternative, smallest-but-insufficient artifact, missing selected deliverable, or pipeline-first routing |
 | Quality-attribute gate | Priority quality attributes are sufficient for task risk and outcome | optimized for wrong quality, unresolved tradeoff, lost precision/actionability/traceability, or unreviewable artifact |
 | Knowledge Evolution gate | Learning, pattern, canon, stale-knowledge, correction/retirement, memory-disposition, Memory Hygiene Intelligence, and advisory Evaluation Signal claims are evidenced, scoped, owned, non-duplicative, proportionate, and reviewable; feedback/outcome claims preserve classification vs disposition, affected area, applicability, contradictions, bounded action, and non-promotion; memory claims preserve canonical source, represented fact, materiality, purpose/sensitivity/value, exact-copy or compact-summary branch, correction/compression/retirement/omission/deferral/no-sync rationale, branch validation, unique context, bounded growth, and non-automation; signal views preserve decision question, comparison window, denominator/exposure when material, missing cases, alternatives, confidence, qualitative judgment, and explicit non-decision | task-local note promoted without evidence, feedback classification treated as automatic learning, no owner, duplicate rule, privacy risk, `/about` treated as canon, stale guidance handled by silent deletion, exact copy edited independently, misleading summary compression, sensitive/task-local propagation, context-erasing consolidation/retirement, unchecked no-sync, automatic memory write/disposition, activity/activation treated as value, unlike comparisons, hidden contradictions, score/KPI/target/rank/maturity use, individual monitoring, or automatic action |
 | Domain Knowledge Pack gate | Active pack use is justified, sourced, bounded, current enough, and subordinate to canonical owners; claimed benefit or burden also traces to actual sections used, task effect evidence, confidence, complexity cost, and non-promotion when material | weak activation, missing source register support, boundary drift, stale-if trigger ignored, activation treated as proof of value, unsupported effect claim, pack treated as policy/capability/role/pipeline/gate, or mandatory artifact creep |
@@ -506,6 +511,10 @@ allow the review stage to close, and the review-specific packet is current:
   statement that route-validity assumptions still hold;
 - when Reader Review is material, `review.md` records all applicable Reader
   Review criteria, evidence, reader consequences, and bounded repair routing;
+- when deliverable choice is material, `review.md` records the applicable
+  requested/recommended/selected, format-authority, sufficiency,
+  explicit-intent, alternative/mismatch, and pipeline-ordering checks inside
+  the existing review gate and cites the orchestration decision;
 - when material is reader-facing, `review.md` records Companion Pass and routes
   substantive repair to Writer Agent before approval;
 - conditional review artifacts exist when their depth triggers apply;
@@ -525,6 +534,8 @@ checks to the shared restart packet:
 - review is the active stage or review is required before the next stage;
 - reviewed material, selected production pipeline, and latest handoff are
   identified;
+- requested and selected deliverables, plus the advisory recommendation when
+  material, are identifiable in the orchestration record;
 - Review Agent independence from the material creator is clear;
 - unsupported, contradicted, missing, stale, or untraceable claims are visible;
 - the next incomplete validation step is clear.
diff --git a/about/social_pipeline.md b/about/social_pipeline.md
index cdbdf60..43ba0c1 100644
--- a/about/social_pipeline.md
+++ b/about/social_pipeline.md
@@ -17,7 +17,10 @@ The pipeline is markdown-first, artifact-backed, deterministic, and restartable

 ## when to use

-Use this pipeline when the requested output is short-form editorial or promotional copy adapted to one or more platforms.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is short-form editorial or promotional copy
+adapted to one or more platforms. A short-form example does not select this
+pipeline when format choice was delegated or only illustrative.

 Use it when:

@@ -48,7 +51,7 @@ only maps Social Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, platform target, audience, constraints, and missing information |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
 | Writing | `writer_agent` | `/agents/writer_agent.md` | Create platform-adapted short-form draft and claim usage notes |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate copy, artifacts, tone, traceability, and governance compliance |
diff --git a/about/ux_writer.md b/about/ux_writer.md
index d02aff3..00b233f 100644
--- a/about/ux_writer.md
+++ b/about/ux_writer.md
@@ -24,7 +24,10 @@ is owned by `/kb/professional_communication.md`.
 ## Primary Responsibilities

 - understand user intent, product context, flow state, intended user action,
-  channel, and constraints;
+  channel, selected deliverable, and constraints;
+- produce the selected deliverable recorded by Chief Editor; if requested,
+  recommended, selected, and pipeline fields conflict, stop instead of choosing
+  a format implicitly;
 - use structure-before-writing notes when provided;
 - use the Editorial Decision Frame in `orchestration_plan.md` as the UX writing
   contract when present;
@@ -148,6 +151,8 @@ Stop and escalate when:
   preserve within the approved product context;
 - the Editorial Decision Frame is missing, stale, or conflicts with the handoff
   for a task handed from Chief Editor planning;
+- requested, recommended, selected deliverable, or selected pipeline records
+  conflict in a way that could change the output;
 - copy would require inventing a product rule or feature;
 - terminology conflicts with glossary, active client profile, or product
   constraints;
diff --git a/about/ux_writing_pipeline.md b/about/ux_writing_pipeline.md
index 8db4e42..0f1c2b5 100644
--- a/about/ux_writing_pipeline.md
+++ b/about/ux_writing_pipeline.md
@@ -21,7 +21,11 @@ The pipeline is markdown-first, artifact-backed, deterministic, and restartable

 ## when to use

-Use this pipeline when the requested output is product-facing copy that appears in or around an interface, product flow, onboarding path, notification, validation state, or user guidance surface.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is product-facing copy that appears in or
+around an interface, product flow, onboarding path, notification, validation
+state, or user guidance surface. A UX example alone does not select this
+pipeline when format choice was delegated or only illustrative.

 Use it when:

@@ -54,7 +58,7 @@ only maps UX Writing Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, supplied UI context, and missing information |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when facts or product context need verification | `research_agent` | `/agents/research_agent.md` | Create evidence base for factual or product claims |
 | UX writing | `ux_writer` | `/agents/ux_writer.md` | Create product-facing copy and UX writing artifacts |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate UX copy and artifacts |
diff --git a/about/writer_agent.md b/about/writer_agent.md
index c1c6f33..d8a9b49 100644
--- a/about/writer_agent.md
+++ b/about/writer_agent.md
@@ -29,7 +29,11 @@ owned by `/kb/domain_knowledge_pack_standard.md`.

 ## Primary Responsibilities

-- understand task goal, audience, channel, output format, and constraints;
+- understand task goal, audience, channel, selected deliverable, output format,
+  and constraints;
+- produce the selected deliverable recorded by Chief Editor; if requested,
+  recommended, selected, and pipeline fields conflict, stop instead of choosing
+  a format implicitly;
 - use structure-before-writing notes when present;
 - use the Editorial Decision Frame in `orchestration_plan.md` as the drafting
   contract when present;
@@ -141,6 +145,8 @@ Conditional:
 - polish around weak evidence, missing structure, or task mismatch instead of
   returning to the right recovery action;
 - silently change task goal, audience, channel, angle, or scope;
+- silently revert to the requested or recommended deliverable when it differs
+  from the selected deliverable;
 - produce generic good text that does not enable the intended reader decision,
   action, understanding, review, or publication outcome;
 - optimize for polish, elegance, completeness, or brevity when those qualities
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
index 3c7e6d4..aecbd7b 100644
--- a/ai-editorial-office/AGENTS.md
+++ b/ai-editorial-office/AGENTS.md
@@ -42,7 +42,7 @@
 | Task status model and transitions | `/kb/task_statuses.md` | status references, not alternate state models |
 | Task object model and artifact view mapping | `/kb/task_object_model.md` | task-specific values, restart pointers, and local consequences |
 | Capability registry and role-capability mapping | `/kb/capability_registry.md` | selected capabilities and task-specific consequences |
-| Task Need Recognition signals, advisory recommendations, uncertainty, negative evidence, and decomposition cues before routing | `/kb/task_need_recognition.md` | compact task-specific recognition view and Chief Editor decision |
+| Task Need Recognition signals, outcome-first deliverable recommendation, uncertainty, negative evidence, and decomposition cues before routing | `/kb/task_need_recognition.md` | compact task-specific recognition view, requested/recommended/selected deliverable decision, and Chief Editor routing decision |
 | Shared lifecycle kernel and stage context contracts | `/kb/shared_lifecycle_kernel.md` | selected stage, task-specific gate evidence, and local pipeline consequences |
 | Editorial evidence taxonomy, confidence labels, and evidence section standard | `/kb/editorial_evidence_framework.md` | task-specific evidence notes, confidence labels, assumptions, and risks |
 | Analytical reasoning moves, hypothesis comparison, disconfirmation, contradiction handling, and sufficiency judgment | `/kb/analytical_reasoning.md` | task-specific analytical notes, assumptions, hypotheses, contradictions, and sufficiency judgments |
@@ -192,6 +192,11 @@ Before production starts, Chief Editor must route the task editorially:
   decomposition, or uncertainty is material; treat it as advisory evidence and
   record the Chief Editor decision separately;
 - determine the task type;
+- before selecting a pipeline, distinguish the requested deliverable from the
+  outcome-first recommended deliverable, identify whether format choice is
+  explicit or delegated, and record the selected deliverable and reason;
+- respect an explicit requested deliverable by default; an alternative format
+  may be recommended, but it must not replace explicit user intent silently;
 - choose the relevant pipeline or editorial mode;
 - determine whether a client profile must be activated;
 - determine whether a Domain Knowledge Pack should be activated when domain
@@ -277,10 +282,11 @@ Exception: direct-production execution is allowed when the user explicitly asks
 to do the work directly, skip the editorial process, bypass the process, not use
 the editorial system, or handle the request as an ordinary non-editorial task.

-After routing, the result must stay within the selected pipeline or mode. For
-example, when `visual_article_sketchnote` is selected, execution must not
-silently drift into an infographic, web page, SVG summary, corporate one-pager,
-or other output genre that contradicts the selected mode.
+After routing, the result must stay within the selected deliverable and the
+pipeline or mode chosen for it. For example, when
+`visual_article_sketchnote` is selected, execution must not silently drift into
+an infographic, web page, SVG summary, corporate one-pager, or other output
+genre that contradicts the selected deliverable and mode.

 ## Core roles and extension roles

@@ -826,12 +832,18 @@ final governance still happens and must be artifact-backed.

 2. Orchestration

-   `chief_editor` выбирает pipeline, назначает core roles или явно легализованные extension roles только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
+   `chief_editor` сначала фиксирует requested, recommended и selected
+   deliverable, затем выбирает подходящий для selected deliverable pipeline,
+   назначает core roles или явно легализованные extension roles только когда
+   их условия выполнены, фиксирует план в `orchestration_plan.md` и
+   поддерживает `task-manifest.md` и `status.md`. Это одна orchestration-stage,
+   а не новая lifecycle stage или gate.

    Before production starts, `chief_editor` records or confirms a compact
    Preflight Gate decision in an existing task artifact. The required fields are:
    Audience (`confirmed` / `inferred` / `unknown`), Channel or context
-   (`confirmed` / `inferred` / `unknown`), Deliverable (`defined` / `unclear`),
+   (`confirmed` / `inferred` / `unknown`), Selected deliverable
+   (`defined` / `unclear`),
    Source boundary (`defined` / `unclear`), Success criterion (`defined` /
    `unclear`), Approval boundary (`defined` / `unclear`), and Missing data
    strategy (`ask` / `constrain` / `proceed` / `block`).
diff --git a/ai-editorial-office/agents/chief_editor.md b/ai-editorial-office/agents/chief_editor.md
index 1d31a42..88bc52e 100644
--- a/ai-editorial-office/agents/chief_editor.md
+++ b/ai-editorial-office/agents/chief_editor.md
@@ -31,7 +31,10 @@ signals and advisory recommendations are owned by

 ## Primary Responsibilities

-- select or confirm the appropriate pipeline and process depth;
+- distinguish requested, recommended, and selected deliverables; select the
+  smallest sufficient outcome-fit deliverable without silently overriding
+  explicit user intent; then select or confirm the appropriate pipeline and
+  process depth for that deliverable;
 - inspect Task Need Recognition evidence when material; accept, reject, narrow,
   or override its recommendations; and keep the recorded Chief Editor decision
   separate from the advisory view, including risk/consequence advice that does
@@ -293,6 +296,10 @@ Required when applicable:
   artifact.
 - compact Task Need Recognition acceptance, rejection, narrowing, override, or
   next-question decision when the advisory view is material.
+- compact outcome-first deliverable decision in `orchestration_plan.md` when
+  deliverable choice is material: requested deliverable, format authority,
+  recommended deliverable and reason, decision, selected deliverable, and any
+  alternative offered without silent substitution.
 - compact audience/outcome alignment note when reader, outcome, detail, tone,
   format, or success criteria materially shape the artifact.
 - compact reader journey inside `orchestration_plan.md` when reader change is
@@ -392,6 +399,9 @@ Conditional:
 - treat Task Need Recognition as an automatic route, task classifier,
   capability/Domain Pack activation, risk/depth choice, decomposition command,
   score, threshold, gate, or planning authority;
+- silently merge requested and recommended deliverables, replace an explicit
+  requested format without user agreement, or choose a pipeline before the
+  selected deliverable is recorded;
 - start production when audience or intended outcome is unknown and could
   materially change route, detail, evidence, tone, or deliverable;
 - start production when quality priorities conflict and the tradeoff could
@@ -414,7 +424,9 @@ Conditional:

 The Chief Editor may decide:

-- pipeline, risk mode, process depth, and active client profile;
+- selected deliverable, whether an advisory alternative is useful, and the
+  pipeline chosen afterward for that deliverable;
+- risk mode, process depth, and active client profile;
 - whether Task Need Recognition is needed and whether each recommendation is
   accepted, rejected, narrowed, overridden, or returned for evidence;
 - role routing and next owner;
@@ -481,6 +493,9 @@ The Chief Editor must not decide:
 - publication or human approval unless approval evidence is explicitly recorded.
 - hidden runtime metadata, unavailable model/mode values, or session details
   that are not needed for task traceability.
+- replace an explicit user-requested deliverable without user agreement; when
+  the mismatch is material, use preflight to ask, constrain, or preserve the
+  request with an explained alternative.

 ## Stop Conditions

@@ -536,6 +551,10 @@ the actual execution row or provide the delta needed for Chief Editor to do so.
 - final readiness is based on saved artifacts, not chat memory;
 - preflight decisions are explicit before production but do not force a separate
   artifact or unnecessary user question;
+- requested, recommended, and selected deliverables remain distinct; format
+  authority is visible; the selected deliverable is sufficient for the actual
+  outcome; explicit user intent is preserved; and pipeline selection follows
+  rather than determines the deliverable decision;
 - Editorial Decision Frame is present before writing or UX writing, is compact,
   names real alternatives with short rejection reasons, does not duplicate
   research, outline, review, or analytical addenda, and gives the next
diff --git a/ai-editorial-office/agents/final_editor.md b/ai-editorial-office/agents/final_editor.md
index 8b96381..5954054 100644
--- a/ai-editorial-office/agents/final_editor.md
+++ b/ai-editorial-office/agents/final_editor.md
@@ -38,6 +38,8 @@ owned by `/kb/domain_knowledge_pack_standard.md`.
   active Domain Knowledge Pack caveats when material, and structure;
 - preserve intended audience, outcome, actionability, detail level, format, and
   tone constraints from the reviewed artifact;
+- preserve the reviewed selected deliverable and do not use finalization to
+  adopt a different requested or recommended format;
 - preserve approved quality attributes and accepted tradeoffs from the reviewed
   artifact;
 - preserve evidence confidence limits, assumptions, and residual risks recorded
@@ -133,6 +135,8 @@ Conditional:
 - add or preserve a claim of client-policy compliance unless review verified it
   against the active client-profile source;
 - silently change meaning, scope, audience, channel, or claims;
+- silently change the selected deliverable or resolve a deliverable/pipeline
+  conflict during finalization;
 - remove selected-approach rationale, accepted tradeoffs, or reconsideration
   triggers when they are still material to user understanding;
 - remove analytical uncertainty, contradiction notes, sufficiency limits, or
diff --git a/ai-editorial-office/agents/intake_agent.md b/ai-editorial-office/agents/intake_agent.md
index 1218e4d..d4b536e 100644
--- a/ai-editorial-office/agents/intake_agent.md
+++ b/ai-editorial-office/agents/intake_agent.md
@@ -28,9 +28,10 @@ Professional Communication guidance is owned by
 - normalize the raw request into task title, goal, audience, output, channel,
   and constraints;
 - surface preflight inputs for Chief Editor: audience, channel/context,
-  intended outcome, reader context, deliverable, required action or decision,
-  format/detail/tone constraints, source boundary, success criterion, approval
-  boundary, missing information, and safe assumptions;
+  intended outcome, reader context, requested deliverable, format authority,
+  required action or decision, format/detail/tone constraints, source boundary,
+  success criterion, approval boundary, missing information, and safe
+  assumptions;
 - capture or conservatively infer the reader starting state, old/incomplete
   model, and desired practical change when teaching, understanding, or complex
   explanation is material; mark uncertainty instead of inventing a persona;
@@ -43,6 +44,10 @@ Professional Communication guidance is owned by
   consequence, significance, ambiguity, decomposition, or uncertainty is
   material; separate observed request evidence from recommendations and
   explicit non-decision;
+- when deliverable choice is material, record the requested deliverable and
+  whether format authority is `explicit`, `delegated`, `inferred`, or
+  `unknown`; surface an outcome-first deliverable recommendation as advisory
+  evidence without selecting it;
 - identify task type and likely pipeline;
 - identify whether a client profile may apply and propose `client_profile` when
   the task is clearly client-scoped;
@@ -166,10 +171,12 @@ handoff. It follows the artifact-minimalism rule in `AGENTS.md`.
 - desired model or practice after use:
 - status: confirmed / inferred / unknown / assumption

-## expected artifact
-- confirmed:
-- inferred:
-- unknown:
+## deliverable
+- requested deliverable: confirmed / inferred / not specified
+- format authority: explicit / delegated / inferred / unknown
+- advisory recommended deliverable, when material:
+- recommendation basis: outcome, use context, sufficiency, and avoidable burden
+- Chief Editor selection: pending

 ## source status
 - supplied sources:
@@ -196,6 +203,12 @@ Expected artifacts and acceptance criteria may come from explicit user wording
 or from labeled, bounded assumptions. If they are not known, mark them
 `unknown` or ask a question; do not fill them with generic defaults.

+Do not turn a request such as `explain this` into a checklist, roadmap, matrix,
+or other compressed artifact solely because it is shorter. Do not turn a
+delegated format choice into an explicit user requirement. Deliverable
+recommendation belongs to Task Need Recognition; selection belongs to Chief
+Editor and must precede pipeline selection.
+
 ### Ask vs proceed

 Ask a clarifying question when missing or ambiguous information:
@@ -343,6 +356,8 @@ Conditional:
 - approve final pipeline choice or final client-profile activation;
 - invent missing requirements, product behavior, facts, or user intent;
 - silently redefine scope, audience, channel, or expected output;
+- select a recommended deliverable, silently replace an explicit requested
+  deliverable, or use pipeline choice to decide the deliverable retroactively;
 - create production, review, finalization, governance, or placeholder artifacts;
 - make optional artifacts appear mandatory;
 - treat legacy task folders as templates;
@@ -355,12 +370,15 @@ The Intake Agent may decide:
 - how to normalize the request into a task package;
 - initial classification, likely pipeline recommendation, and proposed
   `client_profile`;
+- requested deliverable, format-authority classification, and an advisory
+  outcome-first deliverable recommendation when material;
 - whether ambiguity must be surfaced before orchestration;
 - which input gaps are likely material for Chief Editor preflight.

 The Intake Agent must not decide:

 - final pipeline approval or final client-profile activation;
+- selected deliverable or permission to override an explicit requested format;
 - confirmed task type, active capability or Domain Pack, risk/depth,
   decomposition, preflight, route, or next-action decisions;
 - final Preflight Gate outcome;
@@ -384,16 +402,20 @@ Stop and surface ambiguity when:

 ## Handoff Expectations

-Intake handoff must be short and routing-focused: normalized goal, likely
-pipeline, proposed risk mode, proposed client profile if any, known constraints,
-supplied materials, open questions, blockers, and recommended next Chief Editor
-action. It should not include analysis or draft content.
+Intake handoff must be short and routing-focused: normalized goal, requested
+deliverable and format authority, advisory recommended deliverable when
+material, likely pipeline only after that distinction, proposed risk mode,
+proposed client profile if any, known constraints, supplied materials, open
+questions, blockers, and recommended next Chief Editor action. It should not
+include analysis or draft content.

 ## Role-Specific Quality Checks

 - task package can be understood without chat history;
 - material reader starting state and uncertainty are visible without invented
   demographic or psychological detail;
+- requested, recommended, and selected deliverable are not conflated; explicit
+  format intent and delegated choice remain distinguishable;
 - risk mode and client-profile proposals are conservative and justified;
 - open questions are real, not boilerplate;
 - only bootstrap artifacts were created;
diff --git a/ai-editorial-office/agents/review_agent.md b/ai-editorial-office/agents/review_agent.md
index 5d4cca0..a892199 100644
--- a/ai-editorial-office/agents/review_agent.md
+++ b/ai-editorial-office/agents/review_agent.md
@@ -78,6 +78,11 @@ boundaries are owned by `/kb/task_need_recognition.md`.
   keyword classification, negative evidence, risk/consequence,
   proportionality, ambiguity, uncertainty, decomposition basis, owner
   boundaries, and non-automation;
+- verify the outcome-first deliverable decision when material: requested,
+  recommended, and selected deliverables remain distinct; format authority is
+  visible; the selected artifact is sufficient for the user's real objective;
+  explicit format intent was respected; any alternative or override was
+  explained; and pipeline selection followed the selected deliverable;
 - challenge whether the artifact optimized for the right quality attributes and
   whether accepted tradeoffs are visible and safe;
 - challenge each Bounded Utility Tradeoff against its concrete reader need,
@@ -312,6 +317,9 @@ artifacts must never become silently mandatory.
   contradictory evidence, forces a single type, overstates confidence,
   creates unnecessary depth, omits the Chief Editor decision, or performs
   routing, activation, decomposition, scoring, or depth selection;
+- approve a hidden deliverable substitution, an unexplained divergence from an
+  explicit requested format, a smallest artifact that is insufficient for the
+  outcome, or a pipeline selected before the deliverable decision;
 - approve canon evolution based on a single unverified task note, raw feedback,
   duplicate owner, missing source-evidence chain, or `/about` mirror;
 - approve a memory change that lacks a current canonical source, independently
@@ -361,6 +369,9 @@ The Review Agent may decide:
 - whether Task Need Recognition evidence and recommendations are proportionate,
   uncertainty-aware, owner-safe, explicitly advisory, and separated from the
   Chief Editor decision;
+- whether requested, recommended, and selected deliverables are correctly
+  separated; explicit intent is respected; any alternative is justified; and
+  the selected deliverable and downstream pipeline fit the real outcome;
 - whether a failure mode requires bounded repair, return to an earlier stage,
   or blocker;
 - whether option exploration is sufficient for the planning level and risk;
@@ -399,6 +410,9 @@ Stop and mark blocked or escalate when:
 - the Editorial Decision Frame is missing for post-planning writing, or is too
   formal, bloated, or duplicative to validate the chosen route as a usable
   production contract;
+- the orchestration record does not permit the reviewer to determine the
+  requested deliverable, format authority, selected deliverable, or whether the
+  pipeline was chosen after that decision when the distinction is material;
 - reviewer independence cannot be established;
 - required evidence, claim traceability, or source files are missing;
 - evidence confidence is below the minimum needed for the material conclusion
@@ -456,6 +470,11 @@ short examples needed to clarify a finding.
   recommendations, negative evidence, ambiguity, uncertainty, decomposition
   basis, explicit non-decision, and Chief Editor decision remain distinct; no
   keyword, score, threshold, or recommendation performs routing or activation;
+- outcome-first deliverable selection is checked when material: requested,
+  recommended, and selected deliverables remain distinct; the recommendation
+  is outcome-fit and sufficient rather than merely shorter; explicit user
+  format intent is preserved; alternatives or unresolved mismatches are
+  explained; and the pipeline follows the selected deliverable;
 - analytical reasoning is checked when material: the work does not answer the
   wrong question, close prematurely, confirm only the preferred answer, hide
   assumptions, smooth contradictions, inflate precision, overrun research, or
diff --git a/ai-editorial-office/agents/ux_writer.md b/ai-editorial-office/agents/ux_writer.md
index d02aff3..00b233f 100644
--- a/ai-editorial-office/agents/ux_writer.md
+++ b/ai-editorial-office/agents/ux_writer.md
@@ -24,7 +24,10 @@ is owned by `/kb/professional_communication.md`.
 ## Primary Responsibilities

 - understand user intent, product context, flow state, intended user action,
-  channel, and constraints;
+  channel, selected deliverable, and constraints;
+- produce the selected deliverable recorded by Chief Editor; if requested,
+  recommended, selected, and pipeline fields conflict, stop instead of choosing
+  a format implicitly;
 - use structure-before-writing notes when provided;
 - use the Editorial Decision Frame in `orchestration_plan.md` as the UX writing
   contract when present;
@@ -148,6 +151,8 @@ Stop and escalate when:
   preserve within the approved product context;
 - the Editorial Decision Frame is missing, stale, or conflicts with the handoff
   for a task handed from Chief Editor planning;
+- requested, recommended, selected deliverable, or selected pipeline records
+  conflict in a way that could change the output;
 - copy would require inventing a product rule or feature;
 - terminology conflicts with glossary, active client profile, or product
   constraints;
diff --git a/ai-editorial-office/agents/writer_agent.md b/ai-editorial-office/agents/writer_agent.md
index c1c6f33..d8a9b49 100644
--- a/ai-editorial-office/agents/writer_agent.md
+++ b/ai-editorial-office/agents/writer_agent.md
@@ -29,7 +29,11 @@ owned by `/kb/domain_knowledge_pack_standard.md`.

 ## Primary Responsibilities

-- understand task goal, audience, channel, output format, and constraints;
+- understand task goal, audience, channel, selected deliverable, output format,
+  and constraints;
+- produce the selected deliverable recorded by Chief Editor; if requested,
+  recommended, selected, and pipeline fields conflict, stop instead of choosing
+  a format implicitly;
 - use structure-before-writing notes when present;
 - use the Editorial Decision Frame in `orchestration_plan.md` as the drafting
   contract when present;
@@ -141,6 +145,8 @@ Conditional:
 - polish around weak evidence, missing structure, or task mismatch instead of
   returning to the right recovery action;
 - silently change task goal, audience, channel, angle, or scope;
+- silently revert to the requested or recommended deliverable when it differs
+  from the selected deliverable;
 - produce generic good text that does not enable the intended reader decision,
   action, understanding, review, or publication outcome;
 - optimize for polish, elegance, completeness, or brevity when those qualities
diff --git a/ai-editorial-office/kb/capability_registry.md b/ai-editorial-office/kb/capability_registry.md
index 8d264c8..7f071be 100644
--- a/ai-editorial-office/kb/capability_registry.md
+++ b/ai-editorial-office/kb/capability_registry.md
@@ -153,27 +153,31 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
 ### Task Need Recognition

 - Purpose: turn available request evidence into an advisory view of likely task
-  type, capabilities, Domain Packs, research/evidence/review needs, risk and
-  consequence,
+  type, outcome-first deliverable, capabilities, Domain Packs,
+  research/evidence/review needs, risk and consequence,
   architectural/engineering/communication significance, ambiguity,
   decomposition need, uncertainty, and negative evidence before Chief Editor
   routing.
-- Typical inputs: normalized or raw request, intended outcome, deliverable,
-  audience/context, source state, work surface, consequence, constraints,
-  affected boundaries, domain materiality, and known unknowns.
+- Typical inputs: normalized or raw request, intended outcome, requested
+  deliverable, format authority, audience/context, source state, work surface,
+  consequence, constraints, affected boundaries, domain materiality, and known
+  unknowns.
 - Typical outputs: compact recognition view in `brief.md`,
   `orchestration_plan.md`, or `task-manifest.md`, with observed signals,
-  recommendations, confidence/negative evidence, explicit non-decision, and
-  Chief Editor next question or decision.
+  recommendations including the smallest sufficient outcome-fit deliverable,
+  confidence/negative evidence, explicit non-decision, and Chief Editor next
+  question or decision.
 - Accountability wrapper: Intake Agent normally assembles the initial view;
-  Chief Editor challenges it and owns every routing/preflight/activation/depth/
-  decomposition decision; Review Agent challenges material downstream reliance.
+  Chief Editor challenges it and owns every selected-deliverable/routing/
+  preflight/activation/depth/decomposition decision; Review Agent challenges
+  material downstream reliance.
 - Required artifacts: none beyond existing task artifacts; omit or compress the
   view when the task is trivial and obvious.
 - Optional artifacts: conditional section in an existing brief, plan, or
   manifest; never a mandatory standalone recognition file.
 - Stop conditions: keyword-only recommendation, forced single type despite
-  mixed evidence, hidden ambiguity/negative evidence, duplicate owner,
+  mixed evidence, hidden ambiguity/negative evidence, requested/recommended
+  deliverable conflation, silent explicit-format override, duplicate owner,
   automatic action, score/threshold authority, or unjustified process weight.
 - Quality criteria: observed evidence is separate from recommendation and Chief
   Editor decision; recommendations are multi-signal, proportionate,
@@ -184,9 +188,10 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.

 ### Routing And Preflight

-- Purpose: choose task type, pipeline/mode/mini-contract, risk mode, process
-  depth, active capabilities, active roles, client profile status, and next
-  action.
+- Purpose: choose the selected deliverable from requested and advisory
+  recommended deliverables, then choose task type, pipeline/mode/mini-contract,
+  risk mode, process depth, active capabilities, active roles, client profile
+  status, and next action.
 - Typical inputs: `brief.md`, `task-manifest.md`, current user instruction,
   relevant pipeline/mode candidates, client-profile indicators.
 - Typical outputs: `orchestration_plan.md`, task-manifest updates, status
@@ -198,8 +203,11 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
 - Stop conditions: risk mode unknown before production, missing critical input,
   unauthorized extension role, review-bypass request, source/instruction
   conflict.
-- Quality criteria: route is deliberate, compact when safe, expanded when
-  needed, review gate preserved.
+- Quality criteria: requested/recommended/selected deliverables are distinct;
+  explicit user intent is preserved; selected deliverable is sufficient for the
+  actual outcome; pipeline follows the deliverable decision; route is
+  deliberate, compact when safe, expanded when needed, and review gate is
+  preserved.
 - Expansion triggers: high-governance risk, source-heavy task, client-profile
   uncertainty, human approval complexity, version conflict, reviewer uncertainty.

@@ -914,12 +922,12 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.

 | Role | Wrapped capabilities |
 | --- | --- |
-| Chief Editor | Task Need Recognition challenge and decision separation; routing and preflight; reader-journey design for material reader-facing work; analytical reasoning depth for complex or decision-heavy work; Professional Analysis selection for structured interpretation, synthesis, recommendation, and decision-support work; Professional Communication selection for message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, and caveat-preserving reader transfer when material; Architecture Review selection for architecture-sensitive work; Engineering Review selection for implementation-sensitive work; quality attribute selection for route/depth decisions; audience/outcome alignment for route/depth decisions; planning and option evaluation for route/commitment decisions; source boundary decision when routing; evidence-confidence decision for material routes and governance; failure-mode reroute/escalation; editorial structure contract; client-profile activation; governance closure; memory curation; Knowledge Evolution disposition; learning extraction and canon-evolution routing; mini-contract authorization. |
-| Intake Agent | Intake normalization; initial Task Need Recognition signal and advisory view when material; initial audience/outcome and Reader Model starting-state capture or inference; initial Professional Communication materiality signal when the request depends on executive brief, recommendation or ask, technical explanation, teaching, policy/stakeholder memo, implementation handoff, or dense source compression; initial source boundary detection; initial separation of user-provided facts, assumptions, and unknowns; early task-misunderstanding and missing-constraint detection; planning-depth signal; risk/client-profile suggestion. |
+| Chief Editor | Task Need Recognition challenge and decision separation; outcome-first selected deliverable decision before pipeline selection; routing and preflight; reader-journey design for material reader-facing work; analytical reasoning depth for complex or decision-heavy work; Professional Analysis selection for structured interpretation, synthesis, recommendation, and decision-support work; Professional Communication selection for message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, and caveat-preserving reader transfer when material; Architecture Review selection for architecture-sensitive work; Engineering Review selection for implementation-sensitive work; quality attribute selection for route/depth decisions; audience/outcome alignment for route/depth decisions; planning and option evaluation for route/commitment decisions; source boundary decision when routing; evidence-confidence decision for material routes and governance; failure-mode reroute/escalation; editorial structure contract; client-profile activation; governance closure; memory curation; Knowledge Evolution disposition; learning extraction and canon-evolution routing; mini-contract authorization. |
+| Intake Agent | Intake normalization; requested deliverable and format-authority capture; initial outcome-first deliverable recommendation inside Task Need Recognition when material; initial audience/outcome and Reader Model starting-state capture or inference; initial Professional Communication materiality signal when the request depends on executive brief, recommendation or ask, technical explanation, teaching, policy/stakeholder memo, implementation handoff, or dense source compression; initial source boundary detection; initial separation of user-provided facts, assumptions, and unknowns; early task-misunderstanding and missing-constraint detection; planning-depth signal; risk/client-profile suggestion. |
 | Research Agent | Research/evidence classification; analytical decomposition, hypothesis testing, contradiction preservation, and diagnostic evidence support when material; Professional Analysis evidence support, source synthesis, implications, and decision-context support when assigned; Professional Communication support through evidence, confidence, caveat, unknown, and source-meaning preservation when communication transfer is material; architecture driver, constraint, quality-attribute evidence, tradeoff, assumption, and risk support when material; engineering-review evidence support when implementation change safety needs professional, repository, validation, dependency, security, or operational evidence; evidence confidence assessment when research is assigned; evidence for competing options; durable evidence/context signal when material; evidence-weakness and confidence-inflation detection; source boundary detection; evidence repair. |
 | Writer Agent | Editorial structure and Learning Design within the approved route; drafting from approved evidence; realization of Cognitive Bridge, Moments of Insight, Practical Transformation, and supported examples when material; preservation of analytical structure, Professional Analysis product shape, Professional Communication message architecture, synthesis, recommendation, architecture rationale, assumptions, alternatives, uncertainty, caveats, density choices, action path, and sufficiency cues when material; quality-preservation during drafting; audience/outcome shaping; tradeoff communication; over-polishing/unsupported-claim detection; assumption/caveat preservation; repair for draft findings; bounded source-conversion production only when a mini-contract assigns it. |
 | UX Writer | UX writing from product evidence; quality-preservation for product copy; audience/outcome shaping for user action and UI state; Professional Communication support when broader product communication transfer, action path, evidence caveat, or density is material; over-polishing/product-assumption detection; UX assumption/caveat preservation; UX repair; client-profile application for product copy. |
-| Review Agent | Independent review; Task Need Recognition challenge for evidence/recommendation/decision separation, proportionality, negative evidence, uncertainty, owner boundaries, and non-automation when material; Professional Analysis challenge for unclear analytical product, missing decision context, weak synthesis, hidden options or criteria, unsupported recommendation, missing implications or risks, and unreviewable uncertainty when material; Professional Communication and deterministic Reader Review challenge for missing or buried main point, weak message architecture, wrong density, unclear recommendation or ask, missing next action, hidden caveats, misleading compression, weak explanation fit, broken Cognitive Bridge, missing application path, reader burden, technical ambiguity, and unreviewable reader transfer when material; architecture-review challenge for missing drivers, vague quality attributes, missing scenarios, hidden assumptions, architecture/implementation confusion, missing rejected alternatives, undocumented accepted risks, and decisions without rationale; Engineering Review challenge for changed surface, selected lenses, validation, security/config/interface/data/reliability/performance risks, and engineering residual risk when material; analytical-reasoning challenge for wrong question, premature closure, confirmation bias, hidden assumptions, contradiction smoothing, false precision, unsupported recommendation, weak sufficiency, and unbounded research; quality-attribute challenge; audience/outcome mismatch challenge; option-evaluation challenge; evidence-confidence challenge; failure-mode challenge; learning/canon candidate, stale-knowledge, correction/retirement, and memory-sync challenge when material; review-side source/client/profile checks; re-review after repair. |
+| Review Agent | Independent review; Task Need Recognition challenge for evidence/recommendation/decision separation, requested/recommended/selected deliverable separation, explicit-intent preservation, outcome-fit sufficiency, pipeline-after-deliverable ordering, proportionality, negative evidence, uncertainty, owner boundaries, and non-automation when material; Professional Analysis challenge for unclear analytical product, missing decision context, weak synthesis, hidden options or criteria, unsupported recommendation, missing implications or risks, and unreviewable uncertainty when material; Professional Communication and deterministic Reader Review challenge for missing or buried main point, weak message architecture, wrong density, unclear recommendation or ask, missing next action, hidden caveats, misleading compression, weak explanation fit, broken Cognitive Bridge, missing application path, reader burden, technical ambiguity, and unreviewable reader transfer when material; architecture-review challenge for missing drivers, vague quality attributes, missing scenarios, hidden assumptions, architecture/implementation confusion, missing rejected alternatives, undocumented accepted risks, and decisions without rationale; Engineering Review challenge for changed surface, selected lenses, validation, security/config/interface/data/reliability/performance risks, and engineering residual risk when material; analytical-reasoning challenge for wrong question, premature closure, confirmation bias, hidden assumptions, contradiction smoothing, false precision, unsupported recommendation, weak sufficiency, and unbounded research; quality-attribute challenge; audience/outcome mismatch challenge; option-evaluation challenge; evidence-confidence challenge; failure-mode challenge; learning/canon candidate, stale-knowledge, correction/retirement, and memory-sync challenge when material; review-side source/client/profile checks; re-review after repair. |
 | Final Editor | Controlled finalization when transformation after approved review is needed; preservation of approved quality attributes; preservation of audience fit and actionability; preservation of selected-approach rationale, Professional Analysis judgment and recommendation, Professional Communication message path, density, caveats, reader action, architecture rationale, accepted risks, and analytical traceability when material; preservation of reusable learning cues without classification; premature-finalization and caveat-loss detection; preservation of evidence-backed caveats and residual risks. |
 | Artist Agent | Frozen visual-output extension for explicitly activated visual branch after visual meaning brief prerequisites; preservation of evidence-backed visual meaning. |

diff --git a/ai-editorial-office/kb/shared_lifecycle_kernel.md b/ai-editorial-office/kb/shared_lifecycle_kernel.md
index 64e62f4..7afc831 100644
--- a/ai-editorial-office/kb/shared_lifecycle_kernel.md
+++ b/ai-editorial-office/kb/shared_lifecycle_kernel.md
@@ -312,17 +312,20 @@ justified.
 - Forbidden context: all old task folders, all pipelines, all role specs, or the
   legacy/private archive by default.
 - Expected outputs: `brief.md`, initial or updated `task-manifest.md`, audience
-  and intended outcome when known or material, optional advisory Task Need
-  Recognition view when material, missing information or preflight blocker.
+  and intended outcome when known or material, requested deliverable and format
+  authority, optional advisory Task Need Recognition view with recommended
+  deliverable when material, missing information or preflight blocker.
 - Stop conditions: unclear objective, unsafe instruction conflict, missing task
   identity, or repository/path ambiguity.
 - Next stage: routing, clarification, or blocked.

 ### Routing

-- Purpose: choose risk, process depth, planning level, pipeline or
+- Purpose: select the deliverable from requested and advisory recommended
+  options, then choose risk, process depth, planning level, pipeline or
   mini-contract, audience/outcome fit, quality priorities, roles, capabilities,
-  active Domain Knowledge Packs when material, gates, and next owner.
+  active Domain Knowledge Packs when material, gates, and next owner. This
+  ordering stays inside Routing; it is not a new lifecycle stage or gate.
 - Minimum required context: `brief.md`, `task-manifest.md`, `AGENTS.md`,
   `/kb/task_statuses.md`, relevant pipeline candidate, and active client profile
   files only when selected.
@@ -335,8 +338,10 @@ justified.
   current `project-state.md`, previous handoff when resuming.
 - Forbidden context: unrelated pipelines, inactive client profiles, role specs
   for unassigned roles, and historical retrospectives as active policy.
-- Expected outputs: `orchestration_plan.md`, updated manifest/status, selected
-  workflow overlay or mini-contract, audience/outcome fit when material,
+- Expected outputs: `orchestration_plan.md`, updated manifest/status, explicit
+  requested/recommended/selected deliverable decision when material, selected
+  workflow overlay or mini-contract chosen for that deliverable,
+  audience/outcome fit when material,
   quality priorities/tradeoffs when material, planning level and options
   considered when material, Chief Editor acceptance/rejection/narrowing of the
   Task Need Recognition recommendations when material, analytical question or
@@ -422,6 +427,7 @@ justified.
   creator, unrelated old drafts, or optional artifacts demanded without a review
   need.
 - Expected outputs: `review.md` with checked scope, independence basis,
+  requested/recommended/selected deliverable challenge when material,
   audience/outcome fit when material, quality-attribute challenge when
   material, evidence/confidence challenge when material, option-evaluation
   challenge when material, analytical-reasoning challenge when material,
diff --git a/ai-editorial-office/kb/task_need_recognition.md b/ai-editorial-office/kb/task_need_recognition.md
index 3f40112..13f602c 100644
--- a/ai-editorial-office/kb/task_need_recognition.md
+++ b/ai-editorial-office/kb/task_need_recognition.md
@@ -4,11 +4,11 @@ This file owns the shared Task Need Recognition capability for AI Editorial
 Office. It defines how available request evidence becomes an advisory view of
 likely task needs before Chief Editor routing.

-It does not own or perform task classification, routing, preflight, risk mode,
-process depth, research depth, review scope, capability activation, Domain Pack
-activation, role assignment, decomposition, planning, lifecycle transition, or
-governance. Those decisions remain with `AGENTS.md`, Chief Editor, and their
-existing canonical owners.
+It does not own or perform selected-deliverable choice, task classification,
+routing, preflight, risk mode, process depth, research depth, review scope,
+capability activation, Domain Pack activation, role assignment, decomposition,
+planning, lifecycle transition, or governance. Those decisions remain with
+`AGENTS.md`, Chief Editor, and their existing canonical owners.

 ## Purpose

@@ -16,6 +16,8 @@ Task Need Recognition helps the office inspect a request before work begins and
 answer, provisionally:

 - what kind of work appears to be present;
+- which deliverable would solve the user's real objective with the least
+  unnecessary burden while preserving required depth, evidence, and use value;
 - which capabilities are likely to matter;
 - which Domain Packs may provide material context;
 - how much research, evidence, and review may be justified;
@@ -94,6 +96,64 @@ Start from available evidence, not a keyword list:
 | Ambiguity and conflict | missing audience/output, mixed intents, incompatible constraints, contradictory evidence | clarification, constrain, uncertainty, or decomposition recommendation |
 | Task structure | divergent deliverables, owners, evidence, risks, domains, validation paths, or sequencing dependencies | split, sequence, or keep-coherent recommendation |

+## Outcome-First Deliverable Recommendation
+
+Before Chief Editor selects a pipeline, recognition should answer the advisory
+question:
+
+> What is the smallest sufficient artifact that best solves the user's actual
+> problem?
+
+This is not permission to substitute a preferred format for the user's request.
+Keep four values distinct whenever deliverable choice is material:
+
+| Field | Meaning |
+| --- | --- |
+| Requested deliverable | The format or artifact named by the user, or `not specified`. |
+| Format authority | `explicit`, `delegated`, `inferred`, or `unknown`; this describes who chose the format, not whether the format is good. |
+| Recommended deliverable | The advisory artifact shape that best fits the outcome and use context. |
+| Selected deliverable | The Chief Editor decision used for pipeline selection and production. |
+
+Evaluate the recommendation from the outcome and use situation rather than a
+format keyword alone:
+
+- the problem the user is actually trying to solve;
+- the decision, action, understanding, comparison, approval, implementation, or
+  reuse the artifact must enable;
+- the audience, channel, presentation context, time available, and expected
+  depth;
+- the minimum structure and evidence needed to make the result sufficient;
+- reader/user effort, maintenance burden, and avoidable production bulk;
+- whether the requested format is essential, explicit, only an example, safely
+  inferred, or delegated to the office.
+
+Possible recommendations include article, report, memo, executive brief,
+checklist, roadmap, FAQ, decision matrix, comparison, presentation,
+spreadsheet, specification, BRD, implementation plan, research report,
+tutorial, reference, interview, dialogue, or mind map. This list is illustrative,
+not a closed taxonomy and not a pipeline list.
+
+Use these decision rules:
+
+1. When the user explicitly requests a deliverable, recommend alternatives only
+   when they add material value, and select the requested deliverable by default.
+2. When the user delegates format choice, recommend and select the strongest
+   outcome-fit deliverable, with a compact reason.
+3. When format is inferred from the goal or use context, keep the inference
+   visible and ask only if plausible formats would produce materially different
+   outcomes or commitments.
+4. When an explicit format appears unable to satisfy the stated outcome, do not
+   replace it silently. Explain the mismatch and use Chief Editor preflight to
+   `ask`, `constrain`, or preserve the requested deliverable with a clearly
+   bounded alternative recommendation.
+5. A vague verb such as `explain`, `help`, or `summarize` does not by itself
+   justify a checklist, matrix, roadmap, or other compressed format. The
+   recommendation must preserve the actual communication job.
+
+The selected deliverable must be recorded before the selected pipeline. The
+pipeline, mode, or mini-contract then follows the selected deliverable; it does
+not retroactively decide what the deliverable should be.
+
 Name negative evidence when it prevents unnecessary depth. For example, a
 simple copyedit that happens to mention security terms has no security-sensitive
 claim, asset, threat, control, behavior change, or review consequence and
@@ -256,6 +316,9 @@ Record the smallest useful view in `brief.md`, `orchestration_plan.md`, or
 ```markdown
 ## task need recognition
 - observed request signals:
+- requested deliverable:
+- format authority: explicit / delegated / inferred / unknown
+- recommended deliverable and outcome-fit reason:
 - likely primary task type:
 - material secondary aspects:
 - likely capabilities and why:
@@ -268,7 +331,10 @@ Record the smallest useful view in `brief.md`, `orchestration_plan.md`, or
 - decomposition recommendation:
 - confidence and negative evidence:
 - explicit non-decision:
-- Chief Editor decision or next question:
+- Chief Editor deliverable decision: respect_requested / select_recommended /
+  ask_before_change / constrain_with_explanation
+- selected deliverable:
+- Chief Editor routing decision or next question:
 ```

 Separate observed signals from recommendations. Record the Chief Editor
@@ -293,8 +359,8 @@ material. For compact work, combine or omit fields that add no decision value.

 | Role | Responsibility |
 | --- | --- |
-| Intake Agent | Capture observed request evidence and prepare the initial advisory view when material; do not route or activate. |
-| Chief Editor | Challenge evidence, accept/reject/narrow recommendations, make every routing/preflight/activation/depth/decomposition decision, and record the result. |
+| Intake Agent | Capture observed request evidence, requested deliverable, format authority, and the initial advisory view when material; do not select the deliverable, route, or activate. |
+| Chief Editor | Challenge evidence, accept/reject/narrow recommendations, select the deliverable before the pipeline, make every routing/preflight/activation/depth/decomposition decision, and record the result. |
 | Research Agent | Verify missing domain/current-state evidence when assigned; do not retroactively present research as an intake decision. |
 | Writer Agent / UX Writer | Follow the approved route; flag new evidence that invalidates the recognition assumptions. |
 | Review Agent | When downstream scope materially depends on recognition, challenge evidence, negative cases, proportionality, uncertainty, owner boundaries, and non-decision. |
@@ -309,6 +375,14 @@ When recognition materially affected the route, Review Agent may ask:

 - Are observed signals separated from inference, recommendation, and Chief
   Editor decision?
+- Are requested, recommended, and selected deliverables distinct, and is format
+  authority recorded?
+- Does the recommended deliverable minimize avoidable burden while remaining
+  sufficient for the intended outcome, use context, and evidence need?
+- Was an explicit requested deliverable preserved unless the user agreed to a
+  change, or was any unresolved mismatch routed through preflight rather than
+  silently overridden?
+- Was the pipeline chosen after and because of the selected deliverable?
 - Does the primary task type follow outcome/work surface rather than keywords?
 - Are material secondary aspects preserved without forcing one class?
 - Are capability and pack recommendations tied to their actual owner criteria?
@@ -330,6 +404,10 @@ Stop, narrow, or return to Chief Editor when:
 - the request cannot be distinguished from a different plausible task without
   material clarification;
 - a recommendation depends only on keywords or topic names;
+- requested and recommended deliverables have been silently merged;
+- an explicit requested format would be replaced without user agreement or a
+  visible preflight decision;
+- the proposed artifact is smaller but no longer sufficient for the outcome;
 - a Domain Pack/capability owner would be overridden;
 - the view hides contradictory or negative evidence;
 - a score, threshold, or classifier output is being treated as authority;
@@ -344,9 +422,12 @@ Task Need Recognition does not:

 - create automatic routing, classification, capability activation, Domain Pack
   activation, review level, research level, or planning;
+- silently override an explicit requested deliverable or treat a recommendation
+  as user consent;
 - create a role, pipeline, lifecycle stage, status, gate, task taxonomy,
   framework, store, model, classifier, score, threshold, or dashboard;
-- make task type, risk, depth, pack, capability, split, or next-action decisions;
+- make selected-deliverable, task type, risk, depth, pack, capability, split, or
+  next-action decisions;
 - replace Preflight, Intake Normalization, Professional Analysis, Professional
   Communication, Architecture Review, Engineering Review, Evaluation Signals,
   Evidence Confidence, Domain Pack activation, Review Agent, or Chief Editor;
diff --git a/ai-editorial-office/kb/task_object_model.md b/ai-editorial-office/kb/task_object_model.md
index 1f7df95..29926d3 100644
--- a/ai-editorial-office/kb/task_object_model.md
+++ b/ai-editorial-office/kb/task_object_model.md
@@ -86,7 +86,10 @@ file.
 | `detail_level` | Compact, standard, deep, or task-specific depth needed by the audience and outcome. | `orchestration_plan.md`, production notes, review artifacts |
 | `tone_requirements` | Tone, formality, sensitivity, and vocabulary constraints required by reader context and evidence quality. | `brief.md`, relevant KB, production notes |
 | `channel_context` | Publication channel, product context, internal/external use, or task environment. | `brief.md`, `orchestration_plan.md` |
-| `deliverable` | Expected output or artifact set. | `brief.md`, `task-manifest.md` |
+| `requested_deliverable` | Output or artifact explicitly requested by the user, safely inferred from the request, or `not specified`. | `brief.md`, intake handoff, `orchestration_plan.md` |
+| `deliverable_format_authority` | Whether format choice is `explicit`, `delegated`, `inferred`, or `unknown`. | `brief.md`, `orchestration_plan.md` |
+| `recommended_deliverable` | Advisory smallest sufficient artifact that best fits the actual outcome and use context. | Task Need Recognition view in `brief.md` or `orchestration_plan.md` |
+| `selected_deliverable` | Chief Editor decision used for production and chosen before `selected_workflow`; an explicit requested format is preserved unless the user agrees otherwise. | `orchestration_plan.md`, `task-manifest.md` when a current-state pointer is useful |
 | `quality_priorities` | Selected quality attributes that matter most for this task, such as correctness, actionability, traceability, audience fit, implementation readiness, or reviewability. | `brief.md`, `orchestration_plan.md`, production/review notes |
 | `quality_tradeoffs` | Accepted quality tradeoffs, such as completeness vs brevity or elegance vs implementation value. | `orchestration_plan.md`, Editorial Decision Frame, `review.md` |
 | `source_boundary` | What is source data, instruction, assumption, contradiction, or unknown. | `brief.md`, `orchestration_plan.md`, `research.md`, `sources.md` |
@@ -111,7 +114,7 @@ file.
 | `success_criterion` | How readiness and audience usefulness will be judged for this task. | `brief.md`, `orchestration_plan.md`, `review.md` |
 | `risk_mode` | `low-risk`, `standard`, `high-governance`, or unresolved/blocked until determined. | `task-manifest.md`, `orchestration_plan.md`, `status.md` |
 | `process_depth` | `compact`, `normal`, or `full`. | `task-manifest.md`, `orchestration_plan.md` |
-| `selected_workflow` | Selected pipeline overlay, editorial mode, or task-local mini-contract. | `orchestration_plan.md`, `task-manifest.md` |
+| `selected_workflow` | Selected pipeline overlay, editorial mode, or task-local mini-contract chosen after and for `selected_deliverable`. | `orchestration_plan.md`, `task-manifest.md` |
 | `planning_level` | `trivial`, `standard`, or `strategic` planning depth selected for meaningful decisions. | `orchestration_plan.md`, `task-manifest.md` |
 | `options_considered` | Credible alternatives considered before selecting route, recommendation, or implementation plan. | `orchestration_plan.md`, Editorial Decision Frame, review artifacts |
 | `selected_option` | Chosen approach and why it best serves the task now. | `orchestration_plan.md`, Editorial Decision Frame, final decision |
@@ -140,6 +143,12 @@ file.
 | `post_task_learning` | Compact Knowledge Evolution closure note deciding whether learning stays task-local, becomes feedback/pattern, needs canon update, is stale/conflicting, or is rejected/deferred. Optional. | `final_decision.md`, `feedback.md` |
 | `memory_disposition` | Whether task learning stays local, becomes feedback, becomes a pattern, needs `/about` sync, or needs a separate system update. | `feedback.md`, `final_decision.md`, `kb/feedback_patterns.md` |

+Historical tasks that use one generic `deliverable` field remain valid. For a
+clear explicit-format task with no material alternative, that field may be read
+as both requested and selected. New or materially ambiguous routing must use the
+split fields so a recommendation cannot be mistaken for user intent or Chief
+Editor selection.
+
 ## Artifact Views Over The Task Object

 Artifacts are views over task state. They should not duplicate each other unless
@@ -148,10 +157,10 @@ requires it.

 | Artifact | Task-object responsibility |
 | --- | --- |
-| `brief.md` | Defines objective, user request summary, audience, intended outcome, reader context when known, channel/context, deliverable, source boundary, constraints, quality cues when material, success criterion, and an optional initial Task Need Recognition view when routing needs it. |
+| `brief.md` | Defines objective, user request summary, audience, intended outcome, reader context when known, channel/context, requested deliverable and format authority, source boundary, constraints, quality cues when material, success criterion, and an optional initial Task Need Recognition view with advisory recommended deliverable when routing needs it. |
 | `task-manifest.md` | Compact current-state view: task id, selected workflow, active capabilities/roles, active Domain Knowledge Packs when material, actual runtime execution when material and known, current owner/status, artifact inventory, current pointer, constraints, gates, review/finalization state, and next action. |
 | `status.md` | Transition history, blocker history, rationale for state changes, approvals, and recovery path. It must not become a duplicate manifest. |
-| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, planned runtime topology when material, gates, artifact scope, Editorial Decision Frame with Cognitive Bridge, Moments of Insight, and Practical Transformation when material, evidence basis/confidence for material route decisions, and expansion triggers. |
+| `orchestration_plan.md` | Execution contract: requested, recommended, and selected deliverable decision before the selected pipeline or mini-contract; risk mode; process depth; planning level; optional Task Need Recognition view and Chief Editor decision when material; analytical question and assumptions when material; architecture review scope and drivers when material; audience/outcome fit and Reader Outcome Contract when material; quality priorities/guardrails/tradeoffs when material; options considered when material; active capabilities; active Domain Knowledge Packs when material; active roles; planned runtime topology when material; gates; artifact scope; Editorial Decision Frame with Cognitive Bridge, Moments of Insight, and Practical Transformation when material; evidence basis/confidence for material route decisions; and expansion triggers. |
 | `research.md` | Research scope, verified facts, interpretations, assumptions, hypotheses, contradictions, diagnostic evidence, source confidence, evidence class, sufficiency judgment, and evidence limits. |
 | `sources.md` | Source inventory, provenance, freshness, reliability, relevance, and evidence class. |
 | `facts.md` | Fact-level evidence when needed by factual sensitivity, downstream review, or high-governance scope. |
diff --git a/ai-editorial-office/pipelines/article_pipeline.md b/ai-editorial-office/pipelines/article_pipeline.md
index 8c6117f..99ff7de 100644
--- a/ai-editorial-office/pipelines/article_pipeline.md
+++ b/ai-editorial-office/pipelines/article_pipeline.md
@@ -22,7 +22,11 @@ The pipeline is markdown-first, artifact-backed, and restartable from `/tasks/TA

 ## when to use

-Use this pipeline when the requested output is an article-like text that needs editorial structure, source-aware writing, and review before finalization.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is an article-like text that needs editorial
+structure, source-aware writing, and review before finalization. An article
+mention alone does not select this pipeline when format choice was delegated or
+only illustrative.

 Use it when:

@@ -55,7 +59,7 @@ only maps Article Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize raw request into task artifacts |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
 | Writing | `writer_agent` | `/agents/writer_agent.md` | Create outline, draft, writer notes, and claims-used |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate draft and artifacts |
diff --git a/ai-editorial-office/pipelines/research_pipeline.md b/ai-editorial-office/pipelines/research_pipeline.md
index 0b9af9a..c49f026 100644
--- a/ai-editorial-office/pipelines/research_pipeline.md
+++ b/ai-editorial-office/pipelines/research_pipeline.md
@@ -14,6 +14,10 @@ conditional and claim-driven, not automatic.

 ## when to use

+Chief Editor selects this evidence pipeline only after the intended outcome and
+selected deliverable are known enough to define what evidence that deliverable
+needs. Research need does not decide the final artifact format retroactively.
+
 Use this pipeline when any of these are true:

 - the task needs factual claims, dates, names, numbers, quotes, product behavior, policy details, market context, or source-backed reasoning;
@@ -49,7 +53,7 @@ only maps Research Pipeline responsibilities to current roles.
 | Stage responsibility | Required role | Agent spec |
 | --- | --- | --- |
 | Intake package, if not already complete | `intake_agent` | `/agents/intake_agent.md` |
-| Pipeline selection and status governance | `chief_editor` | `/agents/chief_editor.md` |
+| Deliverable-first pipeline selection and status governance | `chief_editor` | `/agents/chief_editor.md` |
 | Research execution | `research_agent` | `/agents/research_agent.md` |
 | Downstream drafting, if research is sufficient for article or editorial copy | `writer_agent` | `/agents/writer_agent.md` |
 | Downstream UX copy, if research is sufficient for product-language work | `ux_writer` | `/agents/ux_writer.md` |
diff --git a/ai-editorial-office/pipelines/review_pipeline.md b/ai-editorial-office/pipelines/review_pipeline.md
index 877ddbb..82dc4ce 100644
--- a/ai-editorial-office/pipelines/review_pipeline.md
+++ b/ai-editorial-office/pipelines/review_pipeline.md
@@ -57,8 +57,10 @@ When downstream scope materially depends on Task Need Recognition, review
 applies `/kb/task_need_recognition.md` to challenge observed evidence,
 recommendation-versus-Chief Editor decision separation, keyword-only or forced
 classification, negative evidence, risk/consequence, proportionality,
-ambiguity, uncertainty, decomposition basis, owner boundaries, and
-non-automation. This is part of the
+ambiguity, uncertainty, decomposition basis, requested/recommended/selected
+deliverable separation, format authority, explicit-intent preservation,
+outcome-fit sufficiency, pipeline-after-deliverable ordering, owner boundaries,
+and non-automation. This is part of the
 existing review gate, not a new routing or review gate.

 When reviewed work shows wrong-task drift, weak evidence, hidden assumptions,
@@ -271,7 +273,7 @@ compact evidence. Missing evidence for material claims should produce
 | `task-manifest.md` | Compact current state and review outcome fields | all roles | never for active tasks |
 | `status.md` | Detailed status/history and blockers | all roles | never for active tasks |
 | `brief.md` | Review scope and acceptance criteria | review_agent, chief_editor | never for review |
-| `orchestration_plan.md` | Selected production pipeline and review gates | review_agent, chief_editor | never after orchestration starts |
+| `orchestration_plan.md` | Requested/recommended/selected deliverable decision, selected production pipeline, and review gates | review_agent, chief_editor | never after orchestration starts |
 | reviewed material | The artifact being independently reviewed | review_agent, final_editor | never for review |
 | `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Reader Review Lens when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
 | review handoff | Delta-transfer to next valid role | receiving role | only when no role transition occurs |
@@ -450,7 +452,10 @@ It does not restate detailed review logic. Review Agent owns:
 - Task Need Recognition challenge, including hidden request evidence,
   keyword-only or forced classification, missing negative evidence,
   disproportionate depth, hidden ambiguity/uncertainty, unsupported
-  decomposition, owner override, and recommendations treated as decisions;
+  decomposition, requested/recommended/selected deliverable conflation, silent
+  explicit-format override, insufficient artifact recommendation, pipeline
+  selection before the deliverable decision, owner override, and
+  recommendations treated as decisions;
 - Domain Knowledge Pack challenge, including weak activation, unsupported
   source register use, boundary drift, stale-if trigger neglect, canonical
   owner override, and misuse as policy, capability ownership, role, pipeline,
@@ -483,7 +488,7 @@ Quality gates are mandatory and artifact-backed.
 | Reader Review gate | When material, understanding, retention, application, Cognitive Bridge, Learning Design sequence, and reader burden have deterministic statuses tied to the Reader Outcome Contract and exact artifact evidence | missing bridge, headings substituted for memorable ideas, vague Practical Transformation, academic or jargon overload that blocks the outcome, or a taste preference presented as a finding |
 | Companion Pass gate | Reader-facing work is natural and concrete enough for the intended reader while preserving precision, evidence, caveats, boundaries, and traceability | taxonomy dump, synthetic expert performance, avoidable academic distance, unsupported friendliness, precision loss, or substantive repair deferred to Final Editor |
 | Professional-communication gate | Communication transfer is sufficient when message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, or caveat-preserving reader transfer is material | buried main point, wrong density, unclear ask or next action, hidden caveat, misleading compression, weak explanation, technical ambiguity, or unreviewable reader path |
-| Task Need Recognition gate | When downstream scope materially depends on recognition, observed evidence, recommendations, negative evidence, uncertainty, decomposition basis, explicit non-decision, and Chief Editor decision are distinct, proportionate, and owner-safe | keyword-only or forced type, hidden ambiguity, missing negative evidence, unsupported split, score/threshold authority, automatic routing/activation/depth, or Chief Editor decision absent |
+| Task Need Recognition gate | When downstream scope materially depends on recognition, observed evidence, recommendations, negative evidence, uncertainty, decomposition basis, explicit non-decision, and Chief Editor decision are distinct, proportionate, and owner-safe; when deliverable choice is material, requested, recommended, and selected deliverables are distinct, format authority is visible, the selected artifact is sufficient for the actual outcome, explicit user intent is respected, any alternative or unresolved mismatch is explained, and the pipeline was chosen afterward for the selected deliverable | keyword-only or forced type, hidden ambiguity, missing negative evidence, unsupported split, score/threshold authority, automatic routing/activation/depth, Chief Editor decision absent, silent format substitution, requested/recommended conflation, unjustified alternative, smallest-but-insufficient artifact, missing selected deliverable, or pipeline-first routing |
 | Quality-attribute gate | Priority quality attributes are sufficient for task risk and outcome | optimized for wrong quality, unresolved tradeoff, lost precision/actionability/traceability, or unreviewable artifact |
 | Knowledge Evolution gate | Learning, pattern, canon, stale-knowledge, correction/retirement, memory-disposition, Memory Hygiene Intelligence, and advisory Evaluation Signal claims are evidenced, scoped, owned, non-duplicative, proportionate, and reviewable; feedback/outcome claims preserve classification vs disposition, affected area, applicability, contradictions, bounded action, and non-promotion; memory claims preserve canonical source, represented fact, materiality, purpose/sensitivity/value, exact-copy or compact-summary branch, correction/compression/retirement/omission/deferral/no-sync rationale, branch validation, unique context, bounded growth, and non-automation; signal views preserve decision question, comparison window, denominator/exposure when material, missing cases, alternatives, confidence, qualitative judgment, and explicit non-decision | task-local note promoted without evidence, feedback classification treated as automatic learning, no owner, duplicate rule, privacy risk, `/about` treated as canon, stale guidance handled by silent deletion, exact copy edited independently, misleading summary compression, sensitive/task-local propagation, context-erasing consolidation/retirement, unchecked no-sync, automatic memory write/disposition, activity/activation treated as value, unlike comparisons, hidden contradictions, score/KPI/target/rank/maturity use, individual monitoring, or automatic action |
 | Domain Knowledge Pack gate | Active pack use is justified, sourced, bounded, current enough, and subordinate to canonical owners; claimed benefit or burden also traces to actual sections used, task effect evidence, confidence, complexity cost, and non-promotion when material | weak activation, missing source register support, boundary drift, stale-if trigger ignored, activation treated as proof of value, unsupported effect claim, pack treated as policy/capability/role/pipeline/gate, or mandatory artifact creep |
@@ -506,6 +511,10 @@ allow the review stage to close, and the review-specific packet is current:
   statement that route-validity assumptions still hold;
 - when Reader Review is material, `review.md` records all applicable Reader
   Review criteria, evidence, reader consequences, and bounded repair routing;
+- when deliverable choice is material, `review.md` records the applicable
+  requested/recommended/selected, format-authority, sufficiency,
+  explicit-intent, alternative/mismatch, and pipeline-ordering checks inside
+  the existing review gate and cites the orchestration decision;
 - when material is reader-facing, `review.md` records Companion Pass and routes
   substantive repair to Writer Agent before approval;
 - conditional review artifacts exist when their depth triggers apply;
@@ -525,6 +534,8 @@ checks to the shared restart packet:
 - review is the active stage or review is required before the next stage;
 - reviewed material, selected production pipeline, and latest handoff are
   identified;
+- requested and selected deliverables, plus the advisory recommendation when
+  material, are identifiable in the orchestration record;
 - Review Agent independence from the material creator is clear;
 - unsupported, contradicted, missing, stale, or untraceable claims are visible;
 - the next incomplete validation step is clear.
diff --git a/ai-editorial-office/pipelines/social_pipeline.md b/ai-editorial-office/pipelines/social_pipeline.md
index cdbdf60..43ba0c1 100644
--- a/ai-editorial-office/pipelines/social_pipeline.md
+++ b/ai-editorial-office/pipelines/social_pipeline.md
@@ -17,7 +17,10 @@ The pipeline is markdown-first, artifact-backed, deterministic, and restartable

 ## when to use

-Use this pipeline when the requested output is short-form editorial or promotional copy adapted to one or more platforms.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is short-form editorial or promotional copy
+adapted to one or more platforms. A short-form example does not select this
+pipeline when format choice was delegated or only illustrative.

 Use it when:

@@ -48,7 +51,7 @@ only maps Social Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, platform target, audience, constraints, and missing information |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when required | `research_agent` | `/agents/research_agent.md` | Create evidence base and claim traceability |
 | Writing | `writer_agent` | `/agents/writer_agent.md` | Create platform-adapted short-form draft and claim usage notes |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate copy, artifacts, tone, traceability, and governance compliance |
diff --git a/ai-editorial-office/pipelines/ux_writing_pipeline.md b/ai-editorial-office/pipelines/ux_writing_pipeline.md
index 8db4e42..0f1c2b5 100644
--- a/ai-editorial-office/pipelines/ux_writing_pipeline.md
+++ b/ai-editorial-office/pipelines/ux_writing_pipeline.md
@@ -21,7 +21,11 @@ The pipeline is markdown-first, artifact-backed, deterministic, and restartable

 ## when to use

-Use this pipeline when the requested output is product-facing copy that appears in or around an interface, product flow, onboarding path, notification, validation state, or user guidance surface.
+Use this pipeline when the selected deliverable, recorded after the
+outcome-first deliverable decision, is product-facing copy that appears in or
+around an interface, product flow, onboarding path, notification, validation
+state, or user guidance surface. A UX example alone does not select this
+pipeline when format choice was delegated or only illustrative.

 Use it when:

@@ -54,7 +58,7 @@ only maps UX Writing Pipeline responsibilities to current roles.
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
 | Intake | `intake_agent` | `/agents/intake_agent.md` | Normalize request, supplied UI context, and missing information |
-| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select pipeline, assign roles, maintain status, make final decision |
+| Orchestration and governance | `chief_editor` | `/agents/chief_editor.md` | Select deliverable, then pipeline; assign roles, maintain status, make final decision |
 | Research, when facts or product context need verification | `research_agent` | `/agents/research_agent.md` | Create evidence base for factual or product claims |
 | UX writing | `ux_writer` | `/agents/ux_writer.md` | Create product-facing copy and UX writing artifacts |
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate UX copy and artifacts |
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/brief.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/brief.md
new file mode 100644
index 0000000..4772727
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/brief.md
@@ -0,0 +1,47 @@
+# Brief
+
+## Task
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- Goal: add outcome-first deliverable selection before pipeline selection while
+  preserving evidence discipline, governance, traceability, review, and the
+  existing architecture.
+- Source instruction: user-provided Codex task dated 2026-07-13.
+
+## User Objective
+
+Make AI Editorial Office determine whether the initially mentioned artifact is
+the best way to solve the user's real problem before it chooses how to produce
+that artifact.
+
+## Deliverable
+
+- Requested deliverables: canonical implementation, implementation report,
+  complete diff, modified-canonical-files summary, architectural decision
+  explanation, and synthetic tests.
+- Format authority: `explicit`.
+- Advisory recommended deliverable: the requested bounded patch and evidence
+  package are already sufficient.
+- Selected deliverable: same as requested; no alternative format needed.
+
+## Constraints
+
+- Do not redesign the system.
+- Do not add a permanent role, pipeline, lifecycle stage, gate, score, or
+  mandatory standalone artifact.
+- Do not silently weaken explicit user format authority.
+- Do not modify unrelated systems or pre-existing untracked task material.
+- Keep Task Need Recognition advisory and Chief Editor authoritative.
+- Keep independent review mandatory.
+
+## Acceptance Criteria
+
+- Requested, recommended, and selected deliverables are distinct in canon.
+- Format authority is explicit and silent override is forbidden.
+- Chief Editor selects the deliverable before the pipeline.
+- Intake captures request evidence without selecting the deliverable.
+- Review verifies artifact suitability, explicit-intent preservation,
+  explanation of alternatives, and pipeline ordering.
+- Synthetic cases cover the five required examples and material negative cases.
+- `/about` exact-copy package remains synchronized.
+- Existing validators and smoke tests pass.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final.md
new file mode 100644
index 0000000..5fc9f5b
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final.md
@@ -0,0 +1,14 @@
+# Final Delivery
+
+Task: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+Review outcome: `approved`
+
+## Delivery package
+
+- [Implementation report](implementation-report.md)
+- [Complete diff](complete-diff.md)
+- [Synthetic smoke-test specification](../../tests/outcome_first_deliverable_selection_smoke_test.md)
+- [Executable test](../../tests/test_outcome_first_deliverable_selection.sh)
+- [Independent review](review.md)
+
+The canonical patch and tests were not changed during finalization.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final_decision.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final_decision.md
new file mode 100644
index 0000000..db87ea2
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/final_decision.md
@@ -0,0 +1,56 @@
+# Final Decision
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- Chief Editor decision: `ready_for_delivery`
+- Review outcome: `approved`
+- Blocking findings: none
+- Human approval required before local delivery: no
+- Publication or GitHub push authorized: no
+
+## Governance Basis
+
+- The implementation extends existing Task Need Recognition, Chief Editor,
+  task-object, lifecycle, role, pipeline, template, and Review owners.
+- Requested, recommended, and selected deliverables and format authority remain
+  distinct.
+- Explicit user intent cannot be silently overridden; material mismatch uses
+  existing preflight.
+- Selected deliverable precedes and governs pipeline selection.
+- No permanent role, pipeline, lifecycle stage, gate, score, taxonomy, or
+  mandatory standalone operational artifact was added.
+- Independent review approved the package after OFD-001 was repaired by folding
+  outcome-first checks into the existing Task Need Recognition gate.
+
+## Validation Basis
+
+- Outcome-first executable regression: pass; ten synthetic cases present.
+- Task lifecycle smoke test: 14/14 pass.
+- Task-pack generator smoke test: 13/13 pass.
+- `/about` exact-copy validation: 20/20 pass.
+- Current task lifecycle: 0 blockers, 0 warnings.
+- Forbidden standalone gate label: absent from active canon and `/about`.
+- `git diff --check`: pass.
+
+## Delivery Artifacts
+
+- `implementation-report.md`
+- `complete-diff.md`, generated as the final mechanical snapshot after this
+  decision; no implementation content may change afterward without renewed
+  review
+- `final.md`
+- `review.md`
+- `tests/outcome_first_deliverable_selection_smoke_test.md`
+- `tests/test_outcome_first_deliverable_selection.sh`
+
+## Scope Decision
+
+Pre-existing unrelated untracked `TASKS/`, release/research/task packs, and
+`diff_intake.md` remain outside scope and untouched.
+
+## Learning And Memory Disposition
+
+- Outcome-first deliverable selection is now canonical in the repository.
+- Real-world outcome improvement remains unproven; synthetic validation must
+  not be promoted as user-value evidence.
+- No additional memory sync, backlog item, new role, or architecture update is
+  required by this task.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-finalization-final-editor-to-chief-editor.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-finalization-final-editor-to-chief-editor.md
new file mode 100644
index 0000000..3afce0f
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-finalization-final-editor-to-chief-editor.md
@@ -0,0 +1,35 @@
+# Handoff: Final Editor To Chief Editor
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- From: Final Editor
+- To: Chief Editor
+- Review outcome: `approved`
+- Blocking findings: none; OFD-001 resolved after one bounded repair and
+  bounded re-review
+
+## Changed artifacts
+
+- `implementation-report.md` — updated only `## Review state` to record the
+  approved independent review, resolved OFD-001 repair, and absence of blockers.
+- `final.md` — created as the compact delivery pointer.
+- `handoff-finalization-final-editor-to-chief-editor.md` — created as this
+  task-local delta transfer.
+
+## Intentionally unchanged
+
+- Canonical patch: untouched.
+- Tests and synthetic case expectations: untouched.
+- `review.md`, `task-manifest.md`, `status.md`, architecture decisions, and
+  scope: untouched.
+- No finalization notes or checklist were created.
+
+## Chief Editor next action
+
+1. Generate `complete-diff.md` from the final reviewed snapshot as the last
+   mechanical closeout step.
+2. Verify the delivery package, record the final governance decision, and make
+   any required lifecycle-state updates.
+3. Stop and investigate if the generated diff exposes unexpected scope or a
+   changed canonical/test snapshot.
+
+Publication or GitHub push is not authorized by this finalization handoff.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-implementation-writer-agent-to-review-agent.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-implementation-writer-agent-to-review-agent.md
new file mode 100644
index 0000000..159f107
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-implementation-writer-agent-to-review-agent.md
@@ -0,0 +1,43 @@
+# Handoff: Implementation To Review Agent
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- From: Writer / implementation function
+- To: Review Agent
+- Status recommendation: `review`
+- Reviewed target: current repository diff plus task-local implementation report
+  and synthetic tests
+
+## Required Review
+
+- Verify the patch adds deliverable selection before pipeline selection.
+- Verify requested, recommended, and selected deliverables and format authority
+  are not conflated.
+- Verify explicit user intent cannot be silently overridden and material
+  mismatch routes through existing preflight.
+- Verify Task Need Recognition stays advisory and Chief Editor stays the only
+  deliverable/pipeline decision owner.
+- Verify Intake, production roles, Review, Final Editor, task model, lifecycle,
+  templates, and affected pipelines are consistent.
+- Verify the required synthetic positive and negative cases are deterministic.
+- Verify no new role, pipeline, lifecycle stage, gate, score, taxonomy, or
+  mandatory standalone operational artifact was created.
+- Verify `/about` exact copies and existing validators remain valid.
+- Verify unrelated pre-existing untracked files are outside scope.
+
+## Evidence
+
+- `brief.md`
+- `orchestration_plan.md`
+- `implementation-report.md`
+- `tests/outcome_first_deliverable_selection_smoke_test.md`
+- `tests/test_outcome_first_deliverable_selection.sh`
+- current `git diff`
+
+## Boundaries
+
+- Review only; do not edit or rewrite repository files.
+- Record exact blocking/required findings with file and line evidence.
+- Suggestions that do not block the stated acceptance criteria must remain
+  non-blocking.
+- Complete diff is intentionally generated after bounded repairs so it reflects
+  the final reviewed snapshot.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-repair-writer-agent-to-review-agent.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-repair-writer-agent-to-review-agent.md
new file mode 100644
index 0000000..1bb900a
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-repair-writer-agent-to-review-agent.md
@@ -0,0 +1,32 @@
+# Handoff: OFD-001 Repair To Review Agent
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- From: Writer / implementation function
+- To: Review Agent
+- Status recommendation: `review`
+- Repair source: `review.md`, finding `OFD-001`
+
+## Changed Scope
+
+- `pipelines/review_pipeline.md`: standalone outcome-first gate row removed;
+  criteria and blockers folded into existing Task Need Recognition gate;
+  completion wording now records checks inside the existing review gate.
+- `about/review_pipeline.md`: exact mirror resynchronized.
+- `tests/test_outcome_first_deliverable_selection.sh`: negative assertion added
+  for the forbidden standalone gate label.
+
+## Validation
+
+- Outcome-first executable regression: pass.
+- Forbidden standalone label search across active canon and `/about`: pass.
+- Lifecycle smoke test: 14/14 pass.
+- Task-pack generator smoke test: 13/13 pass.
+- `/about` exact-copy check: 20/20 pass.
+- Current task lifecycle validator: 0 blockers, 0 warnings.
+- `git diff --check`: pass.
+
+## Re-review Boundary
+
+Re-review only the three changed files, the no-new-gate statement in
+`implementation-report.md`, and the validation evidence unless the repair
+invalidates a broader approved check.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-approval-review-agent-to-final-editor.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-approval-review-agent-to-final-editor.md
new file mode 100644
index 0000000..5e2b432
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-approval-review-agent-to-final-editor.md
@@ -0,0 +1,23 @@
+# Handoff: Approved Review To Final Editor
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- From: Review Agent
+- To: Final Editor
+- Review outcome: `approved`
+- Review artifact: `review.md`
+- Blocking findings: none; OFD-001 resolved in bounded re-review
+
+## Allowed Finalization
+
+- Update only the `Review state` section of `implementation-report.md` to record
+  approved independent review and the resolved bounded finding.
+- Create compact `final.md` pointing to the implementation report, complete
+  diff (generated as the last mechanical closeout step), tests, and review.
+- Create a compact finalization handoff to Chief Editor.
+
+## Forbidden
+
+- Do not change canonical files, tests, synthetic case expectations, scope,
+  claims, architecture decisions, or review verdict.
+- Do not add new deliverable-selection logic during finalization.
+- Do not treat publication or GitHub push as authorized.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-review-agent-to-writer-agent.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-review-agent-to-writer-agent.md
new file mode 100644
index 0000000..432f1b2
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/handoff-review-review-agent-to-writer-agent.md
@@ -0,0 +1,29 @@
+# Handoff: Review Agent To Writer
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- From: Review Agent
+- To: Writer / implementation function
+- Review outcome: `changes_requested`
+- Source: `review.md`, finding `OFD-001`
+
+## Required Repair
+
+- Fold outcome-first deliverable criteria and blockers into the existing Task
+  Need Recognition gate row in `pipelines/review_pipeline.md`.
+- Remove the standalone `Outcome-first deliverable gate` label and replace the
+  completion wording with criteria inside the existing review gate.
+- Resynchronize `about/review_pipeline.md`.
+- Add a negative assertion to
+  `tests/test_outcome_first_deliverable_selection.sh` that rejects the
+  standalone gate label.
+
+## Bounded Re-review Scope
+
+- `pipelines/review_pipeline.md`
+- `about/review_pipeline.md`
+- `tests/test_outcome_first_deliverable_selection.sh`
+- validation rerun and truthfulness of the no-new-gate statement in
+  `implementation-report.md`
+
+Do not change the approved deliverable model, role ownership, template ordering,
+synthetic case expectations, or unrelated files.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/implementation-report.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/implementation-report.md
new file mode 100644
index 0000000..b9e5ca0
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/implementation-report.md
@@ -0,0 +1,191 @@
+# Отчёт о реализации Outcome-First Deliverable Selection
+
+Дата: 2026-07-13
+Task: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+
+## Результат
+
+AI Editorial Office теперь различает решение о том, **что произвести**, и
+решение о том, **как это произвести**.
+
+Рабочий порядок зафиксирован так:
+
+```text
+запрос и реальная цель
+-> requested / recommended / selected deliverable
+-> pipeline, mode или task-local mini-contract
+-> production
+-> independent review
+```
+
+Изменение расширяет существующую архитектуру. Новые постоянные роли, pipelines,
+lifecycle stages, gates, scores и обязательные отдельные артефакты не созданы.
+
+## Архитектурные решения
+
+### 1. Canonical owner — Task Need Recognition
+
+`kb/task_need_recognition.md` уже отвечает за advisory interpretation запроса до
+Chief Editor routing. Поэтому в него добавлена `Outcome-First Deliverable
+Recommendation`, а не новый Deliverable/Format Agent или отдельный framework.
+
+Capability оценивает:
+
+- реальную проблему и нужный outcome;
+- действие, решение, понимание, сравнение, approval или implementation, которые
+  должен поддержать результат;
+- audience, channel, use context и достаточную глубину;
+- минимальный достаточный artifact shape;
+- reader/user effort, maintenance burden и лишний production bulk;
+- степень свободы выбора формата.
+
+Список возможных deliverables остаётся иллюстративным и не становится закрытой
+taxonomy или списком pipelines.
+
+### 2. Четыре раздельных значения
+
+Task object и orchestration теперь различают:
+
+- `requested_deliverable` — что запросил или обозначил пользователь;
+- `deliverable_format_authority` — `explicit`, `delegated`, `inferred` или
+  `unknown`;
+- `recommended_deliverable` — advisory recommendation smallest sufficient
+  artifact;
+- `selected_deliverable` — решение Chief Editor, которое используется в
+  production и предшествует pipeline selection.
+
+Для старых task packs оставлена совместимость: одно поле `deliverable` можно
+читать как requested+selected только для очевидной explicit-format задачи без
+материальной альтернативы.
+
+### 3. Explicit user intent не переопределяется молча
+
+Добавлены четыре Chief Editor decisions:
+
+- `respect_requested`;
+- `select_recommended`;
+- `ask_before_change`;
+- `constrain_with_explanation`.
+
+Explicit requested deliverable сохраняется по умолчанию. Альтернативу можно
+предложить, но нельзя незаметно подменить. Если формат не способен выполнить
+заявленный outcome, задача возвращается в существующий Preflight Gate через
+`ask` или `constrain`, а не получает скрытый override.
+
+### 4. Pipeline следует за selected deliverable
+
+В `orchestration_plan_template.md` блок `outcome-first deliverable decision`
+физически расположен перед `selected pipeline`. Article, Social, UX Writing и
+Research Pipeline теперь опираются на уже выбранный deliverable или его
+evidence need, а не на первое упоминание формата в запросе.
+
+Если подходящего специального pipeline нет, Chief Editor использует существующий
+mode или ограниченный task-local mini-contract. Новый pipeline только ради memo,
+roadmap, presentation или matrix не создаётся.
+
+### 5. Ответственность существующих ролей
+
+- Intake Agent фиксирует requested deliverable, format authority и advisory
+  recommendation, но не выбирает результат.
+- Chief Editor выбирает deliverable, затем pipeline и фиксирует решение в
+  `orchestration_plan.md`.
+- Writer Agent и UX Writer производят selected deliverable и останавливаются при
+  конфликте request/recommendation/selection/pipeline.
+- Review Agent проверяет outcome fit, sufficiency, explicit-intent preservation,
+  объяснение alternative/override и правильный порядок pipeline selection.
+- Final Editor сохраняет reviewed selected deliverable и не решает конфликт
+  форматов во время cleanup.
+
+## Изменённые канонические компоненты
+
+### Entry и governance
+
+- `/AGENTS.md`
+- `ai-editorial-office/AGENTS.md`
+
+### Canonical knowledge owners
+
+- `kb/task_need_recognition.md`
+- `kb/task_object_model.md`
+- `kb/capability_registry.md`
+- `kb/shared_lifecycle_kernel.md`
+
+### Существующие роли
+
+- `agents/intake_agent.md`
+- `agents/chief_editor.md`
+- `agents/writer_agent.md`
+- `agents/ux_writer.md`
+- `agents/review_agent.md`
+- `agents/final_editor.md`
+
+### Существующие pipelines
+
+- `pipelines/article_pipeline.md`
+- `pipelines/social_pipeline.md`
+- `pipelines/ux_writing_pipeline.md`
+- `pipelines/research_pipeline.md`
+- `pipelines/review_pipeline.md`
+
+### Existing templates
+
+- `templates/artifacts/orchestration_plan_template.md`
+- `templates/artifacts/task_manifest_template.md`
+- `templates/tasks/article_task_template.md`
+- `templates/tasks/social_task_template.md`
+- `templates/tasks/ux_writing_task_template.md`
+- `templates/tasks/review_task_template.md`
+
+### Tests и documentation
+
+- `tests/outcome_first_deliverable_selection_smoke_test.md`
+- `tests/test_outcome_first_deliverable_selection.sh`
+- `tests/README.md`
+
+### Exact-copy memory package
+
+Синхронизированы 12 существующих `/about` mirrors: `AGENTS.md`, шесть role
+specs и пять pipeline specs. Новые `/about`-файлы не создавались; размер пакета
+остался 20 файлов.
+
+## Synthetic test coverage
+
+Десять кейсов проверяют:
+
+1. explicit article остаётся article;
+2. delegated learning request получает learning roadmap;
+3. bare `explain` не может быть заменён checklist только ради краткости;
+4. presentation use context поддерживает presentation;
+5. compare outcome поддерживает comparison matrix;
+6. management persuasion поддерживает decision memo;
+7. requirements request различает BRD и specification ambiguity;
+8. explicit presentation не заменяется memo;
+9. невозможный format/outcome mismatch возвращается в preflight;
+10. trivial typo repair остаётся compact и не получает лишний governance.
+
+Executable static regression дополнительно проверяет canonical contract,
+физический порядок блоков orchestration template, наличие ровно десяти кейсов и
+отсутствие запрещённых Deliverable/Format Agent или pipeline files.
+
+## Проверки
+
+На текущем implementation snapshot успешно выполнены:
+
+- `git diff --check`;
+- `sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh`;
+- `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` — 14/14;
+- `sh ai-editorial-office/tests/test_task_pack_generator.sh` — 13/13;
+- `sh ai-editorial-office/scripts/check_about_memory_package.sh` — 20/20;
+- lifecycle validation текущего task pack — 0 blockers, 0 warnings.
+
+## Ограничения доказательства
+
+Synthetic tests доказывают coverage контракта и отсутствие архитектурного
+drift, но не доказывают real-world improvement. Практический эффект следует
+проверять на будущих задачах с explicit, delegated и ambiguous format authority
+и сопоставлять выбранный artifact с фактическим пользовательским outcome.
+
+## Review state
+
+Independent Review Agent: `approved` after one bounded repair, `OFD-001`.
+Bounded re-review confirmed the finding resolved; blocking findings: none.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/orchestration_plan.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/orchestration_plan.md
new file mode 100644
index 0000000..daeacf4
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/orchestration_plan.md
@@ -0,0 +1,115 @@
+# Orchestration Plan
+
+## task summary
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- User goal: make the office choose the best artifact for the real objective
+  before selecting a production pipeline.
+- Requested deliverable: canonical implementation, tests, implementation report,
+  complete diff, file summary, and architecture explanation.
+- Format authority: `explicit`.
+- Selected deliverable: same as requested.
+
+## task need recognition
+
+- Observed request signals: bounded architecture extension; existing Task Need
+  Recognition, Chief Editor, orchestration, and Review owners named; explicit
+  forbidden architecture growth; synthetic tests required.
+- Recommended deliverable: bounded canonical patch plus task-local test/report/
+  diff evidence.
+- Likely primary task type: canonical system capability update.
+- Material secondary aspects: architecture fit, Engineering Review, deterministic
+  review, `/about` synchronization.
+- Research/evidence recommendation: source-light repository inspection; no web
+  research required because the design objective and constraints are supplied.
+- Review recommendation: standard independent review with architecture and
+  regression checks.
+- Explicit non-decision: recognition does not select the deliverable, pipeline,
+  role set, status, or review outcome.
+
+## outcome-first deliverable decision
+
+- User problem to solve: extend routing judgment without architecture redesign.
+- Requested deliverable: implementation package defined above.
+- Format authority: `explicit`.
+- Recommended deliverable: same bounded implementation package.
+- Why this is the smallest sufficient outcome-fit artifact: it changes the
+  existing owners, proves behavior with synthetic cases, and returns the exact
+  evidence requested without a release pack or new framework.
+- Decision: `respect_requested`.
+- Selected deliverable: bounded canonical patch, synthetic test,
+  implementation report, and complete diff.
+- Explicit-intent preservation note: no requested artifact is replaced.
+
+## selected pipeline
+
+- Pipeline: `review_pipeline` with a task-local system-update mini-contract.
+- Why it fits the selected deliverable: the task changes markdown canon,
+  templates, and tests; no production pipeline exactly owns repository
+  implementation, while Review Pipeline provides the required independent gate.
+- New pipeline created: no.
+
+## preflight gate
+
+| Field | Decision |
+| --- | --- |
+| Audience | confirmed |
+| Channel or context | confirmed |
+| Selected deliverable | defined |
+| Source boundary | defined |
+| Success criterion | defined |
+| Approval boundary | defined |
+| Missing data strategy | proceed |
+
+- Production may start: yes.
+- Scope boundary: canonical outcome-first integration only; unrelated untracked
+  files remain untouched.
+
+## required roles
+
+| Stage | Role | Required | Notes |
+| --- | --- | --- | --- |
+| Orchestration | Chief Editor | yes | Own deliverable and workflow decision |
+| Implementation | Writer / implementation function | yes | Patch canonical docs/templates/tests |
+| Review | Review Agent | yes | Independent role instance and `review.md` |
+| Final governance | Chief Editor | yes | Close only after approved review |
+
+No Deliverable Agent, Format Agent, or other permanent role is created.
+
+## artifact scope
+
+- Required: brief, manifest, status, orchestration plan, user-requested report
+  and complete diff, independent review, compact final pointer, final decision.
+- Omitted: research pack, claims table, QA checklist, release pack, roadmap,
+  standalone deliverable-selection artifact, new pipeline specification.
+
+## execution order
+
+1. Inspect current owners and constraints.
+2. Extend Task Need Recognition with advisory deliverable recommendation.
+3. Extend Intake, Chief Editor, task model, orchestration, pipeline contracts,
+   production preservation, and Review.
+4. Add synthetic regression cases.
+5. Synchronize `/about` exact copies.
+6. Validate and hand off to an independent Review Agent.
+7. Repair only bounded findings, revalidate, and finalize.
+
+## review requirements
+
+- Verify requested/recommended/selected separation.
+- Verify explicit intent cannot be silently overridden.
+- Verify selected deliverable precedes and governs pipeline choice.
+- Verify a bare `explain` request cannot become a checklist without outcome
+  evidence.
+- Verify no permanent role, pipeline, stage, gate, score, or mandatory artifact
+  was added.
+- Verify tests cover explicit, delegated, inferred, mismatch, and compact cases.
+- Verify unrelated files are untouched and `/about` is synchronized.
+
+## completion criteria
+
+- Required canonical integrations are internally consistent.
+- Synthetic test contract is complete.
+- Existing validators pass.
+- Independent review outcome is `approved`.
+- Report and complete diff are current.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/review.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/review.md
new file mode 100644
index 0000000..faaa842
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/review.md
@@ -0,0 +1,207 @@
+# Independent Review
+
+## Verdict
+
+Status: approved
+
+Reviewer role: `review_agent`
+Reviewed snapshot: current working tree on 2026-07-13, including the latest
+wording fixes in `chief_editor.md`, `intake_agent.md`, and
+`task_need_recognition.md`, the bounded OFD-001 repair, and the resynchronized
+`/about` mirrors.
+
+## Review history
+
+- Round 1 outcome: `changes_requested`.
+- Round 1 finding: OFD-001 identified a separately named
+  `Outcome-first deliverable gate` that conflicted with the no-new-gate task
+  constraint.
+- Bounded re-review: OFD-001 is resolved on the repaired current snapshot; no
+  unaffected Round 1 check was invalidated.
+
+## Independence basis
+
+- This review was performed by a separate Review Agent runtime instance from
+  the Writer / implementation function identified in `task-manifest.md` and
+  `handoff-implementation-writer-agent-to-review-agent.md`.
+- The reviewer did not create the implementation patch, implementation report,
+  smoke-test specification, or executable test.
+- The reviewer changed no canonical, template, pipeline, role, test, report,
+  manifest, status, or handoff file. This `review.md` is the only review output.
+
+## Checked scope
+
+- Authority and task contract: root `AGENTS.md`,
+  `ai-editorial-office/AGENTS.md`, the user-provided task text, `brief.md`,
+  `task-manifest.md`, `status.md`, `orchestration_plan.md`, and the latest
+  implementation-to-review handoff.
+- Canonical ownership and task model: `kb/task_need_recognition.md`,
+  `kb/task_object_model.md`, `kb/capability_registry.md`, and
+  `kb/shared_lifecycle_kernel.md`.
+- Existing role boundaries: Intake Agent, Chief Editor, Writer Agent, UX Writer,
+  Review Agent, and Final Editor.
+- Existing pipeline integration: Article, Social, UX Writing, Research, and
+  Review pipelines.
+- Existing artifact/task templates changed by the patch, including the physical
+  ordering in `orchestration_plan_template.md`.
+- Test evidence: `outcome_first_deliverable_selection_smoke_test.md`,
+  `test_outcome_first_deliverable_selection.sh`, and `tests/README.md`.
+- Delivery evidence: `implementation-report.md`, current repository diff and
+  status, `/about` exact-copy synchronization, validator output, and unrelated
+  untracked paths.
+
+## Deterministic checklist
+
+| Criterion | Status | Evidence | Required action |
+| --- | --- | --- | --- |
+| Requested, recommended, and selected deliverables are separate | pass | `kb/task_need_recognition.md` defines four distinct fields; `kb/task_object_model.md` stores distinct task-object values; the orchestration template records the decision explicitly | none |
+| Format authority and explicit-intent preservation | pass | Canon records `explicit`, `delegated`, `inferred`, and `unknown`; Chief Editor defaults to the explicit request and routes material mismatch through existing preflight | none |
+| Intake remains advisory | pass | `agents/intake_agent.md` may capture/request/recommend but cannot select the deliverable or approve the pipeline | none |
+| Chief Editor remains decision owner | pass | `agents/chief_editor.md`, capability map, lifecycle kernel, and orchestration template assign selected-deliverable and later pipeline decisions to Chief Editor | none |
+| Deliverable decision precedes pipeline selection | pass | `templates/artifacts/orchestration_plan_template.md` places `outcome-first deliverable decision` before `selected pipeline`; executable static check verifies line ordering | none |
+| Production and finalization preserve the selected deliverable | pass | Writer Agent and UX Writer stop on conflicting fields; Final Editor cannot change the reviewed selected deliverable | none |
+| Review checks outcome fit, intent, alternatives, and ordering | pass | Review Agent and Review Pipeline contain deterministic checks and failure conditions for each required dimension | none |
+| Required synthetic cases | pass | Ten cases cover explicit article, delegated choice, invalid checklist substitution for `explain`, presentation use, comparison, decision memo, BRD/spec ambiguity, explicit presentation preservation, mismatch/preflight, and compact typo repair | none |
+| No permanent role, pipeline, lifecycle stage, score, or mandatory standalone operational artifact | pass | No Deliverable/Format Agent or pipeline file exists; the decision is a conditional section in existing orchestration; lifecycle stages and status model are unchanged | none |
+| No new gate | pass | The standalone label is absent from active canon and `/about`; outcome-first criteria and blockers are folded into the existing Task Need Recognition gate at `pipelines/review_pipeline.md:491`, and lines 514-517 record checks inside the existing review gate | none |
+| `/about` synchronization | pass | `check_about_memory_package.sh` reports 20 files and exact canonical copies; all 12 changed mirrors match | none |
+| Validation evidence | pass | All commands listed below passed on the repaired reviewed snapshot | none |
+| Unrelated-scope preservation | pass | Tracked diff is limited to the named integration surface; pre-existing untracked `TASKS/`, release/research/task packs, and `diff_intake.md` remain unmodified and outside the patch | do not stage or edit unrelated paths |
+| Complete-diff delivery artifact | pass for review stage | Manifest and handoff explicitly defer `complete-diff.md` until bounded repairs are complete so it records the final reviewed snapshot | generate only after repair and approval |
+
+## Round 1 finding OFD-001 — resolved in bounded re-review
+
+Round 1 severity: blocking for approval.
+Repair owner: Writer / implementation function.
+
+Resolution: resolved. The Writer / implementation function performed only the
+declared bounded repair. The standalone gate row and completion reference were
+removed, the criteria and blockers were folded into the existing Task Need
+Recognition gate, the `/about` mirror was resynchronized, and the negative
+regression was added.
+
+### Problem
+
+The task contract forbids adding a gate (`brief.md:29-31`), but the Round 1
+canonical Review Pipeline added `Outcome-first deliverable gate` as a distinct row
+(`pipelines/review_pipeline.md:492`). The table states that failure at any gate
+prevents approval (`pipelines/review_pipeline.md:499`), and the completion
+conditions require this newly named gate to pass
+(`pipelines/review_pipeline.md:515-516`). This is an actual new quality gate,
+not merely a review lens or criteria added to the existing gate.
+
+On the Round 1 snapshot, it also made the implementation report's statement
+that no gates were created (`implementation-report.md:21-22`) false.
+
+This paragraph records the Round 1 state. On the repaired snapshot,
+`implementation-report.md:21-22` is accurate.
+
+### Bounded repair scope
+
+1. In `ai-editorial-office/pipelines/review_pipeline.md`, remove the standalone
+   `Outcome-first deliverable gate` row and fold its deterministic criteria and
+   blockers into the existing `Task Need Recognition gate` row, which already
+   owns challenge of recognition evidence and Chief Editor decision separation.
+2. Replace the completion-condition reference to the named gate with a compact
+   requirement that `review.md` records the outcome-first deliverable checks.
+   Keep those checks inside the existing review gate; do not introduce another
+   gate, stage, cycle, status, role, or artifact.
+3. Resynchronize `about/review_pipeline.md` as an exact mirror.
+4. Strengthen `tests/test_outcome_first_deliverable_selection.sh` with a
+   deterministic negative assertion that the forbidden standalone
+   `Outcome-first deliverable gate` label is absent. Keep the existing positive
+   assertions and ten-case suite unchanged.
+
+### Do-not-change area
+
+- Do not weaken or remove requested/recommended/selected separation, format
+  authority, explicit-intent preservation, outcome-fit sufficiency, alternative
+  explanation, preflight mismatch routing, or deliverable-before-pipeline
+  ordering.
+- Do not change the ten synthetic case expectations.
+- Do not add a role, pipeline, lifecycle stage, gate, score, taxonomy,
+  mandatory standalone artifact, or unrelated documentation.
+- Do not touch pre-existing unrelated untracked paths.
+
+### Re-review scope
+
+- Exact diff for `pipelines/review_pipeline.md`,
+  `about/review_pipeline.md`, and
+  `tests/test_outcome_first_deliverable_selection.sh`.
+- Search proving the standalone label is absent from active canonical and
+  `/about` files.
+- Re-run the validations listed below.
+- Confirm `implementation-report.md:21-22` is true after the repair and update
+  only its review-state/validation evidence if finalization requires it.
+
+### Bounded re-review evidence
+
+- `pipelines/review_pipeline.md:491` contains the complete outcome-first
+  criteria and blockers inside the pre-existing Task Need Recognition gate.
+- `pipelines/review_pipeline.md:514-517` requires the checks to be recorded
+  inside the existing review gate without naming or creating another gate.
+- Exact-label search across root/office `AGENTS.md`, active `agents/`, `kb/`,
+  `pipelines/`, `templates/`, and `/about` returned no occurrence.
+- `cmp -s ai-editorial-office/pipelines/review_pipeline.md
+  about/review_pipeline.md` passed.
+- `tests/test_outcome_first_deliverable_selection.sh:28-32` now fails if the
+  forbidden standalone label appears in the canonical Review Pipeline.
+- No changed repair file invalidated the requested/recommended/selected,
+  explicit-intent, sufficiency, mismatch/preflight, or pipeline-order checks
+  approved in Round 1.
+
+## Editorial Challenge Lens
+
+- Decision under challenge: extend Task Need Recognition, Chief Editor
+  orchestration, existing roles, pipelines, templates, and Review rather than
+  creating a new architecture branch.
+- Assumption: all new behavior can remain a conditional capability and review
+  lens inside existing owners.
+- Challenge condition: if the patch creates a separately named approval-blocking
+  gate, the bounded architecture assumption no longer fully holds.
+- Round 1 assumption check: `partially_changed` because of OFD-001.
+- Bounded re-review assumption check: `holds`.
+- Evidence: the repaired Review Pipeline keeps all outcome-first checks under
+  the existing Task Need Recognition gate; no separate role, pipeline, stage,
+  gate, score, or mandatory artifact remains.
+- Consequence: the bounded repair is sufficient; no reroute, redesign, or
+  broader rewrite is justified.
+
+## Validation evidence
+
+Re-executed from `/Users/sa/Projects/ai-editorial-office-github` on the repaired
+current snapshot:
+
+- Exact forbidden-label search over active canon and `/about` — pass, no
+  occurrence.
+- Canonical-to-`/about` `cmp` for Review Pipeline — pass.
+- `git diff --check` — pass.
+- `sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh` —
+  pass; negative gate assertion, canonical contract, and ten cases present.
+- `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` — pass,
+  14/14 cases.
+- `sh ai-editorial-office/tests/test_task_pack_generator.sh` — pass, 13/13
+  cases.
+- `sh ai-editorial-office/scripts/check_about_memory_package.sh` — pass, 20
+  exact-copy files.
+- `python3 ai-editorial-office/scripts/validate_task_lifecycle.py
+  ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION` — pass,
+  0 blockers and 0 warnings.
+
+The exact canonical inspection, mirror comparison, negative regression, and
+full validator rerun resolve OFD-001 without relying on a passing test alone.
+
+## Non-critical observations
+
+- Manual synthetic cases and the executable static regression demonstrate
+  contract coverage, not real-world outcome improvement. The implementation
+  report states this limitation accurately.
+- Deferring `complete-diff.md` until repairs are complete is appropriate; it
+  must be generated from the final reviewed snapshot before delivery.
+
+## Blockers and next action
+
+- Blocking findings: none. OFD-001 is resolved.
+- Open evidence questions: none.
+- Next action: hand the approved reviewed snapshot to Chief Editor for compact
+  finalization, final diff generation, and governance closure.
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/status.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/status.md
new file mode 100644
index 0000000..c8a4dd1
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/status.md
@@ -0,0 +1,23 @@
+# Status
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- Current status: finalized
+- Previous status: approved
+- Current owner: chief_editor
+- Review required: yes
+- Human approval required: no for local implementation; publication was not
+  requested
+- Open blockers: none
+- Next action: deliver implementation report and complete diff to user
+
+## history
+
+| Date | From | To | Owner | Reason |
+| --- | --- | --- | --- | --- |
+| 2026-07-13 | intake | planning | chief_editor | Request and architectural constraints normalized |
+| 2026-07-13 | planning | writing | writer_agent | Outcome-first deliverable and task-local system-update route selected |
+| 2026-07-13 | writing | review | writer_agent | Canonical patch, synthetic tests, report draft, and review handoff completed |
+| 2026-07-13 | review | changes_requested | review_agent | OFD-001: standalone named gate must be folded into existing Task Need Recognition gate |
+| 2026-07-13 | changes_requested | review | writer_agent | OFD-001 repaired, exact mirror synchronized, negative regression added, validations passed |
+| 2026-07-13 | review | approved | review_agent | Bounded re-review approved; OFD-001 resolved; no blockers remain |
+| 2026-07-13 | approved | finalized | chief_editor | Compact finalization accepted; final governance decision recorded; complete diff is the last mechanical snapshot |
diff --git a/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/task-manifest.md b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/task-manifest.md
new file mode 100644
index 0000000..bd8108e
--- /dev/null
+++ b/ai-editorial-office/tasks/TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION/task-manifest.md
@@ -0,0 +1,53 @@
+# Task Manifest
+
+## task identity
+
+- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
+- Task title: Add Outcome-First Deliverable Selection
+- Task type: canonical system capability update
+- Owner/current role: `chief_editor`
+- Created: 2026-07-13
+- Last updated: 2026-07-13
+
+## current state
+
+- Current status: `finalized`
+- Selected deliverable: bounded canonical patch, synthetic test, implementation
+  report, and complete diff
+- Selected pipeline: `review_pipeline`
+- Risk mode: `standard`
+- Process depth: `normal`
+- Execution profile: `compact`
+- Client profile: `none`
+- Client profile status: `not_applicable`
+- Current working artifact: `final.md`
+- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
+- Next required action: deliver package to user
+
+## artifact inventory
+
+| Artifact | Required | State | Purpose |
+| --- | --- | --- | --- |
+| `brief.md` | yes | current | Scope and acceptance contract |
+| `orchestration_plan.md` | yes | current | Deliverable-first route and execution contract |
+| `status.md` | yes | current | Lifecycle and blocker state |
+| `implementation-report.md` | yes | current | User-requested implementation report |
+| `complete-diff.md` | yes | current after final mechanical generation | User-requested complete patch record |
+| `review.md` | yes | current: approved | Independent review verdict |
+| `handoff-implementation-writer-agent-to-review-agent.md` | yes | current | Review scope and independence boundary |
+| `handoff-review-review-agent-to-writer-agent.md` | yes | current | Bounded OFD-001 repair contract |
+| `handoff-repair-writer-agent-to-review-agent.md` | yes | current | Repair evidence and bounded re-review scope |
+| `handoff-review-approval-review-agent-to-final-editor.md` | yes | current | Approved-scope finalization contract |
+| `handoff-finalization-final-editor-to-chief-editor.md` | yes | current | Finalization delta and closeout action |
+| `final.md` | yes | current | Final delivery pointer |
+| `final_decision.md` | yes | current | Chief Editor governance decision |
+
+## runtime execution
+
+| Stream ID | Canonical function | Scope | Artifacts/packages | Boundary |
+| --- | --- | --- | --- | --- |
+| `implementation-main` | Writer / implementation function | Canonical owner edits, templates, tests, report, diff | repository patch and task-local package | Does not independently review or approve |
+| `review-independent` | Review Agent | Patch, tests, architecture constraints, scope | `review.md` and bounded findings | Must be a separate role instance |
+
+Model/mode metadata: not recorded; no runtime nickname is used as process
+identity.
diff --git a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
index 0763af1..c7fb0df 100644
--- a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
+++ b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
@@ -12,7 +12,9 @@ the fields needed to make routing and review safe.

 - Task ID:
 - User goal:
-- Deliverable:
+- Requested deliverable:
+- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
+- Selected deliverable: pending / value
 - Audience/channel:
 - Current active version:

@@ -32,12 +34,6 @@ the fields needed to make routing and review safe.
 - Forbidden depth shortcuts:
 - Expanded profile trigger, if any:

-## selected pipeline
-
-- Pipeline:
-- Why this pipeline:
-- Pipeline exceptions or local constraints:
-
 ## client profile

 - Client profile: `none` / `sber` / `unknown`
@@ -63,6 +59,9 @@ material. Omit it for trivial, obvious work. It is advisory evidence, not a
 route, activation, depth choice, gate, or standalone artifact.

 - Observed request signals:
+- Requested deliverable:
+- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
+- Recommended deliverable and outcome-fit reason:
 - Likely primary task type:
 - Material secondary aspects:
 - Likely capabilities and why:
@@ -77,6 +76,36 @@ route, activation, depth choice, gate, or standalone artifact.
 - Explicit non-decision:
 - Chief Editor decision or next question:

+## outcome-first deliverable decision
+
+Complete before pipeline selection when deliverable choice is material. For an
+obvious compact task, one line may record that requested, recommended, and
+selected deliverables are the same. Do not create a separate artifact.
+
+- User problem to solve:
+- Requested deliverable: value / `not specified`
+- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
+- Recommended deliverable:
+- Why this is the smallest sufficient outcome-fit artifact:
+- Alternative value or mismatch, if any:
+- Decision: `respect_requested` / `select_recommended` /
+  `ask_before_change` / `constrain_with_explanation`
+- Selected deliverable:
+- Explicit-intent preservation note:
+
+An explicit requested deliverable remains selected by default. Recommend an
+alternative when useful, but do not substitute it without user agreement. If
+the mismatch makes the request unsafe or unable to achieve its stated outcome,
+route it through preflight rather than silently overriding it.
+
+## selected pipeline
+
+Select only after the selected deliverable above is known.
+
+- Pipeline:
+- Why this pipeline fits the selected deliverable:
+- Pipeline exceptions or local constraints:
+
 ## preflight gate

 Use before production starts. Keep compact; do not create a separate artifact
@@ -86,7 +115,7 @@ unless a task-specific governance or restartability need justifies it.
 | --- | --- |
 | Audience | `confirmed` / `inferred` / `unknown` |
 | Channel or context | `confirmed` / `inferred` / `unknown` |
-| Deliverable | `defined` / `unclear` |
+| Selected deliverable | `defined` / `unclear` |
 | Source boundary | `defined` / `unclear` |
 | Success criterion | `defined` / `unclear` |
 | Approval boundary | `defined` / `unclear` |
@@ -109,7 +138,7 @@ if the decision needs extended justification, use a task-local analytical
 artifact and keep this frame compact.

 - Chosen editorial route:
-- Why this route serves the task:
+- Why this route serves the selected deliverable and task outcome:
 - Reader journey rationale, when material: starting state -> required change ->
   explanation sequence -> practical result
 - Cognitive Bridge, required for teaching/understanding work or `not applicable`
diff --git a/ai-editorial-office/templates/artifacts/task_manifest_template.md b/ai-editorial-office/templates/artifacts/task_manifest_template.md
index f4dea8c..793c4fc 100644
--- a/ai-editorial-office/templates/artifacts/task_manifest_template.md
+++ b/ai-editorial-office/templates/artifacts/task_manifest_template.md
@@ -15,6 +15,7 @@ artifact. Keep it short, current, and explicit about versions.
 ## current state

 - Current status:
+- Selected deliverable:
 - Selected pipeline:
 - Risk mode:
 - Process depth:
diff --git a/ai-editorial-office/templates/tasks/article_task_template.md b/ai-editorial-office/templates/tasks/article_task_template.md
index 2356502..d8584ce 100644
--- a/ai-editorial-office/templates/tasks/article_task_template.md
+++ b/ai-editorial-office/templates/tasks/article_task_template.md
@@ -102,6 +102,11 @@ governance, or non-trivial coordination must be recorded.

 ## deliverable

+- requested deliverable:
+- format authority: explicit/delegated/inferred/unknown
+- advisory recommended deliverable, when material:
+- selected deliverable: Chief Editor records in `orchestration_plan.md`
+
 ## channel or publication context

 ## scope
diff --git a/ai-editorial-office/templates/tasks/review_task_template.md b/ai-editorial-office/templates/tasks/review_task_template.md
index 7b631be..1ebfc4f 100644
--- a/ai-editorial-office/templates/tasks/review_task_template.md
+++ b/ai-editorial-office/templates/tasks/review_task_template.md
@@ -114,6 +114,17 @@ Conditional files:
 - Structure/usefulness validation:
 - Governance validation:

+## outcome-first deliverable review, when material
+
+- Requested deliverable:
+- Format authority: explicit/delegated/inferred/unknown
+- Recommended deliverable:
+- Selected deliverable:
+- Explicit intent respected: pass/fail/needs clarification
+- Selected artifact sufficient for actual outcome: pass/fail/needs clarification
+- Alternative or override justified: pass/fail/not applicable/needs clarification
+- Pipeline selected after and for the selected deliverable: pass/fail/needs clarification
+
 ## compact reader review, when selected

 | Question | Status | Evidence | Required action |
diff --git a/ai-editorial-office/templates/tasks/social_task_template.md b/ai-editorial-office/templates/tasks/social_task_template.md
index a44b469..bb08e82 100644
--- a/ai-editorial-office/templates/tasks/social_task_template.md
+++ b/ai-editorial-office/templates/tasks/social_task_template.md
@@ -86,6 +86,11 @@ Conditional files:

 ## deliverable

+- requested deliverable:
+- format authority: explicit/delegated/inferred/unknown
+- advisory recommended deliverable, when material:
+- selected deliverable: Chief Editor records in `orchestration_plan.md`
+
 ## message priority

 ## CTA
diff --git a/ai-editorial-office/templates/tasks/ux_writing_task_template.md b/ai-editorial-office/templates/tasks/ux_writing_task_template.md
index d15b64d..dedbae6 100644
--- a/ai-editorial-office/templates/tasks/ux_writing_task_template.md
+++ b/ai-editorial-office/templates/tasks/ux_writing_task_template.md
@@ -93,6 +93,11 @@ Conditional files:

 ## deliverable

+- requested deliverable:
+- format authority: explicit/delegated/inferred/unknown
+- advisory recommended deliverable, when material:
+- selected deliverable: Chief Editor records in `orchestration_plan.md`
+
 ## constraints

 ## client profile
diff --git a/ai-editorial-office/tests/README.md b/ai-editorial-office/tests/README.md
index 8f7f7ac..7392530 100644
--- a/ai-editorial-office/tests/README.md
+++ b/ai-editorial-office/tests/README.md
@@ -57,6 +57,14 @@ markdown smoke-tests и synthetic examples:
 - `reader-centered-quality-smoke-test.md` - manual synthetic regression cases
   for Reader Outcome Contract, Learning Design, Reader Review, Companion Pass,
   bounded utility tradeoffs, and compact non-activation.
+- `outcome_first_deliverable_selection_smoke_test.md` - manual synthetic
+  regression cases for requested/recommended/selected deliverable separation,
+  explicit-intent preservation, delegated format choice, outcome-fit
+  sufficiency, pipeline-after-deliverable ordering, mismatch escalation, and
+  compact non-activation.
+- `test_outcome_first_deliverable_selection.sh` - executable static regression
+  check for the canonical owner text, orchestration ordering, ten-case synthetic
+  suite, and absence of forbidden Deliverable/Format Agent or pipeline files.
 - `knowledge_evolution_smoke_test.md` - manual synthetic cases for Knowledge
   Evolution disposition, stale-knowledge challenge, canon-update candidates,
   and `/about` memory sync; it is not production governance.
@@ -219,6 +227,24 @@ good and bad cognitive bridges and bounded tradeoffs, reject taste-only review,
 and keep short low-risk text compact. It does not define active rules or replace
 the canonical owners listed in the file.

+`outcome_first_deliverable_selection_smoke_test.md` records ten synthetic cases
+for explicit article and presentation requests, delegated learning format,
+invalid checklist substitution for an explanation, presentation use context,
+comparison matrix, decision memo, BRD/specification ambiguity, material format
+mismatch, and trivial copy repair. It checks that the selected deliverable is
+outcome-fit and recorded before pipeline selection without creating a role,
+pipeline, lifecycle stage, gate, score, or mandatory standalone artifact. It
+does not define active rules or prove real-world improvement.
+
+Run the bounded static contract check with:
+
+```bash
+sh ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh
+```
+
+The script verifies canonical integration and test coverage only. It does not
+classify requests, select deliverables, route tasks, or replace Review Agent.
+
 `knowledge_evolution_smoke_test.md` records synthetic disposition cases for
 `/kb/editorial_learning_framework.md`. It checks that reusable learning,
 pattern candidates, canon-update candidates, stale/conflicting knowledge,
diff --git a/ai-editorial-office/tests/outcome_first_deliverable_selection_smoke_test.md b/ai-editorial-office/tests/outcome_first_deliverable_selection_smoke_test.md
new file mode 100644
index 0000000..e8ab74f
--- /dev/null
+++ b/ai-editorial-office/tests/outcome_first_deliverable_selection_smoke_test.md
@@ -0,0 +1,241 @@
+# Outcome-First Deliverable Selection Smoke Test
+
+Status: manual synthetic regression test. These cases are not task materials,
+real user evidence, an automatic classifier, or a new review gate.
+
+## Contract Under Test
+
+The test passes only when the record:
+
+1. separates requested, recommended, and selected deliverables;
+2. labels format authority as `explicit`, `delegated`, `inferred`, or `unknown`;
+3. recommends the smallest artifact that is still sufficient for the actual
+   outcome and use context;
+4. preserves explicit user format intent unless the user agrees to change it;
+5. explains alternatives or unresolved mismatches rather than silently
+   overriding the request;
+6. selects the pipeline, mode, or task-local mini-contract after and for the
+   selected deliverable;
+7. creates no Deliverable Agent, Format Agent, pipeline, lifecycle stage, gate,
+   score, or mandatory standalone artifact.
+
+## Case 1: Explicit Article Stays Article
+
+### Synthetic request
+
+> Write an article that helps experienced managers understand our new incident
+> response policy.
+
+### Expected decision
+
+- Requested deliverable: article.
+- Format authority: `explicit`.
+- Recommended deliverable: article; an executive checklist may be suggested as
+  an optional appendix, not a replacement.
+- Decision: `respect_requested`.
+- Selected deliverable: article.
+- Pipeline consequence: Article Pipeline is selected after the deliverable.
+
+### Expected result
+
+Pass. The office may improve the article shape but may not silently turn it into
+a checklist, memo, or slide deck.
+
+## Case 2: Delegated Format Produces A Learning Roadmap
+
+### Synthetic request
+
+> I need to catch up on modern AI practice. Format and structure are up to you.
+
+### Expected decision
+
+- Requested deliverable: `not specified`.
+- Format authority: `delegated`.
+- Recommended deliverable: learning roadmap with reading order and practical
+  checkpoints.
+- Decision: `select_recommended`.
+- Selected deliverable: learning roadmap.
+- Pipeline consequence: use the existing Article Pipeline only if its
+  knowledge-content contract fits; otherwise use a bounded task-local
+  mini-contract with current Writer, Review, and governance owners. Do not add a
+  roadmap pipeline.
+
+### Expected result
+
+Pass. Delegation authorizes format choice, and the recommendation is tied to
+the learning outcome rather than to the first familiar document type.
+
+## Case 3: Bare Explain Request Cannot Become A Checklist
+
+### Synthetic request
+
+> Explain how the new access model works.
+
+### Invalid decision
+
+- Recommended deliverable: checklist.
+- Reason: shorter and easier to scan.
+
+### Expected result
+
+Fail. `Explain` requires a communication artifact capable of building the
+model. A checklist may support later application, but brevity alone does not
+make it sufficient. Recommend an explainer/tutorial or ask about the use case if
+the required depth is materially ambiguous.
+
+## Case 4: Presentable Outcome Selects Presentation
+
+### Synthetic request
+
+> I need something I can present to the steering committee in fifteen minutes.
+
+### Expected decision
+
+- Requested deliverable: `not specified`.
+- Format authority: `inferred` from the explicit presentation use context.
+- Recommended deliverable: presentation with a concise decision summary.
+- Decision: `select_recommended` when no competing format changes the outcome;
+  otherwise ask one bounded question.
+- Selected deliverable: presentation.
+- Pipeline consequence: select an existing compatible mode or bounded
+  mini-contract after the presentation decision; do not create a presentation
+  pipeline merely for this case.
+
+### Expected result
+
+Pass. The use situation supports the artifact shape.
+
+## Case 5: Compare Outcome Selects Comparison Matrix
+
+### Synthetic request
+
+> Help me compare three onboarding platforms for a purchase decision.
+
+### Expected decision
+
+- Requested deliverable: `not specified`.
+- Format authority: `delegated` or safely `inferred`, depending on surrounding
+  context.
+- Recommended deliverable: comparison matrix with criteria, evidence notes,
+  tradeoffs, and a bounded recommendation if requested.
+- Decision: `select_recommended`.
+- Selected deliverable: comparison matrix.
+- Pipeline consequence: research depth follows claim/evidence need; the writing
+  or analytical mini-contract follows the selected matrix.
+
+### Expected result
+
+Pass. A matrix directly enables comparison and is more outcome-fit than an
+unstructured essay without weakening evidence.
+
+## Case 6: Management Persuasion Selects Decision Memo
+
+### Synthetic request
+
+> I need to convince management to fund the migration. Give me the strongest
+> format.
+
+### Expected decision
+
+- Requested deliverable: `not specified`.
+- Format authority: `delegated`.
+- Recommended deliverable: decision memo with recommendation, evidence,
+  alternatives, costs, risks, and explicit ask.
+- Decision: `select_recommended`.
+- Selected deliverable: decision memo.
+- Pipeline consequence: Professional Communication and Professional Analysis
+  may be activated; no new memo role or pipeline is created.
+
+### Expected result
+
+Pass. The deliverable supports a management decision rather than merely
+describing the technical topic.
+
+## Case 7: Requirements Need Selects BRD
+
+### Synthetic request
+
+> I need requirements that product, engineering, and procurement can approve.
+
+### Expected decision
+
+- Requested deliverable: requirements, format not fully specified.
+- Format authority: `inferred`.
+- Recommended deliverable: BRD or specification, with the choice tied to the
+  approval and downstream-use context.
+- Decision: `select_recommended` if the context clearly supports BRD;
+  `ask_before_change` if BRD versus technical specification changes ownership
+  or acceptance materially.
+- Selected deliverable: recorded before the pipeline or mini-contract.
+
+### Expected result
+
+Pass only when the recommendation basis and ambiguity handling are visible.
+
+## Case 8: Explicit Presentation Is Not Replaced By A Memo
+
+### Synthetic request
+
+> Create a presentation for the board. A memo might be easier for you, but I
+> need slides for the meeting.
+
+### Expected decision
+
+- Requested deliverable: presentation.
+- Format authority: `explicit`.
+- Recommended deliverable: presentation; an executive memo may be an optional
+  companion only if useful and in scope.
+- Decision: `respect_requested`.
+- Selected deliverable: presentation.
+
+### Expected result
+
+Pass. Production convenience cannot override explicit meeting needs.
+
+## Case 9: Material Format Mismatch Routes Through Preflight
+
+### Synthetic request
+
+> Write a one-page memo that fully trains new operators to perform a complex
+> recovery procedure without supervision.
+
+### Expected decision
+
+- Requested deliverable: one-page memo.
+- Format authority: `explicit`.
+- Recommended deliverable: tutorial/runbook or staged training package.
+- Decision: `ask_before_change` or `constrain_with_explanation`.
+- Selected deliverable: not changed silently; production does not start until
+  preflight resolves the mismatch or records a safe bounded scope.
+
+### Expected result
+
+Pass. Respect for intent does not require pretending the requested artifact can
+meet an impossible outcome.
+
+## Case 10: Trivial Obvious Work Stays Compact
+
+### Synthetic request
+
+> Fix the typo in this email and return the corrected email.
+
+### Expected decision
+
+- Requested deliverable: corrected email.
+- Format authority: `explicit`.
+- Recommended deliverable: corrected email.
+- Decision: `respect_requested`.
+- Selected deliverable: corrected email.
+- Pipeline consequence: compact existing route; no expanded recognition block
+  or new artifact is required.
+
+### Expected result
+
+Pass. Outcome-first selection does not make obvious work heavier.
+
+## Regression Verdict
+
+The capability passes this smoke test only if Cases 1, 2, 4, 5, 6, 8, 9, and
+10 produce the expected pass behavior, Case 3 is rejected, and Case 7 preserves
+the stated conditional ambiguity handling. Synthetic success does not prove
+real-world improvement; it demonstrates contract coverage and restraint.
diff --git a/ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh b/ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh
new file mode 100644
index 0000000..d9b92e2
--- /dev/null
+++ b/ai-editorial-office/tests/test_outcome_first_deliverable_selection.sh
@@ -0,0 +1,64 @@
+#!/usr/bin/env sh
+set -eu
+
+repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
+office="$repo_root/ai-editorial-office"
+
+require_text() {
+  file="$1"
+  text="$2"
+  if ! grep -Fq "$text" "$file"; then
+    echo "FAIL: $file is missing required contract text: $text"
+    exit 1
+  fi
+}
+
+require_text "$office/kb/task_need_recognition.md" "## Outcome-First Deliverable Recommendation"
+require_text "$office/kb/task_need_recognition.md" "Requested deliverable"
+require_text "$office/kb/task_need_recognition.md" "Recommended deliverable"
+require_text "$office/kb/task_need_recognition.md" "Selected deliverable"
+require_text "$office/kb/task_need_recognition.md" "silently override"
+require_text "$office/agents/chief_editor.md" "then select or confirm the appropriate pipeline"
+require_text "$office/agents/review_agent.md" "pipeline selection followed the selected deliverable"
+require_text "$office/templates/artifacts/orchestration_plan_template.md" "## outcome-first deliverable decision"
+require_text "$office/templates/artifacts/orchestration_plan_template.md" "## selected pipeline"
+require_text "$office/tests/outcome_first_deliverable_selection_smoke_test.md" "Bare Explain Request Cannot Become A Checklist"
+require_text "$office/tests/outcome_first_deliverable_selection_smoke_test.md" 'Fail. `Explain` requires'
+
+if grep -Fq "Outcome-first deliverable gate" \
+  "$office/pipelines/review_pipeline.md"; then
+  echo "FAIL: outcome-first checks must stay inside the existing Task Need Recognition gate."
+  exit 1
+fi
+
+decision_line=$(awk '/^## outcome-first deliverable decision$/ { print NR; exit }' \
+  "$office/templates/artifacts/orchestration_plan_template.md")
+pipeline_line=$(awk '/^## selected pipeline$/ { print NR; exit }' \
+  "$office/templates/artifacts/orchestration_plan_template.md")
+
+if [ -z "$decision_line" ] || [ -z "$pipeline_line" ] || \
+  [ "$decision_line" -ge "$pipeline_line" ]; then
+  echo "FAIL: deliverable decision must appear before selected pipeline in orchestration template."
+  exit 1
+fi
+
+case_count=$(grep -c '^## Case ' \
+  "$office/tests/outcome_first_deliverable_selection_smoke_test.md")
+if [ "$case_count" -ne 10 ]; then
+  echo "FAIL: expected 10 synthetic cases, found $case_count."
+  exit 1
+fi
+
+for forbidden in \
+  "$office/agents/deliverable_agent.md" \
+  "$office/agents/format_agent.md" \
+  "$office/pipelines/deliverable_pipeline.md" \
+  "$office/pipelines/format_pipeline.md"
+do
+  if [ -e "$forbidden" ]; then
+    echo "FAIL: forbidden architecture element exists: $forbidden"
+    exit 1
+  fi
+done
+
+echo "PASS: outcome-first deliverable selection contract and 10 synthetic cases are present."
~~~~
