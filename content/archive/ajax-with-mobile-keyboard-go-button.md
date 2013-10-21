Title: ajax with mobile keyboard go button
Date: 2013-04-07 22:58
Author: carlcarl
Post_ID: 813
Category: js
Tags: ajax, mobile
Slug: ajax-with-mobile-keyboard-go-button

最近弄 ajax 在手機上測的時候發現按 keyboard 上的 go 按鈕不會自動
submit，所以看了一下是怎麼回事。找了一些資料加上自己測試了一下，發現原來
go 按鈕跟 enter 是一樣的 event。

我最後決定的做法是將原本 ajax 要 submit 的 部分先用 form tag
包起來，ajax 的按鈕則改成 `<button type="submit"></button>`，`type` 用
`submit` 可以使得在按 enter 或是 手機上按 go 的時候能 trigger submit 的
event，這邊用 `<input>` 也是可以，不過因為我有用一些 icon 在按鈕中，用
button tag 相對比較好做。再來就是註冊 form tag 的 event，用 jQuery
來說就是 `$('#myform').submit(myfunction);`，接著在 `myfunction`
中記得最後要 `return false;`，以避免真的 submit 頁面上去。

參考網址：  
<http://stackoverflow.com/questions/1960240/jquery-ajax-submit-form>
