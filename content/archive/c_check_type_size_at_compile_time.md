Title: Check Type Size at Compile Time in C
Date: 2015-01-30 17:00
Author: carlcarl
Post_ID: 1405
Category: c
Tags: c
Slug: c_check_type_size_at_compile_time

查資料的時候看到的，不過資料裡的方式，宣告 0 陣列還是會過，所以我乾脆多減一：

	:::c
	#define TYPE_SIZE ((sizeof(int) == 4) - 1)
	char arr[TYPE_SIZE];


完全不確定的話，也可以用 `>` or `<` 抓範圍 lol。

Ref:  
[Compile Time Assertions in C]

[Compile Time Assertions in C]: http://www.jaggersoft.com/pubs/CVu11_3.html

