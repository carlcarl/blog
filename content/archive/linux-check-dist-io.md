Title: Linux check disk IO
Date: 2011-06-13 10:44
Author: carlcarl
Post_ID: 23
Category: linux
Slug: linux-check-dist-io

讀取速度 輸入下面這行指令

	:::bash
	hdparm -t /dev/sda


`/dev/sda` 可以換成想測的硬碟裝置

輸入之後會產生類似以下的輸出

	:::text
	Timing buffered disk reads:  1168 MB in  3.00 seconds = 389.29 MB/sec


組 RAID5 速度快很多= =+

 

寫入速度 輸入下面這行指令

	:::bash
	time sh -c "dd if=/dev/zero of=tmp.dd bs=1000k count=100; sync"


會產生類似以下的輸入

	:::text
	100+0 records in
	100+0 records out
	102400000 bytes (102 MB) copied, 0.0820241 s, 1.2 GB/s
	real    0m1.669s
	user    0m0.000s
	sys 0m0.088s

 

接著將 102MB 除以 real 的時間(這裡是 1.669)就可以算出寫入的時間了，測完記得要把 `outfile` 這個檔案刪掉，因為他是直接生出一個檔案到目錄底下。

 

參考網址

<http://cha.homeip.net/blog/2010/05/2263.html>
