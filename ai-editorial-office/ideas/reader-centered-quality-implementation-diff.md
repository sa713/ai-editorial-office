# Reader-Centered Quality Implementation Diff

Дата: 2026-07-13

Baseline: локальный снимок канонического `ai-editorial-office` до implementation (`09dc2e0`).

Diff разделён по backlog-задачам в порядке выполнения. Последний раздел содержит только closeout-изменения backlog и implementation report. Этот файл не включает собственный self-diff, потому что такой diff был бы рекурсивным.

## ROQ-P0-01 reader outcome contract

Commit slice: `41e87f7`

Изменённые файлы:

- `AGENTS.md`
- `kb/audience_outcome_alignment.md`
- `kb/editorial_quality_attributes.md`
- `kb/task_object_model.md`

~~~~diff
diff --git a/AGENTS.md b/AGENTS.md
index 81ed570..39a2fb2 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -55,2 +55,2 @@
-| Audience and outcome alignment | `/kb/audience_outcome_alignment.md` | task-specific audience, intended outcome, reader context, detail/tone/format fit, and usefulness criteria |
-| Editorial quality attributes and tradeoffs | `/kb/editorial_quality_attributes.md` | task-specific quality priorities, accepted tradeoffs, and preservation risks |
+| Audience, outcome, and Reader Outcome Contract | `/kb/audience_outcome_alignment.md` | task-specific audience, intended outcome, reader context, reader starting state, required change, practical result, detail/tone/format fit, and usefulness criteria |
+| Editorial quality attributes, priority, guardrails, and tradeoffs | `/kb/editorial_quality_attributes.md` | task-specific quality priorities, non-relaxable guardrails, accepted tradeoffs, and preservation risks |
@@ -220,0 +221,3 @@ Before production starts, Chief Editor must route the task editorially:
+- define a compact Reader Outcome Contract for material reader-facing work:
+  starting state, required change in understanding or practice, practical
+  result, and failure signal;
@@ -250 +253,2 @@ decision, action, understanding, or publication outcome the artifact must
-enable.
+enable. It also owns the compact Reader Outcome Contract used when the task
+must change what a reader understands, remembers, decides, or does.
@@ -1209,0 +1214,3 @@ Needs verification: yes/no
+- ценным для конкретного читателя и заявленного outcome;
+- способным дать требуемое изменение понимания, решения или практики, когда
+  такое изменение является целью задачи;
@@ -1216,0 +1224,2 @@ Needs verification: yes/no
+Reader value не разрешает ослаблять correctness, evidence support,
+neutrality, traceability, честную неопределённость или независимый review.
diff --git a/kb/audience_outcome_alignment.md b/kb/audience_outcome_alignment.md
index 0527fea..c0ae464 100644
--- a/kb/audience_outcome_alignment.md
+++ b/kb/audience_outcome_alignment.md
@@ -4,3 +4,3 @@ This file is the canonical owner for audience identification, intended
-outcome, reader context, required action or decision, required depth, tone and
-language fit, artifact success criteria, mismatch warning signs, and correction
-patterns in AI Editorial Office.
+outcome, reader context, Reader Outcome Contract, required action or decision,
+required depth, tone and language fit, artifact success criteria, mismatch
+warning signs, and correction patterns in AI Editorial Office.
@@ -31,0 +32,36 @@ a generic reader.
+## Reader Outcome Contract
+
+For material reader-facing work, audience identification is not enough. Record
+the smallest contract that makes the intended reader change reviewable:
+
+```markdown
+## reader outcome contract
+- reader starting state:
+- required change in understanding, decision, or practice:
+- practical result after use:
+- failure signal:
+- evidence and precision guardrails:
+```
+
+The contract answers four different questions:
+
+1. What does this reader already know, believe, use, or misunderstand?
+2. What must be different after the artifact is used?
+3. What observable decision, action, explanation, or working habit should the
+   artifact enable?
+4. What result would be correct in content but still useless for this reader?
+
+Use the contract for teaching, explanation, change communication, decision
+support, implementation guidance, or other work where a generic audience label
+does not make success reviewable. Keep it compact for short or low-risk work.
+Use `not applicable` with a reason when the task has no material reader change.
+
+Reader value is bounded by evidence. The contract may change structure,
+examples, detail, product bridge, chronology, or action path, but it may not
+weaken correctness, source boundaries, neutrality, traceability, uncertainty,
+review independence, or required caveats.
+
+The Reader Outcome Contract normally lives in `brief.md`,
+`orchestration_plan.md`, production notes, or `review.md`. It is not a new role,
+pipeline, review gate, score, persona document, or mandatory standalone file.
+
@@ -35,0 +72,2 @@ audience fit affects the result. Record it only as deeply as the task requires.
+When reader change is material, use it together with the Reader Outcome
+Contract.
@@ -244,0 +283 @@ This framework does not:
+- require a Reader Outcome Contract when no material reader change is expected;
diff --git a/kb/editorial_quality_attributes.md b/kb/editorial_quality_attributes.md
index 7fcb138..1dd0801 100644
--- a/kb/editorial_quality_attributes.md
+++ b/kb/editorial_quality_attributes.md
@@ -46,0 +47 @@ is required for every task.
+| Reader outcome | The artifact produces the required change in understanding, decision, memory, or practice for the intended reader. | Reader Outcome Contract, visible cognitive or action transition, retained key ideas, practical result, reader-review evidence. |
@@ -55,0 +57,21 @@ system update promotes them.
+## Quality Priority And Non-Relaxable Guardrails
+
+For material reader-facing work, quality is not complete when the artifact is
+only correct, complete, and well structured. The selected profile must consider
+reader value, the required change in the reader's model or decision, and
+practical applicability alongside correctness and evidence.
+
+This is not a license to trade truth for usefulness. The following guardrails
+are non-relaxable whenever they are material:
+
+- correctness against sources, repository state, product behavior, and canon;
+- evidence support and honest confidence;
+- neutrality when the task requires objective treatment;
+- traceability required by review or governance;
+- visible uncertainty, caveats, source boundaries, and residual risk;
+- independent review and the existing review gate.
+
+A task may prioritize reader outcome above completeness, durability, breadth,
+formality, or exhaustive chronology. It may not call an unsupported,
+misleading, biased, or unreviewable result useful.
+
@@ -62,0 +85,2 @@ Use this compact pattern when quality priorities are material:
+- reader outcome priority:
+- non-relaxable guardrails:
@@ -87,0 +112 @@ Quality tradeoffs should be handled deliberately, not hidden.
+| Reader value vs evidence discipline | Change route, examples, layering, or detail; never remove evidence boundaries, caveats, neutrality, or required traceability to make the result easier or more persuasive. |
@@ -104 +129 @@ rigid matrix.
-| Editorial article | Audience fit, clarity, structural coherence, evidence support, tone, relevance. | Exhaustive traceability in reader-facing copy when review artifacts preserve it. |
+| Editorial article | Reader outcome, audience fit, clarity, structural coherence, evidence support, tone, relevance. | Exhaustive traceability in reader-facing copy when review artifacts preserve it. |
@@ -120,0 +146,2 @@ Evaluate quality by asking:
+7. Would the intended reader change understanding, decision, or practice in the
+   way the Reader Outcome Contract requires?
@@ -221,0 +249,2 @@ This framework does not:
+- treat reader value as permission to weaken correctness, evidence, neutrality,
+  traceability, uncertainty, or review independence;
diff --git a/kb/task_object_model.md b/kb/task_object_model.md
index 721f645..7d0e4b4 100644
--- a/kb/task_object_model.md
+++ b/kb/task_object_model.md
@@ -79,0 +80 @@ file.
+| `reader_outcome_contract` | Compact statement of reader starting state, required change in understanding/decision/practice, practical result, failure signal, and evidence guardrails when reader change is material. | `brief.md`, `orchestration_plan.md`, production notes, `review.md` |
@@ -148 +149 @@ requires it.
-| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit when material, quality priorities/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame when required, evidence basis/confidence for material route decisions, and expansion triggers. |
+| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame when required, evidence basis/confidence for material route decisions, and expansion triggers. |
~~~~

## ROQ-P0-02 chief editor reader journey

Commit slice: `dcb7688`

Изменённые файлы:

- `agents/chief_editor.md`
- `kb/capability_registry.md`
- `kb/editorial_planning_framework.md`
- `templates/artifacts/orchestration_plan_template.md`

~~~~diff
diff --git a/agents/chief_editor.md b/agents/chief_editor.md
index 8d1c705..a5608c9 100644
--- a/agents/chief_editor.md
+++ b/agents/chief_editor.md
@@ -46,0 +47,2 @@ signals and advisory recommendations are owned by
+- design the reader journey for material reader-facing work: starting state,
+  required change, explanation sequence, and practical result after use;
@@ -151,0 +154,3 @@ Conditional:
+- reader starting state, required change in understanding or practice,
+  explanation sequence, practical result, and reader-outcome failure signal
+  when the artifact must teach, explain, reorient, or change action;
@@ -278,0 +284,2 @@ Required when applicable:
+- compact reader journey inside `orchestration_plan.md` when reader change is
+  material; it must be a production contract, not a second audience framework.
@@ -395,0 +403,2 @@ The Chief Editor may decide:
+- reader starting state, target understanding or practice, explanation order,
+  and practical result needed to make a reader-facing route useful;
@@ -417 +426,2 @@ The Chief Editor may decide:
-  rejected alternatives kept to short route/reason pairs;
+  rejected alternatives kept to short route/reason pairs and the selected
+  route justified by the reader journey rather than subject order alone;
@@ -496,0 +507,3 @@ Do not repeat the full Editorial Decision Frame. It should not use
+- material reader-facing work has a compact journey from reader starting state
+  to required understanding, decision, or action, and the selected structure
+  can be explained through that journey;
diff --git a/kb/capability_registry.md b/kb/capability_registry.md
index dd509dd..2da3ad8 100644
--- a/kb/capability_registry.md
+++ b/kb/capability_registry.md
@@ -532,3 +532,4 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-- Typical outputs: audience/outcome note in an existing artifact, detail level,
-  format/tone constraints, required action or decision, usefulness criteria,
-  mismatch warning, or correction action.
+- Typical outputs: audience/outcome note in an existing artifact, Reader
+  Outcome Contract and reader journey when material, detail level, format/tone
+  constraints, required action or decision, usefulness criteria, mismatch
+  warning, or correction action.
@@ -546,3 +547,4 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-- Quality criteria: audience is explicit enough, outcome is actionable,
-  evidence and detail match reader need, tone does not hide uncertainty, and
-  irrelevant process or theory is omitted.
+- Quality criteria: audience is explicit enough, outcome is actionable, reader
+  starting state and required change are visible when material, evidence and
+  detail match reader need, tone does not hide uncertainty, and irrelevant
+  process or theory is omitted.
@@ -608,2 +610,4 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-  pipeline, Editorial Decision Frame.
-- Typical outputs: outline, structure notes, writing contract, review focus.
+  pipeline, Reader Outcome Contract and reader journey when material,
+  Editorial Decision Frame.
+- Typical outputs: outline, reader-journey rationale, structure notes, writing
+  contract, review focus.
@@ -617,2 +621,2 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-- Quality criteria: structure follows reader task and evidence, not generic
-  format habit.
+- Quality criteria: structure follows reader starting state, required change,
+  task, and evidence, not generic format habit or subject taxonomy alone.
@@ -904 +908 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-| Chief Editor | Task Need Recognition challenge and decision separation; routing and preflight; analytical reasoning depth for complex or decision-heavy work; Professional Analysis selection for structured interpretation, synthesis, recommendation, and decision-support work; Professional Communication selection for message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, and caveat-preserving reader transfer when material; Architecture Review selection for architecture-sensitive work; Engineering Review selection for implementation-sensitive work; quality attribute selection for route/depth decisions; audience/outcome alignment for route/depth decisions; planning and option evaluation for route/commitment decisions; source boundary decision when routing; evidence-confidence decision for material routes and governance; failure-mode reroute/escalation; editorial structure contract; client-profile activation; governance closure; memory curation; Knowledge Evolution disposition; learning extraction and canon-evolution routing; mini-contract authorization. |
+| Chief Editor | Task Need Recognition challenge and decision separation; routing and preflight; reader-journey design for material reader-facing work; analytical reasoning depth for complex or decision-heavy work; Professional Analysis selection for structured interpretation, synthesis, recommendation, and decision-support work; Professional Communication selection for message architecture, recommendation presentation, explanation fit, technical communication, information density, actionability, and caveat-preserving reader transfer when material; Architecture Review selection for architecture-sensitive work; Engineering Review selection for implementation-sensitive work; quality attribute selection for route/depth decisions; audience/outcome alignment for route/depth decisions; planning and option evaluation for route/commitment decisions; source boundary decision when routing; evidence-confidence decision for material routes and governance; failure-mode reroute/escalation; editorial structure contract; client-profile activation; governance closure; memory curation; Knowledge Evolution disposition; learning extraction and canon-evolution routing; mini-contract authorization. |
diff --git a/kb/editorial_planning_framework.md b/kb/editorial_planning_framework.md
index bb84da5..611e8f3 100644
--- a/kb/editorial_planning_framework.md
+++ b/kb/editorial_planning_framework.md
@@ -83,0 +84 @@ Select only the dimensions that matter for the current task.
+| Reader journey fit | Does this option connect the reader's starting state to the required change in a learnable and usable sequence? |
@@ -88,0 +90,21 @@ short bullets, or a paragraph is enough when it makes the tradeoff visible.
+## Reader Journey Fit
+
+For material reader-facing work, evaluate routes as learning or action paths,
+not only as subject structures. A route should answer:
+
+1. What does the reader know, believe, use, or misunderstand now?
+2. What must change before the reader can understand, decide, or act?
+3. Which sequence makes that change easiest without hiding evidence or
+   complexity?
+4. What can the reader do, explain, or decide after the artifact?
+
+`Concept-first`, `chronology-first`, `product-first`, `problem-first`, and
+`action-first` are possible routes, not defaults. Choose the one that best
+serves the recorded reader journey and source boundary. If the request names a
+stopping point such as "I last understood X", treat it as evidence for a bridge
+from X rather than as incidental background.
+
+Keep this judgment inside the existing option evaluation and Editorial
+Decision Frame. Do not create a reader-journey framework, role, score, or
+standalone artifact.
+
@@ -133,0 +156,2 @@ Planning is complete when:
+- reader-facing route order is justified by the reader journey when reader
+  change is material;
diff --git a/templates/artifacts/orchestration_plan_template.md b/templates/artifacts/orchestration_plan_template.md
index d64ba67..f019bd7 100644
--- a/templates/artifacts/orchestration_plan_template.md
+++ b/templates/artifacts/orchestration_plan_template.md
@@ -112,0 +113,2 @@ artifact and keep this frame compact.
+- Reader journey rationale, when material: starting state -> required change ->
+  explanation sequence -> practical result
~~~~

## ROQ-P0-03 extend editorial decision frame

Commit slice: `0475ff4`

Изменённые файлы:

- `AGENTS.md`
- `agents/chief_editor.md`
- `agents/writer_agent.md`
- `kb/task_object_model.md`
- `templates/artifacts/orchestration_plan_template.md`
- `templates/tasks/article_task_template.md`

~~~~diff
diff --git a/AGENTS.md b/AGENTS.md
index 39a2fb2..d8a4646 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -242,2 +242,5 @@ alternatives, rejection reasons, Writer/UX Writer contract, review focus, and
-reroute triggers. It lives inside `orchestration_plan.md`; it is not a new
-pipeline, role, status, `final_decision.md`, or mandatory standalone
+reroute triggers. For teaching, understanding, or other material reader-change
+work, it also records a compact `Cognitive Bridge`, 3-5 `Moments of Insight`,
+and `Practical Transformation`. These fields may be `not applicable` with a
+reason for other tasks. The frame lives inside `orchestration_plan.md`; it is
+not a new pipeline, role, status, `final_decision.md`, or mandatory standalone
@@ -848 +851,3 @@ final governance still happens and must be artifact-backed.
-   inside the frame.
+   inside the frame. When reader change is material, the frame also includes
+   the Cognitive Bridge, 3-5 formulated Moments of Insight, and Practical
+   Transformation; these are production fields, not new artifacts.
diff --git a/agents/chief_editor.md b/agents/chief_editor.md
index a5608c9..512700c 100644
--- a/agents/chief_editor.md
+++ b/agents/chief_editor.md
@@ -80,0 +81,3 @@ signals and advisory recommendations are owned by
+- require the Editorial Decision Frame to include a Cognitive Bridge, 3-5
+  formulated Moments of Insight, and Practical Transformation when teaching,
+  understanding, or another material reader change is the intended outcome;
@@ -158,0 +162,2 @@ Conditional:
+- old or incomplete reader model, required transition, 3-5 retained ideas, and
+  observable post-use action when reader change is material;
@@ -289,0 +295,3 @@ Required when applicable:
+- Cognitive Bridge, 3-5 Moments of Insight, and Practical Transformation inside
+  that frame when teaching, understanding, or another reader change is
+  material; otherwise a compact `not applicable` rationale is allowed.
@@ -509,0 +518,3 @@ Do not repeat the full Editorial Decision Frame. It should not use
+- Cognitive Bridge names the old/incomplete model and transition, Moments of
+  Insight are formulated ideas rather than headings, and Practical
+  Transformation is observable when those fields are material;
diff --git a/agents/writer_agent.md b/agents/writer_agent.md
index 81872fc..d038520 100644
--- a/agents/writer_agent.md
+++ b/agents/writer_agent.md
@@ -35,0 +36,3 @@ owned by `/kb/domain_knowledge_pack_standard.md`.
+- realize the approved Cognitive Bridge, Moments of Insight, and Practical
+  Transformation when those fields are material, without inventing a reader
+  model or changing the approved route;
@@ -94,0 +98,2 @@ Conditional:
+- Cognitive Bridge, Moments of Insight, and Practical Transformation from the
+  Editorial Decision Frame when reader change is material;
@@ -140,0 +146,2 @@ Conditional:
+- turn Moments of Insight into generic section labels, omit a material
+  Cognitive Bridge, or replace Practical Transformation with a vague promise;
@@ -211,0 +219,2 @@ should not repeat full research or status history.
+- material Cognitive Bridge is visible in the reading path, the 3-5 Moments of
+  Insight are actually expressed, and Practical Transformation is actionable;
diff --git a/kb/task_object_model.md b/kb/task_object_model.md
index 7d0e4b4..65cd0c0 100644
--- a/kb/task_object_model.md
+++ b/kb/task_object_model.md
@@ -80,0 +81,3 @@ file.
+| `cognitive_bridge` | What the reader already knows, which old or incomplete model must change, and the transition needed. Required for teaching/understanding work when material; otherwise conditional. | Editorial Decision Frame in `orchestration_plan.md`, production notes, `review.md` |
+| `moments_of_insight` | Three to five formulated ideas the reader should retain; these are claims or mental-model shifts, not section titles. | Editorial Decision Frame, outline/draft, `review.md` |
+| `practical_transformation` | Observable action, decision, explanation, or working habit the reader should perform differently after using the artifact. | Editorial Decision Frame, production artifact, `review.md` |
@@ -149 +152 @@ requires it.
-| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame when required, evidence basis/confidence for material route decisions, and expansion triggers. |
+| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame with Cognitive Bridge, Moments of Insight, and Practical Transformation when material, evidence basis/confidence for material route decisions, and expansion triggers. |
diff --git a/templates/artifacts/orchestration_plan_template.md b/templates/artifacts/orchestration_plan_template.md
index f019bd7..6641e0d 100644
--- a/templates/artifacts/orchestration_plan_template.md
+++ b/templates/artifacts/orchestration_plan_template.md
@@ -114,0 +115,7 @@ artifact and keep this frame compact.
+- Cognitive Bridge, required for teaching/understanding work or `not applicable`
+  with reason:
+  - What the reader already knows:
+  - Old or incomplete model to update:
+  - Required transition:
+- Moments of Insight, 3-5 formulated ideas rather than section titles:
+- Practical Transformation, observable action/decision/habit after use:
diff --git a/templates/tasks/article_task_template.md b/templates/tasks/article_task_template.md
index ffc5562..2356502 100644
--- a/templates/tasks/article_task_template.md
+++ b/templates/tasks/article_task_template.md
@@ -89,0 +90,13 @@ governance, or non-trivial coordination must be recorded.
+## reader outcome contract, when material
+
+- reader starting state:
+- required change:
+- practical result:
+- failure signal:
+
+## Cognitive Bridge / Moments of Insight / Practical Transformation
+
+- Cognitive Bridge:
+- Moments of Insight, 3-5 formulated ideas:
+- Practical Transformation:
+
~~~~

## ROQ-P0-04 reader model and learning design

Commit slice: `4434a40`

Изменённые файлы:

- `agents/chief_editor.md`
- `agents/intake_agent.md`
- `agents/writer_agent.md`
- `kb/audience_outcome_alignment.md`
- `kb/capability_registry.md`
- `kb/professional_communication.md`
- `pipelines/article_pipeline.md`

~~~~diff
diff --git a/agents/chief_editor.md b/agents/chief_editor.md
index 512700c..839002d 100644
--- a/agents/chief_editor.md
+++ b/agents/chief_editor.md
@@ -62,0 +63,2 @@ signals and advisory recommendations are owned by
+- select the Learning Design lens within Professional Communication when the
+  task must teach, update a mental model, or explain a changed practice;
@@ -424,0 +427,3 @@ The Chief Editor may decide:
+- whether a material teaching/explanation task needs the conditional
+  `раньше -> сейчас -> почему -> пример -> что делать` pattern or a different
+  reader-journey sequence;
diff --git a/agents/intake_agent.md b/agents/intake_agent.md
index a58f7f4..1218e4d 100644
--- a/agents/intake_agent.md
+++ b/agents/intake_agent.md
@@ -33,0 +34,3 @@ Professional Communication guidance is owned by
+- capture or conservatively infer the reader starting state, old/incomplete
+  model, and desired practical change when teaching, understanding, or complex
+  explanation is material; mark uncertainty instead of inventing a persona;
@@ -158,0 +162,7 @@ handoff. It follows the artifact-minimalism rule in `AGENTS.md`.
+## reader model, when material
+- starting knowledge or practice:
+- old or incomplete model to update:
+- likely confusion or overload point:
+- desired model or practice after use:
+- status: confirmed / inferred / unknown / assumption
+
@@ -367,0 +378,2 @@ Stop and surface ambiguity when:
+- reader starting state is unknown and different plausible states would require
+  materially different teaching or explanation;
@@ -382,0 +395,2 @@ action. It should not include analysis or draft content.
+- material reader starting state and uncertainty are visible without invented
+  demographic or psychological detail;
diff --git a/agents/writer_agent.md b/agents/writer_agent.md
index d038520..c1c6f33 100644
--- a/agents/writer_agent.md
+++ b/agents/writer_agent.md
@@ -53,0 +54,3 @@ owned by `/kb/domain_knowledge_pack_standard.md`.
+- apply the conditional Learning Design sequence `раньше -> сейчас -> почему ->
+  пример -> что делать` when approved and useful, adapting it rather than
+  forcing a five-part outline;
@@ -131,0 +135 @@ Conditional:
+- use an unsupported example to make a learning transition feel concrete;
@@ -235,0 +240,3 @@ should not repeat full research or status history.
+- teaching/explanation uses the approved reader transition and supported
+  examples without becoming formulaic or overexplaining what the reader already
+  knows;
diff --git a/kb/audience_outcome_alignment.md b/kb/audience_outcome_alignment.md
index c0ae464..32954a9 100644
--- a/kb/audience_outcome_alignment.md
+++ b/kb/audience_outcome_alignment.md
@@ -67,0 +68,32 @@ pipeline, review gate, score, persona document, or mandatory standalone file.
+## Reader Model Function
+
+Reader Model is a shared process function for `Teach`, `Understand`, complex
+explanation, change communication, and other tasks where prior knowledge or an
+old mental model materially affects success. It is not a standing role.
+
+Use the smallest useful model:
+
+- known starting knowledge or practice;
+- old, incomplete, or misleading model to update;
+- terms, examples, or assumptions the reader already has;
+- likely point of confusion or overload;
+- target model or action after the artifact.
+
+The model must be grounded in the request, supplied context, prior task
+evidence, or an explicit bounded assumption. Do not invent demographic,
+psychological, motivational, emotional, or proficiency details. If uncertainty
+could materially change the artifact, ask, constrain, or mark the assumption.
+
+Responsibility stays distributed:
+
+- Intake Agent captures or conservatively infers the starting state;
+- Chief Editor confirms the transition and route;
+- Writer Agent realizes the transition in structure, examples, and action;
+- Review Agent challenges whether the intended reader can make the transition;
+- Final Editor preserves the approved transition during controlled
+  finalization.
+
+Record Reader Model only in existing task artifacts. A separate reader-model
+file requires a distinct downstream or governance need and is never the
+default.
+
@@ -271,3 +303,3 @@ Audience and outcome alignment is shared work, not a new role.
-| Intake Agent | Capture or conservatively infer audience, intended outcome, reader context, constraints, and success criteria. |
-| Chief Editor | Route by intended outcome, choose depth, and require audience/outcome fit before production. |
-| Writer Agent | Shape structure, detail, tone, evidence, and next action for the reader. |
+| Intake Agent | Capture or conservatively infer audience, intended outcome, reader starting state, reader context, constraints, and success criteria. |
+| Chief Editor | Confirm the Reader Model transition, route by intended outcome, choose depth, and require audience/outcome fit before production. |
+| Writer Agent | Shape structure, examples, detail, tone, evidence, and next action so the approved reader transition is usable. |
@@ -275,2 +307,2 @@ Audience and outcome alignment is shared work, not a new role.
-| Review Agent | Flag audience mismatch, wrong depth, missing actionability, and generic useful-looking text. |
-| Final Editor | Preserve audience fit, actionability, caveats, and format constraints during finalization. |
+| Review Agent | Flag audience mismatch, broken reader transition, wrong depth, missing actionability, and generic useful-looking text. |
+| Final Editor | Preserve the approved reader transition, audience fit, actionability, caveats, and format constraints during finalization. |
@@ -282,0 +315 @@ This framework does not:
+- create a Reader Model Agent or require a standalone reader-model file;
diff --git a/kb/capability_registry.md b/kb/capability_registry.md
index 2da3ad8..4aa589d 100644
--- a/kb/capability_registry.md
+++ b/kb/capability_registry.md
@@ -525,3 +525,3 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-- Purpose: shape an artifact around the intended reader, decision/action,
-  required depth, tone, format, evidence burden, and success criteria so it is
-  useful rather than merely well-written.
+- Purpose: shape an artifact around the intended reader, Reader Model,
+  decision/action, required depth, tone, format, evidence burden, and success
+  criteria so it is useful rather than merely well-written.
@@ -537,2 +537,3 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-  or infers, Chief Editor routes, Writer Agent and UX Writer apply, Review
-  Agent challenges mismatch, and Final Editor preserves fit.
+  or infers the starting state, Chief Editor confirms the transition and route,
+  Writer Agent and UX Writer apply, Review Agent challenges mismatch, and Final
+  Editor preserves fit.
@@ -909 +910 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-| Intake Agent | Intake normalization; initial Task Need Recognition signal and advisory view when material; initial audience/outcome capture or inference; initial Professional Communication materiality signal when the request depends on executive brief, recommendation or ask, technical explanation, policy/stakeholder memo, implementation handoff, or dense source compression; initial source boundary detection; initial separation of user-provided facts, assumptions, and unknowns; early task-misunderstanding and missing-constraint detection; planning-depth signal; risk/client-profile suggestion. |
+| Intake Agent | Intake normalization; initial Task Need Recognition signal and advisory view when material; initial audience/outcome and Reader Model starting-state capture or inference; initial Professional Communication materiality signal when the request depends on executive brief, recommendation or ask, technical explanation, teaching, policy/stakeholder memo, implementation handoff, or dense source compression; initial source boundary detection; initial separation of user-provided facts, assumptions, and unknowns; early task-misunderstanding and missing-constraint detection; planning-depth signal; risk/client-profile suggestion. |
@@ -911 +912 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-| Writer Agent | Editorial structure planning within approved route; drafting from approved evidence; preservation of analytical structure, Professional Analysis product shape, Professional Communication message architecture, synthesis, recommendation, architecture rationale, assumptions, alternatives, uncertainty, caveats, density choices, action path, and sufficiency cues when material; quality-preservation during drafting; audience/outcome shaping; tradeoff communication; over-polishing/unsupported-claim detection; assumption/caveat preservation; repair for draft findings; bounded source-conversion production only when a mini-contract assigns it. |
+| Writer Agent | Editorial structure and Learning Design within the approved route; drafting from approved evidence; realization of Cognitive Bridge, Moments of Insight, Practical Transformation, and supported examples when material; preservation of analytical structure, Professional Analysis product shape, Professional Communication message architecture, synthesis, recommendation, architecture rationale, assumptions, alternatives, uncertainty, caveats, density choices, action path, and sufficiency cues when material; quality-preservation during drafting; audience/outcome shaping; tradeoff communication; over-polishing/unsupported-claim detection; assumption/caveat preservation; repair for draft findings; bounded source-conversion production only when a mini-contract assigns it. |
diff --git a/kb/professional_communication.md b/kb/professional_communication.md
index fafa85c..a3a91f1 100644
--- a/kb/professional_communication.md
+++ b/kb/professional_communication.md
@@ -6 +6,2 @@ lenses for message architecture, recommendation presentation, explanation
-quality, technical communication, information density, and actionability.
+quality, learning design, technical communication, information density, and
+actionability.
@@ -25,0 +27,2 @@ It helps agents:
+- sequence teaching and explanation from the reader's current model to a usable
+  new model or practice;
@@ -93,0 +97 @@ Select only the lenses that fit the task.
+| Learning design | The artifact must update a mental model or teach a repeatable practice. | What was true or believed before, what is true now, why did it change, which example makes it concrete, and what should the reader do? |
@@ -117,0 +122,29 @@ review need, or governance need justifies it.
+## Reader Model And Learning Design
+
+Audience & Outcome Alignment owns the Reader Model and Reader Outcome Contract.
+Professional Communication owns the explanation sequence used to realize them.
+
+For teaching, understanding, and complex explanation, consider this conditional
+pattern:
+
+```text
+раньше -> сейчас -> почему -> пример -> что делать
+```
+
+- `раньше`: name the reader's prior model or practice without caricaturing it;
+- `сейчас`: state the updated model or current practice;
+- `почему`: explain the change, mechanism, evidence, or tradeoff;
+- `пример`: make the difference concrete with a supported example;
+- `что делать`: translate the new model into an action, decision, or habit.
+
+The pattern is not a mandatory five-part outline. Combine, reorder, or omit
+parts when another sequence better serves the reader. Do not force chronology
+into a task that needs an action-first, problem-first, reference, decision, or
+implementation structure. Examples must stay inside the source boundary; an
+illustrative example must be labeled and must not invent product behavior.
+
+Learning Design is complete only when the Cognitive Bridge is usable, the
+Moments of Insight are actually expressed, and Practical Transformation is
+specific enough to review. It does not create a Learning Designer role,
+pipeline, score, stage, or standalone artifact.
+
@@ -145,0 +179,3 @@ Use `/kb/editorial_failure_modes.md` when these warning signs appear:
+- explanation that presents only the new model and makes the reader infer why
+  the old model no longer works;
+- abstract teaching with no supported example or usable next practice;
@@ -187,0 +224,3 @@ state:
+- whether material teaching connects the old/current model to the updated
+  model, makes the transition concrete, and enables the approved practical
+  transformation;
@@ -197,2 +236,2 @@ Professional Communication is shared work, not a new role.
-| Chief Editor | Select the capability when communication transfer quality materially affects route, depth, review, or governance. |
-| Intake Agent | Capture or infer early signs that reader action, decision, channel, or density will shape communication. |
+| Chief Editor | Select the capability and Learning Design lens when communication transfer or reader change materially affects route, depth, review, or governance. |
+| Intake Agent | Capture or infer early signs that reader starting state, action, decision, channel, or density will shape communication. |
@@ -200 +239 @@ Professional Communication is shared work, not a new role.
-| Writer Agent | Shape draft message architecture, density, explanation, recommendations, and action path inside approved scope. |
+| Writer Agent | Shape draft message architecture, density, explanation, supported examples, reader transition, recommendations, and action path inside approved scope. |
@@ -214,0 +254,2 @@ Professional Communication does not:
+- create a Learning Designer role or force the learning pattern onto every
+  artifact;
diff --git a/pipelines/article_pipeline.md b/pipelines/article_pipeline.md
index 53bcb60..30e5ce8 100644
--- a/pipelines/article_pipeline.md
+++ b/pipelines/article_pipeline.md
@@ -14 +14,6 @@ This pipeline governs creation of article-style editorial materials:
-The pipeline turns a task brief into a reviewed and finalized article deliverable through controlled intake, orchestration, optional research, writing, review, finalization, and Chief Editor governance.
+The pipeline turns a task brief into a reviewed and finalized article
+deliverable through controlled intake, orchestration, optional research,
+writing, review, finalization, and Chief Editor governance. When teaching,
+understanding, or complex explanation is material, it also preserves the
+approved Reader Model transition and Learning Design without adding a role or
+artifact.
@@ -74,0 +80,2 @@ packet from those owners, then add only article-specific context:
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and approved Learning Design sequence when material.
@@ -276,0 +284,2 @@ Writing rules:
+- teaching/explanation must realize the approved reader transition and use only
+  supported or clearly labeled illustrative examples;
@@ -295,0 +305 @@ Review Agent must validate:
+- approved Reader Model transition and Learning Design when material;
@@ -376 +386 @@ Quality gates are mandatory and artifact-backed.
-| Orchestration gate | `orchestration_plan.md` selects Article Pipeline, assigns roles, and records research need | missing plan or invalid role |
+| Orchestration gate | `orchestration_plan.md` selects Article Pipeline, assigns roles, records research need, and includes the reader transition when material | missing plan, invalid role, or missing material Reader Model contract |
@@ -378 +388 @@ Quality gates are mandatory and artifact-backed.
-| Writing gate | `outline.md`, `draft.md`, and `claims-used.md` when needed exist and avoid unsafe claims | invented facts or missing claim traceability |
+| Writing gate | `outline.md`, `draft.md`, and `claims-used.md` when needed exist, avoid unsafe claims, and realize the approved reader transition when material | invented facts, missing claim traceability, or broken material Cognitive Bridge |
~~~~

## ROQ-P0-05 reader review lens

Commit slice: `ff18cf4`

Изменённые файлы:

- `AGENTS.md`
- `agents/review_agent.md`
- `kb/audience_outcome_alignment.md`
- `kb/capability_registry.md`
- `kb/professional_communication.md`
- `kb/task_object_model.md`
- `pipelines/review_pipeline.md`
- `templates/tasks/review_task_template.md`

~~~~diff
diff --git a/AGENTS.md b/AGENTS.md
index d8a4646..3c7e6d4 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1276,0 +1277,5 @@ Review должен быть максимально воспроизводимы
+- когда Reader Review материален: понимание, запоминаемость, применимость,
+  Cognitive Bridge, Learning Design sequence и reader burden с явными
+  `pass`/`fail`/`not applicable`/`needs clarification` статусами и ссылками на
+  Reader Outcome Contract или точные места артефакта; вкус сам по себе не
+  является finding;
diff --git a/agents/review_agent.md b/agents/review_agent.md
index 0196f06..4aa4fbd 100644
--- a/agents/review_agent.md
+++ b/agents/review_agent.md
@@ -69,0 +70,3 @@ boundaries are owned by `/kb/task_need_recognition.md`.
+- run the conditional Reader Review Lens when a Reader Outcome Contract,
+  Cognitive Bridge, teaching/understanding outcome, or other material reader
+  change governs the artifact;
@@ -115,0 +119,28 @@ boundaries are owned by `/kb/task_need_recognition.md`.
+## Reader Review Lens
+
+Reader Review is a deterministic lens inside the existing `review.md`. It is
+not a new role, gate, cycle, score, or standalone artifact.
+
+Activate it when the task must teach, explain, update a mental model, change a
+reader practice, or otherwise has a material Reader Outcome Contract. For each
+criterion use `pass`, `fail`, `not applicable`, or `needs clarification`:
+
+| Criterion | Review question |
+| --- | --- |
+| Understanding | Can the intended reader state the updated model, decision, or main transfer without reconstructing it from scattered sections? |
+| Retention | Are the approved 3-5 Moments of Insight actually expressed as memorable ideas rather than headings or generic summaries? |
+| Application | Can the reader perform the approved Practical Transformation with the detail and boundaries provided? |
+| Cognitive Bridge | Does the artifact connect the recorded old/incomplete model to the new model instead of presenting only the destination? |
+| Learning sequence | When material, does the explanation provide an effective equivalent of `раньше -> сейчас -> почему -> пример -> что делать` without forcing that exact outline? |
+| Reader burden | Do jargon density, academic distance, abstraction, duplication, or overload prevent the intended outcome? |
+
+Every `fail` or `needs clarification` must cite the Reader Outcome Contract,
+brief, Editorial Decision Frame, and/or exact artifact section. State the
+reader consequence, repair owner, bounded repair scope, do-not-change area, and
+re-review scope. A preference such as "I would write this more simply" is not a
+finding unless the reviewer can show which reader outcome it blocks.
+
+Reader Review does not test whether prose is merely pleasant or easy. It may
+not weaken factual validation, evidence, neutrality, traceability, caveats,
+uncertainty, source boundaries, or review independence.
+
@@ -136,0 +168,2 @@ Conditional:
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and Learning Design notes when Reader Review is material;
@@ -173,0 +207 @@ Required:
+  Reader Review Lens when applicable,
@@ -223,0 +258,2 @@ artifacts must never become silently mandatory.
+- fail Reader Review on taste, personal style, generic readability preference,
+  or an imagined persona not supported by task evidence;
@@ -292,0 +329,2 @@ The Review Agent may decide:
+- whether Reader Review is `pass`, `fail`, `not applicable`, or
+  `needs clarification` for each material criterion;
@@ -346,0 +385,2 @@ Stop and mark blocked or escalate when:
+- the Reader Outcome Contract or reader starting state is missing or ambiguous
+  enough that a material teaching/explanation outcome cannot be reviewed;
@@ -403,0 +444,3 @@ short examples needed to clarify a finding.
+- Reader Review is completed when material: understanding, retention,
+  application, Cognitive Bridge, Learning Design sequence, and reader burden
+  have deterministic statuses and evidence-backed bounded repairs;
diff --git a/kb/audience_outcome_alignment.md b/kb/audience_outcome_alignment.md
index 32954a9..9f06139 100644
--- a/kb/audience_outcome_alignment.md
+++ b/kb/audience_outcome_alignment.md
@@ -273,0 +274,3 @@ Final Editor preserves actionability and fit inside the approved scope.
+When a Reader Outcome Contract is material, Review Agent records the
+deterministic Reader Review Lens inside `review.md`; this does not create a new
+role or artifact.
diff --git a/kb/capability_registry.md b/kb/capability_registry.md
index 4aa589d..ee0a9f8 100644
--- a/kb/capability_registry.md
+++ b/kb/capability_registry.md
@@ -914 +914 @@ gates, lifecycle stages, pipelines, or mandatory ordinary task artifacts.
-| Review Agent | Independent review; Task Need Recognition challenge for evidence/recommendation/decision separation, proportionality, negative evidence, uncertainty, owner boundaries, and non-automation when material; Professional Analysis challenge for unclear analytical product, missing decision context, weak synthesis, hidden options or criteria, unsupported recommendation, missing implications or risks, and unreviewable uncertainty when material; Professional Communication challenge for missing or buried main point, weak message architecture, wrong density, unclear recommendation or ask, missing next action, hidden caveats, misleading compression, weak explanation fit, technical ambiguity, and unreviewable reader transfer when material; architecture-review challenge for missing drivers, vague quality attributes, missing scenarios, hidden assumptions, architecture/implementation confusion, missing rejected alternatives, undocumented accepted risks, and decisions without rationale; Engineering Review challenge for changed surface, selected lenses, validation, security/config/interface/data/reliability/performance risks, and engineering residual risk when material; analytical-reasoning challenge for wrong question, premature closure, confirmation bias, hidden assumptions, contradiction smoothing, false precision, unsupported recommendation, weak sufficiency, and unbounded research; quality-attribute challenge; audience/outcome mismatch challenge; option-evaluation challenge; evidence-confidence challenge; failure-mode challenge; learning/canon candidate, stale-knowledge, correction/retirement, and memory-sync challenge when material; review-side source/client/profile checks; re-review after repair. |
+| Review Agent | Independent review; Task Need Recognition challenge for evidence/recommendation/decision separation, proportionality, negative evidence, uncertainty, owner boundaries, and non-automation when material; Professional Analysis challenge for unclear analytical product, missing decision context, weak synthesis, hidden options or criteria, unsupported recommendation, missing implications or risks, and unreviewable uncertainty when material; Professional Communication and deterministic Reader Review challenge for missing or buried main point, weak message architecture, wrong density, unclear recommendation or ask, missing next action, hidden caveats, misleading compression, weak explanation fit, broken Cognitive Bridge, missing application path, reader burden, technical ambiguity, and unreviewable reader transfer when material; architecture-review challenge for missing drivers, vague quality attributes, missing scenarios, hidden assumptions, architecture/implementation confusion, missing rejected alternatives, undocumented accepted risks, and decisions without rationale; Engineering Review challenge for changed surface, selected lenses, validation, security/config/interface/data/reliability/performance risks, and engineering residual risk when material; analytical-reasoning challenge for wrong question, premature closure, confirmation bias, hidden assumptions, contradiction smoothing, false precision, unsupported recommendation, weak sufficiency, and unbounded research; quality-attribute challenge; audience/outcome mismatch challenge; option-evaluation challenge; evidence-confidence challenge; failure-mode challenge; learning/canon candidate, stale-knowledge, correction/retirement, and memory-sync challenge when material; review-side source/client/profile checks; re-review after repair. |
diff --git a/kb/professional_communication.md b/kb/professional_communication.md
index a3a91f1..ed3f4a4 100644
--- a/kb/professional_communication.md
+++ b/kb/professional_communication.md
@@ -241 +241 @@ Professional Communication is shared work, not a new role.
-| Review Agent | Challenge communication failures inside existing `review.md` when material. |
+| Review Agent | Challenge communication failures and, for material learning/explanation work, apply Reader Review against the approved reader outcome and Learning Design inside existing `review.md`; taste alone is not a finding. |
diff --git a/kb/task_object_model.md b/kb/task_object_model.md
index 65cd0c0..3d4d910 100644
--- a/kb/task_object_model.md
+++ b/kb/task_object_model.md
@@ -161 +161 @@ requires it.
-| `review.md` | Independent confidence gate: reviewed artifacts, independence basis, analytical reasoning challenge when material, Professional Analysis challenge when material, Professional Communication challenge when material, Architecture Review challenge when material, Engineering Review challenge when material, active Domain Knowledge Pack activation/boundary/source challenge when material, audience/outcome fit, quality-attribute fit when material, evidence/confidence challenge, assumptions and unknowns, findings, verdict, required changes, blockers, learning/canon candidates when material, and next action. |
+| `review.md` | Independent confidence gate: reviewed artifacts, independence basis, analytical reasoning challenge when material, Professional Analysis challenge when material, Professional Communication challenge when material, Reader Review Lens when material, Architecture Review challenge when material, Engineering Review challenge when material, active Domain Knowledge Pack activation/boundary/source challenge when material, audience/outcome fit, quality-attribute fit when material, evidence/confidence challenge, assumptions and unknowns, findings, verdict, required changes, blockers, learning/canon candidates when material, and next action. |
diff --git a/pipelines/review_pipeline.md b/pipelines/review_pipeline.md
index da07f46..a4bd6ac 100644
--- a/pipelines/review_pipeline.md
+++ b/pipelines/review_pipeline.md
@@ -79,0 +80,5 @@ detail level, tone, format, evidence depth, omissions, and success criteria.
+When reviewed work has a material Reader Outcome Contract, teaches or explains,
+updates a mental model, or must change reader practice, review applies the
+Reader Review Lens defined in `/agents/review_agent.md`. The result stays inside
+`review.md`; it does not create a new role, gate, cycle, score, or artifact.
+
@@ -186,0 +192,3 @@ packet from those owners, then add only review-specific context:
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and Learning Design notes when the reader outcome is
+  material;
@@ -264 +272 @@ compact evidence. Missing evidence for material claims should produce
-| `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
+| `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Reader Review Lens when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
@@ -378,0 +387,4 @@ Compact review minimum:
+- compact Reader Review when a material Reader Outcome Contract, Cognitive
+  Bridge, teaching/understanding outcome, or reader-practice change governs the
+  work; record deterministic statuses for understanding, retention,
+  application, bridge, learning sequence, and reader burden;
@@ -458,0 +471 @@ Quality gates are mandatory and artifact-backed.
+| Reader Review gate | When material, understanding, retention, application, Cognitive Bridge, Learning Design sequence, and reader burden have deterministic statuses tied to the Reader Outcome Contract and exact artifact evidence | missing bridge, headings substituted for memorable ideas, vague Practical Transformation, academic or jargon overload that blocks the outcome, or a taste preference presented as a finding |
@@ -480,0 +494,2 @@ allow the review stage to close, and the review-specific packet is current:
+- when Reader Review is material, `review.md` records all applicable Reader
+  Review criteria, evidence, reader consequences, and bounded repair routing;
diff --git a/templates/tasks/review_task_template.md b/templates/tasks/review_task_template.md
index f87603c..13f0033 100644
--- a/templates/tasks/review_task_template.md
+++ b/templates/tasks/review_task_template.md
@@ -110,0 +111,16 @@ Conditional files:
+## reader review, when material
+
+| Criterion | Status | Evidence | Reader consequence | Required action |
+| --- | --- | --- | --- | --- |
+| Understanding | pass/fail/not applicable/needs clarification | | | |
+| Retention | pass/fail/not applicable/needs clarification | | | |
+| Application | pass/fail/not applicable/needs clarification | | | |
+| Cognitive Bridge | pass/fail/not applicable/needs clarification | | | |
+| Learning sequence | pass/fail/not applicable/needs clarification | | | |
+| Reader burden | pass/fail/not applicable/needs clarification | | | |
+
+- Bounded repair owner:
+- Repair scope:
+- Do-not-change:
+- Re-review scope:
+
@@ -199,0 +216 @@ blockers, and next action.
+- Reader Review is complete or explicitly not applicable.
~~~~

## ROQ-P0-06 companion pass

Commit slice: `50f2399`

Изменённые файлы:

- `agents/final_editor.md`
- `agents/review_agent.md`
- `kb/professional_communication.md`
- `pipelines/review_pipeline.md`
- `templates/tasks/review_task_template.md`

~~~~diff
diff --git a/agents/final_editor.md b/agents/final_editor.md
index 7545bad..8b96381 100644
--- a/agents/final_editor.md
+++ b/agents/final_editor.md
@@ -51,0 +52,3 @@ owned by `/kb/domain_knowledge_pack_standard.md`.
+- preserve the approved Companion Pass balance of naturalness, concreteness,
+  distance, and precision; do not perform substantive companion rewriting
+  during finalization;
@@ -127,0 +131,2 @@ Conditional:
+- repair a failed, missing, or `needs clarification` Companion Pass through
+  substantive finalization edits;
@@ -191,0 +197,2 @@ Stop and route back when:
+- Companion Pass is failed, missing when reader-facing, or requires changes to
+  structure, claims, examples, argument, or meaning;
@@ -221,0 +229,2 @@ status history.
+- approved Companion Pass balance remains intact and no substantive companion
+  rewrite occurred during finalization;
diff --git a/agents/review_agent.md b/agents/review_agent.md
index 4aa4fbd..5d40c51 100644
--- a/agents/review_agent.md
+++ b/agents/review_agent.md
@@ -72,0 +73,3 @@ boundaries are owned by `/kb/task_need_recognition.md`.
+- run Companion Pass for reader-facing material before `approved`, and route
+  substantive communication repair back to Writer Agent rather than using
+  finalization as a rewrite stage;
@@ -146,0 +150,13 @@ uncertainty, source boundaries, or review independence.
+## Companion Pass
+
+For reader-facing material, record `pass`, `fail`, `not applicable`, or
+`needs clarification` for naturalness, concreteness, avoidable academic or
+jargon distance, and precision preservation. Use the canonical criteria in
+`/kb/professional_communication.md`.
+
+Companion Pass is part of `review.md`, not a new role, gate, cycle, score, or
+artifact. A failure must identify the exact wording or pattern, the concrete
+reader consequence, and a bounded repair. If repair would change structure,
+claims, examples, argument, or meaning, outcome cannot be `approved` for Final
+Editor cleanup; route it to Writer Agent and re-review the repaired scope.
+
@@ -207,0 +224 @@ Required:
+  Companion Pass when reader-facing,
@@ -259,0 +277,2 @@ artifacts must never become silently mandatory.
+- treat Companion Pass as permission for fake empathy, invented familiarity,
+  sales language, jokes, new claims, or precision loss;
@@ -330,0 +350,3 @@ The Review Agent may decide:
+- whether Companion Pass is `pass`, `fail`, `not applicable`, or
+  `needs clarification` for each material criterion and whether repair is
+  substantive enough to require Writer Agent;
diff --git a/kb/professional_communication.md b/kb/professional_communication.md
index ed3f4a4..341097a 100644
--- a/kb/professional_communication.md
+++ b/kb/professional_communication.md
@@ -150,0 +151,25 @@ pipeline, score, stage, or standalone artifact.
+## Companion Pass
+
+Companion Pass is the last communication check inside the existing review
+before reader-facing material can receive `approved`. It asks:
+
+> Could a knowledgeable colleague explain this to the intended reader in this
+> way, naturally and directly, without losing precision?
+
+Use `pass`, `fail`, `not applicable`, or `needs clarification` for:
+
+- naturalness: sentences sound like purposeful explanation rather than a
+  template, taxonomy dump, or performance of expertise;
+- concreteness: abstractions are connected to supported examples, decisions,
+  actions, or consequences when needed;
+- distance: jargon, nominalization, formalism, and academic framing do not
+  create avoidable distance from the intended reader;
+- precision preservation: simplification retains evidence, boundaries,
+  caveats, uncertainty, technical meaning, and traceability.
+
+This is not an invitation to add fake empathy, invented familiarity, jokes,
+sales language, or an ungrounded conversational persona. It cannot authorize
+new facts or meaning changes. If passing it requires substantive rewriting,
+Review Agent returns bounded repair to Writer Agent; Final Editor must not use
+finalization to perform that rewrite.
+
@@ -185,0 +211,3 @@ Use `/kb/editorial_failure_modes.md` when these warning signs appear:
+- reader-facing prose that is correct but sounds like an academic checklist,
+  taxonomy dump, or synthetic expert performance instead of a direct
+  explanation;
@@ -226,0 +255,2 @@ state:
+- whether Companion Pass is complete for reader-facing material without
+  trading precision for warmth or ease;
@@ -241,2 +271,2 @@ Professional Communication is shared work, not a new role.
-| Review Agent | Challenge communication failures and, for material learning/explanation work, apply Reader Review against the approved reader outcome and Learning Design inside existing `review.md`; taste alone is not a finding. |
-| Final Editor | Preserve approved message path, actionability, caveats, density, and reader fit during finalization. |
+| Review Agent | Challenge communication failures, apply Reader Review when material, and run Companion Pass for reader-facing material inside existing `review.md`; taste alone is not a finding. |
+| Final Editor | Preserve approved message path, Companion Pass balance, actionability, caveats, density, and reader fit during finalization; do not perform substantive companion rewriting. |
@@ -255,0 +286 @@ Professional Communication does not:
+- create a Companion Agent, stage, gate, score, or standalone artifact;
diff --git a/pipelines/review_pipeline.md b/pipelines/review_pipeline.md
index a4bd6ac..010bbb2 100644
--- a/pipelines/review_pipeline.md
+++ b/pipelines/review_pipeline.md
@@ -84,0 +85,4 @@ Reader Review Lens defined in `/agents/review_agent.md`. The result stays inside
+Reader-facing work also receives Companion Pass inside the same review. A
+failure that requires substantive rewriting routes to Writer Agent and
+bounded re-review; Final Editor is not a substitute repair owner.
+
@@ -390,0 +395,2 @@ Compact review minimum:
+- compact Companion Pass for reader-facing work: naturalness, concreteness,
+  avoidable academic or jargon distance, and precision preservation;
@@ -471,0 +478 @@ Quality gates are mandatory and artifact-backed.
+| Companion Pass gate | Reader-facing work is natural and concrete enough for the intended reader while preserving precision, evidence, caveats, boundaries, and traceability | taxonomy dump, synthetic expert performance, avoidable academic distance, unsupported friendliness, precision loss, or substantive repair deferred to Final Editor |
@@ -495,0 +503,2 @@ allow the review stage to close, and the review-specific packet is current:
+- when material is reader-facing, `review.md` records Companion Pass and routes
+  substantive repair to Writer Agent before approval;
diff --git a/templates/tasks/review_task_template.md b/templates/tasks/review_task_template.md
index 13f0033..964a4e1 100644
--- a/templates/tasks/review_task_template.md
+++ b/templates/tasks/review_task_template.md
@@ -126,0 +127,11 @@ Conditional files:
+## companion pass, when reader-facing
+
+| Criterion | Status | Evidence | Reader consequence | Required action |
+| --- | --- | --- | --- | --- |
+| Naturalness | pass/fail/not applicable/needs clarification | | | |
+| Concreteness | pass/fail/not applicable/needs clarification | | | |
+| Avoidable academic or jargon distance | pass/fail/not applicable/needs clarification | | | |
+| Precision preservation | pass/fail/not applicable/needs clarification | | | |
+
+- Substantive Writer repair required: yes/no
+
@@ -216,0 +228 @@ blockers, and next action.
+- Companion Pass is complete or explicitly not applicable.
~~~~

## ROQ-P0-07 bounded utility tradeoff

Commit slice: `b53154b`

Изменённые файлы:

- `agents/chief_editor.md`
- `agents/review_agent.md`
- `kb/editorial_planning_framework.md`
- `kb/editorial_quality_attributes.md`
- `templates/artifacts/orchestration_plan_template.md`

~~~~diff
diff --git a/agents/chief_editor.md b/agents/chief_editor.md
index 839002d..b032151 100644
--- a/agents/chief_editor.md
+++ b/agents/chief_editor.md
@@ -50,0 +51,4 @@ signals and advisory recommendations are owned by
+- authorize a Bounded Utility Tradeoff only for a concrete recorded reader need
+  and only with bounded scope, evidence/freshness basis, stale-if trigger,
+  intentionally relaxed attribute, expected benefit, and preserved
+  non-relaxable guardrails;
@@ -294,0 +299,3 @@ Required when applicable:
+- compact Bounded Utility Tradeoff inside the existing Editorial Decision Frame
+  or quality profile when a less durable, product-specific, chronological, or
+  otherwise local bridge materially improves the recorded reader journey.
@@ -416,0 +424 @@ The Chief Editor may decide:
+- whether a Bounded Utility Tradeoff is justified and sufficiently bounded;
diff --git a/agents/review_agent.md b/agents/review_agent.md
index 5d40c51..0e5416a 100644
--- a/agents/review_agent.md
+++ b/agents/review_agent.md
@@ -82,0 +83,3 @@ boundaries are owned by `/kb/task_need_recognition.md`.
+- challenge each Bounded Utility Tradeoff against its concrete reader need,
+  bounded scope, evidence/freshness basis, stale-if trigger, intentionally
+  relaxed attribute, expected benefit, and non-relaxable guardrails;
@@ -285,0 +289,2 @@ artifacts must never become silently mandatory.
+- approve a Bounded Utility Tradeoff that is implicit, unbounded, stale,
+  promotional, unsupported, or relaxes a non-relaxable guardrail;
@@ -354,0 +360,2 @@ The Review Agent may decide:
+- whether each Bounded Utility Tradeoff is explicit, limited, evidence-backed,
+  fresh enough, useful to the recorded reader, and guardrail-safe;
diff --git a/kb/editorial_planning_framework.md b/kb/editorial_planning_framework.md
index 611e8f3..182636a 100644
--- a/kb/editorial_planning_framework.md
+++ b/kb/editorial_planning_framework.md
@@ -125,0 +126,8 @@ Record, at the planning depth required:
+When a concrete reader starting point makes a short chronology, current
+product bridge, or other less durable route materially more useful, Chief
+Editor may record a Bounded Utility Tradeoff from
+`/kb/editorial_quality_attributes.md`. It must name the bounded scope,
+evidence/freshness basis, stale-if trigger, intentionally relaxed attribute,
+expected reader benefit, and preserved non-relaxable guardrails. Convenience
+or liveliness alone is not sufficient.
+
@@ -157,0 +166,2 @@ Planning is complete when:
+- any bounded utility tradeoff is explicit, evidence-backed, limited, and
+  reviewable rather than an implicit exception;
diff --git a/kb/editorial_quality_attributes.md b/kb/editorial_quality_attributes.md
index 1dd0801..e556b57 100644
--- a/kb/editorial_quality_attributes.md
+++ b/kb/editorial_quality_attributes.md
@@ -116,0 +117,29 @@ artifact that the next owner or reviewer will read.
+## Bounded Utility Tradeoff
+
+Chief Editor may authorize a local, explicit tradeoff when a concrete reader
+need is better served by a less durable, less exhaustive, more product-specific,
+or more chronological bridge. Examples include a short chronology from the
+reader's named stopping point or a current product bridge that makes an
+otherwise abstract change usable.
+
+Record the decision in the existing Editorial Decision Frame or quality
+profile:
+
+```markdown
+## bounded utility tradeoff
+- concrete reader need:
+- bounded scope:
+- evidence and freshness basis:
+- stale-if or review trigger:
+- attribute intentionally relaxed:
+- non-relaxable guardrails preserved:
+- expected reader benefit:
+```
+
+The decision may relax completeness, durability, breadth, formality, or
+exhaustive chronology. It may not relax correctness, evidence support,
+neutrality, traceability required by governance, visible uncertainty and
+caveats, source boundaries, or independent review. Product-specific material
+must state availability or date boundaries when they matter. Review Agent
+challenges both the claimed reader benefit and the preserved guardrails.
+
@@ -163 +192,3 @@ Do not assign numeric scores. Use findings such as `sufficient`, `weak`,
-  whether any quality loss blocks approval.
+  whether any quality loss blocks approval; challenge bounded utility
+  tradeoffs against their reader need, evidence/freshness basis, scope, stale-if
+  trigger, and non-relaxable guardrails.
@@ -252,0 +284,2 @@ This framework does not:
+- use a bounded utility tradeoff to hide unsupported, stale, misleading,
+  promotional, biased, untraceable, or unreviewed content.
diff --git a/templates/artifacts/orchestration_plan_template.md b/templates/artifacts/orchestration_plan_template.md
index 6641e0d..8b59f44 100644
--- a/templates/artifacts/orchestration_plan_template.md
+++ b/templates/artifacts/orchestration_plan_template.md
@@ -121,0 +122,9 @@ artifact and keep this frame compact.
+- Bounded Utility Tradeoff, only when a local chronology, product bridge, or
+  less durable detail directly serves the recorded reader need:
+  - Concrete reader need:
+  - Bounded scope:
+  - Evidence and freshness basis:
+  - Stale-if or review trigger:
+  - Attribute intentionally relaxed:
+  - Expected reader benefit:
+  - Non-relaxable guardrails preserved:
@@ -136,0 +146 @@ artifact and keep this frame compact.
+- Bounded utility tradeoff challenge, if applicable:
~~~~

## ROQ-P1-01 compact reader context integration

Commit slice: `082f543`

Изменённые файлы:

- `scripts/generate_task_pack.py`
- `templates/artifacts/task_manifest_template.md`
- `templates/tasks/social_task_template.md`
- `tests/fixtures/task_pack/reader_outcome_material/brief.md`
- `tests/fixtures/task_pack/reader_outcome_material/draft.md`
- `tests/fixtures/task_pack/reader_outcome_material/orchestration_plan.md`
- `tests/fixtures/task_pack/reader_outcome_material/status.md`
- `tests/fixtures/task_pack/reader_outcome_material/task-manifest.md`
- `tests/test_task_pack_generator.sh`

~~~~diff
diff --git a/scripts/generate_task_pack.py b/scripts/generate_task_pack.py
index dda65d1..0fbc091 100644
--- a/scripts/generate_task_pack.py
+++ b/scripts/generate_task_pack.py
@@ -45,0 +46,5 @@ SOURCE_EVIDENCE_MODE_RE = re.compile(
+READER_OUTCOME_RE = re.compile(
+    r"(?i)\b(reader outcome(?: contract)?|cognitive bridge|moments of insight|"
+    r"practical transformation|learning design|reader review|companion pass|"
+    r"bounded utility tradeoff)\b"
+)
@@ -432,0 +438,17 @@ def generate_pack(task_dir: Path, role: str) -> tuple[dict[str, list[ReadItem]],
+    if role in {"writer", "review_agent"} and READER_OUTCOME_RE.search(combined_context):
+        for file_name, reason in (
+            (
+                "audience_outcome_alignment.md",
+                "Reader Outcome Contract or Reader Model is material in task context",
+            ),
+            (
+                "professional_communication.md",
+                "Learning Design, Reader Review, or Companion Pass is material in task context",
+            ),
+            (
+                "editorial_quality_attributes.md",
+                "reader outcome priority or bounded utility tradeoff is material in task context",
+            ),
+        ):
+            add_item(sections, seen, "Conditional", KB_DIR / file_name, task_dir, reason)
+
diff --git a/templates/artifacts/task_manifest_template.md b/templates/artifacts/task_manifest_template.md
index a757a4a..712c861 100644
--- a/templates/artifacts/task_manifest_template.md
+++ b/templates/artifacts/task_manifest_template.md
@@ -27,0 +28,11 @@ artifact. Keep it short, current, and explicit about versions.
+## reader outcome state
+
+Use only when reader change is material; otherwise omit or mark the first field
+`not applicable`. Keep the full contract and rationale in `brief.md` and
+`orchestration_plan.md` rather than duplicating them here.
+
+- Reader outcome material: yes/no/not applicable
+- Reader Outcome Contract pointer:
+- Reader Review required: compact/normal/full/not applicable
+- Companion Pass required: yes/no/not applicable
+
diff --git a/templates/tasks/social_task_template.md b/templates/tasks/social_task_template.md
index 549546f..a44b469 100644
--- a/templates/tasks/social_task_template.md
+++ b/templates/tasks/social_task_template.md
@@ -102,0 +103,8 @@ Conditional files:
+## reader outcome, only when material
+
+- Starting state or immediate context:
+- Required understanding or action:
+- Failure signal:
+- Reader Review depth: compact/normal/not applicable
+- Companion Pass: required/not applicable
+
@@ -189,0 +198,7 @@ Create only when claims need evidence.
+## compact reader review, when material
+
+- Reader understands the main transfer: pass/fail/not applicable
+- Reader can take the intended action: pass/fail/not applicable
+- Avoidable burden or artificial tone blocks the outcome: yes/no/not applicable
+- Companion Pass: pass/fail/not applicable
+
@@ -224,0 +240 @@ claim caveats, blockers, and next action.
+- Reader outcome checks are compact or explicitly not applicable.
diff --git a/tests/fixtures/task_pack/reader_outcome_material/brief.md b/tests/fixtures/task_pack/reader_outcome_material/brief.md
new file mode 100644
index 0000000..e9149f9
--- /dev/null
+++ b/tests/fixtures/task_pack/reader_outcome_material/brief.md
@@ -0,0 +1,11 @@
+# Brief
+
+Synthetic material reader-outcome fixture. No real task materials.
+
+## Reader Outcome Contract
+
+- Starting state: reader knows the old workflow.
+- Required change: reader can select and use the updated workflow.
+- Practical result: reader applies the new workflow without guessing.
+- Failure signal: reader can repeat terms but cannot act.
+- Guardrails: preserve evidence and uncertainty.
diff --git a/tests/fixtures/task_pack/reader_outcome_material/draft.md b/tests/fixtures/task_pack/reader_outcome_material/draft.md
new file mode 100644
index 0000000..083d489
--- /dev/null
+++ b/tests/fixtures/task_pack/reader_outcome_material/draft.md
@@ -0,0 +1,3 @@
+# Draft
+
+Synthetic draft for reader-outcome task pack fixture.
diff --git a/tests/fixtures/task_pack/reader_outcome_material/orchestration_plan.md b/tests/fixtures/task_pack/reader_outcome_material/orchestration_plan.md
new file mode 100644
index 0000000..cbfdb03
--- /dev/null
+++ b/tests/fixtures/task_pack/reader_outcome_material/orchestration_plan.md
@@ -0,0 +1,12 @@
+# Orchestration Plan
+
+Pipeline: article
+Risk mode: standard
+
+## Editorial Decision Frame
+
+- Cognitive Bridge: old workflow to updated workflow.
+- Moments of Insight: why the workflow changed; how to select it; how to verify it.
+- Practical Transformation: select, execute, and verify the updated workflow.
+- Bounded Utility Tradeoff: not applicable.
+- Review focus: Reader Review and Companion Pass.
diff --git a/tests/fixtures/task_pack/reader_outcome_material/status.md b/tests/fixtures/task_pack/reader_outcome_material/status.md
new file mode 100644
index 0000000..176e552
--- /dev/null
+++ b/tests/fixtures/task_pack/reader_outcome_material/status.md
@@ -0,0 +1,5 @@
+# Status
+
+Current status: writing
+Previous status: planning
+Responsible role: writer
diff --git a/tests/fixtures/task_pack/reader_outcome_material/task-manifest.md b/tests/fixtures/task_pack/reader_outcome_material/task-manifest.md
new file mode 100644
index 0000000..f5db910
--- /dev/null
+++ b/tests/fixtures/task_pack/reader_outcome_material/task-manifest.md
@@ -0,0 +1,12 @@
+# Task Manifest
+
+Task ID: SYNTHETIC-PACK-READER-OUTCOME
+Current status: writing
+Selected pipeline: article
+Client profile: none
+Current artifact: draft.md
+Reader outcome material: yes
+Reader Outcome Contract pointer: brief.md
+Reader Review required: normal
+Companion Pass required: yes
+Next required action: continue synthetic draft.
diff --git a/tests/test_task_pack_generator.sh b/tests/test_task_pack_generator.sh
index ae7dc29..2208c27 100644
--- a/tests/test_task_pack_generator.sh
+++ b/tests/test_task_pack_generator.sh
@@ -82,0 +83,3 @@ run_case_absent "client_profile_pending" "writer" 0 "explicit active client-prof
+run_case "reader_outcome_material" "writer" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
+run_case "reader_outcome_material" "review_agent" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
+run_case_absent "writer_minimal" "writer" 0 "audience_outcome_alignment.md" "professional_communication.md" "editorial_quality_attributes.md"
~~~~

## ROQ-P1-02 calibrate three pilot types

Commit slice: `f9d5c87`

Изменённые файлы:

- `tests/reader-centered-quality-pilot.md`

~~~~diff
diff --git a/tests/reader-centered-quality-pilot.md b/tests/reader-centered-quality-pilot.md
new file mode 100644
index 0000000..4924375
--- /dev/null
+++ b/tests/reader-centered-quality-pilot.md
@@ -0,0 +1,234 @@
+# Reader-Centered Quality Pilot
+
+Status: `synthetic calibration complete; external comparative promotion check pending`
+
+Date: 2026-07-13
+
+## Purpose And Limits
+
+This manual trial calibrates the proposed reader-outcome controls across three
+different artifact types before they become routine. It does not claim that the
+initiative has passed its promotion gate. A strong single-model comparator was
+available only as a prior human comparison for the longread, not as a saved
+artifact in this repository. No equivalent comparator outputs exist here for
+the working document or short text. Project Lead must therefore run or accept a
+label-neutral comparative review before claiming parity on every material
+criterion.
+
+The trial uses no numeric score. Each case records observable evidence,
+regressions to block, the smallest useful Reader Review depth, and the remaining
+human decision.
+
+## Shared Comparison Conditions
+
+- same raw request, brief, source boundary, freshness date, and output
+  constraint for every pair;
+- final user-facing output evaluated separately from governance artifacts;
+- correctness, evidence support, neutrality, traceability, and independent
+  review are non-relaxable;
+- labels are hidden from the human evaluator where practical;
+- model, mode, tools, source set, and date are recorded for every real rerun;
+- a mixed or negative result remains a finding;
+- Project Lead judgment is final; a producing model cannot approve its own
+  comparative result.
+
+## Evaluation Matrix
+
+For each material criterion use `not worse`, `regressed`, `not applicable`, or
+`not yet evidenced`, with exact output fragments or artifact pointers.
+
+| Criterion | Evidence question |
+| --- | --- |
+| Correctness | Are material statements true within the allowed source boundary? |
+| Evidence support | Are material claims supported at the required confidence? |
+| Neutrality | Is the result free of unsupported vendor, product, or editorial bias? |
+| Traceability | Can material claims and decisions be followed to evidence? |
+| Reader fit | Does the result meet the recorded starting state and intended use? |
+| Clarity | Can the reader reconstruct the main transfer without unnecessary work? |
+| Concreteness | Are abstractions connected to supported examples, actions, or decisions? |
+| Model change | Does the Cognitive Bridge move the reader from the old model to the new one? |
+| Retention | Are 3-5 intended ideas expressed as memorable ideas rather than headings? |
+| Practical action | Can the reader perform the Practical Transformation? |
+| Naturalness | Does the material pass Companion Pass without precision loss? |
+| Governance cost | Did the reader benefit justify any extra process or context? |
+
+## Pilot 1 — Educational Longread
+
+### Controlled Input
+
+- Task source: `tasks/TASK-0001-AI-PRACTICE-CATCHUP/brief.md`.
+- Available baseline: `tasks/TASK-0001-AI-PRACTICE-CATCHUP/final_editorial.md`.
+- Reader starting state: experienced AI user whose working model stopped around
+  prompt craft, early projects, and early skills.
+- Required change: adopt a current, practical model for choosing and governing
+  AI work.
+- Source boundary: dated primary sources, no rumors, financial coverage, or
+  OpenAI promotion.
+
+### Baseline Evidence
+
+The baseline preserves strong evidence discipline, neutrality, a dated source
+boundary, a practical four-sprint plan, and an explicit shift from prompt craft
+to a managed work system. It already contains a useful old/new transition in
+`Главный сдвиг: управлять не разговором, а контуром работы` and practical paths
+for research, writing, and applications.
+
+The prior human comparison nevertheless found a reader-fit gap: the user's
+named stopping point was treated mainly as an imprecise date marker. The text
+did not provide a compact, concrete bridge titled or organized around “what
+changed from the practice you remember”, and its high density of terms such as
+Task Contract, provenance, deterministic checks, semantic validation, and
+workflow decomposition could create academic distance.
+
+### Revised Reader Contract To Test
+
+- Cognitive Bridge: “golden prompt formula is still useful, but it now lives
+  inside a larger contract/context/tools/verification system.”
+- Moments of Insight:
+  1. prompt quality is one controllable surface, not the whole system;
+  2. context must be selected and governed, not merely enlarged;
+  3. workflow is the default when the route is known; autonomy is earned;
+  4. product surfaces are interfaces to practices, not the organizing theory;
+  5. evals and human acceptance are part of execution, not postscript.
+- Practical Transformation: tomorrow the reader rewrites one recurring task as
+  a contract, separates stable knowledge from step context, chooses workflow or
+  agent deliberately, and adds a verification loop.
+- Bounded Utility Tradeoff: allow a short dated “then/current practice” bridge
+  with provider-specific examples only when primary sources and availability
+  notes support it; do not turn the material into a release catalog.
+- Reader Review depth: `full`.
+
+### Calibration Result
+
+| Criterion | Result | Evidence or required proof |
+| --- | --- | --- |
+| Correctness, evidence, neutrality, traceability | not worse required | Existing evidence chain remains the preservation baseline. |
+| Reader fit and model change | likely improved by contract; not yet evidenced in a rerun | Revised bridge directly uses the recorded starting point; final output is still required. |
+| Clarity, concreteness, retention, action | not yet evidenced | Full rerun must show the bridge, five ideas, examples, and tomorrow-morning practice in final copy. |
+| Naturalness | not yet evidenced | Companion Pass must cite exact dense or academic passages and preserve technical precision. |
+| Governance cost | acceptable at full depth if output improves | Longread is source-heavy and explicitly educational. |
+
+Human decision still required: label-neutral comparison of the revised final
+output, saved baseline, and a current strong single-model comparator.
+
+## Pilot 2 — Working Document
+
+### Synthetic Controlled Input
+
+Request: prepare a one-page decision memo for a project owner choosing whether
+to automate a recurring source check now. Supplied evidence says the task occurs
+weekly, takes two hours, has two known edge cases, and lacks a stable upstream
+API. Do not invent cost, reliability, or security facts. The reader must choose
+`pilot`, `defer`, or `reject` and assign the next action.
+
+### Failure Baseline
+
+A correct but weak memo can restate workflow options, risks, and automation
+principles without placing the decision first. It may be factually safe yet
+leave the owner to reconstruct the recommendation, evidence boundary, owner,
+and next step.
+
+### Revised Reader Contract To Test
+
+- Starting state: owner knows the recurring pain but not whether evidence is
+  sufficient for automation.
+- Cognitive Bridge: move from “automation saves two hours” to “a bounded pilot
+  is justified only if the unstable input and two edge cases are observable and
+  reversible.”
+- Moments of Insight: decision; evidence basis; key uncertainty; pilot boundary.
+- Practical Transformation: choose one of three outcomes and assign a named
+  validation action.
+- Learning Design: decision-first rather than the five-part educational pattern.
+- Reader Review depth: `normal`.
+
+### Representative Acceptance Evidence
+
+The improved memo must make these elements findable without inference:
+
+1. recommendation: bounded pilot, defer, or reject;
+2. why the available evidence supports only that strength of decision;
+3. explicit unknowns about the upstream source;
+4. two edge cases as validation slices;
+5. owner, next action, stop condition, and reconsideration trigger.
+
+### Calibration Result
+
+| Criterion | Result | Evidence or required proof |
+| --- | --- | --- |
+| Correctness and evidence | not worse by design | No new facts are permitted; recommendation strength is bounded by supplied evidence. |
+| Reader fit, clarity, practical action | improved in the acceptance contract | Decision and next action must be above background. |
+| Model change and retention | material but lighter than longread | Four decision ideas are enough; full teaching sequence would add overhead. |
+| Naturalness | Companion Pass required | Memo must be direct without fake informality. |
+| Governance cost | normal depth justified | The artifact drives a decision; a full pedagogical review is unnecessary. |
+
+Human decision still required: compare actual paired outputs against the five
+representative acceptance elements and the shared matrix.
+
+## Pilot 3 — Short User Text
+
+### Synthetic Controlled Input
+
+Request: reply in at most 80 words to an experienced colleague asking whether
+an agent is always better than a fixed workflow. Use only this supplied fact:
+an agent selects steps dynamically; a workflow follows a defined route. Give a
+practical selection rule and no product claims.
+
+### Failure Baselines
+
+- Academic failure: defines orchestration, autonomy, and control planes but does
+  not answer the selection question inside 80 words.
+- Pleasant unsupported failure: claims agents are smarter, faster, or more
+  modern without evidence.
+- Governance failure: forces a five-part learning outline and a full six-row
+  Reader Review onto a simple low-risk answer.
+
+### Representative Passing Shape
+
+The answer should state that neither is universally better, use a workflow when
+the route is known and repeatable, use an agent when choosing the next step is
+part of the task, and verify the result in either case. It must not add product
+behavior, performance claims, or fake familiarity.
+
+### Calibration Result
+
+| Criterion | Result | Evidence or required proof |
+| --- | --- | --- |
+| Correctness and evidence | preserved | Every statement stays within the two supplied definitions or is a labeled selection rule. |
+| Reader fit, clarity, concreteness, action | satisfiable with compact checks | Reader receives a direct rule inside the word limit. |
+| Model change and retention | compact | One contrast and one action rule are sufficient. |
+| Naturalness | compact Companion Pass | Direct professional language; no artificial pedagogical scaffolding. |
+| Governance cost | must remain minimal | No new artifacts; three outcome questions inside normal review are enough. |
+
+Human decision still required: compare actual paired outputs if promotion is
+claimed. The synthetic case is sufficient only to calibrate `compact` depth and
+anti-regression expectations.
+
+## Cross-Pilot Findings
+
+1. Reader Review depth should depend on intended outcome, reader risk, and
+   explanation complexity, not artifact length alone.
+2. `full` is justified for source-heavy teaching that must update a mental
+   model; `normal` fits decision documents; `compact` fits short low-risk text.
+3. Cognitive Bridge is not always chronology. It may be a contrast, decision
+   rule, or old-assumption/new-boundary transition.
+4. Companion Pass belongs before approval, but it cannot authorize unsupported
+   warmth, simplification, or substantive finalization rewrite.
+5. The longread supplies real baseline evidence; the other cases are synthetic
+   calibration. None of the three proves comparator parity until actual outputs
+   receive Project Lead review.
+
+## Promotion Status
+
+`not yet proven`
+
+Reasons:
+
+- no saved strong single-model comparator is available in this repository;
+- two cases are calibration trials rather than completed production runs;
+- the revised longread has not been generated and reviewed under the new
+  contract;
+- Project Lead has not issued a label-neutral comparative judgment.
+
+This honest non-promotion is a passing governance result. It allows depth
+calibration and regression tests to proceed while preventing synthetic evidence
+from becoming a claim that the initiative already meets its Definition of Done.
~~~~

## ROQ-P1-03 calibrate reader review depth

Commit slice: `720c15b`

Изменённые файлы:

- `agents/review_agent.md`
- `kb/shared_lifecycle_kernel.md`
- `pipelines/article_pipeline.md`
- `pipelines/review_pipeline.md`
- `pipelines/social_pipeline.md`
- `templates/tasks/review_task_template.md`

~~~~diff
diff --git a/agents/review_agent.md b/agents/review_agent.md
index 0e5416a..5d4cca0 100644
--- a/agents/review_agent.md
+++ b/agents/review_agent.md
@@ -131,2 +131,12 @@ Activate it when the task must teach, explain, update a mental model, change a
-reader practice, or otherwise has a material Reader Outcome Contract. For each
-criterion use `pass`, `fail`, `not applicable`, or `needs clarification`:
+reader practice, or otherwise has a material Reader Outcome Contract. Use the
+depth selected under `/kb/shared_lifecycle_kernel.md`:
+
+- `compact`: record whether the reader can understand the main transfer, take
+  the intended action, and do so without avoidable burden or artificial tone;
+- `normal`: use the applicable criteria below and Companion Pass;
+- `full`: use all criteria below, trace them to Cognitive Bridge, Moments of
+  Insight, Practical Transformation, and Learning Design, and challenge any
+  Bounded Utility Tradeoff.
+
+For each recorded criterion use `pass`, `fail`, `not applicable`, or
+`needs clarification`:
@@ -148,0 +159,5 @@ finding unless the reviewer can show which reader outcome it blocks.
+Review Agent may expand the selected depth when inspected evidence reveals a
+material reader risk, but must state the trigger. It may not reduce depth below
+the Chief Editor decision silently. Low-risk short text does not receive the
+six-row teaching check merely because it is reader-facing.
+
@@ -354,0 +370,2 @@ The Review Agent may decide:
+- whether selected Reader Review depth fits intended outcome, reader risk, and
+  explanation complexity, and whether any expansion has a recorded trigger;
@@ -528,0 +546,3 @@ short examples needed to clarify a finding.
+- reader-outcome re-review is limited to the changed scope when independence,
+  evidence checks, and all unaffected findings remain current; otherwise
+  re-review expands only to the invalidated checks;
diff --git a/kb/shared_lifecycle_kernel.md b/kb/shared_lifecycle_kernel.md
index aabedf0..84d63a2 100644
--- a/kb/shared_lifecycle_kernel.md
+++ b/kb/shared_lifecycle_kernel.md
@@ -130,0 +131,17 @@ that every possible artifact must exist.
+### Reader Review Depth
+
+Chief Editor selects the smallest Reader Review depth that fits intended
+outcome, reader risk, and explanation complexity. Review Agent may expand depth
+when inspected material exposes a reader-outcome risk, but must record why.
+
+| Depth | Use when | Minimum existing-review content |
+| --- | --- | --- |
+| `compact` | Short, low-risk material with a simple transfer or action and no complex model change. | Can the reader understand the main transfer, take the intended action, and do so without avoidable burden or artificial tone? |
+| `normal` | A working document, explanation, recommendation, or standard reader-facing artifact has a material Reader Outcome Contract. | Applicable Reader Review criteria, evidence-backed findings, and Companion Pass inside `review.md`. |
+| `full` | A source-heavy or high-governance teaching artifact must change a mental model, sequence complex learning, or justify a Bounded Utility Tradeoff. | Full Cognitive Bridge, 3-5 Moments of Insight, Practical Transformation, Learning Design, all Reader Review criteria, Companion Pass, tradeoff challenge when applicable, and traceability to contract and exact output evidence. |
+
+`not applicable` is valid when reader change is not material. Depth changes the
+amount of recorded evidence, not review independence, factual checks, evidence
+discipline, neutrality, traceability, or the review gate. It never creates a
+standalone reader artifact.
+
@@ -146 +163 @@ it is not a new parallel lifecycle.
-| Repair | Update only the artifacts affected by the bounded issue and preserve re-review scope. |
+| Repair | Update only the artifacts affected by the bounded issue and preserve re-review scope; reader-outcome repair names owner, scope, do-not-change area, and exact re-review scope. |
diff --git a/pipelines/article_pipeline.md b/pipelines/article_pipeline.md
index 30e5ce8..8c6117f 100644
--- a/pipelines/article_pipeline.md
+++ b/pipelines/article_pipeline.md
@@ -207,0 +208,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review is `compact` for a simple reader transfer; a complex teaching
+  outcome may require `normal` despite low factual risk;
@@ -215,0 +218,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review is normally `normal` when reader change is material and
+  `not applicable` when it is not.
@@ -222,0 +227,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review is `full` when the article teaches, updates a mental model, or
+  justifies a Bounded Utility Tradeoff; otherwise record the applicable depth.
diff --git a/pipelines/review_pipeline.md b/pipelines/review_pipeline.md
index 010bbb2..877ddbb 100644
--- a/pipelines/review_pipeline.md
+++ b/pipelines/review_pipeline.md
@@ -359,0 +360,6 @@ required for high-governance material claims.
+Reader Review depth follows `/kb/shared_lifecycle_kernel.md`: `compact` for a
+simple low-risk transfer, `normal` for a material standard reader outcome, and
+`full` for complex or source-heavy model change and high-governance teaching.
+The trigger is intended outcome, reader risk, and explanation complexity, not
+length alone.
+
@@ -391,6 +397,6 @@ Compact review minimum:
-- compact Reader Review when a material Reader Outcome Contract, Cognitive
-  Bridge, teaching/understanding outcome, or reader-practice change governs the
-  work; record deterministic statuses for understanding, retention,
-  application, bridge, learning sequence, and reader burden;
-- compact Companion Pass for reader-facing work: naturalness, concreteness,
-  avoidable academic or jargon distance, and precision preservation;
+- selected-depth Reader Review when a material Reader Outcome Contract governs
+  the work; compact review asks only about main transfer, intended action, and
+  avoidable burden/artificial tone, while normal and full use the applicable
+  detailed criteria;
+- selected-depth Companion Pass for reader-facing work, with full criteria when
+  depth is normal or full;
@@ -419 +425 @@ Normal review uses separate checklist or summary only when downstream review, ro
-For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope.
+For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope. Re-review stays limited to changed scope when unaffected independence, evidence, and review checks remain current; otherwise it expands only to invalidated checks.
diff --git a/pipelines/social_pipeline.md b/pipelines/social_pipeline.md
index 6a18ef7..cdbdf60 100644
--- a/pipelines/social_pipeline.md
+++ b/pipelines/social_pipeline.md
@@ -197,0 +198,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review is normally `compact` or `not applicable`; do not force the
+  full learning block onto short copy;
@@ -206,0 +209,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review remains `compact` unless explanation complexity or reader risk
+  makes `normal` necessary.
@@ -213,0 +218,2 @@ Risk mode classification follows `AGENTS.md` and `/project-state.md`.
+- Reader Review depth still follows reader outcome; high governance does not
+  make an irrelevant teaching block material.
diff --git a/templates/tasks/review_task_template.md b/templates/tasks/review_task_template.md
index 964a4e1..7b631be 100644
--- a/templates/tasks/review_task_template.md
+++ b/templates/tasks/review_task_template.md
@@ -63,0 +64,6 @@ Conditional files:
+## reader review depth
+
+- Selected: compact/normal/full/not applicable
+- Trigger: intended outcome / reader risk / explanation complexity
+- Expanded during review: no/yes and why
+
@@ -111 +117,9 @@ Conditional files:
-## reader review, when material
+## compact reader review, when selected
+
+| Question | Status | Evidence | Required action |
+| --- | --- | --- | --- |
+| Reader understands the main transfer | pass/fail/needs clarification | | |
+| Reader can take the intended action | pass/fail/not applicable/needs clarification | | |
+| Avoidable burden or artificial tone blocks the outcome | pass/fail/needs clarification | | |
+
+## normal or full reader review, when selected
~~~~

## ROQ-P1-04 add reader quality regressions

Commit slice: `8f02041`

Изменённые файлы:

- `tests/README.md`
- `tests/reader-centered-quality-smoke-test.md`

~~~~diff
diff --git a/tests/README.md b/tests/README.md
index 2fff552..8f7f7ac 100644
--- a/tests/README.md
+++ b/tests/README.md
@@ -53,0 +54,6 @@ markdown smoke-tests и synthetic examples:
+- `reader-centered-quality-pilot.md` - three-type manual calibration pilot for
+  longread, working document, and short text; external comparator promotion
+  remains pending.
+- `reader-centered-quality-smoke-test.md` - manual synthetic regression cases
+  for Reader Outcome Contract, Learning Design, Reader Review, Companion Pass,
+  bounded utility tradeoffs, and compact non-activation.
@@ -204,0 +211,11 @@ Professional Communication KB.
+`reader-centered-quality-pilot.md` records the longread baseline evidence and
+two synthetic calibration cases used to select full, normal, and compact Reader
+Review depth. It explicitly does not claim comparator parity or production
+improvement without actual paired outputs and Project Lead judgment.
+
+`reader-centered-quality-smoke-test.md` records eight synthetic cases that
+separate reader outcome from readability, preserve evidence guardrails, test
+good and bad cognitive bridges and bounded tradeoffs, reject taste-only review,
+and keep short low-risk text compact. It does not define active rules or replace
+the canonical owners listed in the file.
+
diff --git a/tests/reader-centered-quality-smoke-test.md b/tests/reader-centered-quality-smoke-test.md
new file mode 100644
index 0000000..3517914
--- /dev/null
+++ b/tests/reader-centered-quality-smoke-test.md
@@ -0,0 +1,158 @@
+# Reader-Centered Quality Smoke Test
+
+Purpose: manually verify activation, restraint, evidence guardrails, bounded
+tradeoffs, Reader Review determinism, Companion Pass, and depth calibration.
+These synthetic cases are not task materials, production evidence, or proof of
+real-world improvement.
+
+Canonical owners:
+
+- `/kb/audience_outcome_alignment.md`
+- `/kb/professional_communication.md`
+- `/kb/editorial_quality_attributes.md`
+- `/kb/shared_lifecycle_kernel.md`
+- `/agents/review_agent.md`
+- `/pipelines/review_pipeline.md`
+
+For every case record activation, depth, finding, evidence pointer, outcome,
+repair owner/scope when needed, and which non-relaxable guardrails remain.
+
+## Case 1 — Correct But Academically Useless
+
+Input: a source-backed article for an experienced practitioner defines twelve
+current concepts accurately, but never connects them to the reader's recorded
+old workflow, provides no supported example, and ends without an action.
+
+Expected:
+
+- Reader Review: material, `full`;
+- Cognitive Bridge: `fail`;
+- Application: `fail`;
+- Reader burden: `fail` only with exact dense passages and the blocked outcome;
+- Companion Pass: `fail` for avoidable academic distance;
+- outcome: `changes_requested`;
+- repair: Writer Agent adds the approved bridge, example, and action without
+  changing claims or source boundaries; re-review is bounded to those changes
+  plus affected traceability.
+
+## Case 2 — Pleasant But Unsupported
+
+Input: a lively short answer says a product is safer, faster, and easier than
+alternatives without supplied evidence. The selection advice is memorable.
+
+Expected:
+
+- Reader Review and Companion Pass cannot compensate for unsupported claims;
+- factual/evidence gate: `fail`;
+- outcome: `changes_requested` or `blocked` according to evidence availability;
+- repair: remove or research the claims through the existing owner;
+- forbidden result: `approved` because the answer is easy to read.
+
+## Case 3 — Usable Cognitive Bridge
+
+Input: the brief records “reader still treats a prompt as the whole control
+surface.” The artifact says that prompt quality still matters, then shows how
+contract, selected context, tools, permissions, and verification now surround
+it, with one source-backed before/after example and a tomorrow-morning action.
+
+Expected:
+
+- Cognitive Bridge: `pass`;
+- Understanding, retention, and application: `pass` when exact sections support
+  them;
+- Learning sequence may differ from five literal headings;
+- evidence and Companion Pass remain independently checked;
+- outcome may be `approved` if all other gates pass.
+
+## Case 4 — Feature Dump Instead Of Bridge
+
+Input: a reader names an old product/version stopping point. The response lists
+twenty current features by provider but never explains which working model
+changed, which features matter to the reader's tasks, or what to do.
+
+Expected:
+
+- Reader fit, Cognitive Bridge, retention, and application: `fail`;
+- more features are not a valid repair by themselves;
+- vendor neutrality and freshness are reviewed separately;
+- bounded repair selects only evidenced examples that serve the recorded
+  transition.
+
+## Case 5 — Justified Bounded Utility Tradeoff
+
+Input: a reader explicitly asks what changed since a named dated practice. Chief
+Editor records a six-item chronology limited to verified provider sources as of
+a named date, marks availability limits, states that durability is relaxed, and
+keeps correctness, evidence, neutrality, traceability, caveats, and review.
+
+Expected:
+
+- Bounded Utility Tradeoff: `pass` if the chronology materially improves the
+  bridge;
+- stale-if trigger is present;
+- product specificity does not become promotion or exhaustive catalog;
+- full Reader Review challenges claimed reader benefit as well as guardrails.
+
+## Case 6 — Unjustified Bounded Utility Tradeoff
+
+Input: Chief Editor says “current products are more engaging” and permits a
+feature catalog with no date, evidence boundary, scope, relaxed attribute, or
+stale-if trigger.
+
+Expected:
+
+- Bounded Utility Tradeoff: `fail`;
+- correctness and neutrality cannot be declared relaxable;
+- outcome: `changes_requested` or `blocked`;
+- repair owner: Chief Editor for route/contract, Research Agent for missing
+  evidence only if the route remains justified.
+
+## Case 7 — Reader Review As Taste
+
+Input: Reviewer writes “I prefer shorter sentences and a warmer opening” but
+cannot connect either preference to the Reader Outcome Contract, a criterion,
+or an exact blocked passage.
+
+Expected:
+
+- finding is rejected as preference-only;
+- Reviewer may record a non-blocking suggestion only if task conventions allow;
+- no rewrite, new persona, or fake empathy is required;
+- another valid route is not a blocker when the approved route works.
+
+## Case 8 — Short Text With Full Learning Design Not Applicable
+
+Input: answer in at most 50 words whether to use a fixed workflow or an agent,
+using two supplied definitions and one practical selection rule.
+
+Expected:
+
+- Reader Review depth: `compact`;
+- checks: main transfer understood, intended action possible, no avoidable
+  burden/artificial tone;
+- full Cognitive Bridge/Moments/Learning Design table: `not applicable`;
+- evidence and independent review still apply;
+- no new role, stage, gate, or standalone reader artifact appears.
+
+## Architecture Restraint Checks
+
+All cases must preserve these invariants:
+
+- no Reader Model Agent, Learning Designer, Companion Agent, or separate reader
+  testing role;
+- no `reader-model.md`, `learning-design.md`, `reader-review.md`, or
+  `companion-pass.md` requirement;
+- Reader Review and Companion Pass remain inside the existing review gate and
+  `review.md`;
+- depth changes evidence volume, not the existence of review;
+- synthetic results do not update canon, backlog, roles, or promotion status
+  automatically.
+
+## Pass Condition
+
+The smoke test passes only when cases 1-8 produce the expected distinctions:
+reader value is not mere readability, pleasant unsupported copy fails evidence,
+good bridges are reviewable, feature dumps do not substitute for transitions,
+utility tradeoffs remain bounded, taste does not become a blocker, and compact
+tasks remain compact. Existing lifecycle and task-pack automated smoke tests
+must also pass.
~~~~

## ROQ-P2-01 record runtime topology

Commit slice: `752ee3f`

Изменённые файлы:

- `agents/chief_editor.md`
- `kb/shared_lifecycle_kernel.md`
- `kb/task_object_model.md`
- `scripts/generate_task_pack.py`
- `templates/artifacts/orchestration_plan_template.md`
- `templates/artifacts/task_manifest_template.md`
- `tests/fixtures/task_pack/runtime_execution_record/draft.md`
- `tests/fixtures/task_pack/runtime_execution_record/orchestration_plan.md`
- `tests/fixtures/task_pack/runtime_execution_record/status.md`
- `tests/fixtures/task_pack/runtime_execution_record/task-manifest.md`
- `tests/test_task_pack_generator.sh`

~~~~diff
diff --git a/agents/chief_editor.md b/agents/chief_editor.md
index b032151..1d31a42 100644
--- a/agents/chief_editor.md
+++ b/agents/chief_editor.md
@@ -92,0 +93,3 @@ signals and advisory recommendations are owned by
+- keep planned and actual runtime topology distinct when multiple material
+  subagent streams are used; use task-local IDs, record file-less package
+  contributions, and leave unavailable model/mode metadata unknown;
@@ -329,0 +333,3 @@ Required when applicable:
+- planned runtime topology in `orchestration_plan.md` and actual execution in
+  `task-manifest.md` when multiple material runtime streams are used; never as
+  a new standalone artifact.
@@ -414,0 +421,2 @@ The Chief Editor may decide:
+- material runtime stream boundaries, stable task-local IDs, and coordination
+  relations when actual execution uses multiple streams;
@@ -473,0 +482,2 @@ The Chief Editor must not decide:
+- hidden runtime metadata, unavailable model/mode values, or session details
+  that are not needed for task traceability.
@@ -498,0 +509,2 @@ Do not repeat the full Editorial Decision Frame. It should not use
+When a material runtime stream starts or completes, the handoff should update
+the actual execution row or provide the delta needed for Chief Editor to do so.
@@ -510,0 +523,3 @@ Do not repeat the full Editorial Decision Frame. It should not use
+- planned and actual runtime records, when material, use task-local IDs, show
+  artifacts or inter-agent packages and responsibility boundaries, contain no
+  guessed metadata, and avoid secrets or unrelated session data;
diff --git a/kb/shared_lifecycle_kernel.md b/kb/shared_lifecycle_kernel.md
index 84d63a2..64e62f4 100644
--- a/kb/shared_lifecycle_kernel.md
+++ b/kb/shared_lifecycle_kernel.md
@@ -147,0 +148,23 @@ standalone reader artifact.
+### Runtime Execution Record
+
+When one task uses multiple material subagent sessions or parallel streams,
+keep a compact best-effort record in existing artifacts:
+
+- `orchestration_plan.md` records planned topology;
+- `task-manifest.md` records actual execution;
+- handoffs update the actual record when a material stream starts, transfers a
+  package or artifact, changes boundary, or completes.
+
+Use stable task-local IDs such as `research-platforms-01`, not runtime
+nicknames. Record canonical role/function, purpose and scope, parent or
+coordination relation, model/mode only when available, input boundary,
+artifacts or inter-agent packages produced, responsibility boundary, and
+status. A stream with no direct file write is still material when its package
+changes downstream evidence or decisions.
+
+Do not guess missing metadata; use `unknown` or `not recorded`. Do not copy
+session IDs, hidden prompts, credentials, personal data, filesystem-wide
+metadata, or unrelated runtime logs. This record is traceability context, not a
+new role, gate, required standalone artifact, runtime controller, or dependency
+on a specific Codex nickname scheme.
+
diff --git a/kb/task_object_model.md b/kb/task_object_model.md
index 3d4d910..1f7df95 100644
--- a/kb/task_object_model.md
+++ b/kb/task_object_model.md
@@ -122,0 +123,2 @@ file.
+| `planned_runtime_topology` | Optional best-effort plan for material runtime streams using stable task-local IDs, canonical role/function, scope, coordination relation, model/mode when known, input/output boundaries, and responsibility boundary. | `orchestration_plan.md` |
+| `actual_runtime_execution` | Optional best-effort record of material runtime streams actually used, including streams that transferred an inter-agent package without writing a file. Unknown runtime metadata stays unknown. | `task-manifest.md`, handoffs |
@@ -150 +152 @@ requires it.
-| `task-manifest.md` | Compact current-state view: task id, selected workflow, active capabilities/roles, active Domain Knowledge Packs when material, current owner/status, artifact inventory, current pointer, constraints, gates, review/finalization state, and next action. |
+| `task-manifest.md` | Compact current-state view: task id, selected workflow, active capabilities/roles, active Domain Knowledge Packs when material, actual runtime execution when material and known, current owner/status, artifact inventory, current pointer, constraints, gates, review/finalization state, and next action. |
@@ -152 +154 @@ requires it.
-| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, gates, artifact scope, Editorial Decision Frame with Cognitive Bridge, Moments of Insight, and Practical Transformation when material, evidence basis/confidence for material route decisions, and expansion triggers. |
+| `orchestration_plan.md` | Execution contract: selected pipeline or mini-contract, risk mode, process depth, planning level, optional Task Need Recognition view and Chief Editor decision when material, analytical question and assumptions when material, architecture review scope and drivers when material, audience/outcome fit and Reader Outcome Contract when material, quality priorities/guardrails/tradeoffs when material, options considered when material, active capabilities, active Domain Knowledge Packs when material, active roles, planned runtime topology when material, gates, artifact scope, Editorial Decision Frame with Cognitive Bridge, Moments of Insight, and Practical Transformation when material, evidence basis/confidence for material route decisions, and expansion triggers. |
diff --git a/scripts/generate_task_pack.py b/scripts/generate_task_pack.py
index 0fbc091..ce7f6ce 100644
--- a/scripts/generate_task_pack.py
+++ b/scripts/generate_task_pack.py
@@ -50,0 +51,2 @@ READER_OUTCOME_RE = re.compile(
+PLANNED_RUNTIME_RE = re.compile(r"(?im)^\s*##\s+planned runtime topology\s*$")
+ACTUAL_RUNTIME_RE = re.compile(r"(?im)^\s*##\s+actual runtime execution\s*$")
@@ -300,0 +303,19 @@ def generate_pack(task_dir: Path, role: str) -> tuple[dict[str, list[ReadItem]],
+    if ACTUAL_RUNTIME_RE.search(manifest_text):
+        add_item(
+            sections,
+            seen,
+            "Required",
+            manifest_path,
+            task_dir,
+            "actual runtime execution record and material stream contributions",
+        )
+    if PLANNED_RUNTIME_RE.search(orchestration_text):
+        add_item(
+            sections,
+            seen,
+            "Required",
+            orchestration_path,
+            task_dir,
+            "planned runtime topology and stream responsibility boundaries",
+        )
+
diff --git a/templates/artifacts/orchestration_plan_template.md b/templates/artifacts/orchestration_plan_template.md
index 8b59f44..0763af1 100644
--- a/templates/artifacts/orchestration_plan_template.md
+++ b/templates/artifacts/orchestration_plan_template.md
@@ -170,0 +171,9 @@ weaken review, governance, role boundaries, or required fields.
+## planned runtime topology
+
+Use only when multiple material runtime streams are planned. Use stable
+task-local IDs; do not use random nicknames as process identifiers. Model/mode
+may be `unknown` or `not recorded`.
+
+| Stream ID | Canonical role/function | Purpose and scope | Parent/coordination | Model/mode if known | Input boundary | Expected artifact/package | Responsibility boundary |
+| --- | --- | --- | --- | --- | --- | --- | --- |
+
diff --git a/templates/artifacts/task_manifest_template.md b/templates/artifacts/task_manifest_template.md
index 712c861..f4dea8c 100644
--- a/templates/artifacts/task_manifest_template.md
+++ b/templates/artifacts/task_manifest_template.md
@@ -98,0 +99,11 @@ Required when a task has multiple versions.
+## actual runtime execution
+
+Use only when multiple material runtime streams were actually used. Keep it
+best-effort and current. Include inter-agent packages even when a stream did not
+write a file. Use `unknown` or `not recorded` instead of guessing. Do not store
+session IDs, hidden prompts, credentials, personal data, or unrelated runtime
+metadata. A random runtime nickname may appear only as an optional note.
+
+| Task-local ID | Canonical role/function | Purpose and scope | Parent/relation | Model/mode | Input boundary | Artifacts or packages | Responsibility/status |
+| --- | --- | --- | --- | --- | --- | --- | --- |
+
diff --git a/tests/fixtures/task_pack/runtime_execution_record/draft.md b/tests/fixtures/task_pack/runtime_execution_record/draft.md
new file mode 100644
index 0000000..123b9ca
--- /dev/null
+++ b/tests/fixtures/task_pack/runtime_execution_record/draft.md
@@ -0,0 +1,3 @@
+# Draft
+
+Synthetic draft for runtime execution record fixture.
diff --git a/tests/fixtures/task_pack/runtime_execution_record/orchestration_plan.md b/tests/fixtures/task_pack/runtime_execution_record/orchestration_plan.md
new file mode 100644
index 0000000..3102988
--- /dev/null
+++ b/tests/fixtures/task_pack/runtime_execution_record/orchestration_plan.md
@@ -0,0 +1,10 @@
+# Orchestration Plan
+
+Pipeline: article
+Risk mode: standard
+
+## planned runtime topology
+
+| Stream ID | Canonical role/function | Purpose and scope | Parent/coordination | Model/mode if known | Input boundary | Expected artifact/package | Responsibility boundary |
+| --- | --- | --- | --- | --- | --- | --- | --- |
+| `research-platforms-01` | Research / platform evidence | Verify platform facts | `research-primary-01` | unknown | brief and provider sources | evidence package | no synthesis or writing |
diff --git a/tests/fixtures/task_pack/runtime_execution_record/status.md b/tests/fixtures/task_pack/runtime_execution_record/status.md
new file mode 100644
index 0000000..176e552
--- /dev/null
+++ b/tests/fixtures/task_pack/runtime_execution_record/status.md
@@ -0,0 +1,5 @@
+# Status
+
+Current status: writing
+Previous status: planning
+Responsible role: writer
diff --git a/tests/fixtures/task_pack/runtime_execution_record/task-manifest.md b/tests/fixtures/task_pack/runtime_execution_record/task-manifest.md
new file mode 100644
index 0000000..3894098
--- /dev/null
+++ b/tests/fixtures/task_pack/runtime_execution_record/task-manifest.md
@@ -0,0 +1,15 @@
+# Task Manifest
+
+Task ID: SYNTHETIC-PACK-RUNTIME
+Current status: writing
+Selected pipeline: article
+Client profile: none
+Current artifact: draft.md
+
+## actual runtime execution
+
+| Task-local ID | Canonical role/function | Purpose and scope | Parent/relation | Model/mode | Input boundary | Artifacts or packages | Responsibility/status |
+| --- | --- | --- | --- | --- | --- | --- | --- |
+| `research-platforms-01` | Research / platform evidence | Verified platform facts | `research-primary-01` | not recorded | brief and provider sources | inter-agent evidence package | complete; no synthesis or writing |
+
+Next required action: continue synthetic draft.
diff --git a/tests/test_task_pack_generator.sh b/tests/test_task_pack_generator.sh
index 2208c27..b6b0895 100644
--- a/tests/test_task_pack_generator.sh
+++ b/tests/test_task_pack_generator.sh
@@ -85,0 +86 @@ run_case_absent "writer_minimal" "writer" 0 "audience_outcome_alignment.md" "pro
+run_case "runtime_execution_record" "writer" 0 "planned runtime topology" "actual runtime execution record"
~~~~

## ROQ-P2-02 govern evidence-based evolution

Commit slice: `2817d3d`

Изменённые файлы:

- `kb/capability_registry.md`
- `kb/editorial_learning_framework.md`
- `kb/feedback_patterns.md`
- `tests/reader-centered-quality-smoke-test.md`

~~~~diff
diff --git a/kb/capability_registry.md b/kb/capability_registry.md
index ee0a9f8..8d264c8 100644
--- a/kb/capability_registry.md
+++ b/kb/capability_registry.md
@@ -88 +88,5 @@ The following are not current default roles:
-- Memory Manager.
+- Memory Manager;
+- Reader Model Agent;
+- Learning Designer;
+- Reader Reviewer;
+- Companion Agent.
@@ -112,0 +117,4 @@ Audience and outcome alignment is a shared capability, not a standing role.
+Reader Model is a function of Audience and Outcome Alignment; Learning Design
+and Companion Pass are functions of Professional Communication; Reader Review
+is a Review Agent lens. None is a standing role, pipeline, stage, gate, score,
+or standalone artifact.
@@ -939,0 +948,4 @@ are context packages, not reusable operations.
+- Reader Model;
+- Learning Design;
+- Reader Review;
+- Companion Pass;
diff --git a/kb/editorial_learning_framework.md b/kb/editorial_learning_framework.md
index 61648d0..38ee7ca 100644
--- a/kb/editorial_learning_framework.md
+++ b/kb/editorial_learning_framework.md
@@ -163,0 +164,49 @@ review. If the check is weak, keep the signal local, reject it, or defer it.
+## Reader-Centered Outcome Evolution
+
+Reader-centered changes are evaluated through the same feedback, Evaluation
+Signal, pattern, and Knowledge Evolution mechanisms. When material, preserve:
+
+- task type and Reader Outcome Contract;
+- actual final-output evidence, not only completed template fields;
+- correctness, evidence support, neutrality, traceability, reader fit, clarity,
+  concreteness, model change, retention, practical action, naturalness, and
+  governance cost;
+- baseline or comparator conditions when a comparison is claimed;
+- positive, negative, mixed, missing, and contradictory results;
+- which existing role, decision frame, review lens, or template change was
+  actually used;
+- alternative explanations such as stronger sources, more time, longer output,
+  different model/mode, or extra agents;
+- explicit non-promotion and the next human decision.
+
+Outcome feedback is distinct from taste. “I liked the tone” is a preference
+unless evidence shows a material effect on understanding, decision, action, or
+the recorded failure signal. Activity counts, filled fields, number of agents,
+longer outputs, and review volume do not prove reader value.
+
+### Threshold For A New Permanent Role
+
+Reader Model, Learning Design, Reader Review, and Companion Pass remain shared
+functions of existing roles. A new permanent role may be considered only when
+all of these conditions are evidenced:
+
+1. comparable failures recur across materially different task types or
+   contexts, with positive, negative, and contradictory cases preserved;
+2. existing owners have been given bounded, reviewed changes and still cannot
+   resolve the failure reliably;
+3. the remaining problem is an accountability or independence conflict, not
+   missing instructions, weak evidence, poor routing, or a template gap;
+4. a separate role has a testable benefit above its context, coordination,
+   handoff, latency, maintenance, and governance cost;
+5. scope, non-applicability, authority, inputs, outputs, stop conditions, and
+   interaction with current roles can be defined without duplicating an owner;
+6. an existing Evaluation Signal and Knowledge Evolution disposition support a
+   separate reviewed system update and Project Lead decision.
+
+No numeric count or threshold creates the role automatically. Failure to meet
+the threshold means `no role change`, which is a normal successful outcome when
+existing roles perform the functions adequately. The same evidence may still
+justify a smaller owner patch, calibration, deferral, rejection, or no action.
+`ideas/master_backlog.md`, role specifications, pipelines, and canon do not
+change merely because a reader-centered candidate exists.
+
diff --git a/kb/feedback_patterns.md b/kb/feedback_patterns.md
index ce80790..7fbcaee 100644
--- a/kb/feedback_patterns.md
+++ b/kb/feedback_patterns.md
@@ -45,0 +46,5 @@ task_local / preference -> observation -> confirmed_pattern -> system_change_can
+- Reader-outcome criterion, when material: reader fit / clarity / concreteness / model change / retention / practical action / naturalness / governance cost
+- Comparator or baseline and shared conditions, when a comparison is claimed:
+- Evidence that this is outcome feedback rather than taste or readability alone:
+- Existing-role response already tried and observed effect:
+- Ownership conflict, if any:
@@ -55,0 +61,6 @@ No validated patterns yet.
+
+Reader-centered signals use this same journal only when comparable evidence is
+worth tracking across tasks. Preserve positive, negative, mixed, and
+contradictory outcomes. A pleasant style preference is not reader-outcome
+evidence unless it can be tied to an intended understanding, decision, action,
+or failure signal. Do not create a separate reader-feedback registry.
diff --git a/tests/reader-centered-quality-smoke-test.md b/tests/reader-centered-quality-smoke-test.md
index 3517914..167580d 100644
--- a/tests/reader-centered-quality-smoke-test.md
+++ b/tests/reader-centered-quality-smoke-test.md
@@ -150,0 +151,17 @@ All cases must preserve these invariants:
+## Evolution Restraint Cases
+
+### One Positive Pilot
+
+A longread improves after adding a Cognitive Bridge, while working-document and
+short-text evidence is missing. Expected disposition: `learning_candidate` or
+`deferred`; no permanent role, master backlog change, or canon claim.
+
+### Repeated Cross-Task Failure
+
+Several comparable task types fail Reader Review after bounded changes to
+existing owners. Evidence identifies a genuine accountability/independence
+conflict and estimates coordination cost. Expected disposition: at most
+`canon_update_candidate` for a separate reviewed system update and Project Lead
+decision. No count or Evaluation Signal creates the role automatically; a
+smaller owner patch, rejection, deferral, or `no role change` remains valid.
+
~~~~

## Closeout — Document reader quality implementation status

Commit slice: `6dc9bc7`

Изменённые файлы:

- `ideas/reader-centered-quality-backlog.md`
- `ideas/reader-centered-quality-implementation-report.md`

~~~~diff
diff --git a/ideas/reader-centered-quality-backlog.md b/ideas/reader-centered-quality-backlog.md
index 5dd592e..9ffa656 100644
--- a/ideas/reader-centered-quality-backlog.md
+++ b/ideas/reader-centered-quality-backlog.md
@@ -3 +3 @@
-Статус документа: `proposal / not active canon`
+Статус документа: `implementation complete / comparative promotion pending`
@@ -9 +9,24 @@
-Этот документ — отдельный proposal-backlog в `ideas/`. Он не заменяет активный `ideas/master_backlog.md`, не меняет `ROADMAP.md` или `BACKLOG.md`, не вводит production-правила и не считается принятым системным обновлением без отдельного review и решения Project Lead.
+Этот документ — отдельный backlog и execution ledger в `ideas/`. Он не
+заменяет активный `ideas/master_backlog.md`, `ROADMAP.md` или `BACKLOG.md`.
+Описанные изменения реализованы в существующих canonical owners, ролях,
+pipelines, templates и tests последовательными bounded slices. При этом
+заявление о достигнутом паритете с сильным одиночным ChatGPT остаётся
+неподтверждённым до фактических comparative runs и решения Project Lead.
+
+## Статус реализации
+
+| ID | Статус | Краткий результат |
+| --- | --- | --- |
+| `ROQ-P0-01` | implemented | Reader Outcome Contract и неослабляемые quality/evidence guardrails закреплены в существующем каноне. |
+| `ROQ-P0-02` | implemented | Chief Editor проектирует reader journey и обосновывает выбранный порядок через исходное состояние и требуемое изменение. |
+| `ROQ-P0-03` | implemented | Cognitive Bridge, 3-5 Moments of Insight и Practical Transformation встроены в Editorial Decision Frame. |
+| `ROQ-P0-04` | implemented | Reader Model и Learning Design распределены между существующими ролями; новых ролей нет. |
+| `ROQ-P0-05` | implemented | Детерминированный Reader Review встроен в `review.md` и существующий review gate. |
+| `ROQ-P0-06` | implemented | Companion Pass выполняется до approval; substantive repair остаётся у Writer Agent. |
+| `ROQ-P0-07` | implemented | Chief Editor может принять только явный, ограниченный и reviewable Bounded Utility Tradeoff. |
+| `ROQ-P1-01` | implemented and automated | Material reader context передаётся Writer/Review task packs без новых task artifacts; fixture и smoke test добавлены. |
+| `ROQ-P1-02` | calibrated; external comparison pending | Реальный longread baseline и два synthetic cases зафиксированы; promotion gate честно оставлен `not yet proven`. |
+| `ROQ-P1-03` | implemented from calibration evidence | Определены `compact`, `normal`, `full` depth и bounded re-review. |
+| `ROQ-P1-04` | implemented | Добавлены восемь anti-regression cases и architecture-restraint checks. |
+| `ROQ-P2-01` | implemented and automated | Planned/actual runtime topology живёт в plan/manifest; task-pack fixture проверяет передачу record. |
+| `ROQ-P2-02` | implemented | Feedback/Learning Framework хранит outcome evidence и задаёт высокий evidence threshold для новой постоянной роли. |
diff --git a/ideas/reader-centered-quality-implementation-report.md b/ideas/reader-centered-quality-implementation-report.md
new file mode 100644
index 0000000..1bf1fc8
--- /dev/null
+++ b/ideas/reader-centered-quality-implementation-report.md
@@ -0,0 +1,97 @@
+# Reader-Centered Quality Implementation Report
+
+Дата: 2026-07-13
+
+Статус: `implementation complete / comparative promotion pending`
+
+## Итог
+
+`reader-centered-quality-backlog.md` отработан последовательно от `ROQ-P0-01`
+до `ROQ-P2-02`. Reader-centered quality встроено в существующую архитектуру AI
+Editorial Office: Chief Editor проектирует переход читателя; Writer реализует
+его; Review Agent проверяет outcome и живость объяснения; Final Editor сохраняет
+одобренный баланс. Новых постоянных ролей, lifecycle stages, review gates или
+обязательных reader-specific task files не создано.
+
+Корректность, evidence support, нейтральность, трассируемость, неопределённость,
+source boundary и независимый review сохранены как неослабляемые ограничения.
+
+## Выполнение по задачам
+
+| Задача | Выполнено | Основные файлы |
+| --- | --- | --- |
+| `ROQ-P0-01` | Добавлены Reader Outcome Contract, reader-outcome quality attribute и non-relaxable guardrails. | `AGENTS.md`, `kb/audience_outcome_alignment.md`, `kb/editorial_quality_attributes.md`, `kb/task_object_model.md` |
+| `ROQ-P0-02` | Reader journey стал обязанностью Chief Editor и evaluation dimension planning. | `agents/chief_editor.md`, `kb/editorial_planning_framework.md`, `kb/capability_registry.md`, orchestration template |
+| `ROQ-P0-03` | В Editorial Decision Frame добавлены Cognitive Bridge, 3-5 Moments of Insight и Practical Transformation. | `AGENTS.md`, Chief/Writer specs, task model, article/orchestration templates |
+| `ROQ-P0-04` | Reader Model распределён по Intake/Chief/Writer/Review/Final; Learning Design закреплён как условный pattern. | audience/communication KB, Intake/Chief/Writer, capability registry, article pipeline |
+| `ROQ-P0-05` | Reader Review получил воспроизводимые критерии и bounded repair routing внутри `review.md`. | Review Agent/Pipeline, review template, canonical references |
+| `ROQ-P0-06` | Companion Pass проверяет naturalness, concreteness, distance и precision до approval. | communication KB, Review Agent/Pipeline, Final Editor, review template |
+| `ROQ-P0-07` | Локальная хронология или product bridge разрешены только как явный Bounded Utility Tradeoff. | quality/planning KB, Chief/Review, orchestration template |
+| `ROQ-P1-01` | Material reader fields протянуты в templates и Writer/Review task packs; compact tasks не получают KB context автоматически. | manifest/social templates, generator, fixture, generator test |
+| `ROQ-P1-02` | Проведена трёхтиповая calibration: реальный longread baseline, synthetic working document и short text. | `tests/reader-centered-quality-pilot.md` |
+| `ROQ-P1-03` | Определены `compact`, `normal`, `full`; re-review ограничен изменённым или инвалидированным scope. | lifecycle kernel, Article/Social/Review pipelines, Review Agent/template |
+| `ROQ-P1-04` | Добавлены regression cases для academic-but-useless, pleasant-but-unsupported, bridge, feature dump, tradeoff, taste и short N/A. | tests README и reader-centered smoke test |
+| `ROQ-P2-01` | Planned topology отделена от actual execution; file-less subagent packages видимы; nicknames необязательны. | task model/lifecycle, Chief, plan/manifest templates, generator fixture/test |
+| `ROQ-P2-02` | Outcome feedback отделён от вкуса; новая роль требует repeated evidence, ownership conflict и отдельного reviewed update. | feedback patterns, learning framework, capability registry, regression test |
+
+## Архитектурные ограничения, которые сохранены
+
+- Reader Model, Learning Design, Reader Review и Companion Pass остаются
+  функциями существующих ролей.
+- Reader Review и Companion Pass находятся внутри существующего `review.md`.
+- Не созданы `reader-model.md`, `learning-design.md`, `reader-review.md`,
+  `companion-pass.md` или отдельный runtime record file.
+- Reader Review depth меняет объём evidence, а не обязательность review.
+- Bounded Utility Tradeoff не может ослабить correctness, evidence, neutrality,
+  required traceability, caveats, source boundaries или review independence.
+- Runtime record использует стабильные task-local IDs и не сохраняет secrets,
+  session IDs, hidden prompts или лишние персональные/runtime metadata.
+- `ideas/master_backlog.md`, `ROADMAP.md`, `BACKLOG.md` и `/about` не менялись.
+
+## Проверка и evidence
+
+Добавлены два автоматизированных task-pack cases:
+
+- `reader_outcome_material` проверяет material-only загрузку audience,
+  communication и quality KB для Writer и Review Agent;
+- `runtime_execution_record` проверяет, что planned и actual topology остаются
+  в обязательном task-pack read set.
+
+Добавлены manual/synthetic evidence:
+
+- трёхтиповый calibration pilot;
+- восемь reader-outcome anti-regression cases;
+- два evolution-restraint cases.
+
+Проверки выполнения:
+
+- `git diff --check` — pass;
+- `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` — pass, 14/14 cases;
+- `sh ai-editorial-office/tests/test_task_pack_generator.sh` — pass, 13/13 cases.
+
+## Ограничение результата
+
+Implementation готова, но общий Definition of Done инициативы ещё не доказан.
+В репозитории нет сохранённого сильного одиночного comparator для всех трёх
+типов задач; working-document и short-text cases являются synthetic calibration,
+а longread не был заново произведён по обновлённому контракту. Поэтому
+promotion status остаётся `not yet proven`, пока Project Lead не сравнит
+фактические paired outputs при одинаковых brief, source set, date, model/mode и
+tools.
+
+Это ограничение не блокирует использование реализованной логики, но блокирует
+утверждение «Редакция уже не хуже comparator по всем параметрам».
+
+## Изменённая поверхность
+
+До closeout-артефактов implementation затронула 37 файлов: canonical
+governance, 5 role specs, 9 KB owners, 3 pipelines, 3 templates groups,
+task-pack generator и tests/fixtures. Полный patch сохранён отдельно в
+`ideas/reader-centered-quality-implementation-diff.md` и разделён по backlog ID.
+
+## Рекомендуемый следующий шаг
+
+Провести один реальный повторный longread run и по одному реальному working
+document/short-text run. Сохранить comparator outputs, скрыть labels при оценке,
+получить Project Lead judgment по каждому material criterion и только затем
+решать: подтвердить, сузить, откалибровать или частично откатить линзы.
~~~~

## Closeout — Report exact-copy memory synchronization

Commit slice: `355d5f7`

Изменённые файлы:

- `ideas/reader-centered-quality-implementation-report.md`

~~~~diff
diff --git a/ideas/reader-centered-quality-implementation-report.md b/ideas/reader-centered-quality-implementation-report.md
index 1bf1fc8..4ae9b72 100644
--- a/ideas/reader-centered-quality-implementation-report.md
+++ b/ideas/reader-centered-quality-implementation-report.md
@@ -49 +49,7 @@ source boundary и независимый review сохранены как не
-- `ideas/master_backlog.md`, `ROADMAP.md`, `BACKLOG.md` и `/about` не менялись.
+- `ideas/master_backlog.md`, `ROADMAP.md` и `BACKLOG.md` не менялись.
+
+После canonical implementation девять изменённых files, которые входят в
+exact-copy `/about` memory package, синхронизированы механически. Это не
+самостоятельное изменение правил: `/about` остаётся неканоническим зеркалом,
+проверяемым `check_about_memory_package.sh`. `ideas/master_backlog.md`,
+`ROADMAP.md` и `BACKLOG.md` не менялись.
@@ -70,0 +77,2 @@ source boundary и независимый review сохранены как не
+- `sh ai-editorial-office/scripts/check_about_memory_package.sh` — pass после
+  exact-copy sync, 20/20 package files present and mapped copies current.
@@ -90,0 +99,2 @@ task-pack generator и tests/fixtures. Полный patch сохранён от
+Итоговая repository surface — 49 файлов: 40 implementation/report/diff files
+в `ai-editorial-office` и 9 механических exact copies в `/about`.
~~~~

## Closeout — exact-copy /about memory synchronization

Эти изменения повторяют уже показанные canonical diffs и нужны только для обязательного non-canonical memory mirror.

Изменённые файлы:

- `about/AGENTS.md`
- `about/chief_editor.md`
- `about/final_editor.md`
- `about/intake_agent.md`
- `about/review_agent.md`
- `about/writer_agent.md`
- `about/article_pipeline.md`
- `about/review_pipeline.md`
- `about/social_pipeline.md`

~~~~diff
--- a/about/AGENTS.md
+++ b/about/AGENTS.md
@@ -55,2 +55,2 @@
-| Audience and outcome alignment | `/kb/audience_outcome_alignment.md` | task-specific audience, intended outcome, reader context, detail/tone/format fit, and usefulness criteria |
-| Editorial quality attributes and tradeoffs | `/kb/editorial_quality_attributes.md` | task-specific quality priorities, accepted tradeoffs, and preservation risks |
+| Audience, outcome, and Reader Outcome Contract | `/kb/audience_outcome_alignment.md` | task-specific audience, intended outcome, reader context, reader starting state, required change, practical result, detail/tone/format fit, and usefulness criteria |
+| Editorial quality attributes, priority, guardrails, and tradeoffs | `/kb/editorial_quality_attributes.md` | task-specific quality priorities, non-relaxable guardrails, accepted tradeoffs, and preservation risks |
@@ -220,0 +221,3 @@
+- define a compact Reader Outcome Contract for material reader-facing work:
+  starting state, required change in understanding or practice, practical
+  result, and failure signal;
@@ -239,2 +242,5 @@
-reroute triggers. It lives inside `orchestration_plan.md`; it is not a new
-pipeline, role, status, `final_decision.md`, or mandatory standalone
+reroute triggers. For teaching, understanding, or other material reader-change
+work, it also records a compact `Cognitive Bridge`, 3-5 `Moments of Insight`,
+and `Practical Transformation`. These fields may be `not applicable` with a
+reason for other tasks. The frame lives inside `orchestration_plan.md`; it is
+not a new pipeline, role, status, `final_decision.md`, or mandatory standalone
@@ -250 +256,2 @@
-enable.
+enable. It also owns the compact Reader Outcome Contract used when the task
+must change what a reader understands, remembers, decides, or does.
@@ -844 +851,3 @@
-   inside the frame.
+   inside the frame. When reader change is material, the frame also includes
+   the Cognitive Bridge, 3-5 formulated Moments of Insight, and Practical
+   Transformation; these are production fields, not new artifacts.
@@ -1209,0 +1219,3 @@
+- ценным для конкретного читателя и заявленного outcome;
+- способным дать требуемое изменение понимания, решения или практики, когда
+  такое изменение является целью задачи;
@@ -1216,0 +1229,2 @@
+Reader value не разрешает ослаблять correctness, evidence support,
+neutrality, traceability, честную неопределённость или независимый review.
@@ -1262,0 +1277,5 @@
+- когда Reader Review материален: понимание, запоминаемость, применимость,
+  Cognitive Bridge, Learning Design sequence и reader burden с явными
+  `pass`/`fail`/`not applicable`/`needs clarification` статусами и ссылками на
+  Reader Outcome Contract или точные места артефакта; вкус сам по себе не
+  является finding;
--- a/about/chief_editor.md
+++ b/about/chief_editor.md
@@ -46,0 +47,2 @@
+- design the reader journey for material reader-facing work: starting state,
+  required change, explanation sequence, and practical result after use;
@@ -48,0 +51,4 @@
+- authorize a Bounded Utility Tradeoff only for a concrete recorded reader need
+  and only with bounded scope, evidence/freshness basis, stale-if trigger,
+  intentionally relaxed attribute, expected benefit, and preserved
+  non-relaxable guardrails;
@@ -60,0 +67,2 @@
+- select the Learning Design lens within Professional Communication when the
+  task must teach, update a mental model, or explain a changed practice;
@@ -78,0 +87,3 @@
+- require the Editorial Decision Frame to include a Cognitive Bridge, 3-5
+  formulated Moments of Insight, and Practical Transformation when teaching,
+  understanding, or another material reader change is the intended outcome;
@@ -81,0 +93,3 @@
+- keep planned and actual runtime topology distinct when multiple material
+  subagent streams are used; use task-local IDs, record file-less package
+  contributions, and leave unavailable model/mode metadata unknown;
@@ -151,0 +166,3 @@
+- reader starting state, required change in understanding or practice,
+  explanation sequence, practical result, and reader-outcome failure signal
+  when the artifact must teach, explain, reorient, or change action;
@@ -153,0 +171,2 @@
+- old or incomplete reader model, required transition, 3-5 retained ideas, and
+  observable post-use action when reader change is material;
@@ -278,0 +298,2 @@
+- compact reader journey inside `orchestration_plan.md` when reader change is
+  material; it must be a production contract, not a second audience framework.
@@ -280,0 +302,3 @@
+- compact Bounded Utility Tradeoff inside the existing Editorial Decision Frame
+  or quality profile when a less durable, product-specific, chronological, or
+  otherwise local bridge materially improves the recorded reader journey.
@@ -282,0 +307,3 @@
+- Cognitive Bridge, 3-5 Moments of Insight, and Practical Transformation inside
+  that frame when teaching, understanding, or another reader change is
+  material; otherwise a compact `not applicable` rationale is allowed.
@@ -305,0 +333,3 @@
+- planned runtime topology in `orchestration_plan.md` and actual execution in
+  `task-manifest.md` when multiple material runtime streams are used; never as
+  a new standalone artifact.
@@ -390,0 +421,2 @@
+- material runtime stream boundaries, stable task-local IDs, and coordination
+  relations when actual execution uses multiple streams;
@@ -395,0 +428,2 @@
+- reader starting state, target understanding or practice, explanation order,
+  and practical result needed to make a reader-facing route useful;
@@ -397,0 +432 @@
+- whether a Bounded Utility Tradeoff is justified and sufficiently bounded;
@@ -407,0 +443,3 @@
+- whether a material teaching/explanation task needs the conditional
+  `раньше -> сейчас -> почему -> пример -> что делать` pattern or a different
+  reader-journey sequence;
@@ -417 +455,2 @@
-  rejected alternatives kept to short route/reason pairs;
+  rejected alternatives kept to short route/reason pairs and the selected
+  route justified by the reader journey rather than subject order alone;
@@ -442,0 +482,2 @@
+- hidden runtime metadata, unavailable model/mode values, or session details
+  that are not needed for task traceability.
@@ -467,0 +509,2 @@
+When a material runtime stream starts or completes, the handoff should update
+the actual execution row or provide the delta needed for Chief Editor to do so.
@@ -479,0 +523,3 @@
+- planned and actual runtime records, when material, use task-local IDs, show
+  artifacts or inter-agent packages and responsibility boundaries, contain no
+  guessed metadata, and avoid secrets or unrelated session data;
@@ -496,0 +543,6 @@
+- material reader-facing work has a compact journey from reader starting state
+  to required understanding, decision, or action, and the selected structure
+  can be explained through that journey;
+- Cognitive Bridge names the old/incomplete model and transition, Moments of
+  Insight are formulated ideas rather than headings, and Practical
+  Transformation is observable when those fields are material;
--- a/about/final_editor.md
+++ b/about/final_editor.md
@@ -51,0 +52,3 @@
+- preserve the approved Companion Pass balance of naturalness, concreteness,
+  distance, and precision; do not perform substantive companion rewriting
+  during finalization;
@@ -127,0 +131,2 @@
+- repair a failed, missing, or `needs clarification` Companion Pass through
+  substantive finalization edits;
@@ -191,0 +197,2 @@
+- Companion Pass is failed, missing when reader-facing, or requires changes to
+  structure, claims, examples, argument, or meaning;
@@ -221,0 +229,2 @@
+- approved Companion Pass balance remains intact and no substantive companion
+  rewrite occurred during finalization;
--- a/about/intake_agent.md
+++ b/about/intake_agent.md
@@ -33,0 +34,3 @@
+- capture or conservatively infer the reader starting state, old/incomplete
+  model, and desired practical change when teaching, understanding, or complex
+  explanation is material; mark uncertainty instead of inventing a persona;
@@ -157,0 +161,7 @@
+
+## reader model, when material
+- starting knowledge or practice:
+- old or incomplete model to update:
+- likely confusion or overload point:
+- desired model or practice after use:
+- status: confirmed / inferred / unknown / assumption
@@ -367,0 +378,2 @@
+- reader starting state is unknown and different plausible states would require
+  materially different teaching or explanation;
@@ -382,0 +395,2 @@
+- material reader starting state and uncertainty are visible without invented
+  demographic or psychological detail;
--- a/about/review_agent.md
+++ b/about/review_agent.md
@@ -69,0 +70,6 @@
+- run the conditional Reader Review Lens when a Reader Outcome Contract,
+  Cognitive Bridge, teaching/understanding outcome, or other material reader
+  change governs the artifact;
+- run Companion Pass for reader-facing material before `approved`, and route
+  substantive communication repair back to Writer Agent rather than using
+  finalization as a rewrite stage;
@@ -76,0 +83,3 @@
+- challenge each Bounded Utility Tradeoff against its concrete reader need,
+  bounded scope, evidence/freshness basis, stale-if trigger, intentionally
+  relaxed attribute, expected benefit, and non-relaxable guardrails;
@@ -114,0 +124,39 @@
+
+## Reader Review Lens
+
+Reader Review is a deterministic lens inside the existing `review.md`. It is
+not a new role, gate, cycle, score, or standalone artifact.
+
+Activate it when the task must teach, explain, update a mental model, change a
+reader practice, or otherwise has a material Reader Outcome Contract. Use the
+depth selected under `/kb/shared_lifecycle_kernel.md`:
+
+- `compact`: record whether the reader can understand the main transfer, take
+  the intended action, and do so without avoidable burden or artificial tone;
+- `normal`: use the applicable criteria below and Companion Pass;
+- `full`: use all criteria below, trace them to Cognitive Bridge, Moments of
+  Insight, Practical Transformation, and Learning Design, and challenge any
+  Bounded Utility Tradeoff.
+
+For each recorded criterion use `pass`, `fail`, `not applicable`, or
+`needs clarification`:
+
+| Criterion | Review question |
+| --- | --- |
+| Understanding | Can the intended reader state the updated model, decision, or main transfer without reconstructing it from scattered sections? |
+| Retention | Are the approved 3-5 Moments of Insight actually expressed as memorable ideas rather than headings or generic summaries? |
+| Application | Can the reader perform the approved Practical Transformation with the detail and boundaries provided? |
+| Cognitive Bridge | Does the artifact connect the recorded old/incomplete model to the new model instead of presenting only the destination? |
+| Learning sequence | When material, does the explanation provide an effective equivalent of `раньше -> сейчас -> почему -> пример -> что делать` without forcing that exact outline? |
+| Reader burden | Do jargon density, academic distance, abstraction, duplication, or overload prevent the intended outcome? |
+
+Every `fail` or `needs clarification` must cite the Reader Outcome Contract,
+brief, Editorial Decision Frame, and/or exact artifact section. State the
+reader consequence, repair owner, bounded repair scope, do-not-change area, and
+re-review scope. A preference such as "I would write this more simply" is not a
+finding unless the reviewer can show which reader outcome it blocks.
+
+Review Agent may expand the selected depth when inspected evidence reveals a
+material reader risk, but must state the trigger. It may not reduce depth below
+the Chief Editor decision silently. Low-risk short text does not receive the
+six-row teaching check merely because it is reader-facing.
@@ -115,0 +164,17 @@
+Reader Review does not test whether prose is merely pleasant or easy. It may
+not weaken factual validation, evidence, neutrality, traceability, caveats,
+uncertainty, source boundaries, or review independence.
+
+## Companion Pass
+
+For reader-facing material, record `pass`, `fail`, `not applicable`, or
+`needs clarification` for naturalness, concreteness, avoidable academic or
+jargon distance, and precision preservation. Use the canonical criteria in
+`/kb/professional_communication.md`.
+
+Companion Pass is part of `review.md`, not a new role, gate, cycle, score, or
+artifact. A failure must identify the exact wording or pattern, the concrete
+reader consequence, and a bounded repair. If repair would change structure,
+claims, examples, argument, or meaning, outcome cannot be `approved` for Final
+Editor cleanup; route it to Writer Agent and re-review the repaired scope.
+
@@ -136,0 +202,2 @@
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and Learning Design notes when Reader Review is material;
@@ -173,0 +241,2 @@
+  Reader Review Lens when applicable,
+  Companion Pass when reader-facing,
@@ -223,0 +293,4 @@
+- fail Reader Review on taste, personal style, generic readability preference,
+  or an imagined persona not supported by task evidence;
+- treat Companion Pass as permission for fake empathy, invented familiarity,
+  sales language, jokes, new claims, or precision loss;
@@ -230,0 +304,2 @@
+- approve a Bounded Utility Tradeoff that is implicit, unbounded, stale,
+  promotional, unsupported, or relaxes a non-relaxable guardrail;
@@ -292,0 +368,7 @@
+- whether Reader Review is `pass`, `fail`, `not applicable`, or
+  `needs clarification` for each material criterion;
+- whether selected Reader Review depth fits intended outcome, reader risk, and
+  explanation complexity, and whether any expansion has a recorded trigger;
+- whether Companion Pass is `pass`, `fail`, `not applicable`, or
+  `needs clarification` for each material criterion and whether repair is
+  substantive enough to require Writer Agent;
@@ -294,0 +377,2 @@
+- whether each Bounded Utility Tradeoff is explicit, limited, evidence-backed,
+  fresh enough, useful to the recorded reader, and guardrail-safe;
@@ -346,0 +431,2 @@
+- the Reader Outcome Contract or reader starting state is missing or ambiguous
+  enough that a material teaching/explanation outcome cannot be reviewed;
@@ -403,0 +490,3 @@
+- Reader Review is completed when material: understanding, retention,
+  application, Cognitive Bridge, Learning Design sequence, and reader burden
+  have deterministic statuses and evidence-backed bounded repairs;
@@ -456,0 +546,3 @@
+- reader-outcome re-review is limited to the changed scope when independence,
+  evidence checks, and all unaffected findings remain current; otherwise
+  re-review expands only to the invalidated checks;
--- a/about/writer_agent.md
+++ b/about/writer_agent.md
@@ -35,0 +36,3 @@
+- realize the approved Cognitive Bridge, Moments of Insight, and Practical
+  Transformation when those fields are material, without inventing a reader
+  model or changing the approved route;
@@ -50,0 +54,3 @@
+- apply the conditional Learning Design sequence `раньше -> сейчас -> почему ->
+  пример -> что делать` when approved and useful, adapting it rather than
+  forcing a five-part outline;
@@ -94,0 +101,2 @@
+- Cognitive Bridge, Moments of Insight, and Practical Transformation from the
+  Editorial Decision Frame when reader change is material;
@@ -126,0 +135 @@
+- use an unsupported example to make a learning transition feel concrete;
@@ -140,0 +150,2 @@
+- turn Moments of Insight into generic section labels, omit a material
+  Cognitive Bridge, or replace Practical Transformation with a vague promise;
@@ -211,0 +223,2 @@
+- material Cognitive Bridge is visible in the reading path, the 3-5 Moments of
+  Insight are actually expressed, and Practical Transformation is actionable;
@@ -226,0 +240,3 @@
+- teaching/explanation uses the approved reader transition and supported
+  examples without becoming formulaic or overexplaining what the reader already
+  knows;
--- a/about/article_pipeline.md
+++ b/about/article_pipeline.md
@@ -14 +14,6 @@
-The pipeline turns a task brief into a reviewed and finalized article deliverable through controlled intake, orchestration, optional research, writing, review, finalization, and Chief Editor governance.
+The pipeline turns a task brief into a reviewed and finalized article
+deliverable through controlled intake, orchestration, optional research,
+writing, review, finalization, and Chief Editor governance. When teaching,
+understanding, or complex explanation is material, it also preserves the
+approved Reader Model transition and Learning Design without adding a role or
+artifact.
@@ -74,0 +80,2 @@
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and approved Learning Design sequence when material.
@@ -200,0 +208,2 @@
+- Reader Review is `compact` for a simple reader transfer; a complex teaching
+  outcome may require `normal` despite low factual risk;
@@ -208,0 +218,2 @@
+- Reader Review is normally `normal` when reader change is material and
+  `not applicable` when it is not.
@@ -215,0 +227,2 @@
+- Reader Review is `full` when the article teaches, updates a mental model, or
+  justifies a Bounded Utility Tradeoff; otherwise record the applicable depth.
@@ -276,0 +290,2 @@
+- teaching/explanation must realize the approved reader transition and use only
+  supported or clearly labeled illustrative examples;
@@ -295,0 +311 @@
+- approved Reader Model transition and Learning Design when material;
@@ -376 +392 @@
-| Orchestration gate | `orchestration_plan.md` selects Article Pipeline, assigns roles, and records research need | missing plan or invalid role |
+| Orchestration gate | `orchestration_plan.md` selects Article Pipeline, assigns roles, records research need, and includes the reader transition when material | missing plan, invalid role, or missing material Reader Model contract |
@@ -378 +394 @@
-| Writing gate | `outline.md`, `draft.md`, and `claims-used.md` when needed exist and avoid unsafe claims | invented facts or missing claim traceability |
+| Writing gate | `outline.md`, `draft.md`, and `claims-used.md` when needed exist, avoid unsafe claims, and realize the approved reader transition when material | invented facts, missing claim traceability, or broken material Cognitive Bridge |
--- a/about/review_pipeline.md
+++ b/about/review_pipeline.md
@@ -79,0 +80,9 @@
+When reviewed work has a material Reader Outcome Contract, teaches or explains,
+updates a mental model, or must change reader practice, review applies the
+Reader Review Lens defined in `/agents/review_agent.md`. The result stays inside
+`review.md`; it does not create a new role, gate, cycle, score, or artifact.
+
+Reader-facing work also receives Companion Pass inside the same review. A
+failure that requires substantive rewriting routes to Writer Agent and
+bounded re-review; Final Editor is not a substitute repair owner.
+
@@ -186,0 +196,3 @@
+- Reader Outcome Contract, Cognitive Bridge, Moments of Insight, Practical
+  Transformation, and Learning Design notes when the reader outcome is
+  material;
@@ -264 +276 @@
-| `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
+| `review.md` | Deterministic verdict, analytical-reasoning challenge when applicable, Professional Analysis challenge when applicable, Professional Communication challenge when applicable, Reader Review Lens when applicable, Architecture Review challenge when applicable, active Domain Knowledge Pack challenge when applicable, quality-attribute challenge when applicable, audience/outcome challenge when applicable, option-evaluation challenge when applicable, evidence-confidence challenge, failure-mode findings when applicable, learning/canon candidate challenge when applicable, Editorial Challenge Lens when applicable, required changes | final_editor, chief_editor | never before finalization |
@@ -346,0 +359,6 @@
+
+Reader Review depth follows `/kb/shared_lifecycle_kernel.md`: `compact` for a
+simple low-risk transfer, `normal` for a material standard reader outcome, and
+`full` for complex or source-heavy model change and high-governance teaching.
+The trigger is intended outcome, reader risk, and explanation complexity, not
+length alone.
@@ -378,0 +397,6 @@
+- selected-depth Reader Review when a material Reader Outcome Contract governs
+  the work; compact review asks only about main transfer, intended action, and
+  avoidable burden/artificial tone, while normal and full use the applicable
+  detailed criteria;
+- selected-depth Companion Pass for reader-facing work, with full criteria when
+  depth is normal or full;
@@ -401 +425 @@
-For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope.
+For `changes_requested`, bounded revision is the default. `review.md` must define issue, why it blocks, repair owner, repair scope, do-not-change area, and re-review scope. Re-review stays limited to changed scope when unaffected independence, evidence, and review checks remain current; otherwise it expands only to invalidated checks.
@@ -458,0 +483,2 @@
+| Reader Review gate | When material, understanding, retention, application, Cognitive Bridge, Learning Design sequence, and reader burden have deterministic statuses tied to the Reader Outcome Contract and exact artifact evidence | missing bridge, headings substituted for memorable ideas, vague Practical Transformation, academic or jargon overload that blocks the outcome, or a taste preference presented as a finding |
+| Companion Pass gate | Reader-facing work is natural and concrete enough for the intended reader while preserving precision, evidence, caveats, boundaries, and traceability | taxonomy dump, synthetic expert performance, avoidable academic distance, unsupported friendliness, precision loss, or substantive repair deferred to Final Editor |
@@ -480,0 +507,4 @@
+- when Reader Review is material, `review.md` records all applicable Reader
+  Review criteria, evidence, reader consequences, and bounded repair routing;
+- when material is reader-facing, `review.md` records Companion Pass and routes
+  substantive repair to Writer Agent before approval;
--- a/about/social_pipeline.md
+++ b/about/social_pipeline.md
@@ -197,0 +198,2 @@
+- Reader Review is normally `compact` or `not applicable`; do not force the
+  full learning block onto short copy;
@@ -206,0 +209,2 @@
+- Reader Review remains `compact` unless explanation complexity or reader risk
+  makes `normal` necessary.
@@ -213,0 +218,2 @@
+- Reader Review depth still follows reader outcome; high governance does not
+  make an irrelevant teaching block material.
~~~~
