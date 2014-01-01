Title: git export files to some existed directory
Date: 2011-05-24 16:14
Author: carlcarl
Post_ID: 21
Category: version-control
Tags: bashrc, git, vimrc
Slug: git-export-files-to-some-existed-directory

最近想把 vimrc 和 bashrc 等設定檔作同步，想說大家都在用 git，所以就不用 svn 改用 git 看看了!

但是在同步的時候卻遇到了問題，本來想說直接輸入看看

	:::bash
	git clone <git repo url>


結果出現錯誤: `fatal: destination path
'home目錄' git clone already exists and is not an empty directory`

因為我的 home 目錄已經存在 而且也沒辦法 merge = =，沒辦法，只好來找一下資料。

說真的還找得滿久的，以下是我覺得算是比較能接受的一種解決方法(有其他方法歡迎提供QQ)

	:::bash
	git init
	git remote add origin gitpath
	git fetch
	git branch master origin/master
	git checkout master


在家目錄下作以上動作，接著就可以看到 git 上的 .bashrc 終於出現在我的家目錄底下了orz

 

參考網頁

<http://code.google.com/p/tortoisegit/issues/detail?id=204>
