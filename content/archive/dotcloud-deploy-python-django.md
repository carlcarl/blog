Title: Dotcloud deploy python+django
Date: 2011-06-21 09:00
Author: carlcarl
Post_ID: 27
Category: python
Slug: dotcloud-deploy-python-django

[dotcloud][] 是個可以讓你佈署網站的平台，而且提供了 python, php, ruby 甚至是最近剛發展起來的 node.js 都有，資料庫方面也支援了幾種 像是最常見的 mysql, sqlite, mongodb 等，另外我看了一下 居然還有 hadoop!  感覺還滿有趣的。

除了提供多種開發套件以外，dotcloud 有個不錯的地方是支援ssh連線登入，超方便!

 

之前在 PTT 就有看過有人在講這個服務了，雖然現在還在beta的階段 不過就我現在用起來 感覺其實還滿不錯的，希望以後還是有提供免費的服務XD。如果要註冊的話，這部份還滿特別的，先在首頁輸入 email，接著等大概一天吧(還滿久的 = =||)，就會收到email認證，接著就能順利註冊了。

 

這次我要在 dotcloud 上裝的是 python + django。首先先準備裝套件吧 話說 python-setuptools 這個套件，官網好像沒有講得很清楚，查了一下才發現要裝，不然會沒 easy_install 這指令:

	:::bash
	sudo apt-get install python python-setuptools
	sudo easy_install dotcloud

 

接著是開 project 啦，test 是我測試的名稱，可以依據需要修改:

	:::bash
	dotcloud create test


輸入完後 應該會要求你輸入 API key，這個就去網頁的設定部份就找得到了，複製貼上即可。

 

開完 project，接著要指定使用的語言和 url 位置。如果這邊輸入 test.www 的話，到時候 url 就會是`www.test.dotcloud.com` 這樣:

	:::bash
	dotcloud deploy -t python test.www

 

接著開一個資料夾，並且在裡面開個 django project 在加上一些設定檔:

	:::bash
	mkdir test-on-dotcloud
	cd test-on-dotcloud
	echo django > requirements.txt
	django-admin.py startproject test

 

在 test-on-dotcloud 底下開一個 wsgi.py 檔，輸入以下內容(test.setting 的 test 記得根據前面的設定作修改):

	:::python
	import os
	import sys
	os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'
	import django.core.handlers.wsgi
	djangoapplication = django.core.handlers.wsgi.WSGIHandler()
	def application(environ, start_response):
		if 'SCRIPT_NAME' in environ:
			del environ['SCRIPT_NAME']
		return djangoapplication(environ, start_response)

 

<span style="color: #ff0000;">記得不要把 wsgi.py 和 requirements.txt 放進去 test 裡面，這樣一定會失敗</span>


接著在 test-on-dotcloud 底下執行:

	:::bash
	dotcloud push test.www .


<span style="color: #ff0000;">記得不要漏掉 test.www 後面的點</span>

接著連上 www.test.dotcloud.com 應該就可以看到成功的訊息了。(這個網域名照理來說應該在前面會發生有重複名稱的錯誤(我猜啦)所以實際上應該不會輸入到這個網址才對XD)

 

參考網頁

<http://simple-is-better.com/news/378>

<http://docs.dotcloud.com/tutorials/django/>

<http://docs.dotcloud.com/cli/\#install-dotcloud/>

<http://dmyz.org/archives/110>

 

 

  [dotcloud]: https://www.dotcloud.com/
  [http://docs.dotcloud.com/cli/\#install-dotcloud]: http://docs.dotcloud.com/cli/#install-dotcloud
