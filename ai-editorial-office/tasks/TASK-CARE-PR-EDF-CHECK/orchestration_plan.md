# Orchestration Plan

## task summary

- Task ID: `TASK-CARE-PR-EDF-CHECK`
- User goal: test Editorial Decision Frame on the existing CARE PR case.
- Deliverable: task-local Editorial Decision Frame and Review Agent addendum.
- Source task:
  `/Users/sa/Documents/codex/Care/PR/TASK-CARE-PR-STRATEGY`
- Current active version: `review-addendum.md`

## task classification

- Task type: review / mechanism test-run.
- Risk mode: `standard`
- Factual sensitivity: medium; source-backed/editorial-development boundary is
  central to the check.
- Human approval likely required: only for writing into the external CARE PR
  source folder.
- Rationale: the check validates whether the new decision frame makes the
  already-successful CARE PR route more explicit and reviewable.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: this is a narrow mechanism check, not a rewrite of the CARE PR
  result.
- Forbidden depth shortcuts: do not invent new CARE PR evidence, channels,
  owners, KPIs, dates, approval decisions, or stakeholder claims.
- Expanded profile trigger, if any: user asks to revise `final.md` or turn the
  working framework into implementation-ready PR materials.

## selected pipeline

- Pipeline: review / mechanism test-run over an existing source-bound analytical
  package.
- Why this pipeline: the existing CARE PR task already completed the editorial
  lifecycle; this run evaluates the new pre-writing decision mechanism against
  that result.
- Pipeline exceptions or local constraints: external CARE PR files are read as
  source artifacts and are not overwritten in this workspace-local check.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `constrain` |

- Rationale: the source artifacts are available; the correct test is to constrain
  the frame to the saved CARE PR evidence and existing final output.
- Production may start: yes, as a task-local check only.
- If `block`: not applicable.

## editorial decision frame

### selected editorial route

Prepare a source-bound analytical recommendation package: an internal editorial
conclusion plus a working framework for a future Care image/PR working group.
The result should explain why the source is not ready for PR execution and then
turn the raw brainstorm into a structured problem map, workstreams, sequence,
and implementation boundaries.

### alternatives considered and rejected

1. Immediate PR materials: posts, announcements, slogans, posters, campaign
   copy, or ready-to-send internal communications.
   - Rejected because the source has no approved message, target-channel
     decision, audience priority, owner, metric, sign-off path, or examples of
     final materials.
   - This would turn a raw diagnostic brainstorm into publishable
     communication and would overstate the evidence.
2. Launch-ready PR/action plan.
   - Rejected because the source lists ideas but does not validate them,
     prioritize them, assign owners, set deadlines, define resources, choose
     channels, or establish approval.
   - This would imply implementation decisions that the evidence does not
     support.
3. Research-only classification.
   - Rejected because a pure evidence memo would be too thin for the user's
     requested outcome and for the source's own intent to move toward a future
     working group.
   - The source supports a structured editorial framework as long as the output
     clearly separates source-backed observations from editorial development.

### why the selected route is better

The working-framework route preserves the useful signal in the source while
avoiding premature PR execution. It treats the "low image" issue as a subjective
source hypothesis, not a measured fact; keeps the Care audience, service,
visibility, quality, and internal-process threads visible; and gives a future
working group a practical structure without pretending that channels, KPIs,
owners, promises, or approvals already exist.

### contract for Writer Agent

- Write an internal analytical memo / working framework, not PR copy and not a
  launch plan.
- Start from the editorial decision: the source is a raw diagnostic brainstorm
  that should be structured before any PR materials are produced.
- Separate source-backed observations from editorial synthesis and future-work
  recommendations.
- Preserve the caveat that low Care image is a subjective perception in the
  source, not an established fact.
- Use only saved CARE PR source artifacts; do not add external evidence or
  organizational assumptions.
- Include the core elements needed by the selected route: source classification,
  problem architecture, audience map, reasons not to start with PR materials,
  recommended workstreams, suggested sequence, artifact list, and boundaries.
- Do not invent channels, owners, deadlines, KPIs, survey methodology,
  stakeholder quotes, approved promises, or proof that Care's image is
  objectively low.

### focus for Review Agent

- Verify that `final.md` follows the working-framework route rather than
  becoming PR copy, a campaign plan, or a research-only memo.
- Check that rejected alternatives do not re-enter the final artifact without
  explanation.
- Check that the source-backed/editorial-development boundary is visible,
  especially around the "low image" claim, workstreams, sequence, and artifact
  list.
- Check that the result does not hide premature consulting, overclaiming, or
  task substitution behind a confident framework.

### reroute triggers

- Return to Research Agent if new source files, stakeholder inputs, metrics, or
  examples are introduced.
- Return to Chief Editor if the expected output changes from a working framework
  to PR copy, campaign planning, stakeholder-approval material, or an
  implementation roadmap.
- Return to the user if the team wants publication-ready materials, chosen
  channels, owners, dates, KPIs, or validated claims about Care perception.
- Block if the final must assert factual conclusions that the source only frames
  as hypotheses or subjective impressions.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Source check | Chief Editor | yes | Locate and classify CARE PR artifacts |
| Decision frame | Chief Editor | yes | Record pre-writing decision frame task-locally |
| Review | Review Agent | yes | Assess decision quality and final compliance |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user-provided external path | `search-report.md` | CARE PR found |
| 2 | Chief Editor | CARE PR artifacts | `orchestration_plan.md` | EDF recorded |
| 3 | Review Agent | EDF plus CARE PR `final.md` and evidence artifacts | `review-addendum.md` | mechanism quality assessed |

## completion criteria

- Actual CARE PR source folder is identified.
- Task-local `orchestration_plan.md` contains a meaningful Editorial Decision
  Frame.
- Existing CARE PR `final.md` is checked against the chosen route.
- Review addendum assesses decision quality, not only block presence.
- Production files remain unchanged by this test-run.
