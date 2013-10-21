Title: Ubuntu Nginx installation
Date: 2011-06-13 15:51
Author: carlcarl
Post_ID: 24
Category: linux
Slug: ubuntu-nginx-installation

[更新] 這邊有修改過的[簡單版][]

 

弄了好久，參考了幾篇教學，應該算是能跑了吧囧a。話說有幾篇教學講得都不太一樣 害我也不知道該看哪篇才好，後來是找了[這一篇][]來作看看。

首先先抓套件來安裝吧:

	:::bash
	apt-get install nginx php5-cli php5-cgi spawn-fcgi psmisc
 

接著在 `/etc/nginx/sites-available/`，底下應該會有個 `default` 設定檔，直接來修改這個檔案:

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
			fastcgi_pass unix:/var/run/php-fastcgi/php-fastcgi.socket;
			fastcgi_index  index.php;
			fastcgi_param  SCRIPT_FILENAME  $php_root$fastcgi_script_name;
			include /etc/nginx/fastcgi_params;
		}
	}


`listen` 指定 port，而 `location /` 的 `root` 位置，安裝完 `nginx` 之後，通常網頁目錄會是這個位置。另外我還有安裝 phpmyadmin，所以這邊有 phpmyadmin 的設定，至於在最後面的 `location` 設定，需要用 `if` 來判斷是在 `/var/www/nginx-default` 還是 `/usr/share` 來設定 `SCRIPT_FILENAME`，不然 phpmyadmin 會有錯誤。


接著在 `/usr/bin` 底下新增一個檔案叫做 `php-fastcgi`，將以下內容複製進去

 

	:::bash
	#!/bin/bash
	FASTCGI_USER=www-data
	FASTCGI_GROUP=www-data
	SOCKET=/var/run/php-fastcgi/php-fastcgi.socket
	PIDFILE=/var/run/php-fastcgi/php-fastcgi.pid
	CHILDREN=6
	PHP5=/usr/bin/php5-cgi
	/usr/bin/spawn-fcgi -s $SOCKET -P $PIDFILE -C $CHILDREN -u $FASTCGI_USER -g $FASTCGI_GROUP -f $PHP5

然後修改權限:

	:::bash
	chmod +x /usr/bin/php-fastcgi

 

接著在 `site-enabled` 底下建立一個到 `sites-available` 底下 `default` 的連結:

	:::bash
	cd /etc/nginx/sites-enabled/
	ln -s /etc/nginx/sites-available/default

 

接下來到 `/etc/init.d/` 底下建立一個 `php-fastcgi` 的檔案，以下是內容:

	:::bash
	#!/bin/bash
	PHP_SCRIPT=/usr/bin/php-fastcgi
	FASTCGI_USER=www-data
	FASTCGI_GROUP=www-data
	PID_DIR=/var/run/php-fastcgi
	PID_FILE=/var/run/php-fastcgi/php-fastcgi.pid
	RET_VAL=0
	case "$1" in
	start)
		if [[ ! -d $PID_DIR ]] 
		then
			mkdir $PID_DIR
			chown $FASTCGI_USER:$FASTCGI_GROUP $PID_DIR
			chmod 0770 $PID_DIR
		fi
		if [[ -r $PID_FILE ]]
		then
			echo "php-fastcgi already running with PID `cat $PID_FILE`"
			RET_VAL=1
		else
			$PHP_SCRIPT
			RET_VAL=$?
		fi
	;;
	stop)
		if [[ -r $PID_FILE ]]
		then
			kill `cat $PID_FILE`
			rm $PID_FILE
			RET_VAL=$?
		else
			echo "Could not find PID file $PID_FILE"
			RET_VAL=1
		fi
	;;
	restart)
		if [[ -r $PID_FILE ]]
		then
			kill `cat $PID_FILE`
			rm $PID_FILE
			RET_VAL=$?
		else
			echo "Could not find PID file $PID_FILE"
		fi
		$PHP_SCRIPT
		RET_VAL=$?
	;;
	status)
		if [[ -r $PID_FILE ]]
		then
			echo "php-fastcgi running with PID `cat $PID_FILE`"
			RET_VAL=$?
		else
			echo "Could not find PID file $PID_FILE, php-fastcgi does not appear to be running"
		fi
	;;
	*)
		echo "Usage: php-fastcgi {start|stop|restart|status}"
		RET_VAL=1
	;;
	esac
	exit $RET_VAL


最後就是設定並啟動服務啦:

	:::bash
	chmod +x /etc/init.d/php-fastcgi
	update-rc.d php-fastcgi defaults
	/etc/init.d/php-fastcgi start
	/etc/init.d/nginx start


第一行是將這個檔案加上執行權限，`update-rc.d` 將這個檔案加入預設開機就會執行的服務，後面兩行就是執行這兩個服務了。

 

接下來可以在 `/var/www/nginx-default` 底下建立一個 `index.php`，裡面可以加上以下的內容來驗證是否正確:

	:::bash
	<?php phpinfo(); ?>
 

大致差不多就是這樣。根據我個人的經驗 好像是只要改到一些設定的話，nginx 和 php-fastcgi 都要重啟才會生效的樣子。另外教學網頁中有講的 unix socket 和 tcp socket 的設定也不太一樣，效能上 unix socket 應該會好些。

 

參考網址:  
<http://arnisoft.com/253/nginx-phpmyadmin-configuration/>  
<http://i.laoer.com/nginx-alias-php.html>  

  [簡單版]: /25/ubuntu-nginx-installation-easier/
  [這一篇]: http://library.linode.com/web-servers/nginx/php-fastcgi/ubuntu-10.04-lucid
