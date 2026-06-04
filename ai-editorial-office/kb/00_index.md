# KB index

`/kb` stores reusable editorial standards and reference material. It does not own workflow lifecycle, role boundaries, or artifact responsibility rules unless a specific KB file is named as canonical owner in `AGENTS.md`.

Canonical KB ownership:

- `task_statuses.md` owns allowed operational task statuses and transitions.
- `feedback_patterns.md` owns recurring or significant feedback pattern tracking; it does not store every task-local feedback item.
- `compact_execution.md` gives practical guidance for compact execution and
  artifact minimalism. It does not override `AGENTS.md`, selected pipelines, or
  task-local governance artifacts.
- `clients/CLIENT-ID/` owns task-scoped client profiles. Client profiles are
  loaded only when `task-manifest.md` or `orchestration_plan.md` explicitly
  activates them.
- Other KB files own reusable standards, examples, tone, glossary, and forbidden patterns for editorial work.

Current client profiles:

- `clients/sber/` — Sber client profile. It is not global editorial policy and
  must not activate for independent materials where Sber is only mentioned as a
  topic, example, source, or competitor.

If a KB rule conflicts with `AGENTS.md`, pipelines, or task-local governance, follow the authority hierarchy in `AGENTS.md` and stop if the conflict affects production.
