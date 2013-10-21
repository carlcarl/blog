Title: doxygen show files with directory level
Date: 2011-09-30 18:15
Author: carlcarl
Post_ID: 46
Category: linux
Tags: doxygen
Slug: doxygen-show-files-with-directory-level

因為 project 的檔案太多，用 doxygen parse過後檔案還是多的要死，想說有沒有分資料夾階層顯示的方式。找了很久，後來找到一個折衷的方法，那就是在 config 檔中作以下設定。

	:::text
	SHOW_DIRECTORIES = YES


以下是顯示出來的樣子......。好吧，個人是覺得有點陽春，可以的話如果有收合的功能就更好了，只能希望之後的版本會有囉。

![doxygen_dir.png][]  

 

參考網址：

<http://stackoverflow.com/questions/6874800/directories-within-file-list-in-doxygen>

  [doxygen_dir.png]: http://i.imgur.com/WlsqsDB.png
    "doxygen_dir.png"
