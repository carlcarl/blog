Title: Raspberry Pi beginner
Date: 2014-01-21 02:30
Author: carlcarl
Post_ID: 1386
Category: linux
Tags: raspberry
Slug: raspberry_pi_beginner


之前在 COSCUP 拿到的 Raspberry Pi 一直放著沒動，最近想說還是拿來玩一下好了，不然有點浪費XD。

## 基本配備
大部份其實都有了，SD 卡則是自己另外買了一張 [SanDisk Extreme SDHC UHS-I 16GB]，USB hub 可能之後也會需要，不過還不知道要買哪一個，這邊有 [USB hubs 的清單] 可以看。OS 則是用 Arch。

## 燒錄 image 到 SD 卡
在 Mac 和 Linux 底下可以直接用 `dd`，ex: `dd bs=1M if=Path/to/archlinux-hf-2013-02-11.img of=/dev/mmcblk1`。Mac 底下如果遇到 `Resource busy` 的 error 的話，可以參考 [Using dd I'm getting a Resource Busy error]，

## Resize Paritions
一開始燒 image 進去之後，空間會是固定的，想要利用到 SD 卡所有的儲存空間的話，需要自己做延伸，可以參考這篇: [How can I resize my / (root) partition?]。


其他的設定可以參考這幾篇：  
[Raspberry Pi 安裝心得、教學、簡介]  
[建構Raspberry Pi with Arch Linux ARM]  
[Raspberry Pi 購買指南]  


[SanDisk Extreme SDHC UHS-I 16GB]: http://shopping.pchome.com.tw/?mod=item&func=exhibit&IT_NO=DGAG0H-A79608303&SR_NO=DGAG0H&ROWNO=25
[USB hubs 的清單]: http://elinux.org/RPi_Powered_USB_Hubs
[How can I resize my / (root) partition?]: https://raspberrypi.stackexchange.com/questions/499/how-can-i-resize-my-root-partition
[Using dd I'm getting a Resource Busy error]: http://forums.macrumors.com/showthread.php?t=384730
[Raspberry Pi 安裝心得、教學、簡介]: http://wwssllabcd.github.io/blog/2013/01/31/how-to-setup-raspberry-pi/
[建構Raspberry Pi with Arch Linux ARM]: http://blog.xuite.net/zack_pan/blog/73179035-建構Raspberry+Pi+with+Arch+Linux+ARM
[Raspberry Pi 購買指南]: http://life-of-raspberrypi.blogspot.tw/2013/01/raspberry-pi-310.html