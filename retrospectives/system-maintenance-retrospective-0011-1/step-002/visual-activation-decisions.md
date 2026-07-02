# Visual Activation Decisions

## Primary Decision

Visual branch activation belongs to Chief Editor during orchestration.

This avoids a second decision path and keeps visual work inside the existing task orchestration contract.

## Activate When

Activate the visual branch when a task requires a meaningful illustration for a text, such as:

- article;
- longread;
- analytical material;
- educational material;
- important announcement;
- publication where the illustration must carry the text's meaning.

## Do Not Activate When

Do not activate the visual branch for:

- purely technical image generation;
- simple decorative images;
- tasks where the visual meaning is already fully defined in the direct request;
- cases where direct prompt preparation is enough without editorial analysis.

## Compact Visual Path

For low-risk or simple illustration tasks, Chief Editor may choose a compact visual path:

`text` -> `visual_concept.md` -> `illustration_brief.md` -> Artist Agent

This is not a new pipeline. It is a bounded process-depth choice within ordinary orchestration.

## Artist Agent Gate

Artist Agent cannot be assigned unless the visual branch is activated.

Even after activation, Artist Agent still requires approved:

- `visual_concept.md`;
- `illustration_brief.md`.

## Boundary Decision

No special exceptions were created for article, longread, announcement, education, or analysis as separate workflows. They are examples only. The decision criterion is whether the illustration must carry text meaning.
