# Handoff: Writer Agent to Review Agent

## Transfer

- From: `writer_agent`
- To: `review_agent`
- Reason: roadmap candidate and lightweight navigation edits are ready for
  independent review.

## Created or Updated

- Created `../../ROADMAP.md`.
- Updated root `../../../README.md`.
- Updated `../../project-state.md`.
- Created task-local routing and writing notes.

## Review Focus

- Confirm the roadmap preserves P0-P10 roadmap content without inventing or
  dropping roadmap items.
- Confirm `ROADMAP.md` is framed as strategy, not operational canon.
- Confirm canonical ownership remains with files named in `AGENTS.md`.
- Confirm navigation is lightweight and not scattered across many documents.
- Confirm prohibited areas were not touched.

## Stop Conditions

Stop or request changes if:

- roadmap text changes architecture or behavior;
- roadmap becomes governance, lifecycle, capability, workflow, or review-gate
  owner;
- roadmap omits or invents roadmap items;
- navigation turns into policy duplication;
- `/about`, `diff_intake.md`, or legacy paths are touched.
