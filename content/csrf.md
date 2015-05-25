Title: CSRF 資料
Date: 2015-05-25 17:40
Author: carlcarl
Post_ID: 1430
Category: web
Tags: 
Slug: csrf



預防 Cross-Site Request Forgery (CSRF) 的一些資料，以下兩個連結講了蠻多的:

* [Why is it common to put CSRF prevention tokens in cookies?]
* [Cross-Site Request Forgery (CSRF) Prevention Cheat Sheet]

其中看到比較特別的是 Double Submit Cookies。將 CSRF token 放到 POST 和 cookie 欄位中，接著 server 只要比對兩者一樣不一樣就可以了，還滿有趣的。


[Why is it common to put CSRF prevention tokens in cookies?]: https://stackoverflow.com/questions/20504846/why-is-it-common-to-put-csrf-prevention-tokens-in-cookies
[Cross-Site Request Forgery (CSRF) Prevention Cheat Sheet]: https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)_Prevention_Cheat_Sheet#Double_Submit_Cookies
