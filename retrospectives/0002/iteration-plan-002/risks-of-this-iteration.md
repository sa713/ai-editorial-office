# Risks of this iteration

## Risk 1: Scope creep into persuasion

**Description**

Reader-state awareness может быть ошибочно понята как permission строить persuasion system.

**How it could happen**

- появляются engagement goals;
- тексты начинают оцениваться по "вовлечению";
- review спрашивает, достаточно ли текст мотивирует;
- soft entry превращается в adoption strategy.

**Mitigation**

Закрепить boundary: цель — reduction of unnecessary friction, not persuasion. Не вводить metrics, scoring или activation language.

## Risk 2: Fake softness hides real rules

**Description**

Стремление снизить давление может сделать обязательные правила расплывчатыми.

**How it could happen**

- mandatory action подаётся как optional;
- ограничения убираются из первых экранов;
- governance blockers звучат как рекомендации;
- publication approval становится неявным.

**Mitigation**

Использовать honesty rule: mandatory stays mandatory. Low-pressure entry применим только к реальным optional или reversible actions.

## Risk 3: New terminology causes drift

**Description**

Reader-state, low-pressure entry, workspace framing и passive participation могут начать жить как разные doctrine layers.

**How it could happen**

- каждый документ определяет термины заново;
- templates добавляют разные поля;
- review agents интерпретируют слой шире, чем нужно.

**Mitigation**

Определить термины один раз в canonical editorial knowledge. В остальных местах использовать короткие ссылки или prompts.

## Risk 4: Review becomes subjective tone policing

**Description**

Reviewer может начать спорить о "чувствах" текста вместо конкретных reader-action failures.

**How it could happen**

- замечания формулируются как "мало тепла";
- нет привязки к first step;
- review требует больше дружелюбия без цели;
- corporate hospitality заменяет operational clarity.

**Mitigation**

Review issue должен указывать: observed friction, effect on reader action, minimal repair.

## Risk 5: Workspace framing becomes unsupported claim

**Description**

Желание показать "живое пространство" может привести к выдуманным признакам активности.

**How it could happen**

- текст говорит, что коллеги уже там работают;
- появляются намёки на популярность;
- пространство описывается как активное без данных;
- examples звучат как текущие факты.

**Mitigation**

Разрешать только factual или hypothetical framing. TASK-0009 v2 — пример: "можно посмотреть `To Do`", а не "там уже много задач".

## Risk 6: Over-application

**Description**

Reader-state block может начать применяться к любому тексту.

**How it could happen**

- templates делают блок обязательным;
- agents добавляют behavioral notes в summaries;
- простые factual tasks получают лишние checks.

**Mitigation**

Применять только к задачам с reader action, onboarding, participation или change communication.

## Risk 7: Bounded refinement under-fixes structural problems

**Description**

Default на точечную правку может скрыть случаи, где структура канала действительно сломана.

**How it could happen**

- письмо продолжает выполнять роль инструкции;
- пост копирует email;
- portal page остаётся регламентом;
- low-pressure sentence добавляется поверх тяжёлой структуры.

**Mitigation**

Bounded by default, not bounded always. Escalate when channel role or reader outcome fails structurally.

## Overall risk rating

Medium-low.

Итерация безопасна, если останется маленьким редакционным уточнением. Главный риск — переименовать persuasion в reader-state и незаметно расширить систему.
