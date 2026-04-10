# Demo E2E Plan for `Galzi1/github-pr-kb-demo`

This file separates what was created automatically from the steps that still need a human because they involve secrets, pull request review judgment, or GitHub UI actions.

## Automated setup already completed

1. Created the public GitHub repository `Galzi1/github-pr-kb-demo`.
2. Cloned it locally to `C:\Users\galzi\src\github-pr-kb-demo`.
3. Added a demo target file: `demo_app.py`.
4. Added `.gitignore` entries for `.github-pr-kb/`, `.env`, and local Python artifacts.
5. Copied the shipped workflow into `.github/workflows/github-pr-kb.yml`.
6. Added this runbook and updated the demo repo `README.md`.
7. Committed and pushed the initial demo scaffold to `main`.

## Remaining manual setup

### 1. Add repository secrets

You must add these in **GitHub -> Settings -> Secrets and variables -> Actions**:

| Secret | Required | Notes |
| --- | --- | --- |
| `ANTHROPIC_API_KEY` | yes | Needed for `classify` and `generate` in the workflow |
| `KB_VARIABLES_TOKEN` | recommended quickstart | Fine-grained PAT with `Variables`, `Contents`, and `Pull requests` set to **Read and write** |
| `KB_VARIABLES_APP_ID` | optional advanced path | Use instead of PAT if you prefer a GitHub App |
| `KB_VARIABLES_APP_PRIVATE_KEY` | optional advanced path | Pair with `KB_VARIABLES_APP_ID` |

Do not commit these to the repo. The workflow already uses the default `KB_TOOL_REPOSITORY` and pinned `KB_TOOL_REF` from the source project.

### 2. Confirm Actions are enabled

Open the **Actions** tab in `Galzi1/github-pr-kb-demo` and confirm workflows are allowed to run for the repository.

## Demo scenario walkthrough

### 3. Create a pull request that will generate useful review discussion

Recommended example:

1. Create a branch such as `demo/pricing-update`.
2. Change `demo_app.py` in a way that invites review discussion, for example:
   - rename `tax_rate` to a more domain-specific name,
   - add a second pricing helper,
   - introduce a small bug or ambiguous behavior for reviewers to comment on.
3. Push the branch and open a PR.

### 4. Add meaningful PR comments before merge

The demo is only useful if the PR has real discussion. Add comments such as:

- a review comment on a changed line in `demo_app.py`,
- a general PR conversation comment explaining a tradeoff,
- a follow-up note after an implementation change.

If you are doing this solo, at least add issue comments on the PR conversation and one review comment from a second GitHub account if possible.

### 5. Merge the PR

After the comments exist, merge the PR into `main`.

### 6. Watch the workflow

The merged PR should trigger `.github/workflows/github-pr-kb.yml` automatically. You can also use **Run workflow** (`workflow_dispatch`) for recovery or backfill.

Expected behavior:

1. The workflow restores `.github-pr-kb/cache/`.
2. It checks whether the merged PR is newer than `KB_LAST_SUCCESSFUL_CURSOR`.
3. It runs `extract`, `classify`, and `generate` only when needed.
4. It updates or creates the rolling branch `automation/github-pr-kb`.
5. It opens or updates the rolling PR titled `chore: update PR knowledge base`.

### 7. Verify generated KB output

Open the rolling PR and confirm it includes:

- `kb/INDEX.md`
- `kb/.manifest.json`
- one or more generated markdown files under `kb/`

### 8. Merge the rolling KB PR

Merge the `automation/github-pr-kb` PR so the generated KB becomes part of the demo repository's main branch.

## Optional recovery exercises

Try one or both after the happy path works:

1. **No-new-PR check**: run `workflow_dispatch` with no new merged PRs and confirm the workflow skips before the expensive pipeline.
2. **Backfill check**: run `workflow_dispatch` with a `since` value older than the current cursor and confirm the workflow still preserves the latest `KB_LAST_SUCCESSFUL_CURSOR`.

## Success criteria

The demo is successful when:

1. At least one merged PR with meaningful discussion exists.
2. The workflow creates or updates the rolling PR automatically.
3. The rolling PR contains KB files under `kb/`.
4. Re-running without new merged PRs cleanly no-ops.
