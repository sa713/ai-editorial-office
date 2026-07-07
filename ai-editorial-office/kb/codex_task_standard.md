# Codex Task Standard

Purpose: turn a normalized brief into a compact, executable Codex task and a
small review packet. This standard is used when the editorial office needs to
ask Codex to modify files, inspect a local system, or prepare a patch.

This file is guidance, not a new role, pipeline, capability pack, validator, or
mandatory artifact for every editorial task. Chief Editor owns the decision to
use it and must keep the selected task pipeline, review-gate, and role
boundaries intact. Implementation-task dilution and recovery are covered by
`/kb/editorial_failure_modes.md`; planning depth and option evaluation are
covered by `/kb/editorial_planning_framework.md`; Codex as implementer audience
is covered by `/kb/audience_outcome_alignment.md`; implementation-task quality
attributes are covered by `/kb/editorial_quality_attributes.md`; reusable
learning and canon-update signals are covered by
`/kb/editorial_learning_framework.md`.

## owner and chain

Current chain:

```text
raw request -> normalized brief -> Codex task -> implementation -> check-pack -> review
```

Ownership:

- Intake Agent owns raw request -> normalized brief.
- Chief Editor owns normalized brief -> Codex task and check-pack contract.
- Codex executes only within the task boundaries.
- Review remains separate when the result requires review.

`generate_task_pack.py` is only a read-only context helper. It can suggest a
restart/read set, but it does not generate Codex tasks, route work, or replace
Chief Editor judgment.

## Codex task shape

Use one compact markdown prompt. Include only sections that help execution or
review.

```md
# Задача для Codex

## Цель

## Контекст

## Рабочая зона

## Source of truth

## Что можно менять

## Что нельзя менять

## Глубина работы

## Acceptance criteria

## Формат результата

## Что прислать на проверку
```

Minimum expectations:

- `Цель`: what must change and what result is needed.
- `Контекст`: why the change matters and what behavior it improves.
- `Рабочая зона`: exact files or directories to inspect/change.
- `Source of truth`: ordered rules and files Codex should trust.
- `Что можно менять`: allowed files or bounded areas.
- `Что нельзя менять`: hard stops, role/pipeline/review-gate boundaries, and
  sensitive exclusions.
- `Глубина работы`: compact patch, normal patch, or broader change, with
  explicit non-goals.
- `Acceptance criteria`: observable completion checks.
- `Формат результата`: expected files, notes, and whether chat should stay
  short.
- `Что прислать на проверку`: diff summary, changed files, key fragments,
  implementation notes, check-pack, checks, and reusable learning/canon-update
  signals only when material.

Audience fit: Codex is the reader and executor. The task should make the next
repository action obvious, bounded, and reviewable.

Quality fit: a Codex task should be repository-aware, implementation-focused,
appropriately scoped, technically precise, validation-ready, actionable, low in
ambiguity, high in implementation value, and reviewable.

## task writing rules

- Start from the normalized brief, not from chat noise.
- Confirm the active repository and forbidden paths before asking Codex to edit
  files.
- For non-trivial implementation tasks, name why the selected repository slice
  is the next highest-value option compared with credible alternatives.
- State the expected value of the slice and the action Codex must complete,
  not only the abstract strategy.
- Include enough repository context, likely files, boundaries, validation, and
  deliver-back format for Codex to execute without guessing.
- Prefer implementation readiness, technical precision, validation readiness,
  and reviewability over broad theory or polished process language.
- Surface reusable learning, stale assumptions, or canon-update candidates only
  when they are material and evidence-backed; do not turn every Codex task into
  a retrospective.
- Preserve `confirmed`, `inferred`, `unknown`, `assumption`, and `question`
  distinctions when they affect scope.
- Do not invent source materials, requirements, acceptance criteria, files,
  roles, pipelines, or implementation strategy.
- Prefer exact file paths and bounded areas over broad project scans.
- Use the smallest source-of-truth list that can safely constrain Codex.
- Put prohibitions close to the work they protect.
- Ask for clarification or mark `unknown` when a missing field can materially
  change implementation.
- Keep the task copyable as one markdown block when the user needs to paste it
  elsewhere.

## Codex task quality guard

Stop and repair the task before execution when it is too process-heavy, too
vague, mostly documentation without repository value, disconnected from current
git/files, missing validation, missing deliver-back requirements, or aimed at
Studio/legacy paths instead of the active Editorial Office repository.

Recovery:

- restate the active repository and forbidden paths;
- inspect actual files before proposing architecture;
- compare credible implementation options when the first idea is not obviously
  sufficient;
- re-align the task for Codex as implementer: goal, context, files,
  boundaries, validation, deliver-back, expected value, and exclusions;
- re-select quality priorities when the task is optimizing for strategy,
  elegance, or completeness instead of implementation value;
- extract learning deliberately when the implementation reveals a reusable
  pattern, stale canon, or canon-update candidate;
- name the smallest useful implementation outcome;
- include validation and deliver-back requirements;
- remove process narration that does not help implementation or review;
- defer speculative future work unless it is explicitly requested.

## Check Pack shape

Create a check-pack when the user requests review support, when a system patch
needs external review, or when the change should be easy to verify after
context loss. Keep it short.

```md
# Check pack

## Краткая суть изменения

## Список изменённых файлов

## Git diff summary

## Ключевые фрагменты изменённых файлов

## Риски

## Что нужно прислать ChatGPT на ревью
```

Optional additions are allowed only when useful:

- `Manual check / smoke-test results`;
- `Known limitations`;
- `Reusable learning or canon-update signal`;
- `Open questions`.

Do not turn check-pack into a duplicate of the full diff, a long report, a
review verdict, or a replacement for `review.md` when review is required by the
selected pipeline.

## Examples

### brief -> Codex task

Normalized brief:

```md
Goal: add a source-status field to one task template.
Working area: one template file.
Source of truth: AGENTS.md, current template, source provenance KB.
Unknown: whether `/about` has a synced copy.
Forbidden: no new roles, no pipeline changes, no validator.
Acceptance: field exists, examples stay compact, no review-gate change.
```

Good Codex task:

```md
# Задача для Codex

## Цель
Add a compact source-status field to the named task template.

## Рабочая зона
Only `ai-editorial-office/templates/tasks/example_task_template.md`.

## Source of truth
1. `ai-editorial-office/AGENTS.md`
2. `ai-editorial-office/kb/source_provenance.md`
3. current template file

## Что нельзя менять
- Do not add roles, pipelines, validators, or mandatory artifacts.
- Do not change review-gate.
- Do not edit unrelated templates.

## Acceptance criteria
- Template has a concise source-status field.
- Existing structure remains intact.
- Change is easy to review in diff.

## Что прислать на проверку
- git diff summary;
- changed file;
- key fragment;
- manual check result.
```

### brief -> Check Pack

Good check-pack:

```md
# Check pack

## Краткая суть изменения
Added a source-status field to one task template.

## Список изменённых файлов
- `ai-editorial-office/templates/tasks/example_task_template.md`

## Git diff summary
`1 file changed, 4 insertions(+)`

## Ключевые фрагменты изменённых файлов
- New `## source status` section with `confirmed / unknown / pending` guidance.

## Риски
- Field could be misread as mandatory evidence for no-source tasks.

## Что нужно прислать ChatGPT на ревью
- template diff;
- this check-pack;
- manual check result.
```
