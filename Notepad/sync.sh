#!/bin/sh

REPO_DIR=$(pwd)

if [ ! -d "$REPO_DIR/.git" ]; then
  echo "Not a git repository! Exiting..."
  exit 1
fi

if [[ -n $(git status --porcelain) ]]; then
  echo "Changes detected, committing and pushing..."
  
  git add .

  git commit -m "$(TZ='UTC' date '+%a %m.%d.%Y %H:%M')"

  git push origin master
else
  echo "No changes to commit."
fi
