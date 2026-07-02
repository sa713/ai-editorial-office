# Индекс editorial_knowledge

`editorial_knowledge/` хранит знания о качестве редакционной работы:
полезность, режимы взаимодействия читателя с текстом, компактный бриф, review и
типовые провалы.

`ai-editorial-office/AGENTS.md` остаётся главным источником архитектурных
правил, иерархии управления, ролей, пайплайнов, governance и review-gate. Этот
индекс не создаёт новых правил и не заменяет `AGENTS.md`.

## Как читать эту папку

Читайте только файлы, которые нужны для текущего решения: например modes для
выбора поведения текста, failure patterns для диагностики review или cases для
примеров.

Не загружайте всю папку по умолчанию. Не используйте placeholder/reserved-файлы
как активное руководство.

## Категории файлов

| Файл или группа | Категория | Как использовать |
| --- | --- | --- |
| `00_sources.md` | source list | Список источников редакционных идей; не является оперативным регламентом |
| `01_principles.md` | active doctrine | Редакционные принципы полезности и честной работы с сырой идеей |
| `02_editorial_intent.md` | placeholder/reserved | Каркас без активных правил или руководства |
| `03_usefulness_review.md` | placeholder/reserved | Каркас без активных правил или руководства |
| `10_operational_rules.md` | active doctrine | Практические редакционные правила качества текста и структуры |
| `20_editorial_modes.md` | active doctrine | Режимы взаимодействия читателя с текстом; визуальные разделы внутри файла заморожены |
| `30_compact_editorial_brief.md` | operational support | Рабочая поддержка для компактного брифа и перехода от intake к writing/review |
| `31_usefulness_dimensions.md` | operational support | Дополнительные измерения полезности для диагностики и уточнения reader outcome |
| `40_editorial_review_system.md` | active doctrine | Доктрина редакционного review; визуальные review-pass внутри файла заморожены |
| `50_editorial_failure_patterns.md` | operational support | Диагностические паттерны провалов; визуальный sketchnote-паттерн заморожен |
| `90_system_review.md` | system review | Разбор состояния системы, сильных мест, рисков роста и слабых зон |
| `cases/CASE-001_people_uek_announcement.md` | case/example | Реальный пример применения редакционной логики |
| `cases/CASE-PATTERNS-001.md` | case/example | Выводы и паттерны из кейсов |
| `cases/CASE_TEMPLATE.md` | placeholder/reserved | Заготовка для будущих кейсов; не активное правило |

## Замороженные visual-related знания

Визуальные знания сохранены только как frozen visual-related knowledge:

- визуальные режимы в `20_editorial_modes.md`;
- visual review checks в `40_editorial_review_system.md`;
- sketchnote failure pattern в `50_editorial_failure_patterns.md`.

Эти материалы не активируют визуальную подсистему. Визуальная ветка остаётся
inactive/frozen и может использоваться только если `AGENTS.md` и явная
пользовательская просьба разрешают её запуск.
