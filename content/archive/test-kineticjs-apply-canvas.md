Title: Test KineticJS apply canvas
Date: 2012-09-04 01:54
Author: carlcarl
Post_ID: 606
Category: js
Tags: canvas, kineticjs
Slug: test-kineticjs-apply-canvas

寫起來跟以前寫 Java 作類似東西的感覺很像，東西基本上都已經用物件包好，然後還有提供 layer
讓你可以很方便的在不同 layer 放你要的物件。  

我嘗試把我原本[播放棋譜][]的 canvas 改成套用 KineticJS，不過後來發現，因為我的 canvas
操作沒很複雜，所以真的是太大材小用了...。

以可讀性來講，因為我大部分畫 canvas 都是放在一個 function 裡，大致用幾個註解分幾個段落，其實就知道各部份的流程，換成物件的方式後，整個 function 感覺並沒有更好讀，而且程式沒有比較短=.=。

然後我用一個固定的測試流程來作測試(這個流程不包括前面的 js file loading，是讀完後才開始作操作測試)，測試的結果原本是 200ms，換成 KineticJS 之後是 800ms，整個很不划算 ~.~。

雖然 KineticJS 有提供 layer，不過如果只是簡單操作的話，這個我自己幹也是
OK，就動態新增幾個 canvas，設 z-index 就有類似一樣的效果，我自己現在是設定棋盤一個 background layer，棋子和其他一些標示設到 front layer。

然後只 render 「改變的部份」這塊，KineticJS 需要紀錄在 layer
中的每個物件，不然在移除棋子的時候，沒辦法知道是要 remove
layer中的哪個棋子，但是這樣就變成需要多一個資料結構來紀錄，個人覺得不太划算。

原本的 canvas 我要作的話，像是移除某個棋子，我只要把 background layer
的那部份拿來蓋掉棋子就可以了，相較之下會比較方便些，後來實作這部份之後，時間也從
200ms，降到 130ms 左右。之前測從一個 layer 切成兩個 layer 後，時間似乎沒啥差囧。

不過使用者點擊的這部份 目前還是 render 全部，因為假如我按上一步的話，現在這一步的棋盤會移除掉，當我要畫上一步的棋盤時就沒辦法根據差異來只畫改變的部份，我現在是存棋盤上一個狀態是在哪一步，當然如果要改成存上一個狀態的整個棋盤就能解決，但是我怕 overhead 會太大。

所以結論是 我覺得如果會需要用到一些 mouse event(ex: drag) 或是
animation...等一些比較複雜的操作的話，這時候再考慮用 KineticJS
吧，不然只有一些簡單的操作的話用 canvas 就好。另外 KineticJS 在設定一些
shape 的 attr，會發現比 canvas 的還少一點，因為有些都在程式裡寫死了，這個可能要注意一下。

  [播放棋譜]: https://github.com/carlcarl/CaGo/blob/master/js/cago.js
