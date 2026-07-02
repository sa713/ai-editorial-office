# Implementation plan

Step executed: Step 1 only, Ownership map implementation.

## Changed files

## `ai-editorial-office/AGENTS.md`

- Why: `AGENTS.md` is the canonical owner for system invariants and rule-placement boundaries.
- What changed: added a short `Canonical ownership map` section with owners for system rules, state, statuses, pipelines, agents, templates, editorial knowledge, and task-local artifacts.
- Why safe: it clarifies where rules belong without changing lifecycle, statuses, review requirements, templates, or pipeline behavior.

## `ai-editorial-office/project-state.md`

- Why: it repeated permanent rules that should be owned by `AGENTS.md`.
- What changed: added a note that permanent rule ownership lives in `AGENTS.md`; replaced repeated architecture principles, risk-mode definitions, and artifact responsibility map with short ownership references.
- Why safe: current phase, active MVP agents, current focus, and normalization decisions remain. No task lifecycle semantics changed.

## `ai-editorial-office/kb/00_index.md`

- Why: the KB index was empty, so KB ownership was implicit.
- What changed: added a short note that `/kb` owns reusable standards, while `task_statuses.md` owns statuses and transitions.
- Why safe: it does not create a new rule system; it points back to `AGENTS.md` for authority hierarchy.

## Explicit non-changes

- No compact path implementation.
- No governance block implementation.
- No review behavior change.
- No template changes.
- No new statuses.
- No new agents.
- No pipeline rewrite.
- No lifecycle change.
