# Step 4 Implementation Plan

## Scope

Perform only Step 4: compress `ai-editorial-office/templates/**/*.md` into
usable working forms while preserving governance-critical fields, review
requirements, conditional artifact behavior, and the short restart read path.

## Plan

1. Inspect all markdown templates under `ai-editorial-office/templates/`.
2. Save a temporary baseline for template diff review.
3. Compress artifact and agent templates first, removing repeated policy prose
   and replacing it with short canonical references.
4. Compress task templates while preserving required files, conditional artifact
   rules, source/evidence fields, review verdict fields, blockers/open
   questions, risk mode, process depth, current-version pointers, and restart
   read set.
5. Do not edit roles, pipelines, `AGENTS.md`, governance model, or review-gate
   rules.
6. Record changed files, decisions, safety checks, rollback notes, and template
   diff summary.

## Completion

Completed. Changes were limited to `ai-editorial-office/templates/**/*.md` plus
the required Step 4 retrospective files.
