# Step 3 Implementation Plan

## Scope

Perform only Step 3: compress `ai-editorial-office/agents/*.md` role specs by
removing repeated global rules and preserving role-specific boundaries.

## Plan

1. Inspect all current agent specs and identify repeated material from
   `AGENTS.md`, pipelines, templates, review-gate policy, artifact minimalism,
   and context-loading policy.
2. Replace each agent spec with a compact role-local structure:
   mission, primary responsibilities, inputs, outputs, forbidden actions,
   decision boundaries, stop conditions, handoff expectations, and
   role-specific quality checks.
3. Preserve safety-critical role boundaries:
   Chief Editor coordinates, Reviewer reviews, Research provides evidence,
   Writer drafts, UX Writer writes interface copy, Final Editor finalizes after
   review, and Intake normalizes requests.
4. Do not change pipelines, templates, governance model, MVP agent set,
   automation, or review-gate requirements.
5. Verify line-count reduction and scan for repeated lifecycle, context-loading,
   artifact, and pipeline boilerplate.
6. Record changed files, decisions, safety checks, rollback notes, and semantic
   diff summaries for Step 3.

## Completion

Completed. Changes were limited to `ai-editorial-office/agents/*.md` plus the
required Step 3 retrospective files.
