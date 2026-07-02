# Operational editorial rules

These rules are not stylistic preferences. They are editorial decision heuristics for AI-driven content systems.

## Rule

### Principle
If the reader needs an answer, recommendation, or decision support, start with the answer or decision frame before giving background.

### Why it exists
Prevents essay-mode openings that delay the useful part with history, importance framing, or broad context.

### Reader impact
The reader quickly understands what to do, believe, compare, or decide.

### Writing implication
Lead with the conclusion, recommendation, or decision criteria; move background below it only if it changes the reader's action.

### Anti-pattern
Starting with why the topic is important, how it evolved, or what people generally think before stating the useful answer.

## Rule

### Principle
Every section must answer a reader task, not merely cover a topic.

### Why it exists
Prevents table-of-contents writing where sections exist because the subject has subtopics, not because the reader needs them.

### Reader impact
The reader can use each section to make progress toward a concrete outcome.

### Writing implication
Name or structure sections around questions, decisions, actions, checks, or trade-offs instead of abstract categories.

### Anti-pattern
Sections such as "Overview", "History", "Key aspects", and "Additional considerations" that do not reveal what the reader can do with them.

## Rule

### Principle
Do not include context unless it changes interpretation, priority, risk, or next action.

### Why it exists
Prevents completeness bias and background accumulation.

### Reader impact
The reader receives enough context to act without carrying irrelevant mental load.

### Writing implication
Before adding context, test whether removing it would make the answer less usable or more likely to be misunderstood.

### Anti-pattern
Adding industry history, definitions, stakeholder background, or process detail because it is true rather than because it is operationally needed.

## Rule

### Principle
When a request implies comparison or choice, structure the text around decision criteria before describing options.

### Why it exists
Prevents option catalogues that leave the reader to infer how to choose.

### Reader impact
The reader can compare alternatives using explicit, relevant dimensions.

### Writing implication
State the selection criteria, then evaluate each option against those criteria; avoid separate promotional descriptions of each option.

### Anti-pattern
Listing several options with features and benefits but no decision logic.

## Rule

### Principle
If the reader's next action is known, make the text end with that action or a clear stopping point.

### Why it exists
Prevents informational drift where the text explains but does not land.

### Reader impact
The reader knows what to do next, what to check, or why no action is needed.

### Writing implication
Close with a decision, checklist, next step, handoff, or explicit "no action" conclusion when appropriate.

### Anti-pattern
Ending with a generic summary, broad reflection, or "it depends" without usable direction.

## Rule

### Principle
Use the reader's current state of knowledge as the entry point, not the author's preferred conceptual order.

### Why it exists
Prevents expert-first explanations that require the reader to absorb theory before solving their problem.

### Reader impact
The reader starts from a recognizable problem, signal, symptom, or goal.

### Writing implication
Order information from the reader's situation toward the underlying model, not from taxonomy toward application.

### Anti-pattern
Beginning with definitions, frameworks, or classifications when the reader came with a practical question.

## Rule

### Principle
For practical content, prefer "condition -> action -> result" movement over narrative or thematic movement.

### Why it exists
Prevents prose that feels coherent but does not support execution.

### Reader impact
The reader can map situations to actions and anticipate the consequence.

### Writing implication
Frame guidance as when to use it, what to do, and what changes after doing it.

### Anti-pattern
Explaining ideas in a smooth essay sequence without showing when they apply or what they produce.

## Rule

### Principle
Separate facts, interpretation, and recommendation when the reader must trust a judgment.

### Why it exists
Prevents unsupported authority and makes editorial reasoning inspectable.

### Reader impact
The reader can see what is known, what is inferred, and what is being advised.

### Writing implication
Present evidence or observable signals first, then the meaning of those signals, then the recommended action.

### Anti-pattern
Making a confident recommendation without showing the factual basis or the reasoning bridge.

## Rule

### Principle
For diagnostic analysis, mark confidence only where uncertainty affects the analysis.

### Why it exists
Prevents hidden inference, artificial certainty, and quiet completion of raw ideas.

### Reader impact
The reader can distinguish what is directly supported by materials, implied by materials, an editorial interpretation, a bounded hypothesis, or something that requires confirmation.

### Writing implication
Use lightweight labels only when they clarify the analysis:
- directly supported by materials;
- implied by materials;
- editorial interpretation;
- bounded hypothesis;
- requires confirmation.

The goal is semantic honesty, distinction clarity, and uncertainty visibility, not formal rigor.

### Review implication
Review may check whether interpretation is being presented as fact, or whether a hypothesis is hidden as an obvious conclusion. This should stay editorial and should not become formal audit behavior.

### Anti-pattern
Scoring confidence, mandatory tagging, evidence matrices, full traceability systems, confidence protocols, or labeling every phrase.

## Rule

### Principle
Separate editorial diagnosis, author concept diagnosis, and solution design before choosing the output shape.

### Why it exists
Prevents the editorial system from mixing material analysis, the author's idea state, and solution architecture in one response.

### Reader impact
The reader receives the type of help they asked for and can see when a different type of work would be a separate next step.

### Writing implication
Use the working question to keep the response inside the right boundary:

- Editorial diagnosis asks: "What is happening with the material as an object of editorial work?" Focus on clarity, completeness, structure, gaps, and readiness for further editorial work.
- Author concept diagnosis asks: "What is happening with the author's idea?" Focus on the central thought, problem, intention, mechanism, audience, expected change, success criterion, and what is mixed or not distinguished.
- Solution design asks: "How should the solution be arranged?" Focus on model, process, roles, scenarios, roadmap, metrics, governance, and implementation.

Move from one type of work to another only when the task explicitly asks for it or records it. If the task is diagnosis, do not turn it into solution design. If design is needed, name it as a separate next step first.

### Repair implication
If the response mixes types, return it to the requested type of work; name what is analysis, interpretation, and proposed development; remove ready-made solutions that were not requested.

### Anti-pattern
Diagnosing a weak material by inventing a program, treating an author's unresolved idea as a design brief, or hiding solution design inside diagnostic recommendations.

## Rule

### Principle
If a term or distinction does not affect reader action, remove it or demote it.

### Why it exists
Prevents vocabulary-driven structure and unnecessary conceptual load.

### Reader impact
The reader does not have to learn labels that do not change their task.

### Writing implication
Introduce terminology only when it helps the reader choose, diagnose, execute, or avoid a mistake.

### Anti-pattern
Defining concepts because they are standard in the domain, even though the rest of the text does not rely on them.

## Rule

### Principle
Make hidden assumptions explicit when they change the validity of the advice.

### Why it exists
Prevents overgeneralized guidance that silently depends on audience, channel, risk, timing, or constraints.

### Reader impact
The reader can judge whether the answer applies to their situation.

### Writing implication
State scope conditions near the recommendation, especially for trade-offs, exceptions, and high-risk contexts.

### Anti-pattern
Presenting advice as universal when it only works for a specific audience, format, maturity level, or operational constraint.

## Rule

### Principle
When writing for scanning, expose the information hierarchy in headings and first sentences.

### Why it exists
Prevents dense linear text that hides the answer inside paragraphs.

### Reader impact
The reader can locate the relevant part quickly and decide whether to read deeper.

### Writing implication
Use headings, paragraph leads, and lists to show priority, sequence, and decision points.

### Anti-pattern
Using clever or vague headings and paragraphs whose main point appears only at the end.

## Rule

### Principle
Remove any paragraph that does not advance the reader from question to answer, decision, or action.

### Why it exists
Prevents polished filler and thematic padding.

### Reader impact
The reader spends attention only on information that moves the task forward.

### Writing implication
During review, assign each paragraph a job; cut or merge paragraphs with no distinct operational function.

### Anti-pattern
Paragraphs that restate the premise, decorate the argument, or provide general commentary without changing the reader's understanding or action.

## Rule

### Principle
For Russian editorial clarity, replace bureaucratic noun chains with actors, actions, and concrete objects when the text gives instructions or explanations.

### Why it exists
Prevents канцелярит and abstract procedural fog.

### Reader impact
The reader sees who does what, with what, and why it matters.

### Writing implication
Prefer verbs, agents, and observable actions over nominalized processes when describing work, responsibility, or consequences.

### Anti-pattern
Phrases built around "осуществление", "проведение", "реализация", "в рамках", or "по вопросам" where the actor and action disappear.
