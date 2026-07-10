# Task Need Recognition Release Report

Date: 2026-07-10

Release: `S5.R4 - Task Need Recognition`

Status: Release Candidate ready for Project Lead review

## Executive result

S5.R4 adds one bounded, evidence-first Task Need Recognition capability before
Chief Editor routing. It turns available request evidence into inspectable
recommendations about likely task type, material capabilities, likely Domain
Packs, research/evidence and review needs, risk/consequence, architecture/engineering/
communication significance, ambiguity, decomposition, uncertainty, and
negative evidence.

The capability never decides. Intake Agent may assemble the initial advisory
view; Chief Editor challenges it and remains responsible for preflight, task
type, route, risk, process/evidence/review depth, capability and Domain Pack
activation, role assignment, decomposition, planning, and next action. Review
Agent challenges material use inside the existing review gate.

## Research result

The research landscape combines requirements and engineering intake,
architecture decision intake, problem framing, issue triage, incident
classification, intent recognition, model routing, and human-AI decision
support.

The transferable pattern is contextual and multi-signal:

- start with outcome, stakeholder, work surface, constraints, consequence, and
  evidence state;
- separate task type from risk, priority, depth, and decision authority;
- use structured recommendations as inputs to human judgment;
- preserve missing information, contradictions, alternatives, out-of-scope
  conditions, and uncertainty;
- use impact and exposure to justify depth;
- protect simple work from methods whose cost is not justified;
- treat automatic intent/model routing as a contrast case, not the release
  architecture.

Primary and authoritative evidence is registered in
`tasks/TASK-TASK-NEED-RECOGNITION-RELEASE/sources.md`; repository facts and
downstream claims are traced in `facts.md` and `claims_table.md`.

## Architecture synthesis

### New bounded owner

`kb/task_need_recognition.md` owns only the shared request-to-need advisory
contract. A canonical owner is justified because existing files own component
signals and all decisions, but no shared file previously defined how available
request evidence becomes a non-decisional need view across capabilities and
Domain Packs.

### Existing owners preserved

| Concern | Existing owner | S5.R4 relationship |
| --- | --- | --- |
| faithful request state and unknowns | Intake Normalization / Intake Agent | produces observed signals and an initial recommendation when material |
| route, task type, risk, depth, activations, roles, split, next action | Chief Editor and Routing And Preflight | sole decision authority |
| sufficiency to begin | Preflight Gate | consumes evidence; not duplicated |
| evidence classes and confidence | Editorial Evidence Framework | reused directly |
| reasoning and decomposition moves | Analytical Reasoning | recommended when material; not reproduced |
| decision-ready analysis | Professional Analysis | downstream product owner; not a live router |
| reader transfer | Professional Communication | downstream quality owner |
| design significance | Architecture Review | materiality owner |
| implementation/change significance | Engineering Review | materiality and validation owner |
| domain activation criteria and limits | Domain Pack Standard and each pack | recognition may recommend; Chief Editor activates |
| saved evidence views for later decisions | Evaluation Signals | remains separate from live intake |
| independent outcome | Review Agent / Review Pipeline | challenges the view; does not route or approve activation |

### Manual and advisory boundary

Recognition is advisory, optional when immaterial, qualitative, and stored only
inside existing task artifacts. It creates no classifier, score, threshold,
taxonomy owner, standalone artifact family, automatic action, role, pipeline,
lifecycle stage, status, review gate, store, dashboard, or autonomous plan.

## Implemented changes

### Canonical integration

- Added `kb/task_need_recognition.md` with evidence-first signal families,
  qualitative recommendation dimensions, compact advisory view, owner map,
  review questions, stop conditions, and non-goals.
- Registered the capability in `kb/00_index.md` and
  `kb/capability_registry.md`.
- Connected it to existing task-object and lifecycle surfaces without adding a
  required field or artifact.
- Added bounded Intake Agent, Chief Editor, Review Agent, and Review Pipeline
  responsibilities.
- Added a conditional section to the existing orchestration-plan template.
- Added the owner and entry references to `AGENTS.md`.

### Recognition behavior

The capability supports:

- one likely primary task type plus material secondary aspects, without a
  forced exhaustive taxonomy;
- capability and Domain Pack recommendations tied to evidence and existing
  owner criteria;
- qualitative `none or source-light`, `compact`, or `full` research/evidence
  recommendations;
- qualitative risk/consequence recommendations from exposure, sensitivity,
  reversibility, blast radius, uncertainty, and wrong-result cost, while Chief
  Editor retains risk-mode selection;
- qualitative `focused`, `standard`, or `deep` review recommendations that do
  not create review levels or select scope;
- architecture, engineering, professional communication, and analytical
  significance signals;
- ambiguity, contradiction, missing information, uncertainty, negative
  evidence, and confidence;
- split/sequence recommendations based on divergent deliverables, owners,
  evidence, risk, domain, validation, or dependency;
- an explicit non-decision and a separately recorded Chief Editor decision or
  next question.

## Representative validation

`tests/task_need_recognition_smoke_test.md` records ten synthetic cases:

| Case | Expected recognition | Result |
| --- | --- | --- |
| simple editing | compact, no pack, no research expansion | passed |
| architecture review | Architecture Review and Software Architecture context | passed |
| engineering implementation | Engineering Review without architecture/pack inflation | passed |
| AI engineering | AI Engineering primary with conditional adjacent owners | passed |
| DevSecOps | DevSecOps primary and Cybersecurity adjacent | passed |
| cybersecurity | defensive Cybersecurity primary and architecture context | passed |
| ambiguous mixed request | uncertainty and Chief Editor clarification/decomposition | passed |
| multi-domain request | coherent integrated decision with four material packs | passed |
| research-heavy request | full evidence and analysis without unjustified pack | passed |
| many keywords, simple outcome | simple copyedit; no capability/pack activation | passed |

All 10 cases expose observed evidence, recommendations, uncertainty/negative
evidence, explicit non-decision, and a separate Chief Editor decision. The
cases demonstrate the contract, but do not prove real-world routing accuracy or
future system improvement.

## State and memory disposition

- `BACKLOG.md`, `ROADMAP.md`, and `project-state.md` record accepted S5.R3,
  S5.R4 in `Review`, and S5.R5 `Not Started`.
- Exact-copy `/about` files affected by canonical changes are synchronized.
- Compact memory summaries include the new capability, owner, and release
  state without adding a twenty-first memory file.
- Root `diff_intake.md` remains untouched and outside the release.

## Architecture impact

Impact: small.

The release adds one non-role capability owner and concise references across
existing owners. It changes no decision authority, stage, gate, status,
pipeline, role, or automation boundary.

## Known limits and residual risk

- Advisory quality depends on the evidence present and the human challenge;
  no accuracy guarantee or calibrated probability is claimed.
- Qualitative depth recommendations require judgment and may vary between
  comparable tasks.
- A compact view can become process weight if applied to trivial requests;
  omission or one-line treatment is explicitly allowed.
- Multi-domain and decomposition recommendations remain context-sensitive.
- Accepted Domain Packs can become stale; their own source registers and
  stale-if triggers remain authoritative.
- Synthetic validation cannot measure real-world routing improvement, missed
  capability needs, or operational cost reduction.

## Release conclusion

S5.R4 meets the mission boundary and is ready for Project Lead review as a
Release Candidate. Project Lead acceptance is pending; S5.R5 has not started.
