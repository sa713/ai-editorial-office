# Step 3 Role Compression Decisions

## Canonical Ownership

Agent specs now refer briefly to canonical owners instead of repeating them:

- `AGENTS.md` owns global authority, governance, artifact minimalism,
  review-gate, context-loading, and task-local storage invariants.
- Pipelines own sequence, stage routing, process depth, and required stage
  conditions.
- Artifact templates own detailed artifact shape.
- Agent specs own only role-specific consequences, local boundaries, stop
  conditions, inputs, outputs, and quality checks.

## Retained In Every Agent

Each agent spec keeps:

- mission;
- primary responsibilities;
- inputs;
- outputs;
- forbidden actions;
- decision boundaries;
- stop conditions;
- handoff expectations;
- role-specific quality checks.

## Removed Or Replaced By Short Reference

The compressed specs removed repeated local copies of:

- broad `AGENTS.md` compliance lists;
- full lifecycle descriptions;
- pipeline sequence details;
- artifact minimalism policy;
- review-gate policy;
- context-loading policy;
- general governance rules;
- large artifact shape examples already owned by templates.

## Role Boundary Decisions

- Chief Editor remains coordinator and final governance owner, not writer,
  reviewer, researcher, or finalizer.
- Final Editor remains controlled finalizer after review, not governance
  approver.
- Intake remains request normalizer and classifier, not analyst, designer,
  writer, reviewer, or approver.
- Research remains evidence provider, not writer or final wording owner.
- Review remains independent validator, not rewriter or finalizer.
- UX Writer remains interface-copy owner, not general Writer, product manager,
  reviewer, or approver.
- Writer remains draft owner, not researcher, reviewer, UX Writer, finalizer, or
  governance owner.

## Safety-Preserving Compression

Safety-critical prohibitions were retained when they protect role separation,
claim traceability, review independence, governance approval, or product
behavior boundaries. Repeated operational detail was removed only when the rule
already lives in a canonical owner.

## Artifact Depth

The specs keep Step 1 behavior: `review.md` remains mandatory and primary for
low-risk and simple standard review. Optional artifacts remain conditional and
are not silently mandatory.

## Context Loading

The specs no longer reproduce the full Step 2 context-loading profile. They
only reference the canonical rule and name role-local consequences when needed.
