Title: PHP: Unable to allocate memory for pool
Date: 2013-06-10 22:29
Author: carlcarl
Post_ID: 961
Category: php
Tags: apc, nginx, php
Slug: php-unable-to-allocate-memory-for-pool

其實本來一開始的問題是 nginx 突然出現 `404 bad gateway`，後來去看 log
才發現這個錯誤，所以看來如果出現 bad gateway
的問題的話，可能就是跟後端的連線出了問題這樣。

查了一下資料，發現到[這篇][]說可能是 php apc
的關係，剛好我也有裝，於是跟著把 `apc.shm_size` 調大之後並重開就 OK 了。

不過老實說不能確定是因為重開，還是因為 cache
有調大的關係。可能之後還要再觀察看看，目前過了幾天，看起來是都沒問題這樣～～。

  [這篇]: http://www.cyberciti.biz/faq/linux-unix-php-warning-unable-to-allocate-memory-for-pool/
