# Orchestration Plan Template

Purpose: define the execution contract for a task. Keep this plan compact and
stage-specific. Global governance rules live in `AGENTS.md`; sequence details
live in the selected pipeline.

Create for tasks that need role routing, process-depth decisions, high-risk
traceability, or non-trivial coordination. For compact low-risk work, use only
the fields needed to make routing and review safe.

## task summary

- Task ID:
- User goal:
- Requested deliverable:
- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
- Selected deliverable: pending / value
- Audience/channel:
- Current active version:

## task classification

- Task type:
- Risk mode: `low-risk` / `standard` / `high-governance` / `unknown`
- Factual sensitivity:
- Human approval likely required: yes/no/unknown
- Rationale:

## process depth

- Depth: `compact` / `normal` / `full`
- Execution profile: `compact` / `expanded`
- Rationale:
- Forbidden depth shortcuts:
- Expanded profile trigger, if any:

## client profile

- Client profile: `none` / `sber` / `unknown`
- Client profile status: `not_applicable` / `active` / `pending_source`
- Activation reason:
- Non-activation reason, if considered and rejected:
- Client-profile files:
  - `/kb/clients/sber/usage-rules.md`
  - `/kb/clients/sber/editorial-policy.md`
  - `/kb/clients/sber/sber-review-checklist.md`
- Stop condition:

Use `client_profile: sber` only for Sber-owned, Sber-product,
Sber-communication, or explicit Sber-redpolicy tasks. Do not activate it for
independent materials where Sber is only mentioned as topic, example, source, or
competitor.

## task need recognition

Use this conditional view only when task nature, likely capabilities or Domain
Packs, depth, significance, ambiguity, decomposition, or uncertainty is
material. Omit it for trivial, obvious work. It is advisory evidence, not a
route, activation, depth choice, gate, or standalone artifact.

- Observed request signals:
- Requested deliverable:
- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
- Recommended deliverable and outcome-fit reason:
- Likely primary task type:
- Material secondary aspects:
- Likely capabilities and why:
- Likely Domain Packs and why:
- Research / evidence recommendation:
- Risk / consequence recommendation:
- Review recommendation:
- Architecture / engineering / communication significance:
- Ambiguity, contradiction, or missing information:
- Decomposition recommendation:
- Confidence and negative evidence:
- Explicit non-decision:
- Chief Editor decision or next question:

## outcome-first deliverable decision

Complete before pipeline selection when deliverable choice is material. For an
obvious compact task, one line may record that requested, recommended, and
selected deliverables are the same. Do not create a separate artifact.

- User problem to solve:
- Requested deliverable: value / `not specified`
- Format authority: `explicit` / `delegated` / `inferred` / `unknown`
- Recommended deliverable:
- Why this is the smallest sufficient outcome-fit artifact:
- Alternative value or mismatch, if any:
- Decision: `respect_requested` / `select_recommended` /
  `ask_before_change` / `constrain_with_explanation`
- Selected deliverable:
- Explicit-intent preservation note:

An explicit requested deliverable remains selected by default. Recommend an
alternative when useful, but do not substitute it without user agreement. If
the mismatch makes the request unsafe or unable to achieve its stated outcome,
route it through preflight rather than silently overriding it.

## selected pipeline

Select only after the selected deliverable above is known.

- Pipeline:
- Why this pipeline fits the selected deliverable:
- Pipeline exceptions or local constraints:

## preflight gate

Use before production starts. Keep compact; do not create a separate artifact
unless a task-specific governance or restartability need justifies it.

| Field | Decision |
| --- | --- |
| Audience | `confirmed` / `inferred` / `unknown` |
| Channel or context | `confirmed` / `inferred` / `unknown` |
| Selected deliverable | `defined` / `unclear` |
| Source boundary | `defined` / `unclear` |
| Success criterion | `defined` / `unclear` |
| Approval boundary | `defined` / `unclear` |
| Missing data strategy | `ask` / `constrain` / `proceed` / `block` |

- Rationale:
- Production may start: yes/no
- If `ask`: smallest question to user:
- If `constrain`: explicit scope boundary:
- If `block`: blocking reason:

## editorial decision frame

Use before handing work to Writer Agent or UX Writer. If research is required,
fill or refresh this after research sufficiency is known. Keep this as a short
management block, not an analytical document. Do not duplicate research,
outline, review, rejected-alternative addenda, or long rationale here. Do not
create a standalone `editorial_decision.md` only because this reasoning is long;
if the decision needs extended justification, use a task-local analytical
artifact and keep this frame compact.

- Chosen editorial route:
- Why this route serves the selected deliverable and task outcome:
- Reader journey rationale, when material: starting state -> required change ->
  explanation sequence -> practical result
- Cognitive Bridge, required for teaching/understanding work or `not applicable`
  with reason:
  - What the reader already knows:
  - Old or incomplete model to update:
  - Required transition:
- Moments of Insight, 3-5 formulated ideas rather than section titles:
- Practical Transformation, observable action/decision/habit after use:
- Bounded Utility Tradeoff, only when a local chronology, product bridge, or
  less durable detail directly serves the recorded reader need:
  - Concrete reader need:
  - Bounded scope:
  - Evidence and freshness basis:
  - Stale-if or review trigger:
  - Attribute intentionally relaxed:
  - Expected reader benefit:
  - Non-relaxable guardrails preserved:
- Alternatives considered, usually 2-3 compact options:
  - Alternative route, one line:
    - Why rejected, one line:
  - Alternative route, one line:
    - Why rejected, one line:
  - Alternative route, one line, if useful:
    - Why rejected, one line:
- Writer/UX Writer contract:
  - Result type:
  - Angle or reader path:
  - Scope boundary:
  - Must include:
  - Must not include:
  - Source boundary and confidence:
- Review focus:
- Bounded utility tradeoff challenge, if applicable:
- Reroute triggers:

## custom workflow mini-contract

Use only when the selected pipeline needs a documented local deviation. Do not
weaken review, governance, role boundaries, or required fields.

- Deviation:
- Reason:
- Owner:
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake |  |  |  |
| Research |  |  |  |
| Writing/UX writing |  |  |  |
| Review | Review Agent | yes | `review.md` required |
| Finalization |  |  |  |
| Final governance | Chief Editor | if applicable |  |

## planned runtime topology

Use only when multiple material runtime streams are planned. Use stable
task-local IDs; do not use random nicknames as process identifiers. Model/mode
may be `unknown` or `not recorded`.

| Stream ID | Canonical role/function | Purpose and scope | Parent/coordination | Model/mode if known | Input boundary | Expected artifact/package | Responsibility boundary |
| --- | --- | --- | --- | --- | --- | --- | --- |

## required knowledge and evidence

- Required KB:
- Required source/evidence files:
- Evidence gaps:

## artifact scope

Classify artifacts before creating them. Conditional artifacts need a consumer
or governance/traceability reason.

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles |  |
| `review.md` | required before finalization | Chief Editor / Final Editor |  |
| `review-summary.md` | conditional |  |  |
| `qa-checklist.md` | conditional |  |  |
| `open-questions.md` | conditional |  |  |
| `finalization-notes.md` | conditional |  |  |
| `finalization-checklist.md` | conditional |  |  |

## structure-before-writing plan

Use when the material is instructional, operational, reference-like, role-based,
or repeat-use.

- Reader path:
- Section roles:
- Required structure:
- Duplication risks:

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |

## status transitions

- Starting status:
- Next expected status:
- Status owner:
- Status update trigger:

## review requirements

- Review artifact: `review.md`
- Review depth:
- Reviewer independence requirement:
- Claims/evidence checks required:
- Optional review artifacts justified: yes/no and why

## human approval requirements

- Required: yes/no/unknown
- Approval owner:
- Evidence needed:
- Cannot proceed past:

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |

## unresolved questions

- None / list question, owner, and blocking status.

## escalation conditions

- Stop or escalate if:

## completion criteria

- Required artifacts complete:
- Review outcome acceptable:
- Blockers resolved:
- Governance fields complete:

## finalization conditions

- Finalization may start when:
- Finalization must stop when:
- Compact finalization shape allowed: yes/no and why
- Conditional finalization artifacts needed: yes/no and why

## restart notes

- Minimum read set:
- Current active version:
- Deprecated/previous versions:
- Latest relevant handoff:
- Directly relevant pipeline/KB:
