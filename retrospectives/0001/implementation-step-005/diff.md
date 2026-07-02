# Step 5 diff

## `ai-editorial-office/agents/review_agent.md`

```diff
@@
 Review depth rules:
 
 - low-risk review may use a compact checklist section inside `review.md`, but review is still required;
 - standard review may use separate `qa-checklist.md` when required by the selected pipeline;
 - high-governance review requires full review depth and must not approve if source traceability, claim coverage, required research artifacts, reviewer independence, or human approval assessment is incomplete.
+
+Compact review minimum:
+
+- verdict: `approved`, `changes_requested`, or `blocked`;
+- reviewed artifact or artifact set;
+- lightweight independence check: writer/source role, reviewer role, result, and basis;
+- usefulness/pass rationale or blocking issues;
+- governance note when approval, finalization, or publication/delivery risk matters;
+- one clear next action.
+
+Normal review may use separate `qa-checklist.md` and `review-summary.md` when they have downstream consumers. Full review is reserved for high-governance or source-heavy work and should preserve detailed source, claim, artifact, independence, and governance evidence.
+
+Bounded revision is the default for `changes_requested`: name the issue, why it blocks approval, repair owner, repair scope, what not to change, and re-review scope. Full rewrite, new research, or orchestration escalation requires a blocker, evidence gap, instruction conflict, scope problem, reader outcome failure, or repeated failed repair.
 
 ## forbidden actions
@@
 The agent must produce:
 
 - `/tasks/TASK-ID/review.md`;
-- `/tasks/TASK-ID/qa-checklist.md`;
-- `/tasks/TASK-ID/review-summary.md`;
-- `/tasks/TASK-ID/reviewer-notes.md`;
 - `/tasks/TASK-ID/handoff-review-review-agent-to-chief-editor.md`.
 
+The agent produces `qa-checklist.md`, `review-summary.md`, or `reviewer-notes.md` only when review depth, downstream routing, risk, or unresolved caveats justify separate artifacts. Compact review may keep checklist and summary content inside `review.md`.
+
 The agent may also recommend updates to `/tasks/TASK-ID/status.md`.
@@
 `review outcome` must be exactly one of `approved`, `changes_requested`, or `blocked`.
+
+If outcome is `changes_requested`, `review.md` must include bounded revision fields:
+
+```markdown
+## Required change
+
+Issue:
+Why it blocks approval:
+Repair owner:
+Repair scope:
+Do not change:
+Re-review scope:
+```
+
+Re-review must focus on the stated repair scope unless the repair introduces a new blocker.
 
 ### qa-checklist.md structure
```

## `ai-editorial-office/pipelines/review_pipeline.md`

```diff
@@
 `low-risk` review may use a compact checklist section inside `review.md`. Review is still required before finalization.
 
 `standard` review may use separate `qa-checklist.md` under the normal Review Pipeline requirements.
 
 `high-governance` review must use full review depth and must not approve if source traceability, required research artifacts, claim coverage, reviewer independence, human approval assessment, or governance-sensitive caveats are incomplete.
+
+Compact review minimum:
+
+- verdict;
+- reviewed artifact or artifact set;
+- lightweight independence check;
+- usefulness/pass rationale or blocking issues;
+- governance note when relevant;
+- one next action.
+
+Normal review uses separate checklist or summary only when downstream review, routing, or risk needs them. Full review is required for high-governance and source-heavy work.
+
+For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope.
 
 ## review rule ownership
@@
 Review Pipeline is complete only when:
 
 - `task-manifest.md` is current and reflects review outcome and review artifact states;
 - required review inputs were checked or missing inputs were documented;
 - reviewer independence was checked;
 - `review.md` exists and includes reviewed artifacts, findings, blockers, required changes, and outcome;
-- `qa-checklist.md` exists with pass, fail, or not_applicable statuses;
-- `review-summary.md` exists with operational outcome and next action;
-- `reviewer-notes.md` exists;
+- `qa-checklist.md` exists with pass, fail, or not_applicable statuses when separate checklist depth is required;
+- `review-summary.md` exists with operational outcome and next action when concise transfer is not already covered by `review.md` and handoff;
+- `reviewer-notes.md` exists when extra caveats or borderline reasoning do not fit in `review.md`;
 - review outcome is exactly `approved`, `changes_requested`, or `blocked`;
 - review outcome maps to a valid operational status under `/kb/task_statuses.md`;
 - handoff exists to the correct next MVP role;
```

## `ai-editorial-office/AGENTS.md`

```diff
@@
 Если review требует изменений, задача возвращается к `writer_agent` для доработки draft, к `ux_writer` для доработки UX copy или к `research_agent` для восполнения evidence gaps. После изменений требуется повторный review.
+
+`changes_requested` по умолчанию означает bounded revision: review должен назвать blocking issue, repair owner, repair scope и re-review scope. Это не разрешение на полный rewrite, новый research или redesign без отдельного blocker, evidence gap, instruction conflict, scope problem или reader outcome failure.
 
 ## Canonical ownership of review rules
```

## `ai-editorial-office/project-state.md`

```diff
@@
 - Review changes_requested should be bounded by default; full rewrite, new research, or orchestration escalation requires a blocker, evidence gap, instruction conflict, or scope problem.
 - Bounded re-review should be clearly separated from the initial review inside review artifacts.
+- Compact review may keep checklist and summary in `review.md` when minimum evidence is present; separate review artifacts stay conditional.
 - Compact process depth is available only inside a selected pipeline when Chief Editor records the rationale, review target, and intentionally omitted artifacts. It is not a new pipeline and never removes review-gate.
```
