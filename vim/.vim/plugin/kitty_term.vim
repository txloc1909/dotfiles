" specific configuration for the kitty terminal

if &term != 'xterm-kitty'
    finish
endif

" vim hardcodes background color erase even if the terminfo file does
" not contain bce (not to mention that libvte based terminals
" incorrectly contain bce in their terminfo files). This causes
" incorrect background rendering when using a color theme with a
" background color.
" see: https://github.com/kovidgoyal/kitty/issues/108
let &t_ut=''
