---
layout: page
title: "FAQ - Project 3: BYOW"
nav_order: 0
parent: >-
    Project 3: BYOW
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
    Project 3 FAQ.
released: true
---

# Topics

- [Common Problems and Errors](#common-problems-and-errors)
- [Autograder Errors](#autograder-errors)
- [Custom World Features](#custom-world-features)

## Common Problems and Errors

### I can't get text to show up / My tile characters became weird / My HUD flickers!

See the [Common UI Problems](./ui_bugs.md) page. 

### Two instances of my class are saying they are not equal when they should be. Also, I set the instance of my class to be the key in a HashMap, but I can't find it when I try to access that key.

Make sure that if you create any classes, override the `.equals()` method AND the `.hashcode()` method. This will guarantee that two instances that are equal will have the same hashcode


### I'm not passing the test where the input is "lwsd".

We provided a valid input with a seed prior to calling lwsd. Likely, you're not handling persistence properly. Make sure to input the exact sequence of calls to replicate this functionality (edit configurations to call getWorldFromInput with a valid parameter, then call it again with "lwsd").

### I'm getting an `AccessControlException` - what do I do?

Be sure you're only creating / writing to _files_ (not _directories_). This means that you should only be writing to `CWD` in a file ending with `.txt`, for example — not any other folders or subfolders.

### I'm trying to implement `getWorldFromInput` but my world is not rendering when I'm running `Main.java`!

Make sure to temporarily call ter.renderFrame() (with your appropriate 2-D TETile array input) in getWorldFromInput - you must comment this method call out before submitting to the autograder. If you're using a separate class to generate random worlds, you can debug by creating a main method within that class and calling ter.renderFrame().

### How do I close my world after the input `:q`?

Call System.exit(0); You are allowed to System.exit(0), but you cannot use it in your getWorldFromInput method.

### What do I do if the input to `getWorldFromInput()` has extra characters after `:q`?

You do not need to worry about replay strings that contain multiple saves or characters after the save, i.e. "N5SDD:QD" is not considered a valid replay string.

## Autograder Errors

### Why is the 3A autograder saying "Could not initialize class edu.princeton.cs.algs4.StdDraw"?

Somewhere in your code, your `getWorldFromInput` method tries to use the `StdDraw` class which is not allowed. For example if you call `TERenderer.initialize()`, you are using `StdDraw`. No `StdDraw` window should open when you call `getWorldFromInput`. We've seen some students whose code only opens a `StdDraw` window for some seeds, so look very carefully.

### The autograder is getting a `NumberFormatException` caused by `Integer.parseInt`.

The `Random` class takes `long` as input, so the seeds we provide are too big to fit into an `int`. You need to use the `Long` class instead to parse the seed.

### The autograder is telling me my worlds are not distinct, even though I run the seeds locally, and the worlds appear visually different.

Check to see that every tile you use is represented by a distinct character. This is especially important if you create any new tiles.

### I am getting weird autograder messages that don't make sense with the internals of my code.

Make sure you are not changing TETile.java's `character` field or `character()` method.

### I'm getting "unreported exception `IOException` (or some other exception) must be caught or declared to be thrown" on the autograder, but my code works fine locally.

The autograder probably won't compile if you throw exceptions in your method signatures. Instead, use a try-catch block with the part of your code that throws the exception, then remove `throws` from your method signatures.

### The autograder seems to be exiting early, even when I don't have a bug in my code?

Make sure you are not calling `System.exit()`.

## Custom World Features

### I want to make a world where we can explore the outdoors or caves or something like that, not a bunch of rooms. What should I do?

That’s fine, you can just use the seed to create a starter house (with rooms and hallways) for your avatar that they can freely exit.

### Can I make a world, that supports scrolling or multiple levels (i.e. stairs)?

Sure. In this case, `getWorldFromInput` should return only the part of the world that is visible on the screen at the time that the last character in the replay string is entered.

### Can I add the ability for users to customize their character before creating a world?

Yes, but you'll need to create a fourth main menu option. Your project must support exactly the API described in this spec. That is, "N23123S" must always create a new world with the seed 23123, and must not ask for any additional input from the user.

### Do I need Main Menu for 3A Autograder or 3A Manual Checkoff?

No, we won't grade you on that.

### Can I resubmit 3A Checkoff form?

Yes. But if you resubmit after the deadline, that would not be valid.

### Are there any live checkoffs?

Yes, sign ups will be released on Ed at a later date.

### Would it be possible to get points back if we lost some points during 3A checkoff?

Yes, there will be some instructions about it later on in the 3C script!
