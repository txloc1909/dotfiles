"
" .vimrc
"

" First thing first,
set nocompatible
filetype plugin on
syntax on

let mapleader=" "
let maplocalleader=","

call plug#begin()
Plug 'safv12/andromeda.vim'
Plug 'tomasr/molokai'
Plug 'sonph/onehalf', {'rtp': 'vim/'}
Plug 'sjl/badwolf'
Plug 'NLKNguyen/papercolor-theme'

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'dense-analysis/ale'
Plug 'vim-python/python-syntax', { 'for': 'python' }
Plug 'airblade/vim-gitgutter'

Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'mhinz/vim-sayonara', { 'on': 'Sayonara' }
Plug 'unblevable/quick-scope'
Plug 'jiangmiao/auto-pairs'

Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install()  }, 'for': ['markdown', 'vim-plug'] }

call plug#end()


" General settings
filetype indent on
set showcmd
set number relativenumber
set cursorline cursorcolumn
set lazyredraw
set showmatch
set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent autoindent
set smarttab expandtab
set incsearch nohlsearch
set noerrorbells
set nowrap
set scrolloff=8
set signcolumn=yes
set colorcolumn=80
set encoding=utf-8
set splitbelow splitright
set hidden
set confirm
set laststatus=2
set t_Co=256
set timeout ttimeout
set timeoutlen=300 ttimeoutlen=-1

let g:airline_powerline_fonts = 1
let g:airline_theme='badwolf'
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif
let g:airline_symbols.branch = ''
let g:airline_symbols.colnr = ' :'
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ' :'
let g:airline_symbols.maxlinenr = '☰ '
let g:airline_symbols.dirty='⚡'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#ale#enabled = 1

let g:NERDTreeWinSize=20
let g:NERDTreeShowHidden=1

let g:fzf_preview_window = ['right:50%', 'ctrl-/']
let g:fzf_buffers_jump = 1

let g:python_highlight_all = 1

let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 1
let g:mkdp_refresh_slow = 1
let g:mkdp_browser = '/usr/bin/qutebrowser'
let g:mkdp_theme = 'dark'

let g:ale_fixers = {
\   '*': ['remove_trailing_lines', 'trim_whitespace'],
\   'python': ['black'],
\}
let g:ale_fix_on_save = 1
let g:ale_linter = {
\   'python': ['flake8', 'mypy'],
\}
let g:ale_linter_explicit = 1
let g:ale_virtualenv_dir_names = []
let g:ale_python_flake8_options = '--max-line-length=88'

let g:goyo_width = 88
let g:goyo_linenr = 1
function! s:goyo_enter()
    if executable('tmux') && strlen($TMUX)
        silent !tmux set status off
        silent !tmux list-panes -F '\#F' | grep -q Z || tmux resize-pane -Z
    endif
    set noshowmode
    set noshowcmd
    set nocursorline nocursorcolumn
    set scrolloff=999
    Limelight
endfunction
function! s:goyo_leave()
    if executable('tmux') && strlen($TMUX)
        silent !tmux set status on
        silent !tmux list-panes -F '\#F' | grep -q Z && tmux resize-pane -Z
    endif
    set showmode
    set showcmd
    set cursorline cursorcolumn
    set scrolloff=8
    Limelight!
endfunction
autocmd! User GoyoEnter nested call <SID>goyo_enter()
autocmd! User GoyoLeave nested call <SID>goyo_leave()

" Quickscope
" Trigger a highlight in the appropriate direction when pressing these
let g:qs_highlight_on_keys = ['f', 'F', 't', 'T']
let g:qs_max_chars=120
" Must set quickscope color BEFORE set colorscheme
augroup qs_color
    autocmd!
    autocmd ColorScheme * highlight QuickScopePrimary guifg='#afff5f' gui=underline ctermfg=155 cterm=underline
    autocmd ColorScheme * highlight QuickScopeSecondary guifg='#5fffff' gui=underline ctermfg=81 cterm=underline
augroup END

set background=dark
colorscheme badwolf

let g:gitgutter_map_keys = 0
highlight GitGutterAdd guifg=#009900 ctermfg=Green
highlight GitGutterChange guifg=#bbbb00 ctermfg=Yellow
highlight GitGutterDelete guifg=#ff2222 ctermfg=Red

augroup git_gutter
    autocmd!
    autocmd BufWritePost * :GitGutter
augroup END

" Enable autocompletion
set wildmenu
set wildmode=longest,list,full
set completeopt=menuone,longest

" Cursor shape
let &t_SI = "\e[6 q"            " Beam
let &t_EI = "\e[2 q"            " Block
augroup reset_cursor_shape
    autocmd!
    autocmd VimEnter * normal! :startinsert :stopinsert
augroup END

" Keybindings

" Back to normal
inoremap jk <Esc>
cnoremap jk <Esc><CR>

" Quickly access .vimrc
nnoremap <Leader>ev :edit $MYVIMRC<CR>
nnoremap <Leader>sv :source $MYVIMRC<CR>

" Write and quit
nnoremap <Leader>q :w<CR>:Sayonara<CR>
nnoremap <Leader>Q :qa!<CR>
nnoremap <Leader><Leader>q :Sayonara<CR>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>s :update<CR>

" Open splits
nnoremap <Leader><Leader>s :split<CR>
nnoremap <Leader><Leader>v :vsplit<CR>

" Buffer navigations
nnoremap <Leader><Tab> <C-^>

" Quick git
nnoremap <Leader><Leader>g :Git<CR>

" Fuzzy search
nnoremap <Leader>p :GFiles<CR>
nnoremap <Leader>b :Buffers<CR>

" Move visual line
nnoremap j gj
nnoremap k gk

" Navigating splits
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Resizing splits
nnoremap <C-S-Left> :vertical resize -3<CR>
nnoremap <C-S-Right> :vertical resize +3<CR>
nnoremap <C-S-Up> :resize +3<CR>
nnoremap <C-S-Down> :resize -3<CR>

" Make Y behavior consistent with others
nnoremap Y y$

" Move to begin or end of line easier
nnoremap H ^
nnoremap L $
vnoremap H ^
vnoremap L $

" Toggle distraction-free writing mode
nnoremap <Leader>z :Goyo<CR>

" Access system clipboard, Ctrl+Alt+C and Ctrl+Alt+V to copy and paste
set clipboard+=unnamedplus
vnoremap <C-M-c> "+y
nnoremap <C-M-v> "+P

" Automatically deletes all trailing whitespaces and newlines at end of file
" on save, then reset cursor position
augroup trailing_whitespaces_newlines
    autocmd!
    autocmd BufWritePre * let currPos = getpos(".")
    autocmd BufWritePre * %s/\s\+$//e
    autocmd BufWritePre * %s/\n\+\%$//e
    autocmd BufWritePre *.[ch] %s/\%$/\r/e
    autocmd BufWritePre * cal cursor(currPos[1], currPos[2])
augroup END

" python with virtualenv support
if has('python3')
py3 << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    env_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(env_base_dir, 'bin/activate_this.py')
    exec(open(activate_this).read(), dict(__file__=activate_this))
EOF
endif

" Minimalist-TabComplete-Plugin
inoremap <expr> <Tab> TabComplete()
fun! TabComplete()
    if getline('.')[col('.') - 2] =~ '\K' || pumvisible()
        return "\<C-P>"
    else
        return "\<Tab>"
    endif
endfun

" Minimalist-AutoCompletePop-Plugin
set completeopt=menu,menuone,noinsert
inoremap <expr> <CR> pumvisible() ? "\<C-Y>" : "\<CR>"
autocmd InsertCharPre * call AutoComplete()
fun! AutoComplete()
    if v:char =~ '\K'
        \ && getline('.')[col('.') - 4] !~ '\K'
        \ && getline('.')[col('.') - 3] =~ '\K'
        \ && getline('.')[col('.') - 2] =~ '\K' " last char
        \ && getline('.')[col('.') - 1] !~ '\K'
        call feedkeys("\<C-P>", 'n')
    end
endfun

" set linewrap in markdown and latex file
autocmd BufRead,BufNewFile *.md,*.tex set wrap
