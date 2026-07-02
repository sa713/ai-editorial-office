# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0014`

Step: `step-002`

Name: Codex Entry Bootstrap

Goal: make Codex see the editorial entry contract before working on any
`TASK-*` request.

## Findings

The main editorial charter exists at:

```text
ai-editorial-office/AGENTS.md
```

There was no repository-root `AGENTS.md` at:

```text
AGENTS.md
```

Because the working directory is the repository root, Codex could enter a
`TASK-*` request through file operations before loading the nested editorial
charter.

## Implementation Steps

1. Create a short root `AGENTS.md`.
2. Keep it as a bootstrap pointer, not a duplicate charter.
3. Require reading `ai-editorial-office/AGENTS.md` when a request mentions
   `TASK-*`, work happens in a `TASK-*` folder, or the task belongs to the
   editorial system.
4. Require editorial entry activation before production: `chief_editor`, task
   type, pipeline or mode, `task-manifest.md`, `orchestration_plan.md`,
   `status.md`, and required roles.
5. Explicitly forbid direct `PDF -> SVG/PNG/MD` production for editorial
   `TASK-*` work unless the user asks to bypass the editorial process.

## Non-Goals

- No visual branch changes.
- No Artist Agent changes.
- No review system changes.
- No pipeline changes.
- No retroactive repair of `TASK-0019` or `TASK-0020` outputs.

## Status

Completed.
