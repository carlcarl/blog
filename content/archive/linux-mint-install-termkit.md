Title: Linux Mint install Termkit
Date: 2011-09-04 08:15
Author: carlcarl
Post_ID: 41
Category: js, node.js
Tags: node.js, npm, termkit
Slug: linux-mint-install-termkit

[![1315124444-2969515523][]][1315124444-2969515523]

其實之前就有看到這個東西了，當時覺得還滿炫的，不過當時好像只有支援 Mac 的樣子，後來就沒去理了。最近又看到這樣東西，發現在 Linux 上面已經有成功執行的例子了，所以想說也來裝裝看這樣，我目前是在 Linut Mint 上面裝，Ubuntu 應該理所當然也可以。

這個工具簡單講算是在機器上跑一個Server，然後再利用瀏覽器連上去，所以必須在 webkit 瀏覽器上面執行的樣子，像是 chrome(或 chromium)或是safari瀏覽器才能跑。

首先一開始先把需要的套件裝一裝吧

	:::bash
	sudo apt-get install build-essential git libssl-dev

 

接下來有三個東西要裝：node.js、npm、termkit。

開始裝 node.js，一開始偷懶想直接裝套件的版本，不過在後面卻一直打牆，後來才發現套件版的版本舊的可怕，[npm的安裝需要node.js較新的版本][]，所以不建議裝套件版的！但是也有發現[新版unstable的版本也是有點問題][]，所以建議大家去[官網][]抓個 stable 的版本比較安全，也比較省時間XD。

將 node.js 壓縮檔下載下來之後作解壓縮，然後進入解壓縮的目錄輸入以下指令：

	:::bash
	./configure
	make
	sudo make install

 
接著要安裝 npm 這個 node.js 的套件管理工具，要記得不要使用 apt-get 之類的去裝，因為根本沒有這個東西，你可能輸入 npm 之後，假如你沒裝，他會建議你去裝一個套件，但是那個套件只是指令剛好同名而已，可以不用理。這邊利用 git 下載：

	:::bash
	git clone http://github.com/isaacs/npm.git
	cd npm
	sudo make install
	

前面裝 node.js 之所以沒有用 git 是因為抓下來的版本是 unstable，好像也可以設定版本啦，不過有點懶得用就是了。

 

裝好之後，接下來來裝 TermKit 啦：

	:::bash
	cd ..
	git clone https://github.com/Floby/TermKit.git --recursive
	cd TermKit/
	npm install
	node Node/nodekit.js


（要注意一下自己放的目錄，最好是不要把某個目錄放在其他兩個目錄裡，難保不會有事......。）

最後一行的 `node Node/nodekit.js` 是執行這個工具的意思，所以接下來可以用瀏覽器連 `localhost:2222` 看看，應該就看得到囉。

 

雖然用起來還滿炫的，不過實際功能還是有點弱，像是 `clear` 這個指令目前是沒有作用的。

[![1315126055-3193988822][]][1315126055-3193988822]

另外如果想開 `vim` 的話也是直接炸。

[![1315126080-3520003698][]][1315126080-3520003698]

所以目前還比較像體驗性質感覺的就是了，希望之後的功能還能更加完善囉。

 

參考網址：  

<http://blog.easytech.com.ar/2011/05/21/playing-with-termkit-with-chrome/>  
<http://clonn.blogspot.com/2011/01/nodejs-npm.html>

  [1315124444-2969515523]: http://i.imgur.com/6ZoWGJLl.png
  [npm的安裝需要node.js較新的版本]: https://github.com/isaacs/npm/issues/1185
  [新版unstable的版本也是有點問題]: http://askubuntu.com/questions/54617/error-while-installing-termkit
  [官網]: http://nodejs.org/#download
  [1315126055-3193988822]: http://i.imgur.com/BSqCtg0.png
  [1315126080-3520003698]: http://i.imgur.com/7jQ5RA6l.png
