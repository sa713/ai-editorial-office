# Professional Analysis

This file owns practical Professional Analysis guidance for AI Editorial
Office. It translates professional analytical practice into lightweight
decision-support lenses for structured interpretation, synthesis, judgment, and
recommendation work.

It is not a new role, framework, pipeline, lifecycle stage, review gate,
workflow engine, scoring model, consulting methodology, or mandatory artifact
set. Use it only when an artifact must turn complex information into a
decision-ready analytical product.

## Purpose

Professional Analysis helps agents produce clear analytical products that a
reader can use to understand a situation, compare options, decide, approve,
prioritize, challenge, or act.

It helps agents:

- define the analytical product and decision context;
- interpret complex information without losing source boundaries;
- synthesize evidence into decision-relevant findings;
- compare options, implications, risks, and tradeoffs;
- build recommendations that do not exceed the evidence;
- communicate analytical judgment with appropriate confidence and uncertainty;
- keep professional analysis inside the existing role, lifecycle, and review
  architecture.

## Relationship To Analytical Reasoning

Analytical Reasoning owns the cognitive moves: framing the question,
decomposing the problem, comparing explanations, testing assumptions, seeking
disconfirmation, preserving contradictions, judging sufficiency, and
communicating uncertainty.

Professional Analysis owns the analytical product shape: what kind of analysis
is needed, what decision it supports, how findings are synthesized, how options
and implications are presented, what recommendation is justified, and what the
reader can do next.

Use both when a professional analysis product depends on complex reasoning,
ambiguous evidence, competing explanations, contradiction, or high-consequence
judgment.

## Relationship To Existing Capabilities

- Evidence framework owns evidence classes, confidence labels, assumptions,
  unknowns, and validation needed.
- Planning framework owns planning depth, option generation, option evaluation,
  selected approach, tradeoffs, and reconsideration triggers.
- Audience and outcome alignment owns reader, decision, action, detail, tone,
  format, and usefulness fit.
- Quality attributes own task-specific quality priorities and tradeoffs.
- Architecture Review owns design-fitness assessment.
- Engineering Review owns implementation/change-safety assessment.
- Product Intent Review owns the conditional, evidence-bounded product-intent
  lens defined in `/kb/product_intent_review.md`. It is a narrow specialized
  lens inside the Professional Analysis family, not an expansion of this
  general contract.

Professional Analysis may consume these capabilities, but it does not replace
or become their owner.

This relationship note does not accept, release, broaden, or finalize the
current Professional Analysis release candidate.

## When To Use

Use Professional Analysis when a task asks for or materially depends on:

- structured analysis, assessment, synthesis, interpretation, or judgment;
- a recommendation, decision brief, options memo, strategy note, or analytical
  executive summary;
- business, product, policy, technology, market, operational, or organizational
  analysis;
- discovery work that must define the problem, needs, constraints,
  opportunities, and decision implications;
- synthesis across multiple sources, stakeholders, constraints, or evidence
  streams;
- evidence-backed conclusions where the reader must decide, approve,
  prioritize, challenge, or act.

Do not use Professional Analysis for ordinary summarization, copyediting,
low-risk factual lookup, simple markdown formatting, Architecture Review,
Engineering Review, or reasoning visibility by itself.

## Analysis Lenses

Select only the lenses that fit the task.

| Lens | Use when | Core questions |
| --- | --- | --- |
| Situation assessment | A reader needs to understand what is happening and why it matters. | What is the issue, context, evidence, uncertainty, and consequence? |
| Synthesis brief | Multiple evidence streams must be combined into usable findings. | What patterns, contradictions, and decision-relevant insights emerge? |
| Options and recommendation | A choice or priority decision is needed. | What options exist, how do they compare, and which is justified now? |
| Business or needs analysis | Value, stakeholder need, process, operating model, or change context matters. | What need or opportunity exists, for whom, and what outcome would create value? |
| Policy or impact analysis | Public, organizational, risk, governance, or stakeholder impact matters. | What effects, tradeoffs, constraints, distributional impacts, and risks matter? |
| Product discovery analysis | A product or service problem must be understood before solution commitment. | What user problem, context, constraint, opportunity, and success signal matter? |
| Technology assessment | A technology choice, implication, readiness, or risk must be evaluated. | What does the technology enable, what risks or limits exist, and what decision follows? |
| Executive decision brief | A time-limited decision-maker needs the usable conclusion first. | What is the bottom line, evidence level, recommendation, risk, and next decision? |

## Professional Analysis Pattern

Use this compact pattern inside the smallest existing artifact when
Professional Analysis is material:

```markdown
## professional analysis
- analytical product:
- decision or use context:
- audience and required action:
- scope and exclusions:
- evidence basis and confidence:
- synthesis:
- options or interpretations:
- implications and risks:
- recommendation or judgment:
- uncertainty and what would change this:
- next decision or action:
```

For a compact task, this may be one paragraph. Do not create a standalone
Professional Analysis artifact unless the selected task depth, review need, or
governance need justifies it.

## Good Professional Analysis Criteria

Good Professional Analysis is:

- decision-led rather than source-led;
- explicit about reader, purpose, and use context;
- clear about scope, exclusions, assumptions, and uncertainty;
- grounded in evidence with confidence calibrated to that evidence;
- synthetic rather than a loose collection of facts;
- balanced across credible options, implications, risks, and tradeoffs when a
  choice is involved;
- specific about what follows from the analysis;
- honest about what would change the conclusion;
- compact enough for the decision need and detailed enough for review.

## Stop Conditions

Stop, route repair, or block when:

- the decision or use context is unclear enough to change the product;
- the analysis answers a different problem from the one requested;
- synthesis is just summary and does not produce decision-relevant insight;
- options, criteria, implications, or risks are hidden when a recommendation is
  requested;
- the recommendation exceeds the evidence or hides material uncertainty;
- assumptions or stakeholder needs are treated as facts;
- a domain-specialist conclusion is needed but no source-backed domain evidence
  exists;
- Architecture Review or Engineering Review is required but the work is being
  handled only as general analysis;
- Review Agent cannot reconstruct the evidence, reasoning, recommendation, and
  residual risk.

## Completion Criteria

Professional Analysis is complete for a task when the reviewing role can state:

- what analytical product was needed;
- what decision, action, approval, or understanding it supports;
- what evidence basis and confidence support material conclusions;
- what synthesis or interpretation the analysis provides beyond summary;
- what options, implications, risks, tradeoffs, or recommendations are material;
- what uncertainty remains and what would change the conclusion;
- whether the correct outcome is `approved`, `changes_requested`, `blocked`, or
  escalation through the existing lifecycle.

## Non-Goals

Professional Analysis does not:

- create an Analyst, Consultant, Business Analyst, Policy Analyst, Product
  Strategist, Intelligence Analyst, or Technology Analyst role;
- create a new pipeline, lifecycle stage, review gate, checklist system,
  consulting framework, or mandatory artifact;
- replace Analytical Reasoning, evidence confidence, planning and option
  evaluation, audience/outcome alignment, quality attributes, Architecture
  Review, Engineering Review, or Review Agent;
- require professional analysis for ordinary editorial drafting or low-risk
  summaries;
- provide deep domain expertise without a domain pack or source-backed task
  evidence;
- make recommendations when the evidence supports only constrained findings,
  caveats, or a request for more information.
