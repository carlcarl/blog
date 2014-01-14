Title: g0v.tw nav menu fix
Date: 2014-01-02 00:40
Author: carlcarl
Post_ID: 1383
Category: web
Tags: g0v, jade, css
Slug: g0v_tw_nav_menu_fix


[g0v.tw] 最近改版了，css framework 也改用 [semantic-ui]，看起來還蠻潮的，不過目前在用，感覺問題還蠻多的，其中一個大問題應該就是沒有 responsive layout 可以直接套用，所以大概就只能自己土炮吧～。不過這次修的問題跟這個無關，主要是要讓 nav menu 可以隨著在不同網頁，然後 highlight color 到不同 menu item 上，主要有遇到幾個問題：

## 網頁不是用 ajax，而是直接連結到不同網頁
所以就不能用 javascript 直接 assign class 到對應的 menu item 上，只能在 template 上動手腳，template 是用 `jade`。首先先在 nav menu 的 template 開頭加上變數宣告，define 一個 `vars` block，然後把這些變數塞到各個 menu item 的 classs 內：

    :::jade
    - var nav_cls = {}
    - nav_cls.index = nav_cls.about = nav_cls.talk = ''
    - nav_cls.actinfo = nav_cls.join = nav_cls.contact = ''
    block vars
    .ui.fluid.seven.item.menu
    a(class="item #{ nav_cls.index }",href="/index.html")
      | 首頁
    div(class="ui pointing dropdown link item #{ nav_cls.about }")


然後在各個 sub template 引用 `vars` 這個 block，然後在這個 block 內，assgin value 給對應的 variable ,至於為啥用 `highlight` 不用 `active` 下面還會再解釋：

    :::jade
    block vars
    - nav_cls.about = 'highlight'

這個是目前想到的解法。有想過直接給一個固定的 variable，裡面塞對應的 element id，再用 javascript assign class 進去就好，寫法簡潔得多，不過這樣在 render 上就有點不太好看了 orz。

## Dropdown menu 不支援 active 下的 color 顯示
嗯...，用 semantic-ui 本身的 menu color highlight，只對 `<a>` element 有效，而且 dropdown menu 在 pop  menu 時會加上 `.active`，但是 hide menu 之後會把 `.active` 拿掉囧，所以乾脆自己生一個 class 來代替，如下：

    :::css
    .highlight {
	    border-color: #F05940!important;
	    color: #F05940!important;
	    -webkit-box-shadow: 0 .2em 0 inset !important;
	    box-shadow: 0 .2em 0 inset !important;
	    border-radius: 0 !important;
    }

Ref commit: [https://github.com/g0v/g0v.tw/commit/df20f4c917521977eb33f0f29ab932395843de49]

參考連結:  
[variable in class name jade]  
[Multi-line variable declaration is not supported]  

[g0v.tw]: http://g0v.tw
[semantic-ui]: http://semantic-ui.com
[https://github.com/g0v/g0v.tw/commit/df20f4c917521977eb33f0f29ab932395843de49]: https://github.com/g0v/g0v.tw/commit/df20f4c917521977eb33f0f29ab932395843de49
[variable in class name jade]: http://stackoverflow.com/questions/13668881/variable-in-class-name-jade
[Multi-line variable declaration is not supported]: https://github.com/visionmedia/jade/issues/698
