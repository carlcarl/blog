Title: Ubuntu desktop record: recorditnow+ffmpeg
Date: 2012-03-29 02:13
Author: carlcarl
Post_ID: 326
Category: linux
Tags: ffmpeg, recorditnow, ubuntu
Slug: ubuntu-desktop-record-recorditnow-ffmpeg

![recorditnow][]

最近找了很多類似的軟體，不過有些都弄不起來，不然就是怪怪的囧，後來試了這套組合發現還不錯：recorditnow + ffmpeg，ffmpeg 是核心，recorditnow 是 frontend。

下面是使用教學的影片，可以參考看看：  
<http://www.youtube.com/watch?v=dEnZe-qfLWA>

不過我直接下 recorditnow 執行 ffmpeg 選項會有沒辦法停止的問題。  
<https://bugs.launchpad.net/ubuntu/+source/recorditnow/+bug/858973>  
上面這個連結有提供修正的 PPA  
以 ubuntu 來講，執行：

	:::bash
	sudo add-apt-repository ppa:ap10336/ppa
	sudo apt-get update
	sudo apt-get install recorditnow

這樣就 ok 了。

  [recorditnow]: http://i.imgur.com/EQUigGel.png
    "RecordItNow_507"
 