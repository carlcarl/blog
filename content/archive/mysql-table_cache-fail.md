Title: MySQL table_cache fail
Date: 2012-05-31 15:26
Author: carlcarl
Post_ID: 495
Category: database
Tags: mysql, table_cache
Slug: mysql-table_cache-fail

一直記得之前好像遇過同樣的問題，後來才想到應該是 ulimit 的限制。ulimit
會限制一個 user 可開啟的檔案，MySQL 也不例外，預設會被限制在最多開 1024
個檔案，以下是跟 MySQL 有關的算式：

	:::text
	max_open_files = max_connections + (table_cache * 2)

`max_open_files` 基本上是固定 1024，所以後面的部份一旦自己設太大，MySQL
會自己再調整參數，所以可能會遇到你將 `max_connections` 設到
1024、`table_cache` 設到512，可是在 MySQL command line
中去查，`table_cache` 卻還是預設 64 的情形，`max_connections`
的值也會同樣被降低。

要預防這種情形就必須修改 `ulimit` 限制，在 `/etc/security/limits.conf` 加上

	:::conf
	mysql soft nofile 4096
    mysql hard nofile 8192

接著重開 MySQL 即可。

參考網址：  
<http://www.neweguo.com/club/display.asp?id=44>
