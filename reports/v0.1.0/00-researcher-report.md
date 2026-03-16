# RESEARCHER Report

## Topic

GitHub collaboration best practices for small teams with a live `main` branch and temporary work branches.

## Research Brief

### Facts

1. GitHub Flow is a lightweight branch-based workflow built around creating a branch, making isolated changes, opening a pull request, merging after approval, and deleting the branch.
2. GitHub recommends short, descriptive branch names and a separate branch for each unrelated change set.
3. Protected branches can require pull request reviews, status checks, conversation resolution, linear history, deployments, merge queue, push restrictions, and bypass restrictions.
4. Strict status checks require the branch to be up to date before merging.
5. CODEOWNERS can auto-request the right reviewers and can be required through branch protection.
6. Rulesets can layer with each other and with branch protection; the most restrictive rule applies.
7. Updating pull requests with base-branch changes helps catch problems before merge.
8. GitHub can automatically delete merged head branches.
9. GitHub lets maintainers enforce a single merge method by enabling only the desired option.
10. GitHub documents squash merge as a good way to streamline default-branch history, but warns about drawbacks for long-running branches.
11. GitHub documents that rebase-and-merge may require rebase plus force-push work on the topic branch before it becomes available.
12. GitHub says merge queue is particularly useful on busy branches with many pull requests from many users each day.

### Risks

- Direct pushes to `main` reduce review discipline.
- Long-running branches increase repeated conflicts and reduce squash-merge clarity.
- Force pushes can remove history other collaborators depend on.
- Missing review ownership on workflow or release files creates hidden risk.

### Assumptions

- Team size is usually two to four contributors.
- `main` is the deployment branch.
- Temporary branches are disposable after merge.

### Recommendation

Use GitHub Flow with:

- protected `main`
- pull-request-only merges
- one short-lived topic branch per task
- one approving review from someone else
- stale approval dismissal
- strict status checks
- conversation resolution
- linear history
- squash merge only
- automatic deletion of merged branches

The squash-only and no-merge-queue default is an inference from the official sources plus the stated team size and branch model.

### Sources

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Keeping your pull request in sync with the base branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch)
- [Managing the automatic deletion of branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches)
- [About merge methods on GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)
- [Managing and standardizing pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/managing-and-standardizing-pull-requests)
