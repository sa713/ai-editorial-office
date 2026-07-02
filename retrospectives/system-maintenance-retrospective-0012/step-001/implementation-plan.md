# Step 1 implementation plan

Status: completed as inventory-only work.

Scope:

- Find active and historical mentions of `MVP`, including the requested phrase families: `MVP role`, `MVP agent`, `MVP workflow`, `MVP architecture`, and `MVP phase`.
- Classify mentions into active policy versus historical / retrospective material.
- Identify why `MVP` is used in active policy and what replacement category would preserve meaning.
- Identify risky replacement zones.
- Propose a safe replacement strategy without implementing it.

Non-goals:

- Do not edit `AGENTS.md`.
- Do not edit `project-state.md`.
- Do not edit `agents/*.md`.
- Do not edit `pipelines/*.md`.
- Do not edit `templates/**/*.md`.
- Do not edit `editorial_knowledge/*.md`.
- Do not edit `kb/*.md`.
- Do not start Step 2.
- Do not automatically replace `MVP`.

Search approach:

- Active policy search covered:
  - `ai-editorial-office/AGENTS.md`
  - `ai-editorial-office/project-state.md`
  - `ai-editorial-office/agents/*.md`
  - `ai-editorial-office/pipelines/*.md`
  - `ai-editorial-office/templates/**/*.md`
  - `editorial_knowledge/*.md`
  - `ai-editorial-office/kb/*.md`
- Historical search covered:
  - `retrospectives/**/*.md`
  - `ai-editorial-office/tasks/**/*.md`
  - old review / report files discovered in repository search, including `about/project_tree.md`.
- Search was run case-insensitively for Markdown files with `\bMVP\b`.
- A non-Markdown false positive in a PDF body was ignored as binary/source noise.

Deliverables created in this step:

- `implementation-plan.md`
- `mvp-inventory.md`
- `active-policy-findings.md`
- `historical-findings.md`
- `replacement-strategy.md`
- `safety-check.md`

Completion criteria mapping:

- Where `MVP` affects the system: covered in `active-policy-findings.md` and `safety-check.md`.
- Where `MVP` is just history: covered in `historical-findings.md`.
- What to replace it with: covered in `active-policy-findings.md` and `replacement-strategy.md`.
- No working policy files changed: covered in `safety-check.md`.
