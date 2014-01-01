Title: Python: can't use a string pattern on a bytes-like object
Date: 2013-05-23 16:25
Author: carlcarl
Post_ID: 852
Category: python
Tags: encode, httplib, json, python, python2, python3
Slug: python-cant-use-a-string-pattern-on-a-bytes-like-object

最近嘗試將 Python2 的程式轉成
Python3，看起來好像很順利，不過在執行的時候就出現了 Excepion
囧，內容就是
`can't use a string pattern on a bytes-like object`，看了一下，是 `json`
的 `loads` 在轉`httplib` `read` 的 output 出現問題，而原來在 Python2
中並不會出現這個問題，原來程式如下：  

	:::python
	result = json.loads(self._connect.getresponse().read())


後來查了一下資料才發現，這邊的 `read`，似乎讀出的資料是 `byte` 的
type，還需要做 encode 才行，所以後來加上 encode utf-8 之後，在 Python2
和 Python3 測試就都 OK 了：

	:::python
	json.loads(self._connect.getresponse().read().decode('utf-8'))


參考網址：  

<http://stackoverflow.com/questions/10846112/use-byte-like-object-from-urlopen-read-with-json>
