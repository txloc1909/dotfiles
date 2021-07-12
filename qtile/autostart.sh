#!/bin/sh

# make CaspLock an additional Escape
setxkbmap -option caps:escape &

# network manager applet 
nm-applet & 

# load configs from ~/.Xresources
xrdb -merge ~/.Xresources &

# set wallpaper
nitrogen --restore &
