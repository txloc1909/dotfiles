#!/bin/sh

xset r rate 300 50

setxkbmap -option

setxkbmap -option ctrl:nocaps
#setxkbmap -option caps:ctrl_modifier
#setxkbmap -option caps:none
killall xcape 2>/dev/null; xcape -e 'Control_L=Escape'

xmodmap -e 'keycode 135 = Super_R'

xset -q | grep "Caps Lock:\s on" && xdotool key Caps_Lock
