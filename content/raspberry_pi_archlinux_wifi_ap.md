Title: Raspberry-pi Archlinux wifi ap
Date: 2014-06-04 02:30
Author: carlcarl
Post_ID: 1399
Category: linux
Tags: raspberry
Slug: raspberry_pi_archlinux_wifi_ap



弄了兩天，網路上方法很多，不過用的無線網卡種類繁多，然後 OS 有些是 Arch，有些是 Debian，然後裝的套件也會有些許不同，所以整個實驗的 branch 非常多啊~~~，弄了好久，最後終於成功了QQ。不過因為弄得蠻亂的，所以有些步驟其實不是非常確定，只能憑印象來記錄。

無線網卡我是用 TP-LINK WN725N v2.0 版本，主要是因為體積小，然後網路上也可以查得到一些教學，不過怎麼判斷 v1 還是 v2 就很難了，因為一般網路拍賣好像都不會註明，實際拿到的包裝盒上倒是可以看到是哪一版。

首先，Arch 上最新的版本應該是可以讀到這個網卡，可以用 `lsmod` 看有沒有 `r8188eu`，如果有就 OK。

## 設置 wlan0
接下來要把 `wlan0` 設置起來，建立 `/etc/systemd/system/network-wireless@.service` 這個檔案並編輯它的內容:

    :::text
    [Unit]
	Description=Wireless network connectivity (%i)
	Wants=network.target
	Before=network.target
	BindsTo=sys-subsystem-net-devices-%i.device
	After=sys-subsystem-net-devices-%i.device
	
	[Service]
	Type=oneshot
	RemainAfterExit=yes
	EnvironmentFile=/etc/conf.d/network-wireless@%i

	ExecStart=/usr/bin/ip link set dev %i up
	ExecStart=/usr/bin/ip addr add ${address}/${netmask} broadcast ${broadcast} dev %i
	
	
	ExecStop=/usr/bin/ip addr flush dev %i
	ExecStop=/usr/bin/ip link set dev %i down
	
	[Install]
	WantedBy=multi-user.target

接著建立並編輯 `/etc/conf.d/network-wireless@wlan0`:

    :::text
    address=192.168.42.1
	netmask=24
	broadcast=192.168.42.255

`address` 的部分就自己設個範圍，預設是由有線出去，所以這邊就不用加上 gateway 了。編輯完就可以 enable 這個 service:

	:::shell
	sudo systemctl enable network-wireless@wlan0.service
	sudo systemctl start network-wireless@wlan0.service

## 設置 dnsmasq

安裝 `dnsmasq`:

	:::shell
	sudo yaourt -S dnsmasq

編輯 `/etc/dnsmasq.conf`，參考以下做修改:

	:::text
	interface=wlan0
	dhcp-range=192.168.42.2,192.168.42.10,255.255.255.0,12h

Enable service:

	:::text
	sudo systemctl enable dnsmasq
	sudo systemctl start dnsmasq

## 設置 hostapd

安裝 `hostapd`:

    :::shell
    sudo yaourt -S hostapd-8188eu

編輯 `/etc/hostapd/hostapd.conf` 檔案內容，參考下方做修改，來源參考 [Software access point]:

	:::text
	ssid=YourWifiName
	wpa_passphrase=Somepassphrase
	interface=wlan0
	auth_algs=3
	channel=7
	hw_mode=g
	logger_stdout=-1
	logger_stdout_level=2
	max_num_sta=5
	rsn_pairwise=CCMP
	wpa=2
	wpa_key_mgmt=WPA-PSK
	wpa_pairwise=TKIP CCMP

`ssid` 是 wifi 的 名稱，`wpa_passphrase` 是 wifi 密碼，其他的不知道也沒差 lol。

Enable service:

	:::text
	sudo systemctl enable hostpad
	sudo systemctl start hostpad


`hostpad` 啟動後，應該就會有 wifi 的訊號出來，然後輸入 wifi 密碼之後是可以連上的，不過還沒辦法連外才對。這時候還需要設定 NAT 的部分。

## 設置 NAT

編輯 `/etc/sysctl.d/30-ipforward.conf`，加上以下內容:

	:::text
	net.ipv4.ip_forward=1
	net.ipv6.conf.default.forwarding=1
	net.ipv6.conf.all.forwarding=1

設定 `iptables` 並啟動 service:

	:::shell
	sudo iptables -t nat -A POSTROUTING -o internet0 -j MASQUERADE
	sudo iptables -A FORWARD -i net0 -o internet0 -j ACCEPT
	sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
	
	sudo sh -c "iptables-save > /etc/iptables/iptables.rules"
	sudo systemctl enable iptables
	sudo systemctl start iptables

`iptables` 預設會讀取 `/etc/iptables/iptables.rules`，所以不需要再多做讀取 rule 的設置。

最後 reboot 板子，測試連外是否正常就 ok 了。

參考資料:  
[RPI-Wireless-Hotspot]  
[Wireless network configuration]  
[Internet sharing]  
[Network configuration]  
[How To : Use The Raspberry Pi As A Wireless Access Point/Router Part 1]  
[Wireless AP]  
[使用 notebook 上的無線網卡來當無線 AP - arch linux 篇]  
[iptables]  

[Software access point]: https://wiki.archlinux.org/index.php/Software_Access_Point
[RPI-Wireless-Hotspot]: http://elinux.org/RPI-Wireless-Hotspot
[Wireless network configuration]: https://wiki.archlinux.org/index.php/Wireless_network_configuration#Manual_wireless_connection_at_boot_using_systemd_and_dhcpcd
[Internet sharing]: https://wiki.archlinux.org/index.php/Internet_sharing
[Network configuration]: https://wiki.archlinux.org/index.php/Network_configuration#Static_IP_address
[How To : Use The Raspberry Pi As A Wireless Access Point/Router Part 1]: http://sirlagz.net/2012/08/09/how-to-use-the-raspberry-pi-as-a-wireless-access-pointrouter-part-1/
[Wireless AP]: http://www.raspberrypi.org/forums/viewtopic.php?f=29&t=27005
[使用 notebook 上的無線網卡來當無線 AP - arch linux 篇]: http://guildwar23.blogspot.tw/2013/03/notebook-ap-arch-linux.html
[iptables]: https://wiki.archlinux.org/index.php/iptables


