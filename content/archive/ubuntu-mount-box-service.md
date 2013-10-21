Title: Ubuntu mount Box service
Date: 2012-04-20 00:20
Author: carlcarl
Post_ID: 390
Category: linux
Tags: box, boxfs
Slug: ubuntu-mount-box-service

之前在 PTT 看到有人分享可以用 boxfs 這個套件來掛載 [Box][] 到本地端的資料夾上，感覺好像還不錯，而且因為之前買 Sony Ericsson 的手機，所以有 Box 額外送的 50G 空間，所以就想說拿來加減用啦。

首先要先安裝相依的套件：

	:::bash
	sudo apt-get install libxml2-dev libfuse-dev libcurl4-gnutls-dev libzip-dev


接著到 [這邊][] 下載最新版本的 boxfs。下載完成後，解壓縮：

	:::bash
tar xzf boxfs-relno.tgz

 

接著進入 `box-版本` 資料夾，像我的就是 `boxfs-0.7`:

	:::bash
	cd boxfs-0.7

 

這邊還需要再另外安裝 libapp，這邊需要用到 git ，沒有的話就要安裝：

	:::bash
	sudo apt-get install git-core
	git clone http://github.com/drotiro/libapp.git
 

進入 libapp 資料夾並編譯安裝：

	:::bash
	cd libapp
	make
	sudo make install
	sudo ldconfig
	make apptest

 
安裝好 libapp 之後，到外層的資料夾並編譯安裝 boxfs：

	:::bash
	cd ..
	make
	sudo make install
 

到此 boxfs 套件算是安裝完畢，不過還需要登入並掛載到你的檔案系統上，這邊以掛載到你的家目錄底下
box 資料夾為例：

	:::bash
	mkdir ~/box
	boxfs -u usermail -p password ~/box
 

執行完後，check 一下你的 `~/box` 底下是否有東西，有的話就代表掛載成功囉~。 
 
目前我遇到的小問題是：  
如果我在手機端刪除掉檔案，在電腦上會發現檔案還存在，必須卸載後再掛載才會更新，卸載的話可以直接使用 `umount` 這個指令：

	:::bash
	umount ~/box
 

參考網址：  
<http://code.google.com/p/boxfs/wiki/Compiling>

  [Box]: http://www.box.com/
  [這邊]: http://code.google.com/p/boxfs/downloads/list
