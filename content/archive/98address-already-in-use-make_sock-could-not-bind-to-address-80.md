Title: (98)Address already in use: make_sock: could not bind to address 80
Date: 2011-12-05 19:37
Author: carlcarl
Post_ID: 166
Category: linux
Tags: fuser, ubuntu
Slug: 98address-already-in-use-make_sock-could-not-bind-to-address-80

最近在重開 server 的時候突然發現 apache
怎麼沒有開，重開之後就出現如標題的錯誤，查了一下，應該是有個莫名的
process 把 port 給 bind 住了，用了一堆指令，一直 kill
process，結果怎麼好像都沒用囧，後來才試到一個可以解決的指令：

	:::bash
	sudo fuser 80/tcp

執行之後就會顯示是哪個 process id 佔住的。  
很奇怪的是我使用「netstat」去看居然是找不到的=
=，另外要注意的是記得使用「sudo」或者是用 root
來查看，不然有可能會看不到。砍掉之後，再開啟 apache
就可以成功開啟了，算是一個滿怪的問題，當初忙著砍掉，忘記先查看 process
的名稱是什麼，只能先紀錄起來，下次如果還是發生一樣的情況的話，再來看看哩。

參考網址：  

<http://www.chriskirkland.net/news/76_Apache---Address-already-in-use:-make_sock:-could-not-bind-to-address.html>  
<http://www.wallpaperama.com/forums/98address-already-in-use-make-sock-could-not-bind-to-address-80-t1091.html>  
<http://www.linuxquestions.org/questions/linux-software-2/98-address-already-in-use-make_sock-could-not-bind-to-address-0-0-0-0-443-a-110753/>  
<http://www.directadmin.com/forum/showthread.php?t=33412&page=1>
