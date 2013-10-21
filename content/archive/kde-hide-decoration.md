Title: KDE hide decoration
Date: 2012-12-02 08:45
Author: carlcarl
Post_ID: 726
Category: KDE, linux
Tags: KDE
Slug: kde-hide-decoration

之前為了隱藏 KDE 視窗的 decoration
找方法找好久，結果後來不經意就看到了這個資訊囧，不過可惜只能透過改設定檔的方式，GUI
上似乎沒有這個設定。

<!--more-->

修改 `.kde4/share/config/kwinrc`，找到 `[Windows]`，在下一行加上：

	:::conf
    BorderlessMaximizedWindows=true

如果找不到 `[Windows]` ，就自己在檔案裡面補上去就可以了：

	:::conf
    [Windows]
    BorderlessMaximizedWindows=true

用好之後，可以再搭配 [KWin Button applet
improved][]，個人覺得還滿方便的～。

參考網址：  
<http://majewsky.wordpress.com/2010/03/24/the-kwin-button-applet/>

  [KWin Button applet improved]: http://kde-apps.org/content/show.php?content=143971
