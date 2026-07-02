# Step 1 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011.1 / step-001`

Focus: legalize Artist Agent as a bounded non-MVP extension role for illustration-to-text tasks.

Goal: remove the conflict between `ai-editorial-office/agents/artist_agent.md` and the active-role policy without making Artist Agent part of ordinary text tasks.

## Discovery

Conflicting language was found in:

- `ai-editorial-office/AGENTS.md`;
- `ai-editorial-office/pipelines/article_pipeline.md`;
- `ai-editorial-office/pipelines/social_pipeline.md`;
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`;
- `ai-editorial-office/pipelines/research_pipeline.md`;
- `ai-editorial-office/pipelines/review_pipeline.md`.

The conflict was not that Artist Agent lacked a role file. The conflict was that global and pipeline wording still treated every non-MVP role as forbidden in all cases.

## Implementation Steps

1. Update `AGENTS.md` to keep the MVP set unchanged for ordinary text tasks.
2. Add a default rule: non-MVP extension roles are forbidden unless explicitly legalized.
3. Legalize Artist Agent only for illustration-to-text tasks with approved `visual_concept.md` and approved `illustration_brief.md`.
4. State that Artist Agent is not a semantic editor, reviewer, writer, designer, comic artist, or presentation designer.
5. Replace pipeline absolute non-MVP bans with default bans plus explicitly legalized extension exceptions.
6. Do not change Artist Agent, visual templates, review system, or pipelines structurally.

## Non-Goals

- No new agents.
- No Artist Agent changes.
- No new pipeline.
- No comics.
- No presentations.
- No review-system changes.
- No visual-branch expansion.
- No Artist Agent use for ordinary text tasks.

## Status

Completed.
