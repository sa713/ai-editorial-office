# Handoff: Writer Agent -> Review Agent

- Task: TASK-0021
- Manifest: `task-manifest.md`
- Sending role: `writer_agent`
- Receiving role: `review_agent`
- Current status recommendation: `review`
- What changed: short email draft created.
- Artifacts created or updated: `draft.md`, `writer-notes.md`
- Constraints changed: none.
- Blockers: none.
- Next role: `review_agent`
- Next action: independently review `draft.md` against `brief.md`, `orchestration_plan.md`, Social Pipeline compact requirements, tone, and editorial policy.
- Expected outputs: `review.md` with verdict and embedded checklist; handoff for finalization or changes.
- Forbidden outputs: do not rewrite as final, do not approve without checking required access instructions.
- Escalation conditions: missing required point, tone mismatch, unsupported added claim, or confusing access sequence.
