# System Change Proposal

## proposal metadata

- Proposal ID: `EDF-STEP-1`
- Source: user request on 2026-06-30
- Date: 2026-06-30
- Proposed by: Chief Editor
- Related task(s): `TASK-EDITORIAL-DECISION-FRAMEWORK-STEP-1`

## problem signal

The editorial office often reaches a good strategic choice, but the artifact
trail does not show enough of the reasoning before writing starts. Downstream
readers can see the selected result, but not the alternatives considered, why
they were rejected, or why the chosen path is the right editorial route.

## proposed change

Add a compact `editorial decision frame` to the existing Chief Editor
orchestration/planning step. It should live inside `orchestration_plan.md`, with
a short pointer or summary in the planning handoff to Writer Agent or UX Writer.

This is not a new pipeline, role, status, or mandatory standalone artifact.

## where the decision happens

The decision should happen after intake and, when research is required, after
research sufficiency is known, but before writing or UX writing begins.

In the existing lifecycle this means:

- during Chief Editor orchestration for simple tasks that can move directly from
  `intake` to `planning` or `writing`;
- during the `planning` step after research for tasks that need evidence first;
- before `handoff-planning-chief-editor-to-writer-agent.md` or
  `handoff-planning-chief-editor-to-ux-writer.md`.

## owner

Chief Editor owns the decision. Intake Agent supplies normalized inputs.
Research Agent supplies evidence and constraints when needed. Writer Agent and
UX Writer consume the decision but do not own the editorial route. Review Agent
checks the decision trail and whether the produced artifact follows it.

## artifact decision

Do not introduce a mandatory new artifact.

Use `orchestration_plan.md` because its canonical responsibility is the
task-specific execution contract: selected pipeline, roles, artifact scope,
gates, and local constraints. The editorial decision frame is part of that
contract.

Do not use `final_decision.md`: it is the Chief Editor final governance decision
after review and finalization, not a pre-writing route decision.

Do not canonize the legacy `editorial_decision.md` example as a standard
artifact. A task-local standalone decision note may still be allowed only when a
specific high-governance or restartability need exceeds what the orchestration
plan can hold.

## data into the decision

- Normalized brief: goal, audience, channel/context, deliverable, constraints,
  acceptance criteria.
- Source boundary: what may be used, what is missing, and what must not be
  invented.
- Risk mode, process depth, execution profile, and client profile state.
- Research findings, contradictions, caveats, and no-research rationale when
  applicable.
- Candidate editorial routes: output type, angle, reader path, scope, evidence
  strategy, artifact depth, and handoff target.
- User constraints and explicit non-goals.

## data out of the decision

- Chosen editorial route.
- Alternatives considered, usually two or three compact options.
- Rejection rationale for each non-selected path.
- Reason the chosen route serves the user goal better.
- Writing or UX writing contract: angle, reader path, scope, must-include,
  do-not-include, evidence/caveat requirements, and review focus.
- Reroute triggers: conditions that send the task back to research, Chief
  Editor, user clarification, or blocked state.

## transfer to Writer Agent

Writer Agent receives the decision through:

- `orchestration_plan.md` as the source of truth;
- the planning handoff as a compact delta summary;
- `task-manifest.md` only as a pointer to the current plan and next action.

The handoff should not repeat the full decision. It should name the chosen route,
the rejected paths that Writer must not resurrect, and the review focus.

## reviewer validation

Review Agent can check:

- `orchestration_plan.md` contains a visible editorial decision frame before
  writing started, unless compact omission is justified;
- the decision includes a chosen route and rejected alternatives with reasons;
- the chosen route is consistent with the brief, evidence, risk mode, and source
  boundary;
- Writer Agent or UX Writer followed the chosen route;
- rejected paths did not reappear silently in the draft;
- missing or weak rationale creates a review finding only when it affects
  reviewability, traceability, governance, or output quality.

## likely implementation files

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/writer_agent.md`
- `ai-editorial-office/agents/ux_writer.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/artifacts/handoff_template.md`

Potentially update `ai-editorial-office/project-state.md` after implementation
to record the active normalization decision. Existing pipeline files do not need
to change in the minimal version because they already route through Chief Editor
planning and require compliance with `orchestration_plan.md`.

## proposed orchestration section

```markdown
## editorial decision frame

- Chosen route:
- Why this route:
- Alternatives considered:
  - Option:
    - Why rejected:
- Writer/UX Writer contract:
  - Angle or reader path:
  - Scope:
  - Must include:
  - Must not include:
  - Evidence and caveats:
  - Review focus:
- Reroute triggers:
```

For compact tasks, the section may be three short bullets: chosen route, one
rejected alternative, and writer contract.

## non-goals

- No new role.
- No new pipeline.
- No new status.
- No mandatory standalone `editorial_decision.md`.
- No duplication between manifest, status, orchestration plan, handoff, and
  review.
- No requirement to make every small task produce a large strategy memo.

## risks

- Artifact bloat if the section becomes long by default.
- Chief Editor could over-explain instead of making a compact decision.
- Reviewer could start judging taste instead of checking decision quality.

Mitigation: keep the frame compact and review it only as an operational contract
needed for writing, reviewability, and traceability.

## decision

- Status: proposed
- Decision owner: user / Chief Editor
- Decision notes: recommended as the minimal change for implementation step 2.
