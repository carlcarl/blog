Title: Raspberry Pi BT Transmission
Date: 2014-01-21 03:00
Author: carlcarl
Post_ID: 1387
Category: linux
Tags: raspberry
Slug: raspberry_pi_bt_transmission


研究了一下怎麼在 [raspberry pi] + [ArchLinux] 上用 BT，好像都是用 [transmission]，所以我就跟著用了XD，下面是一些步驟。

## 安裝 transmission daemon

    :::shell
    sudo pacman -S transmission-cli
    
## Run transmission daemon
由於一開始沒有設定檔，要先跑過才有，所以先跑一下，是說要這樣做也太囧。

    :::shell
    sudo systemctl enable transmission
    sudo systemctl start transmission
    sudo systemctl stop transmission
    
## 修改設定檔
設定檔位置在 `/var/lib/transmission/.config/transmission-daemon/settings.json` (這位置好爛)，我自己的設定檔如下，後方的 `M` 表示新增或改過的:

    :::js
    {
        "alt-speed-down": 50,
        "alt-speed-enabled": false,
        "alt-speed-time-begin": 540,
        "alt-speed-time-day": 127,
        "alt-speed-time-enabled": false,
        "alt-speed-time-end": 1020,
        "alt-speed-up": 50,
        "bind-address-ipv4": "0.0.0.0",
        "bind-address-ipv6": "::",
        "blocklist-enabled": false,
        "blocklist-url": "http://www.example.com/blocklist",
        "cache-size-mb": 4,
        "dht-enabled": true,
        "download-dir": "/mnt/BT/Complete", /* M */
        "download-queue-enabled": true,
        "download-queue-size": 10, /* M */
        "encryption": 1,
        "idle-seeding-limit": 30,
        "idle-seeding-limit-enabled": false,
        "incomplete-dir": "/mnt/BT/Incomplete", /* M */
        "incomplete-dir-enabled": true, /* M */
        "lpd-enabled": false,
        "message-level": 1,
        "peer-congestion-algorithm": "",
        "peer-id-ttl-hours": 6,
        "peer-limit-global": 200,
        "peer-limit-per-torrent": 50,
        "peer-port": 51413,
        "peer-port-random-high": 65535,
        "peer-port-random-low": 49152,
        "peer-port-random-on-start": false,
        "peer-socket-tos": "default",
        "pex-enabled": true,
        "port-forwarding-enabled": true,
        "preallocation": 1,
        "prefetch-enabled": 1,    
        "queue-stalled-enabled": true,
        "queue-stalled-minutes": 30,
        "ratio-limit": 2,
        "ratio-limit-enabled": false,
        "rename-partial-files": true,
        "rpc-authentication-required": false,
        "rpc-bind-address": "0.0.0.0",
        "rpc-enabled": true,
        "rpc-password": "{a803e8f49fd53e7d4516b14511e68ea109f4a62bfbiCsfoS",
        "rpc-port": 9091,
        "rpc-url": "/transmission/",
        "rpc-username": "carlcarl", /* M */
        "rpc-whitelist": "192.168.11.*", /* M */
        "rpc-whitelist-enabled": true,
        "scrape-paused-torrents-enabled": true,
        "script-torrent-done-enabled": false,
        "script-torrent-done-filename": "",
        "seed-queue-enabled": false,
        "seed-queue-size": 10,
        "speed-limit-down": 2500, /* M */
        "speed-limit-down-enabled": true, /* M */
        "speed-limit-up": 50, /* M */
        "speed-limit-up-enabled": true, /* M */
        "start-added-torrents": true,
        "trash-original-torrent-files": false,
        "umask": 18,
        "upload-slots-per-torrent": 14,
        "utp-enabled": true,
        "watch-dir": "/mnt/BT/Torrents", /* M */
        "watch-dir-enabled": true /* M */
    }
    
`download-dir` 和 `incomplete-dir` 分開來放比較能分清楚；rpc 的部分就修改了一下可以連 web 的 ip，這邊限制在 `192.168.11.*`，`rpc-username` 這邊應該可以不用，就改一下放著這樣XD，`speed-limit-*` 系列的就是限制下載和上傳的速度，基本上是要設，也可以透過 web 界面再來設定，`watch-dir` 是自動偵測如果這個資料夾底下有新的 torrent，就開始那個 torrent 的下載，目前可能還用不太到，也是先放著這樣，目前透過 web 上傳 torrent 應該就夠用了。

## 執行 transmission deamon again
改完設定檔後，連 `http://<ip>:9091` 應該就看得到了(`<ip>` 就是你板子的 ip)。

    :::shell    
    sudo systemctl start transmission


## 其他建議
我個人是建議可以把下載資料夾改成 `775` 權限，然後將資料夾的 owner 設為自己的帳號，group owner 則用 `transmission`，使用上會比較方便，權限也做一點保留。



參考資料：  
[Transmission-daemon on Archlinux ARM]  
[Transmission Archlinux Wiki]  
[打造脫機下載農場，使用Raspberry Pi + Transmission-daemon]  
[在VPS上安裝TRANSMISSION來進行BT下載]  
[fstab]  

[raspberry pi]: http://www.raspberrypi.org
[ArchLinux]: https://www.archlinux.org
[transmission]: http://www.transmissionbt.com
[Transmission-daemon on Archlinux ARM]: https://lnxslck.wordpress.com/2013/03/08/transmission-daemon-on-archlinux-arm/
[Transmission Archlinux Wiki]: https://wiki.archlinux.org/index.php/Transmission
[打造脫機下載農場，使用Raspberry Pi + Transmission-daemon]: http://wwssllabcd.github.io/blog/2013/04/22/how-to-setup-transmission-deamon-in-raspberry-pi/
[在VPS上安裝TRANSMISSION來進行BT下載]: http://kasdia.tw/blog/2013/09/16/在vps上安裝transmission來進行bt下載/
[fstab]: https://wiki.archlinux.org/index.php/fstab