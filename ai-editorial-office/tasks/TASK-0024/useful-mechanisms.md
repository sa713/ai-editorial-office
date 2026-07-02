# Каталог сильных решений

## 1. Review gate

Evidence: `TASK-0001`, `TASK-0002`, `TASK-0003`, `TASK-0004`, `TASK-0006`,
`TASK-0021`, `TASK-0022`, `TASK-0023`.

Value:

- prevents finalization without independent validation;
- catches unsupported certainty;
- makes residual risks explicit;
- separates editorial approval from publication approval.

## 2. Source boundary

Evidence: `TASK-0004B`, `TASK-0005`, `TASK-0006`, `TASK-0021`, `TASK-0022`,
`TASK-0023`.

Value:

- lets Chief Editor safely omit external research;
- protects against added mechanics, promises, dates, links, and commitments;
- gives Review Agent a clear pass/fail basis.

## 3. Claims table / claims-used discipline

Evidence: `TASK-0001`, `TASK-0002`.

Value:

- turns factual caution into reviewable evidence;
- blocks broad AI/productivity claims;
- lets writing use safe claims without burying caveats;
- makes review findings precise and repairable.

## 4. Structure-before-writing

Evidence: `SYSTEM-MAINTENANCE-0004`, `TASK-0004B`, `TASK-0006`, `TASK-0007`,
`TASK-0021`.

Value:

- catches reader-path problems before prose;
- reduces duplicated explanation;
- makes operational documents usable selectively;
- gives Writer Agent section roles and reading mode before drafting.

## 5. Bounded revision

Evidence: `TASK-0002`, `TASK-0003`, `TASK-0003B`, `TASK-0009`.

Value:

- prevents review findings from becoming uncontrolled rewrites;
- keeps the repair scope small;
- preserves what already works;
- lowers risk of new defects.

## 6. Reader-state and usefulness checks

Evidence: `TASK-0004`, `TASK-0005`, `TASK-0006`, `TASK-0007`, `TASK-0008`.

Value:

- shifts the system from "nice text" to "reader can act";
- exposes answer delay;
- blocks corporate filler;
- supports channel-specific writing.

## 7. Relevance / replaceability pressure

Evidence: `SYSTEM-MAINTENANCE-0001`, `TASK-0003B`, `TASK-0007`.

Value:

- prevents generic format-purpose copy;
- asks whether the text belongs to this release/material;
- catches pleasant but replaceable announcements.

## 8. Final decision boundary language

Evidence: `TASK-0001`, `TASK-0003`, `TASK-0006`, `TASK-0008`, `TASK-0009`,
`TASK-0021`, `TASK-0022`, `TASK-0023`.

Value:

- protects against false publication approval;
- records what is and is not ready;
- makes placeholders and human decisions visible;
- closes lifecycle without pretending external approval exists.

## 9. Compact mode

Evidence: `TASK-0021`, `TASK-0022`, `TASK-0023`.

Value:

- preserves review and governance while avoiding early-task heaviness;
- embeds checklist in `review.md` when a separate QA file is not useful;
- keeps small tasks restartable without overproducing artifacts.

## 10. Visual semantic ownership path

Evidence: `TASK-0020`.

Value:

- prevents raw PDF-to-image production;
- separates source reading, visual concept, sketchnote brief, image prompt,
  execution, and review;
- keeps visual output tied to article meaning rather than decorative summary.

## 11. Maintenance as learning loop

Evidence: `SYSTEM-MAINTENANCE-0001` to `0004`, `0016`, `0018`.

Value:

- system fixes are based on observed failures;
- redundancy is compressed rather than endlessly added;
- canonical ownership reduces policy drift;
- normalized brief contract addresses a real intake/routing weakness.

## mechanisms with limited value

These are useful only when justified:

- separate `qa-checklist.md` for low-risk tasks;
- separate `review-summary.md` when `review.md` already contains next action;
- finalization notes when finalization is a direct copy from approved draft;
- broad handoff chains for single-step compact tasks;
- full facts/claims/source stack when the source boundary is closed and no new
  factual claims are introduced.
