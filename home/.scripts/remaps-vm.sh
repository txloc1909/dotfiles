#!/bin/sh

# This script is called on startup to remaps key

# This script is written specifically for virtual machines running on top of Windows host. 
# Since Windows host machine already maps Capslock to Escape, 
# this script aims to turn the escape-producing signal when press CapsLock from the host machine 
# to behave as desired (Escape when pressed, Super when held)

# Increase key speed via a rate change
xset r rate 300 50

# Make Escape produces Super when held, but acts normally when pressed
spare_modifier="Hyper_L"
xmodmap -e "keycode 9 = $spare_modifier"
xmodmap -e "remove mod4 = $spare_modifier"
xmodmap -e "keycode any = Escape"
killall xcape 2>/dev/null; xcape -e "$spare_modifier=Escape;"

# Map the menu button to right super as well
xmodmap -e 'keycode 135 = Super_R'

# Turn off capslock if on, since there is no longer a key for it
xset -q | grep "Caps Lock:\s on" && xdotool key Caps_Lock
