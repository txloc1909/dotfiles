#!/bin/sh

cli="shell vim git tmux wget"

for program in $cli; do
    echo "Deploying $program"
    stow --target=$HOME --restow $program
done
