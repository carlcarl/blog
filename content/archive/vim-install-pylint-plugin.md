Title: vim install pylint plugin
Date: 2011-11-11 13:21
Author: carlcarl
Post_ID: 51
Category: vim
Tags: pylint, vim
Slug: vim-install-pylint-plugin

最近在練習 python，所以開始找相關的 vim plugin 來裝裝看，[pydiction][]
這個可以補完一些基本的語法，還滿不錯的，可惜會跟我的[xptemplate][]
plugin 衝到QQ，沒辦法就只好捨棄掉了，因為 xptemplate
對我還說還是比較實用～。

後來在找可以檢查 python 語法的 plugin，在 stackoverflow
這個網站上有看到相關的討論，感覺[pylint][]
這個功能最強大，就想說用這個看看好了。不過通常功能越強大，要安裝或調整就會越麻煩，要不然就是會跟系統有相依性，像
pylint 就必須要先裝套件在系統上才行，在 ubuntu 上可以直接用套件安裝
pylint：

	:::bash
	sudo apt-get install pylint


安裝完之後就可以當作一般指令來檢查 python 程式，例如：

	:::bash
	pylint test.py

 

接下來如果要整合到 vim 裡面，那就必須再安裝這個 [vim plugin][]，沒有 `compiler` 這個資料夾的話可以自己手動建立就好了，檔案放完之後在 `.vimrc` 檔中加入：

	:::text
	autocmd FileType python compiler pylint


<span style="color: #ff0000;">上面這行在網頁上沒有講到，所以要注意一下。</span>

安裝完後，在開啟 python 檔案的 vim 介面中，輸入(先輸入冒號，冒號跟 P
連在一起會變表情符號囧)：

	:::bash
	Pylint

就會告知警告和錯誤囉～。

 

另外在儲存檔案的時候，也會跑訊息出來，有時候是覺得滿惱人的，這時候可以去修改那個
vim plugin 的檔案，將以下這個設定從 1 改為 0 就可以了：

	:::bash
	#let g:pylint_onwrite = 1
	let g:pylint_onwrite = 0

 

參考網址：

<http://blog.csdn.net/airekans/article/details/6869518>

  [pydiction]: http://www.vim.org/scripts/script.php?script_id=850
  [xptemplate]: http://www.vim.org/scripts/script.php?script_id=2611
  [pylint]: http://www.logilab.org/857
  [vim plugin]: http://www.vim.org/scripts/script.php?script_id=891
