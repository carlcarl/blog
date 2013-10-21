Title: Javascript MutationObserver
Date: 2013-07-03 18:46
Author: carlcarl
Post_ID: 1113
Category: js
Tags: MutationObserver
Slug: javascript-mutationobserver

最近看到 Aol Reader release，試用了一下，感覺還滿不錯的，但是右邊的廣告實在很礙眼，就算用
adblock 擋掉，右邊還是會留空，想說都沒寫過 browser 的 extension
，所以就拿這個來練功啦～，不然其實寫 userscript 也可以就是。要弄的
extension 以 Opera 和 Chrome 為主，因為兩個基本上架構可以共通，寫起來 CP
值比較高 XD。

<!--more-->

本來想說直接綁定 `window.onload` 在裡面做就好了，不過後來發現 Aol Reader
在 `onload` 之後還會有個它自己 loading
的頁面，處理起來就變麻煩很多，因為除了要觀察 dom 來判斷何時才算真的
ready 以外，另外就是 Opera extension guide 裡說限制不能用 setTimeout
之類的函式，本來我還想用暴力法，每秒檢查要處理的 element
讀好了沒，確定都好了才做，看來是行不通...。

後來大 CA 在噗浪上面說可以用 `MutationObserver`
做，找了一些資料看，好像真的是我要的東西 XD。MutationObserver
簡單說，它可以用來 monitor 某個 element 的變化並呼叫對應的
callback。後來我又發現 Aol Reader 在真正 ready 的情況下，會在 `body`
上加上 `ready` 這個 class，說起來還滿貼心的
XD。所以該有的條件都有了，接下來就是實作啦。下面是部分的實作內容：

	:::javascript
    MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
    observer = new MutationObserver(function (mutationRecord, observer) {
        mutationRecord.forEach(function (mutation) {
            if (body.classList.contains('ready')) {
                // do something here
                // ...

                // Done, remove this event.
                observer.disconnect();
            }
        });
    });
    observer.observe(body, {attributes: true, attributeFilter: ['class']});

這邊設定只關注 attribute 的變化，然後在 `classList` 裡如果有 `ready`
這個 class 的時候就做處理，className
因為要自己再另外切字串，會比較麻煩一點，所以這邊才改用
classList。在做完之後就用 `disconnect()` 把這個綁定的 event
給清除掉。比較要注意的是 `attributeFilter`，如果沒設定的話，會連其他
attribute 有變化的時候也呼叫 callback，這邊設定只對 `class`
有變化的情況下才呼叫 callback，效能上多少會有一點差。[這邊是 source code
的網址][]。

這邊只有大概講一下，其他 MutationObserver
的使用細節可以看下面的參考網址。

參考網址：  
[MutationObserver][]  
[Mutation 事件和 MutationObserver][]

  [這邊是 source code 的網址]: https://github.com/carlcarl/Aol-Reader-No-ads
  [MutationObserver]: https://developer.mozilla.org/zh-CN/docs/DOM/MutationObserver
  [Mutation 事件和 MutationObserver]: http://chrisyip.im/post/mutation-events-and-mutationobserver/
