Title: MongoDB Web management tool： rockmongo
Date: 2011-09-05 18:12
Author: carlcarl
Post_ID: 43
Category: database, mongodb
Tags: mongodb, rockmongo
Slug: mongodb-rockmongo

[![1315246483-954501738][]][1315246483-954501738]

最近找到的一個管理 MongoDB 的網頁介面工具，是用 php5
寫的，介面不是說很好看啦，不過還算好用囉，而且很重要的一點是他有中文繁體，真的是倍感親切XD。

<!--more-->

首先先到[這邊下載][]。

下載完之後解壓縮並且移到網頁目錄下，然後試著連上去看看。如果出現要下載
php 的 mongodb module 的話，就照以下步驟去安裝：

	:::bash
	sudo apt-get install php-pecl
	sudo pecl install mongo


接著在 php.ini 裡面加上一行：

	:::conf
	extension=mongo.so


接著重啟 Web Server。<span style="color: #ff0000;">如果有用 php-fpm
的話記得這個也要重啟才有用</span>，一開始忘記，結果這邊卡好久=.=。再連一次網頁看看應該就可以連上了。

[![1315247147-2959807055][]][1315247147-2959807055]

預設帳密是「admin」(帳密一樣)，接著按登錄就可以進去管理頁面了。但是預設帳密一樣感覺很容易會被侵入，所以先進入管理介面增加一個管理者，可能有些人覺得很奇怪，不是有
admin 了嗎？但是其實這個 admin 是 rockmongo 本身設的登入帳號，而 MongoDB
本身裝完時並沒有所謂管理者帳號這種東西，所以別搞錯了~~。

 

[![1315247440-2431480143][]][1315247440-2431480143]

進去之後點選左邊的「admin」，接著在右邊頁面的「更多」裡，有個用戶的選項，先點進去吧。

   
[![1315247601-1427593127][]][1315247601-1427593127]

接著點選「Add User」。(這邊我已經先新增了一個使用者，原本是沒有的)。接著的頁面輸入名稱和密碼即可。

 

接著更改一下 rockmongo 的認證方式，讓他不要用他自己的驗證，而改認證
MongoDB 這邊的使用者。這邊要去修改 rockmongo 的 config
檔，以我的例子是放在 `/var/www/rockmongo/config.php` 這裡，將下面的 `false` 改為 `true` 即可。

	:::php
	<?php
	$MONGO["servers"][$i]["mongo_auth"] = false;

 

到這邊就大功告成了！以後登入時，原本預設的「admin」便無法登入，而是要用你之前新增的使用者帳密才能登入囉。

 

參考網址:  

[http://www.php.net/manual/en/mongo.installation.php#mongo.installation.nix][]

  [1315246483-954501738]: http://i.imgur.com/BtTNDdsl.png
  [這邊下載]: http://code.google.com/p/rock-php/downloads/list
  [1315247147-2959807055]: http://i.imgur.com/epxeSLs.png
  [1315247440-2431480143]: http://i.imgur.com/kSM5gdil.png
  [1315247601-1427593127]: http://i.imgur.com/sGefpoV.png
  [http://www.php.net/manual/en/mongo.installation.php#mongo.installation.nix]: http://www.php.net/manual/en/mongo.installation.php#mongo.installation.nix
