# Reviewer notes

## Самые спорные места

- Compact path: нужно подтвердить, что allow/deny rules достаточно ясны и не создают hidden bypass.
- Governance state: полезно ли добавлять все поля, или часть стоит оставить только для late-stage tasks.
- Target files: возможно, часть templates не существует сейчас; внедрение должно не создавать лишние templates ради симметрии.
- Source trust rule: важно не превратить его в тяжелую classification procedure.

## Решения, требующие человеческого подтверждения

- Где физически разместить ownership map.
- Нужно ли трогать `AGENTS.md`, или достаточно отдельного canonical doc plus short pointer.
- Какие pipelines получают notes в первой итерации, а какие ждут trial.
- Нужны ли manifest governance fields для всех задач или только at/after review.
- Должен ли `compact-handoff.md` остаться только final user-facing summary.

## Риск over-simplification

- Compact review может стать слишком коротким и потерять usefulness check.
- Omitted artifacts могут скрыть потерю source traceability.
- Bounded revision может лечить локальный симптом вместо reader outcome failure.
- Не мигрировать old tasks правильно, но legacy examples могут продолжить заражать naming.

## Риск новой бюрократии

- Ownership map может стать новым doctrine layer.
- Governance block может вырасти в approval matrix.
- Custom workflow mini-contract может стать обязательным даже when pipeline fits.
- Source labels могут появляться везде без реального trust boundary.
- Validation checklist может превратиться в ritual completion вместо поиска drift.

## Что reviewer должен проверить первым

1. Спецификация не предлагает внедрение внутри этой задачи.
2. Все изменения bounded and reversible.
3. No new agents/engine/scoring/dashboard/modes.
4. Compact path preserves review-gate and governance.
5. Finalization and publication/delivery approval are separate.
6. Target files are specific enough for next implementation step.
