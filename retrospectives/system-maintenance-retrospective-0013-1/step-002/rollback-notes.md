# Rollback Notes

To roll back Step 2:

1. In `ai-editorial-office/agents/artist_agent.md`, remove the
   `Execution Mode: visual_article_sketchnote` section.
2. Remove the `visual_article_sketchnote` PNG default from the Outputs section.
3. Remove the added sketchnote genre, final-format, HTML/SVG, and artifact-drift
   prohibitions from Forbidden Actions, Stop Conditions, and Quality Checks.
4. In `ai-editorial-office/templates/artifacts/image_prompt_template.md`,
   remove the sketchnote-specific fields:
   - `sketchnote genre constraints`;
   - `handwritten note constraints`;
   - `one-sheet constraints`;
   - `anti-infographic constraints`.
5. Remove the `visual_article_sketchnote` PNG/default-format lines from the
   format section of `image_prompt_template.md`.

Rollback impact: Artist Agent would again have weaker execution guidance for
sketchnote tasks and could more easily drift into infographic/SVG/HTML output.
