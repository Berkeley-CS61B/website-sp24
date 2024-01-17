---
layout: page
title: >-
  Mac OS
parent: >-
  Lab 01: Setup
grand_parent: Labs
has_toc: false
has_right_toc: true
released: true
---

## A. Setup

1.  Install the Xcode Command Line Tools through your terminal by running this command
    (it should already be available on macOS - try using the search feature/Finder to find it): 

    ```shell
    xcode-select --install
    ```

    {: .warning}
    This might take a while. If you are on an older system, you may have to update your software. If you run 
    into any error regarding not enough free space, please double check how much free storage you have left (a
    rough estimate of what is needed is at least 40GB of free space). You may need to also restart your laptop. 
    
    {: .warning}
    There is also a StackOverflow post that you can reference
    [here](http://stackoverflow.com/questions/9329243/xcode-4-4-and-later-install-command-line-tools) if  
    it's a similar issue. **If you are having trouble though, please come find a staff member to help you!**

2. At this point, verify that `git` is installed with 

    ```shell
    git --version
    ```

    You have successfully installed git if this command returns a valid version
    number and does not fail. If the installation is good,
    skip the rest of the guide and return to the lab.

## B. Git Install Issues

If you had installation issues with Git try the instructions
"Installing on macOS" at this
[link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Contact your TA if you are still having issues.
