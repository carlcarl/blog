Title: Simple IPython notebook extension
Date: 2014-05-27 23:30
Author: carlcarl
Post_ID: 1398
Category: python
Tags: ipython
Slug: simple_ipython_notebook_extension


最近練習寫了一個 [IPython] 的 notebook extension，查了一些資料就開始著手了。首先是一個簡單的 template，可以在 [IPython extensions] 這邊找到:

	:::python
	# myextension.py

	def load_ipython_extension(ipython):
    	# The ``ipython`` argument is the currently active
    	# :class:`InteractiveShell` instance that can be used in any way.
    	# This allows you do to things like register new magics, plugins or
    	# aliases.

	def unload_ipython_extension(ipython):
    	# If you want your extension to be unloadable, put that logic here.

`load_ipython_extension` 就是載入這個 extension 後要做的事，`unload_ipython_extension` 就是卸載後要做的事。

參考上面連結的內容，接下來要在設定檔裡加入以下設定:

	:::python
	c.InteractiveShellApp.extensions = [
    	'myextension'
	]

但是我卻不知道是哪個設定檔(炸)，查了一下，如果是要在 notebook 版本的加入的話，預設會在 `~/.ipython/profile_default/ipython_notebook_config.py`，如果沒有的話，可以試試看輸入 `ipython profile create`，印象中這樣就會生出來(記憶力不太好...|||)。


然後根據我的需求，我需要輸入一些自定的的 command，然後根據參數做不同事，這裡查到 [define_magic] 這個 method 可以用，以下是官方的範例:

	:::python
	def foo_impl(self,parameter_s=''):
    	'My very own magic!. (Use docstrings, IPython reads them).'
    	print 'Magic function. Passed parameter is between < >:'
    	print '<%s>' % parameter_s
    	print 'The self object is:', self

	ipython.define_magic('foo',foo_impl)

接著可以把這一段加入到 `myextension.py` 中的 `def load_ipython_extension(ipython)` 裡面，然後在 ipython notebook 的介面輸入 `foo` 就會跑到 `foo_impl` 這個 method 來，如果輸入 `foo bar`，`parameter_s` 就會是 `'bar'`。這邊要注意一個地方：如果是輸入 `foo bar test`，`parameter_s` 會是 `'bar test'` (炸)，所以可能還要自己再呼叫個 `parameter_s.split()` 來把參數切成 list 這樣。

然後 `ipython.define_magic('foo',foo_impl)` 的 `ipython` 是從最上面程式片段中的 `load_ipython_extension(ipython)` 的 `ipython` 這個參數來的。

實際的範例可以參考我寫的 [curator-for-ipython]
 


[IPython]: http://ipython.org/
[IPython extensions]: http://ipython.org/ipython-doc/rel-0.12.1/config/extensions/index.html#extensions-overview
[define_magic]: http://ipython.org/ipython-doc/rel-0.12.1/api/generated/IPython.core.interactiveshell.html#IPython.core.interactiveshell.InteractiveShell.define_magic
[curator-for-ipython]: https://github.com/carlcarl/curator-for-ipython



