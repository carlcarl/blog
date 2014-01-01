Title: Django template check if in debug mode
Date: 2013-12-22 21:30
Author: carlcarl
Post_ID: 1382
Category: python
Tags: django
Slug: django_template_check_if_in_debug_mode


找了一下在 template 中確認是否在 debug mode 底下的方法，找了很多，不過好像都有點繞圈子，後來發現其實 Django 內建還是有[簡單的方法]。

在 `settings.py` 裡，先確認 `debug` 是 `True`，然後再加上：

	:::python
	INTERNAL_IPS = (
		'127.0.0.1',
		'localhost',
	)

之後在 template 裡就可以這樣用:

	:::jinja2
	{% if debug %}
	<span>This is debug</span>
	{% else %}
	<span>This is production</span>
	{% endif %}

如果到 production 的話，就將 `debug` 設為 `False`。

參考資料：  
[Template Query Debug]  
[Subclassing Context: RequestContext]  
[Django: Using Different Templates for Production]  

[簡單的方法]: http://www.djangobook.com/en/2.0/chapter09.html
[Template Query Debug]: https://djangosnippets.org/snippets/93/
[Subclassing Context: RequestContext]: https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext
[Django: Using Different Templates for Production]: http://stackoverflow.com/questions/4247717/django-using-different-templates-for-production/
