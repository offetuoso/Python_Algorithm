#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

cd C:\develop\Git\python\Algorithm
git init

git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"


msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

git push origin master