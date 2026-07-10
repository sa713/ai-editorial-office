# Task Need Recognition Architecture Synthesis

Date: 2026-07-10

Release: `S5.R4 - Task Need Recognition`

## Decision

Implement Task Need Recognition as one bounded shared advisory capability with
a concise canonical owner at `kb/task_need_recognition.md`.

The capability turns available request evidence into a compact, inspectable
view of likely task needs. Intake Agent normally assembles the initial view;
Chief Editor challenges it and makes every actual routing decision; Review
Agent challenges recognition only when downstream work materially depends on
it.

```text
raw request and available evidence
-> observed recognition signals
-> advisory recommendations, negative evidence, ambiguity, and uncertainty
-> Chief Editor challenge and decision
-> existing routing, preflight, capability, Domain Pack, depth, and review owners
```

No classifier, score, router, role, pipeline, lifecycle stage, review gate,
task status, mandatory artifact, automatic activation, or autonomous planning
is introduced.

## Architecture question

What is the smallest addition that helps the office recognize task nature and
likely needs before work begins without duplicating Chief Editor routing,
Professional Analysis, Evaluation Signals, capability owners, Domain Pack
activation, or Preflight?

## Why a distinct bounded capability is justified

Current canon owns all decisions and most component signals, but no owner
defines the cross-owner contract that converts raw-request evidence into a
non-decisional view of likely task needs.

- Intake Normalization records confirmed, inferred, unknown, assumption, and
  question state, but it does not define a consistent cross-capability need
  view.
- Routing And Preflight owns decisions, not the evidence-to-recommendation
  pattern that Chief Editor can challenge.
- Individual capability and Domain Pack files define their own activation
  boundaries, but none explains how a request should combine several likely
  needs while preserving negative evidence and uncertainty.
- Evaluation Signals operate over saved task/release evidence for later human
  decisions, not live request intake.

Putting the entire contract into `capability_registry.md` would turn the
registry into an operational handbook. Duplicating the signals across Intake
Agent, Chief Editor, Review Agent, templates, and packs would create several
owners. One small canonical capability file plus concise role/template
consequences is the lowest-duplication design.

## Architectural drivers

- Authority: Chief Editor must retain task type, route, risk, depth,
  capability, role, Domain Pack, planning, preflight, and next-action decisions.
- Proportionality: simple tasks must stay simple even when their text contains
  technical or domain keywords.
- Reviewability: a reviewer must be able to see why a recommendation was made,
  what evidence weakens it, and what remained uncertain.
- Multi-label reality: a task may legitimately require analysis, architecture,
  engineering, communication, and multiple packs.
- Evidence discipline: recommendations must distinguish observed evidence,
  inference, assumption, contradiction, and unknown.
- Maintainability: signal definitions should point to existing owners instead
  of copying capability/pack methods.
- No automation authority: recommendations must not perform state change or
  activation.

## Quality-attribute scenarios

### Authority safety

- Stimulus: Intake recommends AI Engineering and deep review.
- Affected surface: task recognition view and orchestration.
- Expected response: Chief Editor can accept, reject, narrow, or override each
  recommendation with recorded rationale; no activation occurs automatically.
- Evidence: separate recommendation and Chief Editor decision fields.

### Proportionality

- Stimulus: a simple copyedit mentions architecture, AI, and security terms.
- Affected surface: task type, capabilities, packs, research/review depth.
- Expected response: recognition classifies the work as simple editing,
  records negative evidence for domain/significance triggers, and recommends
  no unnecessary pack/research expansion.
- Evidence: keyword-only negative scenario passes.

### Reviewability

- Stimulus: a mixed request appears to need engineering and policy analysis.
- Affected surface: decomposition and capability recommendations.
- Expected response: the view names divergent deliverables/evidence/owners,
  uncertainty, and a split-or-sequence recommendation; Chief Editor decides.
- Evidence: case record exposes observed signals and decision boundary.

### Maintainability

- Stimulus: a new capability or Domain Pack is accepted later.
- Affected surface: recognition guidance.
- Expected response: its own owner defines activation/materiality; Task Need
  Recognition points to that owner and does not grow a copied trigger list.
- Evidence: owner-reference rules and no keyword matrix.

## Ownership map

| Concern | Canonical owner retained | S5.R4 consequence |
| --- | --- | --- |
| Raw-request normalization | `agents/intake_agent.md`, Intake Normalization record | Intake produces observed signals and initial advisory view when material. |
| Task Need Recognition contract | new `kb/task_need_recognition.md` | Owns signal families, advisory view, uncertainty, negative evidence, decomposition recommendation, and non-decision boundary. |
| Task type, pipeline/mode, risk, process/review depth, capabilities, roles, packs, next action | `AGENTS.md`, Chief Editor, Routing And Preflight | Chief Editor decides; recognition supplies evidence only. |
| Preflight ask/constrain/proceed/block | `AGENTS.md` and existing Preflight Gate | Recognition may expose ambiguity/evidence gaps; it never decides start readiness. |
| Evidence classes and confidence | `kb/editorial_evidence_framework.md` | Recognition reuses labels and never adds probabilities/scores. |
| Analytical product and recommendation quality | `kb/professional_analysis.md` | Recognition may recommend Professional Analysis; it does not perform analysis or make recommendations about the task subject. |
| Saved system/release evidence view | `kb/editorial_learning_framework.md` Evaluation Signals | No change of owner or live-routing reuse; S5.R4 mirrors only observation/interpretation/decision separation. |
| Architecture significance | `kb/architecture_review.md` | Recognition points to likely materiality; Architecture Review owns drivers/scenarios/tradeoffs. |
| Engineering significance | `kb/engineering_review.md` | Recognition points to changed surfaces; Engineering Review owns lenses/findings/validation. |
| Communication significance | `kb/professional_communication.md` | Recognition points to a material communication job; the capability owns message design. |
| Research evidence and depth | Evidence Framework, Research Pipeline, Chief Editor | Recognition recommends depth; Chief Editor selects it and Research Agent executes it. |
| Review outcome and challenge | Review Agent and Review Pipeline | Review may challenge recognition-dependent scope inside the existing gate. |
| Domain Pack activation | `kb/domain_knowledge_pack_standard.md` and each pack | Recognition recommends likely primary/adjacent packs; Chief Editor activates or rejects. |
| Task fields/artifact views | `kb/task_object_model.md` | Existing fields carry recognition; no new required task-object field. |
| Risk mode | `AGENTS.md` | Recognition reports consequence/exposure signals; Intake proposes and Chief Editor decides risk mode. |

## What belongs to Task Need Recognition

Task Need Recognition owns only the reusable request-to-need advisory pattern:

- evidence-first recognition from requested outcome, deliverable, audience,
  work surface, consequence, source state, affected boundaries, domain
  materiality, ambiguity, and task structure;
- dominant task type plus material secondary aspects;
- likely capabilities and likely primary/adjacent Domain Packs;
- qualitative research, review, and evidence-depth recommendations;
- likely architectural, engineering, communication, analytical, and
  domain-specific significance;
- ambiguity, contradiction, uncertainty, missing information, and negative
  evidence;
- whether decomposition, sequencing, or a coherent single task appears safer;
- explicit non-decision and Chief Editor handoff.

It does not own the full content or method of any recommended capability/pack.

## What remains with Chief Editor

Chief Editor continues to decide:

- confirmed task type and primary deliverable;
- pipeline, editorial mode, or mini-contract;
- risk mode, process depth, execution profile, research depth, and review
  scope;
- active capabilities, roles, client profile, and Domain Packs;
- whether to ask, constrain, proceed, block, split, sequence, or keep one task;
- planning level, options, Editorial Decision Frame, next owner, and next
  action;
- whether recognition is unnecessary for a trivial task;
- all governance and final readiness decisions.

The Chief Editor must inspect request evidence rather than rubber-stamp the
view.

## What remains with Professional Analysis

Professional Analysis begins when a task needs structured interpretation,
synthesis, options, implications, judgment, or a decision-ready
recommendation. It owns the analytical product shape and recommendation
quality.

Task Need Recognition may say “Professional Analysis likely material because
the request asks for an evidence-backed options recommendation.” It must not
perform that analysis, choose an option, or duplicate the Professional
Analysis lenses.

## What remains with Evaluation Signals

Evaluation Signals assemble material saved evidence for a Project Lead,
review, governance, or canonical-owner decision. They are post-observation
views over tasks/releases and can support future evaluation of whether S5.R4
helps.

Task Need Recognition operates on the current request before routing. It does
not use Evaluation Signal records as a new routing system, does not create
activation telemetry, and does not claim that synthetic validation proves
improvement.

The shared structural principle is only:

```text
evidence -> bounded interpretation/recommendation -> accountable human decision
```

## What remains with Domain Pack activation

The Domain Knowledge Pack Standard continues to decide the activation
contract: context must materially change evidence depth, terminology, risk,
review focus, or output quality. Each pack owns its domain boundary, sources,
stale-if triggers, and non-activation criteria.

Recognition may recommend:

- a likely primary pack;
- one or more adjacent packs;
- task-specific research instead of a pack;
- no pack because mention-only/keyword-only evidence is insufficient.

Only Chief Editor activates, rejects, or narrows the pack set.

## Significance boundaries

### Architectural significance

Recognition signals:

- cross-owner/interface/data/dependency/lifecycle/canon boundary;
- material quality-attribute effect;
- hard-to-reverse commitment;
- design alternatives/tradeoffs or architecture-risk exposure.

Architecture Review owns the actual drivers, scenarios, tradeoffs, evidence,
and judgment.

### Engineering significance

Recognition signals:

- code, script, test, validator, configuration, dependency, automation,
  interface, runtime, data, reliability, observability, performance, or secure
  delivery change;
- required execution/validation evidence;
- possible implementation risk.

Engineering Review owns lenses, findings, validation sufficiency, and residual
risk.

### Communication significance

Recognition signals:

- executive decision/approval brief;
- recommendation or ask;
- policy/stakeholder memo;
- technical explanation or implementation handoff;
- dense evidence that must preserve caveats;
- multi-audience/layered transfer.

Professional Communication owns message architecture, density, explanation,
actionability, caveat preservation, and reader path.

### Analytical significance

Recognition signals:

- structured assessment/synthesis;
- options and recommendation;
- multiple evidence streams;
- implications, judgment, or decision support.

Professional Analysis owns the analytical product; Analytical Reasoning owns
framing, hypotheses, disconfirmation, contradiction, and sufficiency moves.

## Compact advisory view

Use only when the request is not already trivial and obvious or when routing,
risk, capability, Domain Pack, evidence, ambiguity, or decomposition may be
material.

```markdown
## task need recognition
- observed request signals:
- likely primary task type:
- material secondary aspects:
- likely capabilities and why:
- likely Domain Packs and why:
- research / evidence recommendation:
- review recommendation:
- architecture / engineering / communication significance:
- ambiguity, contradiction, or missing information:
- decomposition recommendation:
- confidence and negative evidence:
- explicit non-decision:
- Chief Editor decision or next question:
```

This is a conditional section in `brief.md`, `orchestration_plan.md`, or
`task-manifest.md`, not a mandatory artifact or checklist. For simple work it
may be one line or omitted.

## Recognition rules

1. Start from intended outcome, deliverable, work surface, consequence,
   evidence state, and affected boundaries.
2. Separate observed evidence from inference and recommendation.
3. Prefer multi-label recognition over forcing one exhaustive class, but name
   one dominant task type when evidence supports it.
4. Require material domain surfaces, not keywords, before recommending a pack.
5. State negative evidence that prevents unnecessary depth.
6. Use qualitative depth language with rationale; never score or select depth.
7. Preserve ambiguity, contradiction, missing information, and out-of-scope
   conditions.
8. Recommend decomposition only when deliverables, owners, evidence, risks,
   domains, or validation paths diverge materially.
9. Hand all decisions to Chief Editor and record any override when material.

## Manual and advisory boundaries

Must remain manual and Chief Editor-owned:

- final task classification;
- all pipeline/mode/role/capability/pack activation;
- risk and depth selection;
- preflight decision;
- decomposition/scope change;
- planning and next-action commitment;
- review outcome and final governance.

May remain advisory:

- observed signal summary;
- likely primary/secondary task nature;
- likely capabilities/packs;
- qualitative evidence/research/review needs;
- significance, ambiguity, uncertainty, and decomposition recommendation;
- request for clarification or safe narrowing.

May be automated only through a future separately reviewed mission, and not by
S5.R4:

- collection or formatting of already available facts for human inspection.

No future automation authority is implied by this release.

## Canonical implementation surface

Required canonical changes:

- add `kb/task_need_recognition.md` as the signal/recommendation owner;
- add it to the `AGENTS.md` ownership map and architecture references;
- register the capability and role mapping in `kb/capability_registry.md`;
- clarify conditional task-artifact integration in `kb/task_object_model.md`
  and `kb/shared_lifecycle_kernel.md` without new fields/stages;
- update Intake Agent, Chief Editor, and Review Agent consequences;
- add a conditional compact view to the orchestration-plan template;
- update Review Pipeline and KB index for discoverability/challenge;
- add representative validation, release state, memory disposition, and
  release documentation.

No change is justified to task statuses, pipeline sequence, Domain Pack files,
Professional Analysis, Professional Communication, Architecture Review,
Engineering Review, Evidence Framework, or Evaluation Signals owners.

## Alternatives rejected

### Extend only Preflight

Rejected because Preflight answers whether production can safely start. Task
Need Recognition answers what work appears present and what may be needed.
They are linked but distinct; merging them would overload the gate and hide the
recommendation/decision boundary.

### Extend only Intake Agent

Rejected because role text would become the de facto canonical owner and the
Chief Editor/Review consequences would be duplicated without a shared
contract.

### Put the full contract in Capability Registry

Rejected because the registry should name capabilities and role mappings, not
own a long operational method.

### New classifier/router service

Rejected because it would introduce automatic routing, thresholds, training,
evaluation, runtime authority, and maintenance unsupported by the mission.

### New task-recognition artifact

Rejected because current task artifacts already expose every needed field and
a separate file would become process weight.

## Validation design

Validate ten cases against a stable record:

- observed signals;
- primary and secondary task nature;
- likely capabilities and packs;
- research/evidence and review recommendation;
- significance, ambiguity, decomposition, uncertainty, and negative evidence;
- explicit Chief Editor decision boundary.

Passing means recommendations are proportionate and owner-safe. It does not
prove real-world routing improvement.

## Architecture completion judgment

The proposed shared capability is the minimum clear owner for a genuine gap.
All decisions remain with current owners, the task object and lifecycle stay
unchanged, and the mechanism is usable through existing artifacts and roles.

Confidence: `supported` for the new owner-file design, based on verified owner
inspection and authoritative decision-support patterns.

Residual risk: future agents may still apply the view as a checklist or keyword
router. Negative-case validation, concise wording, explicit non-decision, and
Review Agent challenge are required mitigations.
