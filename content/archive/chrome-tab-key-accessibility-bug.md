Title: Chrome tab key accessibility bug
Date: 2013-08-22 00:58
Author: carlcarl
Post_ID: 1277
Category: web
Tags: chrome, g0v, css
Slug: chrome-tab-key-accessibility-bug

簡單說就是在 link 內容如果是 float 的情況下，這個 link 沒辦法在按 tab
鍵的時候得到 focus。Google 了一下，好像是 [Webkit 的
bug][]，不過好像沒有打算要修的樣子(汗)。  
Link 如果在下面的情況是 OK 的：

	:::html
    <a href="#">
        <div>test</div>
    </a>

但是如果加了 `float` 後就會出問題：

	:::html
    <a href="#">
        <div style="float:left;">test</div>
    </a>

我的解決方法很簡單，就是乾脆把 `float` 移到外面的 element
上(炸)。目前看來是沒問題，Firefox 下測試也 OK，所以應該就先這樣~。

參考資料：  
[Webkit removes links containing only floated elements from the tab
order][]

  [Webkit 的 bug]: https://bugs.webkit.org/show_bug.cgi?id=51333
  [Webkit removes links containing only floated elements from the tab
  order]: http://www.heresonesolution.com/2010/12/google-chrome-float-tab-order/
