#!/usr/bin/env bash
set -euf -o pipefail

result=${PWD##*/}          # to assign to a variable
result=${result:-/}        # to correct for the case where PWD=/

if [[ $result == *"sp24-s"* ]]; then
  printf "
   ________________________________________
  / You f*cked up! Make sure you run the   \\
  \ script outside of your student folder. /
   ----------------------------------------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\\
                  ||----w |
                  ||     ||
  "
  echo
  exit 0
fi

if ssh -q git@github.com; [ $? -eq 255 ]; then
   git clone "https://github.com/Berkeley-CS61B/git-exercise-sp24.git"
else
   git clone "git@github.com:Berkeley-CS61B/git-exercise-sp24.git"
fi
