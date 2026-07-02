# Review heuristics plan

## Purpose

Review heuristics iteration 002 должны помочь reviewer замечать практические сбои входа в действие. Они не заменяют стандартный review на точность, полезность, структуру, канал и governance.

## Additive review block

Для задач с onboarding/participation/change communication добавить короткий блок:

```text
Reader first step:
Pressure risk:
Observation-before-commitment available:
Mandatory elements preserved:
Behavioral friction verdict:
```

Этот блок не обязателен для всех задач. Orchestration или reviewer применяет его, когда есть reader action и риск unnecessary pressure.

## Heuristic 1: Entry friction review

**Question**

Насколько трудно, страшно или "официально" выглядит первый шаг?

**Look for**

- длинный процесс до пользы;
- слишком много правил перед первым действием;
- первый шаг звучит как обязательство;
- непонятно, можно ли просто посмотреть;
- читатель должен сразу "вступить", "подключиться", "начать пользоваться".

**Repair direction**

Снизить первый шаг до честного минимального действия: открыть, посмотреть, прочитать, выбрать сценарий, вернуться позже.

## Heuristic 2: Passive-entry availability

**Question**

Можно ли начать с наблюдения без немедленного участия?

**Look for**

- бинарность "участвуешь / не участвуешь";
- отсутствие safe preview;
- действие предлагается до понимания value;
- просмотр или чтение не названы как допустимые.

**Repair direction**

Явно назвать безопасный режим входа, если он реально доступен.

## Heuristic 3: Living-space test

**Question**

Текст описывает рабочее место или корпоративное внедрение?

**Look for**

- "запускается процесс";
- "необходимо подключиться";
- "новая инициатива";
- абстрактная польза вместо видимых рабочих объектов;
- нет ответа, что читатель увидит внутри.

**Repair direction**

Показать пространство через конкретные объекты: задачи, раздел, список, карточки, примеры действий, место входа.

## Heuristic 4: Pressure audit

**Question**

Есть ли давление, которое не требуется задачей?

**Look for**

- urgency без основания;
- "все уже";
- guilt или social pressure;
- implied evaluation;
- обещания популярности или momentum без данных;
- эмоциональные призывы вместо рабочего next step.

**Repair direction**

Убрать pressure language. Оставить факт, пользу, первый шаг и реальные ограничения.

## Heuristic 5: Human operational language audit

**Question**

Язык звучит как рабочая коммуникация или как кампания?

**Look for**

- overly polished launch tone;
- HR-like hospitality;
- искусственная бодрость;
- рекламные обещания;
- стерильная корпоративность;
- слишком мягкие фразы, которые прячут правила.

**Repair direction**

Вернуть язык к спокойной рабочей речи: конкретная ситуация, конкретный объект, конкретное действие.

## Review output rule

Если проблема найдена, reviewer должен назвать:

```text
Observed issue:
Why it affects reader action:
Minimal repair:
What must remain unchanged:
```

Это удерживает review в bounded mode и не превращает reader-state issue в полный rewrite.
