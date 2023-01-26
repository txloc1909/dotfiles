" Stolen snippet from:
" https://begriffs.com/posts/2019-07-19-history-use-vim.html#backups-and-undo

" Some safeguards
if !isdirectory($HOME . "/.vim/swap")   | call mkdir($HOME . "/.vim/swap", "p", 0700)   | endif
if !isdirectory($HOME . "/.vim/backup") | call mkdir($HOME . "/.vim/backup", "p", 0700) | endif
if !isdirectory($HOME . "/.vim/undo")   | call mkdir($HOME . "/.vim/undo", "p", 0700)   | endif

" Protect changes between writes. Default values of
" updatecount (200 keystrokes) and updatetime
" (4 seconds) are fine
set swapfile
set directory^=~/.vim/swap//

" protect against crash-during-write
set writebackup
" but do not persist backup after successful write
set nobackup
" use rename-and-write-new method whenever safe
set backupcopy=auto
" patch required to honor double slash at end
if has("patch-8.1.0251")
	" consolidate the writebackups -- not a big
	" deal either way, since they usually get deleted
	set backupdir^=~/.vim/backup//
end

" persist the undo tree for each file
set undofile
set undodir^=~/.vim/undo//
