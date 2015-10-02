Title: OS X xhyve virtualization
Date: 2015-10-03 02:00
Author: carlcarl
Post_ID: 1433
Category: mac
Tags: xhyve
Slug: osx_xhyve

[xhyve] 是最近看到的虛擬化技術，源自於 [FreeBSD] 的 [bhyve]，試了一下，大致上沒啥問題，還滿順利的。

範例是照這篇 [xhyve を試してみた] 來做，從 xhyve->docker->ubuntu 這樣，感覺之後拿來在 OSX 上弄 docker 相關的部署會蠻方便的，另外還有一篇 [Mac OS X 上基於 FreeBSD/bhyve 的虛擬技術 xhyve]，中文講解，流程是直接從 xhyve->ubuntu，然後是透過 iso 檔安裝的方式，不過步驟就阿雜多了。

以後要想辦法逼自己多筆記一些資料啊，這樣懶下去不是辦法XD。


[xhyve]: https://github.com/mist64/xhyve
[FreeBSD]: https://www.freebsd.org/
[bhyve]: http://bhyve.org/
[xhyve を試してみた]: http://blog.holidayworking.org/entry/2015/06/15/xhyve_を試してみた
[Mac OS X 上基於 FreeBSD/bhyve 的虛擬技術 xhyve]: http://www.vpsee.com/2015/06/mac-os-x-hypervisor-xhyve-based-on-bhyve/