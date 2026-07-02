# Final recommendation

## What to implement now

Implement a bounded improvement iteration focused on five changes:

1. **Compact execution profile**
   Define when low-risk/simple standard tasks can use fewer artifacts, while keeping review required.

2. **Manifest freshness and governance state**
   Add small freshness fields and normalize review/finalization/human approval state.

3. **Artifact ownership map**
   Clarify which documents own invariants, statuses, pipeline sequence, role behavior, templates and editorial knowledge.

4. **Review ergonomics**
   Add compact review shape, independence check and bounded revision fields.

5. **Handoff and custom workflow clarity**
   Separate role handoff, compact final handoff and context-summary. Add mini-contract for custom workflows.

These changes directly address the recurring problems:

- artifact overhead;
- drift;
- stale state;
- review friction;
- ambiguous handoff;
- custom workflow ambiguity;
- governance confusion.

## What to defer

Defer:

- deep consolidation of all pipelines;
- shortening all agent specs;
- rewriting templates broadly;
- markdown regression suite;
- source snapshot strategy;
- automated validators;
- dashboards or metrics;
- migration of legacy tasks.

These may become useful later, but doing them now would expand scope and risk turning the iteration into redesign.

## What not to do

Do not:

- add new agents;
- introduce workflow engine;
- build automation platform;
- create scoring/eval system;
- expand editorial modes;
- add new doctrine without repeated real failures;
- implement enterprise approval matrices;
- make compact path available for high-governance;
- remove review-gate;
- collapse writing and review;
- imply publication approval from finalization.

## Recommended implementation order

1. Artifact ownership map.
2. Compact execution profile.
3. Manifest freshness/governance state.
4. Handoff semantics.
5. Review ergonomics and bounded revision.
6. Custom workflow mini-contract.
7. Source trust rule.
8. Test on new low-risk/simple standard tasks.

## Decision

The next iteration should make the system lighter, not broader.

The best improvement is not "more AI редакция". It is a clearer, smaller operating layer:

- fewer files when risk is low;
- stronger state when work resumes;
- clearer ownership of rules;
- shorter review where appropriate;
- explicit governance where side effects matter.

That is enough for the next step. Everything larger should wait for repeated real failures.
