#!/bin/sh

/usr/bin/gnome-keyring-daemon --start &
remaps.sh
nm-applet &
volumeicon &
sxhkd &
xrdb -merge ~/.Xresources
nitrogen --restore
dunst &
picom &
ibus-daemon -drxR &
