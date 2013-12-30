Title: tig broken in tmux
Date: 2013-10-05 02:15
Author: carlcarl
Post_ID: 1375
Category: linux, 版本管理
Tags: screen, tig, tmux
Slug: tig-broken-in-tmux

這個問題已經困擾我滿久了，在 [tmux][] 裡用 [tig][]
畫面會一直破碎，不過一直找不到原因，最近想到，於是又找看看有沒有解法，後來試了[一篇][]裡面的做法就
OK 了 QQ。

靈感是在查資料的時候看到有人是因為在 `tmux.conf` 裡設定了
`default-terminal=xterm` 想到的，中間有試了一下 screen，發現 tig 在
screen 中是 OK 的，`echo $TERM` 得到的輸出是 `screen`，而我在 tmux
下得到的輸出卻是 `xterm-256color`，想說朝這個方向去找資料。這邊先找了
`tmux.conf` 中，但是我並沒有設定這個東西，看了
`.zshrc`，原來我是在這邊設定了
`export TERM=xterm-256color`，於是我參看上面連結裡的內容在設定 `TERM`
下面再加上了一行就 OK 了：

    [ -n "$TMUX" ] && export TERM=screen-256color

  [tmux]: http://tmux.sourceforge.net
  [tig]: https://github.com/jonas/tig
  [一篇]: https://wiki.archlinux.org/index.php/tmux
