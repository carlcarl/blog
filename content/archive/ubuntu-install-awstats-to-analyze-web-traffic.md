Title: ubuntu install awstats to analyze web traffic
Date: 2011-07-04 13:04
Author: carlcarl
Post_ID: 30
Category: linux
Tags: awstats
Slug: ubuntu-install-awstats-to-analyze-web-traffic

[![1309785078-4e7966370fbebe6c564d5c251d18d3da_n][]][1309785078-4e7966370fbebe6c564d5c251d18d3da_n]

awstats 這個工具可以透過分析 Server 的access log 檔來統計網站流量，資料的部份可以透過時間長短、來訪者的資料(國籍之類的)、瀏覽器種類來作分類，這些統計資訊則透過Web介面顯示出來。而上面這個圖是裝完 awstats 後的 Web 介面(還不錯精美= =+)

<!--more-->
 

接下來就是安裝的部份啦，首先先安裝套件:

	:::bash
	sudo apt-get install awstats

 

接著到 `/etc/awstats/` 底下可以看到預設的 `awstats.conf` 檔，把這個檔複製並更名 假如網站名稱為 `www.domain.com` 的話

	:::bash
	cp awstats.conf awstats.www.domain.com.conf


到時候指定好 config 的參數 他就會去讀這個檔案的設定，然後要稍微修改一下 `awstats.www.domain.com.conf` 中的內容

-   找到 `LogFile=` 的部份，修改並加上加上你要讀的 access
    log 檔，例如：`LogFile="/var/log/apache2/access.log"`
-   找到 `LogFormat=` 的部份，將預設的 4 修改為 1，如：`LogFormat=1`
    (如果後面執行的時候顯示格式有錯，可以改回 4，但是可能有些東西會沒辦法分析)
-   找到 `SiteDomain=` 的部份，設定你網站的網址，如：`SiteDomain="www.domain.com"`
-   找到 `#LoadPlugin="decodeutfkeys"` 的部份，將前面的 `#` 刪掉，這個能讓 utf 編碼的關鍵字能夠正常顯示(這邊是參考網路上的教學，至於不加會不會有問題，倒是沒有實際測試過)

 

接著到 `/usr/share/awstats/lang` 底下修改語系檔，將 `awstats-tw.txt` 將內容的 `big` 改成 `utf-8` 並用 `utf-8` 的編碼存成 `awstats-utf8.txt` 檔案

	:::bash
	sudo cat awstats-tw.txt | sed -e 's/big5/utf-8/' | iconv -f big5 -t utf8 > awstats-tw-utf8.txt

如果發現有權限的錯誤，可以直接轉成 root 再試，通常這樣就可以解決了。設定好之後就可以開始作第一次分析了:

	:::bash
	/usr/lib/cgi-bin/awstats.pl -config=www.domain.com
 

之後如果要再做分析，只要在後面加上 `-update` 就可以了:

	:::bash
	/usr/lib/cgi-bin/awstats.pl -config=www.domain.com -update

 

分析之後還沒結束，雖然資料分析完了，不過還是需要 Web 介面，所以還必須設定一下目錄，修改 `/etc/apache2/site-available/default` (或是你的其他網站設定檔)，加上以下內容:

	:::text
	Alias /awstatsclasses/ "/usr/share/awstats/lib/"
	Alias /awstats-icon/ "/usr/share/awstats/icon/"
	Alias /awstatscss "/usr/share/doc/awstats/examples/css"
	ScriptAlias /awstats/ /usr/lib/cgi-bin/
	Options ExecCGI -MultiViews +SymLinksIfOwnerMatch
	Options None
	AllowOverride None
	Order allow,deny
	Allow from All

接著看網頁應該就可以看到結果了: 
http://www.domain.com/awstats/awstats.pl?config=www.domain.com

 

另外要注意的是 awstat 並不會自動更新，所以必須設定 crobtab 之類的程式，一天更新一次資料之類的才行，以每天半夜三點執行為例，修改 `/etc/crobtab` 加上以下指令:

	:::text
	00 3 * * * root /usr/lib/cgi-bin/awstats.pl -config=www.domain.com -update > /dev/null


另外這個部份也可以跟 [apache logrotate][] 的設定做搭配

 

參考網頁  
<http://blog.db.idv.tw/2009/09/awstatsweb-log.html>  
<http://2007xyz.blogspot.com/2007/10/ubuntu-704-awstats.html>  
<http://blog.longwin.com.tw/2009/08/ubuntu-904-server-instatll-awstats-2009/>  
<http://vega02.pixnet.net/blog/post/32284929>  
<http://oss.tw/elgg/pg/forum/topic/17314/-ubuntu-1010-awstats/>  
<http://maestric.com/doc/ubuntu/awstats>

  [1309785078-4e7966370fbebe6c564d5c251d18d3da_n]: http://i.imgur.com/gjdRNUQl.png
  [apache logrotate]: /233/naming-apache-log-with-date
    "將apache log改為日期名稱"
