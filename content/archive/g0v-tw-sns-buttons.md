Title: g0v.tw sns buttons
Date: 2013-08-28 01:40
Author: carlcarl
Post_ID: 1292
Category: css
Tags: g0v
Slug: g0v-tw-sns-buttons

修了一下 render 的問題，以結果來看其實並沒有完全做好，還是會有 render
過程中偏移的問題
orz，不過也比原來的情況好多了(汗)，之後功力如果好一點再來深入研究吧 =
=+。

[commit diff][]  
主要修正幾個地方：

### fb button size

fb button 基本上最大就 60px 的樣子，原本設了
500px，導致一開始預留的空間過大，整個會往左邊撐開，render
完後又變一個小按鈕，所以整個看起來很囧，解決方法就是不去限制大小，反正按鈕最大也就那樣而已。

### sns buttons 放大

原本的方法是直接把 button 用 css 加上 `transform` + `scale`
放大，不過如果有多個 button 的話，這樣兩者之間的 margin
會很難去設定，因為 margin
是放大之前的距離，放大之後從螢幕上來看，距離會因為 button
的放大而縮小，後來想到乾脆把包 sns buttons 的 block
整個放大好了，雖然這樣幾個按鈕的大小會不一樣，不過還算是可以接受，間隔距離也比較可以掌握。

### sns buttons 底線對齊

有想過用 translate 手動對齊底線，不過想想這樣太智障了。後來則是用
`table-cell` + `inline-block` + `vertical-align: bottom`
來做對齊。這邊後來也把 `width` 和 `height` 拿掉，`width`
設定會因為放大的關係，導致 button
會出現在左邊，所以乾脆就不設定，讓內容的部分自己把 block
撐開就好，`height` 則是會放大到超過
banner，而這邊其實也不需要特別去設定高度，所以就跟著拿掉了。

參考資料：  
[Tweet, Like, Google +1 and Share][]  
[How to vertically align floating divs to the bottom?][]

  [commit diff]: https://github.com/g0v/g0v.tw/commit/93777efbd4941f3ba74bb0380ffb65c4d4330f13
  [Tweet, Like, Google +1 and Share]: http://wordpress.org/plugins/only-tweet-like-share-and-google-1/
  [How to vertically align floating divs to the bottom?]: http://stackoverflow.com/questions/6116423/how-to-vertically-align-floating-divs-to-the-bottom
