#!/bin/sh

cli="shell vim git wget"

for program in $cli; do
    echo "Deploying $program"
    stow --target=$HOME --restow $program
done
