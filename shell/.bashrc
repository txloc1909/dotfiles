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

# Git prompt options
GIT_PS1_SHOWDIRTYSTATE=true
GIT_PS1_SHOWSTASHSTATE=true
GIT_PS1_SHOWUNTRACKEDFILES=true
GIT_PS1_SHOWUPSTREAM="auto"
GIT_PS1_HIDE_IF_PWD_IGNORED=true
GIT_PS1_SHOWCOLORHINTS=true

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

# Git prompt script on Arch
if [ -f /usr/share/git/git-prompt.sh ]; then
    source /usr/share/git/git-prompt.sh
elif [ -f /usr/share/git/completion/git-prompt.sh ]; then
    source /usr/share/git/completion/git-prompt.sh
fi

# disable terminal flow control (ctrl+s and ctrl+q)
stty -ixon

# enable vi mode
set -o vi

# Aliases
[[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/shell/aliases" ]] && source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/aliases"

# Python's virtualenv and virtualenvwrapper
if [[ -f $HOME/.local/bin/virtualenvwrapper.sh ]]; then
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export WORKON_HOME="${XDG_DATA_HOME}/virtualenvs"
    export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
    source $HOME/.local/bin/virtualenvwrapper.sh
fi

# Colored man pages
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'

## Prompts

# Basic prompt
#export PS1='[\u@\h \W]$(__git_ps1)\$ '

# Minimal prompt
#export PS1=' \[\033[1;36m\]\w \[\033[1;33m\]$(__git_ps1 "(%s)") \[\033[1;36m\]>\[\033[1;34m\]>\[\033[0m\] '

# Two-line prompt
#export PS1='\[\033[;32m\]┌──(\[\033[1;34m\]\u@\h\[\033[;32m\])-[\[\033[0;1m\]\w\[\033[;32m\]]\[\033[01;33m\]$(__git_ps1 " (%s)")\n\[\033[;32m\]└─\[\033[1;34m\]\$\[\033[0m\] '

# Colorful prompt
export PS1='\[\033[1m\]\[\033[1;31m\][\[\033[01;33m\]\u\[\033[11;32m\]@\[\033[11;34m\]\h \[\033[1;35m\]\W\[\033[1;31m\]]\[\033[01;33m\]$(__git_ps1)\[\033[1;37m\]\$ \[\033[0m\]'

# Flexin'
if [[ -x "$(command -v pfetch)" ]]; then
    pfetch
elif [[ -x "$(command -v neofetch)" ]]; then
    neofetch
fi
