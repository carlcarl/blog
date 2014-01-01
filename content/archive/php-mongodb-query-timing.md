Title: PHP MongoDB query timing
Date: 2012-10-12 03:19
Author: carlcarl
Post_ID: 680
Category: database
Tags: mongodb, php
Slug: php-mongodb-query-timing

最近在用 PHP 在對 MongoDB 作壓力測試的時候，發現怎麼我 1 shard 和 3
shards 的 performance 會一樣，卡了很久後來才發現原來是我搞錯 MongoDB
query 的時機，所以在測試的時候，query 其實都沒有發出，難怪數據會一樣。  

在 PHP 的 [manual][] 裡有說明，以下拿它的範例程式來說明 query 的時機：

	:::php
	<?php
	$cursor = $collection->find()->limit(10);
	// query 還沒發出

	$cursor = $cursor->sort(array("a" => 1));
	// query 還是沒發出
	
	var_dump($cursor->getNext()); // 這時才發出 query


也就是說，query 回傳的是一個 cursor ，必須對這個 cursor
操作或取值，才會實際發出 query ，這邊它提供了兩個方法：

	:::php
	<?php
	// 方法 1
	foreach ($cursor as $doc) 
	{
    	// do something to each document or do nothing
	}

	// 方法 2
	$cursor->getNext()


另外再補充一點，有些人可能會問：做完 `find()` 再做 `limit()`
，那資料傳的部份是 limit() 前還是之後的？  
答案是 **之後的** ，因為在做 `limit()` 時，這時候只是對 cursor
作設定，還沒實際發出 query，等到後面拿值的時候，才會發出 query ，這時的
query 就包含了 `find()` 和 `limit()` 的條件了。

參考網址：  

<http://stackoverflow.com/questions/10862109/does-mongodb-limit-load-all-the-documents-in-memory>  
<http://derickrethans.nl/cursors-in-mongodb.html>

  [manual]: http://php.net/manual/en/class.mongocursor.php
