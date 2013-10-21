Title: Another plugin set completefunc! Disabled neocomplcache
Date: 2013-01-10 20:33
Author: carlcarl
Post_ID: 738
Category: vim
Tags: neocomplcache, vim
Slug: another-plugin-set-completefunc-disabled-neocomplcache

最近替 vim 加上了 cscope
的設定後，` neocomplcache `突然有時候會出現問題，查了一下資料發現只要加上一行就可以解決了：

	:::bash
	let g:neocomplcache_force_overwrite_completefunc = 1


參考資料：  

<http://stackoverflow.com/questions/12975098/using-neocomplcache-and-clang-complete>  
<https://github.com/Shougo/neocomplcache/issues/276>
