# Problem Hypothesis Framework Proposal

## proposed change

Add a compact `Problem Hypothesis` section to `orchestration_plan.md`, placed
after the Preflight Gate and before the Editorial Decision Frame.

The section answers a bounded editorial question before route selection becomes
final:

> What problem does the user's request appear to be addressing, based on the
> request, materials, context, and available evidence?

This is not a claim that the editorial office knows the user's true problem. It
is a labeled professional hypothesis that must show its basis, confidence, and
respect boundary.

This is not a new role, pipeline, status, or mandatory standalone artifact. It
is a small orchestration guardrail owned by Chief Editor.

## why this belongs in orchestration

Intake should normalize what the user asked for. Research should clarify
evidence when needed. Chief Editor should form a bounded hypothesis about the
problem the request may be addressing because that hypothesis affects:

- task type;
- pipeline or mode;
- whether the requested deliverable can serve the stated request;
- whether to ask, constrain, proceed, or block;
- the Editorial Decision Frame handed to Writer Agent or UX Writer.

The Problem Hypothesis should be recorded before the Editorial Decision Frame.
If research is needed before the hypothesis can be responsibly formed, Chief
Editor should refresh the hypothesis after research sufficiency is known and
before writing starts.

## suggested compact format

```markdown
## problem hypothesis

- User request:
- Problem hypothesis:
- Basis: `stated-by-user` / `source-backed` / `context-inferred` / `unknown`
- Confidence: `high` / `medium` / `low`
- Respect boundary:
- Routing implication: `honor_request` / `serve_request_with_reframe` /
  `constrain` / `ask_before_reframe` / `block`
```

Keep it short. The goal is not to diagnose the organization, outsmart the
request, or assert hidden user intent. The goal is to make the editorial
interpretation explicit enough to be checked before production.

## field logic

`User request` preserves the user's stated intent in plain language. It is the
anchor that prevents the editorial office from drifting into its own consulting
agenda.

`Problem hypothesis` names the editorial hypothesis, not a fact. It should be
phrased as "the request appears to be about..." or "the source suggests the
underlying editorial need may be..." when the basis is not directly stated.

`Basis` is mandatory because it says why the hypothesis is allowed to exist at
all:

- `stated-by-user`: the user explicitly names the problem, reason, or desired
  change.
- `source-backed`: supplied materials show a recurring issue, gap, ambiguity,
  or tension that supports the hypothesis.
- `context-inferred`: Chief Editor can infer a likely editorial need from the
  request and task context, but the inference must remain labeled.
- `unknown`: the request is too ambiguous or the hypothesis would be too
  speculative.

`Confidence` is mandatory because even a plausible hypothesis can be weak. High
confidence requires direct user wording or strong source support. Medium
confidence is acceptable when the hypothesis is useful but not settled. Low
confidence should push the route toward `constrain`, `ask_before_reframe`, or
`block`.

`Respect boundary` is mandatory because the hypothesis must explain how the
chosen route will still respect the user's stated request. It should name what
the editorial office will not assume, not decide, or not override.

`Routing implication` turns the hypothesis into an operational decision without
pretending it is truth:

- `honor_request`: the requested deliverable and the hypothesis align.
- `serve_request_with_reframe`: the requested goal can be served better by
  reframing the route while staying within the user's intent.
- `constrain`: proceed only within a narrower, explicitly caveated scope.
- `ask_before_reframe`: ask the user before changing deliverable, audience,
  approval boundary, or work scope.
- `block`: do not proceed because the hypothesis is too speculative or the task
  would require unsupported assumptions.

## how to distinguish hypothesis from speculation

Use an evidence ladder.

`stated-by-user`: the user explicitly names the problem or reason.

Example: "Need a presentation because leadership does not understand the
initiative." The hypothesis can be high-confidence because the user supplied
the reason.

`source-backed`: supplied materials show a likely editorial problem even if the
user asks for a format.

Example: the user asks for PR, but the source is a raw brainstorm with unclear
service definition, no approved claims, no audiences, no channels, and no
approval. The hypothesis is not "the user really needs product strategy"; it is
"the request appears to require service clarity before PR materials can be
responsibly written."

`context-inferred`: Chief Editor can infer a possible editorial need from the
request and context, but must label it as inference.

Example: the user asks for an article and provides dense background materials.
The hypothesis may be that the audience lacks context, but the frame must keep
that as an editorial inference unless the user or source says it directly.

`unknown`: the request is too ambiguous, or the inferred hypothesis would
materially change the expected result.

Rule: if the hypothesis would change the user's expected deliverable, audience,
approval boundary, or work scope, Chief Editor should use `ask_before_reframe`
or `constrain`, not silently override the user.

## anti-consulting boundary

Problem Hypothesis must respect the user's intent. It is a service lens, not an
argument.

Chief Editor may say:

- "The user requests a presentation. The materials suggest the likely
  editorial problem is unclear thought structure, so the route should first
  produce a structured narrative that can become slides."
- "The user requests PR. The source supports only a service-clarity hypothesis,
  so PR copy would be premature unless the user confirms a PR-copy task with
  additional inputs."

Chief Editor must not say, without evidence:

- "The user is wrong."
- "The real business problem is X."
- "The organization needs a management intervention."
- "We should refuse the requested format because a better consultant solution
  exists."

The output should preserve a visible line back to the user's stated request:
how the route serves it, where it narrows it, or why clarification is needed
before a reframe.

## lifecycle change

Current lifecycle:

1. Intake
2. Orchestration / Preflight
3. Editorial Decision Frame
4. Research if needed
5. Writing / UX writing
6. Review
7. Finalization
8. Chief Editor final governance

Proposed lifecycle:

1. Intake
2. Orchestration / Preflight
3. Problem Hypothesis
4. Editorial Decision Frame
5. Research if needed, with Problem Hypothesis and Editorial Decision Frame
   refreshed before writing when research changes the hypothesis or route
6. Writing / UX writing
7. Review
8. Finalization
9. Chief Editor final governance

This is not a new stage in the status model. It is a compact decision inside
orchestration.

## handoff behavior

Planning handoff to Writer Agent or UX Writer should include only a one-line
hypothesis summary when it materially affects production:

```markdown
- Problem hypothesis:
- Chosen route:
- Rejected alternatives:
- Writing/UX writing contract:
- Review focus:
```

Do not transfer the full Problem Hypothesis section. Handoff remains
delta-transfer.

## Reviewer validation

Review Agent should check:

- Was the Problem Hypothesis present before writing when the task involved a
  non-trivial user request, source ambiguity, or route reframe?
- Does the hypothesis remain phrased as a hypothesis rather than a claim of
  true user intent?
- Does the stated basis support the confidence level?
- Do `Basis`, `Confidence`, and `Respect boundary` actively limit the
  hypothesis, or are they decorative labels?
- Did Chief Editor preserve the user's stated request instead of replacing it
  with an unsupported consultant diagnosis?
- If the hypothesis changed the route or deliverable, was that change
  constrained or escalated to the user through `ask_before_reframe`?
- Does the Editorial Decision Frame and final draft serve the hypothesis while
  staying inside its confidence and respect boundary?
- Did the draft overreach beyond the hypothesis by adding advice, claims, or
  management conclusions not supported by the source?

If the Problem Hypothesis is missing, overconfident, speculative, or
adversarial, Review Agent should record a finding. Severity depends on impact:
non-critical if the final still serves the request; blocker if the route or
draft materially depends on an unsupported hypothesis.

## production files likely to change

Minimal implementation would touch:

- `ai-editorial-office/AGENTS.md`
  - add Problem Hypothesis to editorial entry discipline and lifecycle.
- `ai-editorial-office/agents/chief_editor.md`
  - add responsibility, inputs, decision boundary, forbidden overreach, and
    quality check for hypothesis formation.
- `ai-editorial-office/agents/review_agent.md`
  - add quality checks for hypothesis basis, confidence, respect boundary, and
    anti-consulting behavior.
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
  - add compact `## problem hypothesis` block after Preflight Gate.
- `ai-editorial-office/templates/artifacts/handoff_template.md`
  - add optional one-line `Problem hypothesis` in planning handoff.

Probably not needed in the first pass:

- `writer_agent.md`
- `ux_writer.md`

Reason: Writer Agent and UX Writer already consume `orchestration_plan.md`,
handoff, and the Editorial Decision Frame as contract. If later testing shows
they ignore the hypothesis boundary, add one sentence to each role. Do not edit
them preemptively.

## new artifacts

No new mandatory artifact is needed.

Do not create `problem_framing.md` or `problem_hypothesis.md` as a canonical
artifact. The Problem Hypothesis is small and belongs in
`orchestration_plan.md`.

Optional task-local analytical support may be created only when a specific
high-governance or complex task needs deeper problem analysis. That support
must not become a default artifact and must not replace the compact Problem
Hypothesis.

## why this does not break architecture

- It uses the existing Chief Editor authority.
- It lives in an existing artifact, `orchestration_plan.md`.
- It feeds the existing Editorial Decision Frame instead of replacing it.
- It adds reviewability without changing review-gate mechanics.
- It does not create a role, pipeline, status, or global new document.
- It remains compatible with simple tasks: when the stated request and
  hypothesis clearly align, the section can be one or two lines.
- It matches the source-bound philosophy by separating user-stated facts,
  source-backed signals, context inference, and confidence.
- It preserves user respect by requiring `Respect boundary` and by making
  `ask_before_reframe` mandatory when a reframe would materially change the
  task.

## implementation sketch

If approved, implement as a minimal production patch:

1. `AGENTS.md`: define Problem Hypothesis as a compact orchestration decision
   before Editorial Decision Frame.
2. `chief_editor.md`: require Chief Editor to identify user request, problem
   hypothesis, basis, confidence, respect boundary, and routing implication.
3. `orchestration_plan_template.md`: add the compact hypothesis block.
4. `handoff_template.md`: include a one-line problem hypothesis in planning
   handoff only when useful.
5. `review_agent.md`: require review of hypothesis language, basis,
   confidence, respect boundary, route alignment, and anti-consulting boundary.

## design self-check

- Minimal entities: pass.
- New roles: none.
- New mandatory documents: none.
- Duplicates Editorial Decision Frame: no; it precedes and informs it.
- Compatible with existing task types: yes.
- Source-bound philosophy: pass; the mechanism labels basis and confidence.
- Prevents false certainty: pass; the core field is a hypothesis, not a fact.
- Prevents arguing with user: yes, by requiring respect boundary and
  `ask_before_reframe` when the reframe materially changes the task.
