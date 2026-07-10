# Handoff: Research Agent to Chief Editor

## Transfer

- From role: `research_agent`
- To role: `chief_editor`
- Current status recommendation: `research` -> `planning`
- Reason: authoritative and repository research is sufficient for architecture
  synthesis.

## Changed artifacts

- `../../research/memory_hygiene_intelligence_landscape.md`
- `sources.md`
- `facts.md`
- `claims_table.md`

## Decision-ready findings

- External memory should remain a derived, provenance-carrying view of a
  versioned authoritative repository source.
- Canonical change is a revalidation/materiality trigger, not an automatic
  write command.
- Exact-copy and summary files require different validation: byte identity
  versus semantic preservation.
- Knowledge-base, records, and privacy practice supports consolidation,
  continuing-value appraisal, explicit retirement, minimization, and rationale.
- AI context research supports density/compactness but cannot validate summary
  correctness; human review remains necessary.
- Existing Knowledge Evolution, Memory Curation, Integrity Checking, Chief
  Editor, Review Agent, and Review Pipeline owners are sufficient.
- Evaluation Signals may expose drift but cannot select or execute disposition.

## Constraints for synthesis

- Preserve `/about` as exactly 20 derived memory files unless a separately
  reviewed package change is justified; no evidence supports such a change.
- Keep checker behavior advisory/read-only.
- Put durable disposition rules in the existing Learning Framework, not in
  state files or `/about`.
- Record no-sync only when material; do not create a per-commit log.
- Normalize accepted S5.R2/S5.R3 RC state before review.

## Next action

Chief Editor should define the exact existing-owner change surface, unchanged
owners, disposition fields, validation contract, and implementation handoff.

## Escalate if

The design requires autonomous synchronization, memory authority over canon,
silent deletion, completeness scoring, or a new owner/role/pipeline/gate.
