# Orchestration Plan

## task summary

- Task ID: `TASK-EDITORIAL-CHALLENGE-FRAMEWORK`
- User goal: implement the assumptions-based Editorial Challenge Framework.
- Deliverable: production instruction patch and `production-diff.md`
- Current active version: `production-diff.md`

## task classification

- Task type: production instruction update.
- Risk mode: `standard`
- Factual sensitivity: low; architecture precision matters.
- Human approval likely required: no.
- Rationale: the user requested implementation after design refinement.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the requested work is a bounded production-doc patch.
- Forbidden depth shortcuts: do not add roles, review-gate changes, or
  mandatory artifacts.
- Expanded profile trigger, if any: conflict with review pipeline or role
  boundaries.

## selected pipeline

- Pipeline: compact production instruction update.
- Why this pipeline: the user requested a minimal production implementation.
- Pipeline exceptions or local constraints: edit only the requested production
  files unless strict necessity appears.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the user provided clear design questions and constraints.
- Production may start: yes.

## problem hypothesis

- User request: implement a challenge mechanism for Review Agent.
- Problem hypothesis: current challenge design needs a deterministic way to
  test whether route-validity assumptions still hold before claiming another
  editorial route is stronger.
- Basis: stated-by-user and source-backed by the current Review Agent scope.
- Confidence: high.
- Respect boundary: the design must strengthen review without turning Reviewer
  into Writer, Chief Editor, or a preference-based judge.
- Routing implication: propose a compact assumptions-based challenge lens inside
  `review.md`.

## editorial decision frame

- Chosen editorial route: update the existing review instructions and template
  around route-validity assumptions.
- Why this route serves the task: it makes editorial challenge less subjective
  without new roles, production artifacts, lifecycle steps, or review cycles.
- Alternatives considered, usually 2-3 compact options:
  - Add a new Challenge Agent:
    - Why rejected: violates no-new-role constraint.
  - Add mandatory `challenge.md`:
    - Why rejected: violates artifact minimalism and duplicates `review.md`.
  - Keep strongest-objection-only model:
    - Why rejected: still leaves too much room for preference-shaped disputes.
  - Let Reviewer propose preferred rewrites:
    - Why rejected: turns Review Agent into Writer or Chief Editor.
- Writer/UX Writer contract: not applicable.
- Review focus: verify assumptions-based challenge, deterministic outcomes, and
  non-preference evidence standard.
- Reroute triggers: conflict with review-gate, role boundaries, or need for
  production files outside the requested list.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Own design routing |
| Implementation | Chief Editor / Codex | yes | Patch requested production files |
| Review | Review Agent | compact self-check | Check constraints, diff, and mechanism |

## completion criteria

- Requested production files are updated.
- No new production files are created.
- No new role, review gate, mandatory artifact, or extra review cycle is added.
- Full requested diff is saved.
- Git status is reported.
