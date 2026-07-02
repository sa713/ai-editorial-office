# Entry Discipline Decisions

## Decision

If a task is presented as an editorial task, the editorial process must be
activated before production.

This prevents the system from treating a TASK-folder request as a generic
technical conversion or image-generation job.

## Canonical Owner

`AGENTS.md` owns this rule.

Reason: the rule governs system entry, orchestration, role selection, and
governance boundaries. It should not be duplicated in individual pipelines,
agent specs, visual modes, or review heuristics.

## Editorial Task Signals

Editorial routing is required when the user works through:

- a `TASK-ID` folder;
- the editorial project;
- an existing editorial workflow;
- a task that clearly maps to an existing editorial mode or pipeline.

## Required Routing

Before production starts, Chief Editor must:

- determine the task type;
- choose a pipeline or editorial mode;
- activate the visual branch when needed;
- determine required roles and bounded extension roles;
- record the routing decision in a task artifact.

## Technical Work Boundary

Technical actions may support the task after routing, but they do not replace
routing:

- SVG;
- PNG;
- HTML;
- image generation;
- PDF extraction;
- OCR;
- parsing;
- conversion;
- scraping;
- rendering.

## Exception

Direct-production execution is allowed only when the user explicitly asks to
work directly, skip editorial process, bypass process, not use the editorial
system, or handle the request as an ordinary non-editorial task.

## Mode Fidelity

After routing, the result must match the selected mode. If
`visual_article_sketchnote` is selected, the system must not silently switch to
infographic, web page, SVG summary, corporate one-pager, or another output
genre.

## Architecture Decision

No new architecture was added. This is a discipline rule at the existing
governance entry point.
