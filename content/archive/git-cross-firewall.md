Title: git cross firewall
Date: 2013-03-17 23:33
Author: carlcarl
Post_ID: 808
Category: 版本管理
Slug: git-cross-firewall

`git://` readonly 的 port 是使用
9418，雖然速度較快，但是也容易被防火牆擋掉，查了一下資料，發現一個不錯的方法：

	:::bash
    git config --global url."https://".insteadOf git://

輸入以上指令就可以把 git 開頭的自動轉爲 https
協定的了，自然就不會無緣無故被擋掉。那爲什麼不直接一開始就改掉就好呢？以我的例子來說，如果我抓了一個別人的
git repo，裏面包含 submodule，且是
`git://`，因爲我沒辦法直接改他的設定，這時就可以考慮這樣用。

設定的部分存在 `~/.gitconfig`，不需要的話可以直接從這邊拿掉。

參考網址：  

<http://stackoverflow.com/questions/4891527/git-protocol-blocked-by-company-how-can-i-get-around-that>
