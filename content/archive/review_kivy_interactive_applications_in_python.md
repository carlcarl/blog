Title: [review] kivy interactive applications in python
Date: 2013-12-08 17:00
Author: carlcarl
Post_ID: 1381
Category: python
Tags: kivy
Slug: review_kivy_interactive_applications_in_python


![kivy interactive applications in python](http://i.imgur.com/87z6yUy.png)

其實很久沒看有關 GUI library 相關的書了，會看這本是因為之前其實就有聽說過 [kivy] 這個 python library，但是一直沒機會摸摸看。前一陣子剛好 [packt] 在找人 review 一些電子書，所以就想說可以試試看。是說 packt 最近感覺還滿活躍的，常在一些網站徵求可以幫忙 review 的人，譬如說我現在就有在看另外一本 zsh 的書，幫忙訂正草稿和給一些意見，事後除了可以得到原來的電子書，也可以另外在網站上選一本自己想要的電子書，還蠻不錯的~~。

從 kivy 的官網可以看到它的一些特色，像 cross platform，license 也是很 free 的 MIT，其他還有像常被拿來講的 multi-touch 之類的 feature。在書中可以看到 kivy 還有一個比較特別的地方就是它有一個 kivy language，其實有種 css 的感覺，主要就是負責整個 GUI 的 view 該怎麼呈現，而且也有各種不同的 layout 可以套用，不過大致上我覺得是有利有弊吧，把 view 切出來，在程式的處理上可能是會比較乾淨，不過這樣也要再花時間另外學一種語言，如果可以的話，我是滿希望可以直接套用 css 語法，這樣學習曲線比較沒那麼陡 XD。

整本書分成幾個部分，一開始就直接講該如何建立一個 GUI app，然後講解 kivy language 的寫法和一些排版該怎麼實作，是說沒講說 kivy 該怎麼安裝，讓我一開始不知道哪種安裝方法比較好，譬如說我可以用 [pip]，可以從官網下載 kivy 的安裝程式，也可以用 [homebrew] 安裝，後來有查一下資料和實際試過幾個方法發現 pip 安裝有點問題，homebrew 安裝會有點不穩，所以就用官方網站上的了。不過我覺得少點篇幅介紹怎麼安裝是件好事就是XD。

接下來幾章則是介紹 canvas 的用法，widget 的 event 該怎麼建立，因為之前有摸過 Java，感覺在使用上算是相差不大，如果有用過其他一些 GUI library 的話，應該不會覺得很陌生，其他接著是一些比較進階的應用，也有講到 multi-touch 的實作。最後一章則是直接實作一個類似小蜜蜂的射擊遊戲。這部分就會包含一些 animation 該怎麼實現，子彈射擊的音效和軌跡該怎麼做之類的。

![Invaders Revenge](http://i.imgur.com/YCH8DwW.png)

整個部分其實章節內容不多，書中有很大的比例都是程式碼，作者會根據這些程式碼分段講解對應的功能，也會有如上圖的截圖解說，不過並不會讓人覺得像是在衝頁數就是(譬如說國內的一些教學工具書)，如果有在用 kivy 的話，這本書是蠻適合參考看看的，因為程式碼很多，就算看不懂解說，也可以從程式大致了解實際上要怎麼用，所以還滿不錯的 XD。


[kivy]: http://kivy.org
[packt]: http://www.packtpub.com
[pip]: https://pypi.python.org/pypi/pip
[homebrew]: http://brew.sh
