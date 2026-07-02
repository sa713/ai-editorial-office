# Meaning Preservation Decisions

## Primary Decision

Add a bounded review check for meaning preservation across:

`visual_concept.md` -> `illustration_brief.md` -> `image_prompt.md`

The check verifies semantic continuity only. It does not review the finished image or artist performance.

## Review Object

The review object is the artifact chain:

- `visual_concept.md`;
- `illustration_brief.md`;
- `image_prompt.md`.

The review object is not:

- a generated image;
- drawing quality;
- artist skill;
- composition;
- color;
- style;
- technique.

## Review Dimensions

The bounded chain check covers:

- meaning continuity;
- viewer takeaway continuity;
- metaphor continuity;
- distortion introduction;
- constraint preservation;
- prompt drift;
- boundary protection.

## Repair Ownership

If meaning drift appears after `visual_concept.md`, repair the downstream artifact where the drift was introduced:

- fix `illustration_brief.md` if the drift appears there;
- fix `image_prompt.md` if the brief is sound but the prompt drifted.

Do not change `visual_concept.md` to accommodate later drift.

## Boundary Decision

The review must remain editorial and semantic.

It must not become:

- image quality review;
- art direction;
- Artist QA;
- artistic critique;
- composition review;
- color review;
- style review;
- drawing-quality review;
- comic work;
- presentation work.

## Deferred Work

Still deferred:

- image quality review;
- Artist QA pipeline;
- comic workflows;
- presentation workflows;
- art-direction methodology.
