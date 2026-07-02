# Rollback Notes

To roll back Step 1:

1. In `ai-editorial-office/AGENTS.md`, remove the visual subsystem frozen /
   experimental status language.
2. Restore automatic visual activation rules for:
   - `visual_illustration_brief`;
   - `visual_article_sketchnote`.
3. Restore the compact visual path wording so it is no longer gated by explicit
   frozen-subsystem activation.
4. In `ai-editorial-office/agents/artist_agent.md`, remove the frozen /
   experimental status paragraph.
5. In `editorial_knowledge/20_editorial_modes.md`, remove the inactive-by-default
   status notes from the two visual modes.

Rollback impact: visual branch can again activate automatically when a request
matches visual illustration or sketchnote behavior.
