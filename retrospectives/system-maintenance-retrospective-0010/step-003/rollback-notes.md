# Step 3 Rollback Notes

## Rollback Scope

Rollback Step 3 by restoring only these files from the pre-Step-3 state:

- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/final_editor.md`
- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/agents/research_agent.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/agents/ux_writer.md`
- `ai-editorial-office/agents/writer_agent.md`

The Step 3 retrospective files may be kept as history or removed if the whole
step is reverted.

## Do Not Roll Back

- Do not change `AGENTS.md` as part of Step 3 rollback.
- Do not change pipelines.
- Do not change templates.
- Do not change governance, review-gate, task status model, or MVP agent set.
- Do not reintroduce Step 1 or Step 2 changes unless a separate rollback asks
  for them.

## Validation After Rollback

After rollback, verify:

- all seven original agent files exist;
- no agents were added or removed;
- review remains mandatory;
- role boundaries remain explicit;
- no Step 4-6 files or automation were introduced.
