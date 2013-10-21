Title: Different color in screen and normal mode
Date: 2012-02-10 00:43
Author: carlcarl
Post_ID: 245
Category: linux
Tags: screen, screenrc, vim
Slug: different-color-in-screen-and-normal-mode

查了一下資料，發現應該是跟顏色的支援有關，要在 `.screerc` 裡加上一行：

	:::text
	termcapinfo xterm 'Co#256:AB=E[48;5;%dm:AF=E[38;5;%dm'


參考網址：  
<http://fcamel-fc.blogspot.com/2009/04/python-vim.html>
