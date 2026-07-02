# Optimization opportunities

## Quick wins

| Улучшение | Проблема | Где | Эффект | Риск | Сложность | Приоритет | Что менять | Что не менять |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Сделать `review-summary.md` условным | Дублирует `review.md` | пайплайны, templates, tasks | меньше файлов | низкий | низкая | высокий | правило: создавать только при отдельном потребителе | review-gate |
| Встроить `qa-checklist` в low-risk review | Лишний файл | review outputs | меньше циклов | низкий | низкая | высокий | compact review shape | high-governance checklist |
| Сократить handoff до delta | Старые handoff раздуты | handoff practice | меньше чтения | низкий | низкая | высокий | лимит: changed, blockers, next action | role transfer |
| Не создавать пустой `open-questions.md` | Файл ради файла | task templates | меньше мусора | низкий | низкая | средний | open questions только при вопросах | blocker visibility |
| Добавить current-version pointer | Много v2/v3 файлов | TASK-0009, TASK-0010 pattern | быстрее restart | низкий | низкая | высокий | короткий блок в manifest | версионность |
| Пометить старые задачи как не-шаблон | Старые артефакты тяжёлые | project_tree / guidelines | меньше копирования плохих форм | низкий | низкая | высокий | одно правило чтения истории | task archive |

## Medium improvements

| Улучшение | Проблема | Где | Эффект | Риск | Сложность | Приоритет | Что менять | Что не менять |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Сократить role specs | Роли повторяют устав и пайплайны | `agents/*.md` | меньше контекста | средний | средняя | высокий | оставить role behavior и boundaries | MVP role set |
| Сократить templates до полей | Templates стали доктриной | `templates/**` | меньше повторов | средний | средняя | высокий | убрать policy prose | artifact shapes |
| Общий lifecycle profile | Пайплайны повторяют одно и то же | `pipelines/*.md` | меньше drift | средний | средняя | средний | вынести общее в owner | task-type distinctions |
| Compact final decision | Финальное решение слишком длинное | `final_decision_template.md` | меньше output | средний | средняя | высокий | профиль для low-risk/standard | governance boundary |
| Short context loading profile | Каждый этап читает слишком много | `AGENTS.md`, roles | экономия лимитов | средний | средняя | высокий | read set by risk/depth | conflict checks |
| Diagnosis mini-contract | Нестандартные диагностики каждый раз заново | custom workflows | быстрее TASK-0008/0010-like | средний | средняя | средний | короткий mini-contract | не новый pipeline |

## Risky improvements

| Улучшение | Проблема | Где | Эффект | Риск | Сложность | Приоритет | Что менять | Что не менять |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Объединить `status.md` и `task-manifest.md` для low-risk | Два состояния | task model | меньше файлов | можно потерять историю | средняя | низкий | только после тестов | status model для standard/high |
| Переписать все пайплайны | Повторы | `pipelines` | чистая структура | сломать устойчивость | высокая | низкий | только по шагам | review/research/finalization |
| Удалить пустые KB/scaffold файлы | Шум | KB/editorial_knowledge | меньше retrieval | можно потерять намерение | низкая | низкий | лучше сначала пометить | active knowledge |
| Ввести проверочный скрипт свежести | Много ручных checks | manifests/status | меньше ошибок | риск платформизации | средняя | низкий | только если ручное правило не работает | не делать engine |

## Do not do

| Идея | Почему не делать |
| --- | --- |
| Новый orchestration engine | Система локальная и markdown-first; проблема решается правилами глубины |
| Новые агенты | Пересечения уже есть; новые роли усилят handoff load |
| Отдельный fact_checker | Research + review достаточно для MVP |
| Отдельный style_editor | Вернёт taste-based review |
| Scoring для review | Превратит полезность в формальность |
| Dashboard, eval, metrics | Нет доказанной нужды |
| Новый behavioral framework | Reader-state уже ограничен как малая чувствительность |
| Новый mode на каждый тип текста | Режимов уже достаточно |
| Делать review optional | Ломает устав |
| Откатывать diagnostic/author-facing updates | Вернёт Artificial Concept Completion и solution substitution |

