# Tests

Эта папка зарезервирована для будущих проверок целостности проекта.

Она существует как место, куда можно будет добавить простые проверки структуры,
навигации, синхронизации служебных пакетов или других безопасных invariants.

Статус папки: активная как место для будущей инфраструктуры. Сейчас содержит
markdown smoke-tests и synthetic examples:

- `sber-mode-smoke-test.md`
- `compact_execution_examples.md` - synthetic examples for compact execution
  and artifact minimalism; these are not task materials.
- `feedback_loop_examples.md` - synthetic examples for feedback classification;
  these are not task materials.
- `feedback_loop_smoke_test.md` - markdown manual smoke-test for feedback
  classification; these cases are synthetic and are not task materials.
- `feedback_loop_manual_trial.md` - sanitized manual trial for post-delivery
  feedback classification; it is not task materials.
- `feedback_loop_acceptance_trial.md` - sanitized manual trial for
  acceptance/future preference feedback classification; it is not task
  materials.
- `source_provenance_examples.md` - synthetic examples for source status
  classification; these are not task materials or source files.
- `source_provenance_smoke_test.md` - markdown manual smoke-test for
  source/provenance classification; these cases are synthetic and are not
  source materials.
- `research_evidence_examples.md` - synthetic examples for no-research,
  compact-evidence, and full-evidence mode selection; these are not task
  materials.
- `research_evidence_smoke_test.md` - markdown manual smoke-test for research
  evidence mode selection; these cases are synthetic and are not task materials.
- `test_task_pack_generator.sh` - shell smoke-test for
  `scripts/generate_task_pack.py`.
- `preflight_gate_examples.md` - synthetic examples for Preflight Gate routing
  decisions `ask`, `constrain`, `proceed`, and `block`; these are not task
  materials and do not replace Intake Agent, Chief Editor, or `AGENTS.md`.
- `preflight_gate_smoke_test.md` - markdown manual smoke-test for Preflight
  Gate routing; these cases are synthetic and are not task materials.
- `preflight_gate_manual_trial.md` - sanitized manual trial for checking
  whether Preflight Gate examples are useful on a realistic scenario; it is not
  task materials.
- `preflight_gate_sber_trial.md` - sanitized manual trial for checking Sber
  profile activation vs non-activation; it is not task materials.
- `preflight_gate_ux_trial.md` - sanitized manual trial for checking UX routing
  with missing product context; it is not task materials.
- `preflight_gate_checker_decision.md` - decision note recording why automated
  Preflight checker is not added yet; it is not production governance.
- `end_to_end_cases/access_pass_security_task/` - sanitized end-to-end case for
  an internal access-pass security task; it is not task materials and contains
  no real credentials, real cards, real system details, or exploit instructions.

## Task lifecycle validator smoke test

Запуск:

```bash
bash ai-editorial-office/tests/test_task_lifecycle_validator.sh
```

Smoke-test запускает `scripts/validate_task_lifecycle.py` на synthetic fixtures
из `tests/fixtures/task_lifecycle/`: valid и warning-only cases должны пройти с
exit code `0`, invalid cases должны завершиться с exit code `1`.

Сейчас smoke-test покрывает базовые lifecycle gates, consistency current status
между `task-manifest.md` и `status.md`, selected pipeline existence и
warning-only missing selected pipeline case. Он также покрывает previous/current
status transition checks из `kb/task_statuses.md`: invalid known transitions
дают blocker, missing previous status и same previous/current status дают
warning. Валидатор трактует unknown status как warning, а не blocker.

Fixtures в `tests/fixtures/task_lifecycle/` полностью искусственные и не
являются real task materials. Они нужны только для проверки локального
валидатора. Тест и валидатор не меняют task-файлы.

## Task pack generator smoke test

Запуск:

```bash
bash ai-editorial-office/tests/test_task_pack_generator.sh
```

Smoke-test запускает `scripts/generate_task_pack.py` на synthetic fixtures из
`tests/fixtures/task_pack/`. Fixtures полностью искусственные и не являются
real task materials. Они проверяют writer, review_agent, final_editor blocker и
chief_editor feedback read sets.

Feedback loop examples and smoke-test are used for manual classification checks:
they help verify when a user reaction is a task-local note, bounded revision,
possible system pattern, or system change proposal. They do not define active
rules and do not replace Chief Editor, Review Agent, `AGENTS.md`, or separate
reviewed system updates.

`feedback_loop_manual_trial.md` records a sanitized post-delivery scenario and
checks classification as bounded revision plus possible pattern watch. It is
not task materials and does not store real feedback.

`feedback_loop_acceptance_trial.md` records a sanitized accepted-result scenario
with a future preference. It checks that acceptance does not reopen the task and
does not become bounded revision without an explicit current-artifact change
request.

Source provenance examples and smoke-test are used for manual source-status
classification checks: they help verify `pending_source`, `active`, `stale`,
and `deprecated` handling. They are not source materials and do not replace
`AGENTS.md`, source notes, client-profile activation rules, or reviewed source
updates.

The reusable source import smoke-test template lives in
`templates/artifacts/source_import_smoke_test_template.md`. Real source import
smoke-tests should be added only for approved sanitized/source-safe cases.

Research evidence examples and smoke-test are used for manual evidence-depth
checks: they help verify when `no-research`, `compact-evidence`, or
`full-evidence` is appropriate. They do not define active rules and do not
replace `AGENTS.md`, selected pipelines, Research Agent, Writer Agent, Review
Agent, or `kb/research_evidence.md`.

Preflight Gate examples and smoke-test are used for manual routing checks only:
they help verify when the safe next strategy is `ask`, `constrain`, `proceed`,
or `block`. They do not define active rules and do not replace Intake Agent,
Chief Editor, or `AGENTS.md`.

`preflight_gate_manual_trial.md` records a sanitized trial of those examples on
a realistic internal coordination scenario. It is used to assess usefulness and
future checker needs, not to store real task materials.

`preflight_gate_sber_trial.md` records a sanitized trial for Sber-owned
communication versus Sber-as-topic routing. It checks when `client_profile`
should be `sber` and when it should remain `none`.

`preflight_gate_ux_trial.md` records a sanitized trial for UX writing with
missing product context. It checks when `ux_writing` can start through
`constrain` without inventing product behavior.

`preflight_gate_checker_decision.md` records the current decision to keep
Preflight Gate checks manual after three sanitized trials. It explains why an
automated checker is not added yet.

`end_to_end_cases/access_pass_security_task/` records a synthetic sanitized
end-to-end editorial case. It checks Preflight Gate `constrain`, compact
execution, no-research mode, no external source import, task pack generator
context, and review-gated finalization. It is not a real task folder and does
not contain real credentials, real cards, real system details, or exploit
instructions.

Читайте эту папку, когда нужно найти или добавить проверку целостности проекта.

Не читайте её как источник редакционных правил, пайплайнов или требований к
ролям.

Содержимое `tests/` не определяет активные правила системы. Тесты, если они
появятся, должны проверять уже существующие правила, а не создавать новые.
