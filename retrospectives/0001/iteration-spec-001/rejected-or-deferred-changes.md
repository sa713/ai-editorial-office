# Rejected or deferred changes

## Новые агенты

- Почему не делаем: больше handoff, coordination overhead и drift; текущие роли уже покрывают research, writing, review, finalization и governance.
- Когда вернуться: если один и тот же тип failure повторится в нескольких задачах и не исправится check/example/rule внутри существующей роли.

## Workflow engine

- Почему не делаем: проблема сейчас в семантике и artifact depth, а не в рантайме.
- Когда вернуться: если появится устойчивый поток задач, где ручной status/orchestration реально ломает delivery.

## Automation platform

- Почему не делаем: автоматизация до стабилизации compact path закрепит текущую сложность.
- Когда вернуться: после нескольких успешных compact/normal/full задач и понятного списка повторяемых операций.

## Scoring/eval system

- Почему не делаем: numeric score может заменить редакционное суждение fake metrics.
- Когда вернуться: если появится набор repeatable regression cases и конкретный вопрос, который нельзя решать review checklist.

## Dashboards

- Почему не делаем: dashboard не исправит unclear ownership, stale manifest или review ambiguity.
- Когда вернуться: если появится много параллельных задач и человеку станет трудно видеть состояние по manifest/status.

## Новые editorial modes

- Почему не делаем: текущая проблема не в нехватке modes, а в применении существующей логики usefulness/mode fit.
- Когда вернуться: если repeated real failures не укладываются в существующие modes и не решаются examples.

## Большие doctrine docs

- Почему не делаем: doctrine inflation уже назван архитектурным риском.
- Когда вернуться: если новый документ заменит несколько дублирующихся правил и будет короче суммарного повторения.

## Массовая миграция старых tasks

- Почему не делаем: legacy folders являются historical data; миграция даст churn без немедленной пользы.
- Когда вернуться: если конкретная старая задача нужна как active template или regression case.

## Переписывание всех pipelines

- Почему не делаем: итерация должна быть bounded; wholesale rewrite увеличит риск drift.
- Когда вернуться: после compact path trial и drift scan, если pipeline conflict реально мешает новым задачам.

## Сокращение всех agent specs

- Почему не делаем: agent specs несут role behavior; массовое сокращение может случайно убрать запреты.
- Когда вернуться: если ownership map покажет точные повторяющиеся блоки, которые можно заменить ссылкой.

## Full event store / run ledger

- Почему не делаем: сейчас достаточно manifest/status/freshness textual evidence.
- Когда вернуться: если review independence или restartability repeatedly fail из-за отсутствия run evidence.

## Автоматические validators

- Почему не делаем: сначала нужны устойчивые правила и несколько новых задач по ним.
- Когда вернуться: если validation checklist станет стабильным и ручная проверка будет часто пропускать ошибки.

## Enterprise approval matrix

- Почему не делаем: single-user редакции нужен явный human approval state, а не многоуровневый sign-off.
- Когда вернуться: если появятся разные human owners с разными полномочиями и реальными side effects.
