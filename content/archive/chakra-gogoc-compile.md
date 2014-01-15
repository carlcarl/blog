Title: Chakra gogoc compile
Date: 2012-06-07 02:31
Author: carlcarl
Post_ID: 499
Category: linux
Tags: chakra, gogoc
Slug: chakra-gogoc-compile

之前在 [Ubuntu 系列上可以很方便的安裝 gogoc][]，但是後來換到 Chakra
之後，ccr 裡並沒有提供安裝包，沒辦法，只好自己編譯。



1.首先先下載安裝包(不能下載的話，就必須到[官網][]註冊帳號並下載囉)、解壓縮，並進入到資料夾中：

	:::bash
	wget http://content.gogo6.com/gogoc-1_2-RELEASE.tar.gz
	tar -xf gogoc-1_2-RELEASE.tar.gz
	cd gogoc-1_2-RELEASE/gogoc-tsp

 

2.接下來是編譯，這邊沒意外的話會有錯（至少我是這樣XD），所以要先做點修改，將
    `#include <stddef.h>` 加到
    `../gogoc-messaging/gogocmessaging/message.h`
    的檔案最上方即可，這邊提供一下錯誤訊息的片斷：

<!-- -->

	:::text
    src/clientmsgsender.cc:145:17: error: expected primary-expression before 『,』 token
 

3.正式編譯（這邊如果還是有錯的話，就是相依套件的問題，可以參考它的
    `INSTALL` 檔案中的套件相依性解說）：

~~~~
make all
~~~~

 

4.以 root 權限安裝：

~~~~
sudo make installdir=/usr/local/gogoc install
~~~~

 
5.修 設定檔，設定檔以上面的安裝路徑來說，會是
    `/usr/local/gogoc/bin/gogoc.conf`
    這個檔案，檔案該如何修改可以參考[我之前這篇][Ubuntu
    系列上可以很方便的安裝 gogoc]。

 

6.為了執行方便，在`/usr/local/bin`中建立一個連結：

	:::bash
	sudo ln -s /usr/local/gogoc/bin/gogoc /usr/local/bin/gogoc

 

7.手動執行，這邊要用 root 權限執行並指定設定檔位置才行，不然會有
    `gogoc Failed to open specified file.` 的錯誤：

	:::bash
	sudo gogoc -f /usr/local/gogoc/bin/gogoc.conf
 

8.如果執行的時候出現以下錯誤不代表失敗，可以利用
<http://test-ipv6.com/> 這個網站實際測試，如果滿分就 OK 囉。

    TSP version not supported by server: 2.0.2.
    Failed to retrieve TSP capabilities.
    Disconnected. Retrying.

9.考慮加入開機時執行，這邊就看你要怎麼放了，我是在`~/.kde4/Autostart`
    中寫一個簡單的 shell，然後這個檔案裡加入上面的這行指令這樣。  
     

參考網址：  

<http://www.gogo6.com/group/gogoclientdevelopment/forum/topics/clientmsgsender-cc-in-member-function-avoid-gogocmessaging>

  [Ubuntu 系列上可以很方便的安裝 gogoc]: http://blog.carlcarl.tw/397/ubuntu-tunnel-broker
    "Ubuntu Tunnel Broker IPv6 連 中研院"
  [官網]: http://www.gogo6.com/
