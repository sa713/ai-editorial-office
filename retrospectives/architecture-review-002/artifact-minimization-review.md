# Artifact minimization review

## Реально используемые артефакты

Почти всегда нужны:

- `brief.md`;
- `task-manifest.md`;
- `status.md`;
- `orchestration_plan.md`;
- рабочий результат этапа: `draft.md`, `ux-copy.md`, `diagnosis.md`, `recommendations.md`, `presentation-outline.md`;
- `review.md`;
- `final_decision.md`, если задача закрывается как редакционная система.

Нужны по условию:

- `research.md`, `sources.md`, `facts.md`, `claims_table.md`;
- `claims-used.md`;
- `qa-checklist.md`;
- `review-summary.md`;
- `finalization-notes.md`;
- `finalization-checklist.md`;
- `compact-handoff.md`;
- `context-summary.md`.

## Что создаётся на всякий случай

- `open-questions.md` с пустым или почти пустым содержанием.
- `qa-checklist.md` для задач, где checklist мог быть в `review.md`.
- `review-summary.md`, когда next action уже есть в `review.md`.
- `finalization-notes.md`, когда финализация не меняла смысл.
- Полные таблицы артефактов в нескольких местах.
- Версионные файлы без указателя, какая версия текущая.

## Что сделать conditional

- `open-questions.md`: создавать только если есть вопрос, влияющий на работу.
- `qa-checklist.md`: отдельно только для standard с реальной сложностью и high-governance.
- `review-summary.md`: только если следующей роли нужен короткий перенос решения.
- `reviewer-notes.md`: только если есть нерешённые наблюдения вне основного review.
- `finalization-checklist.md`: только при существенной финализации или high-governance.
- `compact-handoff.md`: только как финальная пользовательская передача, не как обычный handoff.
- `context-summary.md`: только после потери контекста, а не в штатном процессе.

## Что можно объединить

- `review.md` + `qa-checklist.md` для низкого риска.
- `review.md` + `review-summary.md`, если решение короткое.
- `finalization-notes.md` + `final_decision.md`, если финализация не меняла смысл.
- `writer-notes.md` + `claims-used.md`, если фактов мало и каждый claim легко виден в тексте.
- `task-manifest.md` + короткий status для low-risk, если не нужна длинная история.

## Что убрать из low-risk

- отдельный `qa-checklist.md`;
- отдельный `review-summary.md`;
- отдельный `finalization-checklist.md`;
- длинные role-to-role handoff;
- полный список всех возможных артефактов;
- подробный restart checklist в каждом файле.

## Где артефакты дублируют друг друга

- `task-manifest.md` и `status.md`: текущий статус, владелец, следующий шаг.
- `status.md` и `orchestration_plan.md`: pipeline, роли, список файлов.
- `handoff-*` и `task-manifest.md`: следующий шаг, ограничения, blockers.
- `review.md`, `qa-checklist.md`, `review-summary.md`: результат проверки, риски, действия.
- `finalization-notes.md`, `finalization-checklist.md`, `final_decision.md`: проверка, что финал не вышел за review.

## Минимальное правило

Один смысл — один файл. Если второй файл нужен, он должен отвечать на другой вопрос или быть нужен другой роли.

