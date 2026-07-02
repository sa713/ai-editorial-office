# Rollback Notes

To roll back `system-maintenance-retrospective-0013`:

1. Remove the `visual_article_sketchnote` section from
   `editorial_knowledge/20_editorial_modes.md`.
2. Remove the `visual_article_sketchnote` review and prompt-drift checks from
   `editorial_knowledge/40_editorial_review_system.md`.
3. Revert the Artist Agent allowance in `ai-editorial-office/AGENTS.md` so it
   again only accepts the ordinary illustration brief path.
4. Revert `ai-editorial-office/agents/artist_agent.md` to only reference
   `visual_concept.md` and `illustration_brief.md`.
5. Revert `ai-editorial-office/templates/artifacts/image_prompt_template.md` to
   only source from `illustration_brief.md`.
6. Delete `ai-editorial-office/templates/artifacts/sketchnote_brief_template.md`.
7. Optionally keep this retrospective folder as historical record, or delete
   `retrospectives/system-maintenance-retrospective-0013/` if the update should leave no
   trace.

Rollback impact: ordinary text pipelines and the existing
`visual_illustration_brief` path should continue to work either way.
