# Brief

## task title

Разобрать `Roadmap.md` по `Vibe Coding Community` на пакет markdown-артефактов для руководства сообщества.

## user goal

Подготовить из исходного чернового roadmap набор самостоятельных markdown-документов, которые можно отправить инициаторам и менеджерам сообщества как пакет идей для обсуждения и последующей реализации.

## audience

- инициаторы сообщества;
- менеджеры сообщества;
- люди с компетенциями разработчиков.

## deliverable

Основные markdown-файлы в `ai-editorial-office/tasks/VIBE-CODING-COMMUNITY`:

- `leadership_ideas_pack.md`;
- `community_entities_map.md`;
- `portal_content_ideas.md`.

Task artifacts:

- `brief.md`;
- `task-manifest.md`;
- `status.md`;
- `orchestration_plan.md`;
- `review.md`;
- `final_decision.md`, если review approved и финальное решение уместно.

## channel or publication context

Материалы будут использоваться как письмо или вложение к письму руководству `Vibe Coding Community`. Это не презентация, не слайды и не структура выступления.

## scope

Нужно сохранить смысловую рамку: `Vibe Coding Community` — практическая мастерская, а не база ссылок или статичный портал.

Основная операционная петля:

1. Участник приносит вопрос, кейс, workflow или рабочую проблему.
2. Сообщество разбирает это в коротком формате.
3. Результат превращается в маленький артефакт.
4. Артефакт попадает на страницу сообщества.
5. Другие участники используют артефакт и возвращаются с новыми вопросами, уточнениями или кейсами.

## constraints

- Работать только внутри `ai-editorial-office/tasks/VIBE-CODING-COMMUNITY`.
- Не менять `AGENTS.md`, системные правила ИИ-редакции, роли, review-gate, пайплайны и production-файлы.
- Не создавать презентацию, `.pptx`, структуру слайдов или speaker notes.
- Не делать roadmap реализации.
- Не оценивать ресурсы, сроки, загрузку людей или бюджет.
- Не добавлять KPI и метрики.
- Не создавать отдельный документ «что НЕ делать».
- Не превращать идеи в техническое ТЗ.
- Не проектировать UI и не писать UX-тексты интерфейса.
- Не русифицировать ключевые термины, перечисленные пользователем.

## source materials

- `Roadmap.md` в папке задачи.
- Подробный пользовательский бриф из текущего запроса.

## factual sensitivity

Низкая. Внешняя проверка фактов не требуется: задача состоит в редакционной структуризации исходного файла и пользовательских требований.

## risk mode

Low-risk with mandatory review.

## success criteria

- Работа выполнена внутри `ai-editorial-office/tasks/VIBE-CODING-COMMUNITY`.
- Созданы или обновлены `leadership_ideas_pack.md`, `community_entities_map.md`, `portal_content_ideas.md`.
- Документы написаны на русском языке и пригодны для отправки руководству сообщества.
- Сохранён широкий охват идей из `Roadmap.md`.
- Нет презентационного формата, roadmap реализации, оценки ресурсов, KPI, технического ТЗ, UI-макетов и UX-текстов интерфейса.
- Термины `Vibe Coding Community`, `vibe clinic`, `vibecode challenge`, `workflow demo`, `office hours`, `mini-jams`, `prompt review sessions`, `live debugging sessions`, `workflow library`, `prompt templates`, `troubleshooting notes`, `anti-pattern card`, `digest`, `FAQ`, `onboarding path` сохранены.
- Есть `review.md` с независимой проверкой.
- Если создан `final_decision.md`, он фиксирует, что финальный deliverable — набор подготовленных markdown-файлов.
- `git status --short` показывает только ожидаемые изменения внутри task folder.

## open questions

- None blocking. Вопросы для обсуждения с руководством должны быть включены в основные документы как мягкие discussion prompts, а не как blockers.
