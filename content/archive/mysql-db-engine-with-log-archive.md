Title: MySQL DB engine with log: Archive
Date: 2011-12-17 18:00
Author: carlcarl
Post_ID: 226
Category: database
Tags: archive, innodb, mariadb, myisam, mysql
Slug: mysql-db-engine-with-log-archive

前一陣子在看什麼 engine 比較適合拿來單純存
log，後來看到 `Archive` 這個似乎不錯，主要有以下優點：

-   insert 速度更快。
-   佔的資料量較 Myisam 少。

但是有優勢，就會有相對的劣勢，Archive 有以下缺點：

-   不支援 delete 和 update，只能 insert 和 select。
-   不支援 index。

（如果你是想要存每次最後登入時間的話，那 Archive 的確是不適合，因為不支援
index 和 update。）

但是以現實角度來看單純的 log 表，像是存每次登入的紀錄：

-   其實真的就只會用到 insert，會用到 delete 和 update 那這個應該不太叫
    log。
-   作 select 的機率也是微乎其微，log
    表通常也只有出事的時候會拿出來作搜尋唄。
-   不支援 index，但是老實說，insert 和 select
    的次數比率差太多了，如果真的能建 index，那每次 insert
    都會為建立索引這個動作付出額外的成本，實際上應該是劃不來的。
-   資料表越來越大該怎麼辦？這邊我是還沒實際用過，不過也可以 dump
    出來或是額外命名，再建一個新的空 table 來裝應該也是可以。

那可能很多人會覺得看到大家說他 insert 效能比較好，所以就直接改用 Archive
engine 存 log，不過有時候換 engine
其實也會跟資料庫的參數設定有很大的關係，換了也不一定效能會比較好，像是
Myisam 換成
InnoDB，處理並發量也不一定會比較好，如果你的參數設定還是用原本 Myisam
的話=.=。為了確認在我的環境中是否也是如此，所以就做了一下實驗啦～。

我的 MySQL config 檔案參數主要是以 Myisam
去作調校，InnoDB的部份就沒有作設定哩，主要是試驗是否在此設定中 Archive
的效能還是能比 Myisam 為佳。實驗工具採用「mysqlslap」，實驗內容為5個同時
insert query，各個數量皆為一千三百上下，每個 engine
的實驗都跑五次，數據會較為客觀一點，至於建立的資料表內容這裡就先省略哩，有點懶得打XD。另外由於我實際上是用
MySQL 的 fork 版本 `MaraiDB`，所以順便附上新 engine
 `Aria` 的測試結果。

	:::text
	Myisam：  
	Benchmark  
	Average number of seconds to run all queries: 0.271 seconds  
	Minimum number of seconds to run all queries: 0.263 seconds  
	Maximum number of seconds to run all queries: 0.297 seconds  
	Number of clients running queries: 5  
	Average number of queries per client: 1338

	Aria：  
	Benchmark  
	Average number of seconds to run all queries: 3.103 seconds  
	Minimum number of seconds to run all queries: 3.062 seconds  
	Maximum number of seconds to run all queries: 3.137 seconds  
	Number of clients running queries: 5  
	Average number of queries per client: 1338

	Archive：  
	Benchmark  
	Average number of seconds to run all queries: 0.149 seconds  
	Minimum number of seconds to run all queries: 0.145 seconds  
	Maximum number of seconds to run all queries: 0.158 seconds  
	Number of clients running queries: 5  
	Average number of queries per client: 1338

從數據可以看出 Archive 在 insert 效能上的確是最好的。至於 Aria
明顯很慢，不知道是不是我沒有調校 Aria
的參數設定的關係，這部份可能之後還需要再作驗證就是了。select
的數據應該就不用試了，不能建 index，怎樣都一定會被其他 engine 打死。

參考網址：  
<http://dev.mysql.com/doc/refman/5.1/en/archive-storage-engine.html>  
<http://60.29.242.49/?p=60>
