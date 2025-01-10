#!/bin/sh

REPO_DIR=$(pwd)

if [ ! -d "$REPO_DIR/.git" ]; then
  echo "Not a git repository! Exiting..."
  exit 1
fi

echo "Pulling latest changes from remote repository..."
git pull origin master

  echo "Changes detected, committing and pushing..."
if [[ -n $(git status --porcelain) ]]; then
  
  git add .

  git commit -m "$(TZ='UTC' date '+%a %m.%d.%Y %H:%M')"

  git push origin master
else
  echo "No changes to commit."
fi

echo "Rebasing with remote master..."
git fetch origin
git rebase origin/master
