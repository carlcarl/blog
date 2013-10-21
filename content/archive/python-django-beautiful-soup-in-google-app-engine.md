Title: Python Django Beautiful Soup in Google app engine
Date: 2011-03-19 19:27
Author: carlcarl
Post_ID: 8
Category: python
Slug: python-django-beautiful-soup-in-google-app-engine

之前用原生的 HTMLParser 用到很囧，感覺功能還是不夠強大

後來看到了 `BeautifulSoup` 這個 plugin 就想說用用看，使用很方便，只要把裏面的 BeautifulSoup 複製一份到自己的目錄下，然後 import 進來就好了:

	:::python
	import BeautifulSoup


在 Google app engine 裡，我是搭配urlfetch來使用，如以下的片段範例:

	:::python
	from google.appengine.api import urlfetch
	from BeautifulSoup import BeautifulSoup
	url = 'the url address you want'
	result = urlfetch.fetch(url) # 抓網頁
	if result.status_code == 200:
		book = result.content  # book 會得到html的內容
		soup = BeautifulSoup(book, fromEncoding="utf-8") # 建立一個BeautifulSoup的物件
		book = soup.findAll('div',{'id':'content'})


結果會抓出包含 `div id=content` 的內容, `findAll` 會回傳一個 list，所以在 Django 的 template 裡需要用 for loop 來把 book 的內容印出來，如果要利用 `str(book)` 轉成字串, 需要注意頭尾的 `[` 和 `]`，以及中間用來分開裏面元素的 `,`。
