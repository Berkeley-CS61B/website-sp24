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

## A. Install Java

1.  The first step is install the latest version of the Java OpenJDK.
    The easiest way to do this is to get a pre-built binary from Adoptium, which you can download from
    <https://adoptium.net/temurin/releases>.
    You'll want to select the latest version for Windows x64, and use the `.msi` installer.
    At the time of this writing the latest version is marked with "jdk-17.0.3+7",
    but if some later version of Java has been released at the time you're reading this, you're welcome to download that instead.

    ![JDK Download](img/windows/adoptium_jdk.png)

1.  **Important**: The installer will give you the following four options:

    ![JDK Download 1](img/windows/openJDK_install_1.png)

    You should click the small red Xs and change it from "Entire feature will be unavailable" to "Will be installed on local hard drive" as shown below:

    ![JDK Download 2](img/windows/openJDK_install_2.png)

    When you've done this, it should look like the following:

    ![JDK Download 3](img/windows/openJDK_install_3.png)

1.  Click next until everything is installed.

## B. Install Git

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


## C. Install GitHub Cli

We need to be able to login with our GitHub account from our terminal, in order to do that we install Github-Cli

1. First download the installer from <https://cli.github.com/>

   ![Download Page](img/windows/gh_download.png)

2. Run the installer (this one should be relatively straight forward) and you should be done!

   ![Install_Page](img/windows/gh_install.png)


## D. Install Windows Terminal

All recent versions of Windows 10 and 11 come with the Terminal app pre-installed. If you can find the app by searching 
for terminal in the start menu, you should be good to go for this section and can skip onto the next step: 

![Terminal app in the start menu](img/windows/win_start_terminal.png)

**Note: We're looking for the terminal app selected in the screenshot and not the command prompt.**

If not, we recommend that you install the terminal app from the [Microsoft Store](https://aka.ms/terminal), which does not 
require a login or payment. Alternate installation instructions are [here](https://github.com/microsoft/terminal). 

## E. Configure Windows Terminal

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

## F. Note on WSL2 (experimental)

The Summer 2020 update of Windows contains a Linux kernel called WSL2.
We will not be officially supporting WSL2 for this term.
If you're pretty computer savvy, you're welcome to try it out though!
One word of warning: You will need to install javac, java, and git inside WSL2 again,
following the [Linux](linux) instructions for your chosen distribution.
