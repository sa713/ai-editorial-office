# Iteration goals

## Назначение итерации

Iteration 002 развивает редакционное ядро после TASK-0009 в одном узком направлении: научить систему проверять не только понятность и полезность текста, но и практическую доступность первого шага для читателя.

Это не новая теория влияния на людей. Это bounded improvement iteration про снижение лишнего входного трения в рабочих коммуникациях.

## Основание

TASK-0009 показал повторяемый редакционный риск: текст может быть точным, согласованным и полезным, но всё равно восприниматься как новый обязательный процесс. V2-материалы стали сильнее именно тогда, когда:

- Биржа стала описываться как рабочее место, куда можно зайти посмотреть;
- первый шаг был снижен до просмотра `To Do`;
- участие перестало звучать как немедленное обязательство;
- язык стал ближе к рабочим ситуациям без рекламного тона;
- не появились неподтверждённые обещания, социальное давление или fake momentum.

## Главные цели

1. **Добавить reader-state awareness как малый редакционный слой.**
   Система должна уметь замечать perceived pressure, страх неправильного входа и отсутствие безопасного первого шага.

2. **Закрепить low-pressure entry для подходящих задач.**
   Если коммуникация допускает наблюдение, чтение или пробный вход без немедленного обязательства, это должно быть видно в тексте.

3. **Уточнить review heuristics.**
   Review должен проверять accidental pressure, fake obligation, слишком ранний commitment и процессный framing там, где они могут навредить reader outcome.

4. **Сформулировать failure patterns по TASK-0009.**
   Нужны практичные anti-patterns, которые помогают чинить тексты: mandatory-process framing, pressure-first onboarding, fake adoption momentum, overexplaining before entry.

5. **Ограничить влияние на pipeline.**
   Изменения должны войти как дополнительные вопросы intake/orchestration/writing/review, а не как новый pipeline, новый агент или новая taxonomy.

6. **Сохранить operational honesty.**
   Мягкий вход не должен скрывать обязательность, риски, ограничения, правила или governance.

## Anti-goals

В рамках этой итерации не делать:

- новые агенты или роли;
- behavioral UX agent;
- onboarding strategist;
- persuasion framework;
- emotional scoring;
- personality targeting;
- engagement metrics;
- conversion funnel;
- adoption optimization;
- новую большую taxonomy editorial intents;
- rewrite всех pipelines;
- rewrite agent specs без необходимости;
- автоматические validators или dashboards;
- искусственное расширение системы ради концептуальной полноты.

## Constraints

- Reader-state awareness применяется только там, где reader action, entry, onboarding или participation реально важны.
- Review-gate не меняется и не расширяется в отдельную behavioral approval stage.
- Human approval, factual accuracy и source traceability не ослабляются.
- Если действие действительно обязательно, текст должен говорить об этом честно.
- Нельзя заменять ясные правила "дружелюбной" неопределённостью.
- Нельзя выдумывать признаки использования, популярность, активность коллег или urgency.
- Любой новый чек должен помогать исправлять текст, а не просто добавлять ритуал.

## Success criteria

Итерация успешна, если после неё:

- intake может зафиксировать, нужен ли safe first step;
- orchestration может решить, применять ли low-pressure reader-state checks;
- writer получает короткие практичные правила для мягкого входа без promotional tone;
- review умеет находить accidental pressure и too-early commitment;
- failure patterns помогают чинить текст точечно;
- pipeline не разрастается;
- ядро остаётся редакционным, а не persuasion/growth-системой.

## Non-success signals

Итерация считается неудачной, если:

- появляется отдельный behavioral layer как новая система управления читателем;
- тексты начинают оптимизироваться под вовлечение вместо usefulness;
- review превращается в оценку эмоций;
- мягкость начинает скрывать обязательные правила;
- появляются новые агенты или псевдо-роли;
- каждый текст принудительно проходит behavioral analysis;
- docs становятся длиннее, но writing/review не улучшаются.
