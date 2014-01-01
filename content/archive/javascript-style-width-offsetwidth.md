Title: javascript style.width offsetWidth
Date: 2013-06-28 20:29
Author: carlcarl
Post_ID: 1107
Category: web
Tags: js, css, offsetWidth
Slug: javascript-style-width-offsetwidth

查了一些資料，看起來 `style.width` 是如果 css 沒指定 element 的 width
的話，就會拿到空值，即使它本身的確佔有一個大小。這時候如果想拿到實際大小的話可以用
`offsetWidth`，另外要注意的是 `offsetWidth` 是
`readonly`，所以如果要設寬度，還是得從 `style.width` 著手。還有 [這篇][]
是 `style.width` 和 `offsetWidth` 的效能比較，看來 `offsetWidth`
效能好很多，看來以後抓寬度就直接抓這個值就好了@@。

參考資料：  
[原生js获取宽高与jquery获取宽高的方法的关系][]  
[offsetWidth和width有什么不同啊?][]  
[How to find the width of a div][]

  [這篇]: http://jsperf.com/style-width-vs-offsetwidth1/5
  [原生js获取宽高与jquery获取宽高的方法的关系]: http://zhuweiwu.com/?p=86
  [offsetWidth和width有什么不同啊?]: http://bbs.csdn.net/topics/80381570
  [How to find the width of a div]: http://stackoverflow.com/questions/4787527/how-to-find-the-width-of-a-div
