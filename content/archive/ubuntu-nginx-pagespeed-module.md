Title: Ubuntu nginx pagespeed module
Date: 2013-06-03 21:25
Author: carlcarl
Post_ID: 879
Category: linux
Tags: nginx, pagespeed, ubuntu
Slug: ubuntu-nginx-pagespeed-module

Ubuntu 版本：12.04 Nginx 版本：1.4.1 pagespeed 版本：1.5.27.3
記錄一下安裝的步驟： <!--more-->

	:::bash
    # 到 home 目錄下做，看個人習慣就是
    cd ~
    # add-apt-repository 這個指令需要裝 python-software-properties
    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:nginx/stable
    sudo apt-get update
    # 下載 nginx source code
    sudo apt-get source nginx
    # 裝 build nginx 需要的套件
    sudo apt-get build-dep nginx
    # 裝 pagespeed 需要的套件
    sudo apt-get install build-essential zlib1g-dev libpcre3 libpcre3-dev
     

    # 下載 pagespeed
    wget https://github.com/pagespeed/ngx_pagespeed/archive/release-1.5.27.3-beta.zip
    unzip release-1.5.27.3-beta.zip
    cd ngx_pagespeed-release-1.5.27.3-beta/
    wget https://dl.google.com/dl/page-speed/psol/1.5.27.3.tar.gz
    tar -xzvf 1.5.27.3.tar.gz
     
    cd ~/nginx-1.4.1/
    # 我會需要用到 https，所以加上 --with-http_ssl_module
    ./configure --add-module=$HOME/ngx_pagespeed-release-1.5.27.3-beta --with-http_ssl_module
    make
    sudo make install
     
    # 建個 link。也可以 link 到別的位置，不過記得下面 init sctipt 中的 DAEMON 的位置要跟著改
    sudo ln -s /usr/local/nginx/sbin/nginx /usr/local/sbin/nginx

如果在之前有裝過 nginx 的話，在 `/etc/init.d/` 底下應該有個 nginx 的
init script，我是直接用這個，不過還要加點修改：

	:::conf
    # DAEMON 改成這樣
    DAEMON=/usr/local/sbin/nginx

接著修改 `/usr/local/nginx/conf/nginx.conf`：（這邊是因為我在 configure
的時候沒有另外指定位置，所以在這裡）

	:::text
    # pid 改成這樣，以對應到 init script 中的設定，不然不能 restart 和 stop
    pid /var/run/nginx.pid;
    ...
    http {
        # 加上這兩行以啟用 pagespeed
        pagespeed on;
        pagespeed FileCachePath /var/ngx_pagespeed_cache;
    ...
    }

接著編輯每個 virtualhost 的 conf：

	:::text
    server {
    ...
        # 加上以下幾行
        location ~ "\.pagespeed\.([a-z]\.)?[a-z]{2}\.[^.]{10}\.[^.]+" { add_header "" ""; }
        location ~ "^/ngx_pagespeed_static/" { }
        location ~ "^/ngx_pagespeed_beacon$" { }
        location /ngx_pagespeed_statistics { allow 127.0.0.1; deny all; }
        location /ngx_pagespeed_message { allow 127.0.0.1; deny all; }
    ...
    }
    ...

新增 `/var/ngx_pagespeed_cache` 這個資料夾，並讓 nginx
有寫入的權限。這個資料夾是讓 pagespeed 放 cache 用的，視情況可以考慮放在
`/dev/shm/` 底下加快速度，不過我自己是還沒試過就是 :P。這邊我的 nginx
是用 `www-data`，如以下操作：

	:::bash
    sudo mkdir /var/ngx_pagespeed_cache
    sudo chown www-data:www-data /var/ngx_pagespeed_cache

啟動 nginx:

	:::bash
    sudo service nginx start

接著放個網頁並試試看以下指令，有的話就代表成功了

	:::bash
    curl -I -p 你的網址 | grep X-Page-Speed 

以上是基本的安裝，pagespeed
還有提供很多設定，要指定才會有效，之後有空再另外寫一篇補完。

參考網址：  
<https://github.com/pagespeed/ngx_pagespeed>  
<http://serverfault.com/questions/502764/how-to-build-nginx-1-4-0-and-ngx-pagespeed-in-ubuntu-debian>
<http://serverfault.com/questions/180808/how-to-get-latest-nginx-using-apt-ubuntu>
<https://www.digitalocean.com/community/articles/how-to-install-the-latest-version-of-nginx-on-ubuntu-12-10>
<http://blog.linuxeye.com/318.html>
