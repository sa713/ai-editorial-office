# Research

## Research Scope

Create an evidence base for `VIBE_CODING_ROADMAP.md` from:

- the approved Vibe Coding Community vision;
- roadmap.sh Vibe Coding materials;
- roadmap.sh source content nodes in the public repository.

## Key Findings From Vibe Coding Community Vision

The roadmap must serve the community model, not replace it.

Relevant concept points:

- Vibe Coding Community is a community of practice around working AI tasks.
- The community is not a chat, knowledge base, or interest club; it exists to turn practical experience into reusable knowledge.
- Participant path: novice, practitioner, case author, mentor.
- Community activities include Vibe Clinic, Vibecode Challenge, Workflow Demo, Office Hours, Prompt Review Sessions, Live Debugging Sessions, and case reviews.
- Artifacts include case cards, workflow cards, prompt templates, anti-pattern cards, troubleshooting notes, FAQ, and digest.
- Portal is an interface to community practice and memory.
- Operational loop: question -> review/discussion -> artifact -> publication -> reuse.

Implication for writing:

The roadmap should be a navigation artifact for the participant path and portal, not a standalone curriculum that introduces new governance.

## Key Findings From roadmap.sh Vibe Coding Materials

### 1. Vibe coding starts with natural-language intent, but quality depends on human supervision

roadmap.sh frames vibe coding as AI-assisted software creation through natural-language prompts. Its related materials emphasize that the human shifts from writing every line to directing, checking, and guiding the AI.

Use in roadmap:

- Stage 1 should teach what AI can and cannot do.
- The participant should learn to describe intent, constraints, and expected result.
- The first success should be small and observable.

### 2. Mindset matters: AI behaves like a junior collaborator, not an autonomous authority

roadmap.sh source nodes stress conversation, context, checking output, and guiding iteration. The best-practices guide says the user remains architect, reviewer, and decision maker.

Use in roadmap:

- Make "human remains responsible" a cross-stage principle.
- Add review and verification from early stages, not only advanced stages.

### 3. Planning before building is a central practice

The roadmap.sh source node "Plan before you Code" emphasizes defining MVP, breaking work into phases, and using AI to refine the plan before implementation.

Use in roadmap:

- Include a stage on task framing and planning before implementation.
- Require participants to produce a short task brief before asking AI to build.

### 4. Prompt quality depends on scope, context, examples, constraints, and "what not to do"

The roadmap.sh prompting node and best-practices guide highlight one task at a time, specific prompts, examples, constraints, and context documents.

Use in roadmap:

- Teach participants to write prompts as working briefs.
- Treat prompt templates as community artifacts.

### 5. Work should proceed in small steps with clean checkpoints

roadmap.sh repeatedly recommends one feature or task at a time, clean git state before new work, and testing after accepted changes.

Use in roadmap:

- Build a practical loop: plan -> prompt -> inspect -> test -> record.
- For non-developers or non-code tasks, translate git checkpoint into "save current version / keep source copy / document before change."

### 6. Testing, review, and security are not optional

roadmap.sh best-practices and source nodes emphasize reviewing diffs, running tests, type checks, linting, avoiding secrets exposure, and auditing sensitive parts before release.

Use in roadmap:

- Add an explicit verification stage.
- Include "do not publish/deploy/share until checked" as a readiness criterion.

### 7. Context documents and repeatable workflows turn individual experiments into reliable practice

roadmap.sh discusses config/context files such as `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, and `AGENTS.md`, and encourages reusable workflows for repetitive high-stakes tasks.

Use in roadmap:

- Map this to community artifacts: workflow cards, prompt templates, anti-pattern cards.
- Advanced participants should turn repeated personal practices into reusable community materials.

### 8. Mature practice includes cleanup, refactoring, and sharing patterns

roadmap.sh source nodes include periodic review/refactoring and repeatable workflows. The community vision adds case authors and mentors.

Use in roadmap:

- Final stages should focus on stabilizing workflows, extracting reusable lessons, and helping others.

## Adaptation Decisions

1. The community roadmap should use five participant-facing levels:
   - orientation;
   - first successful task;
   - controlled AI workflow;
   - reliable work practice;
   - contribution and mentoring.

2. These levels should map to the vision stages:
   - novice: orientation and first success;
   - practitioner: controlled workflow and reliable practice;
   - case author: contribution artifacts;
   - mentor: helping others and improving shared materials.

3. The roadmap should stay tool-neutral.
   - Specific tools may be examples, but the route should not depend on Claude Code, Cursor, Codex, Gemini CLI, or any one product.

4. The roadmap should include community touchpoints.
   - Each level should point to formats and artifacts from the vision.

5. The roadmap should include exit criteria.
   - A participant should know when they are ready to move forward.

## Do-Not-Say Constraints

- Do not imply AI removes the need for human responsibility.
- Do not present vibe coding as "accept generated output without review."
- Do not make all activities mandatory.
- Do not turn the roadmap into a software engineering curriculum only.
- Do not introduce new official community roles or activities.

## Research Sufficiency

Evidence is sufficient for writing.
