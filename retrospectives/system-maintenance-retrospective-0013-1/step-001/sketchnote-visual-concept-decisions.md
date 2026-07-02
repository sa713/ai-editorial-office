# Sketchnote Visual Concept Decisions

## Decision

`visual_article_sketchnote` now requires `visual_concept.md` before
`sketchnote_brief.md`.

Reason: direct `article -> sketchnote_brief.md` allowed meaning extraction and
visual execution to collapse into one artifact. That made it easier for the
system to drift into infographic or SVG/HTML production.

## Meaning of `visual_concept.md` in This Mode

For `visual_article_sketchnote`, `visual_concept.md` is not the same as the
ordinary metaphorical illustration concept.

It is the semantic frame of the article and should fix:

- central idea;
- 5-10 key meaning blocks;
- relationships between ideas;
- author conclusions;
- what the viewer should remember;
- emotional or intellectual feeling of the material.

## Relationship to Article

The article remains the source of truth.

`visual_concept.md` extracts and stabilizes the article's semantic frame.
`sketchnote_brief.md` then translates that approved frame into one-sheet
handwritten sketchnote form.

## Relationship to Ordinary Illustration

The ordinary `visual_illustration_brief` branch remains unchanged:

`text -> visual_concept.md -> illustration_brief.md -> Artist Agent`

The sketchnote branch now mirrors the same meaning-before-execution discipline:

`article -> visual_concept.md -> sketchnote_brief.md -> Artist Agent`

The difference is what `visual_concept.md` contains. For illustration it
stabilizes a visual meaning and metaphor. For sketchnote it stabilizes the
article's conceptual structure and conclusions.
