Title: xenserver enable snmpd
Date: 2012-02-19 16:06
Author: carlcarl
Post_ID: 262
Category: linux
Tags: iptables, snmp, snmpd, xenserver
Slug: xenserver-enable-snmpd

我用的 xenserver 版本為「5.6」，6 以上的版本就不能確定能否這樣做囉。

### 首先要先修改防火牆規則
xenserver 雖然本身就有 snmpd 了，不過只單純打開 snmpd 是沒用的，會被防火牆擋下。用 vi
    編輯 `/etc/sysconfig/iptables`，找到 `-A RH-Firewall-1-INPUT –p udp
    –dport 5353` 這行：

	:::text
	-A RH-Firewall-1-INPUT -p ah -j ACCEPT
	-A RH-Firewall-1-INPUT -d 224.0.0.251 -p udp -m udp --dport 5353 -j ACCEPT
	-A RH-Firewall-1-INPUT -p udp -m udp --dport 631 -j ACCEPT


加上一行，這行表示允許 snmp 進來的這個 port，也就是 161。

	:::text
	-A RH-Firewall-1-INPUT -p ah -j ACCEPT
	-A RH-Firewall-1-INPUT -d 224.0.0.251 -p udp -m udp --dport 5353 -j ACCEPT
	-A RH-Firewall-1-INPUT -p udp --dport 161 -j ACCEPT
	-A RH-Firewall-1-INPUT -p udp -m udp --dport 631 -j ACCEPT

編輯完關掉 vi，輸入以下這行來重新啟動防火牆：

	:::bash
	service iptables restart


### 接著打開 snmpd，輸入以下兩行：

	:::bash
	chkconfig snmpd on
	service snmpd start


這樣就算大功告成了，如果有需要，再修改 `/etc/snmp/snmpd.conf`。例如一開始預設是所有人都可以監控，所以可能要把 `com2sec
notConfigUser default public` 中的 `default` 改為允許監控你這台的IP。

參考網址：  
<http://support.citrix.com/article/CTX122337>
