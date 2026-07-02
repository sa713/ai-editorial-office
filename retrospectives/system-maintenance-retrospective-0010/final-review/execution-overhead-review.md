# Execution Overhead Review

## Speed

Likely improved for low-risk and simple standard tasks.

Main reason: fewer required artifacts, shorter role specs, shorter templates,
and a bounded read path.

## Restart Friction

Improved.

Restart now starts from:

- `AGENTS.md` or invariant summary;
- `task-manifest.md`;
- latest relevant handoff;
- current working artifact;
- directly relevant pipeline/KB.

Step 6 also prevents reading all old versions by default.

## Artifact Load

Significantly reduced.

Before, task folders tended toward review summary, QA checklist, finalization
notes, finalization checklist, open questions, and handoffs as routine support
files.

Now these are conditional. For compact tasks the likely set is:

- manifest;
- current working artifact;
- `review.md`;
- final artifact;
- final decision evidence.

## Context-Reading Load

Reduced, but not eliminated.

The biggest remaining cost is full pipeline reading. Pipelines are still long
and contain detailed operational rules. That is acceptable for high-governance,
but still heavy for simple tasks.

## Handoff Weight

Lower.

Handoffs are delta records. Compact finalization can skip the finalization
handoff when manifest, review, and final artifact already provide enough state.

Risk: this only works if the manifest is current.

## Net Assessment

Execution overhead decreased materially. The bottleneck shifted from artifact
creation to correct profile selection and manifest freshness.
