Title: naming apache log with date
Date: 2011-12-19 17:01
Author: carlcarl
Post_ID: 233
Category: linux
Tags: apache, daily, logrotate
Slug: naming-apache-log-with-date

目前是用 `logrotate` 來作，只要在 `/etc/logrotate.d/apache2` 裡加入下面這個參數即可：

-   dateext

另外可以根據需求看要不要把 `weekly` 改為 `daily` 這樣。

處理過後的檔名就會像這樣 `access.log-20111218.gz`，這樣在之後處理和分析
log 會比較方便，另外記得數量也要根據需求改，因為改完後變成能保存的 log
日期也會跟著減少，要增多的話也是直接修改上面 `/etc/logrotate.d/apache2` 這個檔案，將 `rotate` 後面的數字加大，後面的數字表示要存的 log 數量，超過的話就會將最舊的刪除這樣。

後記：  
如果要跟 awstats 搭配的話可以在裡面加入：

	:::bash
	prerotate
    	/usr/lib/cgi-bin/awstats.pl -config=你的config檔  -update > /dev/null
	endscript


這樣才能在壓縮 log 檔之前確保 awstats 不會漏掉log檔的資料

參考網址：  

<http://groups.google.com/group/linux.debian.user/browse_thread/thread/d1a86eebd2d2e862?pli=1>  

<http://www.doubleservice.com/2011/02/configuration-of-logrotate-with-awstats/>
