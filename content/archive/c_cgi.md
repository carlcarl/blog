Title: C CGI Resources
Date: 2015-04-07 14:00
Author: carlcarl
Post_ID: 1419
Category: c
Tags: cgi
Slug: c_cgi_resources


CGI 的 C 範例，大部分都是很簡單的，找不太到比較完整的資料，只找到 C++ 的，不過還是可以參考看看：[http://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm]，裡頭有介紹到如何拿 GET, POST 的資料，還有一些常見的 header 欄位。

另外找了一下，怎麼切 cookie 裡的字串比較好，不過也是沒找到比較正統的做法，只看到這種做法：[http://www.gnu-darwin.orgwww.gnu-darwin.org/www001/src/ports/security/zxid/work/zxid-0.22/zxidcdc.c]，直接用 `strstr` 找到想要的欄位這樣。



[http://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm]: http://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm
[http://www.gnu-darwin.orgwww.gnu-darwin.org/www001/src/ports/security/zxid/work/zxid-0.22/zxidcdc.c]: http://www.gnu-darwin.orgwww.gnu-darwin.org/www001/src/ports/security/zxid/work/zxid-0.22/zxidcdc.c






