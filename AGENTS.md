# Codex Entry Bootstrap

This repository contains an editorial system in `ai-editorial-office/`.

If the user request mentions `TASK-*`, work is performed in a `TASK-*` folder,
or the task belongs to the editorial system, read
`ai-editorial-office/AGENTS.md` before any production action.

Then start the editorial entry flow there:

- activate `chief_editor`;
- determine task type;
- choose the pipeline or mode;
- create or update `task-manifest.md`;
- create or update `orchestration_plan.md`;
- update `status.md` when state changes;
- assign the required roles.

For editorial `TASK-*` work, the direct path `PDF -> SVG/PNG/MD` is forbidden
unless the user explicitly asks to bypass the editorial process.
