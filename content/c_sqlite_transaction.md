Title: C SQLite Transaction
Date: 2015-02-01 11:30
Author: carlcarl
Post_ID: 1407
Category: c
Tags: c, sqlite
Slug: c_sqlite_transaction


	:::c
	sqlite3_exec(db, "BEGIN TRANSACTION;", NULL, NULL, NULL);
	
	// if error
	sqlite3_exec(db, "ROLLBACK;", NULL, NULL, NULL);
	
	//else
	sqlite3_exec(db, "END TRANSACTION;", NULL, NULL, NULL);

如果中間發生錯誤，就單做 `ROLLBACK` 就好, 不需要再做 `END TRANSACTION`，下面 ref 第二篇裡面的邏輯有點問題，做了 `ROLLBACK` 然後 `break` 出去之後又做 `COMMIT`，怪怪的。

Ref:

* [SQLITE (C/C++interface) - How to commit a transaction]
* [C++ SQLite Example with Atomic Transaction]
* [SQLite - TRANSACTIONS]

[SQLITE (C/C++interface) - How to commit a transaction]: http://stackoverflow.com/questions/2880149/sqlite-c-cinterface-how-to-commit-a-transaction
[C++ SQLite Example with Atomic Transaction]: http://www.askyb.com/cpp/c-sqlite-example-with-atomic-transaction/
[SQLite - TRANSACTIONS]: http://www.tutorialspoint.com/sqlite/sqlite_transactions.htm

