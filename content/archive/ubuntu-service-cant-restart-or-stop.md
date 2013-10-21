Title: Ubuntu service can't restart or stop
Date: 2013-06-03 11:48
Author: carlcarl
Post_ID: 873
Category: linux
Tags: nginx, ubuntu
Slug: ubuntu-service-cant-restart-or-stop

在自己編 nginx 的時候遇到的小問題，因為自己裝的 conf 設定和原本 Ubuntu
repo 裡的的不一樣，然後 init script 我是用 repo 裡提供的。

看了一下 repo 提供的 init script，似乎是因為找不到 start service 所建立的
pid 檔案，google 了一下，在 stackoverflow
找到 [這篇問題][] 剛好和我遇到的情況一樣，check 了一下 nginx conf 裡的 pid
檔案位置和 init script 裡的 pid
檔案位置，發現設定並不一樣，改成一樣後，問題就解決了～～。

  [這篇問題]: http://stackoverflow.com/questions/10939072/add-nginx-as-a-ubuntu-service-stop-and-reload-doesnt-work
