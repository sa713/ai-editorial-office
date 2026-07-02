# Canonical Sketchnote Integration Decisions

## Decision

Created:

- `ai-editorial-office/kb/canonical_sketchnote_prompt.md`

The file is a placeholder only. The user will manually supply and maintain the
actual canonical prompt later.

## Source Role

For `visual_article_sketchnote`, Artist Agent now uses:

- approved `visual_concept.md`;
- approved `sketchnote_brief.md`;
- `kb/canonical_sketchnote_prompt.md`.

## Priority Rule

When the canonical prompt exists and is not empty with manually supplied prompt
content beyond the placeholder, it has priority over generic sketchnote
generation logic.

The placeholder itself is not the working prompt.

## Protection Rule

Artist Agent must not replace, summarize, optimize, rewrite, reinterpret, or
reinvent the canonical prompt's execution style.

## Template Integration

`image_prompt_template.md` now has a required canonical prompt source field for
`visual_article_sketchnote`, plus status marking:

- missing;
- placeholder only;
- manually supplied.

## Boundary

This step only integrates the canonical prompt as a source. It does not fill or
edit the prompt and does not change the semantic artifacts.
