# Pipeline implications

## Principle

Iteration 002 не создаёт новый pipeline. Изменения встраиваются как малые проверки в существующие стадии: intake, orchestration, writing, review, refinement и finalization.

## Intake

Для задач, где читателю нужно начать пользоваться, участвовать или перейти в новое рабочее пространство, intake должен фиксировать:

```text
Reader action required:
First-step risk:
Observation-before-commitment possible:
Mandatory elements:
Channels affected:
```

Не добавлять этот блок в задачи, где reader action отсутствует.

## Orchestration

Chief Editor или orchestration artifact должен решить:

- нужен ли reader-state check;
- где риск pressure или process framing;
- какие каналы требуют low-pressure entry;
- какие правила и ограничения нельзя смягчать;
- какой artifact будет review target.

Это решение должно быть коротким. Не нужен отдельный behavioral plan.

## Writing

Writer должен применять reader-state guidance только в пределах editorial intent:

- показать честный первый шаг;
- не требовать early commitment без причины;
- разрешить просмотр, если он доступен;
- использовать конкретные рабочие ситуации;
- не добавлять social proof, urgency или обещания без источников;
- не превращать инструкцию в промо-текст.

## Review

Reviewer добавляет reader-state block только когда он релевантен:

```text
First step clear:
Low-pressure entry preserved:
No fake obligation:
No fake momentum:
Mandatory rules still clear:
Verdict:
```

Review должен оставаться independent. Writer не должен сам закрывать этот чек как замену review.

## Refinement

Если проблема reader-state обнаружена, default repair должен быть bounded:

- поменять вход;
- добавить safe first step;
- убрать pressure language;
- перенести детали в более подходящий канал;
- уточнить обязательность.

Full rewrite нужен только если reader outcome сломан структурно.

## Finalization

Final decision или handoff для таких задач должен кратко фиксировать:

- reader-state issue resolved or not applicable;
- publication blockers;
- human approval still required, if applicable;
- no new unverified claims added.

## What not to change

Не менять:

- core stage sequence;
- review-gate;
- role separation;
- source traceability;
- governance state;
- approval semantics;
- compact/normal/full execution profile from iteration 001.

## Implementation depth

Рекомендуемая глубина внедрения:

1. Документировать guidance в editorial knowledge или ближайшем canonical месте.
2. Добавить короткие optional prompts в orchestration/review templates, если template already owns such fields.
3. Протестировать на 2-3 новых задачах с onboarding/change communication.
4. Только после повторных успешных применений решать, нужны ли более широкие template updates.

Не начинать с массового редактирования всех пайплайнов.
