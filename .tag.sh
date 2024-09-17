#!/bin/bash

# tag it
git tag -a $1 -m $2

# push it
git push origin $1

# update the version
python /c/Users/bat20/OneDrive\ -\ Brigham\ Young\ University/BYU/2024/Fall/ccbcge/get_version.py
