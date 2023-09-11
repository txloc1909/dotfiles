if status is-interactive
    # Commands to run in interactive sessions can go here
    setenv PYENV_ROOT "$HOME/.pyenv"
    setenv PATH "$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
    pyenv rehash
    pyenv init - | source
end
