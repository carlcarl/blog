Title: Django name array
Date: 2012-05-09 17:38
Author: carlcarl
Post_ID: 444
Category: python
Tags: django, python
Slug: django-name-array

在寫 php 的時候，如果想傳多個 checkbox 的值的話，常會在 html
裏面設定這些 checkbox 的 name 為
`list[]`，也就是會加個 `[]` 在名稱後面，在 php 處理的時候就可以利用
`$_POST['list']` 取出這個 array。

而如果是 django name array
要處理的話，方式有點不太一樣，它並不會自動去判斷 `[]`，所以在 django
這邊還是必須讀 `list[]` 這樣的名稱，這也表示在 html
裡，`[]` 是可以不加的，但是我還是建議加上就是了，至少這樣我覺得會比較好懂。  
<!--more-->  
來看一下簡單的範例：

html

	:::html
	<input type="checkbox" name="list[]" value="value 1">
	<input type="checkbox" name="list[]" value="value 2">
	<input type="checkbox" name="list[]" value="value 3">
	<input type="checkbox" name="list[]" value="value 4">
	<input type="checkbox" name="list[]" value="value 5">


django

	:::python
	list = request.POST.getlist('list[]')
	# 用 request.POST['list[]'] 會讀不到

	# 拿到之後可以用 for loop 來抓裏面的值
	for element in list:
    	# do something
    	

這樣就可以拿到 list 這個 array，並做更進一步處理了。

參考網址：  
<http://stackoverflow.com/questions/4997252/>  
<http://stackoverflow.com/questions/801354/>
