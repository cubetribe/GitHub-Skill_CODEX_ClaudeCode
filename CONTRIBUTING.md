# Contributing

Thanks for contributing.

This repository exists to provide a strict, reusable GitHub governance skill. Keep changes small, explicit, and easy to review.

## Ground rules

- Never commit directly to `main`.
- Use short topic branches such as `feat/<slug>`, `fix/<slug>`, `chore/<slug>`, or `refactor/<slug>`.
- Use Conventional Commits.
- Never force-push a shared branch.
- Never rewrite shared history.
- Never include unrelated files in a commit.
- Keep the skill and its references aligned with official GitHub documentation when policy guidance is involved.

## Pull requests

- Open a pull request for every change.
- Use the pull request template.
- Link the relevant issue when one exists.
- Update documentation when behavior or governance changes.

## Validation

Before requesting review, make sure:

- `bash -n scripts/install-skill-locally.sh` passes
- `python3 .agents/skills/github-master/scripts/repo_preflight.py --path .` runs successfully
- the skill still installs into both local targets

## Maintainer

Primary maintainer: Dennis Westermann (`@cubetribe`)
