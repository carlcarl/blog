Title: ipk unarchive
Date: 2013-07-17 16:27
Author: carlcarl
Post_ID: 1224
Category: linux
Tags: ipk, tar
Slug: ipk-unarchive

記錄一下:P

查了一下資料，有些說直接用 `tar`
就可以了，不過怎麼試就是不行zzzzzz。後來看到 [stackoverflow][]
上有人提供的方法，試了一下就成功了 XD。

先用 `ar x xxx.ipk` 就可以解壓縮出幾個檔案，其中 `data.tar.gz`
放的就是程式執行檔之類的，`control.tar.gz` 放的是 ipk 的一些
information。

接下來用 `tar -xf data.tar.gz` or `tar -xf control.tar.gz`
就可以看到裡面的資料了。

  [stackoverflow]: http://stackoverflow.com/questions/17369127/extracting-and-creating-ipk-files
