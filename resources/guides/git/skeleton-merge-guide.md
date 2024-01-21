---
layout: page
title: "Git Pull Skeleton Merge Guide"
parent: Using Git
has_children: false
released: true
---


If you're pulling the latest skeleton code, this will often result in a "merge", as described in the more advanced sections of the Git Guide. 

A text editor will automatically open asking you to provide a message on why you are merging.

On the top line of your text editor, enter a message like "i was just trying to pull new skeleton code" or whatever you'd like. The text you'll enter will go right above:

```
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

After entering your message at the very top of the file, **save and close the text window** and the merge will be done.

Depending on how you installed Git, you may find youself in a _command line_ text editor like `nano` or `vim`. If this happens and you've never used a command line text editor, don't panic! Nano is relatively straightforward to use. Simply type your message, and press "ctrl-o" to save, then "ctrl-x" to exit.

If you followed the directions for Lab 1 Setup properly, you should not be in `vim`. However, if you are nonetheless in vim, please see this [helpful tutorial in youtube](https://www.youtube.com/watch?v=ebZzVAZC7tc) or [this stack overflow post](http://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor) about what to do next.

And if you're still stuck, post on Ed and someone will be able to help you.

Once you've successfully merged, you should see a proj0 directory appear with
files that match [the skeleton
repository](https://github.com/Berkeley-CS61B/skeleton-sp19/tree/master/proj0).

If you somehow end up with a message saying there was a merge conflict, consult the [Git WTFS guide](wtfs.md).

If you get some sort of error, STOP and either figure it out by carefully
reading the git guide or seek help at OH or with Ed. You'll potentially save
yourself a lot of trouble vs. guess-and-check with git commands. If you find
posts on Google that suggest using `git push -f`, **don't**. This can cause
some serious headaches with git. 
