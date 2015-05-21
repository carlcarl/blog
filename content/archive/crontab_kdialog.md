Title: kdialog with crontab
Date: 2015-05-14 15:20
Author: carlcarl
Post_ID: 1426
Category: linux
Tags: kde
Slug: kdialog_with_crontab


環境是用 KDE plasma 5, script 範例:

	:::bash
	#!/bin/sh

	export DISPLAY=:0
	export QT_PLUGIN_PATH=/usr/lib/plugins:/usr/lib/qt5/plugins:/usr/lib/qt5/plugins:/lib/kde5/plugins/
	export KDE_FULL_SESSION=true

	# Fix warning
	export XDG_RUNTIME_DIR=/run/user/1000

	kdialog --msnbox "hello" --title "title"



因為 crontab 不知道這個 UI 顯示是要顯示在哪個螢幕上，所以要指定 `DISPLAY`，`KDE_FULL_SESSION` 也會影響。`QT_PLUGIN_PATH` 我是直接複製我 GUI 使用者的設定，這邊可以看到是 qt5，如果是用 KDE 4 的話，大概是用 qt4，不確定就是，如果少掉這個設定，kdialog 會 fallback 成比較醜的介面，看起來不太舒服。接著在 crontab 裡設定執行上述的 script 即可。


Ref:

* [Trying to use kdialog in cron]



[Trying to use kdialog in cron]: https://forums.opensuse.org/showthread.php/443251-Trying-to-use-kdialog-in-cron


