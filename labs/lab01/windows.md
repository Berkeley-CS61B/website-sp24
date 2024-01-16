---
layout: page
title: Windows
parent: >-
  Lab 01: Setup
grand_parent: Labs
has_toc: false
has_right_toc: true
released: true
---

## A. Install Git

1.  Install git. Head to
    [http://git-scm.com/download/](http://git-scm.com/download/)
    and download the Git for Windows installer.

    ![Windows Download Git 1](img/windows/win_download.png)

    ![Windows Download Git 2](img/windows/win_64.png)

2.  Run the installer. You'll be faced with many options. We'll only be selecting different options on:

    - The **Select Components** page, where we add a Git bash profile to the windows terminal.

      ![Add git bash profile](img/windows/win_git_first.png)

    - The **Configuring Experimental Options** page, where we add support for native console programs.

      ![Add native console programs support](img/windows/win_git_last.png)

3. All the other options should be left as is. The entire install process is shown in the gif below:

   ![Windows git install](img/windows/windows_git.gif)

## B. Install Windows Terminal

All recent versions of Windows 10 and 11 come with the Terminal app pre-installed. If you can find the app by searching 
for terminal in the start menu, you should be good to go for this section and can skip onto the next step: 

![Terminal app in the start menu](img/windows/win_start_terminal.png)

**Note: We're looking for the terminal app selected in the screenshot and not the command prompt.**

If not, we recommend that you install the terminal app from the [Microsoft Store](https://aka.ms/terminal), which does not 
require a login or payment. Alternate installation instructions are [here](https://github.com/microsoft/terminal). 

## C. Configure Windows Terminal

When you start up windows terminal, you'll see a powershell terminal prompt. We don't want to use "PowerShell", which is based on Windows.
Instead, we want to use a "bash shell" (specifically, Git bash), which is based on Linux.
To set this up:

1.  Click on the drop-down arrow next to the plus "+" sign at the top and open the settings page.

    ![Terminal Setup 1](./img/windows/win_settings.png)

2. Set the default profile to Git bash, default terminal application to windows terminal and hit save.

    ![Terminal Setup 2](./img/windows/win_default_profile.png)

3. If you completed the previous steps correctly,
    when you click on the plus sign, you should see a Git Bash shell window open.

    ![Git Bash Setup Correctly](img/windows/git_bash_done.png)

    At this point, you're all done!
    You can now move on with the rest of Lab 1.

## D. Note on WSL2 (experimental)

The Summer 2020 update of Windows contains a Linux kernel called WSL2.
We will not be officially supporting WSL2 for this term.
If you're pretty computer savvy, you're welcome to try it out though!
One word of warning: You will need to install javac, java, and git inside WSL2 again,
following the [Linux](linux) instructions for your chosen distribution.
