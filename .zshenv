#
# ~/.zshenv
#

[[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/shell/profile" ]] && source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/profile"

# set environment variables for ibus-bamboo
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
