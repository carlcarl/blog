Title: windows xdebug, wincachegrind, Zend server
Date: 2011-06-21 00:48
Author: carlcarl
Post_ID: 26
Category: php
Tags: zend framework
Slug: windows-xdebug-wincachegrind-zend-server

最近在想辦法加速 zend framework 的執行速度，弄了超久。下次有這種 case，我死都不用 zend 了= =。

 

這次要用的是利用 xdebug 和 wincachegrind 來分析一下 php 執行的速度和呼叫情況之類的。首先要裝的是[xdebug][]這個工具，進去官網後的下載頁面後可以看到幾種執行檔，我這邊用的是 php5.2 版 有兩種可以選 [PHP 5.2 VC6 (32 bit)][], [PHP 5.2 VC6
TS (32 bit)][]，如果是 php5.3 版就要選另外幾種了，這邊我是分不太清楚前後兩種的差別 不過如果是用一般的 apache server 的話可以用後面那種試試看。

下載後放至 `php` 目錄的 `ext` 資料夾底下，在 `php.ini` 檔裡加上以下幾行

	:::conf
	[Xdebug]
	extension=php_xdebug.dll
	xdebug.profiler_enable=On
	xdebug.profiler_output_dir="C:xdebug"


通常 `php_xdebug.dll` 下載檔名後後面會接一長串版本名，所以我會修改一下檔名 這樣比較不會打錯，`xdebug.profiler_output_dir` 這邊的資料夾要自己建，為了方便 我通常就直接在 `C` 底下直接建一個 `xdebug` 資料夾來用。


接著要用 [wincachegrind][] 來作分析，下載回來後直接開就能用了 這邊要先在 `Tools/Options` 底下去修改 `working folder`，這邊的目錄跟之前 `xdebug.profiler_output_dir` 的目錄會是一樣的，這樣才有辦法分析 xdebug 所產生的檔案。

 

另外，後來 Web server 我改用 [zend server CE][]，速度好像增快了不少，不過在開啟 web 服務的時候遇到了點問題，後來查到，要到 `ZendZendServeretc` 將 `ZendEnablerConf.xml` 前面的亂碼修改成 `<?xml` 並另存成 `UTF-8` 就 ok 了。

但是接著想找怎麼重開 web server，卻找不到地方可以按 orz，只找到輸入 commadn Line 的方式:

	:::text
	net stop Apache2.2-Zend && net start Apache2.2-Zend


但是想用 xdebug 實際量測的時候卻發現好像不能直接用之前的設定= =||，後來查了一些資料 大致要修改一些東西。首先 xdebug 的 dll 檔要選擇前面 [PHP 5.2 VC6 (32 bit)][]，接著修改 `C:Program FilesZendZendServeretccfgdebugger.ini`，將 `zend_extension_manager.dir.debugger=......`，這行前面加個分號註解掉，`php.ini` 檔裡，`xdebug` 移到最前面並作一點修改。

	:::conf
	[Xdebug]
	zend_extension="你的php目錄extphp_xdebug.dll"
	xdebug.profiler_enable=Onxdebug.profiler_output_dir="C:xdebug"
	
`zend_extensioln` 記得是改成自己安裝的對應目錄，安裝的部份差不多這樣就 ok 了。

 

參考網頁:  
<http://daimajishu.iteye.com/blog/958684>  
<http://www.antennule.net/?p=255>  
<http://galide.jazar.co.uk/2011/02/zend-server-hosted-on-windows-restart.html>  

  [xdebug]: http://xdebug.org/
  [PHP 5.2 VC6 (32 bit)]: http://xdebug.org/files/php_xdebug-2.1.1-5.2-vc6-nts.dll
  [PHP 5.2 VC6 TS (32 bit)]: http://xdebug.org/files/php_xdebug-2.1.1-5.2-vc6.dll
  [wincachegrind]: http://sourceforge.net/projects/wincachegrind/files/wincachegrind/wincachegrind-10.0.0.14/
  [zend server CE]: http://www.zend.com/en/products/server-ce/
