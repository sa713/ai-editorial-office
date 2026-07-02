# Brief

Task ID: `TASK-0001`

Task title: `AI support for editors and UX writers in product teams`

Task type: `article`

Requested output: `draft article`

Audience: `editors, UX writers, product teams`

Primary goal:

Create a draft article for an internal portal explaining how AI can help editors and UX writers in product teams without replacing editorial judgment.

Article angle or thesis:

AI should be presented as a practical assistant for editorial work: it helps teams collect draft material faster, test structure, adapt copy, and find weak spots, while the editor remains responsible for meaning, accuracy, tone, and final decisions.

Scope:

- Include: practical ways AI can support editors and UX writers, especially drafting, structure checks, adaptation, and weakness detection;
- Include: clear distinction between AI assistance and human editorial responsibility;
- Include: calm, non-hype framing for internal product-team readers;
- Exclude: claims that AI replaces editors or removes the need for review;
- Exclude: promotional, sensational, or vendor-specific AI messaging.

Format requirements:

- Length: approximately 4000 characters;
- Structure: article draft with a clear thesis, practical sections, and a concise conclusion;
- Tone: calm, practical, non-hype;
- Channel or destination: internal portal.

Factual requirements:

- Factual claims expected: `yes`;
- Research required: `unknown`;
- Source freshness matters: `unknown`;
- Factual sensitivity: `medium`.

Supplied materials:

- Raw user request in chat, no external materials supplied.

Constraints:

- Use Article Pipeline;
- Act as `intake_agent` only;
- Create only initial bootstrap files;
- Do not create `review.md`, `final.md`, `final_decision.md`, or `approval.md` during bootstrap;
- Do not start writing;
- Do not start review.

Acceptance criteria:

- Task folder exists at `/tasks/TASK-0001/`;
- Initial bootstrap files exist: `brief.md`, `status.md`, `open-questions.md`, `handoff-intake-intake-agent-to-chief-editor.md`;
- Brief captures task goal, audience, tone, output, scope, constraints, and acceptance criteria;
- Chief Editor can continue orchestration without relying on chat history;
- review must be completed before finalization;
- final deliverable must be created by `final_editor`;
- final governance decision must be created by `chief_editor`.

Open questions:

- Should Chief Editor require separate research, or can this proceed as a low-source internal thought-leadership article with explicit assumptions?
- Are there internal AI/editorial policies, examples, or product-team practices that should guide the article?
- Should the draft include concrete workflow examples from the organization, or keep examples generic?
