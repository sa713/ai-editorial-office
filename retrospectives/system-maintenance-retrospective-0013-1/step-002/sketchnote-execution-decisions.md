# Sketchnote Execution Decisions

## Decision

Artist Agent now has a distinct execution mode:

`visual_article_sketchnote`

This mode is about the visual result genre, not about changing the article
meaning, `visual_concept.md`, or `sketchnote_brief.md`.

## Core Principle

The result should look as if an intelligent, attentive reader read the article
and summarized it for themselves in a notebook.

Not like a designer.

Not like an analyst.

Not like a marketer.

Like a reader.

## Required Sketchnote Signals

The execution mode requires:

- one sheet of paper;
- one coherent spread;
- handwritten notes;
- liner drawings;
- arrows;
- labels;
- visible relationships between ideas;
- small visual metaphors;
- live thinking-process feeling.

## Genre Prohibitions

The execution mode forbids sketchnote drift into:

- infographic;
- presentation slide;
- poster;
- advertising image;
- corporate one-pager;
- UI mockup;
- set of cards;
- digital scheme;
- web page;
- interactive artifact.

## Visual Prohibitions

The mode avoids:

- strict grid;
- perfect alignment;
- symmetrical structure;
- identical repeated blocks;
- presentation feeling;
- corporate design feeling;
- AI-collage feeling.

## Output Format Decision

For `visual_article_sketchnote`, the standard final image result is PNG.

HTML, SVG, web page, and interactive artifact are not final results for this
mode. SVG may be used only as an internal intermediate if the environment
requires it, but the deliverable remains PNG.

## Prompt Template Decision

`image_prompt_template.md` now includes sketchnote-specific fields:

- sketchnote genre constraints;
- handwritten note constraints;
- one-sheet constraints;
- anti-infographic constraints.

These fields are used only when active visual mode is
`visual_article_sketchnote`.
