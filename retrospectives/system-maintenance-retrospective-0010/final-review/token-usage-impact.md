# Token Usage Impact

## Biggest Savings

1. Role specs compression.

Agent specs dropped from 3460 to 866 lines. This is the clearest recurring
token win.

2. Template compression.

Templates dropped from 5767 to 1735 lines. This reduces scaffolding load and
prevents templates from acting like mini-charters.

3. Short context path.

Restart and stage transition no longer require reading the whole project,
all pipelines, all agent specs, all old tasks, or all versions.

4. Artifact depth normalization.

Low-risk/simple standard tasks no longer need separate review summary, QA
checklist, finalization checklist, open questions, or finalization notes by
default.

## Medium Savings

- Compact finalization shape.
- Conditional finalization handoff.
- Current-version pointer discipline for refinement loops.

These save tokens mostly in later-stage or version-heavy work.

## Remaining Waste

- `AGENTS.md` is still 882 lines.
- Pipelines are still long: article 564, social 656, UX 621.
- `project_tree.md` is large and should not be part of normal restart.
- Editorial knowledge remains broad; careless search can still pull too much.

## Net Assessment

Token usage should drop meaningfully in routine work. The largest remaining
waste is accidental broad reading, not artifact creation.
