Title: MySQL change engine of all tables
Date: 2011-12-10 00:22
Author: carlcarl
Post_ID: 170
Category: mysql
Tags: aria, mariadb, mysql
Slug: mysql-change-engine-of-all-tables

最近裝好[mariaDB][]，想順便把之前用的 `Myisam` 改成新的 `Aria` engine，可是
table 一堆，在 phpmyadmin 介面上也找不到比較方便的功能可以直接轉換所有的
table engine。

後來查了一下，有幾種作法，一種是寫 php，然後 for 迴圈用 sql 修改
engine，不過為了這個寫 php 總是覺得很奇怪。後來查到另外一個作法：

	:::sql
	select concat('alter table ',table_name, ' engine = Aria;')
	from information_schema.tables
	where table_schema in ('db1','db2',....,'dbN')


要注意 `table_name` 不用改，這個是 `informatio_schema.tables` 中的一個欄位，`engine` 後面的 `Aria` 可以改成你要的
engine 名稱，再來是最後的 `db1, db2...` 這些，如果只有一個
database，只需要填一個就好。執行完後，會顯示出所有 alter table
的指令，接下來把這些文字全部複製輸入，就可以一口氣修改所有的 table 啦。

參考網址：  
<http://stackoverflow.com/questions/6317966>

  [mariaDB]: http://mariadb.org/
