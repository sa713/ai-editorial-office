# Orchestration Plan

## Routing Decision

- Active role: `chief_editor`
- Task type: article-style explainer / source summary
- Selected pipeline: `article_pipeline`
- Risk mode: low-risk
- Process depth: compact
- Client profile: none
- Visual subsystem: not activated

## Preflight Gate

- Decision: proceed
- Rationale: user supplied a clear source URL, output filename, structure, constraints, language, and target depth.
- Missing data strategy: constrain to the primary roadmap page and directly linked supporting materials that clarify the page's FAQ and recommendations.

## Role Assignment

- `research_agent`: inspect source page and directly linked supporting guides.
- `writer_agent`: synthesize the concept-focused Russian summary.
- `review_agent`: independently check structure, source fidelity, no-copying constraint, and requested scope.
- `final_editor`: produce the final deliverable file after approval.
- `chief_editor`: record governance decision.

## Artifact Plan

Required:

- `brief.md`
- `task-manifest.md`
- `status.md`
- `orchestration_plan.md`
- `sources.md`
- `draft.md`
- `claims-used.md`
- `review.md`
- `vibe-coding-summary.md`
- `final_decision.md`

Omitted:

- `facts.md`, `claims_table.md`: compact evidence is sufficient for a low-risk concept summary, and source claims are tracked in `sources.md` / `claims-used.md`.
- Separate handoff files: compact execution records stage changes in `status.md`, `review.md`, and this plan.

