Title: Shellcheck
Date: 2015-06-10 15:00
Author: carlcarl
Post_ID: 1431
Category: shell
Tags: shellcheck
Slug: shellcheck


最近發現的工具: [Shellcheck]，可以檢查 shell 的 syntax，還不錯用。

usage: `shellcheck xxx.sh`

除了會顯示錯誤外，也會警告一些用法或是沒用到的 variable，紅色的代表錯誤，咖啡色的通常是沒用到的 variable，綠色比較偏向 style 和寫法的改進。

如果想關掉某些 warning 的話，譬如 `SC2129: Consider using { cmd1; cmd2; } >> file instead of individual redirects.` 就可以下 `shellcheck -e 2129 xxx.sh`，如果嫌麻煩的話，可以另外自己設一個 alias，譬如: `alias sc="shellcheck -e 2129"`。


如果自己想裝來試試看的話：

	:::bash
	sudo apt-get install cabal-install
	sudo cabal update
	sudo cabal install shellcheck --global


另外雖然 shell 本身也有類似的可以用:

	:::bash
	sh -n xxx.sh

但是沒辦法檢查到所有的錯誤，所以並不是很好用。



[Shellcheck]: http://www.shellcheck.net/about.html



