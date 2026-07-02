# Sketchnote Mode Decisions

## Separate Mode

`visual_article_sketchnote` was added as a separate editorial mode instead of
being folded into `visual_illustration_brief`.

Reason: an ordinary illustration asks what image carries the main meaning of a
text. A sketchnote asks how an attentive reader would summarize the article's
content, structure, relationships, and conclusions on one handwritten sheet.

## Activation Rule

`AGENTS.md` now activates the visual branch in `visual_article_sketchnote` when
the user asks for:

- visual article sketchnote;
- sketchnote;
- handwritten article notes;
- handwritten summary;
- one-sheet notes or note sheet;
- an image as if an attentive reader had summarized the article on one sheet.
- "визуальный конспект статьи";
- "рукописный конспект";
- "конспект на листе";
- "изображение, будто читатель законспектировал статью".

## Mode Boundaries

The mode protects against:

- ordinary article illustration replacing the sketchnote;
- corporate infographic drift;
- poster, ad, comic, or presentation drift;
- invented theses;
- fake handwritten filler;
- overloaded "map of everything" behavior;
- decorative image-making that no longer explains the article.

## Pipeline Decision

No new pipeline was added. The existing visual branch can use a compact path:

`article -> sketchnote_brief.md -> Artist Agent`

This keeps the update small and avoids adding process weight.
