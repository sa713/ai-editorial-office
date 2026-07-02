# Target files for next implementation step

Этот список задает потенциальные файлы будущего внедрения. В рамках этой спецификации сами файлы не редактируются.

## `ai-editorial-office/AGENTS.md`

- Зачем нужен: canonical owner системных invariants.
- Предполагаемые изменения: короткая ссылка на ownership, compact path boundaries, review-gate preservation, finalization/publication boundary.
- Canonical ownership: role separation, review-gate, authority hierarchy, context policy, artifact minimalism, governance boundaries.
- Нельзя добавлять: полный pipeline sequence, подробные template fields, длинные examples, editorial doctrine.
- Risk drift: высокий, если AGENTS начнет повторять все новые правила вместо кратких инвариантов.

## `ai-editorial-office/project-state.md`

- Зачем нужен: зафиксировать текущую system iteration как bounded documentation/template update.
- Предполагаемые изменения: статус следующего system update, active MVP constraints, ссылка на approved iteration scope.
- Canonical ownership: current phase, active constraints, current system-level decisions.
- Нельзя добавлять: permanent policy, pipeline details, agent behavior.
- Risk drift: средний, если временные решения останутся как policy.

## `ai-editorial-office/kb/task_statuses.md`

- Зачем нужен: уточнить status/governance semantics, если текущие статусы конфликтуют с new governance block.
- Предполагаемые изменения: короткое различение review outcome, finalization status, governance status, publication/delivery approval.
- Canonical ownership: allowed statuses, transitions, blocked/human approval semantics.
- Нельзя добавлять: artifact lists, compact review template, pipeline sequence.
- Risk drift: высокий, если governance block станет альтернативной status system.

## `ai-editorial-office/pipelines/article_pipeline.md`

- Зачем нужен: один из основных pipeline targets для compact/normal/full depth note.
- Предполагаемые изменения: короткая note о process depth, compact forbidden shortcuts и review still required.
- Canonical ownership: article stage sequence and article-specific artifact requirements.
- Нельзя добавлять: global AGENTS rules, full ownership map, new editorial modes.
- Risk drift: средний, если article pipeline начнет определять compact иначе, чем canonical guidance.

## `ai-editorial-office/pipelines/social_pipeline.md`

- Зачем нужен: вероятный low-risk/simple standard use case для compact path.
- Предполагаемые изменения: compact path usage note for source-light social tasks.
- Canonical ownership: social content pipeline sequence and review focus.
- Нельзя добавлять: publication approval shortcuts, channel-specific micro-modes, full governance theory.
- Risk drift: высокий, если social output mistaken as safe to publish without human approval.

## `ai-editorial-office/pipelines/ux_writing_pipeline.md`

- Зачем нужен: короткие tasks могут выигрывать от compact path, но product claims могут требовать traceability.
- Предполагаемые изменения: compact allowed/forbidden note tied to product/policy claim risk.
- Canonical ownership: UX writing sequence and UX-specific review focus.
- Нельзя добавлять: product governance matrix, new UX modes, full claims doctrine.
- Risk drift: высокий, если compact path ослабит source traceability for product claims.

## `ai-editorial-office/pipelines/review_pipeline.md`

- Зачем нужен: закрепить compact/normal/full review depth and bounded revision.
- Предполагаемые изменения: compact review shape, independence check, bounded revision fields.
- Canonical ownership: review sequence, review artifacts, review depth behavior.
- Нельзя добавлять: writer instructions, full finalization logic, scoring model.
- Risk drift: высокий, если compact review станет optional or shallow approval.

## `ai-editorial-office/pipelines/research_pipeline.md`

- Зачем нужен: source trust rule and traceability boundary for factual tasks.
- Предполагаемые изменения: note that compact path cannot omit traceability when factual claims matter.
- Canonical ownership: research sequence, source handling, evidence artifacts.
- Нельзя добавлять: broad security framework, labels for every paragraph, web research automation.
- Risk drift: средний, если source trust rule becomes ritual.

## `ai-editorial-office/agents/chief_editor.md`

- Зачем нужен: Chief Editor selects process depth and records rationale.
- Предполагаемые изменения: short note on selecting compact/normal/full, artifact omissions, custom workflow mini-contract.
- Canonical ownership: governance decisions, orchestration, final responsibility boundaries.
- Нельзя добавлять: full pipeline text, new role duties, automation behavior.
- Risk drift: высокий, если Chief Editor becomes workflow engine.

## `ai-editorial-office/agents/review_agent.md`

- Зачем нужен: review ergonomics and independence evidence live in reviewer behavior.
- Предполагаемые изменения: compact review minimum, independence check, bounded revision fields.
- Canonical ownership: review mission, findings, approval/changes_requested/blocked behavior.
- Нельзя добавлять: final approval to publish, rewrite duties, scoring.
- Risk drift: высокий, если reviewer starts finalizing or approving publication.

## `ai-editorial-office/agents/writer_agent.md`

- Зачем нужен: bounded revision affects how writer repairs after review.
- Предполагаемые изменения: short note to obey repair scope and do-not-change fields.
- Canonical ownership: writing and revision behavior.
- Нельзя добавлять: review authority, governance decisions, source trust policy.
- Risk drift: средний, если writer treats bounded revision as permission to rewrite broadly.

## `ai-editorial-office/agents/final_editor.md`

- Зачем нужен: finalization must not imply publication/delivery approval.
- Предполагаемые изменения: short note separating final polish/final artifact from governance approval.
- Canonical ownership: final editing and finalization behavior.
- Нельзя добавлять: human approval authority, review re-decision, publication permission.
- Risk drift: высокий, если final editor collapses finalization and approval.

## `ai-editorial-office/templates/artifacts/task_manifest_template.md`

- Зачем нужен: target place for freshness and governance state blocks.
- Предполагаемые изменения: concise fields only.
- Canonical ownership: fillable current-state fields.
- Нельзя добавлять: long explanations, full status history, review findings.
- Risk drift: высокий, если manifest becomes second status.

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

- Зачем нужен: process depth, omitted artifacts and custom workflow mini-contract belong in orchestration.
- Предполагаемые изменения: compact process depth section and custom workflow mini-contract fields.
- Canonical ownership: task-specific execution contract fields.
- Нельзя добавлять: full pipeline copy, status log, complete artifact contents.
- Risk drift: средний, если custom workflow becomes hidden pipeline.

## `ai-editorial-office/templates/artifacts/final_decision_template.md`

- Зачем нужен: final governance status and publication/delivery approval clarity.
- Предполагаемые изменения: short explicit fields for editorial finalized, human approval required, publication/delivery approval.
- Canonical ownership: final governance decision fields.
- Нельзя добавлять: final text body, review details, approval matrix.
- Risk drift: высокий, если final decision implies human send/publish permission.

## `ai-editorial-office/templates/artifacts/handoff_template.md`

- Зачем нужен: role-to-role delta transfer shape.
- Предполагаемые изменения: clarify `handoff-STAGE-FROM-to-TO.md` purpose and what not to include.
- Canonical ownership: handoff fields.
- Нельзя добавлять: full task restart pack, artifact inventory as primary source, status history.
- Risk drift: средний, если handoff duplicates manifest.

## `editorial_knowledge/10_operational_rules.md`

- Зачем нужен: source trust rule and anti-bloat principle may belong here if not owned by AGENTS/templates.
- Предполагаемые изменения: short operational rule only.
- Canonical ownership: editorial operating judgment, not task state.
- Нельзя добавлять: statuses, pipeline sequences, template fields.
- Risk drift: средний, если editorial knowledge starts owning workflow.

## `editorial_knowledge/40_editorial_review_system.md`

- Зачем нужен: usefulness-first review philosophy can reference compact review without operational template bloat.
- Предполагаемые изменения: short distinction between review depth and review existence.
- Canonical ownership: editorial review quality.
- Нельзя добавлять: artifact inventory, status transitions, governance block.
- Risk drift: средний, если philosophy duplicates pipeline review rules.
