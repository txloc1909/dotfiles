" Plugins to add
" Nerdtree 
" vim-fugitive
" YouCompleteMe
" ctrlp
" themes:
"   sonokai
"
" vim-airline 
" vim-airline-themes
" indentpython 
" 

call plug#begin('~/.vim/plugged')

" colorschemes
Plug 'safv12/andromeda.vim'
Plug 'tomasr/molokai'
Plug 'sonph/onehalf', {'rtp': 'vim/'}
Plug 'dracula/vim', {'as': 'dracula'}
Plug 'jnurmine/Zenburn'
Plug 'arcticicestudio/nord-vim'
Plug 'sjl/badwolf'

" Fugitive, a git wrapper
Plug 'tpope/vim-fugitive'

" Directory tree
Plug 'scrooloose/nerdtree'

" Fuzzy search 
Plug 'kien/ctrlp.vim'

" status bar 
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()


" General settings

    set nocp                " set no Vi compatible
    set number              " show line number 
    syntax enable           " enable syntax highlighting 
    set showcmd             " show command in bottom bar
    "set cursorline          " highlight current line
    filetype indent on      " load filetype-specific indent file  
    filetype plugin on      " load filetype-specific plugin, if exists 
    set lazyredraw          " redraw only when need to 
    set showmatch           " highlight matching brackets 
    set wildmenu            " visual autocomplete for command menu

    set tabstop=4           " number of visual spaces per tab 
    set softtabstop=4       " number of space in tab when editing
    set smartindent
    set smarttab            " insert/delete n spaces for tab
    set autoindent 
    set expandtab           " tabs are spaces

    set relativenumber
    set nu

    set incsearch           " search as characters are entered
    set nohlsearch          " not highlight matches in search   
    set noerrorbells 

    set nowrap
    set scrolloff=8

    set signcolumn=yes
    set colorcolumn=86

    set encoding=utf-8

    set background=dark
    colorscheme molokai
    let g:molokai_original = 1

    set splitbelow
    set splitright

set laststatus=2
set t_Co=256

" set theme for status line 
let g:airline_theme='powerlineish'

" python with virtualenv support
"py3 << EOF 
"import os 
"import sys
"if 'VIRTUAL_ENV' in os.environ:
"    env_base_dir = os.environ['VIRTUAL_ENV']
"    activate_this = os.path.join(env_base_dir, 'bin/activate_this.py')
"    exec(open(activate_this).read(), dict(__file__=activate_this))
"EOF





