Title: postfix-modify-setting-after-installation
Date: 2011-04-17 11:31
Author: carlcarl
Post_ID: 16
Category: linux
Slug: postfix-modify-setting-after-installation

之前在裝的時候沒有設定到，結果後來也不知道怎麼再去設定畫面，後來查到了:

	:::bash
	sudo apt-get install --reinstall postfix
	sudo dpkg-reconfigure postfix

 

第一行是重新安裝，第二行是再次設定。下完後就會進入設定畫面了~。
