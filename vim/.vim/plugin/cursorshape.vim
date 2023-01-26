let &t_SI = "\e[6 q"            " Beam
let &t_EI = "\e[2 q"            " Block
augroup reset_cursor_shape
    autocmd!
    autocmd VimEnter * normal! :startinsert :stopinsert
augroup END
