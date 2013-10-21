Title: Install openid server: masquerade
Date: 2012-03-21 04:08
Author: carlcarl
Post_ID: 287
Category: 未分類
Tags: masquerade, openid, RoR
Slug: install-openid-server-masquerade

![masquerade][] 

最近需要安裝 openid server，所以找了很多的 library
來試，我是從這個[openid server
清單][]下去找，主要功能需求是希望能夠支援多人+資料庫+可以直接連線做認證的部份，但是試了好幾個
php, python 的沒一個可以說是符合我需求的，perl
那個文件更是完全看不懂orz。

後來考慮試試看[masquerade][1] 這個基於 RoR 的
library，建完之後發現幾乎符合我的需求，而且安裝基本上不會說太難，所以就選這套啦。作者在
github project 首頁的 README 是比較新的版本(相較於它的 project wiki
)，但是還是有部份是有問題的，所以我另外 fork 出來，再修改一下
README，這是[我的連結][]。

首先要先建立好 RoR 的環境，這邊提供一個可以作為參考的[連結][]，另外
mysql 和 postfix 也可以先安裝好。

接著輸入指令將程式下載下來，這是我的 fork，README 部份有更新，另外修正了
yml 的格式錯誤

	:::bash
	git clone https://carlcarl@github.com/carlcarl/masquerade.git


進入 masquerade 目錄會有提示建議你用 nvm
安裝一個ruby版本，照著它給的指令安裝就OK了。

	:::bash
	cd masqurade


接著可以按照我連結裡的 README 來作，中途有遇到的問題我加進 README 裡的
Notice 部份，我這邊另外列出比較要注意的幾點

1.  設定部份他有分 development, test 和 production
    環境，所以要注意你在啥環境底下執行和要修改哪個環境的設定
2.  database.yml 的部份，想方便的話就只要修改帳號為 root 和修改密碼為
    root 的密碼，資料庫它會幫你建立
3.  app_config.yml
    大部分設定可以先放著不動，等到大致功能測試完畢再來修改也可以。
4.  port預設是在 3000，所以在認證的時候在網址裡也要將 port 加進去。
5.  認證的部份比較詭異的是**它不是直接提供輸入帳密認證的欄位**，而是叫你去網頁裡的連結登入(如下圖)，登入完之後它會再認證，這部份的原理我猜是它在之前把相關的
    request 寫到 session 裡了，所以登入後會去讀之前存的的 request
    session，在允許認證完後，它就會自動導回 client 端去。

![masqurade2](http://i.imgur.com/AG7YaZAl.png)


參考網址：  
<http://railsforum.com/viewtopic.php?id=26700>  
<http://stackoverflow.com/questions/4980877/rails-error-couldnt-parse-yaml>  
<http://www.reyesyang.info/articles/10-rails3-could-not-parse-yaml>

  [masquerade]: http://i.imgur.com/cdwZUHDl.png
    "masquerade"
  [openid server 清單]: http://wiki.openid.net/w/page/12995226/Run-your-own-identity-server
  [1]: https://github.com/dbloete/masquerade
  [我的連結]: https://github.com/carlcarl/masquerade
  [連結]: http://www.cnblogs.com/feichan/archive/2011/11/16/2251659.html
