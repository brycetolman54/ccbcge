#!/bin/bash

# get the root of the project
rt=$(git rev-parse --show-toplevel)

# make the alias string
al=$(echo $rt | sed 's/ /\\\\\\\\ /g')
al=$(echo $al | sed 's/C:/\/c/')

# add the alias to you git config file
echo -e "[alias]\n    tv = !sh $al/.tag.sh \$1 \"\$2\"" >> "$rt/.git/config"
