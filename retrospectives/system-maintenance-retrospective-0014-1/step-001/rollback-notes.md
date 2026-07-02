# Rollback Notes

To roll back Step 1:

1. Delete `ai-editorial-office/kb/canonical_sketchnote_prompt.md`.
2. In `ai-editorial-office/agents/artist_agent.md`, remove references to
   `kb/canonical_sketchnote_prompt.md`.
3. Remove the canonical prompt priority and protection language from Artist
   Agent.
4. In `ai-editorial-office/templates/artifacts/image_prompt_template.md`, remove
   the canonical prompt source fields and priority notes.
5. Leave `visual_concept`, `sketchnote_brief`, review system, pipelines, visual
   modes, and ordinary illustration branch unchanged.

Rollback impact: `visual_article_sketchnote` would return to generic
sketchnote generation logic without a canonical prompt source.
