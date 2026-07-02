# Rollback Notes

To roll back Step 1:

1. In `editorial_knowledge/20_editorial_modes.md`, remove the requirement that
   `visual_article_sketchnote` starts with `visual_concept.md`.
2. Restore the previous `visual_article_sketchnote` behavior where
   `sketchnote_brief.md` could be built directly from the article.
3. In `ai-editorial-office/templates/artifacts/sketchnote_brief_template.md`,
   restore `Source artifact: article or article draft supplied in the task`.
4. Remove the approved-`visual_concept.md` dependency language from the
   sketchnote brief template.
5. In `ai-editorial-office/AGENTS.md`, restore the sketchnote compact path to:
   `article -> sketchnote_brief.md -> Artist Agent`.

Rollback impact: this would bring back the direct article-to-brief path that
Step 1 intentionally removed.
