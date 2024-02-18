---
layout: page
title: >-
  FAQ
parent: >-
  Lab 05: Disjoint Sets
grand_parent: Labs
has_right_toc: true
released: true
---


### I'm running into `StackOverFlowError` or seeing that my assessment timed out 
on one of the tests. 

If you're receiving a `StackOverFlowError`, it might imply that there is an infinite
recursion happening somewhere in your implementation. Double check that you're accounting 
for different cases **correctly** - for example, what should happen if you try to `union`
two vertices within the same set?

