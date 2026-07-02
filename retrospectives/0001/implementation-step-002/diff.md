# Step 2 diff

## `ai-editorial-office/AGENTS.md`

```diff
@@
 `intake_agent` proposes risk mode. `chief_editor` confirms or overrides it during orchestration. If risk mode is `unknown`, it must be resolved before writing or UX writing begins. High-governance tasks require explicit rationale, research, full review, human approval assessment, and a Chief Editor governance decision.
 
+## Process depth
+
+Process depth controls how much artifact detail a task needs inside the selected pipeline. It is not a separate pipeline and does not change lifecycle, statuses, role separation, or review-gate requirements.
+
+Allowed depth values:
+
+- `compact` — for low-risk or simple standard tasks where fewer artifacts do not reduce review, restartability, traceability, or governance clarity.
+- `normal` — default depth for standard tasks when compact is not clearly safe and full depth is not needed.
+- `full` — required for high-governance, source-heavy, sensitive, multi-audience, or high factual sensitivity tasks.
+
+Compact path may be used only when all are true:
+
+- risk mode is `low-risk`, or `standard` with simple source-light scope;
+- no high-governance sensitivity is present;
+- source traceability is not needed for material factual, product, policy, numeric, legal, financial, HR, medical, security, regulatory, or reputational claims;
+- the task has one primary deliverable or a small coherent deliverable set;
+- review can validate the output without a large evidence base.
+
+Compact path is forbidden when:
+
+- risk mode is `high-governance`;
+- sources conflict or material claims need claim-level traceability;
+- human approval state is material and unresolved;
+- the task has multiple audiences with different artifact needs;
+- review cannot validate safely without full artifact context.
+
+Compact path never removes review. It may reduce or combine supporting artifacts only when `chief_editor` records the process depth, rationale, review target, and artifacts intentionally omitted in `orchestration_plan.md`, `task-manifest.md`, or `status.md`.
+
 Каждая задача должна проходить через контролируемые этапы:
```

## `ai-editorial-office/agents/chief_editor.md`

```diff
@@
 High-governance requires explicit rationale, research, stricter artifact requirements, full review, explicit human approval assessment, and a final governance decision that does not silently imply publication or delivery approval.
 
+Process depth is selected by the Chief Editor during orchestration: `compact`, `normal`, or `full`. This is a profile inside the selected pipeline, not a new pipeline. Compact depth is forbidden for high-governance tasks and never removes review-gate. If compact depth is chosen, record the rationale, review target, and intentionally omitted artifacts in `orchestration_plan.md`, `task-manifest.md`, or `status.md`.
+
 Structure-before-writing pressure applies before writing or UX writing when the material teaches, instructs, routes, supports repeated use, or may be read selectively. The Chief Editor should add compact planning notes, not a separate architecture document.
@@
 This agent may decide:
 
 - which pipeline should govern the task;
+- which process depth should apply inside the selected pipeline;
 - which specialized agent should handle the next stage;
```

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

```diff
@@
 Classification rationale:
 
 - `{reason_1}`;
 - `{reason_2}`.
 
+## process depth
+
+Depth: `{compact | normal | full}`
+
+Depth rationale:
+
+- `{short_reason}`;
+
+Compact path check, if depth is `compact`:
+
+- Allowed because: `{low-risk_or_simple_standard_source-light_reason}`;
+- High-governance excluded: `{yes}`;
+- Review still required: `yes`;
+- Review target: `{artifact_or_artifact_set}`;
+- Artifacts intentionally omitted: `{artifact_list_and_one-line_rationale_or_none}`.
+
+Use `normal` unless compact is clearly safe or full depth is required. Compact depth is not a new pipeline and does not change lifecycle, statuses, role separation, or review-gate requirements.
+
 ## selected pipeline
 
 Pipeline file: `/pipelines/{pipeline_name}.md`
```

## `ai-editorial-office/pipelines/article_pipeline.md`

```diff
@@
 `low-risk`:
 
 - research may be skipped with a no-research rationale;
 - evidence artifacts may be combined or omitted when no factual claims are used;
-- future low-risk tasks may use a more compact artifact path when Chief Editor records that choice; this is not automatic in the current MVP;
+- compact process depth may be used when Chief Editor records the choice, rationale, review target, and intentionally omitted artifacts;
 - review is still required, but checklist may be compact inside `review.md`;
 - finalization may be lightweight;
 - handoff must remain compact.
```

## `ai-editorial-office/project-state.md`

```diff
@@
 - Latest handoff is delta-based and should reference task-manifest.md instead of repeating manifest, status, orchestration, KB, restart notes, or full task state.
 - Handoff filenames use one receiving role; route ambiguity belongs inside the handoff body.
 - Late-stage task-manifest next action packets should list only files the next role truly needs.
 - Review changes_requested should be bounded by default; full rewrite, new research, or orchestration escalation requires a blocker, evidence gap, instruction conflict, or scope problem.
 - Bounded re-review should be clearly separated from the initial review inside review artifacts.
-- Future low-risk tasks may use a more compact artifact path, but this is not automatic in the current MVP.
+- Compact process depth is available only inside a selected pipeline when Chief Editor records the rationale, review target, and intentionally omitted artifacts. It is not a new pipeline and never removes review-gate.
 
 ## Artifact minimalism
```
