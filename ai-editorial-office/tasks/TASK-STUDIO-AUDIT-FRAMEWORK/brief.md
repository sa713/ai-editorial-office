# Brief

## Task

Разработать Studio Audit Framework для AI Software Studio: каноническую
методику независимого повторяемого аудита зрелости Студии.

## Deliverable

Пакет markdown-документов Studio Audit Framework, включающий:

1. Executive Summary.
2. Архитектуру Framework.
3. Перечень областей аудита.
4. Критерии оценки.
5. Модель зрелости.
6. Правила сбора доказательств.
7. Правила формирования Audit Report.
8. Связь Framework с Knowledge Base.
9. Выявленные пробелы Knowledge Base.
10. Рекомендации по проведению первого аудита AI Software Studio.

Структура может быть расширена, если это повышает пригодность Framework для
повторного использования.

## Source Boundary

Primary source of truth:

- `/ai-editorial-office/kb/ai-software-studio-knowledge-base/`

Every audit criterion, requirement, rationale, and recommendation must be tied
to explicit Knowledge Base entries. If the Knowledge Base is insufficient for a
criterion or section, the gap must be named instead of inventing a rule.

## Audience

Владелец и будущие независимые аудиторы AI Software Studio.

## Constraints

- Do not conduct an audit of AI Software Studio.
- Do not evaluate the current implementation of the Studio.
- Do not formulate a BRD.
- Do not propose process changes for the Studio.
- Do not write Codex tasks.
- Do not use direct `PDF -> SVG/PNG/MD` conversion path.
- Keep the output as an audit methodology, not an audit result.

## Acceptance Criteria

- Framework is fully grounded in the existing Knowledge Base.
- All criteria include rationale and Knowledge Base linkage.
- A maturity model is defined for criteria, areas, and the whole Studio.
- Evaluation rules and evidence collection rules are defined.
- Future Audit Report structure is defined without being filled.
- Knowledge Base gaps are identified.
- Framework is reusable for repeated audits.
- Framework contains no results of an actual Studio audit.
