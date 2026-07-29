# Validation Method Map

## purpose and boundary

This is a bounded fit map for Step 5 implementation and review. It helps select
the smallest method that can observe the critical uncertainty. It is not an
evidence taxonomy, universal questionnaire, research handbook, automatic
method selector, or permission to run research.

## primary map

| Hypothesis class | Decision question | Suitable bounded methods | Stronger observable signals | Common mismatch |
| --- | --- | --- | --- | --- |
| Problem | Does the material problem exist for the bounded audience and context? | interview; observation; existing-data analysis; work-case analysis; incident review; workaround study | recurring obstacle, consequence, workaround, error, or unmet job in inspected cases | prototype or full pilot before the problem is supported |
| Demand | Will a person voluntarily commit attention, time, effort, access, or another real resource? | participation invitation; registration; alternative choice; application; access request; pre-enrollment; observable commitment | completed voluntary commitment, choice, request, or resource tradeoff | stated interest or liking treated as demand |
| Mechanism | Can the key interaction produce the required intermediate action or decision? | scenario test; short exercise; controlled walkthrough; test fragment; simulation; key-interaction prototype; pre/post decision comparison | changed decision, completed target action, or observed failure in the causal chain | feedback survey used to prove mechanism |
| Behavior | Does real action change and persist or transfer to the work context? | task observation; repeat task; delayed check; actual-usage analysis; work-decision comparison; limited field pilot | changed real action, repeat use, transfer, or sustained error reduction | comprehension, completion, or intent treated as behavior |
| Usability | Can a person understand and complete the key scenario, and where do they fail? | prototype test; task-based usability test; observation; think-aloud; scenario walkthrough | task completion, error, abandonment, hesitation, or obstacle | demand survey or technical spike |
| Feasibility | Can the solution be implemented within material technical, data, process, people, authority, risk, and cost constraints? | technical spike; process walkthrough; limited integration; expert review; dependency audit; proof of concept | dependency resolved or fails, integration works or blocks, required resource/authority is available or absent | user preference used to prove implementability |
| Viability | Can the organization own, fund, support, and sustain the intervention without unacceptable process damage? | owner-and-operating-model check; operating-cost review; process-impact review; bounded viability review | named owner and support commitment, sustainable operating requirement, or observed process conflict | commercial language imposed on an internal product or a demo treated as operating viability |

## selection factors

Method choice also depends on:

- error consequence and the cost of the next step;
- reversibility and ability to stop;
- evidence already available;
- access to the real audience and context;
- ethical, privacy, safety, legal, and organizational constraints;
- whether the key result can be observed within the proposed time and setting.

If these factors make a bounded observation unsafe or non-diagnostic, use the
`insufficient` disposition and route the deeper evidence need to an existing
owner.

## minimality test

A proposed check is minimum only when all are true:

- it examines the critical assumption linked to the main gap;
- it is smaller and cheaper than full implementation;
- unrelated features and production-quality finishing are absent;
- it can be stopped and reversed;
- it yields evidence for one named next decision;
- it does not imply that the result validates the entire product.

## weak-signal rule

Positive reaction, stated intention, perceived clarity, approval, and declared
future use are weak signals. They may supplement evidence but cannot alone
confirm demand, mechanism, behavior change, transfer, persistence, or operating
effect.

## sequence boundary

Problem -> mechanism -> behavior -> usability -> feasibility -> limited rollout
may be a plausible long-term evidence sequence for some products. Product
Intent Review recommends only the next necessary check and must not instantiate
the whole sequence without explicit authority.
