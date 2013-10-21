Title: Ubuntu 11.04 install mongoDB
Date: 2011-09-04 14:28
Author: carlcarl
Post_ID: 42
Category: linux, mongodb
Tags: mongodb
Slug: ubuntu-11-04-install-mongodb

[![1315146936-3546835831][]][1315146936-3546835831]

安裝的步驟比我想得還要多，本來想說應該用套件安裝就好，不過好像不行，所以 google 了一下，找到一個還算簡單的方法：

	:::bash
	sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10


接下來在 `/etc/apt/sources.list` 新增下面一行：

	:::bash
	deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen


接著更新並安裝：

	:::bash
	sudo apt-get update
	sudo apt-get install mongodb-10gen


裝完之後就會自動當作 daemon 來執行，要確認的話可以輸入：

	:::bash
	sudo netstat -antp | grep mongo
 

參考網址：  
<http://www.mongodb.org/display/DOCS/Ubuntu+and+Debian+packages>

  [1315146936-3546835831]: http://i.imgur.com/iAdD5Sfl.png
