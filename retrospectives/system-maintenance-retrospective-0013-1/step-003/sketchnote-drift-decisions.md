# Sketchnote Drift Decisions

## Decision

Added failure pattern:

`Sketchnote → Infographic Drift`

The pattern names a real production failure observed in `TASK-0017`: the
system recognized a sketchnote request but produced infographic/SVG/HTML and
corporate one-pager behavior instead of a handwritten reader's note sheet.

## Scope

The pattern applies only to:

`visual_article_sketchnote`

It does not apply to ordinary illustration tasks. Ordinary visual illustration
can still use its existing meaning-preservation path without inheriting
sketchnote-specific constraints.

## Failure Definition

The failure appears when the editorial system formally works on a sketchnote,
but the output looks like:

- infographic;
- presentation slide;
- corporate one-pager;
- UI-like scheme;
- designed visualization;
- SVG/HTML/web artifact as the main result.

## Diagnostic Emphasis

The pattern helps future editors ask whether the result still looks like notes
made by an attentive reader, or whether it has become clean corporate design.

## Repair Emphasis

The repair starts by returning to the approved `visual_concept.md`, then
checking sketchnote constraints and removing grid/card/corporate/presentation
language from the execution layer.

The fix is genre restoration, not adding a new architecture.
