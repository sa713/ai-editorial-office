# Orchestration Plan

## task summary

- Task ID: TASK-0022
- User goal: переписать только ответ в `task.md`, не меняя вопрос.
- Deliverable: обновленный `task.md` и короткая заметка об улучшениях.
- Audience/channel: ответственное подразделение или место дальнейшего использования ответа.
- Current active version: `task.md`

## task classification

- Task type: compact editorial rewrite of an existing answer
- Risk mode: standard
- Factual sensitivity: medium, because the answer mentions internal security policy, risk assessment, and профильные подразделения.
- Human approval likely required: unknown for publication/delivery; not required for editorial completion.
- Rationale: задача не требует новых фактов, но требует аккуратного сохранения policy/security-смысла.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: один короткий ответ, один источник фактов, нет запроса на исследование или расширенную фактологию.
- Forbidden depth shortcuts: review-gate, role boundaries, source boundary, and final governance are preserved.
- Expanded profile trigger, if any: обнаружение противоречий, необходимость новых фактов, изменение вопроса, или риск добавления новых обязательств.

## selected pipeline

- Pipeline: Article Pipeline as governing lifecycle, operated as compact editorial rewrite mode.
- Why this pipeline: результат является deliverable editorial text, not UX copy or research-only work.
- Pipeline exceptions or local constraints: no separate research, sources, facts, claims table, outline, QA checklist, or review summary; review is compact inside `review.md`.

## custom workflow mini-contract

- Deviation: source-constrained rewrite of the answer directly from `task.md`.
- Reason: user explicitly asks to rewrite only the existing answer and preserve facts.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | Chief Editor | yes | Compact brief created from user request. |
| Research | Research Agent | no | No external or new facts allowed. |
| Writing | Writer Agent | yes | Rewrite answer only; preserve question. |
| Review | Review Agent | yes | Check source-boundary, factual preservation, and no new commitments. |
| Finalization | Final Editor | yes | Apply approved text to `task.md`; create final artifact. |
| Final governance | Chief Editor | yes | Record final readiness. |

## required knowledge and evidence

- Required KB: `AGENTS.md`, `kb/task_statuses.md`, selected lifecycle rules from `article_pipeline.md`.
- Required source/evidence files: `task.md`, `brief.md`, `source-snapshot.md`.
- Evidence gaps: none for the requested editorial rewrite.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Captures exact rewrite boundary. |
| `task-manifest.md` | required | all roles | Restart and governance anchor. |
| `status.md` | required | all roles | State transitions and review state. |
| `orchestration_plan.md` | required | all roles | Routing and compact-mode evidence. |
| `source-snapshot.md` | required | Review Agent / Chief Editor | Preserves original answer after `task.md` is updated. |
| `draft.md` | required | Review Agent | Text under review. |
| `writer-notes.md` | required | Review Agent | Source-boundary notes. |
| `review.md` | required | Final Editor / Chief Editor | Independent review gate. |
| `final.md` | required | Chief Editor | Controlled finalization artifact. |
| `editorial-note.md` | required by user | User / Chief Editor | Short note on improvements. |
| `qa-checklist.md` | omitted | none | Compact review is sufficient. |
| `review-summary.md` | omitted | none | `review.md` and handoff are sufficient. |
| research artifacts | omitted | none | New research is outside the task. |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user request, `task.md` | brief, manifest, plan, status | Route recorded. |
| 2 | Writer Agent | brief, `task.md` | `draft.md`, `writer-notes.md` | Answer rewrite ready for review. |
| 3 | Review Agent | `source-snapshot.md`, draft, brief | `review.md` | Verdict `approved` or bounded changes. |
| 4 | Final Editor | approved review, draft | `final.md`, updated `task.md`, `editorial-note.md` | Final answer applied. |
| 5 | Chief Editor | final, review, manifest | `final_decision.md`, status update | Task finalized. |

## review requirements

- Review artifact: `review.md`
- Review depth: compact
- Reviewer independence requirement: Review Agent checks Writer Agent output and does not rewrite.
- Claims/evidence checks required: compare draft against `source-snapshot.md` only; verify no new promise, срок, решение, or obligation.
- Optional review artifacts justified: no.

## completion criteria

- Required artifacts complete: yes
- Review outcome acceptable: `approved`
- Blockers resolved: yes
- Governance fields complete: yes

## restart notes

- Minimum read set: `task-manifest.md`, `brief.md`, `task.md`, `source-snapshot.md`, latest relevant handoff, `review.md` when finalizing.
- Current active version: updated `task.md`
- Deprecated/previous versions: original answer only visible through chat/history; not a working artifact.
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Directly relevant pipeline/KB: `article_pipeline.md`, `kb/task_statuses.md`
