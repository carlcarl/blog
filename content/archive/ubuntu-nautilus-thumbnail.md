Title: Ubuntu nautilus video thumbnail
Date: 2011-11-03 18:31
Author: carlcarl
Post_ID: 49
Category: linux
Tags: nautilus, thumbnail, ubuntu
Slug: ubuntu-nautilus-thumbnail

最近發現有些影片的預覽圖一直沒辦法看到，想說會不會是播放器的問題，可是搞了老半天卻還是不行。在查了一些資料之後才發現，這個原因好像是因為在之前偵測某幾個影片預覽圖的時候可能失敗還是怎樣，然後這幾個影片就從此不會再作擷取預覽圖的動作，以下是解決方法：

	:::bash
	rm -r ~/.thumbnails/fail/


刪完之後再重新整理就 OK 哩～。

 

參考網址：

<http://www.ubuntu-tw.org/modules/newbb/viewtopic.php?viewmode=compact&topic_id=9430&forum=4>
