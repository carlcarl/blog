Title: awstats analyze large logs at once (include gz files)
Date: 2011-07-04 14:22
Author: carlcarl
Post_ID: 31
Category: linux
Tags: awstats
Slug: awstats-analyze-large-logs-at-once-include-gz-files

[awstats的簡易安裝教學][]

因為在維護的網站log檔有一年份，而且都已經壓縮成gz檔，要用awstats分析的話實在很費工夫，後來發現awstats有好用的工具可以用：<span style="color: #3366ff;">logresolvemerge.pl</span>。

簡單講就是用這個工具將log檔(包含gz壓縮檔)都merge起來為一個大檔案後，再用awstats作分析。

這邊首先要注意的就是
<span style="color: #ff0000;">awstats不會讀較舊的log檔</span>，所以像我之閒已經讀了最新的log檔後想讀舊的，就只能直接砍掉紀錄檔重新開始，到
/var/lib/awstats/底下將底下的檔案刪光，如此就能回到最初的狀態

 

logresolvemerge.pl預設是在<span style="color: #3366ff;">/usr/share/doc/awstats/examples/</span>裡  
可以移到其他地方，不然每次打路徑應該會打到手很酸XD

這裡給個幾個簡單的範例

### 將多個log檔merge成一個log檔

	:::text
	logresolvemerge.pl /var/log/apache2/.log > temp.log


### 將多個gz檔merge成一個log檔(其實跟上面的差不多~)

	:::text
	logresolvemerge.pl /var/log/apache2/.gz > temp.log
 

### merge完後接著用awstats分析 並加上Log File的指定

	:::text
	awstats.pl -config=www.domain.com -LogFile=temp.log


這裡還要注意一個重點！
那就是<span style="color: #ff0000;">merge完後的log檔不能太大，不然很容易失敗！</span>

我建議Log檔就盡量4G以下吧~，之前一次跑1XG的log檔失敗，還不信邪跑了好幾次，後來就放棄，切成幾份來個別做了。

 

話說分析1XG的log檔真的超久......，Server級的也跑了10個小時有了吧orz

 

參考網頁

<http://www.anoneh.com/136.php>  
[http://1024k.de/awstats/1and1/tutorial-04.html ][]  
<http://awstats.sourceforge.net/docs/awstats_tools.html>  
<http://www.smartlabsoftware.com/howto/awstats-log.htm>  
<http://www.webmasterworld.com/forum40/1536.htm>  
<http://www.internetofficer.com/forum/awstats-iis-installation-and-configuration/how-to-analyze-multiple-logfiles/>

  [awstats的簡易安裝教學]: http://carl830.pixnet.net/blog/post/66466219
  [http://1024k.de/awstats/1and1/tutorial-04.html ]: http://1024k.de/awstats/1and1/tutorial-04.html
