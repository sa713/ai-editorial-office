# Editorial core review

## Общая оценка

Редакционное ядро — самая сильная часть системы. Оно не пытается быть универсальным writing assistant. Оно решает конкретную проблему: AI-текст часто выглядит связным, но не помогает читателю действовать, решать, доверять, диагностировать или применять.

Ядро построено вокруг:

- editorial intent;
- usefulness logic;
- compact editorial brief;
- editorial modes;
- review by reader outcome;
- bounded revision;
- governance separation;
- failure patterns.

Это хорошая архитектура именно для рабочей редакции.

## Editorial intent

### Что хорошо

Система требует начинать не с формата, а с reader task и useful outcome.

Это защищает от:

- "напиши статью о X";
- generic announcements;
- topic taxonomy outlines;
- broad context openings;
- inherited purpose as hook.

### Риск

Intent inference может стать слишком уверенным. Если audience, stakes или reader state неясны, система может молча выбрать mode и structure.

### Рекомендация

Сохранить inference-first philosophy, но добавить правило:

```text
If inferred intent materially changes structure or risk, mark confidence and assumption.
```

Не превращать это в форму.

## Usefulness logic

### Что хорошо

Usefulness раскрыта не только как "next action". Есть:

- operational usefulness;
- cognitive usefulness;
- emotional usefulness;
- trust usefulness;
- social usefulness.

Это зрелое решение. Оно защищает систему от чрезмерно сухого "action-only" подхода и одновременно не разрешает декоративную теплоту.

### Риск

Чем больше usefulness dimensions, тем выше риск, что writer начнет оправдывать лишний текст "эмоциональной" или "социальной" полезностью.

### Рекомендация

В review спрашивать:

```text
Does this usefulness dimension change readiness, trust, acceptance, understanding or action?
```

Если нет — это decoration.

## Review system

### Что хорошо

Review hierarchy правильная:

1. usefulness;
2. reader outcome;
3. mode fit;
4. structure;
5. evidence/reasoning;
6. execution clarity;
7. context discipline;
8. language clarity;
9. polish.

Это защищает review от taste-based rewriting.

### Риск

Review Agent одновременно отвечает за:

- factual traceability;
- artifact completeness;
- governance compliance;
- editorial usefulness;
- structural quality;
- mode-specific behavior;
- anti-pattern detection.

Для сложных задач это хорошо. Для простых — может быть тяжело.

### Рекомендация

Ввести review depth:

- compact review: verdict + top blockers + usefulness check;
- normal review: current standard;
- full review: high-governance.

Review-gate остается обязательным, но форма review меняется.

## Bounded revision

### Что хорошо

Система явно понимает риск endless revision loops. Review should request changes only when text fails an editorial job.

Есть сильные правила:

- do not rewrite for taste;
- do not demand context for completeness;
- do not replace working structure with prettier structure;
- lower-priority polish should not block acceptance.

### Риск

Bounded revision пока лучше описан как review philosophy, чем как operational loop. Не всегда ясно:

- сколько итераций допустимо;
- когда changes_requested возвращается к writer vs research;
- когда escalates to chief_editor;
- когда признать scope problem.

### Рекомендация

Добавить compact bounded revision protocol:

```text
1. Name blocking editorial job.
2. Assign repair owner.
3. Limit repair scope.
4. Re-review only changed risk areas plus original blockers.
5. Escalate after repeated failure.
```

## Governance separation

### Что хорошо

Система четко разделяет:

- review approval;
- finalization;
- final governance decision;
- human publication/delivery approval.

Это особенно важно для внутренних коммуникаций и stakeholder-sensitive материалов.

TASK-0006 и TASK-0008 демонстрируют это хорошо: editorial finalization не означает, что текст можно отправлять людям без owner decision.

### Риск

Слово `finalized` может быть прочитано пользователем как "можно отправлять". В manifests это компенсируется полем publication/delivery approval, но не всегда одинаково.

### Рекомендация

Для задач с реальной отправкой всегда использовать явную строку:

```text
Editorial finalized: yes/no
Human send/publication approval: required/granted/not required
```

## Editorial modes

### Что хорошо

Modes описывают interaction behavior, а не форматы. Это зрелое решение.

Они помогают:

- выбирать opening behavior;
- ограничивать narrative density;
- строить review criteria;
- избегать topic taxonomy;
- удерживать dominant mode над supporting mode.

### Риск

Mode list уже близок к верхней границе полезности. Новые micro-modes могут создать classification overhead.

### Рекомендация

Не добавлять новые modes без повторяющегося провала, который нельзя объяснить существующими modes.

Лучше добавлять examples:

```text
brief -> mode -> structure -> review finding
```

## Failure patterns

### Что хорошо

Failure patterns очень практичны. Они называют реальные редакционные провалы:

- fake excitement;
- institutional opening;
- answer delay;
- decorative warmth;
- forced inspiration;
- mode blending;
- emotional avoidance;
- trust without evidence;
- generic engagement language;
- inherited purpose as hook.

Каждый pattern содержит repair move и do-not-over-correct. Это ценно: система не просто запрещает плохое, она показывает минимальное исправление.

### Риск

Если failure patterns превратить в checklist, review станет тяжелым и начнет находить проблемы там, где их нет.

### Рекомендация

Оставить правило из файла: use when text feels wrong but problem is hard to name. Не делать каждый pattern обязательной проверкой.

## Failure patterns системы, а не текста

Для самой AI-редакции вероятны такие системные провалы:

- **Polished process, weak output**: artifacts корректны, но текст не лучше.
- **Review bureaucracy**: review проверяет compliance, но теряет reader outcome.
- **Mode formalism**: mode выбран, но не влияет на структуру.
- **Artifact inertia**: прошлые task folders становятся шаблоном для новых задач.
- **Finalization ambiguity**: finalized путают с approved to send.
- **Context allergy**: система удаляет необходимое объяснение, потому что боится essay-mode.

## Итог

Редакционное ядро не нужно переписывать. Его нужно проверять на реальных задачах, защищать от разрастания и подкреплять примерами. Самое ценное в ядре — не список правил, а связка "reader task -> useful outcome -> mode -> structure -> review".
