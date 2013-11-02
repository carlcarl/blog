Title: Ubuntu resolveconf setting
Date: 2013-11-02 11:00
Author: carlcarl
Post_ID: 1378
Category: ubuntu, linux
Tags: ubuntu
Slug: ubuntu_resolveconf_setting


好久沒設定 ubuntu server 了，最近在用的時候發現重開的時候，DNS 設定 (`resol.conf`) 會 reset，可是我也沒裝 NetworkManager 之類的東西啊 =.=，查了一下，是 `resolveconf` 這個套件的影響，可是我不太想直接把它移除，因為怕有啥 side effect，所以就還是照它的使用方法做，順便記錄一下該怎麼設定：


## 先刪除原本預設的 DNS 設定

	:::bash
	sudo resolvconf -d eth0.inet
	

## 新增設定檔

	::bash
	sudo mkdir -p /etc/resolvconf/resolv.conf.d
	sudo vim /etc/resolvconf/resolv.conf.d/base

## base 的內容(xxx.xxx.xxx.xxx 是你要的 DNS IP)

	:::text
	nameserver xxx.xxx.xxx.xxx
	
## 更新設定

	:::bash
	sudo resolvconf -u
	
應該這樣就可以了，其實上面這些在 [這邊][] 就有了，不過在自己的 blog 搜尋總是比較方便 XD。

[這邊]: https://code.google.com/p/collective-intelligence-framework/wiki/ResolvconfSetup_v1
