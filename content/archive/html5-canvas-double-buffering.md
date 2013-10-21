Title: html5 canvas double buffering
Date: 2013-06-16 19:25
Author: carlcarl
Post_ID: 1023
Category: js
Tags: canvas, html5
Slug: html5-canvas-double-buffering

因為之前寫 java 的經驗，讓我以為在 html5 的 canvas 上也要自己實作 double
buffering，但是在我後來實作後發現，好像哪裡怪怪的，因為其實原本就沒有在閃的感覺了，所以加了
double buffering 好像也沒啥差，重點是 performance 下降很多......。

<!--more-->

後來花了一些時間找資料，我得到的結論－是大部分的情況，不需要自己做
double buffering，因為瀏覽器會很聰明的幫你做。但是它怎麼判斷什麼時候該把
buffer 的部分 render 上去呢？以下是我的鍵盤猜測：

因為現在大多數的螢幕更新頻率都是 60Hz，也就是說大概每 16 ms
就會刷新一次螢幕，而瀏覽器本身在刷新的頻率可能也會接近這個時間，但是有沒有比較高就不知道了，因為你所看到的可能會被你螢幕的更新頻率所限制，就算瀏覽器刷新頻率是
1000Hz，反正一般的銀幕也看不出來:P。

以一個簡單的例子來實驗，假如我在一開始把一個方形塗上顏色然後 clear
掉，等一段時間後再塗上顏色，間隔如果設 10ms
的話，在我的螢幕上就看不到被清空的那段畫面；又假如我設成
20ms，就會看到被刷空白的那段畫面，也就是俗稱的「畫面在閃」，我在這邊實驗的結果是
12ms 就會有閃的感覺，也許是因為程式執行的
delay。然後瀏覽器應該也不會傻傻的即使你什麼都不做也一直重複 render
上去，而是在上次 render
後這段時間，假如有做一些畫面上的操作，才會把畫面再 render
上去，這樣感覺比較合理。

也就是說，如果你的圖形可以在 1x ms 畫完的話，就不需要做 double
buffering；但是如果你的圖形很複雜，你畫這個圖形需要 100ms，又是直接畫在
canvas
上，那可能就會出現半完成的圖形（我說可能的原因是不知道瀏覽器會不會自己做
optimization，等到一個 function 裡的事情都做完再一起
render，因為我之前的實驗使用 `setTimeout` 來做，有可能不符合 browser
optimize 的策略？），在這種情況下就有可能會考慮做 double buffering
。另外還有一種情況就是像 [這篇][] 所提到的，可以省略掉每次都要重新
render 複雜圖形的步驟，效能上會好很多。

如果真的要做 double buffering 的話，
有些簡單的方法，我之前用的方法是用另外生一個 canvas，在上面畫完之後再用
drawImage 把 buffering canvas 畫到 display 用的 canvas
就好了，或是這邊還有 [一個簡單的方法][] 可以參考看看。


參考資料:  
[Do we need to implement double buffering ourselves with \<canvas\>?](http://stackoverflow.com/questions/11777483/do-we-need-to-implement-double-buffering-ourselves-with-canvas)  
[Re: [whatwg] Canvas size and double buffering.](http://www.mail-archive.com/whatwg@lists.whatwg.org/msg19969.html)  

  [這篇]: http://www.html5rocks.com/en/tutorials/canvas/performance/
  [一個簡單的方法]: http://stackoverflow.com/questions/2795269/does-html5-canvas-support-double-buffering
  