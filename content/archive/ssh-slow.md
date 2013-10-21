Title: ssh slow
Date: 2011-10-27 20:41
Author: carlcarl
Post_ID: 47
Category: linux
Tags: ssh
Slug: ssh-slow

貌似是學校最近 DNS 常出問題還是怎樣，ssh 的速度非常緩慢，後來決定把 config 檔案改一改，改完之後速度果然快很多= =+。

修改 `/etc/ssh/sshd_config`，以下是修改內容：

	:::text
	UseDNS no
	GSSAPIAuthentication no


修改完後執行：

	:::bash
	sudo /etc/init.d/ssh restart

 

 收工~，不過如果 DNS 沒問題的話，可能修改這個設定速度不會差太多。

 

參考網址：

[http://jeffxie.blog.51cto.com/1365360/293869][]  
<http://www.dk101.com/Discuz/viewthread.php?tid=157716>  

  [http://jeffxie.blog.51cto.com/1365360/293869]: http://www.dk101.com/Discuz/viewthread.php?tid=157716
