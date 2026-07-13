# Task Need Recognition

This file owns the shared Task Need Recognition capability for AI Editorial
Office. It defines how available request evidence becomes an advisory view of
likely task needs before Chief Editor routing.

It does not own or perform selected-deliverable choice, task classification,
routing, preflight, risk mode, process depth, research depth, review scope,
capability activation, Domain Pack activation, role assignment, decomposition,
planning, lifecycle transition, or governance. Those decisions remain with
`AGENTS.md`, Chief Editor, and their existing canonical owners.

## Purpose

Task Need Recognition helps the office inspect a request before work begins and
answer, provisionally:

- what kind of work appears to be present;
- which deliverable would solve the user's real objective with the least
  unnecessary burden while preserving required depth, evidence, and use value;
- which capabilities are likely to matter;
- which Domain Packs may provide material context;
- how much research, evidence, and review may be justified;
- whether consequence, exposure, sensitivity, reversibility, or uncertainty
  suggests elevated risk for Chief Editor consideration;
- whether architecture, engineering, communication, analysis, or domain
  expertise is materially significant;
- what is ambiguous, contradictory, missing, uncertain, or out of scope;
- whether the request may contain several tasks with different owners,
  evidence, risk, or validation needs.

The capability improves the evidence available to Chief Editor. It never
replaces Chief Editor judgment.

## Relationship To Existing Owners

- Intake Normalization owns the faithful brief and the distinction between
  confirmed, inferred, unknown, assumption, and question.
- Chief Editor and Routing And Preflight own every actual route, activation,
  depth, role, split/sequence, and next-action decision.
- Preflight owns whether the task is understood enough to `ask`, `constrain`,
  `proceed`, or `block`; recognition may supply evidence but does not pass the
  gate.
- Editorial Evidence Framework owns evidence classes and confidence labels.
- Analytical Reasoning owns problem framing, decomposition reasoning,
  hypotheses, contradiction, disconfirmation, and sufficiency moves.
- Professional Analysis owns analytical product shape, synthesis, options,
  implications, judgment, and recommendation quality.
- Professional Communication owns message architecture, explanation fit,
  density, actionability, and caveat-preserving reader transfer.
- Architecture Review owns architectural drivers, scenarios, tradeoffs,
  assumptions, risks, evidence, and design-fitness judgment.
- Engineering Review owns changed-surface lenses, validation, findings, and
  residual implementation risk.
- Domain Knowledge Pack Standard and each active pack own pack activation
  criteria, boundaries, sources, stale-if triggers, and review questions.
- Evaluation Signals own optional views over saved system/release evidence for
  later human decisions; they do not classify a current request.

Task Need Recognition may point to these owners. It must not reproduce their
methods or make their decisions.

## When To Use

Use a compact recognition view when one or more are material:

- task type or dominant deliverable is not immediately obvious;
- multiple capability, domain, evidence, risk, or review needs may coexist;
- architecture, engineering, communication, analysis, or domain significance
  could alter the route;
- the request may be several tasks disguised as one;
- risk, research depth, evidence expectations, or review scope may be easy to
  under- or overestimate;
- ambiguity, contradiction, missing information, or out-of-scope content could
  change the route;
- Chief Editor or Review Agent needs an inspectable basis for a material route.

For a trivial, clear, low-risk request, one line or no separate recognition
section is sufficient. Do not make obvious work heavier merely to show use of
the capability.

## Evidence-First Recognition

Start from available evidence, not a keyword list:

| Signal family | Inspect | Advisory use |
| --- | --- | --- |
| Outcome and deliverable | requested action, reader outcome, artifact, acceptance cue | likely dominant task type and communication job |
| Work surface | prose, analysis, code/config, architecture boundary, product/UI, operational event, domain decision | likely capabilities and review concerns |
| Consequence and exposure | affected users/assets, publication, sensitivity, reversibility, blast radius, approval | risk and review-depth recommendation |
| Evidence state | supplied sources, novelty, volatility, factual claims, contradictions, missing data | research/evidence recommendation |
| Change significance | cross-owner/boundary effects, behavior change, quality attributes, hard-to-reverse commitment | likely Architecture Review or Engineering Review |
| Domain materiality | domain-specific assets, terms, risks, controls, models, delivery surfaces | likely primary/adjacent Domain Packs or task-specific research |
| Communication transfer | executive decision, recommendation/ask, technical explanation, stakeholder memo, dense evidence | likely Professional Communication |
| Analytical product | assessment, synthesis, options, implications, judgment, recommendation | likely Professional Analysis |
| Ambiguity and conflict | missing audience/output, mixed intents, incompatible constraints, contradictory evidence | clarification, constrain, uncertainty, or decomposition recommendation |
| Task structure | divergent deliverables, owners, evidence, risks, domains, validation paths, or sequencing dependencies | split, sequence, or keep-coherent recommendation |

## Outcome-First Deliverable Recommendation

Before Chief Editor selects a pipeline, recognition should answer the advisory
question:

> What is the smallest sufficient artifact that best solves the user's actual
> problem?

This is not permission to substitute a preferred format for the user's request.
Keep four values distinct whenever deliverable choice is material:

| Field | Meaning |
| --- | --- |
| Requested deliverable | The format or artifact named by the user, or `not specified`. |
| Format authority | `explicit`, `delegated`, `inferred`, or `unknown`; this describes who chose the format, not whether the format is good. |
| Recommended deliverable | The advisory artifact shape that best fits the outcome and use context. |
| Selected deliverable | The Chief Editor decision used for pipeline selection and production. |

Evaluate the recommendation from the outcome and use situation rather than a
format keyword alone:

- the problem the user is actually trying to solve;
- the decision, action, understanding, comparison, approval, implementation, or
  reuse the artifact must enable;
- the audience, channel, presentation context, time available, and expected
  depth;
- the minimum structure and evidence needed to make the result sufficient;
- reader/user effort, maintenance burden, and avoidable production bulk;
- whether the requested format is essential, explicit, only an example, safely
  inferred, or delegated to the office.

Possible recommendations include article, report, memo, executive brief,
checklist, roadmap, FAQ, decision matrix, comparison, presentation,
spreadsheet, specification, BRD, implementation plan, research report,
tutorial, reference, interview, dialogue, or mind map. This list is illustrative,
not a closed taxonomy and not a pipeline list.

Use these decision rules:

1. When the user explicitly requests a deliverable, recommend alternatives only
   when they add material value, and select the requested deliverable by default.
2. When the user delegates format choice, recommend and select the strongest
   outcome-fit deliverable, with a compact reason.
3. When format is inferred from the goal or use context, keep the inference
   visible and ask only if plausible formats would produce materially different
   outcomes or commitments.
4. When an explicit format appears unable to satisfy the stated outcome, do not
   replace it silently. Explain the mismatch and use Chief Editor preflight to
   `ask`, `constrain`, or preserve the requested deliverable with a clearly
   bounded alternative recommendation.
5. A vague verb such as `explain`, `help`, or `summarize` does not by itself
   justify a checklist, matrix, roadmap, or other compressed format. The
   recommendation must preserve the actual communication job.

The selected deliverable must be recorded before the selected pipeline. The
pipeline, mode, or mini-contract then follows the selected deliverable; it does
not retroactively decide what the deliverable should be.

Name negative evidence when it prevents unnecessary depth. For example, a
simple copyedit that happens to mention security terms has no security-sensitive
claim, asset, threat, control, behavior change, or review consequence and
should not trigger the Cybersecurity Domain Pack.

## Recognition Dimensions

### Task type

Recommend one likely primary task type when evidence supports it, plus material
secondary aspects. Do not force one exhaustive class when the request is mixed
or unclear.

Use the dominant outcome and deliverable before topic nouns. Examples include:

- editing or transformation;
- research or evidence synthesis;
- analysis, assessment, or recommendation;
- architecture review or design decision;
- engineering implementation or change review;
- UX/product communication;
- professional communication;
- domain-specific work;
- release/system update;
- mixed or decomposition candidate.

These examples are guidance, not a closed taxonomy or task status model.

### Capabilities

Recommend only capabilities whose materiality conditions appear present. Name
the evidence and the owner to consult. A recommendation does not activate the
capability.

Common distinctions:

- Analytical Reasoning when the question, explanations, assumptions,
  contradictions, or sufficiency need inspectability;
- Professional Analysis when the deliverable must synthesize evidence into
  decision-ready judgment or recommendation;
- Professional Communication when reader transfer, explanation, ask,
  technical precision, density, or actionability is material;
- Architecture Review when design fitness, boundaries, quality attributes,
  tradeoffs, or hard-to-reverse consequences are material;
- Engineering Review when code, configuration, automation, interface, runtime,
  data, reliability, performance, security, or validation surfaces change.

### Domain Packs

Recommend a pack only when its context could materially change evidence depth,
terminology, risk, review focus, or output quality.

- Name a likely primary pack when one domain dominates.
- Name adjacent packs only for distinct material surfaces.
- Recommend task-specific research when no accepted pack fits or a pack is
  stale/insufficient.
- Recommend no pack when evidence is mention-only or keyword-only.

Chief Editor confirms, rejects, or narrows all activation.

### Research and evidence

Recommend qualitative depth with a reason:

- `none or source-light`: transformation/editing with no material factual,
  product, policy, numeric, current-state, or domain claim;
- `compact`: bounded source/repository verification can answer the material
  question;
- `full`: conflicting or multiple evidence streams, high-governance claims,
  volatile behavior, domain-specific recommendations, architecture decisions,
  or high uncertainty.

These are advisory descriptions, not new process-depth values. Chief Editor
selects the actual evidence mode, process depth, and pipeline.

Evidence expectations may recommend source classes, current-state inspection,
tests, scenarios, measurements, or explicit caveats. They must not claim that
the evidence already exists when it has not been inspected.

### Risk and consequence

Recommend risk consideration from evidence such as affected people or assets,
sensitivity, external publication, security or safety exposure, legal/policy or
approval consequence, reversibility, blast radius, operational impact,
uncertainty, and the cost of a wrong result.

State what consequence is observed, what remains unknown, and why ordinary or
elevated risk may be plausible. Do not assign a risk mode, severity, priority,
score, threshold, or approval. Risk modes remain owned by `AGENTS.md`; Chief
Editor confirms the task-specific risk mode.

### Review

Recommend qualitative review scope with a reason:

- `focused`: clear, low-risk, source-light work with one bounded deliverable;
- `standard`: factual or implementation surface with ordinary consequence and
  bounded evidence;
- `deep`: high-governance, architecture-significant, cross-domain,
  security-sensitive, source-conflicted, hard-to-reverse, multi-deliverable, or
  highly uncertain work.

These labels do not create a review level, status, gate, or automatic selection.
Review remains mandatory under current canon; Chief Editor selects scope and
Review Agent determines the verdict.

### Significance

Recommend Architecture Review when evidence points to cross-owner/interface/
data/lifecycle/canon boundaries, material quality attributes, design tradeoffs,
architecture risk, or hard-to-reverse commitments.

Recommend Engineering Review when code, scripts, tests, validators,
configuration, dependencies, automation, interfaces, runtime, data,
reliability, observability, performance, security-sensitive behavior, or
validation evidence is material.

Recommend Professional Communication when the artifact must support an
executive decision, recommendation/ask, policy/stakeholder use, technical
implementation, dense evidence transfer, or multiple reader depths.

The named capabilities remain the significance and quality owners.

### Ambiguity and uncertainty

Do not hide:

- missing audience, deliverable, source, success, or approval information;
- several plausible task types or pack choices;
- conflicting instructions or evidence;
- unsupported or out-of-scope needs;
- assumptions that could change risk or route;
- low-confidence inference caused by topic-only language.

Recommend the smallest safe next move: ask, constrain, inspect, research,
decompose, proceed with caveat, or hand the uncertainty to Chief Editor. Only
Chief Editor makes the Preflight or routing decision.

### Decomposition

Recommend split or sequencing when parts of a request have materially different:

- deliverables or audiences;
- owners or role/capability needs;
- source boundaries or evidence bases;
- risk or approval requirements;
- primary domains;
- lifecycle or validation paths;
- prerequisite relationships.

Do not recommend decomposition merely because a request contains many bullets,
technologies, keywords, capabilities, or packs. A coherent decision packet may
remain one task.

## Compact Advisory View

Record the smallest useful view in `brief.md`, `orchestration_plan.md`, or
`task-manifest.md` when material:

```markdown
## task need recognition
- observed request signals:
- requested deliverable:
- format authority: explicit / delegated / inferred / unknown
- recommended deliverable and outcome-fit reason:
- likely primary task type:
- material secondary aspects:
- likely capabilities and why:
- likely Domain Packs and why:
- research / evidence recommendation:
- risk / consequence recommendation:
- review recommendation:
- architecture / engineering / communication significance:
- ambiguity, contradiction, or missing information:
- decomposition recommendation:
- confidence and negative evidence:
- explicit non-decision:
- Chief Editor deliverable decision: respect_requested / select_recommended /
  ask_before_change / constrain_with_explanation
- selected deliverable:
- Chief Editor routing decision or next question:
```

Separate observed signals from recommendations. Record the Chief Editor
decision in the same or another existing routing artifact when the view is
material. For compact work, combine or omit fields that add no decision value.

## Evidence And Confidence

- Use evidence classes and confidence labels from
  `/kb/editorial_evidence_framework.md`.
- Confidence describes the support for the recommendation, not a probability
  that should trigger action.
- Keyword/topic evidence alone normally supports only a question or weak
  hypothesis.
- Negative evidence and plausible alternatives reduce over-activation.
- When evidence is insufficient, use `plausible`, `speculative`, or
  `unsupported` and narrow the recommendation.
- Do not create numeric confidence, complexity, risk, priority, or routing
  scores.

## Role Cooperation

| Role | Responsibility |
| --- | --- |
| Intake Agent | Capture observed request evidence, requested deliverable, format authority, and the initial advisory view when material; do not select the deliverable, route, or activate. |
| Chief Editor | Challenge evidence, accept/reject/narrow recommendations, select the deliverable before the pipeline, make every routing/preflight/activation/depth/decomposition decision, and record the result. |
| Research Agent | Verify missing domain/current-state evidence when assigned; do not retroactively present research as an intake decision. |
| Writer Agent / UX Writer | Follow the approved route; flag new evidence that invalidates the recognition assumptions. |
| Review Agent | When downstream scope materially depends on recognition, challenge evidence, negative cases, proportionality, uncertainty, owner boundaries, and non-decision. |
| Final Editor | Preserve approved boundaries and caveats; do not reclassify the task. |

No Task Router, Classifier, Triage Agent, Analyst, Domain Selector, or Review
Level Selector role is created.

## Review Questions

When recognition materially affected the route, Review Agent may ask:

- Are observed signals separated from inference, recommendation, and Chief
  Editor decision?
- Are requested, recommended, and selected deliverables distinct, and is format
  authority recorded?
- Does the recommended deliverable minimize avoidable burden while remaining
  sufficient for the intended outcome, use context, and evidence need?
- Was an explicit requested deliverable preserved unless the user agreed to a
  change, or was any unresolved mismatch routed through preflight rather than
  silently overridden?
- Was the pipeline chosen after and because of the selected deliverable?
- Does the primary task type follow outcome/work surface rather than keywords?
- Are material secondary aspects preserved without forcing one class?
- Are capability and pack recommendations tied to their actual owner criteria?
- Is negative evidence visible where it prevents unnecessary activation?
- Are research, evidence, and review recommendations proportionate?
- Is risk/consequence advice tied to actual exposure, sensitivity,
  reversibility, uncertainty, or wrong-result cost rather than topic words?
- Are ambiguity, contradictions, missing information, and uncertainty honest?
- Is decomposition supported by divergent deliverables, owners, evidence,
  risk, domains, validation, or sequencing?
- Did Chief Editor make the route decision rather than rubber-stamp the view?
- Did any recommendation trigger an automatic action, score, threshold, or new
  gate?

## Stop Conditions

Stop, narrow, or return to Chief Editor when:

- the request cannot be distinguished from a different plausible task without
  material clarification;
- a recommendation depends only on keywords or topic names;
- requested and recommended deliverables have been silently merged;
- an explicit requested format would be replaced without user agreement or a
  visible preflight decision;
- the proposed artifact is smaller but no longer sufficient for the outcome;
- a Domain Pack/capability owner would be overridden;
- the view hides contradictory or negative evidence;
- a score, threshold, or classifier output is being treated as authority;
- decomposition would change user scope without Chief Editor decision;
- recognition is being used as automatic routing, activation, depth selection,
  planning, approval, or lifecycle transition;
- the view makes a simple task materially heavier without decision value.

## Non-Goals

Task Need Recognition does not:

- create automatic routing, classification, capability activation, Domain Pack
  activation, review level, research level, or planning;
- silently override an explicit requested deliverable or treat a recommendation
  as user consent;
- create a role, pipeline, lifecycle stage, status, gate, task taxonomy,
  framework, store, model, classifier, score, threshold, or dashboard;
- make selected-deliverable, task type, risk, depth, pack, capability, split, or
  next-action decisions;
- replace Preflight, Intake Normalization, Professional Analysis, Professional
  Communication, Architecture Review, Engineering Review, Evaluation Signals,
  Evidence Confidence, Domain Pack activation, Review Agent, or Chief Editor;
- require a standalone artifact or a recognition section for every task;
- treat synthetic validation as proof of real-world system improvement.
