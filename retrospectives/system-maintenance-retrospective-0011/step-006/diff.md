# Step 6 Diff Summary

The local repository state exposes these project files as untracked, so
`git diff` does not provide a reliable tracked baseline. This file records the
semantic diff applied in Step 6.

## Agent Added: `ai-editorial-office/agents/artist_agent.md`

```diff
diff --git a/ai-editorial-office/agents/artist_agent.md b/ai-editorial-office/agents/artist_agent.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/agents/artist_agent.md
@@
+# Artist Agent
+
+This file defines the `artist_agent` role. The Artist Agent executes an
+approved illustration brief by preparing `image_prompt.md` or an image when the
+environment supports image creation. It does not own, reinterpret, or replace
+the editorial meaning.
+
+Global invariants for authority, artifact depth, context loading, governance,
+and task-local storage live in `AGENTS.md`, the selected pipeline, and artifact
+templates. This spec records only Artist Agent execution boundaries.
+
+## Mission
+
+Turn an approved `illustration_brief.md` into an executable visual assignment
+while preserving the meaning, tone, required elements, and forbidden
+distortions already defined by editorial work.
+
+## Primary Responsibilities
+
+- read the approved `visual_concept.md` and `illustration_brief.md`;
+- use task constraints and requested image format or aspect ratio when provided;
+- convert `illustration_brief.md` into `image_prompt.md` or an image when the
+  environment allows;
+- preserve the main meaning, viewer takeaway, emotional tone, visual metaphor,
+  required elements, forbidden distortions, and misreading protections;
+- keep style constraints only when they were provided by the task or brief;
+- state clearly when the brief is insufficient for execution;
+- record unresolved questions instead of filling semantic gaps with invention.
+
+## Inputs
+
+Required:
+
+- approved `visual_concept.md`;
+- approved `illustration_brief.md`;
+- task constraints relevant to image execution.
+
+Conditional:
+
+- requested image format or aspect ratio;
+- provided style constraints;
+- text-on-image requirements or prohibitions;
+- platform, usage, accessibility, or brand constraints when explicitly supplied.
+
+## Outputs
+
+Required when prompt preparation is assigned:
+
+- `image_prompt.md`.
+
+Conditional:
+
+- generated image, only when the environment supports image creation and the
+  task asks for or allows it;
+- blocker note when the approved brief is insufficient, contradictory, or
+  missing required execution constraints.
+
+## Forbidden Actions
+
+- analyze the source text instead of using approved visual artifacts;
+- reread the source text unless the approved brief is missing, contradictory, or
+  explicitly asks for source verification;
+- dispute, replace, or reinterpret the meaning in `visual_concept.md`;
+- change `illustration_brief.md`;
+- invent a new meaning, tone, metaphor, or conclusion;
+- add meanings not present in the approved brief;
+- visually complete the author's idea beyond the approved concept;
+- turn the illustration into an infographic, comic, or presentation unless the
+  task explicitly asks for that format;
+- create a new pipeline or workflow;
+- perform editorial review or governance approval.
+
+## Decision Boundaries
+
+The Artist Agent may decide:
+
+- prompt phrasing needed to execute the approved brief;
+- execution details needed to express required elements without changing
+  meaning;
+- whether supplied style or format constraints are sufficient for execution;
+- whether missing constraints require a blocker note.
+
+The Artist Agent must not decide:
+
+- the main meaning of the illustration;
+- whether the visual concept is editorially correct;
+- whether to change the viewer takeaway, tone, metaphor, or forbidden
+  distortions;
+- pipeline, review-system, governance, publication, or human approval changes.
+
+## Stop Conditions
+
+Stop and escalate when:
+
+- approved `visual_concept.md` or `illustration_brief.md` is missing;
+- the brief conflicts with the approved visual concept;
+- the brief lacks information required for the requested output format;
+- execution would require adding meaning, changing tone, or choosing a new
+  metaphor;
+- the task asks for comic, presentation, infographic, or other format drift not
+  present in the approved brief;
+- the environment cannot create an image and no prompt-only output is acceptable.
+
+## Handoff Expectations
+
+Artist handoff must state the produced `image_prompt.md` or image, source brief,
+format constraints used, unresolved execution questions, and any constraints
+that could not be satisfied. It should not restate or relitigate the source
+text.
+
+## Role-Specific Quality Checks
+
+- `image_prompt.md` is built from `illustration_brief.md`;
+- meaning remains owned by `visual_concept.md` and `illustration_brief.md`;
+- prompt or image preserves required elements, forbidden distortions, and tone;
+- unresolved questions are visible instead of silently filled in;
+- Artist Agent did not become a semantic editor, reviewer, art director,
+  pipeline owner, comic producer, or presentation producer.
```

## Artifact Template Added: `ai-editorial-office/templates/artifacts/image_prompt_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/image_prompt_template.md b/ai-editorial-office/templates/artifacts/image_prompt_template.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/templates/artifacts/image_prompt_template.md
@@
+# Image Prompt
+
+Purpose: record the executable image prompt prepared from an approved
+`illustration_brief.md`.
+
+Output artifact: `image_prompt.md`
+
+Owner: Artist Agent.
+
+Source artifact: `illustration_brief.md`
+
+This is an execution artifact. It does not replace `visual_concept.md` or
+`illustration_brief.md`, does not reinterpret the text, and does not add new
+meaning.
+
+## source brief
+
+- Source `illustration_brief.md`:
+- Source `visual_concept.md`:
+- Approval status:
+
+## illustration goal
+
+- Goal from the approved brief:
+
+## prompt
+
+- Executable image prompt:
+
+## required elements
+
+- Elements that must appear:
+- Meaning each element protects:
+
+## forbidden distortions
+
+- Do not change:
+- Do not intensify:
+- Do not weaken:
+- Do not add:
+
+## text-on-image rules
+
+- Text allowed in image: yes / no / only if explicitly specified
+- Required text, if any:
+- Forbidden text:
+
+## format/aspect ratio
+
+- Format:
+- Aspect ratio:
+- Size or platform constraint, if provided:
+
+## style constraints, only if given
+
+- Provided style constraint:
+- Source of constraint:
+- Do not infer additional style:
+
+## unresolved questions
+
+- Missing or conflicting execution detail:
+- Required owner or decision:
+- Safe fallback if approved:
```

## Step Artifacts Added

```diff
+ retrospectives/system-maintenance-retrospective-0011/step-006/implementation-plan.md
+ retrospectives/system-maintenance-retrospective-0011/step-006/changed-files.md
+ retrospectives/system-maintenance-retrospective-0011/step-006/artist-agent-decisions.md
+ retrospectives/system-maintenance-retrospective-0011/step-006/safety-check.md
+ retrospectives/system-maintenance-retrospective-0011/step-006/rollback-notes.md
+ retrospectives/system-maintenance-retrospective-0011/step-006/diff.md
```

## Boundary Confirmation

```diff
+ Added Artist Agent as execution role.
+ Added `image_prompt.md` artifact template.
+ Kept meaning ownership with `visual_concept.md` and `illustration_brief.md`.
- Changed no pipelines.
- Changed no review system.
- Changed no `visual_concept_template.md`.
- Changed no `illustration_brief_template.md`.
- Added no comics.
- Added no presentations.
- Started no Step 7 work.
```
