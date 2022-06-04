#!/bin/sh

/usr/bin/gnome-keyring-daemon --start --components=ssh
remaps.sh
nm-applet &
volumeicon &
sxhkd &
xrdb -merge ~/.Xresources
nitrogen --restore
dunst &
picom &
ibus-daemon -drxR &
