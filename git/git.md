# Git Tutorial

A complete, hands-on reference for Git and GitHub. Every section includes runnable commands — open a terminal and follow along.

## Table of Contents

**Git Basics**
1. [Git Intro](#1-git-intro)
2. [Git Install](#2-git-install)
3. [Git Config](#3-git-config)
4. [Git Get Started](#4-git-get-started)
5. [Git New Files](#5-git-new-files)
6. [Git Staging](#6-git-staging)
7. [Git Commit](#7-git-commit)
8. [Git Tagging](#8-git-tagging)
9. [Git Stash](#9-git-stash)
10. [Git History](#10-git-history)
11. [Git Help](#11-git-help)
12. [Git Branch](#12-git-branch)
13. [Git Merge](#13-git-merge)
14. [Git Workflow](#14-git-workflow)
15. [Git Best Practices](#15-git-best-practices)
16. [Git Glossary](#16-git-glossary)

**Git and GitHub**
17. [GitHub Get Started](#17-github-get-started)
18. [Git — What is SSH?](#18-git--what-is-ssh)
19. [GitHub Add SSH](#19-github-add-ssh)
20. [GitHub Set Remote](#20-github-set-remote)
21. [GitHub Edit Code](#21-github-edit-code)
22. [Pull from GitHub](#22-pull-from-github)
23. [Push to GitHub](#23-push-to-github)
24. [GitHub Branch](#24-github-branch)
25. [Pull Branch from GitHub](#25-pull-branch-from-github)
26. [Push Branch to GitHub](#26-push-branch-to-github)
27. [GitHub Flow](#27-github-flow)
28. [GitHub Pages](#28-github-pages)
29. [Git GUI Clients](#29-git-gui-clients)

**Git Contribute**
30. [GitHub Fork](#30-github-fork)
31. [Git Clone from GitHub](#31-git-clone-from-github)
32. [GitHub Send Pull Request](#32-github-send-pull-request)

**Git Undo**
33. [Git Revert](#33-git-revert)
34. [Git Reset](#34-git-reset)
35. [Git Amend](#35-git-amend)
36. [Git Rebase](#36-git-rebase)
37. [Git Reflog](#37-git-reflog)
38. [Git Recovery](#38-git-recovery)

**Git Advanced**
39. [Git .gitignore](#39-git-gitignore)
40. [Git .gitattributes](#40-git-gitattributes)
41. [Git Large File Storage (LFS)](#41-git-large-file-storage-lfs)
42. [Git Signing Commits/Tags](#42-git-signing-commitstags)
43. [Git Cherry-pick & Patch](#43-git-cherry-pick--patch)
44. [Git Merge Conflicts](#44-git-merge-conflicts)
45. [Git CI/CD](#45-git-cicd)
46. [Git Hooks](#46-git-hooks)
47. [Git Submodules](#47-git-submodules)
48. [Git Remote Advanced](#48-git-remote-advanced)

**Extras**
49. [Git Aliases](#49-git-aliases)
50. [Git Bisect](#50-git-bisect)
51. [Git Worktree](#51-git-worktree)
52. [Git Cheat Sheet](#52-git-cheat-sheet)

---

## 1. Git Intro

Git is a **distributed version control system (DVCS)**: it tracks changes to files over time so you can recall specific versions later, collaborate without overwriting each other's work, and branch off to try things safely.

- **Distributed** — every clone of a repository is a full copy, including the entire history. There's no single point of failure.
- **Snapshots, not diffs** — conceptually, Git stores a snapshot of the whole project at each commit (though it optimizes storage internally), not just a list of file changes.
- **Local-first** — most operations (commit, diff, log, branch) happen entirely on your machine; no network needed.
- **Git vs. GitHub** — Git is the version control *tool*. GitHub (like GitLab or Bitbucket) is a *hosting service* for Git repositories, adding collaboration features (pull requests, issues, actions) on top.

## 2. Git Install

### macOS
```bash
brew install git
# or, trigger the Xcode Command Line Tools installer
git --version
```

### Windows
Download and run the installer from [git-scm.com](https://git-scm.com/download/win) (installs Git Bash too), or via a package manager:
```powershell
winget install --id Git.Git -e
```

### Linux
```bash
sudo apt install git        # Debian/Ubuntu
sudo dnf install git        # Fedora
sudo pacman -S git          # Arch
```

### Verify
```bash
git --version
```

## 3. Git Config

Git config is layered at three scopes, each overriding the one before it:

| Scope | Flag | File |
|---|---|---|
| System | `--system` | `/etc/gitconfig` |
| Global (your user) | `--global` | `~/.gitconfig` |
| Local (this repo only) | `--local` (default) | `.git/config` |

```bash
# Identity — required before your first commit
git config --global user.name "Deepak Singh"
git config --global user.email "singh.deepak3559@gmail.com"

# Default branch name for new repos
git config --global init.defaultBranch main

# Default editor for commit messages
git config --global core.editor "code --wait"

# View effective config
git config --list
git config --list --show-origin   # also show which file each value came from

# View / set a single key
git config user.email
git config --local user.email "work@example.com"   # override for just this repo
```

## 4. Git Get Started

Two ways to start tracking a project with Git:

```bash
# A) Start a brand-new repository
mkdir my-project && cd my-project
git init                     # creates the .git/ directory
git status                   # check repo state at any time

# B) Get an existing repository
git clone https://github.com/user/repo.git
cd repo
```

`git status` is your most-used command — it tells you the current branch, staged/unstaged changes, and untracked files.

## 5. Git New Files

New files start out **untracked** — Git sees them but isn't following their history yet.

```bash
echo "# My Project" > README.md
git status
# Untracked files:
#   README.md
```

Untracked files are ignored by commits until you explicitly `git add` them (see Staging, next). This is intentional: it lets you create scratch files, build artifacts, or local config without Git nagging about them (combine with [.gitignore](#39-git-gitignore) for permanent exclusions).

## 6. Git Staging

The **staging area** (aka "the index") is a middle step between your working directory and a commit — it lets you build a commit out of exactly the changes you want, not just "everything that changed."

```bash
git add README.md            # stage one file
git add file1.txt file2.txt  # stage multiple files
git add .                    # stage everything in the current directory
git add -A                   # stage everything in the whole repo (incl. deletions)
git add -p                   # interactively stage specific hunks within a file

git status                   # staged changes show as "Changes to be committed"
git diff                     # unstaged changes (working dir vs. staging area)
git diff --staged            # staged changes (staging area vs. last commit)

git restore --staged file.txt   # unstage a file (keeps the edits)
```

## 7. Git Commit

A commit is a permanent, named snapshot of the staged changes, with metadata (author, timestamp, message, parent commit(s)).

```bash
git commit -m "Add README with project overview"

# Stage all tracked, modified files and commit in one step (skips new/untracked files)
git commit -am "Fix typo in config"

# Open your editor for a multi-line message (recommended for non-trivial changes)
git commit
```

**Good commit message style:**
```
Short summary in imperative mood, under ~50 chars

Optional longer body explaining *why*, wrapped at ~72 chars.
Focus on motivation and context — the diff already shows *what*
changed.
```

```bash
git log --oneline -5         # confirm your commit landed
```

## 8. Git Tagging

Tags mark specific commits as significant — most commonly, release points (`v1.0.0`).

```bash
# Lightweight tag — just a name pointing at a commit
git tag v1.0.0

# Annotated tag — recommended; stores tagger, date, and message (like a mini-commit)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag a past commit
git tag -a v0.9.0 <commit-hash> -m "Beta release"

git tag                      # list all tags
git tag -l "v1.*"            # filter by pattern
git show v1.0.0              # inspect a tag

# Tags aren't pushed by default
git push origin v1.0.0       # push a single tag
git push origin --tags       # push all tags

git tag -d v0.9.0                     # delete a local tag
git push origin --delete v0.9.0       # delete a remote tag
```

## 9. Git Stash

Stash lets you set aside uncommitted changes temporarily — e.g. to switch branches without committing half-finished work — and reapply them later.

```bash
git stash                    # stash tracked changes (staged + unstaged)
git stash -u                 # also stash untracked files
git stash push -m "wip: search filter"   # stash with a descriptive label

git stash list                # see all stashes, most recent first
git stash show -p stash@{0}   # preview the diff in a stash

git stash pop                 # reapply the latest stash AND remove it from the stash list
git stash apply                # reapply the latest stash but KEEP it in the list
git stash apply stash@{2}      # reapply a specific, older stash

git stash drop stash@{0}       # delete a specific stash without applying it
git stash clear                # delete ALL stashes
```

## 10. Git History

```bash
git log                              # full history, newest first
git log --oneline                     # one line per commit
git log --oneline --graph --all       # ASCII graph of all branches
git log -p -- path/to/file            # full diffs for commits touching a file
git log --author="Deepak"             # filter by author
git log --since="2 weeks ago"          # filter by date
git log -3                             # limit to 3 commits

git show <commit-hash>                 # full details + diff of one commit
git diff <commit1> <commit2>            # diff between two commits
git blame path/to/file                 # who last changed each line, and in which commit
```

## 11. Git Help

```bash
git help <command>       # full manual page, e.g. `git help commit`
git <command> --help     # same thing
git <command> -h         # short usage summary
git help -a               # list all available commands
git help -g               # list conceptual guides (e.g. "everyday", "workflows")
```

## 12. Git Branch

Branches are lightweight, movable pointers to commits — they let multiple lines of work (features, fixes, experiments) proceed independently.

```bash
git branch                      # list local branches (* marks current)
git branch -a                    # list local AND remote-tracking branches
git branch new-feature           # create a branch (doesn't switch to it)
git switch new-feature           # switch to it (modern command)
git checkout new-feature         # switch to it (classic command, still common)

git switch -c new-feature         # create AND switch in one step
git checkout -b new-feature        # same, classic syntax

git branch -m old-name new-name    # rename a branch
git branch -d new-feature           # delete a branch (safe: refuses if unmerged)
git branch -D new-feature           # force-delete (discards unmerged work — be careful)
```

## 13. Git Merge

Merging brings the changes from one branch into another.

```bash
git switch main
git merge new-feature
```

Two outcomes:
- **Fast-forward** — if `main` hasn't moved since `new-feature` branched off, Git just moves the `main` pointer forward. No merge commit.
- **Three-way merge** — if both branches have diverged, Git creates a new **merge commit** with two parents, combining both histories.

```bash
git merge --no-ff new-feature      # force a merge commit even if fast-forward is possible
                                    # (keeps feature branches visible in history)
git merge --abort                   # bail out of a merge that hit conflicts
```

See [Git Merge Conflicts](#44-git-merge-conflicts) for resolving conflicts, and [Git Rebase](#36-git-rebase) for the alternative, linear-history approach.

## 14. Git Workflow

A typical day-to-day loop:

```bash
git switch main
git pull                              # get the latest changes
git switch -c feature/login-page       # branch off for your work

# ... edit files ...
git add .
git commit -m "Add login form validation"

# ... repeat edit/add/commit as needed ...

git push -u origin feature/login-page   # push, set upstream tracking
# open a Pull Request on GitHub, get it reviewed, merge it
git switch main
git pull                                # sync the merged change back locally
git branch -d feature/login-page         # clean up
```

Common branching models:
- **Feature branching** — one branch per feature/fix, merged via PR (shown above). Simple and works for most teams.
- **Git Flow** — long-lived `main`/`develop` branches plus `feature/`, `release/`, `hotfix/` branches. More structure, better for scheduled releases.
- **Trunk-based development** — everyone commits small, frequent changes directly to `main` (often behind feature flags). Favors continuous delivery.

## 15. Git Best Practices

- **Commit often, in logical units.** Each commit should represent one coherent change that could stand alone.
- **Write meaningful messages.** Imperative mood ("Add", not "Added"), explain *why* not *what*.
- **Pull before you push** to minimize conflicts with others' work.
- **Use branches** for anything beyond a trivial fix — never develop features directly on `main`.
- **Don't commit secrets** (API keys, `.env` files, credentials) — use `.gitignore`, and rotate the secret immediately if one slips through (rewriting history doesn't fully undo exposure).
- **Don't commit generated/build artifacts** — check for a `.gitignore` template for your stack.
- **Review before committing**: `git diff --staged` catches accidental debug prints, stray files, etc.
- **Keep history readable**: prefer small, focused PRs over huge ones; squash noisy "wip" commits before merging if your workflow allows it.
- **Never force-push to shared branches** (`main`, `develop`) — only to your own feature branches, and only when you're sure no one else is using them.

## 16. Git Glossary

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project tracked by Git, including its full history (`.git/` directory). |
| **Working directory** | The actual files on disk that you edit. |
| **Staging area / index** | The intermediate area where changes are gathered before a commit. |
| **Commit** | A saved snapshot of the staged changes, with a unique hash. |
| **Branch** | A movable pointer to a commit; an independent line of development. |
| **HEAD** | A pointer to the commit your working directory currently reflects (usually via the current branch). |
| **Remote** | A version of the repository hosted elsewhere (e.g. GitHub), referenced by a name like `origin`. |
| **Clone** | A full local copy of a remote repository, including its history. |
| **Fork** | A personal copy of someone else's repository on the hosting service (GitHub). |
| **Merge** | Combining the changes from one branch into another. |
| **Rebase** | Replaying commits from one branch onto another, producing linear history. |
| **Conflict** | When Git can't automatically reconcile changes to the same lines and needs manual resolution. |
| **Tag** | A named pointer to a specific commit, typically used for releases. |
| **Stash** | Temporarily shelved, uncommitted changes. |
| **Upstream** | The remote branch a local branch is tracking (e.g. `origin/main`). |
| **Pull request (PR) / merge request (MR)** | A hosting-platform feature for proposing, reviewing, and merging changes from one branch/fork into another. |
| **SHA / commit hash** | The unique 40-character (or abbreviated 7-character) identifier of a commit. |

---

## 17. GitHub Get Started

1. Create an account at [github.com](https://github.com).
2. Create a new repository: **+** → **New repository** → name it, choose public/private, optionally add a README/`.gitignore`/license.
3. Connect it to a local repo (see [GitHub Set Remote](#20-github-set-remote)) or clone it directly (see [Git Clone from GitHub](#31-git-clone-from-github)).
4. Authenticate — GitHub requires either SSH keys (see next section) or a **Personal Access Token (PAT)** for HTTPS pushes; plain passwords no longer work over HTTPS.

## 18. Git — What is SSH?

**SSH (Secure Shell)** is a cryptographic protocol for secure communication over an untrusted network. Git can use it (`git@github.com:user/repo.git` URLs) to authenticate with a hosting service using a public/private **key pair** instead of a username and password every time.

- Your **private key** stays on your machine, never shared.
- Your **public key** is uploaded to GitHub — GitHub uses it to verify you own the matching private key on each connection.

## 19. GitHub Add SSH

```bash
# 1. Generate a new key pair (Ed25519 is the modern recommended algorithm)
ssh-keygen -t ed25519 -C "singh.deepak3559@gmail.com"
# press Enter to accept the default location (~/.ssh/id_ed25519), set a passphrase if you like

# 2. Start the ssh-agent and add your key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 3. Copy the public key
cat ~/.ssh/id_ed25519.pub
# (macOS shortcut: pbcopy < ~/.ssh/id_ed25519.pub)
```

4. On GitHub: **Settings → SSH and GPG keys → New SSH key**, paste the public key, save.

```bash
# 5. Test the connection
ssh -T git@github.com
# "Hi <username>! You've successfully authenticated..."
```

## 20. GitHub Set Remote

A **remote** is a named reference to another copy of the repository (usually hosted elsewhere).

```bash
git remote add origin git@github.com:user/repo.git    # SSH
git remote add origin https://github.com/user/repo.git # HTTPS

git remote -v                       # list remotes and their URLs
git remote show origin               # detailed info: branches, tracking status
git remote set-url origin git@github.com:user/repo.git  # change a remote's URL
git remote rename origin upstream    # rename a remote
git remote remove origin             # remove a remote
```

## 21. GitHub Edit Code

You can edit files directly on GitHub for quick fixes without cloning locally:
- Open a file → click the **pencil (edit)** icon → make changes → **Commit changes**, either directly to the current branch or as a new branch + pull request.
- Press `.` while browsing any GitHub repo to open a full **github.dev** VS Code editor in the browser.

For anything beyond a trivial edit, prefer cloning and working locally so you get linting, tests, and a real terminal.

## 22. Pull from GitHub

`git pull` fetches remote changes and merges (or rebases) them into your current branch. It's shorthand for `git fetch` + `git merge` (or `git rebase`, if configured).

```bash
git pull                        # pull the current branch from its tracked remote
git pull origin main             # explicit: pull the main branch from origin

git pull --rebase                # rebase your local commits on top instead of merging
                                  #   → keeps history linear, avoids extra merge commits

# Safer two-step version, when you want to inspect before integrating:
git fetch origin
git log origin/main..main         # preview what would come in
git merge origin/main
```

## 23. Push to GitHub

`git push` uploads your local commits to a remote branch.

```bash
git push origin main                 # push main to origin
git push -u origin feature/login       # push + set upstream tracking (only needed once per branch)
git push                               # after upstream is set, just this works

git push --force-with-lease            # force-push safely — fails if the remote has commits
                                        # you don't have locally (protects collaborators)
git push --force                        # force-push, overwrites remote unconditionally — risky, avoid on shared branches
```

## 24. GitHub Branch

Branches created locally aren't visible to collaborators until pushed.

```bash
git switch -c feature/dark-mode
# ... commit some work ...
git push -u origin feature/dark-mode
```

On GitHub, the new branch appears under the repo's **branches** dropdown, and GitHub will often prompt **"Compare & pull request"** automatically.

```bash
git ls-remote --heads origin        # list all branches that exist on the remote
```

## 25. Pull Branch from GitHub

To get a branch that a teammate pushed but you don't have locally:

```bash
git fetch origin                        # updates your remote-tracking branches (origin/*)
git switch feature/dark-mode             # Git auto-creates a local branch tracking origin/feature/dark-mode
# equivalent explicit form:
git switch -c feature/dark-mode origin/feature/dark-mode
```

## 26. Push Branch to GitHub

```bash
git push -u origin feature/dark-mode     # first push: creates the branch remotely, sets tracking
git push                                  # subsequent pushes on this branch
```

If the remote branch has moved ahead (someone else pushed to it), you'll need to `git pull` (or `fetch` + `rebase`/`merge`) before you can push again.

## 27. GitHub Flow

A lightweight, widely-used workflow built around `main` always being deployable:

1. Branch off `main` for any change: `git switch -c fix/nav-bug`.
2. Commit and push regularly.
3. Open a Pull Request early, even in draft — invites discussion.
4. Get it reviewed, run CI, address feedback.
5. Merge into `main` (often "squash and merge" for a clean history).
6. Deploy `main` — in a true GitHub Flow setup, every merge to `main` is deployable/deployed.
7. Delete the branch.

```bash
git switch main && git pull
git switch -c fix/nav-bug
# ... work, commit, push, open PR, review, merge on GitHub ...
git switch main && git pull
git branch -d fix/nav-bug
```

## 28. GitHub Pages

Free static-site hosting straight from a GitHub repository.

1. **Settings → Pages** on your repo.
2. Choose a source: a branch (e.g. `main` or a dedicated `gh-pages` branch) and folder (`/` or `/docs`).
3. GitHub builds and serves the site at `https://<username>.github.io/<repo>/` (or a custom domain via `CNAME`).

```bash
# Common pattern: a dedicated gh-pages branch for build output
git switch --orphan gh-pages          # branch with no history/parent
git commit --allow-empty -m "Init gh-pages"
git push -u origin gh-pages
```

Many projects instead automate this with a GitHub Actions workflow that builds and deploys on every push to `main` (see [Git CI/CD](#45-git-cicd)).

## 29. Git GUI Clients

Command line isn't mandatory — GUI clients cover the same operations visually:

- **GitHub Desktop** — simple, GitHub-focused, great for beginners.
- **GitKraken** — powerful visual branch graph, cross-platform.
- **Sourcetree** — free, feature-rich (Atlassian).
- **VS Code's built-in Source Control panel** (+ GitLens extension) — convenient if you already live in the editor.
- **`git gui`** / **`gitk`** — ship with Git itself; `gitk` is a handy history browser (`gitk --all`).

GUIs are great for reviewing diffs and visualizing branch topology; most developers still reach for the CLI for day-to-day staging/committing muscle memory.

---

## 30. GitHub Fork

A **fork** is your own personal copy of someone else's repository on GitHub — used when you don't have push access to the original ("upstream") repo.

1. On the repo's GitHub page, click **Fork**. GitHub creates `github.com/your-username/repo`.
2. Clone *your fork* locally (not the original):
```bash
git clone git@github.com:your-username/repo.git
cd repo
```
3. Add the original repo as a second remote, conventionally named `upstream`:
```bash
git remote add upstream git@github.com:original-owner/repo.git
git remote -v
# origin    -> your fork (read/write)
# upstream  -> original repo (read-only, for syncing)
```
4. Keep your fork in sync:
```bash
git fetch upstream
git switch main
git merge upstream/main       # or: git rebase upstream/main
git push origin main            # update your fork on GitHub
```

## 31. Git Clone from GitHub

```bash
git clone https://github.com/user/repo.git         # HTTPS
git clone git@github.com:user/repo.git              # SSH

git clone --branch develop https://github.com/user/repo.git   # clone a specific branch
git clone --depth 1 https://github.com/user/repo.git           # shallow clone: history-light, faster for CI/one-off use
```

Cloning automatically sets up the `origin` remote pointing at the source URL.

## 32. GitHub Send Pull Request

A **Pull Request (PR)** proposes merging changes from one branch (often on your fork) into another (usually `main` on the upstream repo).

```bash
git switch -c fix/typo
# ... make changes, commit ...
git push -u origin fix/typo
```

On GitHub: open your fork/branch → **Compare & pull request** → fill in a clear title and description (what changed, why, how to test) → **Create pull request**.

- Respond to review comments by pushing more commits to the same branch — the PR updates automatically.
- Once approved and checks pass, a maintainer (or you, if permitted) merges it.
- Afterwards, sync and clean up as shown in [GitHub Fork](#30-github-fork) and delete the now-merged branch.

---

## 33. Git Revert

Reverting creates a **new commit** that undoes the changes from a previous commit — history-safe, ideal for shared/public branches.

```bash
git revert <commit-hash>            # revert a single commit, opens editor for the message
git revert --no-edit <commit-hash>   # revert without prompting for a message
git revert HEAD                      # revert the most recent commit
git revert <oldest>..<newest>         # revert a range of commits (applies as separate reverts)
git revert -n <commit-hash>           # stage the revert without committing, so you can adjust first
```

Unlike `reset`, `revert` doesn't rewrite existing history — safe to use even after pushing.

## 34. Git Reset

Reset moves the current branch pointer (and optionally the staging area / working directory) to a different commit. **Rewrites history — avoid on commits already pushed/shared.**

```bash
git reset --soft <commit>    # move HEAD only; staged + working changes preserved as staged
git reset --mixed <commit>   # (default) move HEAD + unstage changes; working directory files untouched
git reset --hard <commit>    # move HEAD + unstage + DISCARD working directory changes — destructive

git reset HEAD~1              # undo the last commit, keep its changes staged (--mixed default)
git reset --soft HEAD~1        # undo the last commit, keep its changes staged AND ready to re-commit
git reset file.txt              # unstage a single file (same as `git restore --staged file.txt`)
```

> Before any `--hard` reset, double check with `git status`/`git stash` that you're not discarding work you want — it cannot be undone via normal means (though [Git Reflog](#37-git-reflog) can sometimes rescue it).

## 35. Git Amend

Amend replaces the most recent commit with a new one — combining new staged changes and/or a new message into it. **Rewrites history — only amend commits that haven't been pushed (or that you're sure no one else has pulled).**

```bash
git commit --amend -m "Corrected commit message"     # just fix the message

git add forgotten_file.txt
git commit --amend --no-edit                            # add changes, keep the same message

git commit --amend                                       # opens editor to edit the message too
```

If the original commit was already pushed, amending requires a force-push:
```bash
git push --force-with-lease
```

## 36. Git Rebase

Rebase replays your branch's commits on top of another branch's tip, producing a clean, linear history instead of a merge commit.

```bash
git switch feature
git rebase main
# Git replays each of feature's commits, one by one, on top of main's current tip
```

If conflicts arise partway through:
```bash
# fix the conflicted files, then:
git add <resolved-files>
git rebase --continue

git rebase --abort     # bail out entirely, back to pre-rebase state
git rebase --skip       # skip the current commit entirely (rare, use with care)
```

**Interactive rebase** — rewrite, reorder, squash, or drop commits before sharing them:
```bash
git rebase -i HEAD~3
# opens an editor listing the last 3 commits; change "pick" to:
#   reword — edit the message
#   squash / fixup — combine into the previous commit
#   drop — remove the commit entirely
#   edit — pause to amend that commit
```

**Golden rule:** never rebase commits that other people have already pulled/based work on — it rewrites their SHAs and creates a mess for collaborators. Rebase freely on your own not-yet-pushed (or not-yet-shared) branches.

## 37. Git Reflog

Every movement of `HEAD` — commits, resets, checkouts, rebases, amends — is logged locally in the **reflog**, even for commits no longer reachable from any branch. It's your safety net.

```bash
git reflog                       # e.g.:
# a1b2c3d HEAD@{0}: commit: Add search filter
# e4f5g6h HEAD@{1}: reset: moving to HEAD~1
# 7h8i9j0 HEAD@{2}: commit: Fix typo

git reflog show branch-name        # reflog for a specific branch

git checkout a1b2c3d                # jump to a "lost" commit found in the reflog
git branch recovered-work a1b2c3d    # create a branch there to keep it permanently
```

The reflog is local-only (not pushed/cloned) and entries eventually expire (default ~90 days for reachable, ~30 for unreachable) — but it covers almost any "oops" scenario for recent history.

## 38. Git Recovery

Practical recipes for common "I broke it" moments:

```bash
# Discard uncommitted changes to a file
git restore file.txt

# Discard ALL uncommitted changes in the working directory
git restore .

# Recover a deleted (but never-committed) file — nothing Git can do; it was never tracked.
# Recover a deleted file that WAS committed:
git checkout <commit-before-deletion> -- path/to/file.txt

# Recover after a bad `git reset --hard`
git reflog                      # find the commit hash from before the reset
git reset --hard <that-hash>

# Recover a deleted branch
git reflog                      # find a commit that was on the deleted branch
git branch recovered-branch <that-hash>

# Find "dangling" (unreferenced) commits directly, e.g. after a hard reset
git fsck --lost-found
```

---

## 39. Git .gitignore

A `.gitignore` file tells Git which untracked files/patterns to never stage automatically — build output, dependencies, secrets, OS/editor cruft.

```gitignore
# Dependencies
node_modules/
venv/

# Build output
dist/
*.pyc
__pycache__/

# Environment / secrets
.env
*.pem

# OS / editor
.DS_Store
.vscode/
*.swp
```

```bash
git status --ignored           # see what's currently being ignored

# .gitignore only affects UNTRACKED files. To stop tracking a file
# that's already committed (without deleting it from disk):
git rm --cached path/to/file
```

Browse [github.com/github/gitignore](https://github.com/github/gitignore) for ready-made templates per language/framework. Also useful: a **global** gitignore for personal, machine-wide junk (`git config --global core.excludesfile ~/.gitignore_global`).

## 40. Git .gitattributes

`.gitattributes` controls how Git handles specific paths — line endings, diff behavior, merge strategy, LFS routing.

```gitattributes
# Normalize line endings to LF in the repo, checkout as native OS line endings
* text=auto

# Force LF for shell scripts regardless of OS
*.sh text eol=lf

# Treat as binary (no diffing/merging attempts)
*.png binary
*.pdf binary

# Route large files through Git LFS (see next section)
*.psd filter=lfs diff=lfs merge=lfs -text

# Exclude from `git archive` exports
tests/fixtures/** export-ignore

# Custom diff driver, e.g. for Jupyter notebooks (pairs with a configured `git config diff.jupyternotebook.*`)
*.ipynb diff=jupyternotebook
```

## 41. Git Large File Storage (LFS)

Git stores full file history forever, which makes it a poor fit for large binaries (videos, datasets, design files) — every version bloats every clone. **Git LFS** replaces large files in the repo with small text pointers, storing the actual content on a separate LFS server.

```bash
# Install (once per machine)
brew install git-lfs      # or download from git-lfs.github.com
git lfs install

# In a repo: tell LFS which patterns to manage
git lfs track "*.psd"
git lfs track "*.mp4"
git add .gitattributes      # the tracking rules live here — commit this file

git add design.psd
git commit -m "Add hero design file"
git push

git lfs ls-files             # list files currently tracked by LFS
```

Collaborators need `git lfs install` too (usually a one-time setup) — otherwise they'll only see the pointer files.

## 42. Git Signing Commits/Tags

Signing proves a commit/tag genuinely came from you (via GPG or SSH signatures), shown as "Verified" on GitHub.

```bash
# GPG-based signing
gpg --full-generate-key                       # create a key if you don't have one
gpg --list-secret-keys --keyid-format=long      # find your key ID
git config --global user.signingkey <KEY_ID>
git config --global commit.gpgsign true          # sign every commit automatically

# Add the public key to GitHub: Settings -> SSH and GPG keys -> New GPG key
gpg --armor --export <KEY_ID>                    # copy this output to GitHub

git commit -S -m "Signed commit"                 # sign a single commit manually
git tag -s v1.0.0 -m "Signed release"              # signed tag

git log --show-signature -1                        # verify a signature locally
```

```bash
# SSH-based signing (simpler if you already have an SSH key for GitHub)
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

## 43. Git Cherry-pick & Patch

**Cherry-pick** applies one specific commit from another branch onto your current branch — useful for backporting a fix without merging the whole branch.

```bash
git cherry-pick <commit-hash>
git cherry-pick <hash1> <hash2>           # multiple commits
git cherry-pick <hash1>^..<hash3>          # a range (inclusive of hash1)
git cherry-pick -n <commit-hash>            # apply changes without committing (review first)
git cherry-pick --continue                   # after resolving a conflict mid-pick
git cherry-pick --abort
```

**Patches** — export commits as portable `.patch` files, e.g. to share a fix outside of Git (email, ticket attachment):
```bash
git format-patch -1 <commit-hash>            # creates 0001-<message>.patch
git format-patch main..feature                # one file per commit ahead of main

git apply changes.patch                        # apply a plain diff (no commit metadata)
git am 0001-fix-typo.patch                      # apply a format-patch file, preserving author/message as a real commit
```

## 44. Git Merge Conflicts

A conflict occurs when Git can't automatically reconcile changes to the same lines from two branches. Git pauses the merge/rebase and marks the file:

```
<<<<<<< HEAD
your current branch's version
=======
the incoming branch's version
>>>>>>> feature-branch
```

**Resolving:**
```bash
git status                     # lists all files with conflicts

# 1. Open each conflicted file, edit it to the correct final content,
#    removing the <<<<<<<, =======, >>>>>>> markers.
# 2. Mark it resolved:
git add resolved-file.txt

# 3. Finish the operation:
git commit                     # for a merge
git rebase --continue            # for a rebase

# Bail out entirely and return to the pre-conflict state:
git merge --abort
git rebase --abort
```

**Helpful tools:**
```bash
git diff                          # see the conflict markers in context
git mergetool                     # launch a configured visual merge tool
git checkout --ours file.txt       # take your version entirely for this file
git checkout --theirs file.txt      # take the incoming version entirely
```

**Avoiding conflicts:** pull/rebase frequently, keep branches short-lived, communicate with teammates working in the same files.

## 45. Git CI/CD

Continuous Integration / Continuous Deployment pipelines automatically build, test, and deploy code on Git events (push, PR, tag). On GitHub this is **GitHub Actions**, configured via YAML in `.github/workflows/`.

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
```

- **Triggers** (`on:`) — commonly `push`, `pull_request`, `schedule`, or `workflow_dispatch` (manual).
- **Branch protection rules** (Settings → Branches) can *require* checks like this to pass before a PR can merge, enforcing quality gates at the Git level.
- Other common CI/CD systems that integrate with Git the same way: GitLab CI (`.gitlab-ci.yml`), CircleCI, Jenkins, Travis CI.

## 46. Git Hooks

Hooks are scripts Git runs automatically at specific points in the workflow (commit, push, merge, etc.), stored in `.git/hooks/` — local-only, not versioned/shared by default.

```bash
ls .git/hooks/          # sample hooks ship with every repo, disabled by default (*.sample)
```

```bash
# .git/hooks/pre-commit  (make it executable: chmod +x .git/hooks/pre-commit)
#!/bin/sh
npm run lint || exit 1     # non-zero exit blocks the commit
```

Common hooks: `pre-commit` (lint/format before allowing a commit), `commit-msg` (enforce message format), `pre-push` (run tests before pushing), `post-merge` (e.g. auto-install dependencies after pulling).

Since `.git/hooks/` isn't committed, teams typically use a tool like **Husky** (JS) or **pre-commit** (Python) to version-control hook configuration and install it for every contributor automatically.

## 47. Git Submodules

Submodules let you embed one Git repository inside another as a subdirectory, pinned to a specific commit — useful for pulling in a dependency you also need to develop/version separately.

```bash
git submodule add https://github.com/user/library.git libs/library
git commit -m "Add library as a submodule"

# Cloning a repo WITH submodules
git clone --recurse-submodules https://github.com/user/repo.git

# If you already cloned without that flag:
git submodule init
git submodule update

# Pull the latest upstream changes into a submodule
cd libs/library
git pull origin main
cd ../..
git add libs/library
git commit -m "Update library submodule to latest"

# Shortcut to update all submodules to their pinned commits
git submodule update --init --recursive
```

Submodules have a reputation for being fiddly (easy to forget `--recurse-submodules`, easy to leave a submodule on the wrong commit) — many teams prefer package managers or **Git subtree** (`git subtree add/pull`, which merges the code directly, no separate `.git` pointer) where possible.

## 48. Git Remote Advanced

```bash
git remote -v                             # list remotes with URLs
git remote add upstream <url>              # multiple remotes (e.g. fork workflows)
git remote set-url origin <new-url>         # change a remote's URL
git remote set-url --push origin <url>       # different URL for push vs. fetch (e.g. read-only mirror)

git fetch --all                             # fetch from every configured remote
git fetch --prune                            # also remove local refs for branches deleted on the remote

git branch -vv                               # show each local branch's upstream + ahead/behind counts
git push origin --delete old-branch           # delete a remote branch
git remote prune origin                        # clean up stale remote-tracking branches locally

git push origin HEAD                            # push the current branch, whatever it's named, to its same-named remote branch
```

---

## 49. Git Aliases

Shortcuts for commands you type constantly:

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "restore --staged"

# Usage:
git st
git lg
```

Aliases live in `~/.gitconfig` under `[alias]` and can also be edited directly there.

## 50. Git Bisect

Binary search through history to find the exact commit that introduced a bug.

```bash
git bisect start
git bisect bad                      # current commit is broken
git bisect good v1.2.0               # this earlier tag/commit was known-good

# Git checks out a commit halfway between good and bad. Test it, then:
git bisect good     # if this commit works
git bisect bad       # if this commit is broken
# ... repeat; Git narrows the range each time ...
# eventually Git reports the exact first-bad commit

git bisect reset      # done — return to your original HEAD
```

```bash
# Automate it with a test script that exits 0 (good) or non-zero (bad)
git bisect start HEAD v1.2.0
git bisect run npm test
```

## 51. Git Worktree

Worktrees let you check out multiple branches into separate directories *simultaneously*, sharing the same `.git` history — no need to stash/switch when you want to work on two branches side by side (e.g. reviewing a PR while mid-feature).

```bash
git worktree add ../repo-hotfix hotfix/urgent-bug     # new worktree + branch, in a sibling directory
git worktree add ../repo-review existing-branch         # checkout an existing branch into a new worktree

git worktree list                                         # see all active worktrees
git worktree remove ../repo-hotfix                          # clean up when done
git worktree prune                                           # clean up stale worktree metadata
```

## 52. Git Cheat Sheet

| Task | Command |
|---|---|
| Initialize a repo | `git init` |
| Clone a repo | `git clone <url>` |
| Check status | `git status` |
| Stage changes | `git add <file>` / `git add .` |
| Commit | `git commit -m "message"` |
| View history | `git log --oneline --graph --all` |
| Create + switch branch | `git switch -c <branch>` |
| Switch branch | `git switch <branch>` |
| Merge a branch | `git merge <branch>` |
| Rebase onto a branch | `git rebase <branch>` |
| Fetch remote changes | `git fetch` |
| Pull (fetch + merge) | `git pull` |
| Push | `git push` |
| Undo uncommitted changes | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Undo last commit, keep changes | `git reset --soft HEAD~1` |
| Undo a pushed commit safely | `git revert <commit>` |
| Amend last commit | `git commit --amend` |
| Stash work in progress | `git stash` / `git stash pop` |
| Tag a release | `git tag -a v1.0.0 -m "msg"` |
| Cherry-pick a commit | `git cherry-pick <commit>` |
| Find a bug's origin commit | `git bisect start` |
| Recover "lost" work | `git reflog` |
| Compare two commits | `git diff <c1> <c2>` |
| See who changed a line | `git blame <file>` |
