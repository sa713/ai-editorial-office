# Brief

## raw request summary

User proposes creating a separate mode for Sber tasks and asks to briefly sketch
what "we" would do. In this test, no plan, roadmap, architecture decision,
change list, or Sber-mode design is created.

## user goal

- confirmed: consider a separate mode for Sber tasks;
- confirmed: future output requested by the raw prompt is a short plan of what
  to do;
- unknown: the problem this mode should solve, target behavior, scope,
  governance boundary, source basis, and success criterion.

## audience / reader

- confirmed: unknown;
- inferred: likely the user or internal editorial-system maintainer, but this
  is not stated as an audience requirement;
- unknown: whether the future plan is for the user, the editorial office,
  reviewers, implementers, or another decision-maker.

## expected artifact

- confirmed: short plan, in a future production task;
- inferred: management/system-planning task;
- unknown: exact format, depth, decision owner, review standard, and whether the
  output should be proposal, implementation plan, risk note, or decision brief.

## source status

- supplied sources: none;
- source status: `mentioned but not provided`;
- source boundary: "Sber tasks" are mentioned as the subject, but no Sber
  requirements, client policy, examples, task failures, source files, or
  governance constraints are supplied in the raw request.
- client profile status: not activated for this normalization test.

## constraints

- Do not create the plan.
- Do not create a roadmap.
- Do not create an architecture decision.
- Do not create a list of changes.
- Do not invent Sber requirements.
- Do not invent Sber-mode functions, files, roles, architecture, stages, or
  implementation constraints.
- Do not substitute normalization with design.

## explicit requirements

- Consider a separate mode for Sber tasks.
- Future output requested: briefly sketch what to do.

## assumptions

- `assumption`: the raw request is a management/system-change planning request,
  not an ordinary Sber content-production task.
- `assumption`: Sber is a subject of a possible system mode, not an activated
  task-local client profile for content production.
- No assumption is safe enough to define functions, files, roles, architecture,
  stages, implementation constraints, or Sber requirements.

## open questions

- What problem should a separate Sber mode solve?
- What counts as a "Sber task" for this proposal?
- Is there an existing source of Sber requirements or editorial policy to use?
- Should the future plan evaluate whether a separate mode is needed at all?
- What level of plan is expected: decision note, implementation outline,
  governance proposal, or task checklist?
- Who will review or approve the future plan?
- What must not change in the existing editorial system?

## acceptance criteria

- Future plan acceptance criteria: `unknown` beyond being short and about what
  to do regarding a possible Sber task mode.
- Intake acceptance for this test: the normalized task definition must not
  invent mode functions, files, roles, architecture, Sber requirements, stages,
  implementation constraints, or a roadmap.

## suggested task type / pipeline

- Suggested task type: management/system-change planning request.
- Suggested pipeline: not selectable for production until Chief Editor
  clarifies scope and source boundary.
- Missing data strategy: `ask` before any planning/design production.

## risks

- Creating a plan now would invent requirements and implementation direction.
- Mentioning Sber could wrongly activate a client profile or import unstated
  Sber policy.
- A short management request could be over-expanded into architecture without
  user confirmation.
- File, role, and pipeline changes would be speculative.
