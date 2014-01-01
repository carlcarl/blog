Title: Chakra vim not support pythoncomplete
Date: 2012-06-17 22:47
Author: carlcarl
Post_ID: 515
Category: linux
Tags: chakra, python, vim
Slug: chakra-vim-not-support-pythoncomplete

最近在 Chakra 上用 vim 寫 python
的時候才突然發現這個問題，原因似乎是因為 vim 在編譯的時候沒有加上 python
的編譯參數，解決這個問題很簡單，只要改安裝 `vim-qt-git` 就 OK
了，因為它所提供的 vim 是有支援 pythoncomplete 的。vim-qt-git
本身包含一套完整的 vim 以及加上 GUI 的套件，所以安裝的時候會要求將原本的
vim 移除掉，允許移除後，就能順利安裝並使用 pythoncomplete 的補完功能了。

參考網址：  
<https://bbs.archlinux.org/viewtopic.php?id=122091>  
<https://wiki.archlinux.org/index.php/Vim>  

<http://blog.linuxtty.com/post/13022099749/archlinux-vim-python-support>
