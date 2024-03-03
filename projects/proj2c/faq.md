---
layout: page
title: "FAQ - Project 2C"
nav_order: 0
parent: >-
  Project 2C: Ngordnet Enhancements
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 2C FAQ.
released: true
---

## Setup

### I'm getting an error that `spark failed to ignite`.

This may indicate that some other process is already using Spark and hasn't been terminated. Restarting your computer should fix this.

### I have a divergent branches error after trying the command `git pull`.

Run `git config pull.rebase false` and pull again.

### I'm getting 'Cannot invoke "ngordnet.ngrams.TimeSeries.years()" because "ILILILILIILILIILILIILIL" is null'

Re-pull the libraries in `library-sp24`.

### I tried running `git pull` from `library-sp24` but am still getting the above exception.

Be sure you've re-imported the libraries in IntelliJ after getting the new library files.

### No matter what I do, the libraries still aren't working!

Try deleting the `library-sp24` entirely and re-cloning it.

### I'm getting `Failed to bind to /0.0.0.0:4567` when running `Main.java`.

Save your code and restart IntelliJ. If this doesn't work, try restarting your computer as well.

## HyponymsHandler - k > 0

### How do I tiebreak words with the same counts?

It doesn't matter for this project - any behavior is acceptable. This means you can break ties alphabetically, or randomly, or not at all!

### How should I store total popularity of words?

Think about what you have implemented in Proj 2A. `TimeSeries` values are doubles, not ints. If you store the integer counts, you might get integer overflow.

![image](./cheesememe.png)

