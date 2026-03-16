#!/usr/bin/env python3
"""Repository preflight checks for GitHub-governed work."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


def run_git(path: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=path,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def file_exists(path: Path, *parts: str) -> bool:
    return path.joinpath(*parts).exists()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def detect_base_branch(repo: Path, current_branch: str) -> str:
    origin_head = run_git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD")
    if origin_head.startswith("origin/"):
        return origin_head.split("/", 1)[1]

    remote_show = run_git(repo, "remote", "show", "origin")
    match = re.search(r"HEAD branch: ([^\n]+)", remote_show)
    if match:
        head_branch = match.group(1).strip()
        if head_branch and head_branch != "(unknown)":
            return head_branch

    for candidate in ("main", "master"):
        if run_git(repo, "show-ref", "--verify", f"refs/heads/{candidate}"):
            return candidate

    return "main (assumed)" if not current_branch else "main"


def detect_version(repo: Path) -> tuple[str, list[str]]:
    sources: list[str] = []

    package_json = repo / "package.json"
    if package_json.exists():
        try:
            version = json.loads(read_text(package_json)).get("version")
        except json.JSONDecodeError:
            version = None
        if version:
            sources.append("package.json")
            return str(version), sources

    pyproject = repo / "pyproject.toml"
    if pyproject.exists() and tomllib is not None:
        try:
            data = tomllib.loads(read_text(pyproject))
        except tomllib.TOMLDecodeError:
            data = {}
        project_version = data.get("project", {}).get("version")
        poetry_version = data.get("tool", {}).get("poetry", {}).get("version")
        version = project_version or poetry_version
        if version:
            sources.append("pyproject.toml")
            return str(version), sources

    cargo = repo / "Cargo.toml"
    if cargo.exists() and tomllib is not None:
        try:
            data = tomllib.loads(read_text(cargo))
        except tomllib.TOMLDecodeError:
            data = {}
        version = data.get("package", {}).get("version")
        if version:
            sources.append("Cargo.toml")
            return str(version), sources

    composer = repo / "composer.json"
    if composer.exists():
        try:
            version = json.loads(read_text(composer)).get("version")
        except json.JSONDecodeError:
            version = None
        if version:
            sources.append("composer.json")
            return str(version), sources

    version_file = repo / "VERSION"
    if version_file.exists():
        version = read_text(version_file).strip()
        if version:
            sources.append("VERSION")
            return version, sources

    manifest = repo / ".release-please-manifest.json"
    if manifest.exists():
        try:
            data = json.loads(read_text(manifest))
        except json.JSONDecodeError:
            data = {}
        root_version = data.get(".")
        if root_version:
            sources.append(".release-please-manifest.json")
            return str(root_version), sources

    return "not present", sources


def list_files(repo: Path, patterns: Iterable[str]) -> list[str]:
    results: set[str] = set()
    for pattern in patterns:
        for entry in repo.glob(pattern):
            if entry.is_file():
                results.add(str(entry.relative_to(repo)))
    return sorted(results)


def detect_release_workflow(repo: Path) -> str:
    workflow_files = list_files(repo, (".github/workflows/*.yml", ".github/workflows/*.yaml"))
    workflow_text = "\n".join(read_text(repo / name) for name in workflow_files)

    if file_exists(repo, ".release-please-manifest.json") or "release-please" in workflow_text:
        return "release-please"

    if file_exists(repo, ".changeset", "config.json"):
        return "changesets"

    if (
        file_exists(repo, ".releaserc")
        or file_exists(repo, ".releaserc.json")
        or file_exists(repo, ".releaserc.yml")
        or file_exists(repo, ".releaserc.yaml")
        or file_exists(repo, "release.config.js")
        or file_exists(repo, "release.config.cjs")
        or "semantic-release" in read_text(repo / "package.json")
        or "semantic-release" in workflow_text
    ):
        return "semantic-release"

    changelog_files = list_files(repo, ("CHANGELOG*", "HISTORY*"))
    if changelog_files:
        return "manual"

    return "unknown"


def classify_task(task: str) -> dict[str, str]:
    task_lc = task.lower()
    keyword_map = {
        "api": ("api", "endpoint", "rest", "graphql", "webhook"),
        "schema": ("schema", "migration", "database", "table", "prisma"),
        "cli": ("cli", "command", "flag", "argument", "subcommand"),
        "config": ("config", "setting", "env", "environment variable", "yaml", "toml"),
        "user_visible": ("ui", "ux", "readme", "docs", "behavior", "output", "visible"),
    }
    result: dict[str, str] = {}
    for key, keywords in keyword_map.items():
        result[key] = "likely" if any(word in task_lc for word in keywords) else "manual review required"
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run GitHub repo preflight checks.")
    parser.add_argument("--path", required=True, help="Repository path")
    parser.add_argument("--task", default="", help="User request summary for impact hints")
    args = parser.parse_args()

    repo = Path(args.path).expanduser().resolve()
    if not repo.exists():
        raise SystemExit(f"Repository path does not exist: {repo}")

    git_dir = repo / ".git"
    is_repo = git_dir.exists() or run_git(repo, "rev-parse", "--show-toplevel")
    current_branch = run_git(repo, "branch", "--show-current") if is_repo else "not a git repository"
    base_branch = detect_base_branch(repo, current_branch) if is_repo else "not present"
    current_version, version_sources = detect_version(repo)
    release_workflow = detect_release_workflow(repo)
    changelog_files = list_files(repo, ("CHANGELOG*", "HISTORY*"))
    version_files = list_files(
        repo,
        (
            "VERSION",
            "package.json",
            "pyproject.toml",
            "Cargo.toml",
            "composer.json",
            ".release-please-manifest.json",
        ),
    )
    ci_files = list_files(repo, (".github/workflows/*.yml", ".github/workflows/*.yaml"))
    impact_hints = classify_task(args.task)

    print("# Repo Preflight")
    print()
    print(f"- repository: `{repo}`")
    print(f"- current_branch: `{current_branch or 'not present'}`")
    print(f"- target_base_branch: `{base_branch}`")
    print(f"- current_version: `{current_version}`")
    print(f"- version_sources: `{', '.join(version_sources) if version_sources else 'not present'}`")
    print(f"- release_workflow: `{release_workflow}`")
    print(f"- changelog_files: `{', '.join(changelog_files) if changelog_files else 'not present'}`")
    print(f"- version_files: `{', '.join(version_files) if version_files else 'not present'}`")
    print(f"- ci_workflows: `{', '.join(ci_files) if ci_files else 'not present'}`")
    print("- contract_impact_hints:")
    print(f"  - api: `{impact_hints['api']}`")
    print(f"  - schema: `{impact_hints['schema']}`")
    print(f"  - cli: `{impact_hints['cli']}`")
    print(f"  - config: `{impact_hints['config']}`")
    print(f"  - user_visible: `{impact_hints['user_visible']}`")
    print()
    print("Manual review is still required for contract impact before editing.")


if __name__ == "__main__":
    main()
