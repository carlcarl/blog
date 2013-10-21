Title: centos6.2 timezone「tzselect」
Date: 2012-02-24 00:32
Author: carlcarl
Post_ID: 273
Category: linux
Tags: centos, ntp, timezone, tzselect
Slug: centos6-2-timezone-tzselect

最近在裝 centos
來用的時候，在設定的時候也用了 `ntpd` 來同步時間，不過發現一直沒辦法把時間弄正常，即使我把
ntp server
換成台灣的也一樣，後來想到了之前有用過的辦法，用 `/usr/share/zone/info/Asia/Taipei` 覆蓋掉 `/etc/localtime`，結果還是不行（之前這樣用有成功過的說 QQ）。

後來查到一個好像更好的辦法，就是用 `tzselect` 這個指令，執行後會出現互動式介面，照著選時區，設定完就正常啦～～。

參考網址：  
<http://bbs.bitscn.com/146159>
