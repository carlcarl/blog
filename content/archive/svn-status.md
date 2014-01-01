Title: svn status appear「~」
Date: 2012-02-14 23:46
Author: carlcarl
Post_ID: 249
Category: version-control
Tags: svn
Slug: svn-status

最近遇到有人有這個問題，查了一下，這個問題的原因是因為從「一般檔案, 資料夾, 連結」這三種屬性，該檔案從其中一個屬性換成另外一種屬性就會出現這個波浪號狀態。

不過當然有時候事情不是那麼簡單......，這次遇到的主要原因應該是因為資料夾內的
`.svn` 被刪掉了，所以從外面看就會出現這種情形，以下是查到的解決方法：

	:::bash
	mv test test2
	svn delete test
	mv test2 test
	svn add test

首先先改資料夾名稱，因為等下要刪掉原本這個資料夾的 svn 紀錄，直接 delete
的話，資料夾就真的會被刪掉，刪完之後再把改過名稱的資料夾改回原來的名稱，改完之後再重新
add，應該就會顯示正常了。
