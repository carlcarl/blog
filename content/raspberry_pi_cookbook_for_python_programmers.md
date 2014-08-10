Title: Raspberry Pi Cookbook for Python Programmers
Date: 2014-08-11 00:30
Author: carlcarl
Post_ID: 1400
Category: linux
Tags: raspberry
Slug: raspberry_pi_cookbook_for_python_programmers


![Raspberry Pi Cookbook for Python Programmers](http://i.imgur.com/3oE47eK.jpg)

很久沒有看電子書了，最近剛好拿到幾本來看，這本是其中的一本，大致就是在講 Python 在 Raspberry pi 上如何使用和如何操作 Raspberry 的一些硬體功能，像是 GPIO 和 Camera 之類的。其實這本書跟我想像的有點不太一樣，它比較偏向硬體操作，大部分的章節都是如此，反而比較沒有偏向單軟體應用的，所以像我這種硬體不太行的就有點吃癟了QQ。另外要注意的是這本書用的是 Python3，不是 Python2，然後 Raspberry Pi 的作業系統應該是 Debian based 的，這本書裏面其實需要裝蠻多套件的，常看到一堆 `apt-get`，所以如果像是用 Arch 之類的話就要注意，可能對應的套件也還是會有，不過就需要找一下這樣。

書裏面大致分幾個部分：

1. 如何使用 Raspberry Pi。對於第一次摸這塊板子的人有這個章節真的會比較更容易上手，不過跟 Python 其實關係就不大了，是說這部分內容還佔滿多的，我是覺得可以不需要那麼多XD。
2. 用 Python 做視窗程式，寫遊戲，畫 3D model。這部分我是覺得有點囧，一般應該不會有人想用板子來做 3D model 還是啥遊戲的吧...，個人覺得這部分實用度不高。如果有啥做 webpage grap 教學之類的我覺得會比較實用，或者是如果拿來做 NAS 的話，如何用 Python 來處理裏面的資料之類的。
3. 用 Python 處理 GPIO, LED, Camera 之類的硬體功能，這部分蠻有趣的，可惜我硬體不太行，不然我覺得這部分講得還滿實用的，像是 Camera 做 QR code 的 decoder，也可以拍照啥的，LED 燈也可以用來做很多東西的狀態指示。

大致來講，這本書我覺得很適合第一次摸這塊板子的韌(硬)體 programmer，裏面 Python 的 Code 都還滿完整的，解說也很詳細，門檻反而比較偏向是接板子弄 GPIO 那邊，如果本身有點概念的話弄起來應該會容易多。


