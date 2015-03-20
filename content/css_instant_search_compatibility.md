Title: CSS Instant Search Compatibility
Date: 2015-03-21 00:00
Author: carlcarl
Post_ID: 1417
Category: web
Tags: css
Slug: css_instant_search_compatibility


會看這個主要是很久之前看到的這篇文章: [使用 CSS:not 與 data-index 即時搜尋頁面]。

最近剛好又用到，所以順便研究了一下 IE 的相容性問題，其中比較明顯的是 `:not` 這個 pseudo class 在 IE 上的相容性不太好: [CSS3 :not Selector]，IE 的支援從 9 才開始，不過我實際測 IE8 似乎也是可行，IE7 就真的不行了。

本來想到的解法是先把所有的都 `display:none`，然後再篩選符合的去做對應的 display，ex: `table` or `block`，不過後來測試會死在把 css 塞進已存在的 style 這步，查了一下發現[舊 IE 對 style 的 innerHTML 是設定為 read only] = =，所以舊 IE 就沒辦法，只能用 JS 來解，後來發現很奇怪的是在舊 IE 上用 jQuery 來找 `:not` 居然就可以: `$('.wrap:not([data-index*="xxx"])')`，jQuery 的這個方式在舊 IE 上是可以 work 的。至於其他瀏覽器就可以直接用最上面那篇連結裡的方式來解，修改了那個範例如下：

	:::html
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>test</title>
      <style>
      body {
        background: #333;
        font-size: 1em;
        color: #f0f0f0;
        line-height: 1.1em;
      }
      a {
        text-decoration: none;
      }
      .section {
        width: 500px;
        margin: 0 auto;
        background: #555;
        padding: 1em;
        overflow: hidden;
      }
      .header {
        background: #d9444a;
        text-align: center;
        color: #fff;
        font-size: .5em;
        padding: .7em 0;
      }

      h2 {
        font-size: 1em;
        margin: 0 0 .5em 0;
        background: #444;
        display: inline-block;
        padding: .5em 1.2em;
        position: relative;
        left: -1em;
      }

      /* search layout start (you can skip it) */
      .search-form {
        text-align: right;
        input {
          border: none;
          padding: .5em;
          background: rgba(255,255,255,.5);
          color: #555;
        }
      }

      .wrap {
        display: table;
        background: #888;
        margin-right: .5em;
        padding: .5em;
        width: 46%;
        float: left;
      }
      </style>

      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    </head>
    <body>
      <div class="header">
        Search single page by CSS:not<br />
        <a href="http://blog.mukispace.com/pure-css-tooltip-data-tag‎/" target="_blank">(http://blog.mukispace.com/full-text-search-by-css/)‎</a>
      </div>
      <div class="section">
        <div class="search-form">
          <input id="search-input" type="text" placeholder="type name to search" /><button>Search</button>
          <style id="m-search"></style>
        </div>
        <div class="wrap" data-index="ju chu ko">
          <img src="http://lorempixel.com/40/40/people/1" border="0" />
          <div class="name">Ju Chu Ko</div>
        </div>
        <div class="wrap" data-index="browny lin">
          <img src="http://lorempixel.com/40/40/people/2" border="0" />
          <div class="name">Browny Lin</div>
        </div>
        <div class="wrap" data-index="妙卡甜心">
          <img src="http://lorempixel.com/40/40/people/3" border="0" />
          <div class="name">妙卡甜心</div>
        </div>
        <div class="wrap" data-index="mr.壞">
          <img src="http://lorempixel.com/40/40/people/4" border="0" />
          <div class="name">Mr.壞</div>
        </div>
        <div class="wrap" data-index="come on">
          <img src="http://lorempixel.com/40/40/people/5" border="0" />
          <div class="name">Come On!</div>
        </div>
        <div class="wrap" data-index="lester">
          <img src="http://lorempixel.com/40/40/people/6" border="0" />
          <div class="name">Lester</div>
        </div>
        <div class="wrap" data-index="林大中">
          <img src="http://lorempixel.com/40/40/people/7" border="0" />
          <div class="name">林大中</div>
        </div>
        <div class="wrap" data-index="高國滑">
          <img src="http://lorempixel.com/40/40/people/8" border="0" />
          <div class="name">高國滑</div>
        </div>
        <div class="wrap" data-index="kun1342">
          <img src="http://lorempixel.com/40/40/people/9" border="0" />
          <div class="name">Kun1342</div>
        </div>
        <div class="wrap" data-index="jimmy ku">
          <img src="http://lorempixel.com/40/40/people/10" border="0" />
          <div class="name">Jummy Ku</div>
        </div>
      </div>
      <script>


      $(function () {
        "use strict";

        var oldIE;
        if (window.attachEvent && !window.addEventListener) {
          oldIE = true;
        }


        $("#search-input").bind("change paste keyup", function(){
          var value, $mSearch, rule;

          value = $(this).val();

          if (oldIE) {
            if (!value) {
              $('.wrap').css('display', 'block');
              return;
            };

            $('.wrap').css('display', 'none');
            $('.wrap:not([data-index*="' + value.toLowerCase() + '"])').css('display', 'block');

          } else {
            $mSearch = $("#m-search");
            if (!value) {
              $mSearch.html("");
              return;
            };

            rule = '';
            rule += '.wrap:not([data-index*="' + value.toLowerCase() + '"]){display:none;}';
            $mSearch.html(rule);
          }

        });
      });


      </script>
    </body>
    </html>
	


至於多重條件篩選的話，這裏有兩種情況:

1. 一個欄位，只要符合兩種資料的其中一種就做顯示
2. 兩個欄位，兩個分別對兩種資料做篩選出皆符合的資料


以 name 和 phone 和 address 為例，如果有兩個欄位，一個欄位是可以搜尋 name 和 phone，另一個欄位是搜尋 address，兩個欄位可以一起作用，要實作這種情況，用 `:not` 再把不符合的隱藏掉似乎就做不太到，但是如果是先隱藏，再根據條件顯示的話似乎就可行:

	:::css
	.wrap {
	    display: none;
	}
	.wrap[data-address="xxx"][data-name="xxx"] {
	    display: block;
	}
	.wrap[data-address="xxx"][data-phone="xxx"] {
	    display: block;
	}
	
從這邊可以看到一些規則，要同時符合(and)的話，就 append 那個 attribute selector；只要符合其中一個就好的話，就另外加一條規則就可以，以此類推，然後再加上欄位是否為空值，要不要加進去判斷之類的檢查就可以了。不過這個方法有個不便的地方是要知道原來元素的 `display` 是啥 type 就是，如果是 table，你給它設 `block`，顯示可能就會炸了。


Ref:

* [Multiple Attribute Values]
* [CSS: multiple attribute selector]




[使用 CSS:not 與 data-index 即時搜尋頁面]: http://blog.mukispace.com/full-text-search-by-css/
[CSS3 :not Selector]: http://www.w3schools.com/cssref/sel_not.asp
[舊 IE 對 style 的 innerHTML 是設定為 read only]: http://stackoverflow.com/questions/2692770/adding-css-rules-with-text-method-to-style-element-does-not-work-in-ie
[Multiple Attribute Values]: https://css-tricks.com/multiple-attribute-values/
[CSS: multiple attribute selector]: http://stackoverflow.com/questions/12340737/css-multiple-attribute-selector


