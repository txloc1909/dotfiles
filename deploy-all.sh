#!/bin/sh

all=$(find . \( ! -name . -prune \) ! -name ".*" -type d | awk '{ print substr ($0, 3 ) }')

for program in $all; do
    echo "Deploying $program"
    stow --target=$HOME --restow $program
done
