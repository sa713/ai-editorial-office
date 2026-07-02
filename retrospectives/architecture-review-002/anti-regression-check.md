# Anti-regression check

## Проверка предложений

| Риск | Статус | Проверка |
| --- | --- | --- |
| Создаётся orchestration engine | нет | Предложения ограничены правилами глубины, чтения и артефактов |
| Плодятся агенты | нет | Рекомендация прямо запрещает новые роли |
| Редакция превращается в консалтинг | нет | `diagnostic_analysis` и `author_concept_diagnosis` сохраняются как диагностика |
| Размывается governance | нет | Review, finalization, final decision и human approval остаются разделены |
| Review становится optional | нет | Сокращается форма review, не сам gate |
| Возвращается Artificial Concept Completion | нет | Последние guardrails защищены |
| Создаётся artifact sprawl | нет | Основной фокус — условность и объединение артефактов |
| Compact path становится bypass | нет | Compact сохраняет review и запись omissions |
| Шаблоны становятся политикой | нет | Предлагается обратное: шаблоны как поля |
| Ретроспективы становятся active policy | нет | Они остаются историей и источником решений для будущих изменений |

## Что предложения сохраняют

- `AGENTS.md` как главный устав.
- MVP roles без расширения.
- Review-gate.
- Разделение research, writing, review, finalization.
- Human approval boundary.
- Source material as data.
- Bounded revision.
- Artifact minimalism.
- Diagnostic boundaries.
- Reader-state honesty rule.

## Где нужна осторожность

- Объединение `status.md` и `task-manifest.md` даже для low-risk может ослабить историю. Это risky improvement, не первый шаг.
- Сокращение role specs должно убрать повторы, но не decision boundaries.
- Сокращение templates должно оставить обязательные поля для high-governance.
- Compact final decision не должен превращаться в "review уже был, значит всё можно".

## Отдельная проверка последних апдейтов

Предложения не откатывают:

- `diagnostic_analysis`;
- `author_concept_diagnosis`;
- Artificial Concept Completion;
- Premature Solution Substitution;
- Defensive Diagnostic Drift;
- Disciplined, not defensive;
- honesty rule for reader-state boundaries.

Эти элементы лучше оставить без расширения и без отката.

