Title: vim OmniCppComplete+STL support
Date: 2011-07-13 13:41
Author: carlcarl
Post_ID: 34
Category: vim
Slug: vim-omnicppcompletestl-support

搞了很久 一直自己鬼打牆 好不容易終於裝好了orz

 

首先先去 <http://www.vim.org/scripts/script.php?script_id=1520>
下載 OmniCppComplete的 plugin，將其解壓縮在 `.vim` 底下。

 

再來去下載支援 STL 的 plugin
<http://www.vim.org/scripts/script.php?script_id=2358>  
解壓縮至 `.vim` 底下，再來在 `.vim` 底下執行

	:::bash
	ctags -R --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++ cpp_src

 

在 `.vim` 底下會出現一個 `tags` 檔，將其作個簡單的改名，如 `stl_tags` 之類的。

 

然後，在 `.vimrc` 裡加上:

	:::bash
	set tags+=/my/path/to/tags/

`/my/path/tags/` 是剛才的 `tag` 檔完整路徑，以這裡來說的話就是在這裡
 `~/.vim/stl_tags`。

 

照理來說到這裡應該就ok了。我卡住的點就在於忘記把原本程式產生 tag 的指令從

	:::bash
	ctags -R


改成

	:::bash
	ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .


沒錯，不只那個 STL 需要用 c++ 建 tag，原本的程式部份也別忘了要用這個指令來建，因為指令有點長，為了方便，可以將這個指令作 alias 存到 `.bashrc` 之類的檔案。

或是在 `.vimrc` 裡設定快捷建:

	:::bash
	map <C-F12> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR>


上面這個指令在 vim 模式裡，按下 `ctrl` 加上 `F12` 就會自動產生 tags 檔。

參考網址  
<http://www.vim.org/scripts/script.php?script_id=1520>  
<http://www.vim.org/scripts/script.php?script_id=2358>  
<http://liuyix.com/vim-stl-auto-complete>  
<http://hi.baidu.com/dtzw/blog/item/a66aa8ec1cdab63027979177.html>  
<http://blog.csdn.net/hjs1122/article/details/6025150>
