# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-03-16

### Added

- Copy-ready installation prompt at the top of the README for local coding assistants.
- Standalone prompt file under `prompts/install-github-master-skill.md` with standard, Codex-only, and Claude Code-only variants.

### Changed

- README onboarding flow now points users directly to clone-plus-install instructions for AI-assisted setup.

## [0.1.0] - 2026-03-16

### Added

- Initial open-source release of the `github-master` skill for Codex and Claude Code.
- Repo preflight automation for branch, version, release, changelog, and CI detection.
- Research-backed guidance for small teams working from a live `main` branch.
- Local installation sync for `~/.codex/skills` and `~/.claude/skills`.
- Repository-level pull request template, CI validation workflow, and CODEOWNERS.
