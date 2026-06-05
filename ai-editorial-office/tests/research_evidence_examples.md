# Research Evidence Synthetic Examples

## Purpose

These synthetic examples help check evidence mode selection for research
artifacts. They are not task materials and do not replace `AGENTS.md`,
pipelines, role specs, `kb/research_evidence.md`, or review-gate.

## Example 1 - low-risk no-research

Scenario:

> Short internal messenger reminder with no factual, product, policy, numeric,
> legal, HR, security, regulatory, medical, financial, or reputational claims.

Expected evidence mode: `no-research`

Expected handling:

- record short no-research rationale in `task-manifest.md`,
  `orchestration_plan.md`, or `status.md`;
- create the draft only within the known request scope;
- Review Agent confirms that no material claims need evidence.

Must not:

- create `sources.md`, `facts.md`, `claims_table.md`, or `research.md` by
  default;
- block only because `research.md` is missing;
- bypass `review.md` before finalization.

## Example 2 - compact-evidence

Scenario:

> Internal article intro using two user-provided facts and one date.

Expected evidence mode: `compact-evidence`

Required:

- source pointer or brief evidence note for the user-provided facts and date;
- `claims-used.md` if those claims enter the draft;
- enough traceability for Review Agent to verify claims without a full research
  dump.

Expected handling:

- Writer Agent uses only the provided facts and date;
- evidence notes stay compact and tied to output claims;
- Review Agent checks output claim -> `claims-used.md` -> evidence note/source
  pointer.

Must not:

- require full `research.md`, `sources.md`, `facts.md`, and `claims_table.md`
  when compact traceability is sufficient;
- treat user-provided facts as broader approval for additional invented claims;
- hide uncertainty or missing context.

## Example 3 - full-evidence

Scenario:

> External announcement with product behavior, date, user impact, and
> compliance-sensitive claim.

Expected evidence mode: `full-evidence`

Required:

- `research.md`;
- `sources.md`;
- `facts.md`;
- `claims_table.md`;
- `claims-used.md`;
- review claim checks.

Expected handling:

- Research Agent separates facts, assumptions, contradictions, and open
  questions;
- Writer Agent uses only claims marked safe for draft use;
- Review Agent verifies material claims through the full evidence chain before
  approving.

Must not:

- proceed with unsupported product behavior, date, user impact, or compliance
  claims;
- rely on a broad research dump instead of explicit claim traceability;
- approve if material evidence is missing.
