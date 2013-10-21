Title: vim xptemplate add smarty(tpl) support
Date: 2011-06-22 14:10
Author: carlcarl
Post_ID: 28
Category: vim
Slug: vim-xptemplate-add-smartytpl-support

弄了很久 查了一下資料才發現原來那麼簡單=.=。

在 `personal_ftplugin/` 底下要先建一個 `smarty` 資料夾，接著在裡面新增一個 `smarty.xpt.vim` 檔案。

以下是檔案的內容:

	:::text
	XPTemplate priority=personal
	XPTinclude
	html/html


這樣就 ok 了，其實就是把 html 的設定拿來用而已。接著開一個 tpl 副檔名的試試看，應該是 ok。我想應該底層有去做 smarty 和 tpl 副檔名的對應，要不然這邊的內容完全都沒看到 tpl 的對應。

 

參考網頁

[http://groups.google.com/group/xptemplate/browse_thread/thread/9af94f0e27007817#][]

 

  [http://groups.google.com/group/xptemplate/browse_thread/thread/9af94f0e27007817#]: http://groups.google.com/group/xptemplate/browse_thread/thread/9af94f0e27007817#
