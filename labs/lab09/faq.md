---
layout: page
title: >-
  FAQ
parent: >-
  Lab09: Conway's Game of Life
grand_parent: Labs
has_right_toc: true
released: true
---

### I'm on a Windows laptop and the saving test is not working. 

If you’re on Windows, the character(s) to represent a new line are a little different compared 
to how it might be done on Mac and Linux. We’ve updated the skeleton to fix issues that that might 
arise from this. You can run git pull skeleton main to pull in the new changes.

### I'm failing tests 1.4 and 1.6 on the autograder. 
Some common things to look out for are to ensure that you're reading in the width and height back in from the 
file in `loadBoard` and to set the instance variables, so that `width` and `height` are initialized properly.
In addition, since the bottom left is (0. 0), keep in mind that when you load back in the board, 
you might be reading the file from top to bottom, so ensure that the orientation is read back in correctly 
when "populating" the board (when you split the file into an array, the top row of the board is read 
in first as the first row and the bottom row is read in last, so when loading it back into the board, 
make sure that the top row corresponds the top row of the board).
