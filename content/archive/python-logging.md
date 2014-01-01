Title: python logging
Date: 2013-01-28 15:08
Author: carlcarl
Post_ID: 759
Category: python
Tags: logging
Slug: python-logging

紀錄一下 python logging 的一些簡單設定。  

### 可以在一開始設定 log 訊息顯示的等級：
	:::python
	logging.basicConfig(level=logging.DEBUG)

### 設定顯示的訊息格式, ex: `ERROR: error message`

	:::python
	logging.basicConfig(format='%(levelname)s: %(message)s')

### log message 加上變數
	
	:::python
	logging.warning('The value is %s', value)
	
有人可能會想用另外一個較基本的方法：

	:::python
	logging.warning('The value is %s' % value)
	
但是這種方法，就會變成不管 log 不 log，都會執行組合字串的動作，所以並不建議，這邊可以參考 <a href="http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format">stackoverflow</a> 上的討論。


