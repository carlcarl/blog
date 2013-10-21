Title: KDE dolphin network folder ssh fail
Date: 2013-02-28 02:02
Author: carlcarl
Post_ID: 794
Category: KDE, linux
Tags: dolphin, ssh
Slug: kde-dolphin-network-folder-ssh-fail

鬼打牆的小問題，感覺比較像 bug ，想說還是筆記下來好了。

解決方法：  
把 `~/.ssh/known_hosts` 中，找到要連線的 host 那行，然後把那行刪掉，
dolphin 這邊再重連就能夠連上了。

參考連結：  

<http://superuser.com/questions/299940/kubuntu-cant-add-new-ssh-network-folder>
