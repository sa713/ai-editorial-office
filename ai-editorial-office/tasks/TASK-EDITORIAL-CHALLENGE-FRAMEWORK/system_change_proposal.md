# Editorial Challenge Framework Proposal

## proposed model

Add an assumptions-based `Editorial Challenge Lens` to Review Agent's existing
review behavior. It lives inside `review.md`, not in a new artifact.

The lens does not ask Reviewer to argue with Chief Editor or Writer Agent. It
asks Reviewer to test the stability of the accepted editorial decision:

> The chosen route remains valid while these assumptions hold. If one of these
> assumptions no longer holds, another route may become stronger.

This makes challenge less subjective. Reviewer is not trying to prove personal
preference. Reviewer is checking whether the premises that made the chosen route
reasonable are still true under the brief, sources, Problem Hypothesis,
Editorial Decision Frame, draft, risks, and reader outcome.

## compact review shape

For ordinary tasks, embed this compact section in `review.md`:

```markdown
## editorial challenge

- Decision under challenge:
- Chosen route remains valid while:
  - Assumption:
  - Assumption:
  - Assumption:
- Challenge conditions:
  - If ..., then ... route would become stronger.
  - If ..., then ... route would become stronger.
- Assumption check: `holds` / `partially_changed` / `changed`
- Evidence:
- Required action:
```

For very simple low-risk tasks where route and draft are obvious, the section
can be one line:

```markdown
- Editorial challenge: core assumptions still hold; no evidence-backed
  condition makes an alternative route stronger.
```

For high-governance or conflict-heavy tasks, `reviewer-notes.md` may hold
additional assumption reasoning, but only when the reasoning would make
`review.md` too large. It remains optional and task-local.

## where assumptions live

The assumptions block is part of the existing `Editorial Challenge Lens` inside
`review.md`.

Do not create a separate `challenge_assumptions.md`. Do not put assumptions in
`orchestration_plan.md` as a new Chief Editor obligation. Chief Editor already
records the selected route, alternatives, Writer contract, review focus, and
reroute triggers in the Editorial Decision Frame. Reviewer derives challenge
assumptions from those saved decisions during review.

This keeps ownership clean:

- Problem Hypothesis states the bounded hypothesis about the user's likely
  editorial need.
- Editorial Decision Frame states the chosen route and why it should serve the
  task.
- Editorial Challenge Lens extracts the route's stability assumptions and tests
  whether they still hold.

## relationship to Problem Hypothesis and Editorial Decision Frame

The assumptions block must not duplicate either upstream mechanism.

It should not restate the full Problem Hypothesis. It should ask whether the
draft and evidence still fit the hypothesis confidence and respect boundary.

It should not restate the full Editorial Decision Frame. It should extract only
the assumptions that make the chosen route valid.

Example:

- Problem Hypothesis: the request appears to need service clarity before PR
  copy.
- Editorial Decision Frame: chosen route is a working framework, not PR
  materials.
- Challenge assumption: this route remains valid while the source lacks approved
  messages, channels, owners, metrics, or publication-ready claims.
- Challenge condition: if approved messages and channels are present in the
  saved evidence, then PR-copy route may become stronger.

## keeping assumptions compact

Limit the assumptions block to:

- 2-4 route-validity assumptions;
- 1-3 challenge conditions;
- one evidence line or short evidence bullets.

Each assumption should be one line. Each condition should use an
`If..., then...` form.

Long reasoning belongs in the normal findings section, `reviewer-notes.md`, or
task-local analytical support only when risk or conflict justifies it. The
assumptions block is a stability check, not an essay.

## how Reviewer determines that a condition occurred

A challenge condition counts as occurred only when saved artifacts show it.

Valid evidence includes:

- `brief.md`;
- `orchestration_plan.md`;
- Problem Hypothesis, when implemented;
- Editorial Decision Frame;
- research, facts, sources, claims table, or claims-used;
- Writer/UX Writer handoff;
- draft or UX artifact under review;
- explicit user instruction or approval evidence saved in the task.

Invalid evidence:

- Reviewer preference;
- plausible but unsourced organizational diagnosis;
- assumptions from chat memory not saved in artifacts;
- "another version would be nicer";
- new research performed by Reviewer.

The Reviewer must ask:

1. Which assumption made the route valid?
2. What artifact would show the assumption no longer holds?
3. Is that artifact already present?
4. Does the changed assumption materially affect route, draft, evidence,
   governance, or reader outcome?

If the answer to step 3 is no, Reviewer may record uncertainty, request evidence
repair, or escalate. Reviewer must not invent the condition.

## questions Reviewer asks Chief Editor

Reviewer challenges the route's assumptions, not Chief Editor's authority.

Core questions:

- What assumptions make the selected route valid?
- Are those assumptions visible in the Problem Hypothesis, Editorial Decision
  Frame, research, source boundary, or brief?
- Which assumption, if false, would make a rejected alternative stronger?
- Did Chief Editor's reroute triggers already name this condition?
- Did the task proceed even though a reroute trigger has occurred?
- Does the chosen route still fit risk mode, approval boundary, and evidence
  state?
- Does the route depend on an unsupported assumption about user intent,
  evidence, audience, source maturity, or implementation readiness?

The objection must cite saved artifacts. It is not enough to say that another
route is attractive.

## questions Reviewer asks Writer

Reviewer tests whether Writer preserved or broke the route assumptions.

Core questions:

- Did the draft stay inside the assumptions that made the route valid?
- Did the draft introduce material that changes those assumptions, such as
  unsupported claims, implementation decisions, channels, owners, promises, or
  metrics?
- Did rejected alternatives reappear in a way that invalidates the route?
- Does the draft still serve the Problem Hypothesis and Editorial Decision
  Frame?
- Did the draft expose a missing assumption that Chief Editor should revisit?
- Is any weak section repairable within the current route, or does it show that
  a route assumption changed?
- Would a reasonable reader get the outcome promised by the route?

Reviewer may name the needed repair but must not write the replacement
material. Short examples are allowed only to clarify a finding.

## boundary between challenge and rewriting

Challenge is allowed:

- identify route-validity assumptions;
- state compact challenge conditions;
- test conditions against saved artifacts;
- cite evidence that an assumption holds or changed;
- assign severity;
- name repair owner;
- define bounded repair scope;
- define re-review scope.

Rewriting is forbidden:

- produce replacement draft sections;
- choose final wording;
- design a new editorial route as the active route;
- replace Chief Editor's route with Reviewer's preference;
- perform new research;
- finalize the material;
- approve governance.

Reviewer can say:

> The working-framework route remains valid while the source lacks approved
> channels and publication-ready claims. The draft introduces channel-specific
> launch recommendations not supported by `facts.md`; this changes the route
> assumption and requires Writer repair or Chief Editor reroute.

Reviewer must not say:

> I would make this a campaign plan instead.

## when assumptions are preserved

Reviewer should approve or record only a non-blocking note when:

- route-validity assumptions still hold;
- the draft stays inside those assumptions;
- alternatives are possible but no challenge condition occurred;
- any weakness is stylistic, preference-based, or immaterial;
- risks are visible and properly caveated;
- uncertainty is labeled and does not undermine the route.

Principle: an alternative route becoming imaginable is not enough. An
alternative route becomes stronger only when a named challenge condition has
occurred.

## when this leads to changes_requested

Use `changes_requested` when an assumption changed or partially changed, but the
problem is repairable inside the current architecture.

Typical cases:

- Writer violated the route assumption by adding unsupported claims,
  implementation details, promises, channels, owners, or metrics.
- Draft drifted toward a rejected alternative but can be brought back to the
  approved route.
- Evidence exists but was misused or overclaimed.
- A missing caveat makes the route appear more certain than the frame allowed.
- A route assumption needs clarification in `orchestration_plan.md`, handoff, or
  Writer notes, but the selected route is still plausibly valid.

Repair owner may be Writer, UX Writer, Research Agent, or Chief Editor depending
on whether the issue is wording, evidence, or route framing.

## when this leads to blocked

Use `blocked` when the changed assumption prevents deterministic review under
the current route.

Typical cases:

- A challenge condition shows the selected route is no longer supportable, and
  Chief Editor must adjudicate before writing can continue.
- The route depends on evidence or approval that is missing and cannot be
  repaired in the current pass.
- The task now requires user choice because deliverable, audience, approval
  boundary, or scope would change.
- Review independence, active version, or required artifacts cannot be
  established.
- The same assumption failure remains unresolved after one bounded
  repair/adjudication cycle.

`blocked` is not punishment. It means the assumptions that made the route
reviewable no longer support deterministic approval.

## Chief Editor response to changed assumptions

When Reviewer shows that a route assumption changed, Chief Editor should respond
through existing governance:

1. Accept the changed assumption and update `orchestration_plan.md`, Editorial
   Decision Frame, handoff, or route as needed.
2. Reject the challenge with artifact-backed rationale showing that the
   assumption still holds or the condition is immaterial.
3. Return to Research Agent if evidence is missing or conflicting.
4. Return to Writer/UX Writer if execution violated the route while the route
   itself remains valid.
5. Ask the user if the changed assumption affects deliverable, audience,
   approval boundary, or task scope.
6. Set or maintain `blocked` when no deterministic route decision is possible.

Chief Editor does not need to accept Reviewer's preferred alternative. Chief
Editor must answer whether the assumption changed and what that means for the
recorded route.

## disagreement resolution

Use a bounded dispute protocol.

1. Reviewer records assumptions, challenge conditions, evidence, result, repair
   owner, and re-review scope in `review.md`.
2. If assumptions hold, outcome may be `approved` if other checks pass.
3. If an assumption changed but repair is bounded, outcome is
   `changes_requested`.
4. If an assumption changed and route adjudication or user decision is required,
   outcome is `blocked` or `human_approval_required` as allowed by current
   status rules.
5. Chief Editor responds with artifact-backed acceptance, rejection, reroute,
   research return, writer repair, user escalation, or block.
6. Re-review is bounded to the changed assumption and affected artifacts.
7. If the same assumption dispute remains unresolved after one repair or
   adjudication cycle, Chief Editor records a final route decision or escalates.

This prevents endless debate: Reviewer tests assumptions once per review cycle;
Chief Editor owns route adjudication; Review Agent owns whether the reviewed
artifact can pass under the recorded route and assumptions.

## deterministic outcome mapping

The challenge lens does not add review outcomes.

| Assumption check | Meaning | Review outcome |
| --- | --- | --- |
| `holds` | Route-validity assumptions remain true. | `approved`, if other checks pass |
| `partially_changed` | A route assumption is weakened, but repair is bounded. | `changes_requested` or non-critical finding by impact |
| `changed` | A route assumption failed materially. | `changes_requested`, `blocked`, or human escalation by impact |

Reviewer must choose severity from assumption impact, not preference.

## production files likely to change

Minimal implementation would touch:

- `ai-editorial-office/agents/review_agent.md`
  - add assumptions-based Editorial Challenge responsibility, boundaries,
    challenge questions, and outcome mapping.
- `ai-editorial-office/pipelines/review_pipeline.md`
  - add the assumptions lens to review quality gates and compact review minimum.
- `ai-editorial-office/templates/tasks/review_task_template.md`
  - add embedded `## editorial challenge` assumptions section to `review.md`
    scaffold.
- `ai-editorial-office/AGENTS.md`
  - short governance note that review includes evidence-backed assumption
    challenge while preserving role boundaries.

Probably not needed in the first pass:

- `chief_editor.md`
  - Chief Editor already owns route adjudication and final governance. Add only
    if implementation needs explicit assumption-dispute wording there.
- `writer_agent.md`
  - Writer already receives findings and must not self-review. Add only if
    testing shows writers need explicit challenge-response behavior.
- `handoff_template.md`
  - Existing review handoff can already carry outcome, repair owner, and
    re-review scope.

## new artifacts

No new mandatory production artifact is needed.

Use existing `review.md`. Optional `reviewer-notes.md` may hold detailed
assumption reasoning only when downstream, high-governance, conflict, or
traceability needs justify it. Do not create mandatory `challenge.md` or
`challenge_assumptions.md`.

## lifecycle change

Current lifecycle remains:

```text
writing / ux-writing -> review -> changes_requested or approved or blocked ->
finalization -> Chief Editor governance
```

Proposed change inside review:

1. Review readiness and independence checks.
2. Standard compliance/evidence/source checks.
3. Editorial Challenge Lens:
   - extract route-validity assumptions;
   - define challenge conditions;
   - test whether conditions occurred;
   - map result to existing review outcome.
4. Deterministic outcome: `approved`, `changes_requested`, or `blocked`.
5. Bounded repair or finalization path.

No new status, role, gate, or default review cycle is added.

## why this is better than the previous model

The previous model asked Reviewer to make the strongest evidence-backed
objection. That improved ordinary checklist review, but still left room for a
taste-based editorial dispute.

The assumptions model is stronger because it makes challenge conditional:

- first identify why the chosen route was valid;
- then state what would make it invalid or weaker;
- then check artifacts for those conditions;
- then route the outcome deterministically.

This turns challenge into a stability test. Reviewer is not arguing "my route is
better." Reviewer is saying "the chosen route depended on X; X no longer holds,
so the route needs repair or adjudication."

## why this does not break architecture

- It strengthens the existing Review Agent role instead of adding a new role.
- It uses existing `review.md`.
- It preserves the review-gate and existing outcomes.
- It keeps Reviewer from writing, routing, finalizing, or governing.
- It remains artifact-backed and deterministic.
- It naturally consumes Problem Hypothesis and Editorial Decision Frame without
  duplicating them.
- It improves trust in approved work because approval means the route survived
  an assumptions check, not only a compliance checklist.
- It scales down for simple tasks and scales up only when risk or conflict
  justifies optional notes.

## design self-check

- Less subjective than preference challenge: pass.
- Built around route assumptions: pass.
- No duplication of Problem Hypothesis or Editorial Decision Frame: pass.
- No new roles: pass.
- No review-gate change: pass.
- No mandatory new artifact: pass.
- Reviewer does not become Writer: pass.
- Reviewer does not become Chief Editor: pass.
- Pipeline determinism preserved: pass.
