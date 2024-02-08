---
# layout: page
# title: "FAQ - Project 1B: Deques"
# categories: proj
# released: true
# searchable: false

layout: page
title: "FAQ - Project 1B: Array Deque 61B"
nav_order: 0
parent: >-
  Project 1B: ArrayDeque61B
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 1B FAQ.
released: true
---

### I'm sure I wrote tests for coverage, but I'm not attaining those flags on the grader!

There's a chance that when running your tests against the staff version of the code, we run into an assertion error. Make sure that all your assertion statements have the correct expected output! For instance, if you had code that called get(0) on an ArrayDeque61B with the elements 1, 2, 3, and asserted that the 0th element should be 2, any tests written after this incorrect test won't count in the test coverage.

### When I call .get(0) on my ArrayDeque61B, I'm returning items[0], but not getting back the item I expect. What is going on?

Keep in mind that the front item of your Deque isn't necessarily in position 0. For example, in the slides that provide
a
slides [which provide suggested approaches for project 1](https://docs.google.com/presentation/d/1XBJOht0xWz1tEvLuvOL4lOIaY0NSfArXAvqgkrx0zpc/edit#slide=id.g1094ff4355_0_450)
, I arbitrarily picked position 4 as the position where the front of the Deque starts.

### I'm getting a "Required Type is Deque but provided is ..."

There are two possible issues. Make sure you haven't accidentally imported java.util.\* (or java.util.LinkedList or
java.util.ArrayList). The other possible issue comes with an issue in your class signature.

### I keep seeing a "Cannot invoke java.lang.Integer.intValue() because the return value of \_\_\_ is null" error on Gradescope.

This NullPointerException is likely caused by your addFirst or addLast methods. To test this for LinkedListDeque61B, we
have given you a test called
`bigLLDeque61BTest()` that does 1,000,000 addLast operations, followed by 500,000 removeFirsts and 500,000 removeLasts. To
find the cause of this bug, try duplicating the test and doing 1,000,000 addFirst operations, as well as copying the
entire test and writing an identical version that tests ArrayDeque61B as well.


### I'm getting an API error asking me to remove or make my isEmpty() method private.

Currently our grader doesn't recognize an implementation of isEmpty within ArrayDeque61B or LinkedListDeque61B. Please follow
the spec and provide a default implementation within the Deque61B.java file.

### I can't get Java to create an array of generic objects!

Use the strange syntax, i.e. `T[] a = (T[]) new Object[1000];`. Here, `T` is a generic type, it's a placeholder for
other Object types like "String" or "Integer".

### When should my get() method return null? 
You should return null if the index is larger than the size of your ArrayDeque61B, not the underlying array. For instance, if your underlying array has size 8, but your ArrayDeque61B has only called add thrice, then there are only 3 items and any index beyond 2 is out of bounds

### What should `get()` return when there is nothing in the list? 

Return null!

### How do I handle overflow in the indices? 

Think about using the modulo operator!

### What should my toList() method do? 

Your toList method should return a list with the elements in ArrayDeque61B and in the order that the elements were added (i.e. the “conceptual version of the Deque”). As a hint, make use of nextFirst and nextLast! Also, be sure to return only values added as elements into the Deque (don’t return null unless it was explicitly added as an element) 

### I’m having trouble with the constructor. What do I do with nextFirst and nextLast? 

Take a look here (cs61b sp23 proj1B (ArrayDeque) slides). Keep in mind that it’s useful to start off nextLast greater than nextFirst but you can implement it however you choose to do so!

### I’m getting a ExecutionTimeoutException during resizing. What’s going on? 

Make sure you’re resizing using a multiplicative factor and not adding!

### I’m getting an error when trying to @Override getRecursive() in ArrayDeque61B.java. 

Your Deque61B.java interface should not specify a method getRecursive() (that would be saying that every class that implements Deque61B.java should also implement getRecursive(), which is misleading.) Rather, Deque61B.java should not contain getRecursive(), and omit the @Override tag in your implementation in LinkedListDeque61B.
