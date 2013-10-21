Title: Javascript parseInt and Number
Date: 2013-08-07 15:31
Author: carlcarl
Post_ID: 1262
Category: js
Tags: Number, parseInt
Slug: javascript-parseint-and-number

這個是查資料時看到的 benchmark [performance of parseInt()][]

簡單歸納幾點：

1.  `parseInt` 基本上幾乎是比 `Number`
    還要快的，兩者雖然用法有點不同，不過純粹做轉換的話，`parseInt`
    會比較快。
2.  `parseInt('4')` 跟 `parseInt('4', 10)`
    在不同瀏覽器的效能也不一樣。不過直覺來看，感覺應該是 `parseInt('4')`
    會比較快說，因為不需要驗證參數。就個人來說，還是直接 `parseInt('4')`
    就好。
3.  new 會帶來多的 overhead，所以 new Number 又比 Number 慢。

  [performance of parseInt()]: http://jsperf.com/performance-of-parseint
