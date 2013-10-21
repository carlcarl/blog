Title: Linux Mint cinnamon change position of window buttons
Date: 2012-02-04 18:56
Author: carlcarl
Post_ID: 239
Category: linux
Tags: cinnanmon, gconf-editor
Slug: linux-mint-cinnanmon-change-position-of-window-buttons

==================================================  
2012/03/28更新

cinnamon 已經有提供修改按鈕位置的設定了，所以就不用照以下的方法來改哩。
=======================================================================

最近裝了 cinnamon 來玩玩，是有一些有趣的東西沒錯，像是視窗動畫，不過整體來說，我覺得並沒有好到值得我換成這套，所以用了沒多久我就換回來 Gnome 啦～～。

不過這邊還是來講一下 cinnamon 怎麼改變視窗按鈕位置的方法吧。

首先先裝編輯設定的套件

	:::bash
	apt-get install gconf-editor


執行後會出現一個視窗，接著如以下圖片，可以看到右邊有 `button layout` 這個欄位，有關閉，最小化，最大化的值，`:` 代表相對位置，如下圖的話指的是放在左邊，如果要放在右邊的話就把 `:` 移到前面就
OK 了。

![gconf-editor](http://198.199.117.21/wp-content/uploads/2012/02/502.png)
