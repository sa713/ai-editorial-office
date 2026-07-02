# Compact editorial brief

## Design goals

The compact editorial brief is the smallest useful artifact between intake and writing.

It should:
- convert a request into editorial intent;
- identify the reader task and useful outcome;
- select structure behavior before drafting;
- set narrative density and context limits;
- give review a clear target;
- stay small enough to be created by inference, not manual form-filling.

The brief is not a content plan, taxonomy, approval form, or metadata record. It is a working editorial interpretation of what the text must help the reader do.

## Required editorial signals

Use only signals that change editorial behavior. A viable brief should usually include 5-7 of these:

- **Reader task**: what the reader is trying to understand, decide, do, diagnose, trust, or notice.
- **Useful outcome**: what must be different for the reader after the text.
- **Reader state**: what the reader likely knows, lacks, fears, doubts, or is trying to resolve.
- **Dominant editorial mode**: the main interaction mode the text must serve.
- **Structure behavior**: the expected movement of information, such as answer-first, condition -> action -> result, comparison by criteria, or signal -> relevance -> action.
- **Context limit**: what background is allowed because it changes action, interpretation, risk, or trust.
- **Review target**: the main thing review must verify before the text is accepted.

## Inferred signals

The system should infer as much as possible from the request instead of asking the user to fill fields.

It can infer:
- likely editorial mode from verbs such as choose, explain, announce, compare, diagnose, teach, persuade, review, or orient;
- useful outcome from the requested deliverable and reader action implied by it;
- narrative density from mode and reader urgency;
- structure behavior from the reader task;
- level of context from reader state and risk;
- review emphasis from the dominant mode;
- missing assumptions from gaps between the task, audience, and expected outcome.

Inference should remain editable. If the system is unsure, it should mark uncertainty in the brief rather than expand the brief into a questionnaire.

## Optional signals

Optional signals can improve quality but should not block writing:

- audience segment or role;
- channel or surface;
- source material status;
- tone constraints;
- length or depth target;
- legal, brand, or factual risk;
- stakeholder constraints;
- examples to follow or avoid.

Optional signals become required only when they change usefulness, risk, or structure.

## Editorial mode selection

The brief should name one dominant editorial mode and, when useful, one supporting mode.

The dominant mode controls:
- primary reader outcome;
- opening behavior;
- information order;
- narrative density;
- review priorities.

A supporting mode is allowed when the text must perform a secondary job. For example:
- decision support with trust building;
- change communication with operational instruction;
- educational scaffolding with diagnosis;
- awareness with opinion framing.

The supporting mode must not override the dominant mode. If two modes compete for the opening, structure, or review target, the brief should choose the mode tied to the reader's most urgent task.

## Structure implications

The brief should change structure before drafting begins.

- If the reader needs a decision, structure around recommendation, criteria, comparison, risks, and next action.
- If the reader needs execution, structure around prerequisites, steps, checks, exceptions, and recovery.
- If the reader needs orientation, structure around a small mental model, key parts, and next paths.
- If the reader needs trust, separate claim, evidence, interpretation, limits, and accountability.
- If the reader needs change communication, lead with impact, affected groups, timing, required action, rationale, and support.
- If the reader needs diagnosis, start from observable signals, then differentiators, likely causes, tests, and next actions.
- If the reader needs exploration, map the space by useful dimensions and provide a narrowing path.

Other structural controls:
- narrative density follows mode, not writer preference;
- context is included only when it changes action, interpretation, risk, or trust;
- depth follows reader state and outcome, not topic size;
- ordering follows reader progress, not subject taxonomy;
- explanation strategy should move from the reader's current state toward use.

## Review implications

The brief should give review a target beyond "is the text good?"

Review should check:
- whether the text delivers the stated useful outcome;
- whether the structure follows the dominant mode;
- whether the opening matches reader urgency;
- whether context exceeds the context limit;
- whether each section advances the reader task;
- whether assumptions, risks, and limits are visible when they affect the advice;
- whether the ending gives a next action, decision, stopping point, or usable posture;
- whether any paragraph exists mainly to sound complete, thoughtful, or important.

Mode-specific review should override generic preference. A diagnostic text should be judged by signal differentiation, not elegance. An instruction should be judged by executable sequence, not narrative flow. A decision-support text should be judged by criteria and trade-offs, not coverage.

## Minimal viable brief

Reader task: choose whether to introduce a compact editorial brief before drafting.
Useful outcome: editor can decide what the text must do before writing starts.
Reader state: understands editorial rules but may not want workflow overhead.
Dominant mode: decision support.
Supporting mode: orientation.
Structure behavior: recommendation first, then criteria, trade-offs, and implementation limits.
Context limit: include only context that prevents bureaucracy or essay-mode.
Review target: verify that the brief changes structure and review behavior.
Risk: brief becomes a form instead of an editorial decision artifact.

## Anti-bureaucracy rules

- Do not add a field unless it changes writing, structure, review, risk, or usefulness.
- Do not ask the user for information the system can infer with acceptable confidence.
- Do not block drafting because an optional signal is missing.
- Do not turn modes into a rigid taxonomy; choose the mode that best protects the reader task.
- Do not preserve brief fields that no one uses during drafting or review.
- Do not reward completeness of the brief; reward better editorial decisions.
- Do not make the brief longer than the text's complexity justifies.
- Do not use the brief to document internal process when it should clarify reader usefulness.

The brief should feel like editorial thinking made visible, not administration.

## Failure modes

- **Metadata swamp**: the brief collects audience, channel, tone, stakeholders, stages, risks, and references, but does not change the structure.
- **Fake usefulness**: the useful outcome says "reader understands the topic" without naming what the reader can decide, do, notice, trust, or apply.
- **Mode confusion**: the text claims to support a decision but opens as an educational overview or awareness essay.
- **Context inflation**: background grows because it is relevant to the topic, not because it changes reader action or interpretation.
- **Review drift**: reviewers judge style, completeness, or personal preference instead of the stated reader outcome.
- **Over-inference**: the system silently assumes audience, stakes, or constraints and writes confidently from a weak brief.
- **Rigid workflow**: the brief becomes a mandatory form that slows simple work and encourages mechanical answers.
- **Essay-mode relapse**: the structure follows the topic's conceptual order instead of the reader's task progression.
- **Supporting-mode takeover**: a secondary mode adds explanation, persuasion, or context until the dominant reader task is diluted.
