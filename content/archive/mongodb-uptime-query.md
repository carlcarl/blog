Title: MongoDB uptime query
Date: 2012-11-15 07:33
Author: carlcarl
Post_ID: 721
Category: database, mongodb
Tags: mongodb, uptime
Slug: mongodb-uptime-query

在 [stackoverflow][]
看到這個問題，就順便查個資料回了一下，另外有個人是回答可以用 `ps -ef`
來看，不過我想說 MongoDB 本身應該也會有這樣的功能，所以還是查了一下。

<!--more-->

後來果然在 [MongoDB 官方文件][]
找到我要的資料，不過拿到的數據會是以秒為單位，所以必須自己作轉換。

進入 mongo shell 之後輸入：

	:::javascript
	// seconds
	db.serverStatus().uptime


其他的就照單位轉換一下就可以：

	:::javascript
	// minutes
	db.serverStatus().uptime / 60
	// hours
	db.serverStatus().uptime / 3600
	// days
	db.serverStatus().uptime / 86400


如果要固定格式的話，目前似乎沒有直接的 function 可以 call，所以還是必須自己作轉換，像是 [這篇][] 。

  [stackoverflow]: http://stackoverflow.com/questions/13379170/how-long-was-a-mongo-instance-running
  [MongoDB 官方文件]: http://docs.mongodb.org/manual/reference/server-status/
  [這篇]: http://stackoverflow.com/questions/175554/how-to-convert-milliseconds-into-human-readable-form
