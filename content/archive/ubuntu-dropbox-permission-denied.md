Title: Dropbox can't sync  permission denied
Date: 2011-11-23 00:28
Author: carlcarl
Post_ID: 124
Category: linux
Tags: dropbox
Slug: ubuntu-dropbox-permission-denied

最近在備份 wordpress 的資料到 dropbox
上的時候，突然出現了錯誤：`cant sync "file name" permission denied`，看了一下資料夾，只有資料夾有建立起來，但是檔案都沒 sync 成功。但是之前用了也一兩年了都沒有發生這樣的問題，為什麼
dropbox 把資料 sync 到我電腦上的時候會突然出問題呢？  

花了一段時間查了一些資料，後來才發現是因為我用 ubuntu，然後又用另外一個 `ntfs` 裝置來存 dropbox
的東西，才會有這樣的問題。解決方法就是在 `mount` 設定檔要多設定一個「uid」的參數。

首先要修改 `/etc/fstab`，範例如下：

	:::text
	/dev/sda2   /media/Data     ntfs-3g  rw,defaults,umask=0000,uid=1000  0  0


裝置和目錄的地方記得改成自己想要的，後面大致可以直接套用，不過要注意的一點是這邊的
uid 設為 1000，但是其實是要看你帳號的 uid 是多少才決定要輸入多少，你可以用 `id` 這個指令來查看你的 uid：

	:::text
	id 你的帳號

參考網址：  

[http://forums.dropbox.com/topic.php?id=18517&replies=21#post-191690][]  
<http://www.ascc.sinica.edu.tw/nl/92/1911/03.txt>

  [http://forums.dropbox.com/topic.php?id=18517&replies=21#post-191690]: http://forums.dropbox.com/topic.php?id=18517&replies=21#post-191690
