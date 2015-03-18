Title: Semantic UI dropdown restore default
Date: 2015-03-18 19:30
Author: carlcarl
Post_ID: 1416
Category: web
Tags: semantic
Slug: semantic_ui_dropdown_restore_default


鬼打牆了很久，後來才找到一個方法可以做。

	:::js
	// dropdown init:
	$('.ui.dropdown').dropdown();
	
	
	// 假如某個 dropdown 的 id 是 a
	$('.ui.dropdown').has('#a').dropdown('restore defaults');


我有試圖用某個特定 id 做 dropdown init，再用這個 element 做 restore default，不過居然還是會有錯誤...。總之目前用這樣解。總覺得對 semantic UI 的怨念原來越深了...。

Ref:

* [https://github.com/Semantic-Org/Semantic-UI/issues/1717]

[https://github.com/Semantic-Org/Semantic-UI/issues/1717]: https://github.com/Semantic-Org/Semantic-UI/issues/1717


