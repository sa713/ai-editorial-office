# Professional Communication Architecture Synthesis

Date: 2026-07-09

## Executive Decision

Implement `Professional Communication` as one bounded shared capability.

It should help existing roles shape and review how meaning, evidence,
recommendations, explanations, decisions, and next actions are transferred to a
professional reader.

It must not become a new role, pipeline, lifecycle stage, review gate,
mandatory artifact, grammar/style checklist, consulting framework, content
design framework, UX writing framework, or duplicate owner of existing canon.

## Architecture Fit

The current architecture can absorb Professional Communication without redesign:

```text
task object first;
capability map second;
roles as accountability wrappers;
workflows and pipelines as execution guidance;
artifacts as views over task state.
```

Professional Communication fits as a capability in the capability registry and
as a KB owner under `/kb/professional_communication.md`.

The capability can be selected by Chief Editor, used by Research Agent, Writer
Agent, UX Writer, Review Agent, and Final Editor when communication quality is
material, and challenged inside the existing review gate.

No architecture changes are required.

## What Belongs Inside Professional Communication

Professional Communication owns practical guidance for communication transfer
quality:

- message architecture and information hierarchy;
- reader path and communication structure;
- decision-first and recommendation presentation;
- executive communication shape;
- technical communication shape;
- explanation fit for reader expertise and task;
- information density, compression, and layered detail;
- actionability of asks, recommendations, decisions, and next steps;
- preservation of evidence, confidence, caveats, assumptions, uncertainty, and
  residual risk during communication;
- communication review challenge when an artifact is correct but does not
  transfer understanding, decision, or action reliably.

It should provide optional lenses, not mandatory forms:

- executive brief;
- technical explanation;
- recommendation or ask;
- policy or stakeholder memo;
- research or evidence communication;
- implementation handoff;
- multi-audience layered communication.

## What Already Belongs To Writer Agent

Writer Agent remains accountable for drafting ordinary editorial, social,
article, email, memo, and other prose artifacts inside an approved route.

Writer Agent owns:

- turning approved scope, evidence, and route into a draft;
- applying editorial standards and tone;
- preserving approved structure, claims, caveats, and route decisions in the
  draft;
- repairing draft findings after review;
- not self-approving.

Professional Communication does not make Writer Agent optional and does not
create a second drafting owner.

## What Already Belongs To UX Writer

UX Writer remains accountable for product-facing copy, interface text, states,
terminology, accessibility, and product-truth preservation.

Professional Communication may help a UX artifact preserve action path,
evidence caveats, or message structure, but UX Writer and UX writing canon own
the actual product-copy craft.

Professional Communication must not become a product-copy or microcopy
framework.

## What Already Belongs To Audience And Outcome Alignment

`/kb/audience_outcome_alignment.md` owns:

- audience identification;
- intended outcome;
- reader context;
- required decision or action;
- detail, tone, and format fit;
- artifact success criteria;
- mismatch warning signs and correction patterns.

Professional Communication consumes this context. It does not redefine it.

Boundary:

```text
Audience Alignment decides who the reader is and what the artifact must enable.
Professional Communication decides how the message is structured, layered,
compressed, and presented so that transfer succeeds.
```

## What Already Belongs To Quality Attributes

`/kb/editorial_quality_attributes.md` owns:

- quality vocabulary;
- quality priorities;
- accepted tradeoffs;
- preservation of quality across lifecycle;
- review vocabulary for quality findings.

Professional Communication may improve clarity, actionability, audience fit,
structural coherence, reviewability, and precision, but it does not own those
quality attributes as a model.

Boundary:

```text
Quality Attributes says which qualities matter and what tradeoffs are accepted.
Professional Communication applies communication moves that preserve those
qualities in the artifact's reader path.
```

## What Already Belongs To Analytical Reasoning

`/kb/analytical_reasoning.md` owns reasoning moves:

- problem framing;
- decomposition;
- hypotheses and competing explanations;
- assumptions;
- disconfirmation;
- contradiction handling;
- sufficiency judgment;
- uncertainty communication as reasoning visibility.

Professional Communication does not own how conclusions are reasoned. It owns
how a supported conclusion, uncertainty, and reasoning cues are communicated to
the reader.

Boundary:

```text
Analytical Reasoning makes the reasoning inspectable.
Professional Communication makes the resulting explanation, conclusion, and
uncertainty transferable.
```

## What Already Belongs To Professional Analysis

`/kb/professional_analysis.md` owns analytical product shape:

- structured interpretation;
- synthesis;
- options;
- implications;
- tradeoffs;
- recommendation building;
- analytical judgment;
- decision-ready analytical communication.

Professional Communication must not decide whether a recommendation is
justified. It may decide how the justified recommendation is presented to a
reader: bottom line, evidence level, action path, caveats, implementation, and
next decision.

Boundary:

```text
Professional Analysis determines the analytical product and justified
recommendation.
Professional Communication determines the communication path that lets the
reader use that product without meaning or evidence loss.
```

## What Already Belongs To Evidence Framework

`/kb/editorial_evidence_framework.md` owns evidence classes, confidence labels,
source basis, assumptions, unknowns, validation needed, and residual risk.

Professional Communication may require those cues to be visible when the
reader's trust or decision depends on them. It does not define evidence classes
or confidence labels.

## What Already Belongs To Review Gate

Review gate authority remains with `AGENTS.md`, role specs, and
`/pipelines/review_pipeline.md`.

Professional Communication adds a review lens inside existing `review.md`.

It does not create:

- second review gate;
- communication reviewer role;
- mandatory communication checklist;
- communication approval state.

## What Remains Existing Behavior

The release preserves these existing behaviors:

- Chief Editor routes and selects active capabilities.
- Research Agent supports evidence when needed.
- Writer Agent and UX Writer produce artifacts in approved scope.
- Review Agent independently challenges material issues.
- Final Editor preserves approved meaning, caveats, and actionability during
  finalization.
- Review remains mandatory before finalization.
- Artifacts remain minimal and task-local.
- Gates are recorded in existing artifacts, not new mandatory standalone files.

## What Should Be Postponed

Postpone:

- oral presentations, speechwriting, facilitation, negotiation, and live
  stakeholder communication;
- crisis communication, media relations, PR strategy, and campaign management;
- brand voice systems beyond existing client profiles and tone guidance;
- deep accessibility or localization framework beyond existing UX and
  plain-language guidance;
- automated readability scoring;
- mandatory communication templates;
- a communication QA role;
- domain-specific communication packs for legal, medical, finance, security,
  or regulatory work without separate source-backed domain packs;
- broad consulting methodology or Pyramid-Principle canon.

These may be useful later, but they are not needed for S3.R5 and would increase
architecture weight.

## Implementation Decision

Create `ai-editorial-office/kb/professional_communication.md` as the canonical
owner for practical Professional Communication guidance.

Integrate lightly with:

- `AGENTS.md` canonical ownership map and entry-discipline triggers;
- `kb/00_index.md`;
- `kb/capability_registry.md`;
- `kb/shared_lifecycle_kernel.md`;
- `kb/task_object_model.md`;
- `agents/chief_editor.md`;
- `agents/review_agent.md`;
- `agents/writer_agent.md`;
- `agents/final_editor.md`;
- `pipelines/review_pipeline.md`;
- `project-state.md`;
- `BACKLOG.md`;
- `/about` copies and compact memory summaries if copied canonical files
  change;
- manual smoke-test examples.

## Activation Rule

Activate Professional Communication when the task materially depends on the
reader's ability to:

- understand a complex explanation;
- decide, approve, prioritize, or challenge;
- act on a recommendation;
- implement or review technical work;
- use a research/evidence summary without over-trusting it;
- navigate a multi-audience or layered artifact;
- preserve meaning, evidence, caveats, and next action during compression.

Do not activate it for:

- simple grammar cleanup;
- ordinary style polish;
- low-risk rewriting where audience/outcome is already sufficient;
- UX microcopy where UX Writer guidance is enough;
- analytical recommendation building without a communication-transfer problem;
- evidence assessment without a reader-transfer problem.

## Canonical Change Scope

Expected canonical changes are small:

- one new KB owner;
- capability registry entry and role-capability mapping updates;
- lifecycle and task-object references;
- role-spec references for routing, production preservation, review challenge,
  and finalization preservation;
- review pipeline references.

No script or validator changes are required.

## Architecture Risk Assessment

| Risk | Assessment | Mitigation |
| --- | --- | --- |
| Duplicates Audience Alignment | medium | State explicit consumption boundary: reader/outcome owned elsewhere. |
| Duplicates Writer Agent | medium | Define capability as shared transfer guidance, not drafting ownership. |
| Duplicates UX Writer | low-medium | Limit to communication transfer; product copy remains UX Writer. |
| Duplicates Quality Attributes | low-medium | Keep quality vocabulary and tradeoffs in quality framework. |
| Duplicates Professional Analysis | medium | Separate recommendation justification from recommendation presentation. |
| Becomes grammar/style checklist | medium | Make grammar/style non-goals and activation materiality-based. |
| Creates artifact sprawl | low | No mandatory standalone Professional Communication artifact. |

## Release Candidate Acceptance Basis

S3.R5 is ready for Project Lead review when:

- `professional_communication.md` exists and is discoverable;
- adjacent ownership boundaries are explicit;
- role and lifecycle integration is minimal and coherent;
- review challenge is inside existing `review.md`;
- smoke tests cover activation and non-activation;
- validation passes;
- `/about` is synchronized if copied files changed;
- release report and release pack are complete.
