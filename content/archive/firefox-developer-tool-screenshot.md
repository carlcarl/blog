Title: firefox developer tool screenshot
Date: 2013-06-27 19:00
Author: carlcarl
Post_ID: 1095
Category: 未分類
Tags: firefox
Slug: firefox-developer-tool-screenshot

雖然也可以用另外的軟體截圖，不過有時候截的大小不是很準確
orz。這邊我是要對某個 element 做截圖，而且大小要很精確，後來剛好看到
firefox 的 developer tool 也有這樣的功能，所以就試了一下。

<!--more-->

一開始按 `shift+F2` 就會出現一個輸入視窗。嗯，沒錯，它的 screenshot 是
CLI 的 XD。如果是要對某個 element 做截圖的話，例如是一個 id 叫做 target
的區塊，可以這樣下：

	:::text
    screenshot test.png --selector #target

這樣就會把 `#target` 這個部分存成一個圖片檔，名稱為 `test.png`。其他還有
`--delay`, `--clipboard`...等選項，只要輸入 `-`
就會出現選項的提示，詳細的可以直接從裡面看。

參考資料：  
[Take screenshots straight from Firefox’s Developer
Toolbar(裡面前面是舊版的 API，要注意)](http://www.ghacks.net/2012/11/02/take-screenshots-straight-from-firefoxs-developer-toolbar/)

