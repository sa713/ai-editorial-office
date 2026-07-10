# Facts

## Confirmed external-practice findings

| ID | Finding | Evidence | Confidence | Release use |
| --- | --- | --- | --- | --- |
| F01 | Strong intake starts with stakeholder/user, intended use or end state, expectations, constraints, and context before solution work. | S01, S02, S04, S05 | verified | recognize outcome/context signals before task-type recommendation |
| F02 | Received requirements are not sufficient by themselves; iteration and clarification reduce the risk of implementing a different interpretation. | S02 | verified | ambiguity and missing-information signals remain visible |
| F03 | Architecture significance is driven by mission/business concerns, stakeholders, quality attributes, constraints, and scenarios before an architecture exists. | S03 | verified | recommend Architecture Review and Software Architecture context from drivers, not the word “architecture” |
| F04 | Problem framing should challenge solution-shaped requests, name what is outside scope, and understand the wider journey before building. | S04, S05 | verified | detect mixed/decomposition needs and avoid solution-first misclassification |
| F05 | Research depth should be shaped by what is already known, problem novelty, constraints, risk, and expected value; not every task warrants full discovery. | S04, S05 | supported | recommend proportionate research depth without deciding it |
| F06 | Engineering issue intake benefits from structured separation of type, actual/expected behavior, reproduction, environment, and additional context. | S06 | verified | recognize engineering significance from observable change/failure surfaces |
| F07 | Work-item systems keep type, priority, effort, and impact as separable metadata. | S07 | verified | avoid collapsing task type, risk, and depth into one label or score |
| F08 | GitHub's AI issue intake is described as producing triage suggestions such as actionable or needs-information, followed by human review and action. | S08 | verified | direct precedent for advisory recommendations with human decision authority |
| F09 | Incident practice ties prioritization and response depth to impact, affected functionality/users, and context; definitions are product-specific. | S09, S10, S11 | supported | high-risk and review-depth signals depend on consequence and exposure, not generic keywords |
| F10 | Applying every reliability or review method everywhere creates unjustified cost; different traffic/task classes need different depth. | S10 | supported | simple-task protection is a first-class validation requirement |
| F11 | Fixed intent classifiers can perform well in scope yet struggle with out-of-scope inputs, creating a wrong-action risk. | S12 | verified for study | recognition must allow `uncertain`, `mixed`, or unsupported rather than force one type |
| F12 | Learned LLM routers are designed to select models automatically to optimize cost/performance. | S13 | verified for study | contrast case: S5.R4 must not copy router authority or thresholds |
| F13 | Human-AI guidance recommends making capability and likely error limits clear and supporting verification/control because automated inferences are uncertain. | S14 | verified | recognition exposes confidence, limits, and alternatives rather than certainty theatre |
| F14 | NIST AI RMF separates contextual mapping and technical categorization from accountable governance and calls for differentiated human-AI roles and documented oversight. | S15 | verified | recognition/decision separation and Chief Editor authority |
| F15 | NIST warns that representing complex human phenomena as measurable quantities can remove necessary context. | S15 | verified | no score, weighted confidence, or deterministic taxonomy |

## Confirmed repository findings

| ID | Finding | Evidence | Confidence | Release consequence |
| --- | --- | --- | --- | --- |
| F16 | Chief Editor already owns task type, workflow, risk, depth, capabilities, roles, Domain Packs, evidence, planning, and preflight decisions. | R01, R02, R06 | verified | Task Need Recognition cannot own or perform those decisions |
| F17 | Intake Agent already owns raw-request normalization, early task type, risk, research, planning, communication, ambiguity, and missing-constraint signals. | R02, R06 | verified | Intake is the primary signal producer; no new role is needed |
| F18 | Preflight answers whether the system understands the task enough to ask, constrain, proceed, or block. | R01, R02 | verified | recognition informs but does not duplicate the Preflight Gate |
| F19 | Professional Analysis owns analytical product shape after the need for analysis is material; it does not own global task routing. | R03 | verified | recognition may recommend it but cannot reproduce its lenses or recommendations |
| F20 | Evaluation Signals are optional views over saved evidence for later human decisions and do not own live task routing. | R05 | verified | reuse evidence/interpretation/decision separation, not the Evaluation Signal mechanism itself |
| F21 | Domain Pack activation requires material effect on evidence, terminology, risk, review focus, or output; keywords alone are insufficient. | R04 | verified | pack recommendations require domain-specific surfaces and a non-activation check |
| F22 | Architecture Review and Engineering Review already define architectural and implementation/change-safety significance. | R03 | verified | recognition signals must point to those owners and avoid redefining their methods |
| F23 | Existing task-object fields already cover task type, risk, depth, evidence, uncertainty, capabilities, packs, roles, options, and next action. | R02 | verified | no new required task-object fields or artifact family is needed |
| F24 | The current architecture permits reusable capabilities without new roles, pipelines, stages, gates, or mandatory artifacts. | R01, R02 | verified | one bounded shared capability is architecture-compatible if it has a clear owner and advisory boundary |

## Interpretations for synthesis

- A recognition view should separate: observed request evidence, advisory need
  recommendations, uncertainty/negative evidence, and Chief Editor decisions.
- Recognition should be multi-label because one request may legitimately have
  analysis, engineering, architecture, communication, and multiple-domain
  aspects.
- Task type should describe the dominant work and deliverable, not every noun
  present in the request.
- Decomposition is a recommendation when deliverables, owners, evidence bases,
  risk modes, or validation paths diverge materially.
- Research/review recommendations should use qualitative depth language and a
  rationale; existing owners make the actual depth decision.
- A new standalone artifact, score, classifier, or router is not justified.

## Contradictions and limits

- External issue and AI routing sources often automate labels or model choice;
  the mission explicitly forbids importing that authority. Only structured
  signal capture and recommendation patterns transfer.
- Incident and platform systems use local severity/priority scales. Repository
  risk mode and process depth remain canonical; no external scale transfers.
- Intent-classification studies use fixed taxonomies and short utterances.
  Editorial tasks are richer and may be multi-label, so the study supports
  out-of-scope humility, not a repository taxonomy.
- Professional Analysis remains a Release Candidate rather than an accepted
  release in project state, but its canonical owner exists and the mission
  explicitly requires boundary synthesis against it.

## Sufficiency judgment

Evidence is sufficient to synthesize a bounded advisory capability. It is not
sufficient to justify an automatic classifier, numeric scoring model,
universal taxonomy, or new routing authority.
