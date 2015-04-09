Title: JSON-C Resources
Date: 2015-04-10 01:00
Author: carlcarl
Post_ID: 1420
Category: c
Tags: json
Slug: json_c_resources


找了一些 JSON-C 的使用範例:

* [JSON parser in C language - json-c]，簡單 JSON 的 maker 和 parser，不過沒有 array 的例子。
* [C 語言產生 json 檔]，有 array 的例子可以參考。
* [A simple and complete json parser]，包含很多例子，可是都會省略掉 free 的動作，要自己記得加。

不過最上面兩個都有一個同樣的問題，就是多做了幾次不必要的 free，最後的 `json_object_put` 其實只要對最上頭的 root 做一次就好，這個 function 會將其中有參照的 object 都做 free 掉的動作，相關問題可以參照以下連結:

* [Memory Leak Using JSON-C]
* [How to clean a json object created by “json_object_new_string”?]


[JSON parser in C language - json-c]: blog.yslin.tw/2012/06/json-parser-in-c-language-json-c.html
[C 語言產生 json 檔]: http://www.oknow.co/2014/06/c-json.html
[A simple and complete json parser]: https://linuxprograms.wordpress.com/category/json-c/
[Memory Leak Using JSON-C]: stackoverflow.com/questions/8746155/memory-leak-using-json-c
[How to clean a json object created by “json_object_new_string”?]: stackoverflow.com/questions/18382897/how-to-clean-a-json-object-created-by-json-object-new-string


