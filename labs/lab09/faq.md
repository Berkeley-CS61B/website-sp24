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

If you're on Windows, the character(s) to represent a new line are a little different compared to how it might be 
done on Mac and Linux. On Windows, the new line character is represented as `"\r\n"` versus just `"\n"`. We've 
provided a helper method to remove the `"\r"` character, called `newlineReplacer`, that should be used in `saveBoard`. 
When reading it back in with `loadBoard`, please make sure to read it back in with `"\n"` as the delimiter instead of 
using `"\r\n"`. For visually verifying, feel free to use `"\r\n"` but make sure to follow the instructions mentioned 
above. 