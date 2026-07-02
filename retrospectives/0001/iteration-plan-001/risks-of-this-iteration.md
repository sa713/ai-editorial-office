# Risks of this iteration

## Risk 1: Over-simplification

**Description**

Compact path may remove artifacts that were quietly protecting quality, source traceability or restartability.

**How it could happen**

- low-risk label applied too broadly;
- `qa-checklist.md` omitted even when factual review needs it;
- `sources.md` omitted for material claims;
- handoff skipped despite role transfer.

**Mitigation**

- compact path forbidden for high-governance;
- factual claims still require traceability;
- omitted artifacts need one-line rationale;
- review-gate remains mandatory.

## Risk 2: Hidden governance loss

**Description**

Reducing files may blur finalization, final governance and publication approval.

**How it could happen**

- final artifact appears after compact review;
- final decision says finalized;
- human owner assumes send/publish approval.

**Mitigation**

Every final decision or compact handoff for deliverable content states:

```text
Editorial finalized:
Human approval required:
Publication/delivery approval:
```

## Risk 3: Compact-path abuse

**Description**

Agents may choose compact path to avoid hard work.

**How it could happen**

- source-heavy task called "simple";
- standard task with stakeholder sensitivity treated as low-risk;
- review issues dismissed as non-blocking.

**Mitigation**

Compact path requires rationale. It is forbidden when:

- high-governance;
- source conflict;
- sensitive claims;
- external publication risk;
- unclear human approval;
- multiple audiences with different needs.

## Risk 4: New drift from new terminology

**Description**

Adding `compact`, `normal`, `full`, freshness, ownership and handoff semantics can create new concepts that drift across docs.

**How it could happen**

- pipelines define compact differently;
- review agent interprets compact review differently;
- templates add fields not mentioned in AGENTS.

**Mitigation**

Use artifact ownership map first. Define each new term once and reference it.

## Risk 5: Semantic confusion

**Description**

`compact-handoff`, `handoff-*` and `context-summary` may still be confused.

**How it could happen**

- old task folders provide mixed examples;
- agents imitate legacy artifacts;
- final user handoff used as role handoff.

**Mitigation**

State explicitly:

- `handoff-*` = role-to-role delta;
- `compact-handoff.md` = final user-facing transfer summary;
- `context-summary.md` = recovery artifact after context fragmentation.

## Risk 6: Review becomes too thin

**Description**

Compact review may become a rubber stamp.

**How it could happen**

- verdict without scope;
- no independence check;
- no usefulness check;
- no governance note.

**Mitigation**

Compact review minimum:

- verdict;
- scope reviewed;
- independence check;
- usefulness/pass rationale or blockers;
- governance note;
- next action.

## Risk 7: Bounded revision hides deeper problems

**Description**

Defaulting to bounded revision may avoid needed structural rewrite or new research.

**How it could happen**

- review sees local symptoms but misses root problem;
- repair scope too narrow;
- repeated small fixes accumulate.

**Mitigation**

Bounded by default, not bounded always. Escalate to larger revision when:

- reader outcome fails;
- mode mismatch;
- evidence gap;
- scope conflict;
- repeated failure.

## Risk 8: Ownership map becomes another doctrine layer

**Description**

Ownership map may add another document to maintain instead of reducing duplication.

**How it could happen**

- map repeats all rules;
- every doc still repeats the same rules;
- map is not used when editing.

**Mitigation**

Keep map as a table and rule-placement guide. Do not copy policy text into it.

## Risk 9: Source trust rule becomes security theater

**Description**

Source labels could become ritual labels without changing behavior.

**How it could happen**

- every source line gets labels;
- review checks label existence, not actual instruction leakage;
- agents spend time classifying obvious material.

**Mitigation**

Use labels only where trust boundary matters. Keep general rule simple.

## Risk 10: Delayed deeper consolidation

**Description**

This iteration intentionally avoids deep refactor. Some duplication remains.

**How it could happen**

- quick wins reduce pain enough to postpone necessary consolidation;
- pipelines continue drifting slowly.

**Mitigation**

After testing compact path, run a drift scan. Do not consolidate before seeing how compact changes behave.

## Overall risk rating

Medium.

The iteration is safer than redesign because it avoids new agents, engines and doctrine. Its main risk is not technical; it is semantic. Compactness must not be mistaken for lower standards.
