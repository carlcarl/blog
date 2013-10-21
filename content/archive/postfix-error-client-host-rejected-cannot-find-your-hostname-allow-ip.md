Title: postfix error: Client host rejected: cannot find your hostname allow ip
Date: 2011-10-28 13:16
Author: carlcarl
Post_ID: 48
Category: linux
Tags: postfix
Slug: postfix-error-client-host-rejected-cannot-find-your-hostname-allow-ip

最近用了一個 public ip 開了個 svn + trac server，大致上都還滿順利的，不過在測試寄信到 mail
server 的時候卻出現了錯誤，看了一下 log 檔，訊息是 `Client host rejected: cannot find your hostname allow ip`。

不知道可能是 mail server 找不到 svn server 的 hostname 還是怎樣，然後試了一些方法好像也都不行，最後想說直接在 `/etc/hosts` 裡直接加上「ip」和自定義「hostname」看看，結果就 OK 哩，個人覺得這個方法算是還滿不錯的，不過前提是要有 mail server 的權限就是了。

以下是一個簡單的設定例子

	:::text
	111.111.111.111 svn.domain.com.tw svn
	
