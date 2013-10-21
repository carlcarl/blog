Title: HTML script speed up with defer
Date: 2012-07-06 03:49
Author: carlcarl
Post_ID: 525
Category: js
Tags: javascript
Slug: html-script-speed-up-with-defer

在 [script tag 屬性 async defer 差別][] 這邊看到了 script tag 有 async
和 defer 的用法，所以就來試試看。大致測試了一下，速度的確有快了一些(大概加快50 ~ 100ms
左右吧XD)。以下大概講一下我的測試範例內容：

<!--more-->

	:::html
	<!-- 
	這是原本的程式
	a-b.js 需要 a.js, 而 a-c.js 需要 a.js, 這是這 3 個 js 檔的相依關係
	最後會從 a-c.js 裡呼叫 library 來執行
	由於 async 屬性並不適合用來處理有相依性的 js 檔案，load 順序可能會出問題
	defer 則能保證執行的順序關係，所以我等下會是使用 defer 屬性
	如果你的 js 檔案並沒有相依關係的話，是可以考慮用 async 屬性
	-->
	<script type="text/javascript" src="js/a.js"></script>
	<script type="text/javascript" src="js/a-b.js"></script>
	<script type="text/javascript" src="js/a-c.js"></script>
	<script type="text/javascript">
    	c.lib();
	</script>


加上 defer 屬性後：

	:::html
	<script defer type="text/javascript" src="js/a.js"></script>
	<script defer type="text/javascript" src="js/a-b.js"></script>
	<script defer type="text/javascript" src="js/a-c.js"></script>
	<script defer type="text/javascript">
    window.onload = function(){c.lib();};
	</script>

  [script tag 屬性 async defer 差別]: http://blog.xuite.net/vexed/tech/61308318
