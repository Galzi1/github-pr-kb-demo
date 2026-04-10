# github-pr-kb-demo

Public demo repository for validating the `github-pr-kb` consumer workflow end to end.

## What's here

- `.github/workflows/github-pr-kb.yml` copied from the tool repository
- `demo_app.py` as a small file to change in demo pull requests
- `DEMO-E2E.md` with the remaining manual setup and walkthrough steps

## Goal

Create one or more pull requests with meaningful review discussion, merge them, and let the workflow open a rolling PR that publishes KB files under `kb/`.
