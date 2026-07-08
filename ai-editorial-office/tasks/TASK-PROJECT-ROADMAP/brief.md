# Brief

## Task Identity

- Task ID: `TASK-PROJECT-ROADMAP`
- Task title: Introduce Project Roadmap
- Task type: documentation-only system strategy document update

## User Goal

Create `ai-editorial-office/ROADMAP.md` as the strategic roadmap for AI
Editorial Office and add lightweight navigation so future work can discover it.

## Audience

- Primary: future Codex/editorial-system maintainers.
- Secondary: project lead reviewing whether future work fits strategy.

## Deliverables

- `ai-editorial-office/ROADMAP.md`
- Lightweight discoverability updates where appropriate:
  - root `README.md`
  - `ai-editorial-office/project-state.md`

## Source Boundary

- Project lead instructions in the current task.
- Existing roadmap/backlog content in `ai-editorial-office/ideas/master_backlog.md`.
- Canonical ownership and operational boundaries in `ai-editorial-office/AGENTS.md`.

## Constraints

- Documentation only.
- Do not redesign the system.
- Do not modify architecture.
- Do not change behavior.
- Do not make `ROADMAP.md` a canonical operational owner.
- Do not reference the roadmap from every document.
- Do not touch `/about`.
- Do not touch `diff_intake.md`.
- Do not touch `/Users/sa/Documents/codex/redaction`.
- Do not touch legacy repository content.

## Acceptance Criteria

- `ROADMAP.md` exists and preserves the roadmap meaning without inventing or
  removing roadmap items.
- Formatting, readability, and section consistency are improved.
- The roadmap is discoverable through lightweight navigation.
- The roadmap is explicitly treated as strategy, not operational canon.
- Required validation commands pass.
- Final commit hash is reported.
