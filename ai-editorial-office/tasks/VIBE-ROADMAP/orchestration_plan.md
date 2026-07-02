# Orchestration Plan

## task summary

- Task ID: `VIBE-ROADMAP`
- User goal: create a practical participant development roadmap for Vibe Coding Community.
- Deliverable: `VIBE_CODING_ROADMAP.md`
- Audience/channel: community participants and organizers; portal roadmap section.
- Current active version: pending.

## task classification

- Task type: article-like knowledge / roadmap artifact.
- Risk mode: `standard`.
- Factual sensitivity: moderate; external source analysis must remain traceable, but the deliverable is a conceptual adaptation, not factual reporting.
- Human approval likely required: no for producing the requested artifact; yes for later adoption as official community roadmap.
- Rationale: source-aware synthesis is needed before writing.

## process depth

- Depth: `normal`.
- Execution profile: `compact`.
- Rationale: one local concept source plus one external roadmap source; enough evidence for a compact research base and reviewed final artifact.
- Forbidden depth shortcuts: no direct production without source analysis and review.
- Expanded profile trigger, if any: user asks to turn this into a full curriculum, course, portal IA, or multi-month program.

## selected pipeline

- Pipeline: `article_pipeline`.
- Why this pipeline: the output is a structured knowledge artifact with source-aware synthesis and review requirements.
- Pipeline exceptions or local constraints: the final deliverable is named `VIBE_CODING_ROADMAP.md` per user request instead of generic `final.md`.

## client profile

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Activation reason: not applicable.
- Stop condition: none.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `inferred` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: user gave source, target artifact, purpose, and development span.
- Production may start: yes.
- Scope boundary: design a practical roadmap, not a new community strategy.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Route task and maintain state |
| Research | Research Agent | yes | Analyze vision and roadmap.sh source material |
| Writing | Writer Agent | yes | Produce roadmap draft and final requested artifact |
| Review | Review Agent | yes | Validate source alignment and usefulness |
| Final governance | Chief Editor | yes | Record final decision |

## required knowledge and evidence

- Required source/evidence files:
  - `../VIBE-VISION/VIBE_CODING_COMMUNITY_VISION_v1_1.md`
  - `research.md`
  - `sources.md`
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Task scope |
| `task-manifest.md` | required | all roles | State pointer |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `sources.md` | required | Research / Review | External source traceability |
| `research.md` | required | Writer / Review | Source synthesis |
| `outline.md` | required | Writer / Review | Roadmap structure |
| `draft.md` | required | Review | Reviewed draft |
| `claims-used.md` | conditional | Review | Compact source claims in final |
| `review.md` | required | Chief Editor | Independent review |
| `VIBE_CODING_ROADMAP.md` | required | user | Final requested artifact |
| `final_decision.md` | required | Chief Editor | Governance conclusion |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user request, local vision, source boundary | brief, plan, status, manifest | route recorded |
| 2 | Research Agent | vision + roadmap.sh materials | `sources.md`, `research.md` | evidence sufficient |
| 3 | Writer Agent | brief + research | `outline.md`, `draft.md`, `claims-used.md` | draft ready for review |
| 4 | Review Agent | draft + evidence | `review.md` | approved or changes requested |
| 5 | Chief Editor / Final Editor compact | approved draft | `VIBE_CODING_ROADMAP.md`, `final_decision.md` | final artifact complete |

## review requirements

- Review artifact: `review.md`
- Review depth: compact standard review.
- Reviewer independence requirement: review must validate the writer output against the brief, vision, and source synthesis.
- Claims/evidence checks required: source claims about roadmap.sh practices and lifecycle must be traceable.

## completion criteria

- `VIBE_CODING_ROADMAP.md` exists and is current.
- `review.md` approves the roadmap.
- `final_decision.md` records final governance outcome.
- Status and manifest point to the final artifact.
