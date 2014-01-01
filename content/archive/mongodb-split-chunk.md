Title: MongoDB split chunk
Date: 2012-10-09 03:21
Author: carlcarl
Post_ID: 671
Category: database
Tags: mongodb
Slug: mongodb-split-chunk

練習了一下自己手動切 chunk，因為有時候 MongoDB
切出來的不一定是理想的範圍 orz。

大致就兩個步驟，第一個是切 chunk，第二個是移動 chunk 到某個 shard
上，如果 balancer 沒關掉的話，第二個步驟會由 balancer 幫你決定你的 chunk
要移到哪個 shard 上。  
<!--more-->  

### 切 chunk 指令

	:::javascript
	// 第一個參數是指定在哪個 DB 中的 collection，
	// 因為文件裡只說是 collection，所以可能會忘了加上 DB 的名稱
	// 第二個參數是你指定的 sharding key，cutPoint 則是要從哪個數值下去切
	sh.splitAt("yourDB.yourCollection", {key:cutPoint})


or

	:::javascript
	db.runCommand({split:"yourDB.yourcollection", middle:{key:cutPoint}})


### 移動 chunk 指令

	:::javascript
	// 第一個參數是指定在哪個 DB 中的 collection
	// 第二個參數是你指定的 sharding key，cutPoint 則是要從哪個數值下去切
	// 第三個參數是要移到哪個 shard
	sh.moveChunk("yourDB.yourCollection", {key:cutPoint}, "shardName")


or

	:::javascript
	db.runCommand({moveChunk:"yourDB.yourCollection",find:	{key:cutPoint},to:"shardName"})

你會發現這邊有兩個用法，一個是 `sh` 開頭 (表示是 sharding
相關的指令)，一個是 `db` 開頭，如果是在 mongo shell 裡操作的話，`sh`
會較好用，因為 `db` 這邊的操作必須在 `admin` 這個 database
中才能執行，所以會多了 admin 和原來的 database 間的轉換，較為麻煩。

參考網址：  
<http://docs.mongodb.org/manual/reference/method/sh.splitAt/>  
<http://docs.mongodb.org/manual/reference/method/sh.moveChunk/>  
<http://hedatou.com/archives/introduction_to_mongodb.html>
