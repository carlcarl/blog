Title: svn delete only in repo
Date: 2011-07-13 16:24
Author: carlcarl
Post_ID: 35
Category: version-control
Tags: svn
Slug: svn-delete-only-in-repo

版本管理一些檔案像是測資之類的可能會不小心用 svn add 起來，但是有些測資檔案很大，實在不想上傳，所以就想要將檔案從 svn 版本中移除。

之前都很笨的先備份檔案，做刪除，然後再複製回來，後來查資料才發現有參數可以用:

	:::bash
	svn delete --keep-local file


這樣就能保留這個檔案了～。

 

參考網頁:  
[http://www.lampblog.net/2011/01/svn-delete][]

  [http://www.lampblog.net/2011/01/svn-delete]: http://www.lampblog.net/2011/01/svn-delete%EF%BC%8D%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95/
