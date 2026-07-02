# Handoff: Research Agent to Review Agent

- Task ID: TASK-0024
- From: research_agent
- To: review_agent
- Current status recommendation: review
- Date: 2026-06-04

## artifacts created

- `sources.md`
- `research.md`
- `executive-summary.md`
- `behavioral-audit.md`
- `systemic-errors.md`
- `useful-mechanisms.md`
- `top-3-improvements.md`

## review scope

Review the audit package against:

- user request;
- `brief.md`;
- `orchestration_plan.md`;
- evidence sample and limitations in `sources.md`;
- requirement not to change existing system files;
- requirement to evaluate system behavior rather than individual text quality.

## key confidence notes

- Strong confidence for patterns in formal-cycle tasks with review and final
  decision artifacts.
- Medium confidence for transition/direct tasks because many lack full lifecycle
  evidence.
- Supporting maintenance tasks are used as evidence of system learning, not as
  the primary behavior sample.

## requested checks

- Are all six requested deliverable classes present?
- Are findings about repeated system behavior rather than isolated text taste?
- Are top-three improvements prioritized and justified?
- Are limitations clear?
- Are recommendations only, with no system changes made?

## stop conditions

- Block if a required section is missing.
- Block if recommendations rely on unsupported claims.
- Block if the audit implies system changes were implemented.
