Title: mod_wsgi with newer python version
Date: 2015-02-27 00:30
Author: carlcarl
Post_ID: 1414
Category: python
Tags: python
Slug: mod_wsgi_with_newer_python_version


在執行 Apache + mos_msgi + Django 的時候出現了問題：`no module named importlib`。

因為系統是比較舊的 Ubuntu，Python 版本是 2.6，我 Django 是用 1.7，不相容 Python 2.6 以下，所以自己又另外裝了 Python 2.7。本來以為把 virtualenv 設定好後就沒事了，結果因為系統提供的 mod_wsgi 是用 Python 2.6 編譯的，沒有 `importlib` 這個 module，所以就掛了。


解法很直接，另外下載 mod_wsgi 的 source code: [mod_wsgi]，然後用 Python 2.7 來編譯就可以了:

	:::shell
	./configure  --with-python=/usr/bin/python2.7
	make
	sudo make install

是說這個問題也是卡超久啊...，一開始根本搞不清楚狀況。


Ref:

* [Django / Apache / mod_wsgi: No module named importlib]
* [Installing mod_wsgi error - config.status: error: cannot find input file: Makefile.in]
* [How can I rebuild my mod_wsgi to use python 2.7.3?]



[mod_wsgi]: https://github.com/GrahamDumpleton/mod_wsgi
[Django / Apache / mod_wsgi: No module named importlib]: http://stackoverflow.com/questions/11492683/django-apache-mod-wsgi-no-module-named-importlib
[Installing mod_wsgi error - config.status: error: cannot find input file: Makefile.in]: http://serverfault.com/questions/658666/installing-mod-wsgi-error-config-status-error-cannot-find-input-file-makefi
[How can I rebuild my mod_wsgi to use python 2.7.3?]: http://stackoverflow.com/questions/16854023/how-can-i-rebuild-my-mod-wsgi-to-use-python-2-7-3


