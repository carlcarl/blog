Title: jQuery Data Attribute
Date: 2015-05-28 00:00
Author: carlcarl
Post_ID: 1418
Category: js
Tags: jquery
Slug: jquery_data_attribute



最近開始用 `data-*` 的 attribute，後來看到 jQuery 也有 `.data()` 的 method 可以用，`data()` 可以存不只 `String` type 的資料，也可以存 `Number` or `Boolean` 之類的，不過用了之後才發現不是那麼好用，因為假如我把 data attribute 寫在 html 裡的話，ex: 

	:::html
	<div data-value="123"></div>

我用 `data('value')` 取出來的值會是 `Number` type，也就是說，如果能轉的話，它就會自動幫你轉，在很多情況下，這不會是想要的行為，而且一旦不小心，就會造成不同型態比較的錯誤，所以就我自己來說，還是使用 `attr('data-value')` 的方式，可以保證一定是拿到字串，但是 `data()` 還是有它的好處，就是它的內部實作有做 cache，所以讀取上會快些，因為不用 access 到 DOM。


Ref:

* [jQuery.data() with HTML5 Custom Data Attributes]
* [Example]
* [jQuery data() vs attr(data)]


[jQuery.data() with HTML5 Custom Data Attributes]: http://www.sitepoint.com/jquery-data-html5-custom-data-attributes/ 
[Example]: http://jsfiddle.net/KwjvA/
[jQuery data() vs attr(data)]: http://stackoverflow.com/questions/9444679/jquery-data-vs-attrdata

