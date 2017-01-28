set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'gmarik/vundle'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'mattn/emmet-vim'
Bundle 'aperezdc/vim-template'
Bundle 'Yggdroot/indentLine'
Plugin 'Valloric/YouCompleteMe'
Plugin 'honza/vim-snippets'
Plugin 'SirVer/ultisnips'
Plugin 'Lokaltog/vim-powerline'
Bundle 'taglist.vim'
Bundle 'winmanager'
Bundle 'minibufexpl.vim'
Bundle 'gerw/vim-latex-suite'
Plugin 'carlobaldassi/ConqueTerm'
Plugin 'altercation/vim-colors-solarized'
Plugin 'iamcco/mathjax-support-for-mkdp'
Plugin 'iamcco/markdown-preview.vim'
Plugin 'scrooloose/nerdtree'
call vundle#end()            " required
filetype plugin indent on     " required

set laststatus=2
let g:Powerline_colorscheme = 'solarized'

"""""""""""""""""""""""""""""""""""""""""""""""""""
"中文配置
set helplang=cn
set encoding=utf-8
set fenc=utf-8
set fileencodings=ucs-bom,utf-8,cp936
"语法高亮
syntax enable
"set background=dark
let g:colors_name='solarized'
let g:solarized_termcolors=256
let g:solarized_termtrans=1
let g:solarized_contrast='normal'
let g:solarized_visibility='normal'


"忽略swap文件
set noswapfile  

"set mouse=a
set ic
set hls
set ruler

"缩进
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set cindent
set ts=4
set expandtab

set backspace=indent,eol,start





"taglist
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
"需要安装ctags进行配置
let Tlist_Ctags_Cmd = '/usr/local/bin/ctags'
set tags=tags;/


"win manager
"let g:winManagerWindowLayout='FileExplorer|TagList'
nmap wm :WMToggle<cr>

let g:NERDTree_title="[NERDTree]"  
let g:winManagerWindowLayout="NERDTree|TagList"  
  
function! NERDTree_Start()  
    exec 'NERDTree'  
endfunction  
  
function! NERDTree_IsValid()  
    return 1  
endfunction  

"minibuffer
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1






let g:email= 'cfan89@gmail.com'
let g:license='MIT'
let g:Tex_UsePython = 0



"python 快捷键 F12直接运行
nmap \ll :!xelatex % <CR>
"nmap \ll :!make <CR>
nmap \op :!open % <CR>
nmap mk :!make<CR>

let g:tex_conceal = ""

"缩进线
let g:indentLine_color_term = 239

"markdown&markdownpreview
let g:vim_markdown_folding_disabled=1
let g:vim_markdown_math=1
let g:mkdp_path_to_chrome='firefox'

"html 
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstal



"YouCompleteMe & UltiSnips
let g:ycm_key_list_select_completion = [ '<Down>']
let g:ycm_key_list_previous_completion = ['<Up>']
"在注释输入中也能补全
let g:ycm_complete_in_comments = 1
let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

"ConqueTerm
" 水平分割出一个bash
nnoremap    ct              :ConqueTermSplit zsh<CR>
" 垂直分割出一个bash
nnoremap    cp              :ConqueTermVSplit ipython<CR>



""""""""""""""""""""""
"Quickly Run
""""""""""""""""""""""
map \yy :call CompileRunGcc()<CR>
func! CompileRunGcc()
	exec "w"
	if &filetype == 'c'
		exec "!g++ % -o %<"
		exec "!time ./%<"
	elseif &filetype == 'cpp'
		exec "!g++ % -o %<"
		exec "!time ./%<"
	elseif &filetype == 'java'
		exec "!javac %"
		exec "!time java %<"
	elseif &filetype == 'sh'
		:!time bash %
	elseif &filetype == 'python'
		exec "!time python2.7 %"
	elseif &filetype == 'html'
		exec "!firefox % &"
	elseif &filetype == 'go'
		"        exec "!go build %<"
		exec "!time go run %"
	elseif &filetype == 'mkd'
		exec "!~/.vim/markdown.pl % > %.html &"
		exec "!firefox %.html &"
	endif
endfunc
