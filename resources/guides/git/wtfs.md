---
layout: page
title: "Git WTFS"
categories: guides
author: Gilbert Ghang, Josh Hug
parent: Using Git
has_children: false
released: true
---

This document is intended to help you through frequently encountered weird
technical failure scenarios (WTFS) in Git. It will be populated as questions
arise.

## fatal: refusing to merge unrelated histories

This usually happens when someone has changed the skeleton code after you've
pulled from it. Pull with `--allow-unrelated-histories`, i.e.

```console
$ git pull skeleton main --allow-unrelated-histories
```

You may need to [resolve some resulting merge conflicts](#what-are-all-these-symbols-in-my-code).

or, if you're pulling from your own s\*\*\* student repo (on a different computer
for example),

```console
$ git pull origin main --allow-unrelated-histories
```

## HEAD detached at [...] ??

**NOTE:** _As of the FA23 iteration of the course, this failure scenario should
be much less common due to the preferred_ `git restore`.

```console
$ git status
HEAD detached at 1193e06
Untracked files:
  (use "git add <file>..." to include in what will be commited)

        ../seitan/

nothing added to commit but untracked files preset (use "git add" to track)
```

Chances are, you've probably used the `git checkout` command without specifying
a file (or a directory). That's OK! If you haven't made any changes, you can
fix this by using the command `git switch main`. If everything is OK, you
should a message similar to this:

```console
$ git switch main
Previous HEAD position was b405852... added tofu recipes
Switched to branch 'main'
```

If you have made some changes (i.e. using the command `git status` tells you
that you have modified some file(s) like the image below), there are a few
more steps to take.

```console
$ git status
HEAD detached at 1193e06
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

        modified: kung_pao_tofu.txt

Untracked files:
  (use "git add <file>..." to include in what will be commited)

        ../seitan/

no changes added to commit (use "git add" and/or "git commit -a")
```

First, use the command `git stash`. Your modifications may have magically
disappeared! Don't worry - we'll be able to retrieve them in a second!

```console
$ git stash
Saved working directory and index state WIP on (no branch): 1193e06 added tofu
recipes HEAD is now at 1193e06 added tofu recipes

$ git status
HEAD detached at 1193e06
Untracked files:
  (use "git add <file>..." to include in what will be commited)

        ../seitan/

nothing added to commit but untracked files preset (use "git add" to track)
```

From here, use the command `git switch main`. You should see the all clear
message from before:

```console
$ git switch main
Previous HEAD position was b405852... added tofu recipes
Switched to branch 'main'
```

Almost done! Let's go get our changes. Use `git stash pop`. But wait, we've got
a conflict! (This may not always occur. If you don't get a conflict, you should
be good to go from here.)

```console
$ git stash pop
Auto-merging tofu/kung_pao_tofu.txt
CONFLICT (content): Merge conflict in tofu/kung_pao_tofu.txt

$ git status
On branch main
Unmerged paths:
  (use "git reset HEAD <file>..." to unstage)
  (use "git add <file>..." to mark resolution)

        both modified: kung_pao_tofu.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        ../seitan/

no changes added to commit (use "git add" and/or "git commit -a")
```

Now use `git stash drop`:

```console
$ git stash drop
Dropped refs/stash@{0} (57f0ac5c5480964cdf29a94ed6b87e38da823488)<Paste>
```

Now we've got to fix this merge conflict. To learn how, take a look
[here](#what-are-all-these-symbols-in-my-code)!

## Error: failed to push some refs??

Sometimes when working with others, you'll get a message like this when you push:

```console
$ git push origin main
To https://github.com/gilbertghang/recipes.git
 ! [rejected]     main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/gilbertghang/recipes.git"
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

What has happened here is that your remote (i.e. your online Github repository)
contains commits that your local repository does not have. Luckily, Git is very
good about telling you how to fix these errors: if you read the error message
carefully, you'll see that is suggests that you `git pull`. Do that, fix any
[merge conflicts](#what-are-all-these-symbols-in-my-code), and push. Done!

## What are all these >>>> symbols in my code??

Sometimes when you pull from a repository, you'll get a message like this when you pull:

```console
$ git pull origin main
From github.com:Berkeley-CS61B/course-materials-sp16
 * branch            main     -> FETCH_HEAD
Auto-merging proj/proj0/solution/canonical/Planet.java
CONFLICT (content): Merge conflict in proj/proj0/solution/canonical/Planet.java
Automatic merge failed; fix conflicts and then commit the result.
```

The problem here is that the code on your computer had a conflict with the code
in the remote repository you're pulling from, and Git couldn't figure out how
to resolve it. Since it is unsure, Git refuses to overwrite your local code.

However, when you open your Planet.java, you see some kind of crazy garbage
like:

```java
    public Planet(Planet p) {
<<<<<<< HEAD
        this.xPos = p.xPos;
        this.yPos = p.yPos;
=======
        this.xxPos = p.xxPos;
        this.yyPos = p.yyPos;
>>>>>>> 27ddd0c71515e5cfc7f58a43bcf0e2144c127aed
```

This is a good thing! Everything between `<<<<<<< HEAD` and `=======` is what
was on your computer, and everything between `=======` and
`27ddd0c71515e5cfc7f58a43bcf0e2144c127aed` is what was on the remote server.

Your job is to look for these and resolve the merge conflict yourself. In this
case, the remote repository is right, so we simply delete out everything
between `<<<<<<< HEAD` and `=======`, and also delete the
`>>>>>>> 27ddd0c71515e5cfc7f58a43bcf0e2144c127aed` marker, leaving:

```java
public Planet(Planet p) {
    this.xxPos = p.xxPos;
    this.yyPos = p.yyPos;
```

Once you've resolved all of your merge conflicts, add all the files you
manually edited, and commit them as usual, e.g.

```console
git add Planet.java
git commit -m "resolved merge conflict"
git push origin main
```

## error: You have not concluded your merge (MERGE_HEAD exists).

If you see a message like this:

```
error: You have not concluded your merge (MERGE_HEAD exists).
hint: Please, commit your changes before merging.
fatal: Exiting because of unfinished merge.
```

Add and commit your current changes, and then pull again.

If, after pulling again, your terminal shows a message like "Please enter a commit message to explain why this merge is necessary," see the section directly after this one.

## Please enter a commit message to explain why this merge is necessary

If you see a message like this:

```
Merge branch 'main' of https://github.com/Berkeley-CS61B/skeleton-{{ site.semester }}
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
```

Git has opened a terminal text editor for you to enter a commit message. You can leave the default commit message and exit the text editor.

If you see something similar to this at the bottom of your terminal:

```
^G Get Help      ^O WriteOut      ^R Read File      ^Y Prev Pg      ^C Cur Pos
```

This indicates you're using the Nano text editor. To quit, type Ctrl+X (both keys at the same time).

If you see a bunch of tildes (`~` symbols) along the left side of your terminal, and you see something similar to this at the bottom of your terminal:

```
".git/COMMIT_EDITMSG" 9L, 273C      13,1      All
```

This indicates you're using the Vim text editor. To save and quit, type `:wq` - the colon key, then the letter `w`, then the letter `q`, one after the other (not all at the same time).

## fatal: 'skeleton' does not appear to be a git repository

If you see a message like this:

```
fatal: 'skeleton' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights and the repository exists.
```

Git might be having trouble finding where the skeleton repo is.

Try running `git remote -v`. If your repo is set up correctly, you should see:

```
origin  git@github.com:Berkeley-CS61B/{{ site.semester }}-s*** (fetch)
origin  git@github.com:Berkeley-CS61B/{{ site.semester }}-s*** (push)
skeleton  https://github.com/Berkeley-CS61B/skeleton-{{ site.semester }}.git (fetch)
skeleton  https://github.com/Berkeley-CS61B/skeleton-{{ site.semester }}.git (push)
```

If you only see the two lines corresponding to `origin`, and not the two lines corresponding to `skeleton`, then Git doesn't know where to find the skeleton repo.

To fix this, run:

```
git remote add skeleton https://github.com/Berkeley-CS61B/skeleton-{{ site.semester }}.git
```

Then, run `git remote -v` again and ensure that you see two lines corresponding to `origin` and two lines corresponding to `skeleton`.
