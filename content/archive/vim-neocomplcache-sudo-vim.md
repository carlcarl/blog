Title: vim neocomplcache sudo vim error
Date: 2012-08-13 17:51
Author: carlcarl
Post_ID: 584
Category: vim
Tags: neocomplcache, vim
Slug: vim-neocomplcache-sudo-vim

指令輸入 `sudo vim 檔案` 的時候會出現錯誤
`neocomplcache Please use sudo.vim plugin instead of sudo command...`
，不過目前遇到只有在 Ubuntu 環境底下有發生，FreeBSD 和 Chakra
倒是沒出問題。

因為我懶得去裝 sudo.vim
這個套件，而且操作會變麻煩，所以照它另外一個錯誤訊息建議去修改
`/etc/sudoers` 檔案，只要加上 `Defaults always_set_home` 這行就 OK 了。

參考網址：  
[https://github.com/Shougo/neocomplcache/issues/179][]  
[https://bbs.archlinux.org/viewtopic.php?id=72573][]

  [https://github.com/Shougo/neocomplcache/issues/179]: http://https://github.com/Shougo/neocomplcache/issues/179
  [https://bbs.archlinux.org/viewtopic.php?id=72573]: http://https://bbs.archlinux.org/viewtopic.php?id=72573
