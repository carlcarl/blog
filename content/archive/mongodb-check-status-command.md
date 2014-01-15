Title: MongoDB check status command
Date: 2012-10-09 02:15
Author: carlcarl
Post_ID: 663
Category: database
Tags: mongodb
Slug: mongodb-check-status-command

紀錄一下 MongoDB 看狀態時常會用到的指令。  

	:::bash
	# 看目前 state 的指令
	mongostat


以下都是進 mongo shell 後的指令。

	:::javascript
	// 狀態總覽
	db.serverStatus()

	// 看 memory
	db.serverStatus().mem

	// 看 page fault
	db.serverStatus().extra_info

	// 看 sharding 的狀態，兩個指令同樣功能
	db.printShardingStatus()
	sh.status()

	// 查看 db 本身的資訊
	db.stats()

	// 查看 collection 的 index
	db.xxx.getIndexes()

	// 查看目前執行的 operation
	db.currentOP()


參考網址：  
<http://docs.mongodb.org/manual/reference/server-status-index/>  
<http://www.mongodb.org/display/DOCS/Sharding+Administration>  
<http://docs.mongodb.org/manual/reference/database-statistics/>  
<http://www.mongodb.org/display/DOCS/Indexes>
