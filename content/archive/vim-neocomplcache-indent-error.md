Title: vim neocomplcache indent error
Date: 2012-08-12 22:18
Author: carlcarl
Post_ID: 573
Category: vim
Tags: neocomplcache, vim
Slug: vim-neocomplcache-indent-error

最近裝了 [neocomplcache][] 這個 vim
plugin，但是在使用的時候發現，一旦按下 enter 鍵再加上有縮排的話會出現
`neocomplcache indent neocomplcache#smart_close_popup()`
的文字，查了一下資料好像是 [supertab 的問題][] 。

修正的方法是在 `vimrc` 檔案中加入下面這行：

	:::text
	let g:SuperTabCrMapping = 0

  [neocomplcache]: https://github.com/shougo/neocomplcache
  [supertab 的問題]: https://github.com/Shougo/neocomplcache/issues/88
