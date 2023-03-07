#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Setting history
export HISTSIZE=10000
export HISTFILESIZE=10000
export HISTFILE="${XDG_CACHE_HOME:=$HOME/.cache}/bash_history"
export LESSHISTFILE=-

# shopt
shopt -s histappend             # append to history file
shopt -s checkwinsize           # check window size after each command
shopt -s autocd                 # type path to auto cd
shopt -s cdspell                # auto correct cd spelling
shopt -s cmdhist
shopt -s dirspell
shopt -s direxpand

# Bash completion
if [ -f /usr/share/bash-completion/bash_completion ]; then
    source /usr/share/bash-completion/bash_completion
elif [ -f /etc/bash_completion ]; then
    source /etc/bash_completion
    if [ -d /etc/bash_completion.d ]; then
        for f in /etc/bash_completion.d/*; do
            source $f
        done
    fi
fi

# disable terminal flow control (ctrl+s and ctrl+q)
stty -ixon

# Aliases
[[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/shell/aliases" ]] && source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/aliases"

# Colored man pages
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'

# Default prompt
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[0m\]\[\033[1;37m\]\[\033[00m\]\$ '
[[ -f $XDG_CONFIG_HOME/shell/bash_prompt ]] && source $XDG_CONFIG_HOME/shell/bash_prompt

# Flexin'
if [[ -x "$(command -v pfetch)" ]]; then
    pfetch
elif [[ -x "$(command -v neofetch)" ]]; then
    neofetch
fi

# back to $HOME if inside a distrobox container
[[ -f /run/.containerenv || -f /.dockerenv ]] && cd $HOME
