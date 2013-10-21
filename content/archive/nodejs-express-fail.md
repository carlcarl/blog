Title: nodejs express fail
Date: 2011-09-07 12:09
Author: carlcarl
Post_ID: 45
Category: js, node.js
Tags: express, node.js
Slug: nodejs-express-fail

[![1315397444-1533326740][]][1315397444-1533326740]

之前好不容易決定要用 express 這個 framework，可是安裝完執行 project 後卻出現錯誤，拜了 google 大神之後才發現，好像是他不會去找裝在系統中的 express library。事實上，如果有用 npm 裝其他的 module，應該也有可能會出現一樣的錯誤：找不到 module 啊～～。

後來在[stackoverflow也看到有人有同樣的問題][]，雖然原 PO 已經選了其中一個回答當作答案，不過顯然那個答案的作法：每次安裝就要複製 library 實在是不怎麼簡潔。後來在文章下面的回答中有看到一個更好的作法：

	:::bash
	npm link express


問題就輕鬆的解決掉了。

如果之後裝了其他 module，在使用的時候也出現找不到 module 的錯誤，用 `npm link module名稱` 就能解決了。

  [1315397444-1533326740]: http://i.imgur.com/itGPLvWl.png
  [stackoverflow也看到有人有同樣的問題]: http://stackoverflow.com/questions/5919629/express-module-not-found-when-installed-with-npm#_=_
