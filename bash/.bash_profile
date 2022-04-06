#
# ~/.bash_profile
#

[[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/shell/profile" ]] && source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/profile"

[[ -f "$HOME/.bashrc" ]] && . "$HOME/.bashrc"
