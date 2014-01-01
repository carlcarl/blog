Title: VM template can't specify hostname
Date: 2012-06-18 18:07
Author: carlcarl
Post_ID: 519
Category: linux
Tags: hostname, template
Slug: vm-template-cant-specify-hostname

這個應該很多 hypervisor 都適用，在做完 vm 的 template 之後，因為
hostname 在這裡已經固定，所以利用這個 template 再開啟一個新的 instance
的時候，hostname 會還是原本舊的，如果是用 DHCP
的方式的話，照理來說是可以拿到當初指定的 hostname 的。  
<!--more-->  
這邊我找了很多資料，本來從 hypervisor
這邊去找資料，不過都沒什麼結果，後來才發現原來從 Guest OS 這邊去修改就
OK 了，方法很簡單，在你的 VM 裡執行：

	:::bash
	sudo mv /etc/hostname /etc/hostname.old


然後重開 VM，這樣就會根據 DHCP 所指定的 hostname
來設定了。所以同樣的，為了方便，可以在做 template
之前，先執行以上的步驟，這樣之後所開的 instance 就會是指定的 hostname
了。

參考網址：  

<http://cloudstack.org/forum/6-general-discussion/8591-ubuntu-10043-server-64-bit-template-creation-issues-take-snapshot-failed--hostname-not-updating.html>
