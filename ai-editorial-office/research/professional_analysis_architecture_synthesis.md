# Professional Analysis Architecture Synthesis

Date: 2026-07-08

Status: architecture synthesis for Professional Analysis release. This file is
task/release evidence, not a canonical rule owner.

## Decision

Implement Professional Analysis as one shared capability with optional analysis
lenses.

Do not implement separate capabilities or roles for management consulting,
business analysis, strategic analysis, policy analysis, intelligence products,
product discovery, technology assessment, decision analysis, or executive
analytical communication.

## Architectural Rationale

The current AI Editorial Office architecture remains:

```text
task object first;
capability map second;
roles as accountability wrappers;
workflows and pipelines as execution guidance;
artifacts as views over task state.
```

Professional Analysis fits as a shared capability:

- Chief Editor selects it when structured interpretation, synthesis,
  recommendation, or decision support is material.
- Research Agent supports the evidence base when professional analysis depends
  on external sources, source comparison, stakeholder facts, or domain
  evidence.
- Writer Agent turns approved analysis into the requested artifact when the
  selected route calls for production.
- Review Agent challenges the analytical product inside the existing review
  gate.
- Final Editor preserves approved judgment, caveats, recommendation, and next
  action when a final artifact is produced.

No new role, lifecycle stage, pipeline, review gate, mandatory artifact,
framework owner, or scoring model is needed.

## Relationship To Existing Capabilities

### Analytical Reasoning

Analytical Reasoning owns how conclusions are reasoned: problem framing,
decomposition, competing explanations, assumptions, disconfirmation,
contradiction handling, sufficiency, and uncertainty.

Professional Analysis owns what kind of analytical product is being produced
and whether the product serves the decision: assessment, synthesis, options,
implications, recommendation, or executive brief.

Use both when a recommendation or assessment depends on complex reasoning.

### Evidence Framework

Professional Analysis depends on evidence confidence for material conclusions.
It does not create evidence classes, confidence labels, or a separate evidence
standard.

### Planning And Option Evaluation

Planning owns option generation, evaluation dimensions, selected approach,
tradeoffs, and reconsideration triggers. Professional Analysis packages those
planning results into a decision-ready analytical product when a task asks for
options or recommendations.

### Audience And Outcome Alignment

Professional Analysis must fit a reader and decision context, but
audience/outcome alignment remains the owner for reader, outcome, detail, tone,
format, and usefulness criteria.

### Quality Attributes

Professional Analysis often prioritizes evidence support, analytical rigor,
actionability, clarity, traceability, audience fit, and reviewability. Quality
attribute ownership remains with `/kb/editorial_quality_attributes.md`.

### Architecture Review

Architecture Review owns design fitness and architecture-sensitive judgments.
Professional Analysis may identify architecture questions or compare
architecture options, but Architecture Review must be activated when the work
has architectural significance.

### Engineering Review

Engineering Review owns implementation/change safety. Professional Analysis may
assess technology or implementation implications, but Engineering Review must be
activated when code, configuration, automation, interface, data, reliability,
performance, or security-sensitive change safety is material.

## Capability Shape

Create:

- `kb/professional_analysis.md`

Update:

- `AGENTS.md`
- `kb/00_index.md`
- `kb/capability_registry.md`
- `kb/shared_lifecycle_kernel.md`
- `agents/chief_editor.md`
- `agents/review_agent.md`
- `pipelines/review_pipeline.md`
- `BACKLOG.md`
- `project-state.md`
- copied `/about` files as required by the memory-package checker

Do not update:

- Task Object model structure;
- role set;
- pipelines as workflow sequence;
- lifecycle stages;
- review gate;
- capability definitions for Analytical Reasoning, Architecture Review, or
  Engineering Review;
- `ROADMAP.md`.

## Lens Model

Professional Analysis uses these optional lenses:

| Lens | Covers | Status |
| --- | --- | --- |
| Situation assessment | issue, context, evidence, uncertainty, consequence | active |
| Synthesis brief | patterns, contradictions, decision-relevant insights | active |
| Options and recommendation | alternatives, criteria, tradeoffs, recommendation, next action | active |
| Business or needs analysis | stakeholder need, value, constraints, change context | active |
| Policy or impact analysis | effects, tradeoffs, governance, stakeholder impact, risk | active |
| Product discovery analysis | user problem, context, constraints, opportunity, success signals | active |
| Technology assessment | technology purpose, readiness, benefits, limits, risks, implications | trigger-based |
| Executive decision brief | bottom line, evidence level, recommendation, risk, next decision | active |

## Disposition Decisions

### Merged

- Management consulting and strategic analysis merge as situation assessment,
  synthesis, options/recommendation, and executive decision brief lenses.
- Business analysis merges as business or needs analysis.
- Policy analysis merges as policy or impact analysis.
- Product discovery merges as product discovery analysis.
- Technology assessment merges as a trigger-based lens.
- Decision analysis merges as options/recommendation and executive decision
  brief while leaving option-evaluation ownership in the planning framework.
- Intelligence product style merges as situation assessment and uncertainty
  communication while leaving cognitive reasoning moves in Analytical
  Reasoning.

### Postponed

- Deep domain expertise for software architecture, DevSecOps, cybersecurity,
  and AI engineering until Stage 4 domain packs.
- Quantitative modeling, market sizing, financial modeling, statistical
  modeling, and economic appraisal until a task provides evidence, scope, and
  need.
- Legal, regulatory, and compliance-specific analysis until source-backed
  domain scope exists.
- Competitive intelligence as a standalone capability.
- Automated scoring or mandatory analysis templates.

### Rejected

- New professional analysis roles.
- One capability per analytical domain.
- Mandatory Professional Analysis artifacts.
- A consulting framework owner.
- Duplicate ownership of Analytical Reasoning, evidence, planning,
  audience/outcome, quality attributes, Architecture Review, or Engineering
  Review.

## Activation Rules

Professional Analysis should be activated when a task changes or evaluates:

- strategic, business, product, policy, technology, organizational, or
  operating-context decisions;
- a recommendation, decision brief, options memo, issue brief, assessment, or
  synthesis memo;
- multiple evidence streams that must become decision-relevant findings;
- stakeholder needs, implications, tradeoffs, or risks that affect a choice;
- uncertainty or assumptions that would change a recommendation;
- executive communication of analytical judgment.

Professional Analysis should not be activated for:

- simple factual lookup;
- ordinary summary with no decision need;
- copyediting or tone changes;
- low-risk markdown formatting;
- Architecture Review by another name;
- Engineering Review by another name;
- deep domain conclusions without source-backed domain evidence.

## Evidence Requirements

Professional Analysis evidence should be proportional:

- low-risk synthesis: inspected source set, main findings, confidence and
  caveats;
- recommendation: decision context, options, criteria, evidence basis,
  tradeoffs, uncertainty, and next action;
- business/product/policy analysis: stakeholder or user need, constraints,
  implications, risks, and source-backed assumptions;
- technology assessment: technology surface, current evidence, benefits,
  limitations, risks, readiness or maturity caveat, and decision implication;
- executive brief: bottom line, confidence, material assumptions, risk, and
  decision needed.

No separate artifact is mandatory. Evidence can live in `brief.md`,
`orchestration_plan.md`, `research.md`, production notes, `review.md`, or
`final_decision.md`.

## Validation Strategy

Validation for this release should include:

- existing task lifecycle validator smoke test;
- task pack generator smoke test;
- `/about` memory package sync check;
- `git diff --check`;
- `git diff --cached --check`;
- manual activation examples for Professional Analysis:
  - positive options/recommendation case;
  - positive business or needs analysis case;
  - positive product discovery case;
  - positive technology assessment case;
  - negative ordinary summary case;
  - negative Architecture Review and Engineering Review cases.
