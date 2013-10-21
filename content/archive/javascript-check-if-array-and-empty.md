Title: Javascript check if array and empty
Date: 2012-05-09 04:24
Author: carlcarl
Post_ID: 438
Category: js
Tags: array, empty, javascript
Slug: javascript-check-if-array-and-empty

列出一些我覺得比較 OK 的方法，至於其他還有一些方法可以參考最下方的網址。  
判斷是否為 array 的方式：

	:::javascript
	var xxx = [];

	// 第1種：先用 if 判斷瀏覽器是否支援此method 然後再執行
	if (Array.isArray)
    	return Array.isArray(v);

	// 第2種
	Object.prototype.toString.call(xxx) === '[object Array]'

	// 第3種
	3. xxx instanceof Array


判斷 array 是否為 empty的方式：

	:::javascript
	var xxx = [];
	if(xxx.length == 0)
	{
    	alert("Array is empty");
	}


另外如果還要判斷在 array 裡的某個 key 是否存在的話：

	:::javascript
	xxx['key'] != undefined


  參考網址：

<http://stackoverflow.com/questions/4775722/>
<http://stackoverflow.com/questions/2672380/>
<http://stackoverflow.com/questions/1098040/>
