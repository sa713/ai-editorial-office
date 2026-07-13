# Codex Entry Bootstrap

This repository contains an editorial system in `ai-editorial-office/`.

If the user request mentions `TASK-*`, work is performed in a `TASK-*` folder,
or the task belongs to the editorial system, read
`ai-editorial-office/AGENTS.md` before any production action.

Then start the editorial entry flow there:

- activate `chief_editor`;
- determine task type;
- distinguish the requested deliverable from the outcome-first recommended
  deliverable set, then record a single or ordered selected deliverable set
  without silently overriding explicit user intent or generating companions
  automatically;
- choose the pipeline or mode;
- create or update `task-manifest.md`;
- create or update `orchestration_plan.md`;
- update `status.md` when state changes;
- assign the required roles.

For editorial `TASK-*` work, the direct path `PDF -> SVG/PNG/MD` is forbidden
unless the user explicitly asks to bypass the editorial process.
