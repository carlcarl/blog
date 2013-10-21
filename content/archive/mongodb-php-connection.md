Title: mongodb php connection
Date: 2012-08-13 22:16
Author: carlcarl
Post_ID: 589
Category: database, mongodb, php
Tags: mongodb, php
Slug: mongodb-php-connection

大概寫一下 mongodb + auth 的連線步驟，之前我是這樣做連線認証：  
<!--more-->

	:::php
	<?php
	$m = new Mongo("mongodb://localhost:27017");    
	$db = $m->mytable;
	$db->authenticate($DB_USERNAME, $DB_USERPASSWORD);
	

不過後來更新 php mongodb 的 library 後，發現 `authenticate` 這個 method
已經 deprecated 了，所以改用原本 mongodb 的建構式做連線認証：

	:::php
	<?php
	$m = new Mongo("mongodb://${DB_USERNAME}:${DB_USERPASSWORD}@localhost/mydb");
	$db = $m->mydb;


這邊要注意的一點就是，雖然在 Mongo 的建構式中已經對 mydb
做認証並通過了，但是此時回傳的 `$m` 只是 Mongo 的 object
而已，所以一旦要在某個 db 做搜尋的時候，還是必須再指定 db 才行。

另外還有個小 bug 就是，密碼一旦包括 `@` 字元的話會有錯誤，即使 escape 成
`%40` 也是一樣，不知道這部份的問題該怎麼修正就是。

參考網址：  
[http://stackoverflow.com/questions/3748252][]

  [http://stackoverflow.com/questions/3748252]: http://http://stackoverflow.com/questions/3748252
