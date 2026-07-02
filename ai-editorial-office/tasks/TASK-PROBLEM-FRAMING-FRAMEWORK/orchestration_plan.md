# Orchestration Plan

## task summary

- Task ID: `TASK-PROBLEM-FRAMING-FRAMEWORK`
- User goal: refine the design into a Problem Hypothesis Framework for AI
  Editorial Office.
- Deliverable: `system_change_proposal.md`
- Current active version: `system_change_proposal.md`

## task classification

- Task type: design-only system change proposal.
- Risk mode: `standard`
- Factual sensitivity: low; architectural precision matters.
- Human approval likely required: yes, before implementation.
- Rationale: the task changes editorial process instructions, but no production
  files are edited in this step.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the requested output is a bounded design, not implementation.
- Forbidden depth shortcuts: do not add roles, mandatory new artifacts, or a
  consulting stage.
- Expanded profile trigger, if any: if implementation is requested later.

## selected pipeline

- Pipeline: design-only system proposal.
- Why this pipeline: the user requested analysis and design, not a patch.
- Pipeline exceptions or local constraints: production files are read-only for
  this step.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the user provided the exact design questions and constraints.
- Production may start: yes, design-only artifact production.

## problem hypothesis

- User request: refine the design so the office records a problem hypothesis,
  not a claim about the user's true problem.
- Problem hypothesis: the system needs a compact way for Chief Editor to state
  the likely editorial problem a request appears to address before choosing the
  route.
- Basis: stated-by-user and source-backed by the review note in this task; the
  previous categorical wording overstated what the editorial office can know.
- Confidence: high.
- Respect boundary: the mechanism must not claim access to the user's real
  intent, override the stated request, or turn editorial routing into
  consulting.
- Routing implication: add a compact Problem Hypothesis in
  `orchestration_plan.md` before the Editorial Decision Frame.

## editorial decision frame

- Chosen editorial route: refine the design-only system change proposal.
- Why this route serves the task: it answers the architecture questions without
  prematurely editing production instructions.
- Alternatives considered, usually 2-3 compact options:
  - Implement immediately:
    - Why rejected: user explicitly asked for design-only.
  - Add standalone `problem_hypothesis.md`:
    - Why rejected: violates minimal-entity and artifact-minimalism goals.
  - Keep categorical problem wording:
    - Why rejected: it implies knowledge the editorial office does not have.
  - Put the hypothesis only in `brief.md`:
    - Why rejected: Intake normalizes the request; Chief Editor owns routing
      and must distinguish stated request from editorial inference.
- Writer/UX Writer contract: not applicable.
- Review focus: verify hypothesis language, basis/confidence logic, minimality,
  compatibility, and anti-consulting boundary.
- Reroute triggers: implementation request, conflict with existing lifecycle, or
  need for separate high-governance analysis.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Own design routing |
| Design | Chief Editor | yes | Produce proposal |
| Review | Review Agent | compact self-check | Check proposal against constraints |

## completion criteria

- Proposal answers all user questions.
- No production files changed.
- No new production artifacts proposed unless justified.
- Git status is reported.
