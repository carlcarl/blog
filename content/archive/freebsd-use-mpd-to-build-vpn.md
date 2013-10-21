Title: FreeBSD use mpd to build VPN
Date: 2011-07-22 09:43
Author: carlcarl
Post_ID: 37
Category: FreeBSD
Slug: freebsd-use-mpd-to-build-vpn

不習慣用FreeBSD，所以花了一點時間研究要怎麼裝orz

感覺比Linux的還麻煩QQ

 

### 首先先裝 mpd

到 `/usr/ports/net/mpd/` 底下輸入

	:::bash
	make install clean

這樣就安裝好了~。

 

### 接下來是要作設定，先修改 `/usr/local/etc/mpd/mpd.conf` 

	:::conf
	default:
	load pptp1
	pptp1:
	new -i ng0 pptp1 pptp1
	set ipcp ranges 192.168.88.1/32 192.168.88.56/32
	load pptp_def
	pptp_def:
	set iface disable on-demand
	set iface enable proxy-arp
	set iface idle 0
	set iface enable tcpmssfix
	set bundle enable multilink
	set link yes acfcomp protocomp
	set link no pap chap
	set link enable chap-msv2
	set link keep-alive 10 60
	set link mtu 1460
	set ipcp yes vjcomp
	set ipcp dns   <yourDNS Server IP>    
	set ipcp nbns 192.168.88.1
	set bundle enable compression
	set ccp yes mppc
	set ccp yes mpp-e40
	set ccp yes mpp-e128
	set ccp yes mpp-stateless

`pptp1:` 這種是用來作標籤整理用的，所以取什麼應該都 OK，只是 `load` 的時候記得改成對應的就好了。另外要注意的是 `set ipcp dns` 的參數記得改成你要的 dns server，通常跟你的機器上原本所設的 DNS 一樣就可以了。

 

### 再來是修改 `/usr/local/etc/mpd/mpd.links`

	:::conf
	pptp1:
	set link type pptp
	set pptp self <your public IP>
	set pptp enable incoming
	set pptp disable originate

`set pptp self` 這邊是輸入你 VPN Server 的 IP。

 

### 編輯密碼檔 `/usr/local/mpd/mpd.secret`

輸入你要登入的帳號和密碼就可以了，例如:

	:::text
	carlcarl carlcarlpassword
	carlcarl2  carlcarl2password

 

### 修改 `/etc/rc.conf`，加上:

	:::conf
	mpd_enable="YES"
 

### 接下來啟動服務

	:::bash
	/usr/local/etc/rc.d/mpd start

 

到這裡為止你用 VPN 連線應該是能夠連到你的 VPN Server 了，但是還是沒辦法連外，例如想要用瀏覽器看 google 網頁應該是不行的，所以還要再另外設定 NAT(natd) 和 firewall(ipfw)。


### 首先先修改 `/etc/rc.conf`，加上:

	:::conf
	ifconfig_bge0_alias0="inet 192.168.88.1  netmask 255.255.255.0"
	gateway_enable="YES"
	firewall_enable="YES"
	firewall_script="/root/ipfw.rules"
	natd_enable="YES"
	natd_interface="bge0"
	

`ifconfig_bge0_alias0` 的 `bge0` 記得改成你 Public IP 網卡的名稱，`natd_interface` 參數指定裝置的 `bge0` 也是一樣。剛才 `rc.conf` 裡有個 `firewall_script` 是指定你預設要讀的 firewall rule。

### 所以在 `/root/` 底下新增一個 `ipfw.rules` 檔案，加上執行的權限(`chmod +x ipfw.rules`)，並加入以下內容:

	:::text
	$IPFW add 100 divert natd all from 192.168.88.56 to any via msk0
	$IPFW add 101 divert natd all from any to 你的PublicIP via msk0
	#$IPFW add 100 divert natd all from any to any via msk0
	$IPFW add 105 allow ip from any to any


一到三都是指定 NAT 的 rule。如果不介意速度的話，可以只用第三條和第四條規則，我之前只用第三和第四條，可是連一般網路傳輸的速度也被拉下來，所以後來在前面自己加了兩條比較準確的規則，然後把第三條規則給註解掉這樣，第三條規則的意思是所有進入出去的封包都要經過 NAT 程序查看。而我的第一條規則負責看 NAT 出去的，所以只看來源是 `192.168.88.56` 的，第二條規則負責處理 NAT 進來的，這邊是看目標是 VPN Server 的 IP，當然通常不是每個到 VPN Server 的封包都一定是要 NAT 進來的，會有一些其餘的封包也會被 NAT 抓進去作檢查，這邊不知道能不能改善第二條規則就是了，不過也算是比第三條規則好一些了。另外記得後面的 `msk0` 要改成你的要的網卡裝置名稱，改完之後重開應該就可以了～。

 

 

參考網頁

<http://blog.weithenn.org/2009/05/freebsdmpd-pptp-vpn.html>

<http://www.section6.net/wiki/index.php/Setting_up_a_PPTP_VPN_server_in_FreeBSD>

<http://www.huomo.cn/os/article-148b0.html>

<http://zqliangzm.blog.163.com/blog/static/25903097200810510231119/>

<http://www.jb51.net/os/Unix/8786.html>

<http://www.twbsd.org/cht/articles/vpn.htm>

<http://www.4oa.com/Article/html/5/27/398/2005/10865.html>

<http://bbs.51cto.com/thread-31035-1.html>
