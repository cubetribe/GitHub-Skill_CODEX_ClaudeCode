# GitHub Best Practices for Small Teams

Date: 2026-03-16

## Facts

1. GitHub Flow is a lightweight, branch-based workflow: create a branch, make isolated changes, open a pull request, merge after review, and delete the branch.
2. GitHub recommends short, descriptive branch names and a separate branch for each unrelated change set.
3. Protected branches can require pull request reviews, status checks, conversation resolution, linear history, deployments, merge queue, push restrictions, and bypass restrictions.
4. Required status checks can be strict. Strict checks require branches to be up to date before merging.
5. CODEOWNERS automatically request review from responsible people or teams and can be required through branch protection.
6. Rulesets can layer with each other and with branch protection rules. The most restrictive version of a rule applies.
7. Updating a pull request branch with the latest base-branch changes helps catch problems before merge.
8. GitHub can automatically delete merged head branches.
9. GitHub lets a repository enforce a single merge method by enabling only the desired method.
10. Squash merging keeps the default branch history streamlined, but it is a poor fit for long-running branches.
11. Rebase-and-merge can require rebasing and force-pushing on the topic branch before it is available, which increases coordination risk.
12. Merge queue is especially useful on busy branches with many pull requests from many users each day.

## Risks

- Direct pushes to `main` bypass structured review.
- Long-running branches make squash history less useful and increase repeated conflict resolution.
- Force pushes can remove commits other collaborators based work on and can corrupt pull requests.
- Missing CODEOWNERS on critical files weakens review ownership.
- Loose status checks lower friction but raise the chance of incompatible changes landing on `main`.

## Assumptions

- Team size is usually two to four contributors.
- `main` is the production or deployment branch.
- Non-`main` branches are temporary integration branches.
- The team values safety and clarity over preserving every work-in-progress commit on `main`.

## Recommendation

For this exact context, the best default is:

- GitHub Flow
- protected `main`
- one short-lived topic branch per task
- pull-request-only integration
- one approval from another person
- stale approval dismissal
- strict required status checks
- conversation resolution
- linear history
- squash merge only
- automatic deletion of merged branches

This recommendation is an inference from the sources below plus the stated team size and branch model.

## Sources

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) - retrieved 2026-03-16
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) - retrieved 2026-03-16
- [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) - retrieved 2026-03-16
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) - retrieved 2026-03-16
- [Keeping your pull request in sync with the base branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch) - retrieved 2026-03-16
- [Managing the automatic deletion of branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches) - retrieved 2026-03-16
- [About merge methods on GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github) - retrieved 2026-03-16
- [Managing and standardizing pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/managing-and-standardizing-pull-requests) - retrieved 2026-03-16
