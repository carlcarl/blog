Title: XRDP shortcut d with remote connection
Date: 2011-07-07 18:35
Author: carlcarl
Post_ID: 32
Category: linux
Slug: xrdp-shortcut-d-with-remote-connection

之前裝了 XRDP，還滿不錯用的。不僅可以用 Linux 的 Terminal server client，也可以用 Windows 內建的遠端連線直接連進去。

但是卻發現了一個很討厭的問題，那就是按 `d` 的時候會發現，怎麼視窗被縮小跑到桌面去orz，後來查了一些資料好不容易才找到，我以為這個問題很多人都會遇到的說......。
 

首先，問題是出在裝 XRDP 的主機上沒錯，且就是因為快捷鍵的問題，所以只要修改這個設定就 OK 了，這邊假設裝 XRDP 的主機是有 GUI 介面的(沒有的話用 ssh 就好啦XD)

先輸入:

	:::bash
	gconf-editor


應該會出現一個視窗。

接著根據 `apps` : `metacity` : `global_keybindings` 的順序下去找，應該可以找到一個叫做 `show_desktop` 的設定。然後對應的值應該會是 `<Super>d`，這邊就直接把這個值刪掉就好了。改完後重開， 之後再用遠端連線進來應該會發現 `d` 的按鍵可以正常輸入了。

參考網頁  
<http://forums.linuxmint.com/viewtopic.php?f=47&t=61971>  
<http://www.liberiangeek.net/2010/07/connect-ubuntu-10-04-lucid-lynx-remote-desktop-windows-machines/>
