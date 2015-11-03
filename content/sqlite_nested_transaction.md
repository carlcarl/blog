Title: SQLite nested transaction
Date: 2015-11-03 21:30
Author: carlcarl
Post_ID: 1434
Category: programming
Tags: sqlite
Slug: sqlite_nested_transaction


遇到 SQLite 需要 nested transaction 的情況，查了一下，似乎沒辦法直接用 `TRANSACTION` 做。後來是看到另外一個語法 `SAVEPOINT` 可以解決這樣的問題，而且一般的 SQL DB 好像也都支援。以下是相關的用法：

	:::sql
	SAVEPOINT savepoint_name
	
	RELEASE savepoint_name
	
	ROLLBACK TO SAVEPOINT savepoint_name

`savepoint_name` 就取自己要的名稱，需要做 nested 的情況下就用不同的 `savepoint_name`，也可以外層用 `SAVEPOINT`，內層用 `TRANSACTION`；但是不能外層是 `TRANSACTION`，內層用 `SAVEPOINT` 這樣。

參考資料：

* [SQLite 語法]
* [How to use savepoints in SQLite3 in Objective-C]
* [How to avoid nested transactions]


[SQLite 語法]: http://www.runoob.com/sqlite/sqlite-syntax.html
[How to use savepoints in SQLite3 in Objective-C]: http://stackoverflow.com/questions/13455733/how-to-use-savepoints-in-sqlite3-in-objective-c
[How to avoid nested transactions]: http://stackoverflow.com/questions/14444701/how-to-avoid-nested-transactions