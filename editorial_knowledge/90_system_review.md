# Editorial system review

## System purpose

The system is a compact editorial operating layer for AI-driven writing. It solves a specific problem: AI text often sounds coherent while failing to help the reader decide, act, diagnose, trust, or apply anything.

Its difference from generic AI writing systems is that it does not start from format, tone, or content type. It starts from reader task, intended usefulness, editorial mode, structure behavior, and review against outcome.

## Strong architectural decisions

- **Usefulness-first hierarchy**: usefulness is treated as the highest editorial value, above coverage, polish, and writer preference.
- **Structure-from-intent**: structure is chosen from reader task and mode, not from genre templates.
- **Compact editorial brief**: the brief is small enough to be inferred and used, but strong enough to change drafting and review.
- **Editorial modes instead of formats**: the system distinguishes interaction behavior rather than article, post, memo, or instruction.
- **Mode-specific review**: review criteria change by mode, which prevents generic quality checks from flattening the work.
- **Anti-essay controls**: answer delay, context inflation, completeness theater, and pseudo-depth are named as failure patterns.
- **Anti-nitpicking rules**: review is prevented from becoming taste-based rewriting.
- **Inference-first philosophy**: the system avoids turning intake into a heavy form.

## System coherence

The operational files are mostly coherent. Rules, modes, brief, and review all reinforce the same behavior: identify reader task, select useful structure, limit context, and verify outcome.

The compact brief connects well to review: the brief defines reader task, mode, structure behavior, context limit, and review target; the review system uses exactly those inputs.

The modes support structure logic well. Decision support, instruction, trust building, change communication, diagnosis, and exploration all produce distinct ordering behavior.

The strongest hidden tension is between anti-essay discipline and modes that legitimately need narrative or explanation: awareness, persuasion, trust building, educational scaffolding, and opinion framing.

The weakest coherence point is the early scaffold files. `01_principles.md`, `02_editorial_intent.md`, and `03_usefulness_review.md` currently contain headings only, while later files already define much of their substance. They are harmless, but their role is unclear.

## High-leverage components

- `10_operational_rules.md`: gives concrete editorial decisions and anti-patterns that can directly shape writing.
- `20_editorial_modes.md`: changes the system from format selection to reader interaction behavior.
- `30_compact_editorial_brief.md`: creates the practical bridge between intake and drafting.
- `40_editorial_review_system.md`: prevents review from collapsing into style cleanup.

The highest-leverage idea is the combination of dominant mode, structure behavior, context limit, and review target. That small set can prevent most essay-mode drift.

## Weak points

- **Ambiguity handling**: the system says uncertainty should be marked, but does not yet show how to proceed when reader task or audience is genuinely ambiguous.
- **Confidence handling**: trust and evidence are addressed, but there is no compact rule for how confident the system may be under incomplete evidence.
- **Emotional and narrative pacing**: the system protects against fluff, but could under-support texts where pacing, reassurance, or emotional sequencing is part of usefulness.
- **Hybrid modes**: dominant/supporting mode logic exists, but conflicts between modes are not tested in real examples.
- **Reader energy**: the system discusses overload, but does not yet model fatigue, urgency, skim behavior, or willingness to engage.
- **Source constraints**: evidence integrity is mentioned, but source-poor and source-heavy tasks may need different review behavior.

## Missing capabilities

The system may later need:
- a small set of worked examples showing brief -> structure -> review;
- a compact ambiguity protocol for incomplete requests;
- guidance for acceptable confidence and uncertainty language;
- one practical test cycle on real tasks;
- a way to retire or merge rules that stop changing behavior.

These should remain practical additions, not new layers.

## Risk of doctrine inflation

The system can degrade if every edge case becomes a new rule or mode. The current mode set is already near the useful upper limit. More modes could create classification work instead of editorial clarity.

Doctrine inflation would look like:
- adding modes for every content situation;
- adding rules that repeat existing rules in narrower language;
- expanding review triggers into a checklist;
- turning optional signals into required fields;
- documenting every exception instead of using editorial judgment.

The system should resist growth unless a new concept changes structure, review, or usefulness in a way existing concepts cannot.

## Risk of bureaucracy

The largest bureaucracy risk is the compact brief becoming a form. If every task requires filling reader state, dominant mode, supporting mode, structure behavior, context limit, review target, risk, audience, tone, channel, and evidence status, the system will slow down and produce mechanical thinking.

Bureaucracy would also appear if review must explicitly answer every question every time. The review layer should guide judgment, not become a ritual.

The guardrail is simple: if a field or check does not change writing or review, it should not be required.

## Risk of essay-mode relapse

Essay-mode can return even with the rules because models tend to produce coherent exposition when the brief is weak.

Likely relapse paths:
- the reader task is stated vaguely as "explain" or "write about";
- the dominant mode is omitted or inferred too broadly;
- context limit is not enforced during drafting;
- the writer uses topic taxonomy as outline;
- review praises completeness or flow;
- supporting educational or awareness mode overtakes decision, instruction, or change communication.

The most dangerous relapse is polished usefulness theater: the text appears thoughtful, structured, and complete, but does not change what the reader can do.

## Risk of over-correction

The system strongly fights essay-mode, context inflation, and fake depth. That is useful, but it can over-correct.

Over-correction risks:
- explanation becomes too thin for learning tasks;
- trust building loses necessary evidence and limitation handling;
- persuasion loses emotional pacing and reader stakes;
- awareness becomes abrupt and fails to create relevance;
- opinion framing becomes too procedural and loses interpretive force;
- nuance is removed even when it changes risk or decision quality.

The fix is not more context. The fix is mode-aware permission: narrative, explanation, and nuance are allowed when they directly support the dominant mode's reader outcome.

## Operational viability

The system is viable for controlled real-task testing now. It is strong enough to run intake -> compact brief -> draft structure -> usefulness review on actual editorial tasks.

It is not yet fully production-proven. The doctrine is clear, but it has not been stress-tested against messy inputs, conflicting stakeholders, weak source material, or high-emotion communication.

The best current use is guided editorial work: create a compact brief, draft from the mode, then review against reader outcome.

## Real-world pressure points

The system will be stressed by:
- vague requests such as "make this better" or "write an article about X";
- stakeholder-driven texts that want persuasion while pretending to inform;
- sensitive change communication with bad news or incomplete details;
- expert educational content where necessary context looks like essay-mode;
- trust-building tasks with weak evidence;
- hybrid tasks such as "explain the change and convince people to adopt it";
- short-form content where structure must be compressed into very few lines;
- Russian business writing where канцелярит can hide responsibility and action.

These tasks will reveal whether the system can preserve usefulness without becoming rigid.

## Simplification opportunities

- Clarify or fill the scaffold files `01_principles.md`, `02_editorial_intent.md`, and `03_usefulness_review.md`, or acknowledge them as placeholders.
- Merge repeated anti-essay language across rules, brief, and review if duplication starts causing maintenance drift.
- Keep the mode list stable; avoid adding micro-modes.
- Use one compact example per major mode instead of writing more doctrine.
- Treat optional signals as truly optional in all future documents.

No major simplification is needed yet, but the system should now move from doctrine-writing to usage.

## Recommended next step

Run one real editorial task through the system end to end:

1. infer a compact editorial brief;
2. choose dominant and supporting mode;
3. generate structure from the brief;
4. draft or revise the text;
5. review it using the review system;
6. record where the doctrine helped, slowed down, or failed.

This is more valuable than adding another layer. The next learning should come from operational friction, not more theory.

## Long-term risks

- **Layer accumulation**: new documents keep appearing faster than the system is used.
- **Mode ossification**: modes become labels to satisfy instead of thinking tools.
- **Review conservatism**: reviewers reject strong, compact writing because it does not look complete enough.
- **Brief formalism**: the brief becomes a required artifact even for simple tasks.
- **Doctrine drift**: repeated concepts slowly diverge across files.
- **Context allergy**: the system becomes hostile to legitimate explanation, nuance, and emotional pacing.
- **False confidence**: inference-first behavior may hide uncertainty unless the system is trained to expose weak assumptions.
- **Maintenance neglect**: unused rules remain in place and make the system feel heavier than it is.
