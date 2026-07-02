# Step 3 Agent Diff

The local repository exposes `ai-editorial-office/` as untracked, so an exact
tracked `git diff` baseline is unavailable. This file records the per-agent
semantic diff for every changed file under `ai-editorial-office/agents/*.md`.

## Line Count Diff

| File | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `ai-editorial-office/agents/chief_editor.md` | 401 | 132 | -269 |
| `ai-editorial-office/agents/final_editor.md` | 433 | 122 | -311 |
| `ai-editorial-office/agents/intake_agent.md` | 515 | 116 | -399 |
| `ai-editorial-office/agents/research_agent.md` | 525 | 122 | -403 |
| `ai-editorial-office/agents/review_agent.md` | 615 | 130 | -485 |
| `ai-editorial-office/agents/ux_writer.md` | 477 | 121 | -356 |
| `ai-editorial-office/agents/writer_agent.md` | 494 | 123 | -371 |
| Total | 3460 | 866 | -2594 |

## `ai-editorial-office/agents/chief_editor.md`

```diff
- 401-line coordinator spec with repeated artifact minimalism, required KB,
- required pipelines, structure-before-writing, review requirements, context
- loading, prompt behavior, failure behavior, and artifact shape details.
+ 132-line Chief Editor spec focused on orchestration mission,
+ responsibilities, inputs, outputs, forbidden actions, decision boundaries,
+ stop conditions, handoff expectations, and role-specific quality checks.
+ Preserves: pipeline/risk/process-depth ownership, MVP role routing, review
+ gate enforcement, final governance readiness, no writing/research/review/
+ finalization by Chief Editor.
```

## `ai-editorial-office/agents/final_editor.md`

```diff
- 433-line finalization spec with repeated governance, artifact minimalism,
- context loading, review requirements, and detailed finalization artifact
- templates.
+ 122-line Final Editor spec focused on controlled post-review finalization.
+ Preserves: no new claims, no meaning changes, no governance approval, no
+ review bypass, conditional finalization notes/checklist only when justified.
```

## `ai-editorial-office/agents/intake_agent.md`

```diff
- 515-line intake spec with repeated global policy, pipeline reading, context
- loading, review requirements, prompt/failure behavior, and long artifact shape
- examples.
+ 116-line Intake spec focused on raw-request normalization, initial
+ classification, risk proposal, bootstrap artifacts, ambiguity surfacing, and
+ handoff to Chief Editor.
+ Preserves: Intake does not research, analyze, design, write, review, finalize,
+ approve, or start production.
```

## `ai-editorial-office/agents/research_agent.md`

```diff
- 525-line research spec with repeated AGENTS/pipeline/context/review blocks and
- detailed research artifact templates.
+ 122-line Research spec focused on evidence collection, source reliability,
+ confidence, contradictions, claim traceability, stop conditions, and downstream
+ evidence handoff.
+ Preserves: Research does not write, review, finalize, decide final wording, or
+ approve readiness.
```

## `ai-editorial-office/agents/review_agent.md`

```diff
- 615-line review spec with repeated global governance, context loading,
- artifact minimalism, prompt/failure behavior, QA checklist, review summary,
- and reviewer notes scaffolds.
+ 130-line Review spec focused on independent validation, required `review.md`,
+ deterministic outcome, bounded findings, optional review artifacts only when
+ justified, and high-governance traceability.
+ Preserves: Review remains mandatory, Reviewer does not rewrite, research,
+ finalize, or approve governance/publication.
```

## `ai-editorial-office/agents/ux_writer.md`

```diff
- 477-line UX writer spec with repeated global policy, pipeline/context loading,
- artifact minimalism, review requirements, prompt/failure behavior, and UX
- artifact shape examples.
+ 121-line UX Writer spec focused on interface copy, product context,
+ terminology, state coverage, accessibility, unresolved UX questions, and
+ review handoff.
+ Preserves: UX Writer does not become general Writer, product manager,
+ designer, researcher, reviewer, finalizer, or approver.
```

## `ai-editorial-office/agents/writer_agent.md`

```diff
- 494-line writer spec with repeated global governance, artifact minimalism,
- context loading, review requirements, prompt/failure behavior, and writing
- artifact shape examples.
+ 123-line Writer spec focused on drafting from approved evidence, brief, KB,
+ tone/glossary constraints, claim caveats, review handoff, and stop conditions.
+ Preserves: Writer does not research, review, finalize, approve, create
+ `final.md`, or silently change scope/audience/channel.
```
