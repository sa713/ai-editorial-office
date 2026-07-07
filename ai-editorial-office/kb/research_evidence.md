# Research Evidence

## Purpose

Practical guidance for keeping research evidence reviewable without creating
unnecessary artifacts.

This guidance does not override `AGENTS.md`, selected pipelines, role specs,
task artifacts, review-gate, or source provenance rules.

Evidence classes, confidence labels, evidence requirements by output type, and
the reusable evidence section standard are owned by
`/kb/editorial_evidence_framework.md`. This file owns only evidence depth modes
for research artifacts.

## Evidence Modes

### no-research

Use when the task has no factual, product, policy, numeric, legal, HR,
security, regulatory, medical, financial, or reputational claims.

Required:

- short rationale in `task-manifest.md`, `orchestration_plan.md`, or
  `status.md`;
- review confirms that no material claims need evidence.

Must not:

- create `sources.md`, `facts.md`, `claims_table.md`, or `research.md` by
  default;
- block only because research artifacts are missing when no material claims
  exist.

### compact-evidence

Use for simple or source-light tasks with limited material claims.

Required:

- source pointers or brief evidence notes for the claims that affect output;
- facts or claim list only for claims that materially enter the draft;
- `claims-used.md` when Writer Agent uses material claims;
- enough structure for Review Agent to verify claims without reading a full
  research dump.

Compact evidence can live in the smallest task-local place that remains
reviewable: `research.md`, `sources.md`, `facts.md`, `claims-used.md`, a clear
evidence note, or an equivalent compact section in an existing artifact.

### full-evidence

Use for high-governance, external, policy, numeric, security, legal, HR,
regulatory, financial, medical, or reputational claims.

Required:

- `research.md`;
- `sources.md`;
- `facts.md`;
- `claims_table.md`;
- `claims-used.md`;
- review claim checks.

Full evidence is required when unsupported claims could mislead users, create
legal or compliance risk, affect user rights or money, damage reputation, or
make the Review Agent read a large research dump just to find the claims used.

## Artifact Rules

Research artifacts are conditional, not automatic. Create each artifact only
when it has a consumer, traceability purpose, review purpose, governance need,
or explicit task requirement.

Do not create empty source, fact, or claim files as placeholders. Missing
artifacts are acceptable in `no-research` mode when the rationale is visible
and Review Agent can confirm that no material claim needs evidence.

For `compact-evidence`, prefer a small, reviewable evidence chain over a broad
research dump. For `full-evidence`, keep the evidence set explicit and
separate.

## Claim Traceability

Material claims should trace in this direction:

```text
output claim -> claims-used.md -> facts.md or claims_table.md -> sources.md
```

Equivalent compact evidence is acceptable for source-light tasks when the same
relationship is visible.

`claims-used.md` should list only claims that entered the draft or final
artifact. It should not copy the whole research record.

Unsupported, contradicted, or uncertain claims must stay visible. Unsupported
and contradicted claims must not be used as facts. Uncertain claims require a
caveat or must be omitted.

## Writer Handoff

Writer Agent should tell Review Agent which material claims entered the draft
and where their evidence is recorded.

For `no-research`, the handoff or task state should make it clear that the
draft intentionally contains no material claims that require evidence.

For `compact-evidence`, the handoff should point to the exact evidence note,
source pointer, facts list, or `claims-used.md` section the reviewer needs.

For `full-evidence`, the handoff should point to `research.md`, `sources.md`,
`facts.md`, `claims_table.md`, and `claims-used.md` without repeating them.

## Review Expectations

Review Agent should choose evidence depth by risk and claims, not by template
habit.

For `no-research`, Review Agent should not require research artifacts when the
task has no material claims and the no-research rationale is visible.

For `compact-evidence`, Review Agent should verify material claims through
`claims-used.md`, source pointers, facts, or equivalent compact evidence.

For `full-evidence`, Review Agent should block or request changes when
`research.md`, `sources.md`, `facts.md`, `claims_table.md`, `claims-used.md`,
or claim checks are missing or insufficient.

If material claims exist but evidence is missing, the outcome should be
`changes_requested` or `blocked`, depending on severity and recoverability.

## What Not To Do

- Do not make research mandatory for low-risk, no-claim tasks.
- Do not use a full research dump as the only way to understand which claims
  entered the draft.
- Do not create `sources.md`, `facts.md`, or `claims_table.md` automatically
  without a traceability or review purpose.
- Do not let `claims-used.md` become a broad research archive.
- Do not claim source, product, policy, or compliance support without evidence
  and source status that permits the claim.
- Do not let compact evidence bypass review-gate.
