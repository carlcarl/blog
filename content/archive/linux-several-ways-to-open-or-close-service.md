Title: linux several ways to open or close service
Date: 2011-05-12 07:29
Author: carlcarl
Post_ID: 20
Category: linux
Slug: linux-several-ways-to-open-or-close-service

(如果想立即開啟或關掉就要用 service 或是直接到 /etc/init.d/ 底下去操作)

以下是用來設定在系統開啟時預設要執行的 service

在 RedHat 系列底下可以用 `chkconfig`，啟用 httpd (如果已經加到 chkconfig 裡了 就可以不用輸入第一行)

	:::bash
	chkconfig httpd --add
	chkconfig http on

 

停用 httpd (第二行是把 httpd 從 chkconfig 的管理中移除，我的建議是輸入第一行就好了)

	:::bash
	chkconfig httpd off
	chkconfig httpd --del
 

在 Debian 或 Ubuntu 底下的話 可以用 `update-rc.d` 開啟 apache2:

	:::bash
	update-rc.d apache2 defaults

關掉 apache2

	:::bash
	update-rc.d -f apache2 remove
	

至於前面提到的 service，這裡提供一些簡單的範例(找不到這個指令的話可以用套件管理找找看)

用 service 開啟 httpd

	:::bash
	service httpd start


用 service 關閉 httpd

	:::bash
	service httpd stop
 

參考網址:

<http://linuxhelp.blogspot.com/2006/04/enabling-and-disabling-services-during_01.html>
(設定較詳細)
