# Entry Bootstrap Decisions

## Where The Entry Rule Now Lives

The canonical editorial rules remain in:

```text
ai-editorial-office/AGENTS.md
```

A new repository-root bootstrap rule now lives in:

```text
AGENTS.md
```

The root file is intentionally short. It does not replace the editorial
charter; it forces Codex to load the charter before production work.

## Why Codex Will See It Before Task Execution

The repository root is:

```text
/Users/sa/Documents/codex/redaction
```

The previous only `AGENTS.md` file was nested under `ai-editorial-office/`.
When Codex started from the repository root, there was no root-level entry
instruction telling it to read the nested editorial charter before acting on a
`TASK-*` request.

The root `AGENTS.md` is now in the starting directory. It is the first visible
bootstrap instruction for repository work and points immediately to
`ai-editorial-office/AGENTS.md` whenever the request mentions `TASK-*`, work is
inside a `TASK-*` folder, or the task belongs to the editorial system.

## How This Prevents A Repeat Of TASK-0019

For a request such as:

```text
В папке TASK-0019 находится статья. Подготовь визуальный конспект статьи для блога.
```

the root bootstrap now matches `TASK-0019` before any PDF extraction, SVG
authoring, PNG rendering, or Markdown production.

It requires Codex to:

- read `ai-editorial-office/AGENTS.md`;
- activate `chief_editor`;
- determine task type;
- choose the pipeline or mode;
- create or update `task-manifest.md`;
- create or update `orchestration_plan.md`;
- update `status.md` when state changes;
- assign required roles.

The direct technical path `PDF -> SVG/PNG/MD` is explicitly forbidden for
editorial `TASK-*` work unless the user asks to bypass the editorial process.

## Files Changed

- `AGENTS.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/implementation-plan.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/entry-bootstrap-decisions.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/changed-files.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/safety-check.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/rollback-notes.md`
- `retrospectives/system-maintenance-retrospective-0014/step-002/diff.md`
