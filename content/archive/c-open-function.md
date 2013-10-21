Title: C open function
Date: 2011-03-21 17:31
Author: carlcarl
Post_ID: 12
Category: C &amp; C++
Slug: c-open-function

最近好久沒有用 C 寫程式了，一直狂卡QQ

晚上在用 `open` 函式開檔案,
結果後來看發現權限都沒有設，後來查了一下才發現原來後面要加權限的設定，這裡來講就是 `0666` 這串數字：

	:::c
	open(filename, O_RDWR|O_CREAT, 0666)


這數字可以設定使用者、群組、其他人的寫讀執行權限。如果只是開個一般的檔可以無腦一點，`0666` 就行了~，至於第二個參數
 `O_RDWR` 代表在程式中可讀寫，也可以用 `O_WRONLY` 或 `O_RDONLY` 代表只寫或只讀，`O_CREATE` 則代表建立這個檔案。

參考網址：

<http://stackoverflow.com/questions/2245193/c-linux-file-permission-problem-with-open>
