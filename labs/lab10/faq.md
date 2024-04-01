---
layout: page
title: "FAQ - Lab 12: Tetris"
categories: lab
released: true
searchable: true
---

### If you're having trouble with flickering or the logic of `runGame`, we've provided some pseudocode here. 

```sh 
public void runGame() {
    resetActionTimer();
    resetFrameTimer();
    
    // Call on helper method to spawn a piece. 
     
    while (// check for if the game is over) {
        if (shouldRenderNewFrame()) {
            // Once a piece is set to null, it can no longer move
            if (currentTetromino == null) {
               // We then want to call on a helper method to check
               // for rows completed  and clear the lines. 
               
               // As well as spawn a new piece. 
               
            }
            // Call on helper method to take user interactivity.

            // Call on helper method to render the board. 
            
        }
    }
}
```
