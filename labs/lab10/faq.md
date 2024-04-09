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