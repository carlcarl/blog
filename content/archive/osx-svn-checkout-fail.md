Title: OSX svn checkout fail
Date: 2013-03-13 15:36
Author: carlcarl
Post_ID: 799
Category: Mac, 版本管理
Tags: hdiutil, svn
Slug: osx-svn-checkout-fail

在 OSX 上 checkout svn 的 repo 遇到了 error，跟我說 .svn
底下少了某個檔案，後來才發現有兩個同樣名稱的檔案，只是大小寫不一樣，看來好像是因為
OSX 的檔案系統預設大小寫視為一樣的。如果要解決這個問題除了換個名稱，要不然就是做個
case sensitive 的 image mount 上去，指令如下：  
<!--more-->

	:::bash
	# 建立 image 檔案
	hdiutil create -size 100m -fs "Case-sensitive HFS+" -volname xxx xxx.dmg
	# size 後面的參數表示 image 大小
	# volname 後面的參數表示掛載後的名稱
	# xxx.dmg 是 image 檔案的名稱

	# 掛載 image 檔案
	hdiutil attach xxx.dmg

接著就可以在 `/Volumes/` 底下看到剛才掛上去的 image 資料夾。

參考網址：  
<http://stackoverflow.com/questions/2986786>
