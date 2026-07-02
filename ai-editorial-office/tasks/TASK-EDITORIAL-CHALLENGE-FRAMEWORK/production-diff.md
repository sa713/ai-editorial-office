diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
index fca68a4..9dbe681 100644
--- a/ai-editorial-office/AGENTS.md
+++ b/ai-editorial-office/AGENTS.md
@@ -94,6 +94,8 @@ Before production starts, Chief Editor must route the task editorially:
 - activate the visual branch when the selected task requires it;
 - determine the required roles and bounded extension roles;
 - make a compact preflight decision about input sufficiency before production;
+- record a compact Editorial Decision Frame in `orchestration_plan.md` before
+  handing work to Writer Agent or UX Writer;
 - record the routing decision in `orchestration_plan.md`, `task-manifest.md`,
   or `status.md`.
 
@@ -102,6 +104,20 @@ enough to start production, what is missing, and whether the next action is
 `ask`, `constrain`, `proceed`, or `block`. It is a decision gate, not a new
 pipeline, role, status, or mandatory standalone artifact.
 
+The Editorial Decision Frame records the chosen editorial route, considered
+alternatives, rejection reasons, Writer/UX Writer contract, review focus, and
+reroute triggers. It lives inside `orchestration_plan.md`; it is not a new
+pipeline, role, status, `final_decision.md`, or mandatory standalone
+`editorial_decision.md`.
+
+The frame must remain a short management block, not an analytical document.
+Alternatives exist to prove that the chosen route was deliberate: normally use
+2-3 alternatives, with one line for the alternative and one line for the
+rejection reason. Long rationale belongs in research, outline, review, or a
+task-local analytical addendum when one is truly needed; it must not expand the
+frame or create a standalone `editorial_decision.md` only because the reasoning
+is long.
+
 Technical actions are not substitutes for editorial routing. SVG, PNG, HTML,
 image generation, PDF extraction, OCR, parsing, conversion, scraping, rendering,
 or other tool work may support a task only after the editorial route is known.
@@ -660,6 +676,15 @@ final governance still happens and must be artifact-backed.
    is enough, `proceed` when the available input is sufficient, and `block` when
    the task cannot be performed safely.
 
+   Before handing work to Writer Agent or UX Writer, `chief_editor` records or
+   confirms the compact Editorial Decision Frame in `orchestration_plan.md`.
+   When research is required, this happens after research sufficiency is known.
+   The frame must stay short: chosen route, writing or UX writing contract,
+   review focus, reroute triggers, and usually 2-3 rejected alternatives. Each
+   alternative gets one line for the route and one line for the rejection
+   reason. Do not duplicate research, outline, review, or addendum content
+   inside the frame.
+
 3. Research if needed
 
    Если research требуется, `research_agent` собирает и структурирует информацию. Результаты сохраняются в `/tasks/TASK-ID/`.
@@ -670,7 +695,12 @@ final governance still happens and must be artifact-backed.
 
 5. Review
 
-   `review_agent` выполняет независимую проверку. Без положительного review материал не считается готовым.
+   `review_agent` выполняет независимую проверку. Для задач, где writing или
+   UX writing governed by Problem Hypothesis and/or Editorial Decision Frame,
+   review includes a compact Editorial Challenge Lens inside `review.md`:
+   Reviewer tests whether the assumptions that made the chosen route valid
+   still hold. This is evidence-backed review, not rewriting, rerouting, or a
+   new review gate. Без положительного review материал не считается готовым.
 
 6. Finalization
 
@@ -694,6 +724,9 @@ final governance still happens and must be artifact-backed.
 - что изменилось с предыдущего состояния;
 - какие артефакты созданы или обновлены;
 - какие constraints, blockers или open questions важны прямо сейчас;
+- for planning handoff to Writer Agent or UX Writer, the compact editorial
+  decision transfer: chosen route, rejected alternatives, writing contract, and
+  review focus;
 - что следующая роль должна сделать первым;
 - какие outputs ожидаются и какие запрещены;
 - когда нужно остановиться и эскалировать.
@@ -752,6 +785,11 @@ Artifact rules:
 - low-risk and simple standard tasks use `review.md` as the sole review artifact unless a separate support artifact is justified;
 - Preflight Gate is a compact decision in an existing task artifact, not a new
   mandatory file;
+- Editorial Decision Frame is a compact section in `orchestration_plan.md`, not
+  a mandatory standalone artifact, not a use of `final_decision.md`, and not a
+  place to duplicate research, outline, review, or analytical addenda;
+- Editorial Challenge Lens is a compact section inside `review.md`, not a
+  mandatory standalone artifact, new role, new review cycle, or new review gate;
 - `feedback.md` is optional and created only when post-delivery user reaction exists;
 - `review-summary.md`, `qa-checklist.md`, `finalization-checklist.md`, `open-questions.md`, and `finalization-notes.md` are conditional: create them only for an explicit downstream consumer, high-governance mode, a task-specific requirement, real open questions/blockers, or traceability need;
 - agents must not create speculative placeholder files for future use;
@@ -769,7 +807,7 @@ Primary responsibility boundaries:
 | --- | --- | --- |
 | `task-manifest.md` | compact current state, artifact inventory, next action packet | full status history, long rationale, full handoff |
 | `status.md` | detailed status/history, transitions, blockers, escalation notes | full manifest inventory or stage artifacts |
-| `orchestration_plan.md` | selected pipeline, roles, artifact scope, gates | narrative status log or handoff delta |
+| `orchestration_plan.md` | selected pipeline, roles, artifact scope, gates, Editorial Decision Frame | narrative status log or handoff delta |
 | handoff files | short delta-transfer between roles | manifest, status, orchestration plan, full artifact lists |
 | `compact-handoff.md` | final/user-facing transfer summary | role-to-role transfer, status history, full review |
 | `context-summary.md` | recovery after context fragmentation or long-running work | normal status update, final handoff, routine role transfer |
diff --git a/ai-editorial-office/agents/review_agent.md b/ai-editorial-office/agents/review_agent.md
index 7de80ff..b947749 100644
--- a/ai-editorial-office/agents/review_agent.md
+++ b/ai-editorial-office/agents/review_agent.md
@@ -18,6 +18,12 @@ explicit blockers, and a deterministic outcome.
 
 - validate compliance with `brief.md`, selected pipeline, active client profile,
   relevant KB, and task-specific constraints;
+- validate the quality of the Editorial Decision Frame when it governed writing
+  or UX writing, not only whether the block exists;
+- run a compact Editorial Challenge Lens when the task was governed by a
+  Problem Hypothesis and/or Editorial Decision Frame: identify the assumptions
+  that keep the chosen route valid, test whether challenge conditions occurred,
+  and record the result in `review.md`;
 - verify reviewer independence from the producer;
 - validate factual claims against available evidence and claim traceability;
 - detect unsupported claims, hallucination risk, contradictions, tone or glossary
@@ -43,8 +49,8 @@ Required:
 
 Conditional:
 
-- `orchestration_plan.md` when it defines scope, process depth, or acceptance
-  criteria;
+- `orchestration_plan.md` when it defines scope, process depth, acceptance
+  criteria, Problem Hypothesis, or the Editorial Decision Frame;
 - `status.md` when status consistency matters;
 - `research.md`, `sources.md`, `facts.md`, `claims_table.md`, or
   `claims-used.md` when factual claims are present;
@@ -56,8 +62,9 @@ Conditional:
 
 Required:
 
-- `review.md` with reviewed artifacts, independence basis, findings, outcome,
-  risks, required changes, blockers, and next action.
+- `review.md` with reviewed artifacts, independence basis, findings, Editorial
+  Challenge Lens when applicable, outcome, risks, required changes, blockers,
+  and next action.
 
 Conditional:
 
@@ -82,6 +89,10 @@ artifacts must never become silently mandatory.
   its source status is `pending_source`;
 - use plausibility as an evidence standard;
 - silently approve unsupported claims;
+- make preference-only challenges or turn a merely valid alternative into a
+  required change;
+- choose a new active editorial route, replace Chief Editor's route, or treat
+  the challenge lens as governance approval;
 - skip required validations because the task is low-risk;
 - make review optional;
 - create `final.md` or perform finalization;
@@ -93,6 +104,8 @@ artifacts must never become silently mandatory.
 The Review Agent may decide:
 
 - review outcome: `approved`, `changes_requested`, or `blocked`;
+- Editorial Challenge assumption check: `holds`, `partially_changed`, or
+  `changed`;
 - whether a finding is blocking, required, suggested, or informational;
 - repair owner and bounded re-review scope;
 - whether evidence is sufficient for approval.
@@ -102,13 +115,17 @@ The Review Agent must not decide:
 - final wording;
 - final governance readiness;
 - publication or human approval;
-- pipeline replacement or role reassignment beyond escalation recommendation.
+- pipeline replacement, active-route replacement, or role reassignment beyond
+  escalation recommendation.
 
 ## Stop Conditions
 
 Stop and mark blocked or escalate when:
 
 - reviewed artifact is missing, stale, or not the active version;
+- the Editorial Decision Frame is missing for post-planning writing, or is too
+  formal, bloated, or duplicative to validate the chosen route as a usable
+  production contract;
 - reviewer independence cannot be established;
 - required evidence, claim traceability, or source files are missing;
 - instructions conflict, client-profile source status is unresolved, or
@@ -127,6 +144,28 @@ short examples needed to clarify a finding.
 
 - review outcome is deterministic and grounded in saved artifacts;
 - independence is visible;
+- Editorial Decision Frame quality is checked when applicable: chosen route
+  fits the brief, evidence, risks, and source boundary; rejected alternatives
+  have real reasons; Writer Agent or UX Writer followed the route; rejected
+  paths did not return silently; and the route does not hide premature
+  consulting, overclaiming, or task substitution;
+- Editorial Decision Frame compactness is checked when applicable: the frame
+  should remain a short management block, use short route/reason pairs for
+  alternatives, and avoid duplicating research, outline, review, or analytical
+  addenda. If it stops functioning as a contract, record this as a non-critical
+  issue or blocker according to task impact;
+- Editorial Challenge Lens is completed when applicable: the decision under
+  challenge is named; route-validity assumptions are compact; challenge
+  conditions use evidence-backed `if... then...` logic; assumption check is
+  `holds`, `partially_changed`, or `changed`; evidence cites saved artifacts;
+  and required action maps to `approved`, `changes_requested`, `blocked`, or
+  valid escalation;
+- if route-validity assumptions still hold and the draft follows the contract,
+  Reviewer must not request changes merely because another route is also valid;
+- if an assumption partially changed, Reviewer records a bounded finding,
+  repair owner, repair scope, and re-review scope; if an assumption materially
+  changed and deterministic review is impossible, Reviewer records
+  `changes_requested`, `blocked`, or valid human/Chief Editor escalation;
 - `review.md` remains mandatory and sufficient for compact or simple standard
   review unless optional artifacts are justified;
 - findings distinguish blockers from improvements;
diff --git a/ai-editorial-office/pipelines/review_pipeline.md b/ai-editorial-office/pipelines/review_pipeline.md
index 64ae99f..ec5032e 100644
--- a/ai-editorial-office/pipelines/review_pipeline.md
+++ b/ai-editorial-office/pipelines/review_pipeline.md
@@ -17,6 +17,12 @@ For instructional and operational materials, the pipeline also protects informat
 
 Review is a gate, not a writing, editing, finalization, or governance role. It produces evidence-backed findings and one of three allowed outcomes: `approved`, `changes_requested`, or `blocked`.
 
+When a task was governed by a Problem Hypothesis and/or Editorial Decision
+Frame, review also includes an assumptions-based Editorial Challenge Lens inside
+`review.md`. This lens tests whether the assumptions that made the chosen route
+valid still hold. It is part of review, not a new pipeline, role, review gate,
+artifact, or mandatory extra review cycle.
+
 ## when to use
 
 Use this pipeline when a draft, UX copy, edited material, finalization candidate, or task package needs independent validation before moving forward.
@@ -81,6 +87,9 @@ Review execution follows `AGENTS.md` short context loading policy. Use these inp
   `orchestration_plan.md`, only when `client_profile` is set;
 - research and claim artifacts, if applicable.
 
+When present, Problem Hypothesis and Editorial Decision Frame in
+`orchestration_plan.md` are required inputs for the Editorial Challenge Lens.
+
 For article-style review, the material under review is usually:
 
 - `/tasks/TASK-ID/draft.md`;
@@ -155,7 +164,7 @@ compact evidence. Missing evidence for material claims should produce
 | `brief.md` | Review scope and acceptance criteria | review_agent, chief_editor | never for review |
 | `orchestration_plan.md` | Selected production pipeline and review gates | review_agent, chief_editor | never after orchestration starts |
 | reviewed material | The artifact being independently reviewed | review_agent, final_editor | never for review |
-| `review.md` | Deterministic verdict, findings, required changes | final_editor, chief_editor | never before finalization |
+| `review.md` | Deterministic verdict, findings, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
 | review handoff | Delta-transfer to next valid role | receiving role | only when no role transition occurs |
 
 ### conditional artifacts
@@ -209,7 +218,7 @@ Operational sequence:
 | --- | --- | --- | --- | --- | --- |
 | 1 | `writing`, `editing`, or `changes_requested` | `writer_agent` or `ux_writer` | Hand off material ready for independent review | writing or UX artifacts, handoff | `review` |
 | 2 | `review` | `review_agent` | Load required artifacts, verify independence, validate scope | review notes or blocker evidence | `review` or `blocked` |
-| 3 | `review` | `review_agent` | Validate factual traceability, KB compliance, artifact completeness, and governance compliance | `review.md`, `qa-checklist.md` when separate checklist is required, `review-summary.md` when concise transfer is needed, `reviewer-notes.md` when extra notes are needed | `approved`, `changes_requested`, or `blocked` |
+| 3 | `review` | `review_agent` | Validate factual traceability, KB compliance, artifact completeness, governance compliance, and Editorial Challenge Lens when applicable | `review.md`, `qa-checklist.md` when separate checklist is required, `review-summary.md` when concise transfer is needed, `reviewer-notes.md` when extra notes are needed | `approved`, `changes_requested`, or `blocked` |
 | 4 | `changes_requested` | `writer_agent`, `ux_writer`, or `research_agent` | Resolve required changes or evidence gaps | updated artifacts, handoff | `review`, `writing`, `research`, or `blocked` |
 | 5 | `review` | `review_agent` | Re-review changed artifacts | updated review artifacts and handoff | `approved`, `changes_requested`, or `blocked` |
 | 6 | `approved` | `final_editor` | Finalize only after approved review | `final.md`, conditional finalization notes/checklist, finalization handoff unless compact finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md` | `approved` |
@@ -263,6 +272,8 @@ Compact review minimum:
 - verdict;
 - reviewed artifact or artifact set;
 - lightweight independence check;
+- compact Editorial Challenge Lens when the task was governed by Problem
+  Hypothesis and/or Editorial Decision Frame;
 - usefulness/pass rationale or blocking issues;
 - governance note when relevant;
 - one next action.
@@ -280,6 +291,7 @@ It does not restate detailed review logic. Review Agent owns:
 - reviewer independence checks;
 - factual, source, and claim validation;
 - editorial relevance and replaceability pressure;
+- assumptions-based Editorial Challenge Lens;
 - instructional architecture pressure;
 - allowed review outcomes and approval blockers;
 - escalation content;
@@ -314,6 +326,9 @@ Review Pipeline is complete only when:
 - required review inputs were checked or missing inputs were documented;
 - reviewer independence was checked;
 - `review.md` exists and includes reviewed artifacts, findings, blockers, required changes, and outcome;
+- when the reviewed work was governed by Problem Hypothesis and/or Editorial
+  Decision Frame, `review.md` includes Editorial Challenge Lens or a compact
+  statement that route-validity assumptions still hold;
 - `qa-checklist.md` exists with pass, fail, or not_applicable statuses when separate checklist depth is required;
 - `review-summary.md` exists with operational outcome and next action when concise transfer is not already covered by `review.md` and handoff;
 - `reviewer-notes.md` exists when extra caveats or borderline reasoning do not fit in `review.md`;
diff --git a/ai-editorial-office/templates/tasks/review_task_template.md b/ai-editorial-office/templates/tasks/review_task_template.md
index a352151..165e7fa 100644
--- a/ai-editorial-office/templates/tasks/review_task_template.md
+++ b/ai-editorial-office/templates/tasks/review_task_template.md
@@ -107,6 +107,20 @@ Conditional files:
 - Structure/usefulness validation:
 - Governance validation:
 
+## editorial challenge
+
+- Decision under challenge:
+- Chosen route remains valid while:
+  - Assumption:
+  - Assumption:
+  - Assumption:
+- Challenge conditions:
+  - If ..., then ... route would become stronger.
+  - If ..., then ... route would become stronger.
+- Assumption check: `holds` / `partially_changed` / `changed`
+- Evidence:
+- Required action:
+
 ## findings
 
 | Severity | Finding | Evidence | Required action | Owner |
