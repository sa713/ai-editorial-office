# Orchestration Plan

## task summary

- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
- User goal: make the office choose the best artifact for the real objective
  before selecting a production pipeline.
- Requested deliverable: canonical implementation, tests, implementation report,
  complete diff, file summary, and architecture explanation.
- Format authority: `explicit`.
- Selected deliverable: same as requested.

## task need recognition

- Observed request signals: bounded architecture extension; existing Task Need
  Recognition, Chief Editor, orchestration, and Review owners named; explicit
  forbidden architecture growth; synthetic tests required.
- Recommended deliverable: bounded canonical patch plus task-local test/report/
  diff evidence.
- Likely primary task type: canonical system capability update.
- Material secondary aspects: architecture fit, Engineering Review, deterministic
  review, `/about` synchronization.
- Research/evidence recommendation: source-light repository inspection; no web
  research required because the design objective and constraints are supplied.
- Review recommendation: standard independent review with architecture and
  regression checks.
- Explicit non-decision: recognition does not select the deliverable, pipeline,
  role set, status, or review outcome.

## outcome-first deliverable decision

- User problem to solve: extend routing judgment without architecture redesign.
- Requested deliverable: implementation package defined above.
- Format authority: `explicit`.
- Recommended deliverable: same bounded implementation package.
- Why this is the smallest sufficient outcome-fit artifact: it changes the
  existing owners, proves behavior with synthetic cases, and returns the exact
  evidence requested without a release pack or new framework.
- Decision: `respect_requested`.
- Selected deliverable: bounded canonical patch, synthetic test,
  implementation report, and complete diff.
- Explicit-intent preservation note: no requested artifact is replaced.

## selected pipeline

- Pipeline: `review_pipeline` with a task-local system-update mini-contract.
- Why it fits the selected deliverable: the task changes markdown canon,
  templates, and tests; no production pipeline exactly owns repository
  implementation, while Review Pipeline provides the required independent gate.
- New pipeline created: no.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | confirmed |
| Channel or context | confirmed |
| Selected deliverable | defined |
| Source boundary | defined |
| Success criterion | defined |
| Approval boundary | defined |
| Missing data strategy | proceed |

- Production may start: yes.
- Scope boundary: canonical outcome-first integration only; unrelated untracked
  files remain untouched.

## required roles

| Stage | Role | Required | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Own deliverable and workflow decision |
| Implementation | Writer / implementation function | yes | Patch canonical docs/templates/tests |
| Review | Review Agent | yes | Independent role instance and `review.md` |
| Final governance | Chief Editor | yes | Close only after approved review |

No Deliverable Agent, Format Agent, or other permanent role is created.

## artifact scope

- Required: brief, manifest, status, orchestration plan, user-requested report
  and complete diff, independent review, compact final pointer, final decision.
- Omitted: research pack, claims table, QA checklist, release pack, roadmap,
  standalone deliverable-selection artifact, new pipeline specification.

## execution order

1. Inspect current owners and constraints.
2. Extend Task Need Recognition with advisory deliverable recommendation.
3. Extend Intake, Chief Editor, task model, orchestration, pipeline contracts,
   production preservation, and Review.
4. Add synthetic regression cases.
5. Synchronize `/about` exact copies.
6. Validate and hand off to an independent Review Agent.
7. Repair only bounded findings, revalidate, and finalize.

## review requirements

- Verify requested/recommended/selected separation.
- Verify explicit intent cannot be silently overridden.
- Verify selected deliverable precedes and governs pipeline choice.
- Verify a bare `explain` request cannot become a checklist without outcome
  evidence.
- Verify no permanent role, pipeline, stage, gate, score, or mandatory artifact
  was added.
- Verify tests cover explicit, delegated, inferred, mismatch, and compact cases.
- Verify unrelated files are untouched and `/about` is synchronized.

## completion criteria

- Required canonical integrations are internally consistent.
- Synthetic test contract is complete.
- Existing validators pass.
- Independent review outcome is `approved`.
- Report and complete diff are current.
