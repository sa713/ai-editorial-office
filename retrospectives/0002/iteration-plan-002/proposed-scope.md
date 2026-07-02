# Proposed scope

## Scope principle

В scope входят только изменения, которые помогают редакции заметить и убрать лишнее входное трение. Всё, что требует новой роли, новой платформы, скоринга или широкой теории поведения, не входит в iteration 002.

## 1. Reader-state intake questions

**Изменение**

Добавить в intake или orchestration короткий блок вопросов для задач, где есть действие читателя:

```text
Does the reader need to take a first step?
Could the first step feel obligatory or risky?
Is observation before commitment possible?
Should the text explicitly allow a low-pressure entry?
What must remain mandatory or non-negotiable?
```

**Почему именно это**

TASK-0009 улучшился не от новой концепции, а от простого решения: "можно просто зайти посмотреть `To Do`".

**Expected effect**

- меньше pressure-first коммуникаций;
- понятнее первый шаг;
- меньше риска скрыть обязательность;
- reader-state учитывается до writing, а не после.

## 2. Low-pressure entry rule

**Изменение**

Закрепить правило:

```text
If safe observation is available, do not frame the first step as immediate commitment.
```

**Почему именно это**

В TASK-0009 первый вариант уже был точным, но v2 стал сильнее, когда запуск перестал звучать как требование сразу создать карточку или откликнуться.

**Expected effect**

- сотрудник понимает, что можно начать с малого;
- onboarding становится менее тревожным;
- текст не давит там, где действие может быть постепенным.

## 3. Workspace framing guidance

**Изменение**

Добавить короткую guidance для случаев, когда продукт, раздел, доска или процесс лучше воспринимается как рабочее место:

- показывать, куда можно зайти;
- что можно увидеть;
- какой первый безопасный объект посмотреть;
- какой сценарий узнаваем для читателя.

**Почему именно это**

Биржа стала убедительнее, когда была описана как место задач и помощи, а не как очередное внедрение процесса.

**Expected effect**

- меньше "инициатива сверху";
- больше рабочей конкретики;
- меньше необходимости мотивировать читателя искусственной энергией.

## 4. Pressure audit in review

**Изменение**

Добавить в review минимальную проверку:

- есть ли implied obligation;
- есть ли urgency без основания;
- есть ли social pressure;
- требует ли текст commitment до понимания пользы;
- можно ли снизить первый шаг без искажения правил.

**Почему именно это**

Review v2 явно подтвердил: материалы стали лучше, потому что не добавили fake adoption, обещания и давление.

**Expected effect**

- review ловит практические behavioral failures;
- правки остаются bounded;
- качество проверяется без emotional scoring.

## 5. Failure patterns from TASK-0009

**Изменение**

Описать небольшой набор failure patterns:

- mandatory-process framing;
- pressure-first onboarding;
- fake adoption momentum;
- overexplaining before entry;
- corporate hospitality tone;
- forced emotional energy.

**Почему именно это**

Эти паттерны прямо наблюдались или были предотвращены в TASK-0009.

**Expected effect**

- проще объяснять, что именно сломано;
- проще делать bounded refinement;
- меньше риска переписывать всё целиком.

## 6. Bounded refinement default

**Изменение**

Для reader-state проблем default repair должен быть точечным:

```text
Problem:
Pressure/friction source:
Minimal repair:
What must not change:
Re-review target:
```

**Почему именно это**

TASK-0009 v2 был успешен как точечный refinement, а не полный rewrite.

**Expected effect**

- меньше переписывания ради тона;
- сохраняется точность и структура;
- review issues быстрее превращаются в исправления.

## Out of scope

Не входит:

- переписывать ядро;
- редактировать текущие agent specs;
- создавать новых агентов;
- добавлять behavioral scoring;
- расширять все templates;
- строить universal reader psychology model;
- создавать отдельную approval stage;
- оптимизировать тексты под adoption или engagement;
- мигрировать старые задачи.
