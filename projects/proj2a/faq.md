---
layout: page
title: "FAQ - Project 2A"
nav_order: 0
parent: >-
  Project 2A: Ngordnet (NGrams)
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 2A FAQ.
released: true
---

Course staff will continuously add to this page as you all ask questions about the project! If you have a question that
isn't answered here, ask in lab, OH, or on Ed!

### Calling `.years()` in a loop

This might cause errors, please considner not calling `.years()` in a loop.

### I'm getting `SLF4J: No SLF4J providers were found.` error, what should I do?

It is fine if you get this error. Your code will still run but if they want to make the error disappear then you should pull in `library-fa23` and reimport libraries.

## Setup

### I'm getting errors with imports e.g. `Cannot resolve symbol 'spark'`, but already selected the library-fa23 files in IntelliJ.

Per the spec: You should also go to the `library-fa23` folder and run `git pull` to make sure you have all the library
files you’ll need for this project. When adding libraries to your project, select ALL libraries in the `library-fa23`
directory (or, just import the directory as a whole).

You may need to select all the `.jar` files individually when importing (don't just select the entire folder).

### When I run main, I get a bunch of red lines as output, is something wrong?

Probably not—as long as the output says you successfully started the server, everything is working as expected.

## Getting Started

### How can I test the server component?

The best way is to simply make a small change, load the server, and see what happens when you press the button on the
website. If you have having issues with making the strings, consider printing them out in your "handle" methods.

### How should I account for if one year is absent in plus and divide?

For `plus`, just keep the fist year (basically add 0 to it). For `divide`, ignore the year (it should not be in your
output).

### All my methods in NGramMap are getting really long and tough to debug, what should I do?

According to the spec, most of the work in this class should be done in the constructor. That means your job in the
constructor is to parse the datafiles and get them into a nice form such that completing all the other methods will be
easy. This class should remind you of `PercolationStats` in hw2. The constructor does a lot of work and the methods are
relatively simple in comparison.

Also, don't forget to take advantage of abstractions. Remember the `plus` and `divide` methods you wrote for
a `TimeSeries`? You might find some use for them here. If you ever find yourself iterating through the entries of
a `TimeSeries`, ask youself if there is an easier way.

## Common Exceptions

### Why do I receive a `NumberFormatException` when parsing a string to an int?

Integers can only be so large/small in Java due to their underlying bit representation (you'll learn more about this in
61C!) If your string represents a number outside the valid integer range, a `NumberFormatException` is thrown. If you
anticipate storing large numbers, it may be better to use a `Double` instead, which can store a wider range of values.

### Replication of AG Test manually do not give the same results/expectations as AG gives, what is the problem?

This might be related to edge cases. The datasets might not match so the AG expectation and local results might not
match.

### Why do I get randomizedTest timeout errors while everything looks right?

Check your `plus` and `divideBy` methods. See if you have a nested for loop. You don't need to have 2 for statements to
have a nested for loop. Think about how you get **`years`** (by using which method) and see if you are calling any
method on top of that method to **`get`** the specific year.

## Some other possible errors and reminders:

- Bear in mind there is no complexity in handler methods. The complexity relis on `NGramMap`. Also remember to use
  correct method on your `NGramMap`.
- If you are seeing issues in handler methods, check formatting!
- Timeout might also be related to making many calls to `weightHistory` which is an expensive operation. You can take
  advantage of `weightHistory(word, startYear, endYear)`.

## Getting “Your submission failed to complete on the test suite [TEST NAME]. You’re most likely using too much memory” in Gradescope.
This might be related to a glitch on Gradescope’s backend. Please post on Ed if that happens.

## Failing locally, passing on Gradescope
It might be related to how you implement your while loop when you are reading the file. Consider using `isEmpty()` instead of `hasNextLine()` for your check.
