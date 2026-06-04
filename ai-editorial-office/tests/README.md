# Tests

Эта папка зарезервирована для будущих проверок целостности проекта.

Она существует как место, куда можно будет добавить простые проверки структуры,
навигации, синхронизации служебных пакетов или других безопасных invariants.

Статус папки: активная как место для будущей инфраструктуры. Сейчас содержит
markdown smoke-test для Sber-mode:

- `sber-mode-smoke-test.md`
- `compact_execution_examples.md` - synthetic examples for compact execution
  and artifact minimalism; these are not task materials.

## Task lifecycle validator smoke test

Запуск:

```bash
bash ai-editorial-office/tests/test_task_lifecycle_validator.sh
```

Smoke-test запускает `scripts/validate_task_lifecycle.py` на synthetic fixtures
из `tests/fixtures/task_lifecycle/`: один valid case должен пройти с exit code
`0`, invalid cases должны завершиться с exit code `1`.

Fixtures в `tests/fixtures/task_lifecycle/` полностью искусственные и не
являются real task materials. Они нужны только для проверки локального
валидатора. Тест и валидатор не меняют task-файлы.

Читайте эту папку, когда нужно найти или добавить проверку целостности проекта.

Не читайте её как источник редакционных правил, пайплайнов или требований к
ролям.

Содержимое `tests/` не определяет активные правила системы. Тесты, если они
появятся, должны проверять уже существующие правила, а не создавать новые.
