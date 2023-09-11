if status is-interactive
    # Commands to run in interactive sessions can go here

    if type -q eza
        alias ls='eza --icons --group-directories-first'
        alias ll='eza -lahF --icons --group-directories-first'
        alias la='eza -1a --icons --group-directories-first'
    else
        alias ls='ls --color=auto --group-directories-first'
        alias ll='ls -alFh'
        alias la='ls -A'
    end

    if test -d $HOME/.pyenv
        setenv PYENV_ROOT "$HOME/.pyenv"
        setenv PATH "$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
        pyenv rehash
        pyenv init - | source
    end
end
