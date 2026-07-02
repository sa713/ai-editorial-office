# Diff

Purpose: diff of system files changed by `SYSTEM-MAINTENANCE-UPDATE-0021`.

Note: the repository currently has no tracked git baseline for these files, so
this artifact records the task-authored unified diff rather than raw `git diff`
output.

## `ai-editorial-office/AGENTS.md`

```diff
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
--- a/ai-editorial-office/AGENTS.md
+++ b/ai-editorial-office/AGENTS.md
@@
 Before production starts, Chief Editor must route the task editorially:
 
 - determine the task type;
 - choose the relevant pipeline or editorial mode;
 - activate the visual branch when the selected task requires it;
 - determine the required roles and bounded extension roles;
+- make a compact preflight decision about input sufficiency before production;
 - record the routing decision in `orchestration_plan.md`, `task-manifest.md`,
   or `status.md`.
+
+The preflight decision answers whether the system understands the task well
+enough to start production, what is missing, and whether the next action is
+`ask`, `constrain`, `proceed`, or `block`. It is a decision gate, not a new
+pipeline, role, status, or mandatory standalone artifact.
@@
 2. Orchestration
 
    `chief_editor` выбирает pipeline, назначает core roles или явно легализованные extension roles только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
+
+   Before production starts, `chief_editor` records or confirms a compact
+   Preflight Gate decision in an existing task artifact. The required fields are:
+   Audience (`confirmed` / `inferred` / `unknown`), Channel or context
+   (`confirmed` / `inferred` / `unknown`), Deliverable (`defined` / `unclear`),
+   Source boundary (`defined` / `unclear`), Success criterion (`defined` /
+   `unclear`), Approval boundary (`defined` / `unclear`), and Missing data
+   strategy (`ask` / `constrain` / `proceed` / `block`).
+
+   The system is not required to ask a question. It is required to decide. Use
+   `ask` when critical information is missing, `constrain` when safe narrowing
+   is enough, `proceed` when the available input is sufficient, and `block` when
+   the task cannot be performed safely.
@@
 - optional artifacts must not silently become mandatory;
 - low-risk and simple standard tasks use `review.md` as the sole review artifact unless a separate support artifact is justified;
+- Preflight Gate is a compact decision in an existing task artifact, not a new
+  mandatory file;
 - `feedback.md` is optional and created only when post-delivery user reaction exists;
```

## `ai-editorial-office/agents/chief_editor.md`

```diff
diff --git a/ai-editorial-office/agents/chief_editor.md b/ai-editorial-office/agents/chief_editor.md
--- a/ai-editorial-office/agents/chief_editor.md
+++ b/ai-editorial-office/agents/chief_editor.md
@@
 - select or confirm the appropriate pipeline and process depth;
 - confirm or resolve risk mode before production starts;
+- make a compact Preflight Gate decision before production starts;
 - assign work only to current core roles or explicitly legalized extension roles;
@@
 - `orchestration_plan.md` when routing or updating execution;
 - role specs for agents being assigned;
 - relevant KB files required by the chosen pipeline;
+- normalized preflight inputs when available: audience, channel/context,
+  deliverable, source boundary, success criterion, approval boundary, and
+  missing data strategy;
 - production, review, and finalization artifacts before readiness decisions;
@@
- `orchestration_plan.md`;
- status updates or status recommendations;
- role-to-role handoff artifacts;
-- `final_decision.md` for final governance readiness.
+- `final_decision.md` for final governance readiness;
+- compact Preflight Gate decision before production, recorded in an existing
+  artifact.
@@
 - treat post-delivery feedback as automatic task reopening, review failure, or
   retroactive downgrade of the final decision;
+- start production without deciding whether missing data should lead to `ask`,
+  `constrain`, `proceed`, or `block`;
+- turn preflight into automatic clarifying-question generation;
 - require optional artifacts without downstream, governance, task-specific, or
@@
 - pipeline, risk mode, and process depth;
 - role routing and next owner;
 - whether current evidence is sufficient to continue orchestration;
+- whether the Preflight Gate strategy is `ask`, `constrain`, `proceed`, or
+  `block`;
 - whether final governance readiness can be recorded after review;
@@
 - risk mode is `unknown` before production;
+- Preflight Gate outcome is `ask` or `block` and production would start anyway;
 - required input, pipeline, or KB context is missing;
@@
 - final readiness is based on saved artifacts, not chat memory;
+- preflight decisions are explicit before production but do not force a separate
+  artifact or unnecessary user question;
 - no legacy heavy folder structure is treated as a required template.
```

## `ai-editorial-office/agents/intake_agent.md`

```diff
diff --git a/ai-editorial-office/agents/intake_agent.md b/ai-editorial-office/agents/intake_agent.md
--- a/ai-editorial-office/agents/intake_agent.md
+++ b/ai-editorial-office/agents/intake_agent.md
@@
 - normalize the raw request into task title, goal, audience, output, channel,
   and constraints;
+- surface preflight inputs for Chief Editor: audience, channel/context,
+  deliverable, source boundary, success criterion, approval boundary, missing
+  information, and safe assumptions;
 - identify task type and likely pipeline;
@@
 - how to normalize the request into a task package;
 - initial classification and likely pipeline recommendation;
-- whether ambiguity must be surfaced before orchestration.
+- whether ambiguity must be surfaced before orchestration;
+- which input gaps are likely material for Chief Editor preflight.
 
 The Intake Agent must not decide:
 
 - final pipeline approval;
+- final Preflight Gate outcome;
 - research conclusions;
```

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
--- a/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
+++ b/ai-editorial-office/templates/artifacts/orchestration_plan_template.md
@@
 ## selected pipeline
 
 - Pipeline:
 - Why this pipeline:
 - Pipeline exceptions or local constraints:
+
+## preflight gate
+
+Use before production starts. Keep compact; do not create a separate artifact
+unless a task-specific governance or restartability need justifies it.
+
+| Field | Decision |
+| --- | --- |
+| Audience | `confirmed` / `inferred` / `unknown` |
+| Channel or context | `confirmed` / `inferred` / `unknown` |
+| Deliverable | `defined` / `unclear` |
+| Source boundary | `defined` / `unclear` |
+| Success criterion | `defined` / `unclear` |
+| Approval boundary | `defined` / `unclear` |
+| Missing data strategy | `ask` / `constrain` / `proceed` / `block` |
+
+- Rationale:
+- Production may start: yes/no
+- If `ask`: smallest question to user:
+- If `constrain`: explicit scope boundary:
+- If `block`: blocking reason:
 
 ## custom workflow mini-contract
```
