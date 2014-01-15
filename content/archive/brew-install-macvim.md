Title: brew install Macvim
Date: 2013-06-07 19:56
Author: carlcarl
Post_ID: 893
Category: vim
Tags: brew, macvim
Slug: brew-install-macvim

單純小筆記一下，因為每次重裝都會忘記 XDD，放在自己 blog，以後比較好查。

如果只單純下 `brew install macvim` 的話，原本的 vim 還是會留著，如果想用
Macvim 裡的 vim 的話，你可能會想說移掉原本的 vim，然後用 `ln -s`，來建個
link 就好，不過實際做是不行的，會出現一些
error，如：`E254: Cannot allocate color`，解決方法很簡單，就是下：

	:::text
    brew install macvim --override-system-vim
    brew linkapps

這樣就會把原本的 vim 幹掉，直接套用 Macvim 裡的。

參考網址：  

<http://apple.stackexchange.com/questions/14299/replaced-usr-bin-vim-now-i-get-error-messages>  

<http://apple.stackexchange.com/questions/59375/how-do-i-install-macvim>
