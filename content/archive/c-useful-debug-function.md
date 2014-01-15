Title: C useful DEBUG function
Date: 2011-03-31 18:29
Author: carlcarl
Post_ID: 15
Category: C &amp; C++
Slug: c-useful-debug-function

學了那麼久才知道有這種好功能可以用 = ="

	:::c
	#define DBG(msg, arg...) printf("%s:%s(%d): " msg, 	__FILE__, __FUNCTION__, __LINE__, ##arg)


`FILE` 表示這行所在的程式檔案

`FUNCTION` 表示這個函式所在的函式(唸起來好繞口= =)
不過如果是用 gcc 來編譯的話 建議是用 `func`, 我之前用 gcc
編譯前者好像不會過......

`LINE` 代表這函式是在哪一行

其實也只是把 `printf` 有印出一些資訊的版本 define 為一個函式這樣![][]

(不過要我寫我還真不會= =||)

 

而在實際上運用可以這樣:

	:::c
	if(i != 2)
		DBG("%dn", index);


這樣如果 i 不等於 2 的話 就會在前面先印出那些資訊 然後才會印出 index 的值

雖然在一般的小程式內可能用處不大 因為很快就能夠找到錯誤

不過如果是好幾十個檔案的程式發生錯誤且在程式內有用這功能來作處理的話
就能很快找到錯誤囉~~

 

參考網址

<http://cgi.blog.roodo.com/trackback/11456265>

