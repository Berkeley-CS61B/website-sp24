#!/bin/bash

. ../../../demo-magic.sh

cd ~
clear
rm -rf lab01-checkoff
mkdir lab01-checkoff

PROMPT_TIMEOUT=1
DEMO_PROMPT="[${CYAN}git-checkoff${COLOR_RESET}]:${GREEN}\W${COLOR_RESET}$ "

cd lab01-checkoff
git init > /dev/null

git config user.name "CS 61B Staff"
git config user.email "cs61b@berkeley.edu"
git config pager.log false

echo "61b version 1" > 61b.txt
echo "61bee version 1" > 61bee.txt
git add 61b.txt
git commit -m "Add 61b.txt" > /dev/null
echo "61b changed to version 2" > 61b.txt
git add .
git commit -m "Update 61b.txt and add 61bl.txt"  > /dev/null
echo "61b changed to version 3" > 61b.txt

pe "# I've done all of my git commands, and am currently in the lab01-checkoff directory."
pe "git status"
pei ""
for i in {1..3}
do
  wait
done

pe "git log"
pei ""
for i in {1..3}
do
  wait
done
