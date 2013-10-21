Title: Several ways to check process port
Date: 2011-12-15 02:51
Author: carlcarl
Post_ID: 218
Category: linux
Tags: fuser, lsof, netstat, port, rpcinfo
Slug: several-ways-to-check-process-port

目前知道的就以下四種，記得用 root
權限來看，或者是指令前面加 `sudo`，不然有些 process 會看不到。

-   netstat -antp
-   rpcinfo -p
-   lsof -i :port
-   fuser port/tcp

以上指令的 `port` 為你要的 port
數字。基本上用 `netstat` 會列出一堆清單，通常就可以在其中找到，不行的話就使用 `lsof`，還是沒有的話，接下來就用 `fuser`，如果真的還是沒有，最後就用 `rpcinfo` 查看，再沒有我就沒辦法了 XD。

如果是要看 80 port 被什麼所佔用，可以如下使用：

	:::bash
	lsof -i :80
	fuser 80:tcp


參考網址：  
<http://bbs.chinaunix.net/archiver/?tid-1916729.html>  
<http://www.debian-administration.org/articles/184>
