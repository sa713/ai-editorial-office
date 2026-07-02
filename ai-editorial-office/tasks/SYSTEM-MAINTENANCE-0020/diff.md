# Diff

Purpose: task-authored diff for the system files requested after
`SYSTEM-MAINTENANCE-0020` finalization.

Note: the repository currently has no tracked git baseline for these files, so
this artifact records the intended task diff rather than output from
`git diff`.

## `ai-editorial-office/AGENTS.md`

```diff
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
--- a/ai-editorial-office/AGENTS.md
+++ b/ai-editorial-office/AGENTS.md
@@
 | Review artifact | `/tasks/TASK-ID/review.md` | verdict, findings, checked scope, required changes |
 | Final decision | `/tasks/TASK-ID/final_decision.md` | Chief Editor final governance decision |
+| Post-delivery task feedback | `/tasks/TASK-ID/feedback.md` | optional reaction record after delivery |
+| Recurring feedback patterns | `/kb/feedback_patterns.md` | pattern journal, not raw feedback archive |
 
 Rule placement check:
@@
 Default operating workflow:
 
 ```text
 intake -> orchestration -> research if needed -> writing or ux-writing -> review -> finalization -> chief_editor final governance decision
 ```
+
+Optional post-delivery feedback capture may happen after the Chief Editor final
+governance decision when the user reacts to a delivered result. It is not an
+operational status, does not reopen the task automatically, and does not make
+the completed result worse retroactively.
+
+When feedback exists, `chief_editor` may create `/tasks/TASK-ID/feedback.md`.
+No user reaction means no feedback artifact is required.
+
+If the user asks for changes after delivery, distinguish:
+
+- feedback as a quality signal;
+- a new task when the request broadens or changes scope;
+- a bounded revision of the current task only when the current system rules
+  allow it.
+
+A single feedback item does not change the system automatically. System changes
+must follow:
+
+```text
+single feedback ↓ repeated signal ↓ validated pattern ↓ system change proposal ↓ separate reviewed system update
+```
 
 ## Risk Modes
@@
 - optional artifacts must not silently become mandatory;
 - low-risk and simple standard tasks use `review.md` as the sole review artifact unless a separate support artifact is justified;
+- `feedback.md` is optional and created only when post-delivery user reaction exists;
 - `review-summary.md`, `qa-checklist.md`, `finalization-checklist.md`, `open-questions.md`, and `finalization-notes.md` are conditional: create them only for an explicit downstream consumer, high-governance mode, a task-specific requirement, real open questions/blockers, or traceability need;
 - agents must not create speculative placeholder files for future use;
@@
 | `review-summary.md` | concise review outcome and next action | full review reasoning or QA checklist |
 | `finalization-notes.md` | controlled finalization decisions after approved review | review findings, governance decision, or final copy |
 | `finalization-checklist.md` | finalization proof when high governance, downstream governance, task requirement, or traceability needs it | routine finalization already evident from `review.md`, `final.md`, and handoff |
+| `feedback.md` | optional post-delivery user reaction record | review outcome, bounded revision plan, system rule change |
```

## `ai-editorial-office/agents/chief_editor.md`

```diff
diff --git a/ai-editorial-office/agents/chief_editor.md b/ai-editorial-office/agents/chief_editor.md
--- a/ai-editorial-office/agents/chief_editor.md
+++ b/ai-editorial-office/agents/chief_editor.md
@@
 - verify that an independent `review.md` exists before finalization or final
   governance;
 - record final governance readiness in `final_decision.md` when the task reaches
-  final decision.
+  final decision;
+- after delivery, optionally capture user reaction in `feedback.md` when
+  feedback actually exists, without reopening the task automatically;
+- route repeated or significant feedback signals to `/kb/feedback_patterns.md`
+  only when they may represent a system pattern rather than a one-off reaction.
@@
 Conditional:
 
 - compact context or recovery notes only when restart safety requires them;
-- blocker notes when orchestration cannot continue.
+- blocker notes when orchestration cannot continue;
+- `feedback.md` after delivery, only when user reaction exists.
@@
 - collapse specialist stages into one role;
 - treat finalized material as published, delivered, or human-approved without
   explicit evidence;
+- change system rules from a single feedback item;
+- treat post-delivery feedback as automatic task reopening, review failure, or
+  retroactive downgrade of the final decision;
 - require optional artifacts without downstream, governance, task-specific, or
   traceability need;
@@
 - pipeline, risk mode, and process depth;
 - role routing and next owner;
 - whether current evidence is sufficient to continue orchestration;
-- whether final governance readiness can be recorded after review.
+- whether final governance readiness can be recorded after review;
+- whether post-delivery user reaction is task-local feedback, a possible
+  system signal, a new task, or an allowed bounded revision.
```

## `ai-editorial-office/agents/review_agent.md`

```diff
diff --git a/ai-editorial-office/agents/review_agent.md b/ai-editorial-office/agents/review_agent.md
--- a/ai-editorial-office/agents/review_agent.md
+++ b/ai-editorial-office/agents/review_agent.md
@@
 - validate factual claims against available evidence and claim traceability;
 - detect unsupported claims, hallucination risk, contradictions, tone or glossary
   violations, structural problems, and reader-outcome failures;
+- when reviewing feedback-loop or system-process updates, verify that feedback
+  remains optional and does not bypass review, governance, or status rules;
 - apply risk-appropriate review depth without making review optional;
@@
 - findings distinguish blockers from improvements;
 - factual, editorial, structural, UX, and governance risks are covered when
   relevant;
+- post-delivery feedback handling, when present, does not make one reaction a
+  system rule, reopen finalized tasks automatically, create a new role, or add a
+  mandatory pipeline;
 - high-governance review preserves traceability and approval evidence;
```

## `ai-editorial-office/agents/final_editor.md`

No changes in `SYSTEM-MAINTENANCE-0020`.

## `ai-editorial-office/templates/artifacts/feedback_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/feedback_template.md b/ai-editorial-office/templates/artifacts/feedback_template.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/templates/artifacts/feedback_template.md
@@
+# Feedback
+
+Purpose: optional task-local record of user reaction after delivery. Create this
+file only when the user actually responds to a delivered result.
+
+```text
+Один feedback не меняет систему автоматически.
+```
+
+## metadata
+
+- Task ID:
+- Captured date:
+- Captured by: `chief_editor`
+- Related final decision:
+- Related delivered artifact:
+
+## user reaction
+
+- Short summary:
+- Reaction type: `accepted` / `praised` / `needs revision` / `rejected` / `unclear` / `mixed`
+- User wording or paraphrase:
+
+## feedback scope
+
+Relates to:
+
+- understanding the task: yes/no
+- structure: yes/no
+- meaning: yes/no
+- tone: yes/no
+- format: yes/no
+- facts: yes/no
+- process: yes/no
+- usefulness: yes/no
+- other:
+
+## signal classification
+
+- Classification: `single feedback` / `possible system signal`
+- Why:
+- Similar known signals:
+- Should this be considered for `/kb/feedback_patterns.md`: yes/no
+
+## follow-up boundary
+
+- Follow-up needed: yes/no/unclear
+- Follow-up type: none / new task / bounded revision / clarification / system-pattern watch
+- Does this reopen the task automatically: no
+- Does this change the final decision retroactively: no
+
+## what not to infer
+
+- Do not infer:
+- System rules changed by this feedback: no
```

## `ai-editorial-office/kb/feedback_patterns.md`

```diff
diff --git a/ai-editorial-office/kb/feedback_patterns.md b/ai-editorial-office/kb/feedback_patterns.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/kb/feedback_patterns.md
@@
+# Feedback Patterns
+
+Purpose: system-level journal for recurring or significant user feedback
+patterns. This file is not a raw archive of every `feedback.md`.
+
+Use this file only when task-local feedback suggests a pattern worth tracking
+across tasks.
+
+```text
+Один feedback не меняет систему автоматически.
+single feedback ↓ repeated signal ↓ validated pattern ↓ system change proposal ↓ separate reviewed system update
+```
+
+## pattern statuses
+
+- `observed` - one or more signals noticed, not yet validated.
+- `recurring` - similar signal appears across multiple tasks or contexts.
+- `validated` - review confirms the signal is system-relevant, not only taste or a one-off task issue.
+- `system-change-proposed` - a future system update has been proposed but not implemented.
+- `addressed` - a separate reviewed system update has addressed the pattern.
+
+## entry template
+
+```markdown
+## Pattern: <short name>
+
+- Status: `observed` / `recurring` / `validated` / `system-change-proposed` / `addressed`
+- First observed:
+- Last updated:
+- Sources / TASK-:
+- Short description:
+- Why this is a system signal, not a single taste reaction:
+- Related feedback scope: understanding / structure / meaning / tone / format / facts / process / usefulness / other
+- Possible future system changes:
+- Required next review:
+```
+
+## active patterns
+
+No validated patterns yet.
```
