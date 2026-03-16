# VALIDATOR Report

## Validation Report

### Commands

- `bash -n scripts/install-skill-locally.sh`
- `python3 .agents/skills/github-master/scripts/repo_preflight.py --path . --task "Create an open-source GitHub governance skill for Codex and Claude Code, with local installation, README, changelog, CI, and collaboration rules."`
- `./scripts/install-skill-locally.sh`
- `./scripts/install-skill-locally.sh --dry-run`
- `find ~/.codex/skills/github-master -maxdepth 3 -type f`
- `find ~/.claude/skills/github-master -maxdepth 3 -type f`

### Results

- Installer shell syntax: pass
- Repo preflight execution: pass
- Local install into `~/.codex/skills/github-master`: pass
- Local install into `~/.claude/skills/github-master`: pass
- Installed skill file presence in both targets: pass

### Failures

- None

### Reproduction

Run:

```bash
bash -n scripts/install-skill-locally.sh
python3 .agents/skills/github-master/scripts/repo_preflight.py --path . --task "Describe the GitHub task"
./scripts/install-skill-locally.sh --dry-run
./scripts/install-skill-locally.sh
```
