# GitHub Master Skill for Codex and Claude Code

An open-source GitHub governance skill for small teams that work with a live `main` branch, short-lived topic branches, and strict collaboration guardrails.

Created by Dennis Westermann.

## Copy-Paste Prompt

Give this prompt to your local coding assistant if you want it to clone this repository and install the skill automatically:

```text
Clone https://github.com/cubetribe/GitHub-Skill_CODEX_ClaudeCode.git into a sensible local workspace folder on this machine. Then enter the repository root and run ./scripts/install-skill-locally.sh so the github-master skill is installed into ~/.codex/skills/github-master and ~/.claude/skills/github-master. After installation, verify that both target folders contain SKILL.md, agents/openai.yaml, references/, assets/, and scripts/repo_preflight.py. Report the local clone path, the install result for Codex and Claude Code, and any missing prerequisites. Do not push anything to GitHub.
```

A standalone shareable version of the same prompt lives in [`prompts/install-github-master-skill.md`](./prompts/install-github-master-skill.md).

## Why this repository exists

Small teams usually do not need a heavy branching model. They need a safe one.

This repository packages a reusable skill that pushes AI agents toward:

- protected `main`
- short-lived topic branches
- pull requests as the default integration path
- strict review and status-check gates
- explicit release-impact reporting
- a hard push gate: never push without an explicit yes

The skill is designed for Codex and Claude Code local skill directories and includes a repo preflight script so agents can inspect versioning, release tooling, CI files, and branch state before editing.

## What is included

- canonical skill source in [`.agents/skills/github-master`](./.agents/skills/github-master)
- local installer for Codex and Claude Code in [`scripts/install-skill-locally.sh`](./scripts/install-skill-locally.sh)
- shareable installation prompt in [`prompts/install-github-master-skill.md`](./prompts/install-github-master-skill.md)
- research and workflow reports in [`reports/`](./reports)
- repository standards for open-source collaboration

## Recommended workflow

The skill follows a strict delivery loop:

1. `RESEARCHER`
2. `ARCHITECT`
3. `BUILDER`
4. `VALIDATOR`
5. `RELEASE MANAGER`

For small teams with a live `main` branch, the default recommendation is:

- GitHub Flow with short-lived branches
- protected `main`
- pull-request-only merges
- one approval from another person
- stale approval dismissal
- strict required status checks
- linear history
- squash merge only
- automatic deletion of merged branches

## Local installation

Run:

```bash
./scripts/install-skill-locally.sh
```

This syncs the skill into:

- `~/.codex/skills/github-master`
- `~/.claude/skills/github-master`

On this machine, the Claude Code local skill path is `~/.claude/skills`.

## Repository layout

```text
.agents/skills/github-master/   Canonical skill source
.github/                        Repo-level pull request and CI standards
prompts/                        Copy-ready prompts for coding assistants
reports/vX.Y.Z/                 Research, architecture, build, validation, release reports
scripts/                        Local installation helpers
```

## Open source

This repository is released under the MIT License. See [LICENSE](./LICENSE).

## Author

Dennis Westermann  
Cubetribe Oldenburg  
[dennis-westermann.de](https://www.dennis-westermann.de)
