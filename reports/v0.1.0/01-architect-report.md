# ARCHITECT Report

## Architecture Spec

### Decision

Create a canonical, versioned skill inside the repository and distribute it to local tool directories through a dedicated installer.

### Impacted files

- `.agents/skills/github-master/**`
- `scripts/install-skill-locally.sh`
- `.github/**`
- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `CODEOWNERS`

### Interfaces

- Skill interface: `github-master`
- Local install targets:
  - `~/.codex/skills/github-master`
  - `~/.claude/skills/github-master`
- Repo preflight CLI:
  - `python3 .agents/skills/github-master/scripts/repo_preflight.py --path <repo> --task "<summary>"`

### Migrations

- No data migration required.
- Local skill installation is file sync only.

### Rollback risk

Low. The repository is new and empty. The only out-of-repo change is installation into local skill directories, which is isolated to the `github-master` folder.
