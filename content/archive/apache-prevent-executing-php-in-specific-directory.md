Title: apache prevent executing php in specific directory
Date: 2011-12-04 23:12
Author: carlcarl
Post_ID: 159
Category: linux
Tags: apache, php
Slug: apache-prevent-executing-php-in-specific-directory

最近剛修復的問題，其實也滿常見的，不過有時候總是會忽略這種簡單的問題orz。

如果要預防使用者將 php 檔案上傳後去執行的話，只要在 apache 的 config
檔中加入以下設定：

	:::text
    AllowOverride None
    php_flag engine off
    Allow from all


`Directory` 後面的 `/var/www/upload`
記得使用自己要的路徑，設定完並重開 apache 後，如果是在這個目錄底下的
php，就會改成下載 php 而不是執行
php。另外還有一種方法也是可以作，不過是用副檔名的方法作過濾，顯然還是上面的方法會比較好囉。

參考網址：  
<http://www.yunsec.net/a/special/linux/safe/2010/0517/3924.html>
