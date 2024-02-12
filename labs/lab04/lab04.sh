#!/usr/bin/env bash
set -euf -o pipefail

# https://stackoverflow.com/a/1371283
# Get the current folder name
result=${PWD##*/}          # to assign to a variable
result=${result:-/}        # to correct for the case where PWD=/

# https://stackoverflow.com/a/229606
# See if we're in a student folder and exit if so
if [[ $result == *"sp24-s"* ]]; then
  printf "
   ____________________________________
  / Oops! Make sure you run the script \\
  \ outside of your student folder.    /
   ------------------------------------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\\
                  ||----w |
                  ||     ||
  "
  echo
  exit 0
fi

# https://stackoverflow.com/a/52343703
# Determine if ssh is set up with Github with a fallback to https
if ssh -q git@github.com; [ $? -eq 255 ]; then
   git clone "https://github.com/Berkeley-CS61B/git-exercise-sp24.git"
else
   git clone "git@github.com:Berkeley-CS61B/git-exercise-sp24.git"
fi
