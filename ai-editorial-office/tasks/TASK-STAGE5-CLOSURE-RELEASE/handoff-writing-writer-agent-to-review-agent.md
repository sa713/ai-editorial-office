# Handoff: Writer Agent To Review Agent

- Task ID: `TASK-STAGE5-CLOSURE-RELEASE`
- From: `writer_agent`
- To: `review_agent`
- Reason: bounded Stage 5 closure patch is ready for independent review
- Production files changed:
  - `ROADMAP.md`
  - `BACKLOG.md`
  - `project-state.md`
  - `/about/project-state.md`
- Meaning changed: Stage 5 closure pending -> Stage 5 accepted and complete
- Meaning preserved: S5.R1-S5.R5 accepted/Done, S3.R4 Review, no future stage,
  Project v1.0 undecided, architecture unchanged
- Review focus: path allowlist, semantic consistency, exact-copy identity,
  future-stage non-activation, S3.R4 preservation, validators
- Expected output: `review.md` with `approved`, `changes_requested`, or `blocked`
- Forbidden: reviewer edits to production files
- Escalate if: any stale closure-pending state remains in active state owners or
  any unauthorized state decision appears
