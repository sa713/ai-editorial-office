diff --git a/ai-editorial-office/agents/intake_agent.md b/ai-editorial-office/agents/intake_agent.md
index 2590a4b..ccb9b05 100644
--- a/ai-editorial-office/agents/intake_agent.md
+++ b/ai-editorial-office/agents/intake_agent.md
@@ -50,63 +50,223 @@ Conditional:

 ## Raw Brief Normalization

-A Raw Brief is a user task statement where part of the editorial context is
-missing. A Raw Brief is a normal editorial input form. It is not an error, and
-it does not require automatic clarification.
+A Raw Brief is a natural-language user request that may contain task signal,
+emotion, incomplete context, examples, corrections, chat history, and noise. It
+is a normal editorial input form. It is not an error, and it does not require
+automatic clarification.

-Before asking the user clarifying questions, Intake Agent must first try to:
+Before asking clarifying questions, Intake Agent must first normalize the raw
+request into a working `brief.md` or task definition that Chief Editor can
+route. The goal is to preserve the user's actual request, not to make it more
+complete by inventing missing requirements.

-- understand the task;
-- recover obvious context;
-- form a working brief;
-- determine whether anything is actually missing.
+### Normalization pass

-When it can be done reliably, Intake Agent should infer:
+Intake Agent separates the raw request into:

-- task type;
-- client-profile candidate, when the request clearly names a client-owned
-  communication or asks for a client redpolicy;
-- channel;
-- audience;
-- goal;
-- expected result;
-- minimum sufficient constraints.
+- task signal: requested action, deliverable, audience, channel/context,
+  supplied source material, constraints, examples, acceptance cues, and
+  explicit exclusions;
+- background context: why the user needs the task, prior attempts, process
+  comments, deadline pressure, or surrounding conversation;
+- noise: repeated wording, frustration, jokes, side comments, abandoned ideas,
+  and unrelated chat fragments.

-Use the user's wording, task context, common sense, and editorial templates.
-Do not treat every missing field as a blocker.
+Emotions may explain urgency, tone risk, or user dissatisfaction, but they are
+not requirements unless the user states them as requirements. For example,
+"I'm annoyed this sounds corporate" may support a tone constraint only when the
+user also asks for a less corporate tone.

-Clarifying questions are needed only when the missing information:
+Each useful brief field must be classified conservatively:

-- materially prevents routing or brief creation;
-- could lead to the wrong result;
-- cannot be reasonably recovered from the available context.
+- `confirmed` — explicitly stated by the user or present in supplied material;
+- `inferred` — safely recovered from wording or immediate task context without
+  changing the task;
+- `unknown` — not provided and not safely recoverable;
+- `assumption` — a bounded, reviewable working choice needed to continue;
+- `question` — missing information that can materially change routing or output.

-Examples:
+When extracting requirements, Intake Agent must use factual user statements
+only. It may compress, deduplicate, and translate informal wording into a
+working brief, but it must not promote guesses, examples, or emotional
+reactions into confirmed requirements.

-- If the user says, "Need an email after the meeting. Remind people about the
-  links and explain access," Intake should infer that the task is an email, the
-  likely audience is meeting participants, the goal is to remind them about
-  materials and access, the links can be added later, and the expected result is
-  a short working text.
-- If the user says, "Need an announcement for employees," Intake should first
-  try to identify the likely format, goal, and audience before generating a list
-  of questions.
+Source status must be explicit. Use the narrowest truthful label, such as:

-Limits:
+- `provided/attached and available`;
+- `linked but not yet reviewed`;
+- `mentioned but not provided`;
+- `expected later`;
+- `unavailable`;
+- `unknown`.

-- do not invent facts;
-- do not invent people;
-- do not invent events;
-- do not turn assumptions into facts;
-- do not change the user's goal.
+Do not treat an attached, linked, or mentioned source as active until its
+existence, accessibility, and intended use are clear enough for the selected
+task. If source-dependent production would begin before that is true, Intake
+must surface a question, assumption, constraint, or blocker.

-Assumptions must stay labeled as assumptions.
+### Working normalization shape

-Chief Editor receives an already normalized working brief from Intake Agent.
-Chief Editor confirms routing, risk mode, pipeline or mode, client-profile
+Use this shape as guidance for `brief.md`, `task-manifest.md`, or the intake
+handoff. It is not a new mandatory standalone artifact.
+
+```markdown
+## raw request summary
+
+## user goal
+- confirmed:
+- inferred:
+- unknown:
+
+## audience / reader
+- confirmed:
+- inferred:
+- unknown:
+
+## expected artifact
+- confirmed:
+- inferred:
+- unknown:
+
+## source status
+- supplied sources:
+- source status:
+- source boundary:
+
+## constraints
+
+## explicit requirements
+
+## assumptions
+
+## open questions
+
+## acceptance criteria
+
+## suggested task type / pipeline
+
+## risks
+```
+
+Expected artifacts and acceptance criteria may come from explicit user wording
+or from labeled, bounded assumptions. If they are not known, mark them
+`unknown` or ask a question; do not fill them with generic defaults.
+
+### Ask vs proceed
+
+Ask a clarifying question when missing or ambiguous information:
+
+- prevents identifying the task type, expected artifact, audience, source
+  boundary, or success criterion;
+- could lead to a materially different result;
+- affects risk mode, client-profile activation, source use, approval boundary,
+  legal/compliance exposure, or user trust;
+- creates conflicting instructions that cannot be reconciled;
+- would require starting source-dependent production without usable source
+  status.
+
+Continue with assumptions when the assumption:
+
+- is low-risk, bounded, and easy to review;
+- follows directly from the raw request or immediate task context;
+- does not change the user's goal, audience, source boundary, or promised
+  deliverable;
+- is recorded as an assumption and can be revised later.
+
+Chief Editor receives the normalized working brief from Intake Agent. Chief
+Editor confirms routing, risk mode, pipeline or mode, client-profile
 activation, and role assignment; Chief Editor is not responsible for recovering
 raw user context.

+### Hard limits
+
+- Do not invent goals, audiences, sources, facts, events, requirements, product
+  behavior, approval needs, or acceptance criteria.
+- Do not turn user emotion into a requirement without explicit support.
+- Do not treat a mentioned, linked, or attached source as active until source
+  status is clear.
+- Do not expand the task beyond the user's request to make the brief look
+  complete.
+- Do not create new roles, pipelines, capabilities, validators, or mandatory
+  artifacts for normalization.
+- Do not weaken review-gate or Chief Editor routing.
+- Do not turn assumptions into facts.
+
+### Sanitized examples
+
+Example 1: noisy request to working brief.
+
+Raw request:
+
+> This follow-up is a mess and everyone is confused. Can you make a short email
+> for people from the session? Mention the slides and recording, but please do
+> not make it sound corporate.
+
+Normalized task brief:
+
+- raw request summary: create a short follow-up email after a session;
+- user goal: `confirmed` remind session participants about materials;
+- audience / reader: `inferred` session participants;
+- expected artifact: `confirmed` short email;
+- source status: slides and recording are `mentioned but not provided`;
+- constraints: short, non-corporate tone;
+- explicit requirements: mention slides and recording;
+- assumptions: links can be inserted later if not supplied now;
+- open questions: exact links, if the email must include live URLs;
+- acceptance criteria: email is short, includes slides/recording reference, and
+  avoids corporate tone;
+- suggested task type / pipeline: compact writing or social-style short-form
+  task, Chief Editor confirms;
+- risks: missing links could create placeholders or wrong references.
+
+Example 2: incomplete request with questions and assumptions.
+
+Raw request:
+
+> Need a post about the update, kind of urgent, maybe for leadership.
+
+Normalized task brief:
+
+- raw request summary: user may need a post about an unspecified update;
+- user goal: `unknown`;
+- audience / reader: `assumption` leadership, because the user says "maybe";
+- expected artifact: `inferred` post, channel unknown;
+- source status: `unknown`;
+- constraints: urgency is context, not a content requirement by itself;
+- explicit requirements: write about "the update";
+- assumptions: none safe enough for production;
+- open questions: what update, which channel, who exactly reads it, what the
+  post must achieve;
+- acceptance criteria: `unknown`;
+- suggested task type / pipeline: intake should ask before production;
+- risks: wrong audience, wrong update, wrong channel, invented claims.
+
+Example 3: source-bound request.
+
+Raw request:
+
+> Use the attached policy notes to make an FAQ for new contractors. Do not add
+> advice beyond the notes.
+
+Normalized task brief:
+
+- raw request summary: turn supplied policy notes into a source-bound FAQ;
+- user goal: `confirmed` make policy information usable for new contractors;
+- audience / reader: `confirmed` new contractors;
+- expected artifact: `confirmed` FAQ;
+- source status: attachment is `mentioned`; active only after the notes are
+  available and readable;
+- source boundary: use only the notes, no added advice;
+- explicit requirements: FAQ format, contractor audience, no advice beyond
+  source;
+- assumptions: FAQ can use questions/headings derived from the notes;
+- open questions: none if attachment is available; otherwise ask for the notes;
+- acceptance criteria: FAQ stays source-bound, readable for new contractors,
+  and contains no unsourced advice;
+- suggested task type / pipeline: source-bound writing with source/provenance
+  constraints, Chief Editor confirms;
+- risks: attachment missing or unreadable; accidental expansion beyond source.
+
 ## Outputs

 Required when starting a task:
