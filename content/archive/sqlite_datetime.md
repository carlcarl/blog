Title: SQLite datetime 
Date: 2015-01-19 15:00
Author: carlcarl
Post_ID: 1403
Category: database
Tags: sqlite
Slug: sqlite_datetime


一開始以為只要直接 insert timestmap，它就會自動幫我轉，不過好像沒那麼簡單...，原本我是用以下語法:

	:::sql
	INSERT INTO tbl(tx_bytes, rx_bytes, timestamp) VALUES(?, ?, ?);


`timestamp` 這裏是 `datetime` type，可是當我要比較時間的時候:

	:::sql
	SELECT * FROM tbl WHERE timestamp >= '2015-01-01' AND timestamp < '2015-02-01';

結果會完全沒任何東西，後來查了一下，[發現它存的時候是用字串存]囧，在輸入之前需要自己做轉換，所以會變成:

	:::sql
	INSERT INTO data_planner(tx_bytes, rx_bytes, timestamp) VALUES(?, ?, datetime(?, 'unixepoch', 'localtime'));


`localtime` 表示轉成自己所在的時區，不然預設會在 `utc+0`。


Ref:  
[How do I insert datetime value into a SQLite database?]  


[發現它存的時候是用字串存]: http://pro.ctlok.com/2010/08/sqlite-date-time.html
[How do I insert datetime value into a SQLite database?]: http://stackoverflow.com/questions/1933720/how-do-i-insert-datetime-value-into-a-sqlite-database
