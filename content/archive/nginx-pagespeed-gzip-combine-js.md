Title: nginx pagespeed gzip combine js
Date: 2013-06-16 23:10
Author: carlcarl
Post_ID: 1043
Category: linux
Tags: nginx, pagespeed
Slug: nginx-pagespeed-gzip-combine-js

在用 [GTmetrix][] 看網站的效能的時候，發現只有 pagespeed combine 出來的
js，沒有被 gzip 處理過。

google 了一下，在 [Github 上也找到同樣的問題][]，裡面說要加上
`application/javascript`，回頭看了一下我的 nginx 設定檔，果然沒加到= =。

我原本設定是
`gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript`，想說該設的都設了，想不到還是有漏網之魚，加上之後重啟，果然就 OK 哩。

附帶一提，我把 wp-minify 這個外掛也拿掉了，因為 pagespeed
基本上算是可以取代掉它了（而且 wp-minfiy 還有一些怪怪的 bug...）。

  [GTmetrix]: http://gtmetrix.com
  [Github 上也找到同樣的問題]: https://github.com/pagespeed/ngx_pagespeed/issues/368
