---
layout: page
title: >-
  FAQ
parent: >-
  Lab 02: Debugging (Part 1)
grand_parent: Labs
has_right_toc: true
released: true
---

## I'm getting merge conflicts after re-pulling the skeleton

First, add and commit your local changes so that `git status` reads that your working
tree is clean.

Then, refer to the [Git WTFs](../../resources/guides/git/wtfs.md) section on resolving merge
conflicts. You'll need to incorporate both your local changes (this likely
includes your `BombMain` passwords) and the bug fixes
from the skeleton.

After you've resolved the merge conflicts in the files, you'll need to re-add and commit them
to complete the merge.

Come into office hours or lab if you're unsure on what to do!

## There's a lot of red in my IntelliJ

First, be sure you've imported the libraries correctly. Refer back to step 5 of the
[Assignment Workflow](../../resources/guides/assignment-workflow/index.md#opening-in-intellij)
if you need a refresher on how to do this.

If that doesn't work, be sure that `src` is blue and `tests` is green. Refer to
the [IntelliJ WTFS](../../resources/guides/intellij/wtfs/index.md)
to mark your `src` and `tests` folders appropriately.
