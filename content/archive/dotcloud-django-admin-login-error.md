Title: DotCloud Django admin login error
Date: 2011-11-27 16:53
Author: carlcarl
Post_ID: 135
Category: python
Tags: django, Dotcloud, python
Slug: dotcloud-django-admin-login-error

在建置好 admin 相關的設定和 static file 路徑後，終於進到輸入 admin
帳密的畫面了，但是按鈕連結卻是錯誤的，看了一下 source code
的部份，「app_path」這個變數似乎有問題。

找了好久都找不到解決的辦法，後來看到一篇文章發現似乎是 DotCloud
本身的問題。  
[http://stackoverflow.com/questions/7057111 ][]  
如果真的想試試看的話，可以 ssh 到你的 app.www，然後使用 vim：

	:::bash
	vim env/lib/python2.6/site-packages/django/contrib/admin/templates/admin/login.html


將 `{{ app_path }}` 改為 `/admin/`，但是這樣作其實只是治標，因為每次
push 都會重新覆蓋掉，只能等之後看會不會修正了。或者是可以考慮寫個 python
script，然後加入到 `postinstall` 這個檔案，每次 push
完就去修改這個檔案之類的，不過我個人是懶得這樣用就是了orz。

  [http://stackoverflow.com/questions/7057111 ]: http://stackoverflow.com/questions/7057111
