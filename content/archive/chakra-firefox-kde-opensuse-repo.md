Title: Chakra firefox-kde-opensuse repo
Date: 2012-06-09 01:29
Author: carlcarl
Post_ID: 512
Category: linux
Tags: chakra, firefox, firefox-kde-opensuse
Slug: chakra-firefox-kde-opensuse-repo

2012/10/14 更新  
firefox-kde-opensuse 已經進 chakra 的 bundle 了，就叫 firefox ，以後從
bundle 裡安裝即可，就不用加以下的 repo ，而且 repo
畢竟不是官方的，所以更新維護上可能也會有點問題。

* * * * *

因為 firefox-kde-opensuse 要自己編太麻煩了，所以加個 repo
這樣以後安裝比較省時，是說要不是 [Whiksy][]
有提供我還真的不知道原來有......。  
<!--more-->  
以下複製到 `/etc/pacman.conf` 中：

    [chakra-gtk-repo]
    Server = http://chakra-gtk-repo.tk/repo/x86_64/
    [packccr]
    Server = http://repo.stephenmac.com/

這樣就 OK 了。

  [Whiksy]: http://www.plurk.com/maxwux
