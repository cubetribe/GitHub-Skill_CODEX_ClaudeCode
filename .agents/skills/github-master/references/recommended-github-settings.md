# Recommended GitHub Settings

These settings are the default baseline for small teams that deploy from a live `main` branch and keep feature branches temporary.

## Main branch

| Area | Recommendation | Why |
| --- | --- | --- |
| Branch protection | Enabled for `main` | `main` stays reviewable and stable |
| Pull requests before merge | Required | Avoid direct pushes to live |
| Approvals | 1 approving review from another person | Minimum useful collaboration gate for 2-4 people |
| Dismiss stale approvals | Enabled | New commits invalidate old approval context |
| Most recent push approval | Enabled when available | Ensures the last changes are reviewed by someone else |
| Conversation resolution | Required | No unresolved review threads at merge time |
| Status checks | Required | CI becomes a merge gate |
| Up-to-date before merge | Strict | Catch integration problems before merge |
| Linear history | Required | Keep `main` simple to inspect and revert |
| Merge method | Squash only | Best fit for short-lived topic branches |
| Auto-delete merged branches | Enabled | Prevent stale branch reuse |
| Force pushes to `main` | Disabled | Protect shared history |
| Deleting `main` | Disabled | Protect the live branch |
| Bypass protections | Disabled when the repo allows it | Admins should follow the same gate |

## Optional settings

| Setting | When to use it |
| --- | --- |
| CODEOWNERS required review | Use for workflows, infra, release, billing, auth, or security-sensitive paths |
| Rulesets | Use when multiple governance layers or org-wide visibility matter |
| Merge queue | Use only when the branch is busy with many pull requests per day |
| Deployments required before merge | Use when a staging deployment is a real gate in the delivery process |

## Notes

- If the repo uses signed commits as a hard requirement, review the merge-method implications before allowing rebase merges.
- If a repo truly needs long-running branches, revisit the squash-only default because GitHub documents downsides for repeated work on a branch after squash-merge.
