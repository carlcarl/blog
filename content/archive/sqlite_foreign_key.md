Title: SQLite Foreign Key Support
Date: 2015-01-21 11:00
Author: carlcarl
Post_ID: 1404
Category: database
Tags: sqlite
Slug: sqlite_foreign_key_support


SQLite 在設定完 foreign key 之後，對 foreign key 的限制卻沒有生效，例如有一個 table 只有 id=1，但是我在另外一個 table 參照這個 table，並加入 foreign key id=2，是會過的，但是應該是要擋掉才對。查了一下，發現預設並不會開啟= =|||。所以必須在每次的 DB connection 時，都需要做一次這個動作：

	:::sql
	PRAGMA foreign_keys = ON;

直接用 `sqlite3_exec` 之類的執行就可以了。

Ref:  

* [SQLite Foreign Key Support]  
* [Sqlite Foreign Key]  
* [sqlite3 foreign keys on PDO]  

[SQLite Foreign Key Support]: http://www.sqlite.org/foreignkeys.html
[Sqlite Foreign Key]: http://leeleeju.blogspot.tw/2012/09/sqlite-foreign-key.html
[sqlite3 foreign keys on PDO]: http://stackoverflow.com/questions/13534040/sqlite3-foreign-keys-on-pdo
