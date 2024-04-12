---
layout: page
title: >-
  FAQ - Lab10
parent: >-
  Lab 10: Tetris
grand_parent: Labs
has_right_toc: true
released: true
---

### I'm getting the error below, what should I do?

```sh
Test Failed!
------------
java.awt.HeadlessException:
No X11 DISPLAY variable was set,
or no headful library support was found,
but this program performed an operation which requires it,
```

If you're getting the error above in your `testClearLines` method, make sure that you're not 
calling on `renderBoard` in the method or any method that uses the `StdDraw` library. The autograder 
does not have the capacity to render or display, so using the `StdDraw` library will cause an 
issue on the autograder. 

### I'm trying to play the game, but the board shows up as black a screen. 

A common problem results from how `runGame` is structured. It might help to revisit the spec, where 
it goes over the details of `runGame`, specifically this portion: 

- If the current tetromino is unable to move down or can no longer move from its current position, **it is set to `null`.**
  The logic for setting it to `null` has been taken care of for you and you do not need to work with it. 

In what instance would you want to spawn a piece?

Another issue is to ensure that you're not clearing the board each time you render it in `renderScore` or any 
other parts of your implementation. For example, calling on `StdDraw.clear` in `renderScore` might clear 
the screen with a specific color each time the game tries to render the score. 

### My game runs and my clear lines appears to work, but it doesn't pass the autograder test. 

Instead of using the `board` instance variable, you'll want to use the `tiles` variable/object that is
passed into the `clearLines` method. The autograder is constructing its own kind of board and passing it 
in to test your `clearLines` method, so make sure that you're referring to the correct variable! 