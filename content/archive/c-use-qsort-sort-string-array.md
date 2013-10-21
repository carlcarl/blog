Title: C use qsort sort string array
Date: 2011-03-27 19:58
Author: carlcarl
Post_ID: 14
Category: C &amp; C++
Slug: c-use-qsort-sort-string-array

指標真的好難 寫了那麼久還是不太懂

想用qsort sort 字串 array 結果compare函式怎麼用都會錯囧

後來上網查了一下資料 才知道用錯了orz

以下是compare函式範例

	:::c
	int compare(void* a, void* b)
	{
		return(strcmp(*(char**)a, *(char**)b);
	}

像以下這種就可以用上面的compare函式來處理  

	:::c
	array[0] = "123"  
	array[1] = "111222"

 

參考網址

<http://www.c.happycodings.com/Sorting_Searching/code15.html>
