Title: [Review] Learning Python Design Pattern
Date: 2014-01-19 16:00
Author: carlcarl
Post_ID: 1385
Category: python
Tags: python
Slug: review_learning_python_design_pattern


![learning python design pattern](http://i.imgur.com/y1iu7cl.png)

其實之前就想看有關 design pattern 的書了，前一陣子剛好有這個機會看這本書，順便想看看在 Python 上要怎麼運用這些 pattern。

這本書頁數並沒有說很多，約 130 頁左右，看起來不會說很吃力。書中每一章都會對一至兩種 pattern 做解釋，然後說明優缺點，並附上一個不算偷懶的 example，還算好理解的就是，不過覺得有點可惜的是如果有加上沒有應用和應用後的一些實際比較就更好了。

而這本書本身應該會比較適合剛學 Python 一些時間的中 ~ 新手，例如第一章講 MVC 其實我自己就覺得不是很必要了，不過就適合不是很熟的人吧。接下來幾章則會講到 Singleton pattern，Factory Method, Facade pattern, Proxy pattern, Observer pattern, Command pattern 和 Template Method design pattern 這些。

而上述的這些 patterns，其中像是 Facade, Proxy, Command 和 Template Method 我都沒看過 XD。從這本書中所描述的來看，Facade pattern 簡單說就是封裝，把複雜的底層包起來提供一個 interface ；Proxy pattern 則是用來做中介管理，就感覺上，好像也能做到 Singleton pattern 的事，另外也適合拿來做 cache 管理之類的；Command pattern 跟 Proxy 其實也滿像的，不過實際應用的時候細節上會不太一樣，例如 undo, history maintain 的功能；Template Method 看完發現我之前用的好像還蠻像這個的XD，主要是對同類型的應用，細節上可能不太一樣，所以提供一個 abstact 的 template class，再由這些應用繼承並實作不同細節的地方，不過這樣其實就必須先知道每個應用的大概實作方法和架構，才有辦法切開不同的地方，我自己之前寫是分三層，整個功能的流程，每個 method 的流程以及 method 的細部實作，把前兩層寫好一個大致通用的之後，再把細部留給繼承的 class 實作，如果有些差異太大，沒辦法只實作細部實作的話，再考慮覆寫整個 method 的流程這樣。我自己寫的可以參考 [這裡]。

總之，這本書個人是覺得還算 OK 囉，有興趣的可以參考看看 :)。

[這裡]: https://github.com/carlcarl/imgurup