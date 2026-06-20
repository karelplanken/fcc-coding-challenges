# Git Workflow

The core pattern is feature branch &rarr; PR &rarr; squash merge &rarr; sync `main` &rarr; new
branch. This is clean and professional.

---

## The Full Workflow

**Create remote GitHub repo and link local**
```bash
gh repo create <repo-name> <--private/--public>
git remote add origin git@github_ssh_connection:karelplanken/<repo-name>.git
git push -u origin main
```

**One-time setup:**
```bash
git switch -c chore/initial-commit
git add -A
git commit -m "chore: add 202 freeCodeCamp Python challenge solutions"
git push origin chore/initial-commit
gh pr create \
  --title "chore: initial commit of 202 past challenges" \
  --body "Adds all 202 completed freeCodeCamp Python coding challenges." \
  --base main
gh pr view --web
gh pr merge --squash --delete-branch
```

> `gh pr merge --squash --delete-branch` squash-merges the PR, fast-forwards
> local `main` to match `origin/main`, switches to `main`, and deletes both the
> local and remote feature branch. No further sync needed.

**Monthly branch (start of each month):**
```bash
git switch -c chore/cc-<month>-<year>
```

**Daily workflow:**
```bash
# after solving the day's challenge
git add challenges/<number>_<title>.py
git commit -m "chore: challenge <number> - <title>"
git push origin chore/cc-<month>-<year>
```

---

## Rebase Monthly Branch After `main` Was Updated Elsewhere

Use this when another branch (for example, `feature/*`, `fix/*`, or `chore/*`)
was merged into `main` while you were still working on
`chore/cc-<month>-<year>`.

```bash
git switch chore/cc-<month>-<year>
git fetch origin
git rebase origin/main

# if this branch was already pushed before rebasing:
git push --force-with-lease
```

If conflicts appear, resolve them and continue with:

```bash
git rebase --continue
```

**End of month merge:**
```bash
gh pr create \
  --title "chore: <month> <year> challenges (<number start>–<number end>)" \
  --body "Daily freeCodeCamp Python solutions for April 2026." \
  --base main
gh pr view --web
gh pr merge --squash --delete-branch
git switch -c chore/cc-<month>-<year>
```

---

## Working with a Recurring Branch (e.g. `chore/update-readme`)

Some branches are not tied to a month but to a recurring task — like keeping the
README up to date. There are two strategies: **re-use** the branch (never delete
it) or **re-create** it from scratch each time. Re-creating is simpler and
recommended.

### Re-create (recommended)

Use `--delete-branch` as usual. Both the local and remote branch are deleted
after the merge. When you need to update the README again, simply branch off
`main` fresh:

```bash
git switch -c chore/update-readme
```

Then work and merge as usual:

```bash
git add README.md
git commit -m "docs: update README"
git push origin chore/update-readme

gh pr create \
  --title "docs: update README" \
  --body "Updates README with latest info." \
  --base main
gh pr merge --squash --delete-branch
```

Clean, no history to worry about.

### Re-use

Omit `--delete-branch` so both the local and remote branch survive the merge.
When you come back to the branch, it will have stale commits that were already
squash-merged into `main`. Don't rebase — reset instead, which discards that old
history and brings the branch in line with `main`:

```bash
git switch chore/update-readme
git fetch origin
git reset --hard origin/main
```

Then work and merge — but **without** `--delete-branch`:

```bash
git add README.md
git commit -m "docs: update README"
git push --force-with-lease origin chore/update-readme

gh pr create \
  --title "docs: update README" \
  --body "Updates README with latest info." \
  --base main
gh pr merge --squash
```

Next time, start with the same reset:

```bash
git switch chore/update-readme
git fetch origin
git reset --hard origin/main
```

> **Note:** `git push --force-with-lease` is needed here because the reset
> rewrote the branch history that was already on the remote.

---

## Prune Stale Remote-Tracking References

Stale remote-tracking references are local leftovers. Clean them up with:

```bash
git fetch --prune
```

This syncs your local remote-tracking references with what actually exists on
GitHub, removing the ones that have been deleted. After that, `git branch -a`
should match what you see on GitHub.

You can also make this automatic with:

```bash
git config --global fetch.prune true
```

Then every `git fetch` or `git pull` will prune automatically.

---

## A Note on `--squash`

Squash merge is great for keeping `main` history clean (one commit per month).
But you lose the individual daily commits on `main`. That's fine here since the
daily granularity lives on the branch and in the PRs themselves. Stick with it.
