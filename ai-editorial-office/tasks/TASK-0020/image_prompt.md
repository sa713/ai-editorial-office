# Image Prompt

## source brief

- Active visual mode: `visual_article_sketchnote`
- Source `illustration_brief.md`: not applicable
- Source `visual_concept.md`, if applicable; required for `visual_article_sketchnote`: `visual_concept.md`
- Source `sketchnote_brief.md`: `sketchnote_brief.md`
- Source `kb/canonical_sketchnote_prompt.md`, required for `visual_article_sketchnote`: `../../kb/canonical_sketchnote_prompt.md`
- Canonical sketchnote prompt status: manually supplied
- Approval status: approved for Artist Agent execution

## visual goal

- Goal from the approved brief: create one horizontal 16:9 handwritten-style visual article sketchnote for blog publication, showing that AI agents are already an enterprise digital workforce while visibility, ownership, runtime controls, traceability, and governance lag behind autonomous behavior.

## prompt

- Executable image prompt:

```text
Create one cohesive horizontal 16:9 sketchnote as if an attentive Russian-speaking reader summarized the article on a single notebook sheet.

The image should feel hand-drawn: warm off-white paper, imperfect marker/pen lines, loose arrows, underlines, labels, small visual metaphors, slightly uneven boxes, and visible relationships between ideas. It must not feel like a corporate infographic, slide, poster, UI dashboard, card set, product one-pager, comic, or glossy AI collage.

Central idea: AI agents are already part of the enterprise digital workforce, but visibility, ownership, runtime controls, audit trails, and governance are not yet mature enough for autonomous behavior.

Loose layout:
- Center: "AI agents = цифровая рабочая сила"; small agent nodes moving around a dashed old perimeter; label "риск смещается к действиям".
- Top: adoption note with "43%: > половины сотрудников" and "много платформ".
- Left: visibility/accountability: foggy map, missing pins, "shadow AI", "нет полной карты", "владелец?".
- Right: behavior/incidents: agent crosses a boundary, alert triangle, clock, "53%: выход за рамки", "47%: инциденты", "часы/дни".
- Bottom: new control loop: "реестр + владельцы + runtime-контроль + логи + traceability".
- Bottom-right: compliance stamp/checklist: "compliance - не стратегия", "13% готовы".

Keep text sparse and readable. Use Russian handwritten labels exactly from the brief where possible. Use arrows to show: adoption -> fragmented platforms -> visibility gaps -> scope violations/incidents -> need agent-specific controls. Include small visual metaphors only where they clarify the article's argument.
```

## required elements

- Elements that must appear:
  - AI-agent digital workforce cluster.
  - Dashed intended-scope boundary or old perimeter.
  - Visibility/inventory gap.
  - Shadow AI / unclear owner.
  - Scope violation and incident exposure.
  - New control model: registry, ownership, runtime controls, logs, traceability.
  - Compliance as an incomplete starting point.
- Meaning each element protects:
  - The article's central claim that autonomous agent behavior changes the security surface.
  - The link between fragmented adoption and governance gaps.
  - The distinction between compliance alignment and operational readiness.
- For sketchnote, required short handwritten phrases:
  - "AI agents = цифровая рабочая сила"
  - "риск смещается к действиям"
  - "много платформ"
  - "shadow AI"
  - "нет полной карты"
  - "границы нарушаются"
  - "инциденты: часы/дни"
  - "compliance - не стратегия"
  - "нужны: реестр + владельцы + runtime-контроль + traceability"

## forbidden distortions

- Do not change: agent adoption is already operational, not merely future-facing.
- Do not intensify: do not make AI agents look evil or malicious by nature.
- Do not weaken: do not hide the control, traceability, and governance gap.
- Do not add: vendor claims, threat actors, breach scenarios, product dashboards, or invented recommendations.

## text-on-image rules

- Text allowed in image: yes, only controlled sketchnote labels.
- Required text, if any: see required short phrases.
- For sketchnote, controlled handwritten content from `sketchnote_brief.md`: use sparse Russian labels and numeric anchors only.
- Forbidden text: filler handwriting, lorem ipsum, long paragraphs, product slogans, unsupported claims.

## format/aspect ratio

- Format: PNG
- Aspect ratio: 16:9
- Size or platform constraint, if provided: blog publication; use 1600x900.
- For `visual_article_sketchnote`, standard final result: PNG.
- For `visual_article_sketchnote`, not final output: HTML, SVG, web page, interactive artifact.
- SVG intermediate allowed only if the environment requires it: not used.

## sketchnote genre constraints

- Canonical source: `ai-editorial-office/kb/canonical_sketchnote_prompt.md`.
- If canonical prompt exists and is not empty with manually supplied prompt content beyond the placeholder, it has priority over generic sketchnote generation logic.
- Do not replace, summarize, optimize, rewrite, or reinterpret the canonical prompt contents.
- Must look like one handwritten article sketchnote: yes.
- Must feel like notes made by an attentive reader: yes.
- Must not feel like work by a designer, analyst, marketer, product team, or presentation author: yes.

## handwritten note constraints

- Handwritten note qualities to preserve: imperfect, warm, human, sparse, visually connected.
- Liner drawing qualities to preserve: simple black/ink lines with a few muted accent colors.
- Required controlled handwritten phrases: see required elements.
- Fake handwriting or filler text to avoid: any random pseudo-text.

## one-sheet constraints

- One sheet of paper: yes.
- One coherent spread: yes.
- Arrows, labels, and relationships between ideas: required.
- Small visual metaphors: required where meaning-critical.
- Live thinking-process feeling: required.

## anti-infographic constraints

- Do not make an infographic: keep loose, handwritten, and non-grid.
- Do not make a presentation slide: avoid polished hierarchy and slide-title feel.
- Do not make a poster, ad, or corporate one-pager: no promotional hero layout.
- Do not make a UI mockup, card set, digital scheme, web page, or interactive artifact: no UI chrome or repeated cards.
- Avoid strict grid, perfect alignment, symmetry, identical blocks, corporate design feeling, and AI-collage feeling.

## style constraints, only if given

- Provided style constraint: hand-drawn sketchnote / visual notes / notebook sketch.
- Source of constraint: user request and canonical sketchnote prompt.
- Do not infer additional style: no.

## unresolved questions

- Missing or conflicting execution detail: none blocking.
- Required owner or decision: none.
- Safe fallback if approved: deterministic local PNG rendering with readable Russian labels.
