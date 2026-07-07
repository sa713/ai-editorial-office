# Editorial Evidence Framework

This file is the canonical owner for evidence taxonomy, confidence labels,
evidence requirements, reusable evidence collection, and the optional evidence
section standard in AI Editorial Office.

It extends the task object, capability registry, shared lifecycle kernel,
Editorial Decision Frame, and Editorial Challenge Lens. It is not a new
pipeline, role, workflow engine, scoring system, or mandatory artifact set.

## Core Principle

Every material editorial conclusion should be able to answer four questions:

- what evidence supports it;
- how trustworthy that evidence is;
- what assumptions remain;
- what risks or unknowns still exist.

Confidence is derived from evidence quality, not from how certain the model or
agent feels. Assumptions, hypotheses, and intuition may guide exploration, but
they must not be presented as facts.

## Evidence Taxonomy

Evidence classes are extensible. A task may add a local class when the source
boundary, domain, or deliverable requires it, but local classes must still
record provenance, confidence, assumptions, and risks.

| Class | Meaning | Typical confidence ceiling |
| --- | --- | --- |
| User-provided fact | Direct statement from the user about their intent, constraints, context, or supplied private knowledge. | High for user intent; medium for external truth unless independently verified. |
| Uploaded artifact | File, image, document, PDF, dataset, or transcript supplied for the task and inspected directly. | High for what the artifact contains; depends on provenance for truth claims. |
| Repository inspection | Direct reading of repository files, git state, project docs, tests, scripts, or local artifacts. | High for current local state when file/version is identified. |
| Source code inspection | Direct reading of code, configuration, tests, generated outputs, logs, or diffs. | High for observed implementation; medium for inferred runtime behavior without execution. |
| Documentation | Official docs, local canon, client policy, product spec, README, or process documentation. | High when current and authoritative; lower when stale, informal, or contradicted. |
| Measurement | Count, metric, timestamp, benchmark, static check, rendered output, or observed system state. | High when method is recorded and repeatable; lower when sample or method is incomplete. |
| Experiment | Trial run, prototype, manual check, user test, or controlled comparison. | Medium to high depending on setup, repeatability, and coverage. |
| Test | Automated or manual validation with clear inputs, expected behavior, and result. | High for covered behavior; does not prove untested behavior. |
| External verified source | Primary source, official publication, authoritative dataset, or current public record checked directly. | High when source authority and freshness are clear. |
| Corroborated secondary source | Non-primary source supported by independent evidence. | Medium unless validated by primary evidence. |
| Assumption | Working claim accepted temporarily because evidence is incomplete. | Low to medium; must be marked as assumption. |
| Hypothesis | Testable explanation or proposed route not yet verified. | Low to medium; must name validation needed. |
| Analogy or precedent | Similar prior case, pattern, or example used to reason about current work. | Low to medium unless directly comparable and cited. |
| Intuition | Expert judgment, taste, or model sense without direct evidence. | Lowest; acceptable for brainstorming only unless labeled and later verified. |

## Confidence Levels

Use a small scale. Labels describe evidence quality for the claim at hand.

| Level | Meaning | Acceptable use | Typical risks |
| --- | --- | --- | --- |
| `verified` | Supported by direct, current, authoritative evidence or repeatable validation. | Final decisions, code review blockers, high-governance claims, material business recommendations. | Hidden scope limits, stale authority, overgeneralizing beyond verified coverage. |
| `supported` | Supported by relevant evidence, but with some limits in coverage, freshness, or authority. | Standard recommendations, implementation plans, drafts, review findings with caveats. | Missing edge cases, partial source boundary, confidence overstated. |
| `plausible` | Reasonable inference from available context, but not directly confirmed. | Brainstorming, provisional route selection, low-risk planning when caveated. | Treated as fact, untested assumptions, route lock-in. |
| `speculative` | Based mainly on assumption, analogy, incomplete evidence, or intuition. | Exploration, option generation, questions to verify. | Hallucination, false precision, unsupported recommendation. |
| `unsupported` | Required evidence is absent, contradicted, inaccessible, or not inspected. | Must be omitted, caveated, requested, or blocked depending on task risk. | False claim, weak decision, unsafe finalization. |

Do not use a high confidence label for a broad conclusion merely because one
supporting fact is verified. The confidence of a conclusion is limited by the
weakest material evidence needed for that conclusion.

## Evidence Requirements By Output

Not every output needs the same evidence depth. Compact execution remains valid
when the selected route, risk, and review needs allow it.

| Output type | Minimum expected evidence | Minimum confidence for material claims |
| --- | --- | --- |
| Brainstorming | Source boundary and visible assumptions. | `plausible`; mark speculative options. |
| Editorial angle or structure choice | Brief, audience/channel, constraints, and route rationale. | `supported` for chosen route; alternatives may be `plausible`. |
| Design proposal | User goal, constraints, comparable examples or product/repository context, risks. | `supported`; `verified` for hard constraints. |
| Architecture recommendation | Canonical docs, repository inspection, relevant prior decisions, risk/compatibility analysis. | `supported` to `verified`; assumptions explicit. |
| Implementation plan | Current files/state, acceptance criteria, dependency and risk check. | `supported`; `verified` for file paths and existing behavior. |
| Code review | Direct diff/code inspection, tests or reasoned coverage, reproducible finding basis. | `verified` for blockers; `supported` for non-blocking concerns. |
| Research synthesis | Source inventory, relevance, freshness, contradictions, and confidence notes. | `supported` to `verified` for factual claims. |
| Business recommendation | Objective, constraints, decision criteria, evidence for impact/risk, alternatives. | `supported`; `verified` for numbers, commitments, legal/compliance claims. |
| Review verdict | Saved artifact, independence basis, required evidence, unresolved blockers. | `verified` for approval blockers and verdict basis. |
| Final decision | Approved review, final artifact, human approval boundary, residual risks. | `verified` for closure facts; caveat any remaining `supported` risks. |

When the required confidence is not available, the task should choose one of
four moves: request evidence, constrain the conclusion, proceed with explicit
caveats, or block.

## Evidence Collection Pattern

Use this pattern in any stage that makes a material claim, route, review
finding, recommendation, or final decision.

1. What do we know?
2. How do we know it?
3. What class of evidence supports each material claim?
4. What confidence level does that evidence justify?
5. What is missing, contradicted, stale, or uninspected?
6. What assumptions remain, and why are they acceptable or unsafe?
7. What risks remain if the conclusion is wrong?
8. What evidence would most reduce uncertainty?
9. Should the next action be `ask`, `constrain`, `proceed`, or `block`?

The pattern may be recorded compactly inside the smallest existing artifact
that remains reviewable. It does not require a standalone file unless risk,
review, downstream use, or governance needs a separate artifact.

## Evidence Section Standard

Any editorial artifact may include this structure when a claim, decision, or
recommendation needs transparent support. Use only the fields that matter.

```markdown
## evidence

- Claim or decision:
- Evidence:
  - Class:
  - Source or artifact:
  - What was checked:
- Confidence: verified | supported | plausible | speculative | unsupported
- Assumptions:
- Unknowns:
- Risks:
- Validation needed:
- Next action: ask | constrain | proceed | block
```

For compact tasks, this may be a short paragraph or table row. For high-risk or
high-governance tasks, use enough detail for Review Agent and Chief Editor to
reconstruct the evidence path.

## Integration Points

### Task Object

The task object may expose evidence state through existing artifacts rather than
a new mandatory file. Material decisions should be able to point to:

- evidence basis;
- confidence level;
- assumptions;
- unknowns;
- validation needed;
- residual risk.

### Capability Registry

Evidence-confidence assessment is a reusable capability. It can be performed by
different roles at different stages, while Research Agent remains the primary
owner when a dedicated research stage is assigned.

### Shared Lifecycle

Lifecycle gates are evidence-backed confidence decisions. The gate record should
show enough evidence, confidence, assumptions, and unknowns for the next owner
or reviewer to continue safely.

### Editorial Decision Frame

The Editorial Decision Frame should name the evidence basis and confidence for
the chosen route when the route materially affects writing, UX writing, business
recommendation, architecture recommendation, or analysis. Rejected alternatives
can stay compact, but their rejection reasons should not be pure preference when
evidence is available.

### Editorial Challenge Lens

The Editorial Challenge Lens tests whether the assumptions and evidence that
made the chosen route valid still hold. Review should challenge weak evidence,
unsupported claims, hidden assumptions, and route-validity risks without
becoming a new route owner.

## Role Cooperation

Evidence quality is shared work, not a new role.

| Role | Evidence responsibility |
| --- | --- |
| Chief Editor | Select evidence depth during routing, require evidence basis for material route decisions, decide whether weak evidence means ask, constrain, proceed, or block. |
| Intake Agent | Separate user-provided facts, assumptions, unknowns, and source boundary issues before routing. |
| Research Agent | Gather, verify, classify, and structure evidence; label confidence; surface contradictions and unknowns. |
| Writer Agent | Use approved evidence only, preserve caveats, label assumptions in writer notes or claims-used, and request repair when evidence is insufficient. |
| UX Writer | Tie product copy to product evidence, state assumptions, and block copy that would invent behavior or hide risk. |
| Review Agent | Challenge evidence quality, confidence labels, assumptions, and unknowns; request changes or block weak conclusions. |
| Final Editor | Preserve evidence-backed caveats and avoid adding unsupported claims during finalization. |
| Artist Agent | When activated, preserve evidence-backed visual meaning and escalate semantic uncertainty. |

## Stop Conditions

Stop, request repair, or block when:

- a material claim is `unsupported`;
- a required confidence level is not met;
- a fact and assumption are mixed together;
- evidence provenance is missing for a sensitive claim;
- a source was not actually inspected;
- current evidence contradicts the chosen route;
- review cannot reconstruct how a conclusion was reached;
- finalization would remove caveats or add unreviewed evidence.

## Non-Goals

This framework does not:

- create a Fact Checker role;
- make research mandatory for no-claim tasks;
- replace `/kb/research_evidence.md`;
- require every artifact to include an evidence section;
- create numeric scoring;
- weaken compact execution;
- weaken review;
- promote intuition to evidence;
- turn `/about` into canon.
