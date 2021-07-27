#!/bin/sh

# start the session manager
lxsession &

# make CaspLock an additional Escape
setxkbmap -option caps:escape &

# network manager applet 
nm-applet & 

# volume applet
volumeicon &

# bluetooth applet
blueman-applet &

# load configs from ~/.Xresources
xrdb -merge ~/.Xresources &

# set wallpaper
nitrogen --restore &

# start the picom compositor 
picom &

# start urxvt daemon
urxvtd -q -o -f &

# start ibus daemon
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
ibus-daemon -drxR &
