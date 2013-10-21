Title: FreeBSD set default shell to bash
Date: 2011-11-06 08:58
Author: carlcarl
Post_ID: 50
Category: FreeBSD
Tags: bash, freebsd
Slug: freebsd-set-default-shell-to-bash

最近興致來，就想說來把 FreeBSD 上的 csh 改成 bash，畢竟我還是比較習慣用 bash～。

首先先修改預設 shell：

	:::bash
	chsh -s /usr/local/bin/bash


輸入密碼後就修改成功了～。  
   

再下來你可能會有一個已經有設定過的 `.bashrc` 檔案，當你放到家目錄底下的時候可能會發現說："怎麼都沒有反應？"，那是因為FreeBSD這邊吃的是 `.bash\_profile`這個設定檔=.=||，為了能夠兼容，我是自己又另外開了 `.bash_profile` 檔案，然後在裡面輸入：

	:::bash
	source ~/.bashrc


這樣以後就只要更新 `.bashrc` 這個設定檔就好了～。  
   

然後後來又遇到中文無法輸入的問題，這個只要在 `.bashrc` 檔案中加入語系設定就可以了，另外再加上 `ls` 的 `alias`，不然 `ls` 輸出的目錄都不會標顏色：

	:::bash
	export LANG=zh_TW.UTF-8
	export LC_CTYPE=zh_TW.UTF-8
	alias ls='ls -G'

   
如果在 `.bashrc` 裡需要針對OS作判斷的話可以使用 `uname`：

	:::bash
	OS=$('uname')

 

參考網址：

chsh

<http://unix.ctocio.com.cn/138/9289638.shtml>
<http://hsiao-ting.blogspot.com/2007/09/freebsdbash_19.html>

.bash\_profile

<http://franks543.blogspot.com/2007/03/bashrc-bashprofile-freebsd.html>

中文輸入

<http://netlab.cse.yzu.edu.tw/~statue/freebsd/zh-tut/shell.html>
<http://blog.csdn.net/magicbreaker/article/details/2296907>

color

<http://www.cyberciti.biz/tips/freebsd-how-to-enable-colorized-ls-output.html/>
<http://blog.tenyi.com/2007/10/shellcolor-prompt.html/>

OS

<http://stackoverflow.com/questions/394230/detect-os-from-a-bash-script/>
<http://www.cyberciti.biz/tips/freebsd-how-to-enable-colorized-ls-output.html/>
<http://blog.csdn.net/magicbreaker/article/details/2296907/>
