# Editorial Planning & Option Evaluation Framework

This file is the canonical owner for planning depth, option generation, option
evaluation, decision selection, recommendation formation, and planning
completion criteria in AI Editorial Office.

It prevents first-plausible convergence without creating a heavyweight planning
methodology. It is not a new workflow, role, scoring matrix, review gate,
template requirement, or replacement for the Editorial Decision Frame.

## Planning Objective

Planning exists to choose a credible approach before production, review, or
implementation locks onto one path.

Good planning answers:

- what viable options exist;
- which dimensions matter for this task;
- what evidence supports or weakens each option;
- what analytical question, hypotheses, assumptions, or contradictions shape
  the decision when reasoning complexity is material;
- why the selected option is best enough for now;
- what tradeoffs and uncertainty remain;
- when the decision should be reconsidered.

Do not generate fake alternatives. Two credible options are better than three
performative ones. Trivial tasks may need only a one-line route rationale.

## Planning Levels

Planning depth scales with task complexity and risk.

| Level | Use when | Minimum behavior | Avoid |
| --- | --- | --- | --- |
| `trivial` | The correct action is obvious, low-risk, reversible, and tightly scoped. | Name the route and why alternatives are unnecessary or obviously inferior. | Inventing artificial options. |
| `standard` | There are meaningful choices about approach, structure, implementation slice, evidence depth, or workflow. | Compare 2-3 credible options against relevant dimensions and choose one. | Long matrices, speculative future roadmaps. |
| `strategic` | The decision affects architecture, business direction, product behavior, governance, public claims, or long-term maintainability. | Compare credible options with evidence, risks, reversibility, maintenance cost, and reconsideration triggers. | Treating uncertainty as resolved or using planning to delay action. |

Escalate from `trivial` to `standard` when the first plausible option has
material downside, unclear evidence, or non-obvious alternatives. Escalate to
`strategic` when the decision has high-governance, architectural, business, or
long-lived consequences.

## Option Generation

Generate alternatives that could plausibly win under some valid priority.

Useful option families:

- implementation alternatives: small patch, broader refactor, adapter layer,
  no-code documentation/config change, staged migration;
- architectural alternatives: extend existing canon, create a new canonical
  owner, refactor ownership, leave behavior unchanged and document future work;
- workflow alternatives: compact path, expanded path, task-local mini-contract,
  return to an earlier lifecycle stage;
- product alternatives: minimal usable change, guided flow, stricter guardrail,
  defer until product evidence exists;
- research alternatives: no-research rationale, compact evidence, full
  evidence, source conversion first, user clarification first.

Avoid options that are strawmen, forbidden by canon, obviously inferior,
unsupported by evidence, or included only to make the chosen path look better.

## Evaluation Dimensions

Select only the dimensions that matter for the current task.

| Dimension | Question |
| --- | --- |
| User-goal alignment | Does this option directly serve the user's actual goal and deliverable? |
| Implementation complexity | How much work, coordination, or risk does implementation require? |
| Expected value | What useful outcome does this option produce now? |
| Technical risk | Could it break behavior, create maintenance debt, or hide edge cases? |
| Business or editorial risk | Could it mislead, overpromise, damage trust, or create governance exposure? |
| Evidence quality | Is the option supported by inspected sources, repository state, tests, or verified data? |
| Diagnostic value | Which evidence would actually distinguish this option from credible alternatives? |
| Reversibility | Can the decision be undone or adjusted cheaply if wrong? |
| Long-term maintainability | Does it simplify future work or create duplicated concepts? |
| Canon compatibility | Does it integrate with existing canonical owners instead of creating parallel architecture? |
| Reviewability | Can Review Agent validate the option and resulting artifacts without excessive context? |
| Time/value fit | Is this the right-sized next step for the current mission? |
| Audience/outcome fit | Does this option help the intended reader decide, act, review, implement, understand, or publish? |
| Reader journey fit | Does this option connect the reader's starting state to the required change in a learnable and usable sequence? |
| Quality-attribute fit | Which quality attributes does this option strengthen or weaken? |

The framework does not require numeric scores. A compact comparison table,
short bullets, or a paragraph is enough when it makes the tradeoff visible.

## Reader Journey Fit

For material reader-facing work, evaluate routes as learning or action paths,
not only as subject structures. A route should answer:

1. What does the reader know, believe, use, or misunderstand now?
2. What must change before the reader can understand, decide, or act?
3. Which sequence makes that change easiest without hiding evidence or
   complexity?
4. What can the reader do, explain, or decide after the artifact?

`Concept-first`, `chronology-first`, `product-first`, `problem-first`, and
`action-first` are possible routes, not defaults. Choose the one that best
serves the recorded reader journey and source boundary. If the request names a
stopping point such as "I last understood X", treat it as evidence for a bridge
from X rather than as incidental background.

Keep this judgment inside the existing option evaluation and Editorial
Decision Frame. Do not create a reader-journey framework, role, score, or
standalone artifact.

## Decision Selection

The selected option should be justified by evidence and task priorities, not by
being the first plausible idea.

Record, at the planning depth required:

- selected approach;
- why it best serves the task now;
- rejected alternatives and real rejection reasons;
- tradeoffs accepted;
- remaining uncertainty;
- evidence basis and confidence;
- future reconsideration triggers.

When a concrete reader starting point makes a short chronology, current
product bridge, or other less durable route materially more useful, Chief
Editor may record a Bounded Utility Tradeoff from
`/kb/editorial_quality_attributes.md`. It must name the bounded scope,
evidence/freshness basis, stale-if trigger, intentionally relaxed attribute,
expected reader benefit, and preserved non-relaxable guardrails. Convenience
or liveliness alone is not sufficient.

For tasks using an Editorial Decision Frame, keep the final planning result
inside that frame or in the smallest existing planning artifact. Do not create a
standalone planning file unless risk, review, restartability, or governance
needs it.

## Recommendation Formation

A recommendation should state:

- the selected option;
- the decision rule used, such as highest value, lowest risk, best canon fit,
  fastest safe implementation, or strongest evidence;
- what must happen next;
- what not to do now;
- what would change the recommendation later.

When evidence is weak, the recommendation should narrow, caveat, or request
evidence instead of pretending the option is settled.

## Planning Completion Criteria

Planning is complete when:

- the planning level fits task risk and complexity;
- credible alternatives were considered or intentionally not needed;
- evaluation dimensions are relevant, not decorative;
- the selected approach is justified;
- rejected alternatives are not strawmen;
- tradeoffs, uncertainty, and reconsideration triggers are visible when
  material;
- reader-facing route order is justified by the reader journey when reader
  change is material;
- any bounded utility tradeoff is explicit, evidence-backed, limited, and
  reviewable rather than an implicit exception;
- the next action is implementation, research, drafting, UX writing, review,
  repair, or governance rather than more abstract planning.

## Integration Points

### Task Object

Planning state is part of the task object when a decision has meaningful
alternatives: planning level, options considered, selected option, tradeoffs,
remaining uncertainty, and reconsideration triggers.

### Editorial Decision Frame

The Editorial Decision Frame records the chosen route and rejected alternatives.
This framework defines how to make those alternatives credible before the frame
is finalized.

When Product Intent Review mode is `limited` or `full`, the frame also receives
a compact decision transfer from `/kb/product_intent_review.md`: mode and focus,
product finding, one main product gap, evidence boundary, Chief Editor
production consequence and permission, owner decision required, and
reconsideration trigger. Detailed model rows, research narrative, alternatives,
and minimum validation design stay in the selected analytical artifact. The
product finding remains distinct from the existing operational review verdict.

### Editorial Challenge Lens

The Challenge Lens tests whether the assumptions that justified the selected
option still hold, and whether rejected alternatives became stronger.

### Evidence Framework

Option evaluation should use evidence quality and confidence labels from
`/kb/editorial_evidence_framework.md`. Weak evidence should reduce confidence,
not be hidden by a sharper recommendation.

### Analytical Reasoning

When planning depends on complex diagnosis, competing explanations, key
assumptions, contradictions, or sufficiency judgment, use
`/kb/analytical_reasoning.md` to keep those moves visible. Analytical reasoning
does not replace planning; it makes the question-to-option path easier to
review.

### Audience And Outcome Alignment

Option evaluation should use `/kb/audience_outcome_alignment.md` when reader or
outcome fit affects the route. A stronger option on paper may be rejected when
it is too broad, too shallow, too technical, or insufficiently actionable for
the intended audience.

### Quality Attributes

Option evaluation should use `/kb/editorial_quality_attributes.md` when options
optimize for different qualities, such as completeness vs brevity, elegance vs
implementation value, or traceability vs readability.

### Failure Modes

First-plausible convergence, canon duplication, scope drift, and
implementation-task dilution should trigger recovery through
`/kb/editorial_failure_modes.md`.

### Shared Lifecycle

Planning normally happens in routing and may be refreshed after research,
review findings, repair, or governance blockers. It does not create a separate
lifecycle.

## Codex Planning Guidance

For implementation tasks, the selected slice should follow from evaluated
options.

Before asking Codex to implement, confirm:

- why this repository slice is the next highest-value step;
- which alternatives were rejected, such as larger refactor, template-only
  change, future feature, or no-op;
- which files are in scope and out of scope;
- which validation proves the slice worked;
- what future work is intentionally deferred.

Avoid speculative future work. Prefer a small repository-aware implementation
that can be validated and reviewed.

## Non-Goals

This framework does not:

- require a planning artifact for every task;
- require numeric scoring;
- replace Chief Editor routing;
- replace the Editorial Decision Frame;
- replace evidence or review;
- create any new planning role;
- make trivial tasks heavier;
- justify endless exploration before implementation.
