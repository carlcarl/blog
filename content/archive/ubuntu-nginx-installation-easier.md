Title: Ubuntu nginx installation(easier)
Date: 2011-06-21 00:31
Author: carlcarl
Post_ID: 25
Category: linux
Slug: ubuntu-nginx-installation-easier

從 [之前這篇][] 做了點修改

	:::bash
	apt-get install nginx php5-cli php5-cgi spawn-fcgi psmisc

接著在 `/etc/nginx/sites-available/` 底下會有個 `default`，直接來修改這個檔案:

	:::text
	server {
		listen   80 default;
		server_name  localhost;
		access_log  /var/log/nginx/localhost.access.log;
		location / {
			root   /var/www/nginx-default;
			index   index.php;
		}
		location /phpmyadmin {
		root /usr/share;
		index index.php;
		}
		location ~ .php$ {
			set $php_root   /var/www/nginx-default;
			if ($request_uri ~* /phpmyadmin) {
				set $php_root /usr/share;
			}
			fastcgi_pass 127.0.0.1;
			fastcgi_index  index.php;
			fastcgi_param  SCRIPT_FILENAME  $php_root$fastcgi_script_name;
			include /etc/nginx/fastcgi_params;
		}
	}


修改完後來安裝 `php-fpm`，不過我用 10.04 LTS 是找不到這個套件的，所以一開始就要加入某個來源:

	:::bash
	sudo aptitude install python-software-properties
	sudo add-apt-repository ppa:brianmercer/php
	sudo aptitude -y update


接著安裝:

	:::bash
	sudo aptitude -y install php5-fpm

最後啟動 service 就 ok 了:

	:::bash
	sudo service php5-fpm start
	sudo service nginx start

另外有些在參考網頁裡還有加上一些設定 我覺得應該不需要修改也可以 work，試試看唄

 

參考網頁:

<http://gerardmcgarry.com/blog/how-install-php-fpm-nginx-ubuntu-1004-server>

  [之前這篇]: /24/ubuntu-nginx-installation
