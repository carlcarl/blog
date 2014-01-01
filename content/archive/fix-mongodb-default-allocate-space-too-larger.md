Title: fix mongodb default allocate space too larger
Date: 2012-07-27 20:19
Author: carlcarl
Post_ID: 546
Category: database
Tags: mongodb
Slug: fix-mongodb-default-allocate-space-too-larger

最近在做 VM template 的時候才發現到這個問題，安裝好 mongodb 之後，在
`/var/lib/mongodb/journal/` 下面可以發現 mongodb 佔用了 3 GB 的 journal
檔案。

當然，如果硬碟夠大或是沒啥必要的話，這其實可以不用去理它，但是我由於需要加快利用
VM template 安裝系統的速度，而 template 的大小會影響中間網路傳送
template 的時間，因此還是希望能避免不必要的空間浪費。

而其實 mongodb 本身有提供一個參數 `smallfiles`
，這個參數可以讓這些預先生成的 journal 檔案一個從 1G 降到約 13X MB
左右，所以總共 3 個 journal file 會從原本的 3 GB 降到約 400 MB 大小。

如果是用 command line 的方式，就加上 `--smallfiles`
，如果是設定檔的方式，就在設定檔裡加上 `smallfiles = true` ，接著將
`/var/lib/mongodb/journal/prealloc.x` 給刪掉 (x 是數字)，然後重啟
mongodb
，重啟完再察看檔案大小是否有改掉，如果沒有的話可以嘗試重啟幾遍試試看唄。

參考網址：  
<http://www.mongodb.org/display/DOCS/Command+Line+Parameters>
