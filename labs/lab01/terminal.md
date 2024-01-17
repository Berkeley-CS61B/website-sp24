---
layout: page
title: >-
  How to Use the Terminal
parent: >-
  Lab 01: Setup
grand_parent: Labs
has_toc: false
has_right_toc: true
released: true
---

## Terminal Guide

Here are the most important commands that you'll need to know for CS61B:

### `cd`: change your working directory

  ```shell 
  cd hw 
  ```                                                                                                       

This command will change your directory to `hw`.

### `pwd`: print working directory

  ```shell                                                                                                  
  pwd 
  ```                                                                                                       

  This command will tell you the full absolute path for the current 
  directory you are in if you are not sure where you are.

### Shorthand Commands

- `~`: shorthand for your home directory

- `.`: shorthand for your current directory

  ```shell                                                                                                  
  cd .       
  ```                                                                                                       

  This command will change your directory to the current directory (aka. do nothing).

- `..`: shorthand for one parent directory above your current directory

  ```shell                                                                                                  
  cd ..
  ```                                                                                                       

  This command will change your directory to its parent. If you are in `/workspace/day1/`, the 
  command will place you in `/workspace/`.

### `ls`: list files/folders in a directory

  ```shell                                                                                                  
  ls
  ```                                                                                                       

  This command will list all the files and folders in your current directory. 
  You can also use `ls <directory>` to list the contents of a different 
  directory -- try `ls ..`!

### `mkdir`: make a directory

  ```shell                                                                                                  
  mkdir [dirname]
  ```                                                                                                       

  This command will make a new directory within the current directory called `dirname`. You can think of a directory
  as creating another folder on your local computer. 

### `touch`: create a new file

  ```shell                                                                                                  
  touch [filename]
  ```                                                                                                       

  This command will create a file within the current directory called `filename`. To create a text file, you would 
  run the command `touch filename.txt`. 

### `rm`: remove (delete) a file

  ```shell                                                                                                  
  rm [file]
  ```                                                                                                       

  This command will remove `file` from the current directory. It will not work 
  if `file` does not exist.

  ```shell                                                                                                  
  rm -r [dir]
  ```                                                                                                       

  This command will remove the `dir` directory recursively. In other words, it will 
  delete all the files and directories in `dir` in addition to `dir` itself. Be 
  careful with this command!

### `cat`: display the contents of a file

  ```shell                                                                                                  
  cat [file]
  ```                                                                                                       

  This command is useful for inspecting the contents of files in the terminal without 
  having to open them in a program. It is not as useful for large files 
  (which can clutter the terminal) or non-text files (which will likely 
  output gibberish).

### `cp`: copy a file

  ```shell                                                                                                  
  cp lab1/original lab2/duplicate
  ```                                                                                                       

  This command will copy the `original` file in the `lab1` directory and 
  create a `duplicate` file in the `lab2` directory.

### `mv`: move or rename a file

  ```shell                                                                                                  
  mv lab1/original lab2/original
  ```                                                                                                       

  This command moves `original` from `lab1` to `lab2`. Unlike `cp`, mv does not 
  leave original in the `lab1` directory.

  ```shell                                                                                                  
  mv lab1/original lab1/newname
  ```                                                                                                       

  This command does not move the file but rather renames it from `original` to `newname`.

<details markdown="block">                                                                                  
<summary markdown="block">                                                                                  

**Here are some other useful tricks when working in a terminal.**

</summary>                                                                                                  

- Your shell can complete file names and directory names for you with _tab completion_. When you have 
  an incomplete name (for something that already exists), try pressing the `tab` key for autocomplete 
  or a list of possible names.
- You can copy-paste into the terminal. This is straightforward on Mac, but on Windows, right-click 
  to copy and paste highlighted text.
- If you want to run the same command used recently, press the `up` arrow key on your keyboard until
  you see the correct instruction. If you go too far, use the `down` key to go back. 
  This saves typing time if you are doing repetitive instructions.
- You can have multiple terminals open at a time - this might help speed up your workflow if you're 
  running separate tasks that require the terminal.

</details>                                                                                                  