---
layout: page
title: >-
  Homework 2: Percolation FAQ
nav_order: 1
parent: "Homework 2: Percolation"
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Homework 2 FAQ.
released: true
---

## FAQ

### What should `stddev()` return if T equals 1?

The sample standard deviation is undefined. We recommend returning Double.NaN but we will not test this case.

### After the system has percolated, `PercolationVisualizer` colors in light blue all sites connected to open sites on the bottom (in addition to those connected to open sites on the top). Is this "backwash" acceptable?

While allowing backwash does not strictly conform to the Percolation API, it requires quite a bit of ingenuity to fix and it leads to only a small deduction if you don't.

![percolation](images/percolation-backwash.png)

[//]: # "If you are well and truly stuck, you can read the [hints for solving backwash](hints.md)."

### How do I generate a site uniformly at random among all blocked sites for use in `PercolationStats`?

Pick a site at random (by using `StdRandom` or some other library to generate two integers between 0 (inclusive) and N (exclusive) and use this site if it is blocked; if not, repeat.

### I don't get reliable timing information in `PercolationStats` when N = 200. What should I do?

Increase the size of N (say to 400, 800, and 1600), until the mean running time exceeds its standard deviation.

### I'm failing the Chi Squared test but passing everything else.

The issue is that you're using the same random seed for multiple simulations, and the statistical test is catching the fact that they are the same.

If you look at the code for `StdRandom`, you'll see that it sets the seed just once (the first time `StdRandom` is used), which prevents this issue of seed reset. In short, don't set the seed yourself.

Alternately, make sure you're not generating biased random numbers. You should be using the `StdRandom` method that generates integers, not doubles.

### It's telling me that my code reports "false" for `percolates()` but when I run the visualizer I'm getting true!

The visualizer does a very specific sequence of `isOpen()`/`isFull()`/`percolates()` calls. Try creating your own test that only opens sites and then calls `percolates()`. Alternately, disable all `isOpen()` and/or `isFull()` calls in the visualizer so you can focus on the `percolates()` behavior. Alternately, pay close attention to the test labeled `Random Operation Order`.

### My code is compiling on my computer but not on the autograder.

Your code must obey the API exactly. You may not add additional public methods or variables to the `Percolation` class. When we test your `PercolationStats`, we use a reference version of Percolation instead of your version to avoid cascading errors -- which means you can't assume that any additional public methods are available.

### How do I choose which file to run? How do I pass command line/program arguments in IntelliJ?

First, navigate to Run -> Edit Configurations. You can set up different debugging clients here to run different classes as your "main class" (meaning that the program will start and end with the "main" function inside of your main class). You can set up a new client with the small + sign on the upper left side - for the purposes of this class, you'll only need to set up an Application. You can then name your configuration whatever you like, select the main class you want for that configuration, as well as set any command line/program arguments in the program arguments field. Input the program arguments into that field just like you would in the terminal - a single line with spaces separating the arguments.
