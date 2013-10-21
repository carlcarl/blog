Title: Ubuntu VPN Server with pptp
Date: 2011-07-16 12:11
Author: carlcarl
Post_ID: 36
Category: linux
Slug: ubuntu-vpn-server-with-pptp

最近想架 VPN Server，查了一下資料，最常見的好像是 `OpenVPN` 和 `pptp` 兩種方法。pptp 的方式比較簡單，但是相對於 OpenVPN 較為不安全，是說我們系上的好像也是用 pptp，所以我想問題應該不大吧

網路環境：

- 使用Public IP
- 單網卡

 

### 首先要先安裝 `pptpd`

	:::bash
	sudo apt-get install pptpd

 

### 接著修改 `/etc/pptpd.conf`

這邊 `localip` 是 Server 連線之後要用的 IP，基本上跟 Server 本身的 Public IP沒有關係，可以給個 private ip 就 ok 了，`remoteip` 是給 VPN client的 private
ip，大致給個範圍，可以不用像我一樣給了 128 個 Private IP，應該是要看同時會有多少人使用來給範圍，至於為什麼我要從 128 開始，是因為我想保留前面的部份當作另外的用途:

	:::bash
	localip 192.168.0.1
	remoteip 192.168.0.128-255

 

### 再下來是修改 `/etc/ppp/pptpd-options`

這邊要注意一下裡面的 name 設定，通常會設成是 `pptpd`，之後要跟 `/etc/ppp/chap-secrets` 裡的設定作對應，另外還有要設定 `ms-dns`，就看那台 Server 原本指定的 DNS IP，拿過來用就 ok 了。要看 DNS IP 設定可以到 `/etc/resolve.conf` 裡面去看。

 

### 設定完後接下來就是帳號密碼的部份啦

修改 `/etc/ppp/chap/secrets`，以下是大概的格式，這邊要注意 `pptpd` 是對應之前同樣的文字部份，`*` 表示不從這邊設定 IP，而是讀剛才的 `remoteip` 設定:

	:::text
	你要的帳號 pptpd 你要的密碼 *

 

### 重啟pptpd

	:::bash
	sudo /etc/init.d/pptpd restart


接下來試試看 VPN 連線看看，我的情形是還不行啦XD。查了一下資料，應該是有指定到 private
ip，但是封包在 Server 這邊傳不出去，因為沒設定，所以接下來還要再設定一下 NAT 的部份啦。

 

### 設定 iptables

	:::bash
	sudo iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o eth0 -j MASQUERADE


但是這樣的設定在每次重開機之後就會消失，所以設定完後可以用 `iptables-save` 將設定檔存起來，如：

	:::bash
	sudo iptables-save > /etc/iptables-rules

如果出現權限問題就 `sudo su` 轉成 root 再做。但是存起來之後，他並不會幫你在每次重開機都讀那個檔，所以還要再設定，修改 `/etc/network/interfaces`，最後面加上：

	:::bash
	pre-up iptables-restore < /etc/iptables-rules

 

### 最後是修改 `/etc/sysctl.conf`

找到以下這行，將前面的 `#` 給刪掉， `#` 是代表註解，這樣才有forward 封包的功能

	:::conf
	# net.ipv4.ip_forward=1
 

### 改完之後，更新 sysctl 的設定

	:::bash
	sudo sysctl -p

 

OK! 到這裡之後應該是就可以連 VPN 了，如果還不行的話，可以重啟動看看，再不行的話，可以參考看看我下面的參考網頁，也許會有對你有用的資訊。

 

參考網頁:  
<http://www.eubuntu.net/viewthread.php?tid=135&sid=ihmKhL>  
<http://blog.slps.tp.edu.tw/00086/?p=145>  
<http://gsyan888.blogspot.com/2009/11/ubuntu-vpn-server.html>  
<https://wangyan.org/blog/debian-pptp-vpn.html>  
<http://jordy.easymorse.com/?p=272>  
