Title: c edit code but Make only show up to date
Date: 2011-07-13 07:12
Author: carlcarl
Post_ID: 33
Category: C &amp; C++
Slug: c-edit-code-but-make-only-show-up-to-date

感覺好像是很初學的問題，不過我還是不知道原來這個會有關係 orz

<span style="color: #ff0000;">在 Makefile 裡記得要加dependency file</span>

例如檔案是 test.cpp, test.h, test2.cpp, test2.h 要編譯成一個執行檔

	:::makefile
	test:
		g++ -o test test.o test2.o
	test.o:
		g++ -c test.cpp
	test2.o:
		g++ -c test2.cpp

 要改成

	:::makefile
	test: test.o test2.o
		g++ -o test test.o test2.o
	test.o: test.h test.cpp
		g++ -c test.cpp
	test2.o: test2.h test2.cpp
		g++ -c test2.cpp


這樣就ok了~

 

當下了 `make test`，他會去檢查 dependency
file，也就是 test.o 和 test2.o，然後 test.o 和 test2.o 會各自去檢查dependency
file，也就是各自的 cpp 和 h 檔。假如發現 test.cpp 有更改後，test.o 就會重新編譯一次。以此類推，如果改了 test2.h 的話，就變成 test2.o 會重新編譯，當返回test這邊時，發現 test.o 和 test2.o 有變動過，就會重新將兩個 object 檔 link 起來，

所以如果沒加上 dependency
file的話，make的時候就不知道要去檢查哪個檔案是否有更新這樣。

 

參考網頁

<http://ubuntuforums.org/showthread.php?t=1189999>
