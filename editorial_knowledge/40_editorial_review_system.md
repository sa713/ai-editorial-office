# Editorial review system

## Review philosophy

Editorial review exists to verify usefulness, not to make text sound more polished.

Successful review answers one question: does the text help the reader complete the reader task and reach the intended outcome?

Review should:
- protect the reader task;
- verify structure-from-intent;
- catch essay-mode relapse;
- check whether evidence, context, and explanation are sufficient for the mode;
- trigger revision only when the text fails an editorial job.

Review should not:
- rewrite for personal taste;
- optimize style before usefulness;
- demand context for completeness;
- turn every text into an essay;
- reward sophistication that does not help the reader.

## Review goals

- Confirm that the text serves the compact editorial brief.
- Confirm that the dominant editorial mode controls structure and review behavior.
- Confirm that the reader can do, decide, understand, diagnose, trust, apply, or explain what the brief promised.
- Remove or revise material that delays, blurs, or weakens usefulness.
- Preserve working structure even when a prettier structure is possible.

## Review decision hierarchy

Review decisions should follow this priority order:

1. **Usefulness**: does the text help the reader accomplish the task?
2. **Reader outcome**: does the text produce the intended change in reader understanding, decision, action, trust, or capability?
3. **Mode fit**: does the text behave according to the dominant editorial mode?
4. **Structural correctness**: does information move in the order the reader needs?
5. **Evidence and reasoning integrity**: are claims, interpretation, limits, and recommendations supported and separable?
6. **Execution clarity**: can the reader follow steps, distinctions, criteria, or signals without guessing?
7. **Context discipline**: is background limited to what changes action, interpretation, risk, or trust?
8. **Language clarity**: are sentences and terms clear enough for the task?
9. **Stylistic polish**: can wording be improved without changing the editorial behavior?

Lower-priority concerns must not override higher-priority success. A stylistically plain text that delivers the reader outcome is better than an elegant text that misses the task.

## Review inputs

Review must use:
- compact editorial brief;
- reader task;
- intended useful outcome;
- reader state;
- dominant editorial mode;
- supporting editorial mode, if present;
- structure behavior;
- context limit;
- operational editorial rules;
- source or evidence constraints when they affect trust or risk.

If these inputs are missing, review should infer cautiously and flag uncertainty only where it affects an editorial decision.

## Core review questions

- What reader task is this text supposed to support?
- What should the reader be able to do, decide, understand, diagnose, trust, apply, or explain after reading?
- Does the opening match the reader's urgency and mode?
- Does the structure move from reader need to useful outcome?
- Does each section perform a distinct reader-useful job?
- Is context included because it changes the reader's action, interpretation, risk, or trust?
- Are claims, evidence, interpretation, and recommendations separated where trust matters?
- Does the ending give a next action, decision, stopping point, or usable posture?
- Is any part present mainly to sound complete, thoughtful, or important?

## Mode-specific review behavior

- **Operational instruction**: judge sequence, prerequisites, observable results, exception handling, and whether the reader can execute without interpretation.
- **Decision support**: judge recommendation visibility, criteria, trade-offs, alternatives, assumptions, risks, and next action.
- **Trust building**: judge evidence quality, provenance, limits, safeguards, accountability, and whether confidence matches proof.
- **Change communication**: judge impact clarity, affected groups, timing, required action, unchanged areas, rationale placement, and support paths.
- **Awareness**: judge signal strength, relevance, proportionality, reader posture, and whether the text lands on attention, action, or deliberate non-action.
- **Diagnosis**: judge observable signals, differentiators, evidence thresholds, uncertainty, likely causes, tests, and escalation paths.
- **Educational scaffolding**: judge prerequisites, mental model size, example quality, transfer to use, and whether the reader can apply the concept.
- **Exploration**: judge boundaries, useful dimensions, distinct paths, narrowing logic, and whether curiosity becomes navigable.
- **Opinion framing**: judge clarity of lens, separation of fact and interpretation, limits of the frame, and whether the frame can be tested against the case.
- **Diagnostic analysis**: judge whether the text preserves the raw state of the idea, separates observed, implied, inferred, and hypothetical material, and avoids hidden solutioning.

Mode-specific criteria should override generic review habits. Do not review an instruction for narrative richness or a decision-support text for encyclopedic coverage.

For `diagnostic_analysis` tasks, review may add a bounded diagnostic pass:
- **Distinction integrity**: are observed, implied, inferred, and hypothetical points visibly separated?
- **Artificial completion check**: is the editorial system analyzing the idea, or quietly designing it?
- **Uncertainty preservation**: did uncertainty remain visible, or were gaps automatically fixed?
- **Hypothesis discipline**: if development is suggested, is it marked as a hypothesis or clarification direction rather than a ready solution?
- **Rawness preservation**: does the result still show the real state of the materials, or has it become too mature?
- **Confidence proportionality**: does conclusion strength match the materials, or were supported conclusions weakened without reason?
- **Disclaimer inflation**: is uncertainty repeated across sections instead of grouped into one useful limitation block?
- **Usefulness preservation**: can the reader still draw a conclusion, make a decision, or identify the next step?
- **Defensive weakening**: are evident conclusions turned into weak hypotheses, excessive "requires clarification" notes, or self-protective writing?

Use these heuristics only when the task asks for diagnostic analysis of raw or incomplete materials. Do not turn them into a universal checklist, scoring system, confidence matrix, or formal evidence audit. They must not ban uncertainty, demand aggressive confidence, encourage speculative conclusions, or weaken Artificial Concept Completion safeguards.

For `author_concept_diagnosis` tasks, review may add a bounded conceptual pass:
- **Central thought clarity**: does the idea have a central thought, or does it fall into separate observations, wishes, or concerns?
- **Problem vs solution confusion**: are the problem, solution, tool, and desired effect distinct, or are they mixed together?
- **Mechanism visibility**: is it clear why or how the idea is expected to work?
- **Audience definition**: is it clear who the idea is for and whose behavior, state, or understanding should change?
- **Expected change**: is it clear what should change if the idea works?
- **Success criterion**: is it clear how the author would know the idea is working?
- **Boundary clarity**: does the idea have scope, limits, or constraints, or is it trying to explain or solve everything at once?
- **Conceptual mixing**: are diagnosis, goals, processes, values, and implementation details kept distinct?

Use these heuristics only to help the author see what is undefined, mixed, absent, disconnected, or not yet distinguished in the idea. Do not turn them into a mandatory checklist, consulting canvas, maturity model, taxonomy system, scoring tool, or artificial sophistication exercise. They should support author-facing diagnosis, not ideation consulting.

When reviewing `author_concept_diagnosis` output, use a minimal authorship check:
- **Authorship preservation**: does the idea still read as the author's idea, or has conceptual ownership shifted to the editorial system?
- **Diagnosis vs invention**: does the output show the state of the idea, or assemble a new construction for the author?
- **Conceptual visibility**: does the author see what is mixed, absent, undefined, mechanically unclear, boundary-less, or missing a success criterion?
- **Suggestion boundaries**: do suggestions appear as questions, hypotheses, clarification prompts, or directions to test, rather than finished solution design?
- **Usefulness to the author**: would the author understand their own idea better after reading, or mainly receive someone else's concept?

This check must not ban development suggestions, hypotheses, or next-step recommendations. It should catch editorial takeover and hidden consulting drift while keeping review compact, editorial-first, and specific to `author_concept_diagnosis`; it must not become a workflow, scoring model, maturity review, coaching session, or ideation methodology.

For `visual_illustration_brief` outputs, especially `visual_concept.md`, review may add a bounded semantic visual-concept pass:
- **Meaning integrity**: does the concept preserve the text's main meaning, avoid adding a new meaning, and keep the main conclusion visible?
- **Viewer takeaway integrity**: does the 3-5 second viewer takeaway match what the text actually wants to say?
- **Metaphor quality**: does the metaphor carry the meaning, avoid first-obvious banality, and avoid reducing the text to caricature?
- **Distortion check**: did the concept introduce extra meanings, false emphasis, tone distortion, or visual completion of the author's idea?
- **Misreading risk**: does the review identify what the viewer may misunderstand and where the strongest misreading risks are?
- **Visual usefulness**: would the concept help someone understand, become interested in, or retain the text's meaning rather than merely produce a beautiful picture?
- **Boundary protection**: does the review stay away from style, composition, color, drawing technique, artist skill, and artistic taste?

Use this pass only to review the meaning layer before artist or prompt work. It must not review a finished image, judge an artist, become art direction, become design review, teach visual design, create a generation workflow, or prepare prompt wording. If revision is needed, request correction of the semantic concept, not image execution details.

When `visual_concept.md`, `illustration_brief.md`, and `image_prompt.md` all exist, review may add a bounded meaning-preservation chain check:
- **Meaning continuity**: does the main meaning remain stable from `visual_concept.md` to `illustration_brief.md` to `image_prompt.md`?
- **Viewer takeaway continuity**: does the intended viewer understanding stay the same across all three artifacts?
- **Metaphor continuity**: does the selected visual metaphor remain intact, or was it replaced by another metaphor?
- **Distortion introduction**: did `illustration_brief.md` or `image_prompt.md` introduce meanings that were absent from `visual_concept.md`?
- **Constraint preservation**: are required elements, forbidden distortions, and misreading protections preserved downstream?
- **Prompt drift**: does `image_prompt.md` amplify secondary ideas, lose the main conclusion, or visually complete material beyond the approved concept?
- **Boundary protection**: does the review stay focused on meaning rather than image quality, style, composition, color, drawing technique, or artistic taste?

Use this check only to verify semantic continuity across the artifact chain. It must not become image quality review, art direction, Artist QA, artistic critique, composition review, color review, style review, drawing review, comic work, or presentation work. If a problem appears after `visual_concept.md`, fix `illustration_brief.md` or `image_prompt.md` at the point where the meaning drift was introduced; do not change `visual_concept.md` to accommodate later drift.

For `visual_article_sketchnote` outputs, especially `sketchnote_brief.md`, review may add a compact sketchnote meaning pass:
- **Article meaning integrity**: does the sketchnote brief preserve the article's main meaning?
- **Key point coverage**: are 4-7 key theses included, and are they actually present in the article?
- **Author conclusion integrity**: are the author's main conclusions visible without adding new conclusions?
- **Relationship clarity**: are the connections between key points understandable enough for a one-sheet note?
- **No invention**: did the brief invent theses, causal links, examples, warnings, or conclusions absent from the article?
- **One-sheet discipline**: is the sheet selective rather than overloaded, microscopic, or a "map of everything"?
- **Readable phrase control**: are the main handwritten phrases short, meaningful, and controlled rather than fake handwriting filler?
- **Genre protection**: has the result remained a handwritten article sketchnote instead of becoming an infographic, poster, comic, presentation slide, collage, or decorative picture?

When `sketchnote_brief.md` and `image_prompt.md` both exist, review may add a bounded prompt-drift check:
- **Brief-to-prompt continuity**: does `image_prompt.md` preserve article meaning, key points, author conclusions, and "do not show" constraints from `sketchnote_brief.md`?
- **Handwritten content continuity**: do required short phrases remain controlled and meaningful rather than replaced by fake text?
- **Format continuity**: does the prompt still describe one sheet of handwritten notes with liner drawings, arrows, frames, and connections?
- **Drift prevention**: did the prompt turn the sketchnote into a corporate infographic, poster, ordinary illustration, comic, photorealistic scene, collage, or AI-looking decoration?

Use this check only to verify semantic continuity and genre fit for the sketchnote. It must not become OCR requirements, artistic quality scoring, design-system work, drawing critique, composition review, or a new sketchnote methodology. If drift appears, fix the artifact where it was introduced, usually `image_prompt.md`, without changing the approved article meaning in `sketchnote_brief.md`.

## Structure review

Structure review checks information movement.

It asks:
- does the text start where the reader needs to start?
- does the opening deliver the answer, signal, impact, task, or frame required by the mode?
- does ordering follow reader progression rather than subject taxonomy?
- is context placed after the useful frame unless context is needed to prevent misunderstanding?
- does each section answer a reader task rather than merely cover a topic?
- are comparisons structured by criteria rather than parallel descriptions?
- do explanations move from the reader's current state toward use?
- does the ending land on action, decision, diagnosis, application, or a clear stopping point?

Structure revision is required when the useful content exists but appears in the wrong order.

## Usefulness review

Usefulness review checks whether the text creates practical value.

A text is useful when it helps the reader:
- act with less uncertainty;
- decide with clearer criteria;
- understand a situation enough to proceed;
- trust or challenge a claim with visible evidence;
- diagnose a condition or cause;
- apply a concept outside the text;
- know what does not need action.

Review should flag:
- **fake usefulness**: the text says the reader will "understand" but gives no decision, action, distinction, or application;
- **decorative completeness**: extra sections make the text look thorough without changing reader capability;
- **answer delay**: the useful answer appears after avoidable framing;
- **action ambiguity**: the reader learns information but not what to do with it;
- **reader overload**: the text includes more concepts, context, or branches than the outcome requires.

## Essay-mode detection

Essay-mode appears when the text follows the topic's intellectual shape instead of the reader's task.

Review should detect:
- **essay-mode relapse**: introduction -> broad context -> discussion -> conclusion when the mode requires answer, action, impact, or criteria first;
- **academic drift**: definitions, history, frameworks, or literature-style framing before usefulness;
- **completeness theater**: covering all aspects of a topic to appear responsible;
- **context inflation**: background grows beyond what changes action, interpretation, risk, or trust;
- **generic reflection**: paragraphs that sound thoughtful but do not change the reader's next step or understanding;
- **pseudo-depth**: abstraction, terminology, or nuance that does not improve decision, diagnosis, execution, trust, or application.

Common signals:
- the first useful sentence appears late;
- headings describe topics instead of reader jobs;
- the conclusion contains the recommendation that should have opened the text;
- paragraphs can be removed without changing reader outcome;
- the text explains why the topic matters before showing what the reader can do with it.

## Reader outcome verification

Review should test the text against the intended reader outcome.

After reading, can the reader:
- **understand** the relevant model, distinction, change, or situation well enough to proceed?
- **decide** using visible criteria, trade-offs, assumptions, and risks?
- **do** the task in the right order with checks and exception handling?
- **diagnose** likely causes using observable signals and differentiators?
- **choose** between options without inventing their own comparison logic?
- **apply** the idea to a new case using examples or transfer cues?
- **explain** the claim, rationale, or change to someone else without losing the logic?

If the answer is "only after guessing", the text needs revision.

## Revision triggers

Review must trigger meaningful editorial revision when:
- the reader task is unclear or contradicted by the text;
- the useful outcome is not delivered;
- the dominant mode is mismatched or overridden by a supporting mode;
- the opening delays the useful answer, impact, signal, or action;
- structure follows topic taxonomy instead of reader progression;
- context exceeds the brief's context limit;
- claims, evidence, interpretation, and recommendation are mixed where trust matters;
- instructions lack prerequisites, sequence, checks, or exceptions;
- decision support lacks criteria, trade-offs, or a visible recommendation;
- change communication hides impact, timing, affected groups, or required action;
- awareness creates attention but no posture, action, or no-action conclusion;
- diagnosis jumps to causes without signals or differentiators;
- sections exist only for coverage or polish.

Do not trigger revision for wording preferences unless the wording blocks the reader outcome.

## Severity levels

- **Critical usefulness failure**: the text does not help the reader reach the intended outcome. Requires structural or intent-level revision.
- **Structure degradation**: useful material exists but appears in an order that delays, obscures, or weakens reader progress. Requires reordering or reframing.
- **Mode mismatch**: the text uses the wrong editorial behavior for the reader task. Requires mode correction and structure adjustment.
- **Evidence or execution gap**: the text makes a claim, recommendation, diagnosis, or instruction without enough support or operational clarity. Requires targeted revision.
- **Clarity issue**: wording, terminology, or density makes a useful structure harder to use. Requires local editing.
- **Polish improvement**: wording could be smoother but usefulness is intact. Optional; should not block acceptance.

## False-positive prevention

Review should avoid creating problems that the reader does not have.

Before requesting changes, ask:
- does this issue block the reader task or intended outcome?
- is this a mode-specific problem or a personal preference?
- would the change improve usefulness, or only make the text sound more polished?
- would adding context reduce uncertainty or create overload?
- would rewriting disturb a structure that already works?
- am I asking for sophistication where directness is better?
- am I expanding the text because I distrust compactness?

If a text is useful, mode-fit, structurally clear, and adequately supported, review should accept it even if the reviewer would have written it differently.

## Anti-nitpicking rules

- Do not rewrite for taste.
- Do not demand extra context for completeness.
- Do not convert operational content into essay structure.
- Do not break mode behavior to make the text feel more balanced.
- Do not replace a working structure with a prettier structure.
- Do not optimize sentence elegance before reader outcome.
- Do not require terminology changes unless terms affect action, trust, or comprehension.
- Do not add nuance unless it changes decision, risk, diagnosis, execution, or application.
- Do not ask for expansion when deletion would improve usefulness.

## Failure modes

- **Style obsession**: review focuses on voice, smoothness, and polish while usefulness failures remain.
- **Endless revision loops**: review keeps finding lower-priority improvements after the reader outcome is already met.
- **Completeness addiction**: review demands more background, caveats, examples, or sections because the topic allows them.
- **Review drift**: review ignores the brief and judges the text against generic quality standards.
- **Mode blindness**: review uses the same criteria for instruction, decision support, trust building, and exploration.
- **Over-contextualization**: review pushes background upward until the useful answer is delayed.
- **Fake rigor**: review adds frameworks, distinctions, or terminology that make the text look smarter but less usable.
- **Preference laundering**: reviewer taste is presented as editorial necessity.
- **Supporting-mode takeover**: review over-improves a secondary goal until the dominant reader task weakens.
