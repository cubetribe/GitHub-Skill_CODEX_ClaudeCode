#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/.agents/skills/github-master"
DRY_RUN=false
INSTALL_CODEX=true
INSTALL_CLAUDE=true

for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=true
      ;;
    --codex-only)
      INSTALL_CLAUDE=false
      ;;
    --claude-only)
      INSTALL_CODEX=false
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 1
      ;;
  esac
done

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "Skill source not found: ${SOURCE_DIR}" >&2
  exit 1
fi

install_target() {
  local label="$1"
  local target="$2"

  if [[ "${DRY_RUN}" == "true" ]]; then
    echo "[dry-run] ${label}: ${SOURCE_DIR} -> ${target}"
    return 0
  fi

  mkdir -p "$(dirname "${target}")"
  mkdir -p "${target}"
  rsync -a --delete "${SOURCE_DIR}/" "${target}/"
  echo "[ok] ${label}: ${target}"
}

if [[ "${INSTALL_CODEX}" == "true" ]]; then
  install_target "Codex" "${HOME}/.codex/skills/github-master"
fi

if [[ "${INSTALL_CLAUDE}" == "true" ]]; then
  install_target "Claude Code" "${HOME}/.claude/skills/github-master"
fi
