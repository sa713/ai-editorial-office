# Orchestration review

## Общая оценка

Orchestration в системе зрелая, но находится на границе между полезной координацией и возможной процессной тяжестью.

Сильная сторона: роли соответствуют реальным редакционным функциям.

Главный риск: система может начать считать каждый role boundary отдельным "агентским" событием, даже когда задача мала и достаточно compact path.

## Orchestration

### Что хорошо

Chief Editor выполняет нужные функции:

- выбирает pipeline;
- подтверждает risk mode;
- назначает роли;
- ведет status/manifest/orchestration_plan;
- защищает review-gate;
- принимает final governance decision.

Это соответствует harness-подходу: модельные роли не должны сами решать, что система готова; нужен coordinator/governance boundary.

### Риск

Chief Editor может стать bottleneck для слишком многих мелких решений:

- каждый artifact;
- каждый handoff;
- каждый status transition;
- каждый no-research rationale.

### Рекомендация

Chief Editor должен активно использовать risk mode:

- для high-governance — полный orchestration;
- для standard — normal orchestration;
- для low-risk — compact orchestration with minimal artifacts.

## Роль агентов

### Что хорошо

Роли не являются абстрактными "специалистами ради агентности". Они отражают редакционную цепочку:

- intake нормализует задачу;
- research собирает evidence;
- writer пишет;
- UX writer пишет product-facing copy;
- review проверяет независимо;
- final editor делает controlled finalization;
- chief editor отвечает за governance.

### Риск

Некоторые agent specs очень длинные и повторяют pipeline/governance logic. Это повышает вероятность того, что роль будет думать о процессе больше, чем о своей редакционной работе.

### Рекомендация

Сократить role specs до:

- mission;
- responsibilities;
- forbidden actions;
- required inputs/outputs;
- decision boundaries;
- escalation rules.

Последовательность и status transitions держать в pipelines/status model.

## Границы ответственности

### Сильные границы

- Writer не проверяет сам себя.
- Review не пишет финальный текст.
- Final Editor не выдает publication approval.
- Chief Editor не заменяет production roles.
- Human approval остается отдельным от finalized.

Это сильная governance architecture.

### Слабые места

Custom workflows используют "role behavior" вместо явного role ownership. Например TASK-0008:

```text
diagnosis | writer_agent behavior
review | review_agent behavior
final decision | chief_editor behavior
```

Это практично, но может размывать границы: writer_agent behavior начинает означать не только writing, но и diagnosis/strategy/prototypes.

### Рекомендация

Для custom workflows фиксировать:

- production owner role;
- why this role behavior fits;
- what this role must not do;
- review target.

## Pipeline complexity

### Что хорошо

Pipelines выполняют роль execution contracts. Они задают:

- когда применять;
- когда не применять;
- роли;
- artifacts;
- allowed stages;
- status transitions;
- risk mode behavior.

Это полезно для restartability и consistency.

### Риск

Pipeline files очень подробные. Article/social/UX/review pipelines могут дублировать большую часть lifecycle logic.

### Последствия

- изменения lifecycle требуют правки многих файлов;
- агенты могут читать много текста для очевидного действия;
- low-risk задачи получают standard/high-governance overhead.

### Рекомендация

Вынести common lifecycle в один canonical layer. Pipeline-specific files должны описывать только отличия:

- when to use;
- artifact differences;
- review focus;
- role-specific outputs.

## Unnecessary agentization

### Что система делает правильно

Она явно не добавляет:

- separate Editor Agent;
- future fact checker;
- future style editor;
- terminology reviewer;
- structural editor.

Это сильное решение. Best-practices прямо предупреждает: не добавлять subagents до измеренных провалов single/minimal workflow.

### Где риск остается

Сама терминология "agents" может провоцировать будущие расширения:

- каждый review pattern станет агентом;
- каждый editorial mode станет агентом;
- каждый artifact получит owner-agent;
- каждый тип текста получит отдельный pipeline.

### Рекомендация

Новые агенты добавлять только если есть repeated failure, который нельзя решить:

- правилом;
- artifact boundary;
- review check;
- example;
- compact pipeline variant.

## Coordination overhead

### Где overhead полезен

- high-governance communications;
- factual claims;
- external publication;
- stakeholder-sensitive texts;
- source-heavy research;
- tasks with human approval.

### Где overhead вреден

- простое улучшение текста;
- небольшая внутренняя коммуникация без claims;
- single-output review;
- low-risk rewrite with provided source;
- exploratory draft that user expects quickly.

### Рекомендация

Добавить orchestration decision:

```text
Process depth: compact | normal | full
Reason:
Artifacts intentionally omitted:
Review still required:
```

## Hidden coupling

### Виды coupling

1. **AGENTS.md -> all pipelines**
   Все pipeline contracts зависят от устава.

2. **project-state.md -> current normalization decisions**
   Это полезно сейчас, но может стать вторым уставом.

3. **agent specs -> pipeline sequencing**
   Роли содержат часть sequence logic.

4. **templates -> governance assumptions**
   Templates уже несут процессные правила, не только поля.

5. **editorial_knowledge -> review_agent behavior**
   Review Agent использует редакционную теорию, но связь не всегда явно указана в orchestration.

### Риски

- изменение одного правила требует каскадной синхронизации;
- старые task artifacts становятся обучающими примерами устаревшего behavior;
- custom flow обходит canonical pipeline logic.

### Рекомендация

Сделать source-of-truth map:

| Concern | Canonical owner |
| --- | --- |
| system invariants | `AGENTS.md` |
| statuses | `kb/task_statuses.md` |
| role behavior | `agents/*.md` |
| sequence | `pipelines/*.md` |
| artifact fields | `templates/artifacts/*.md` |
| editorial quality | `editorial_knowledge/*` |
| current normalization | `project-state.md` |

## Итог

Orchestration не надо радикально менять. Нужно уменьшить duplication, закрепить compact path и защитить custom workflows от превращения в скрытые, непроверяемые пайплайны.
