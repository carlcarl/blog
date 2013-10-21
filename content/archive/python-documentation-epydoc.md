Title: python documentation: epydoc
Date: 2012-04-01 16:05
Author: carlcarl
Post_ID: 335
Category: python
Tags: epydoc, python
Slug: python-documentation-epydoc

[epydoc][] 是利用 parse python 的程式來製作文件，文件的類型像是一般的 html 和 pdf 都能產生。我個人是比較偏好 html 的格式囉，它的 html 樣板跟 Javadoc 的配置差不多，比較習慣。

它 parse 程式的方法主要是利用 method 一開始的 `"""` 註解，不習慣寫的人可以參考它的 [欄位官方範例][]。

首先要先安裝 `epydoc`，在官方網站上沒講到 ubuntu
的安裝包，用 `apt-get` 也找不到，後來試看看 `pip install epydoc` 就 OK
了。這邊有點要注意的是，如果你的 project
是在 `virtualenv` 環境下的話，建議將 `epydoc` 也裝在 `virtualenv` 裡，不然它 parse 文件時在找相依 library 會有錯誤。

安裝好後就可以執行指令來 parse 了，將 `python_project資料夾` 改成你要
parse 的 project 資料夾名稱，另外再指定「你要的文件資料夾名稱」即可：

	:::bash
	epydoc --html python_project資料夾 -o 你要的文件資料夾名稱


其他更進階的指令參數可以參考[這邊][]。

如果出現 `ImportError: Settings cannot be imported, because environment
variable DJANGO_SETTINGS_MODULE is undefined.` 錯誤的話，最簡單的方式可以在 project
裡的 `**init**.py` 裡加上：

	:::python
	import os
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings' 
	# myapp 改成你的 app 名稱

嘗試用看看 `epydoc` 來 parse python 的程式，出來的 html
文件還算不錯囉，不過不知道還有沒有什麼其他比較好的文件產生工具就是了。

參考網址：  

<http://eliasbland.wordpress.com/2010/01/25/importerror-settings-cannot-be-imported-because-environment-variable-django_settings_module-is-undefined/>

  [epydoc]: http://epydoc.sourceforge.net/index.html
  [欄位官方範例]: http://epydoc.sourceforge.net/fields.html#fields
  [這邊]: http://epydoc.sourceforge.net/using.html
