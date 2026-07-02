# Final Decision

Task ID: `SYSTEM-MAINTENANCE-0003`

Decision owner: `chief_editor`

Decision: `accepted`

## rationale

The review-system had accumulated repeated review logic across `AGENTS.md`, `review_agent.md`, `review_pipeline.md`, and `review_task_template.md`. This increased context load and made future maintenance riskier.

The accepted update applies compression without weakening behavior: detailed review pressure remains canonical in `review_agent.md`; sequencing remains canonical in `review_pipeline.md`; governance invariants remain canonical in `AGENTS.md`; templates now scaffold tasks instead of restating the system.

## consciously not shortened

- Review Agent's detailed review pressure remained mostly intact because it is now the canonical source for review behavior.
- Review Pipeline quality gates remained explicit because they are the operational gate list.
- Governance-level review-gate rules in `AGENTS.md` remained explicit because they are project invariants.

## risks reduced

- Checklist theatre from repeated pressure lists.
- Divergent rule copies across files.
- Higher context cost during review startup.
- Template inflation causing agents to read scaffolding as policy.
- Maintenance drift after future review updates.
