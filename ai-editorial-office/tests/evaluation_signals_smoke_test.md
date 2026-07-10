# Evaluation Signals Smoke Test

Date: 2026-07-10

Release: `S5.R2 - Evaluation Signals`

Status: passed

## Purpose

Validate the advisory Evaluation Signal contract against the eight required
synthetic scenarios. These cases test evidence handling, owner routing, noise,
contradictions, and non-decision behavior. They do not prove actual system
improvement, capability value, Domain Pack value, architecture drift, or
release quality.

## Pass contract

Every material signal must preserve:

- a human decision question;
- observation separated from interpretation;
- exact evidence pointers;
- bounded scope/comparison window;
- denominator or exposure opportunity when material;
- missing, excluded, or ambiguous cases;
- alternatives and contradictions;
- confidence and unknowns;
- existing owner;
- optional human consideration;
- explicit non-decision.

Any case fails if it produces a score, KPI, target, threshold, rank, maturity
level, individual performance measure, automatic release verdict, automatic
priority, automatic capability/pack retirement, or automatic canon/backlog/
roadmap/memory change.

## Case 1: Repeated successful release

### Synthetic evidence

- Three comparable capability releases completed the same lifecycle.
- All three passed repository validation and independent review.
- All three were accepted by the Project Lead.
- Two have saved later-use evidence: one beneficial, one mixed.
- The third has no later-use evidence.

### Evaluation Signal view

- Decision question: Is the release approach producing evidence-backed value
  consistently enough to preserve?
- Observation: three releases passed and were accepted; later-use effect is
  beneficial once, mixed once, and unknown once.
- Scope/comparison: three comparable capability releases; not Domain Pack or
  maintenance releases.
- Interpretation: the lifecycle appears repeatable; realized value is not
  uniformly demonstrated.
- Alternative: Project Lead acceptance may reflect release quality, while the
  mixed/unknown effects may reflect task opportunity or incomplete capture.
- Confidence: `supported` for repeatable release mechanics; `plausible` for
  system improvement.
- Existing owners: release artifacts, Review Agent, Project Lead, affected
  capability owners.
- Human consideration: preserve the current lifecycle and seek comparable use
  evidence before a stronger value claim.
- Explicit non-decision: the next release is not accepted automatically and no
  canon, backlog, roadmap, or capability action occurs.

### Result

Pass. Success count is separated from realized value and future acceptance.

## Case 2: Repeated rejected release

### Synthetic evidence

- Three comparable release candidates received `Changes Requested`.
- Two shared an unsupported owner-boundary claim.
- One failed for stale source evidence.
- All three were repaired before later acceptance.

### Evaluation Signal view

- Decision question: Is repeated rejection exposing a preventable production
  problem, a healthy gate, or both?
- Observation: two comparable owner-boundary findings recur; one different
  source-freshness finding occurred; review prevented all three from advancing.
- Scope/comparison: three comparable release candidates and their repair rounds.
- Interpretation: the owner-boundary recurrence may justify prevention review;
  the rejection count also shows the gate working.
- Alternative: a changed task mix or stricter review could increase rejection
  without declining production quality.
- Confidence: `supported` for owner-boundary recurrence; `unsupported` for a
  general decline claim.
- Existing owners: Review Agent/Review Pipeline, relevant canonical owner,
  Learning Framework for reuse.
- Human consideration: compare the two findings and consider a bounded owner-
  scoped clarification only if duplication checks support it.
- Explicit non-decision: future releases are not rejected automatically and no
  new gate or rule appears.

### Result

Pass. Rejection is not treated as a one-directional failure metric.

## Case 3: Domain Pack rarely activated

### Synthetic evidence

- Cybersecurity Domain Pack activated once in 20 total tasks.
- Only two tasks were security-sensitive enough to present an activation
  opportunity.
- One used the pack beneficially; the other correctly did not activate because
  ordinary research was sufficient.

### Evaluation Signal view

- Decision question: Is the pack rarely activated because it lacks value or
  because relevant tasks are rare?
- Observation: activation is 1/20 overall but 1/2 among plausible exposure
  opportunities; one beneficial use exists.
- Missing cases: no evidence about future high-risk security tasks.
- Interpretation: total-task frequency is misleading; no retirement concern is
  supported.
- Alternative: routing could still miss some unrecognized security-sensitive
  tasks; S5.R4 may later examine task-need recognition.
- Confidence: `supported` for correct bounded use; `unsupported` for retirement.
- Existing owners: Domain Pack Standard, Cybersecurity pack, Learning
  Framework.
- Human consideration: take no action; observe future comparable opportunities.
- Explicit non-decision: no retirement, ranking, activation threshold, or
  roadmap action.

### Result

Pass. Denominator and opportunity prevent a vanity-frequency inference.

## Case 4: Domain Pack frequently activated

### Synthetic evidence

- Software Architecture Domain Pack activated in 8 of 10 architecture-sensitive
  tasks.
- Effect notes: beneficial in three, mixed in two, burdensome in one, unknown
  in two.
- Two tasks did not activate and still passed review.

### Evaluation Signal view

- Decision question: Does frequent activation indicate reliable usefulness or
  unnecessary defaulting?
- Observation: activation is frequent, but effects vary and two non-activated
  tasks succeeded.
- Interpretation: the pack is relevant often; evidence does not support making
  it mandatory or declaring uniform value.
- Alternative: beneficial effects may cluster in higher-complexity tasks while
  burden appears in simpler work.
- Confidence: `supported` for relevance; `plausible` for a routing-scope
  refinement question.
- Existing owners: Domain Pack Standard, Software Architecture pack, Learning
  Framework.
- Human consideration: compare task complexity in future actual-use evidence.
- Explicit non-decision: no mandatory activation, pack promotion, ranking, or
  automatic content change.

### Result

Pass. Frequency is contextualized by actual effects and non-activated success.

## Case 5: Repeated architecture warning

### Synthetic evidence

- Three release reviews identify duplicated canonical ownership.
- The same two owner files and maintainability/reviewability scenario recur.
- One fourth release appears similar but is a local reference, not duplicate
  ownership.

### Evaluation Signal view

- Decision question: Is architectural drift beginning around canonical
  ownership?
- Observation: three comparable warnings share owner, driver, and quality
  scenario; one superficially similar case is non-applicable.
- Interpretation: an architecture pattern candidate is supported, but the exact
  repair remains an architecture-owner judgment.
- Contradiction: the fourth case shows wording similarity alone is insufficient.
- Confidence: `supported` for recurring risk; no confidence assigned to a
  preferred repair.
- Existing owners: Architecture Review, `AGENTS.md` owner map, Learning
  Framework.
- Human consideration: inspect the three evidence chains and consider a
  separate bounded owner update.
- Explicit non-decision: no canon edit, gate, backlog entry, or roadmap change
  occurs automatically.

### Result

Pass. Architecture significance stays scenario-based and qualitative.

## Case 6: Stale knowledge repeatedly detected

### Synthetic evidence

- Three tasks flag the same external source version as stale.
- Two tasks verify a newer official source; one cannot access it.
- Current canon still points to the old version.

### Evaluation Signal view

- Decision question: Should the current canonical owner be verified and
  corrected?
- Observation: repeated freshness warnings plus two authoritative replacement
  checks support an owner investigation.
- Missing case: one access failure does not contradict the newer source.
- Interpretation: a correction or supersession candidate is supported.
- Confidence: `verified` that current citation is stale; `supported` that the
  newer source fits, pending owner review.
- Existing owner: the canonical file that cites the source; Learning Framework
  for correction/supersession disposition.
- Human consideration: open a bounded reviewed owner patch.
- Explicit non-decision: no silent deletion, retirement, memory sync, or canon
  edit happens from the signal view.

### Result

Pass. Repetition supports verification and routing, not automatic mutation.

## Case 7: Noisy metric that should be ignored

### Synthetic evidence

- A proposed metric counts markdown files created per release.
- Release types, artifact requirements, file size, decision value, duplication,
  and review quality are not recorded.
- More files could represent traceability or process bloat.

### Evaluation Signal view

- Decision question: none beyond "Are more files better?"
- Observation: an activity count exists without an outcome, comparable scope,
  denominator, or causal interpretation.
- Interpretation: not decision-useful.
- Confidence: `unsupported` as a quality or improvement signal.
- Existing owner: none needed; artifact minimalism already governs file value.
- Human consideration: ignore/reject the proposed metric.
- Explicit non-decision: do not add the count to a Release Pack, KPI, dashboard,
  rank, target, or acceptance decision.

### Result

Pass. The metric is rejected rather than normalized into a signal.

## Case 8: Contradictory signals

### Synthetic evidence

- Review time fell across four releases.
- Changes-requested findings rose across the same releases.
- Release scope and reviewer changed after release two.
- Post-acceptance user value evidence exists only for one release.

### Evaluation Signal view

- Decision question: Is the release process becoming faster without losing
  quality?
- Observations: review time decreased; findings increased; scope and reviewer
  changed; realized value evidence is sparse.
- Comparison limit: the four releases are not fully comparable.
- Interpretations: faster preparation may coexist with stronger review; broader
  scope or reviewer difference may explain more findings; quality change is
  unresolved.
- Confidence: `verified` for the two observations, `unsupported` for a causal
  quality trend.
- Existing owners: Review Agent/Review Pipeline, release artifacts, Project
  Lead.
- Human consideration: collect comparable scope and repair-outcome evidence or
  take no action.
- Explicit non-decision: do not average the signals, compute a health score,
  change the review gate, or accept/reject future releases automatically.

### Result

Pass. Contradictions are preserved and reduce confidence instead of being
collapsed.

## Summary matrix

| Case | Evidence/context preserved | Existing owner preserved | No score/KPI/rank | No automatic action | Result |
| --- | --- | --- | --- | --- | --- |
| Repeated successful release | yes | yes | yes | yes | pass |
| Repeated rejected release | yes | yes | yes | yes | pass |
| Rare Domain Pack activation | yes | yes | yes | yes | pass |
| Frequent Domain Pack activation | yes | yes | yes | yes | pass |
| Repeated architecture warning | yes | yes | yes | yes | pass |
| Repeated stale knowledge | yes | yes | yes | yes | pass |
| Noisy metric | yes | yes | yes | yes | pass |
| Contradictory signals | yes | yes | yes | yes | pass |

## Final smoke-test result

All eight cases pass.

The cases demonstrate that Evaluation Signals can inform a human question while
remaining optional, evidence-backed, reviewable, qualitative where required,
and non-decisional. They also demonstrate that synthetic success is not real
usage evidence and cannot confirm system improvement.
