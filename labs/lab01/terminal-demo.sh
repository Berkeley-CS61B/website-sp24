#!/bin/bash

. ../../../demo-magic.sh

cd ~
clear
rm -rf temp

PROMPT_TIMEOUT=1
DEMO_PROMPT="[${CYAN}example${COLOR_RESET}]$ "

pe "git --version"
pe "# Git is installed! You don't have to have this exact version."
pe "mkdir ~/temp"
pe "cd ~/temp"
pe "touch HelloWorld.java"

pei "# Use a text editor to copy-paste into HelloWorld.java!"

echo "public class HelloWorld {" >> HelloWorld.java
echo "    public static void main(String[] args) {" >> HelloWorld.java
echo "        System.out.println(\"Hello world!\");" >> HelloWorld.java
echo "    }" >> HelloWorld.java
echo "}" >> HelloWorld.java

pe "cat HelloWorld.java"
pe "ls"
pe "javac HelloWorld.java"
pe "ls"
pe "# We now see HelloWorld.class, which was created by javac."
pe "java HelloWorld"

cd ..
rm -rf temp
