---
layout: page
title: >-
    Lab 100: Git
has_children: false
parent: Labs
has_toc: false
has_right_toc: false
nav_exclude: true
toc_exclude: true
released: false
---

### Task: Git Exercise

Now you're ready to start using git! Your next task is to work through a small
git workflow by setting up a repository and making a couple commits. At the end,
you will need to be checked off by filling out the form linked on Beacon.

{: .info}
> If you need help with creating directories, creating files, changing
> directories, etc., refer back to [_How to Use the Terminal_](terminal.md). 
>
> **As a quick recap, you may find the git commands we just covered useful: 

1.  Create a directory called `lab04-checkoff`. You can put this directory
    anywhere on your computer (unless you have already cloned your `{{ site.semester }}-s***`
    repository, in which case, you **should not put this directory inside
    your `{{ site.semester }}-s***` repo)**.
2.  Move into the `lab04-checkoff` directory, and initialize a git repository.
3.  Create a file called `61b.txt` in any way you'd like. In this text file,
    add the text "Created 61b.txt".
4.  Create another file called `61boba.txt` in any way you'd like. In this text file,
    add the text "Created 61boba.txt".
5.  Begin tracking **only** `61b.txt`, and create a new commit containing just
    this file, with the following commit message: `Add 61b.txt`.
6.  Make a modification in `61b.txt` by changing the text in the file to: "61b.txt
    changed to version 2".
7.  Make another commit, this time containing both `61b.txt` and `61boba.txt`.
    The commit message should be: `Updated 61b.txt and added 61boba.txt`.
8.  Make one more modification to `61b.txt` by changing the text in
    the file to: "61b.txt changed to final version". **Don’t commit this version.**

    At this point, if you were to type in `git status` and `git log`, you'd see
    something similar to the following:

    ![Git Checkoff](img/git_checkoff.png){: style="max-height: 200;" }

9.  **Using git only**, restore `61b.txt` to the version in the most recent
    commit.
    <!-- markdownlint-disable MD030 -->
10. **Using git only**, restore `61b.txt` to the version in the first commit.

<!-- markdownlint-restore -->

Be sure to save this repository and directory until you complete the
asynchronous checkoff form on [Beacon]({{ site.links.beacon }}) and
obtain a **magic word**. Place this magic word on the **first line**
of `magic_word.txt`.

{: .task}
Do the steps above, then get checked off by filling out the Beacon
form.