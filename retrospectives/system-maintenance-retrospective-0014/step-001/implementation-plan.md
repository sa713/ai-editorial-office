# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0014`

Step: `step-001`

Name: Editorial Entry Discipline

Goal: prevent editorial tasks from being silently executed through direct
technical production before editorial routing.

## Context

`TASK-0019` showed that a task could be framed as an editorial task, live in a
TASK folder, and match an existing editorial mode, but still be executed through
a direct technical path:

```text
PDF
↓
data extraction
↓
infographic
↓
SVG/PNG
```

This bypassed editorial routing.

## Canonical Owner

Canonical owner: `ai-editorial-office/AGENTS.md`

Reason: entry discipline is a system invariant and governance boundary. It
controls when Chief Editor must route a task before production. It is not a
pipeline detail, visual-mode rule, review heuristic, or agent-specific behavior.

## Implementation Steps

1. Add an editorial-entry invariant to `AGENTS.md`.
2. Add an `Editorial entry discipline` section.
3. For TASK-folder, editorial-project, or existing-workflow requests, forbid
   direct-production execution before routing.
4. Require Chief Editor to determine task type, select pipeline or mode,
   activate visual branch when needed, and determine roles.
5. State that SVG, PNG, HTML, image generation, PDF extraction, OCR, parsing,
   conversion, scraping, rendering, and other tool work are not substitutes for
   editorial routing.
6. Add explicit bypass exception for user requests to do the work directly,
   skip editorial process, bypass process, not use the editorial system, or
   handle the request as an ordinary non-editorial task.
7. Require output to stay within the selected mode.

## Non-Goals

- No pipeline changes.
- No Artist Agent changes.
- No visual mode changes.
- No review-system changes.
- No new architecture.
- No new agents.

## Status

Completed.
