Title: cherokee + django + uwsgi installation
Date: 2011-06-28 20:43
Author: carlcarl
Post_ID: 29
Category: python
Slug: cherokee-django-uwsgi-installation

首先要先裝好必要的套件，第一行先加入 cherokee 的來源，接著更新來源後才能夠安裝最新的 cherokee。rrdtool 以下三個都是在裝 uwsgi 所必要的套件，uwsgi 似乎找不到套件可以直接裝 這裡是利用pip 安裝網站上的來源: 

	:::bash
	sudo apt-add-repository ppa:cherokee-webserver/ppa
	sudo apt-get update
	sudo apt-get install cherokee
	sudo apt-get install rrdtool
	sudo apt-get install libcherokee-mod-rrd
	sudo apt-get install libxml2
	sudo pip install http://projects.unbit.it/downloads/uwsgi-latest.tar.gz

 

接著在 django 的 project 下加上兩個檔案:

django_wsgi.py

	:::python
	import os
	import django.core.handlers.wsgi
	os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
	application = django.core.handlers.wsgi.WSGIHandler()

 

uwsgi.xml (pythonpath位置設定就加上project的位置和project上一層的位址
這裡的django project的名稱假定為example)

	:::xml
	<uwsgi>
		<pythonpath>/var/www/example/</pythonpath>
		<pythonpath>/var/www/</pythonpath>
		<app mountpoint="/">
			<script>django_wsgi</script>
		</app>
	</uwsgi>


設定大致到這邊。

接下來是執行 cherokee-admin 開啟 web 的管理介面:

	:::bash
	sudo cherokee-admin -b

瀏覽器支援好像不太好 :P

這邊先點擊上面的 `vServers`，接著點選 `Behavior`

![cherokee][]

 

點選下方的 Rule Management

![cherokee2.png][]

 

點選左上角 Behavior 右邊的 + 按鈕

![cherokee3.png][] 

接著在左邊點選 Platforms，右邊選擇 uWSGI 接著點選 Add

![cherokee4.png][]

 

接下來點個 Next 就會來到這個畫面，這邊照理來說只會出現一個欄位，如果另外在上面還有要求選擇 uwsgi 的 binary file 的話，表示之前 uwsgi 沒安裝好。這個 Configulation File 就輸入 uwsgi.xml 在檔案系統上的路徑就 ok 了。以這裡的範例來講就會是: `/var/www/uwsgi.xml`

![cherokee5.png][]

接下來指定網頁路徑就大致成功了~

![cherokee6.png][]

 

參考網頁

<http://whhnote.blogspot.com/2011/01/django-deploy-django-on-cherokee-web.html>  
<http://www.cherokee-project.com/doc/cookbook_uwsgi.html>  
<http://felecan.com/2011/getting-django-work-uwsgi-cherokee/>  
<http://projects.unbit.it/uwsgi/wiki/Install>

  [cherokee]: http://i.imgur.com/8hHPP31l.png
    "cherokee"
  [cherokee2.png]: http://i.imgur.com/g1m4jHOl.png
    "cherokee2.png"
  [cherokee3.png]: http://i.imgur.com/Thb9nbAl.png
    "cherokee3.png"
  [cherokee4.png]: http://i.imgur.com/VSEMD4ol.png
    "cherokee4.png"
  [cherokee5.png]: http://i.imgur.com/TsO5hWBl.png
    "cherokee5.png"
  [cherokee6.png]: http://i.imgur.com/iQx7U3Bl.png
    "cherokee6.png"
