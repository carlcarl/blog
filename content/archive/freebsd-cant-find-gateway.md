Title: FreeBSD can't find gateway
Date: 2011-08-12 19:05
Author: carlcarl
Post_ID: 39
Category: FreeBSD
Tags: freebsd, gateway
Slug: freebsd-cant-find-gateway

最近 Server 卡卡的，想說把network重新啟動看看，結果果然變順很多，想說 OK 就回家了。

然後悲劇就來了......家裡完全連不上Server，好險還可以拿跟 Server 同個 Subnet 底下的機器登入，想說會不會是我之前裝幾個 Service 或防火牆的關係，但是都關掉後也都沒用 orz，後來用 `netstat
-rn` 才看到 `defaultgateway` 不見了！！

但是我明明在 `rc.conf` 裡面就有指定了 `defaultgateway`，看來好像是 `rc.conf` 只會在 OS 重啟才有用，network重啟也不會讀這個檔 = =。

後來查到可以用 `/etc/rc.d/routing restart` 來解決，不過感覺還是麻煩了點，感覺應該有更好的方法才對= =a。


