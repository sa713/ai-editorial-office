# Handoff

## Metadata

- Task ID: `TASK-CARE-PR-STRATEGY`
- From role: `writer_agent`
- To role: `review_agent`
- Date: 2026-06-30
- Current status: `review`
- Risk mode: `high-governance`
- Process depth: `full`
- Current active version: `draft.md`

## Reason For Handoff

- Stage transition: writing to independent review.

## Delta Summary

- What changed since the last reliable checkpoint: outline, draft, writer notes,
  and claims-used were created.
- What matters now: review should test whether the draft overclaims beyond the
  single brainstorm source.

## Artifacts Created Or Updated

| Artifact | Current? | Notes |
| --- | --- | --- |
| `outline.md` | yes | Structure before writing |
| `draft.md` | yes | Strategy memo draft |
| `writer-notes.md` | yes | Assumptions and caveats |
| `claims-used.md` | yes | Claims used in draft |
| `task-manifest.md` | yes | Review assigned |
| `status.md` | yes | Transition to review recorded |

## Active Constraints For Next Role

- High-governance review required.
- Use `claims_table.md` and `claims-used.md`.
- Review must be independent and must not rewrite the draft.

## Editorial Decision Transfer

- Chosen route: service-positioning and 90-day action strategy.
- Rejected alternatives, names or one-line reasons: immediate PR campaign,
  portfolio-only, internal-process-only.
- Writing contract: fulfilled through `draft.md`.
- Review focus: source caveats, traceability, route fidelity, approval boundary.

## Blockers And Open Questions

- No known blockers.
- Open questions about implementation owner are intentionally left as future
  human decisions.

## Next Action

- Required next role action: run full high-governance review.
- Expected output: `review.md`, `qa-checklist.md`, review handoff.
- What not to change: do not finalize or rewrite during review.

## Validation Before Proceeding

- Required read set: `brief.md`, `orchestration_plan.md`, `research.md`,
  `sources.md`, `facts.md`, `claims_table.md`, `outline.md`, `draft.md`,
  `writer-notes.md`, `claims-used.md`.
- Required evidence or review check: claim traceability and approval boundary.
- Version/currentness check: `draft.md` is the artifact under review.

## Escalation Conditions

- Stop or escalate if the draft contains unsupported official claims or if
  reviewer independence cannot be established.
