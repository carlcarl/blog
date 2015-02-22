Title: SQLite datetime group by
Date: 2015-02-22 23:10
Author: carlcarl
Post_ID: 1412
Category: database
Tags: sqlite
Slug: sqlite_datetime_group_by


SQLite 裡的 `datetime` 其實也只是 string 而已，所以用的方式跟 MySQL 之類的不同，MySQL 可以直接 `Date(xxx)` 或是 `Month(xxx)` 之類的做擷取，不過 SQLite 要用 `strftime` 來做，例如:

	:::sql
	SELECT strftime('%Y',datetime) AS year, 
       strftime('%m',datetime) AS month, 
       sum(amount) AS Amount 
	FROM mytable 
	GROUP BY year


Ref:

* [SQL combining GROUP BY and SUM]
* [MySQL/SQL: Group by date only on a Datetime column]


[SQL combining GROUP BY and SUM]: stackoverflow.com/questions/1639906/sql-combining-group-by-and-sum
[MySQL/SQL: Group by date only on a Datetime column]: http://stackoverflow.com/questions/366603/mysql-sql-group-by-date-only-on-a-datetime-column

