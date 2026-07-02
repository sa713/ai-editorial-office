# Task Manifest

## task identity

- Task ID: TASK-0020
- Task title: Visual sketchnote summary for "Enterprise AI Security Starts with AI Agents"
- Task type: visual_article_sketchnote
- Owner/current role: chief_editor
- Created: 2026-06-01
- Last updated: 2026-06-01

## current state

- Current status: finalized
- Selected pipeline: compact visual branch, mode `visual_article_sketchnote`
- Risk mode: standard
- Process depth: compact
- Execution profile: `compact`
- Current working artifact: `final_decision.md`
- Latest relevant handoff: `handoff-artist-artist-agent-to-review-agent.md`
- Next required action: deliver final PNG path to user

## freshness

- Last verified: 2026-06-01
- Verified by: chief_editor
- Stale if: source PDF changes, user changes requested format/channel, or review requests semantic changes.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: source PDF, approved review, final decision, and `visual-conspect-blog.png`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `AGENTS.md`, this manifest, `status.md`, `review.md`, `final_decision.md`, and `visual-conspect-blog.png`.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no for artifact preparation; user approval required before any external publication.
- Human approval evidence: current user request asks for preparation only.
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `/ai-editorial-office/kb/sources/CSA_+_Zenity_Enterprise_AI_Security_Starts_with_AI_Agents.pdf` | yes | required | Source article. |
| `task-manifest.md` | yes | required | Current state pointer. |
| `orchestration_plan.md` | yes | required | Compact visual route and role contract. |
| `status.md` | yes | required | State history and current owner. |
| `article-source.txt` | yes | conditional | Extracted text used for source reading and review support. |
| `visual_concept.md` | yes | required | Semantic frame for sketchnote. |
| `sketchnote_brief.md` | yes | required | Approved source brief for Artist Agent. |
| `image_prompt.md` | yes | required | Artist Agent execution artifact. |
| `render_sketchnote.py` | yes | optional | Local deterministic rendering helper for reproducibility. |
| `visual-conspect-blog.png` | yes | required | Final PNG target. |
| `review.md` | yes | required | Approved. |
| `final_decision.md` | yes | conditional | Final readiness recorded. |

## stale or conflicting state

- None.

## active constraints

- User constraints: prepare a visual article summary for blog publication.
- Pipeline constraints: active visual mode is `visual_article_sketchnote`; final result must be PNG; SVG may be used only as an internal intermediate if needed.
- Governance constraints: review is required before final readiness; Artist Agent cannot invent meaning beyond approved `visual_concept.md` and `sketchnote_brief.md`.

## open questions

- None blocking. Blog platform dimensions are not specified; default from canonical sketchnote prompt is horizontal 16:9.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- current working artifact;
- `kb/canonical_sketchnote_prompt.md`.

Next action:

- Role: chief_editor
- Action: deliver final PNG path to user
- Expected output: user can publish or request changes
- Stop conditions: user requests changes or a platform-specific variant

## lifecycle notes

- Legacy task folders consulted: no; current source is task-local.
- Old artifact versions consulted: no.
- Safe-to-ignore material: `.DS_Store`.
