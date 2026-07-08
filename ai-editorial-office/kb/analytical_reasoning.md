# Analytical Reasoning

This file owns practical analytical reasoning guidance for AI Editorial Office.
It distills professional reasoning practice into lightweight operational moves.

It is not a new role, pipeline, framework, review gate, workflow engine, scoring
model, or mandatory artifact set. Use it only when analytical complexity,
decision impact, evidence ambiguity, competing explanations, contradiction, or
review risk justifies making reasoning more visible.

## Purpose

Analytical reasoning makes the path from question to conclusion inspectable.
It helps agents:

- frame the right question before solving;
- decompose complex work into useful parts;
- generate and compare plausible explanations;
- separate facts, interpretations, assumptions, hypotheses, and judgments;
- seek disconfirming evidence;
- preserve contradictions and uncertainty;
- decide whether evidence is sufficient for the task risk;
- communicate conclusions without false precision.

## When To Use

Use analytical reasoning when any of these are material:

- the task asks for analysis, diagnosis, recommendation, strategy, architecture,
  research synthesis, risk judgment, or implementation direction;
- the first plausible answer may be wrong or incomplete;
- multiple explanations, routes, causes, or options could fit the facts;
- evidence is ambiguous, indirect, stale, incomplete, or contradictory;
- a conclusion depends on key assumptions;
- a recommendation or decision has meaningful consequence, irreversibility, or
  governance exposure;
- Review Agent needs to challenge reasoning, not only wording or source
  presence.

Do not use it to make trivial tasks heavier. Compact tasks may need only one
sentence naming the question, conclusion, and confidence.

## Core Analytical Moves

| Move | Purpose | Compact prompt |
| --- | --- | --- |
| Problem framing | Solve the right question. | What question must this answer, for whom, and for what decision or action? |
| Decomposition | Make the problem inspectable. | What are the main parts, drivers, constraints, or workstreams? |
| Hypothesis generation | Avoid first-answer lock-in. | What plausible explanations or routes could be true? |
| Competing explanation comparison | Test alternatives fairly. | Which evidence supports or weakens each explanation? |
| Key assumptions check | Expose linchpin premises. | What must be true for this conclusion to hold? |
| Disconfirmation | Reduce confirmation bias. | What evidence would make this conclusion unsafe? |
| Contradiction handling | Preserve conflict until resolved. | What conflicts, and is it source, timing, scope, definition, method, or incentive? |
| Diagnostic evidence check | Prefer evidence that separates alternatives. | Which evidence actually changes the answer? |
| Sufficiency judgment | Stop at the right confidence depth. | Is the evidence enough for this decision, risk, and reversibility? |
| Uncertainty communication | Keep readers from over-trusting. | What is known, assumed, unknown, contradicted, or still risky? |

## Good Analysis Criteria

Good analysis is:

- question-led, not source-led;
- explicit about scope and decision need;
- decomposed enough for review;
- open to more than one plausible explanation when alternatives matter;
- grounded in inspected evidence;
- clear about fact, interpretation, assumption, hypothesis, and judgment;
- honest about contradictions and missing evidence;
- calibrated in confidence;
- specific about what would change the conclusion;
- sufficient for the task risk without becoming unbounded research.

## Common Failure Modes

| Failure | Signal | Recovery |
| --- | --- | --- |
| Wrong question | Work is polished but answers the wrong problem. | Restate the analytical question and route back if material. |
| Premature closure | First plausible explanation becomes final. | Generate competing explanations or options. |
| Confirmation bias | Evidence only supports the favored answer. | Search for disconfirming evidence. |
| Unsupported recommendation | Action exceeds inspected evidence. | Downgrade, constrain, ask, or block. |
| Hidden assumption | Premise is treated as fact. | Name the assumption and validation needed. |
| Contradiction smoothing | Conflict disappears in prose. | Preserve the contradiction and classify its type. |
| False precision | Confidence or wording exceeds evidence. | Calibrate confidence and caveat scope. |
| Unbounded research | More collection replaces judgment. | Apply sufficiency criteria tied to decision risk. |
| Non-diagnostic evidence | Sources are true but do not distinguish options. | Identify evidence that would change the conclusion. |
| Decision hiding | Analysis quietly makes the decision. | Separate analyst judgment from decision owner choice. |

## Compact Analytical Pattern

Use this pattern inside the smallest existing artifact when reasoning should be
visible but the task does not need expanded analysis.

```markdown
## analytical reasoning
- analytical question:
- working conclusion:
- key evidence:
- assumptions:
- contradiction or uncertainty:
- confidence/sufficiency:
- what would change this:
```

For very compact tasks, the same pattern may be one paragraph.

## Expanded Analytical Pattern

Use this when analytical complexity, risk, ambiguity, or review need justifies
more detail inside an existing artifact such as `orchestration_plan.md`,
`research.md`, `review.md`, or a production note.

```markdown
## analytical reasoning
- analytical question:
- decomposition:
- hypotheses or explanations considered:
- diagnostic evidence:
- disconfirmation checks:
- key assumptions:
- contradictions:
- sufficiency judgment:
- uncertainty and residual risk:
- conclusion or recommendation:
- revision triggers:
```

Do not create a standalone analytical artifact; keep analytical notes inside
the existing artifact that already owns the relevant route, research, review, or
decision record.

## Stop Conditions

Stop, route repair, or block when:

- the analytical question is unclear and could change the result;
- only one plausible explanation was considered despite meaningful alternatives;
- a key assumption is unsafe, hidden, or untestable for the task risk;
- material contradictions are unresolved and affect the conclusion;
- evidence is non-diagnostic or too weak for the recommendation;
- confidence is inflated beyond evidence quality;
- the conclusion hides uncertainty the reader needs for action;
- research has become unbounded and no sufficiency judgment is visible;
- Review Agent cannot reconstruct how the conclusion was reached.

## Integration Notes

- `/kb/capability_registry.md` maps analytical reasoning as a reusable
  capability, not a role.
- `/kb/task_object_model.md` may expose optional analytical fields when they
  help restart, review, or governance.
- `/kb/editorial_evidence_framework.md` owns evidence classes and confidence
  labels used by analytical reasoning.
- `/kb/editorial_planning_framework.md` owns option evaluation and planning
  depth; analytical reasoning supplies the question, hypotheses, assumptions,
  contradiction handling, and sufficiency moves that support it.
- `/kb/editorial_failure_modes.md` owns recovery when reasoning failure appears.
- `review_pipeline.md` and `/agents/review_agent.md` own review-stage challenge
  behavior inside the existing review gate.
