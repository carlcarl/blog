Title: MySQL insert if duplicate then update
Date: 2012-05-29 22:42
Author: carlcarl
Post_ID: 486
Category: database
Tags: mysql
Slug: mysql-insert-if-duplicate-then-update

在做壓力測試的時候發現出來的數值不太對，後來看了一下，發現是因為程式裏面是拿
SELECT 出來的資料加 1 並給 UPDATE 來使用，但是這樣並不是一個 atomic 的
operation，如果在 SELECT 完之後有其他人也進行 SELECT
就變成會拿一樣的資料且都加 1，兩個做完 UPDATE 的結果就會只是加 1
過的數據，但是預期的結果應該要是加 2 的。  
<!--more-->  
查了一下資料，發現有個簡單的語法可以使用：

	:::sql
	/* If id is the UNIQUE KEY */
	INSERT INTO table (id, num) VALUES ('1', '1') ON DUPLICATE KEY UPDATE num=num+1


它的意思就是說一開始使用 INSERT，一旦有 UNIQUE KEY 的衝突，像這裡 id
如果是跟已存在的任何一個 id 值重複的話，就會轉用使用
UPDATE，並執行你所指定的動作，以我這邊的例子就是數字(num)+1。但是這樣用有個前提就是這裡的
id 必須設定為 UNIQUE KEY 或 PRIMARY KEY。

參考網址：  

<http://stackoverflow.com/questions/6030071/mysql-table-insert-if-not-exist-otherwise-update>
