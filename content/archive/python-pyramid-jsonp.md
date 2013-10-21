Title: Python Pyramid jsonp
Date: 2013-04-09 13:35
Author: carlcarl
Post_ID: 819
Category: python
Tags: jsonp, pyramid
Slug: python-pyramid-jsonp

Python 的 Pyramid Framework 有支援 jsonp 的 renderer，看了一下
doc，設置還算簡單，不過好像漏了個小地方。  
<!--more-->  
首先要先在 `Configurator` 的檔案加入下面內容 (官方 doc 裡面沒提到要從哪邊
 `import JSONP`)：

	:::python
	from pyramid.renderers import JSONP
	# 這裡使用 'callback' 當作預設的 callback function 名稱
	config.add_renderer('jsonp', JSONP(param_name='callback'))


然後在 view 裡面將 `renderer` 改用 `jsonp`，這邊你還是可以加上 `route_name`
等參數：

	:::python
	@view_config(renderer='jsonp')
	

這樣就完成了～～。

參考網址：  

<http://docs.pylonsproject.org/projects/pyramid/en/latest/api/renderers.html>  
<http://irclogs.rulim.de/%23pyramid/%23pyramid.2012-06-15.log.html>
