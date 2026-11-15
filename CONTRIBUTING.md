# Contributing to HASA

Thanks for helping. This page describes how every change gets into the project.

## Workflow: issue → branch → pull request

1. **Open an issue first.** Describe the bug or the feature and what "done" means.
   Small typo fixes can skip this.
2. **Create a branch from `main`.** Never commit directly to `main`.
   Name it `<type>/<issue-number>-<short-description>`, for example:
   - `fix/3-pandas-resample`
   - `feat/12-gev-lmoments`
   - `docs/1-project-workflow`
   - `test/4-regression-baseline`
   - `chore/5-pyproject`
3. **Commit in small steps.** Write commit messages in the imperative
   ("Fix date parsing for DD-MM-YYYY") and mention the issue (`Refs #3`).
4. **Open a pull request** into `main`. Fill in the template and write `Closes #<issue>`
   so the issue closes when the PR is merged.
5. **Update `CHANGELOG.md`** under *Unreleased* in the same pull request.
6. **Merge** after review and green checks, using *Squash and merge*. Delete the branch afterwards.

## Results must not change by accident

The flood estimates from the v1.0.0 release are recorded in [ROADMAP.md](ROADMAP.md).
Once the regression test exists, it must pass on every pull request. If a change is meant to
alter results (for example switching to the hydrological year), say so in the pull request,
explain why, and update the reference values and the changelog together.

## Releases

Versions follow [Semantic Versioning](https://semver.org/). A release is a git tag `vX.Y.Z`
on `main` plus a GitHub release whose notes are the changelog section for that version.

## Code style

- Python 3.11 or newer.
- Calculations live in the core package and are tested; the user interface only calls them.
- Formatting and linting with ruff (set up in Phase 1).

## Licence and authorship

The project is licensed under GPL-3.0 (see [LICENSE](LICENSE)). The original authors are
Akash Handique and Aswatha Narayana Sanagavarapu. Do not copy code from other projects unless
their licence allows it and the source is credited.
