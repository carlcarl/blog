Title: C how to know the file size
Date: 2011-03-27 09:27
Author: carlcarl
Post_ID: 13
Category: C &amp; C++
Slug: c-how-to-know-the-file-size

兩種方法~

1.利用 `fseek`(或 `lseek`)

	:::c
	FILE* f = fopen(fileName, "r+");
	fseek(f, 0, SEEK_END);
	size = ftell(f);
	fseek(f, 0, SEEK_SET);


2.用 `stat` 函式

	:::c
	struct stat st;
	stat(fileName, &st);
	size = st.st_size;
 

參考網址:

<http://stackoverflow.com/questions/238603/how-can-i-get-a-files-size-in-c>

 
