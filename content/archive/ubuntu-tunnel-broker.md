Title: Ubuntu Tunnel Broker IPv6 連 中研院
Date: 2012-05-04 16:36
Author: carlcarl
Post_ID: 397
Category: linux
Tags: ipv6, tunnel broker, ubuntu
Slug: ubuntu-tunnel-broker



最近看到有人用 [Archlinux 設定 Tunnel Broker
的方法][]，所以研究了一下該怎麼用，發現還滿簡單的0.0。

### 申請帳號

到 <http://tb2.ipv6.ascc.net/> 註冊一個帳號。

 

### 安裝 gogoc

	:::bash
	sudo apt-get install gogoc

 

### 設定 gogoc (`/etc/gogoc/gogoc.conf`)
`if_prefix` 要看你的網卡裝置名稱叫啥，不過預設應該都是 eth0。

	:::text
    userid=你的帳號
    passwd=你的密碼
    server=tb2.ipv6.ascc.net
    auth_method=digest-md5
    host_type=host
    prefixlen=64
    if_prefix=eth0

 

### 開啟 gogoc

	:::bash
	sudo /etc/init.d/gogoc start

 

### 網頁測試
<http://test-ipv6.com/>  
<http://ipv6day.tw/20helper.html>

![ipv6 test][]  
![ipv6 test2][]

  [Archlinux 設定 Tunnel Broker 的方法]: http://planykao.blogspot.com/2012/04/archlinux-ipv6-tunnel-broker.html
  [ipv6 test]: http://i.imgur.com/IxTtYxBl.png
  [ipv6 test2]: http://i.imgur.com/tcbmCvdm.png
