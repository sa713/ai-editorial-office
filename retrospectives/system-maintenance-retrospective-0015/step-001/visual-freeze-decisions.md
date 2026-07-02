# Visual Freeze Decisions

## Decision

The visual subsystem is now frozen / experimental.

It remains in the repository as accumulated knowledge, but it is inactive by
default and does not participate in ordinary editorial work.

## Preserved Knowledge

The freeze preserves:

- `visual_illustration_brief`;
- `visual_article_sketchnote`;
- Artist Agent;
- `visual_concept.md`;
- `illustration_brief.md`;
- `sketchnote_brief.md`;
- `image_prompt.md`;
- `canonical_sketchnote_prompt.md`;
- visual failure patterns.

## Activation Rule

Visual requests no longer activate the visual branch automatically.

Requests such as "make an illustration", "make a visual sketchnote", or
"prepare a visual summary" are not enough.

The visual branch can be used only when the user explicitly asks to:

- use the visual subsystem;
- use Artist Agent;
- launch the visual branch;
- activate a visual mode;
- run the frozen visual subsystem despite its inactive default status.

## Main System

The text editorial system remains the active production system.

Visual knowledge is dormant and can be reactivated later without restoring from
history.

## No Architecture Change

No new replacement architecture was added. This is a status and activation
discipline change only.
