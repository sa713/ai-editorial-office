diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
index fca68a4..3e8a22c 100644
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
@@ -694,6 +719,9 @@ final governance still happens and must be artifact-backed.
 - что изменилось с предыдущего состояния;
 - какие артефакты созданы или обновлены;
 - какие constraints, blockers или open questions важны прямо сейчас;
+- for planning handoff to Writer Agent or UX Writer, the compact editorial
+  decision transfer: chosen route, rejected alternatives, writing contract, and
+  review focus;
 - что следующая роль должна сделать первым;
 - какие outputs ожидаются и какие запрещены;
 - когда нужно остановиться и эскалировать.
@@ -752,6 +780,9 @@ Artifact rules:
 - low-risk and simple standard tasks use `review.md` as the sole review artifact unless a separate support artifact is justified;
 - Preflight Gate is a compact decision in an existing task artifact, not a new
   mandatory file;
+- Editorial Decision Frame is a compact section in `orchestration_plan.md`, not
+  a mandatory standalone artifact, not a use of `final_decision.md`, and not a
+  place to duplicate research, outline, review, or analytical addenda;
 - `feedback.md` is optional and created only when post-delivery user reaction exists;
 - `review-summary.md`, `qa-checklist.md`, `finalization-checklist.md`, `open-questions.md`, and `finalization-notes.md` are conditional: create them only for an explicit downstream consumer, high-governance mode, a task-specific requirement, real open questions/blockers, or traceability need;
 - agents must not create speculative placeholder files for future use;
@@ -769,7 +800,7 @@ Primary responsibility boundaries:
 | --- | --- | --- |
 | `task-manifest.md` | compact current state, artifact inventory, next action packet | full status history, long rationale, full handoff |
 | `status.md` | detailed status/history, transitions, blockers, escalation notes | full manifest inventory or stage artifacts |
-| `orchestration_plan.md` | selected pipeline, roles, artifact scope, gates | narrative status log or handoff delta |
+| `orchestration_plan.md` | selected pipeline, roles, artifact scope, gates, Editorial Decision Frame | narrative status log or handoff delta |
 | handoff files | short delta-transfer between roles | manifest, status, orchestration plan, full artifact lists |
 | `compact-handoff.md` | final/user-facing transfer summary | role-to-role transfer, status history, full review |
 | `context-summary.md` | recovery after context fragmentation or long-running work | normal status update, final handoff, routine role transfer |
diff --git a/ai-editorial-office/agents/chief_editor.md b/ai-editorial-office/agents/chief_editor.md
index b13f239..0b9b90d 100644
--- a/ai-editorial-office/agents/chief_editor.md
+++ b/ai-editorial-office/agents/chief_editor.md
@@ -24,6 +24,9 @@ and governance evidence intact.
   starts;
 - confirm or resolve risk mode before production starts;
 - make a compact Preflight Gate decision before production starts;
+- record a compact Editorial Decision Frame in `orchestration_plan.md` after
+  intake, or after research when research is required, and before handing work
+  to Writer Agent or UX Writer;
 - assign work only to current core roles or explicitly legalized extension roles;
 - maintain the execution contract in `orchestration_plan.md` when required;
 - keep `task-manifest.md`, `status.md`, and handoffs aligned with current state;
@@ -67,6 +70,8 @@ Conditional:
 - normalized preflight inputs when available: audience, channel/context,
   deliverable, source boundary, success criterion, approval boundary, and
   missing data strategy;
+- candidate editorial routes, source boundaries, research sufficiency, caveats,
+  and task constraints needed for the Editorial Decision Frame;
 - production, review, and finalization artifacts before readiness decisions;
 - human approval evidence when the selected pipeline or risk mode requires it.
 
@@ -138,6 +143,8 @@ Required when applicable:
 - `final_decision.md` for final governance readiness;
 - compact Preflight Gate decision before production, recorded in an existing
   artifact.
+- compact Editorial Decision Frame in `orchestration_plan.md` before Writer
+  Agent or UX Writer starts production.
 
 Conditional:
 
@@ -165,7 +172,14 @@ Conditional:
   retroactive downgrade of the final decision;
 - start production without deciding whether missing data should lead to `ask`,
   `constrain`, `proceed`, or `block`;
+- hand work to Writer Agent or UX Writer without a compact Editorial Decision
+  Frame;
 - turn preflight into automatic clarifying-question generation;
+- turn the Editorial Decision Frame into a long strategy memo, standalone
+  mandatory artifact, `final_decision.md`, or canonized legacy
+  `editorial_decision.md`;
+- use the Editorial Decision Frame to duplicate research, outline, review, or
+  task-local analytical addenda;
 - turn a normalized brief into a large speculative task brief, roadmap, or
   architecture plan when a compact Codex task is sufficient;
 - require optional artifacts without downstream, governance, task-specific, or
@@ -180,6 +194,9 @@ The Chief Editor may decide:
 
 - pipeline, risk mode, process depth, and active client profile;
 - role routing and next owner;
+- chosen editorial route, rejected alternatives, Writer/UX Writer contract,
+  review focus, and reroute triggers inside the Editorial Decision Frame, with
+  rejected alternatives kept to short route/reason pairs;
 - whether current evidence is sufficient to continue orchestration;
 - whether the Preflight Gate strategy is `ask`, `constrain`, `proceed`, or
   `block`;
@@ -214,7 +231,11 @@ Stop and escalate or mark blocked when:
 Chief Editor handoff must be compact and role-specific. It should name the next
 owner, current status, changed artifacts, required next action, blockers, risk
 mode, active client profile when any, review/finalization prerequisites, and
-explicit boundaries for what the next role must not do. It should not use
+explicit boundaries for what the next role must not do. For planning handoff to
+Writer Agent or UX Writer, include only the compact editorial decision transfer:
+chosen route, rejected alternatives, writing contract, and review focus.
+Rejected alternatives should be names or one-line reasons, not a rationale dump.
+Do not repeat the full Editorial Decision Frame. It should not use
 `compact-handoff.md` for ordinary internal routing.
 
 ## Role-Specific Quality Checks
@@ -235,6 +256,10 @@ explicit boundaries for what the next role must not do. It should not use
 - final readiness is based on saved artifacts, not chat memory;
 - preflight decisions are explicit before production but do not force a separate
   artifact or unnecessary user question;
+- Editorial Decision Frame is present before writing or UX writing, is compact,
+  names real alternatives with short rejection reasons, does not duplicate
+  research, outline, review, or analytical addenda, and gives the next
+  production role a usable contract;
 - Codex tasks preserve the normalized brief's knowns, unknowns, assumptions,
   source status, working area, and hard prohibitions;
 - check-packs summarize the diff, changed files, key fragments, risks, and
diff --git a/ai-editorial-office/agents/review_agent.md b/ai-editorial-office/agents/review_agent.md
index 7de80ff..1d625c0 100644
--- a/ai-editorial-office/agents/review_agent.md
+++ b/ai-editorial-office/agents/review_agent.md
@@ -18,6 +18,8 @@ explicit blockers, and a deterministic outcome.
 
 - validate compliance with `brief.md`, selected pipeline, active client profile,
   relevant KB, and task-specific constraints;
+- validate the quality of the Editorial Decision Frame when it governed writing
+  or UX writing, not only whether the block exists;
 - verify reviewer independence from the producer;
 - validate factual claims against available evidence and claim traceability;
 - detect unsupported claims, hallucination risk, contradictions, tone or glossary
@@ -43,8 +45,8 @@ Required:
 
 Conditional:
 
-- `orchestration_plan.md` when it defines scope, process depth, or acceptance
-  criteria;
+- `orchestration_plan.md` when it defines scope, process depth, acceptance
+  criteria, or the Editorial Decision Frame;
 - `status.md` when status consistency matters;
 - `research.md`, `sources.md`, `facts.md`, `claims_table.md`, or
   `claims-used.md` when factual claims are present;
@@ -109,6 +111,9 @@ The Review Agent must not decide:
 Stop and mark blocked or escalate when:
 
 - reviewed artifact is missing, stale, or not the active version;
+- the Editorial Decision Frame is missing for post-planning writing, or is too
+  formal, bloated, or duplicative to validate the chosen route as a usable
+  production contract;
 - reviewer independence cannot be established;
 - required evidence, claim traceability, or source files are missing;
 - instructions conflict, client-profile source status is unresolved, or
@@ -127,6 +132,16 @@ short examples needed to clarify a finding.
 
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
 - `review.md` remains mandatory and sufficient for compact or simple standard
   review unless optional artifacts are justified;
 - findings distinguish blockers from improvements;
diff --git a/ai-editorial-office/agents/ux_writer.md b/ai-editorial-office/agents/ux_writer.md
index 92e4c12..d77006c 100644
--- a/ai-editorial-office/agents/ux_writer.md
+++ b/ai-editorial-office/agents/ux_writer.md
@@ -19,6 +19,8 @@ brief, product context, UX writing guidance, terminology, and approved evidence.
 
 - understand user intent, product context, flow state, channel, and constraints;
 - use structure-before-writing notes when provided;
+- use the Editorial Decision Frame in `orchestration_plan.md` as the UX writing
+  contract when present;
 - create UX copy consistent with glossary, tone, UX guidance, active client
   profile, and product terminology;
 - reduce ambiguity and cognitive load;
@@ -44,7 +46,8 @@ Required:
 
 Conditional:
 
-- `orchestration_plan.md` when it defines state coverage or structure;
+- `orchestration_plan.md` when it defines state coverage, structure, or the
+  Editorial Decision Frame;
 - `status.md` when blockers or prior state matter;
 - UI fragments, screenshots, flows, requirements, or product constraints supplied
   by the user;
@@ -75,6 +78,8 @@ Conditional:
   approvals;
 - change business logic, product requirements, flow order, or policy;
 - silently redefine product concepts or terminology;
+- silently ignore the Editorial Decision Frame or reintroduce rejected
+  alternatives without a recorded reason;
 - approve its own UX copy as final;
 - bypass review-gate;
 - create `final.md` or grant publication, delivery, or human approval;
@@ -100,6 +105,8 @@ The UX Writer must not decide:
 Stop and escalate when:
 
 - product behavior, state, or user action is unclear;
+- the Editorial Decision Frame is missing, stale, or conflicts with the handoff
+  for a task handed from Chief Editor planning;
 - copy would require inventing a product rule or feature;
 - terminology conflicts with glossary, active client profile, or product
   constraints;
@@ -117,6 +124,8 @@ strategy beyond the assigned UX copy.
 ## Role-Specific Quality Checks
 
 - copy maps to real states and user actions;
+- copy follows the chosen editorial route and does not revive rejected
+  alternatives without explanation;
 - terminology is consistent with glossary, active client profile, and product
   context;
 - no product behavior was invented or changed;
diff --git a/ai-editorial-office/agents/writer_agent.md b/ai-editorial-office/agents/writer_agent.md
index 5c5e7b4..652d608 100644
--- a/ai-editorial-office/agents/writer_agent.md
+++ b/ai-editorial-office/agents/writer_agent.md
@@ -20,6 +20,8 @@ review.
 
 - understand task goal, audience, channel, output format, and constraints;
 - use structure-before-writing notes when present;
+- use the Editorial Decision Frame in `orchestration_plan.md` as the drafting
+  contract when present;
 - create or update `outline.md` before drafting when needed;
 - draft from the brief, approved research artifacts, active client profile, and
   relevant KB;
@@ -47,8 +49,8 @@ Conditional:
 
 - active client-profile files when `task-manifest.md` or `orchestration_plan.md`
   names `client_profile`;
-- `orchestration_plan.md` when it defines structure, scope, or acceptance
-  criteria;
+- `orchestration_plan.md` when it defines structure, scope, acceptance
+  criteria, or the Editorial Decision Frame;
 - `status.md` when blockers or prior state matter;
 - `research.md`, `facts.md`, `claims_table.md`, and `sources.md` when factual
   claims are required;
@@ -78,6 +80,8 @@ Conditional:
   is `pending_source` or the source rule has not been checked;
 - use unsupported or contradicted claims as facts;
 - silently change task goal, audience, channel, angle, or scope;
+- silently ignore the Editorial Decision Frame or reintroduce rejected
+  alternatives without a recorded reason;
 - become UX Writer for interface copy unless specifically assigned that role;
 - approve its own draft;
 - perform independent review or controlled finalization;
@@ -107,6 +111,8 @@ Stop and escalate when:
 
 - required brief, scope, evidence, client-profile context, or KB context is
   missing;
+- the Editorial Decision Frame is missing, stale, or conflicts with the handoff
+  for a task handed from Chief Editor planning;
 - claims needed for the draft are unsupported or contradicted;
 - the user or source material requires facts not in evidence;
 - requested changes would alter task goal, product behavior, or governance
@@ -122,6 +128,8 @@ should not repeat full research or status history.
 ## Role-Specific Quality Checks
 
 - draft serves the current brief rather than generic format expectations;
+- draft follows the chosen editorial route and does not revive rejected
+  alternatives without explanation;
 - factual claims are supported, caveated, or omitted;
 - tone, glossary, editorial policy, and active client profile are applied;
 - structure supports the reader path and avoids unnecessary duplication;
diff --git a/ai-editorial-office/templates/artifacts/handoff_template.md b/ai-editorial-office/templates/artifacts/handoff_template.md
index 14461a9..62bf7e0 100644
--- a/ai-editorial-office/templates/artifacts/handoff_template.md
+++ b/ai-editorial-office/templates/artifacts/handoff_template.md
@@ -36,6 +36,19 @@ transfer or explicit context migration.
 
 - ...
 
+## editorial decision transfer
+
+Use for Chief Editor planning handoff to Writer Agent or UX Writer. Keep short;
+do not repeat the full Editorial Decision Frame from `orchestration_plan.md`.
+Pass only the operational summary; rejected alternatives should be names or
+one-line reasons, not the full rationale. For other handoffs, use
+`not_applicable`.
+
+- Chosen route:
+- Rejected alternatives, names or one-line reasons:
+- Writing/UX writing contract:
+- Review focus:
+
 ## blockers and open questions
 
 - None / list with owner and required action.
diff --git a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
index e26a077..ea98fe5 100644
--- a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
+++ b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
@@ -76,6 +76,35 @@ unless a task-specific governance or restartability need justifies it.
 - If `constrain`: explicit scope boundary:
 - If `block`: blocking reason:
 
+## editorial decision frame
+
+Use before handing work to Writer Agent or UX Writer. If research is required,
+fill or refresh this after research sufficiency is known. Keep this as a short
+management block, not an analytical document. Do not duplicate research,
+outline, review, rejected-alternative addenda, or long rationale here. Do not
+create a standalone `editorial_decision.md` only because this reasoning is long;
+if the decision needs extended justification, use a task-local analytical
+artifact and keep this frame compact.
+
+- Chosen editorial route:
+- Why this route serves the task:
+- Alternatives considered, usually 2-3 compact options:
+  - Alternative route, one line:
+    - Why rejected, one line:
+  - Alternative route, one line:
+    - Why rejected, one line:
+  - Alternative route, one line, if useful:
+    - Why rejected, one line:
+- Writer/UX Writer contract:
+  - Result type:
+  - Angle or reader path:
+  - Scope boundary:
+  - Must include:
+  - Must not include:
+  - Source boundary and confidence:
+- Review focus:
+- Reroute triggers:
+
 ## custom workflow mini-contract
 
 Use only when the selected pipeline needs a documented local deviation. Do not
