# Handoff: Writer Agent to Artist Agent

- Task ID: TASK-0020
- Date: 2026-06-01
- From: writer_agent
- To: artist_agent
- Current status: writing
- Active visual mode: `visual_article_sketchnote`

## Approved Source Artifacts

- `visual_concept.md`: approved semantic frame.
- `sketchnote_brief.md`: approved sketchnote execution brief.
- `kb/canonical_sketchnote_prompt.md`: canonical genre source.

## Execution Request

Create:

- `image_prompt.md`
- `visual-conspect-blog.png`

Use the approved Russian handwritten phrases from `sketchnote_brief.md`. Keep the final output a horizontal 16:9 PNG and preserve sketchnote genre constraints.

## Boundaries

- Do not reread or reinterpret the source PDF unless required for verification.
- Do not add new article conclusions or extra recommendations.
- Do not turn the result into a corporate infographic, presentation slide, dashboard, poster, comic, or product one-pager.
- Do not deliver SVG/HTML/web page as final output.

## Review Readiness

After rendering, hand off to `review_agent` for compact source-aware review against `visual_concept.md`, `sketchnote_brief.md`, `image_prompt.md`, and the PNG.
