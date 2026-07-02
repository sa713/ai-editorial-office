This is a task-local system-update packet for P5. It does not contain real task
materials.

# Orchestration Plan

## Editorial Entry

- Active orchestrator: chief_editor
- Task type: system update / generator patch
- Process depth: compact
- Assigned roles: chief_editor, Codex
- Review mode: external/user review through `check-pack.md` and
  `chatgpt_p5.md`

## Route

1. Locate task pack generator owner.
2. Identify why `source_summary.md` is omitted.
3. Add narrow source-evidence inclusion rule.
4. Extend smoke tests with positive, negative, and client-profile guard checks.
5. Update backlog and task-local review packet.

## Production Boundary

Do not change roles, pipelines, review-gate, lifecycle, client-profile
activation rules, or historical E2E case reports.
