Title: backbone.js some tips
Date: 2014-01-15 01:00
Author: carlcarl
Post_ID: 1384
Category: web
Tags: backbone
Slug: backbone_js_some_tips


用了個簡單的網站改成用 [backbone.js] 來套，之所以用 backbone 是因為不太喜歡在 html 上加一堆 attributes，backbone 這樣偏純 js，再加上 [underscore] 做 template 的方式覺得比較適合我，以後如果有興趣再碰看看 [ember.js] 吧，[angular.js] 現階段感覺還蠻流行的，不過就不太想碰就是 XD。

套完 backbone 之後，程式硬是多出了一倍的量，不知道到底有沒有幫助到我(炸)，而且 backbone 官網的 docuemtn 常會漏掉一些重要的資訊，讓我卡超久= =，這邊順便記錄一下這樣。架構的話，看到有篇 stackoverflow 上的問題，他的 example code 我還蠻喜歡的，也許可以參考看看: [Backbone parsing json response]。

## Create element in views

如果是要 create elements 的話，在 views 裡要用 `tagname`，例如要 create 一個 `<tr></tr>`的話就用: `tagname: tr`，而如果是要操作在 DOM 中的 element 的話就用 `el`，例如: `el: $('#content')`。

## Receive events

要注意 event 中要 monitor 的 element，必須在 `el` 這個 element 裡面，不然永遠聽不到= =。例如:

    :::js
    Backbone.View.extend({
        el: $('#content'),
        events: {
            'submit #myform': 'mysubmit'
        }
    });
    
`#myform` 就必須是在 `#content` 裡面。


## Parse ajax response

Ajax 的 response 格式有很多種，每個網站可能都有自己的格式，在 Collection 的部分，假如要讀的多筆資料都在 `response.data` 裡的話，就會需要在 Collection 裡頭加上 `parse` 來處理:

    :::js
    /* json example
    {
        "data": [ {
            "id": "1",
            "value": "1"
            }, {
            "id": "2",
            "value": "2"
        } ],
        "meta": "test"
    }
    */
    App.Collections.Items = Backbone.Collection.extend({
        model: new App.Models.Item(),
        url: '/',
        parse: function (response) {
            return response.data;
        }
    });

又假如在 `response.data` 這個 array 裡，主要的 attribute 名稱不是 `id`，而是其他名稱，比如說 `name`，就要在 Model 裡加上定義，不然 Model parse 會有問題:

    :::js
    /* json example from response
    {
        "data": [ {
            "name": "1",
            "value": "1"
            }, {
            "name": "2",
            "value": "2"
        } ],
        "meta": "test"
    }
    */

    App.Models.Item = Backbone.Model.extend({
        idAttribute: 'name'
    });

## Serialize form inputs

我之前是用 [jquery-serialize-object]，後來因為要 submit 的資料不多，所以就把這個 plugin 拿掉，改用 jquery selector 來拿了。

其他也可以參考這篇: [Serialize form inputs to JSON using Backbone.js]


## Pass values to Model

如果不想要傳過去的資料變成 Model 的 attributes，而是其他額外的資料的話，例如要傳一個 flag 的話，可以這樣做:

    :::js
    App.Models.Item = Backbone.Model.extend({
        initialize: function(attributes, options) {
            this.flag = options.flag;
        }
    });
    var item = new App.Models.Item({name: 'car'}, {flag: true});

## spinner animation with ajax

在 ajax 發出和收到的時候分別顯示和隱藏 spinner，原本其實就可以用 `ajaxStart` 和 `ajaxStop` 這兩個 event 來處理，在 backbone 裡也可以用以下的方式:

    :::js
    initialize: function(){
        this.items = new APP.Models.Item();
        this.items.bind('request', this.ajaxStart, this);
        this.items.bind('sync', this.ajaxComplete, this);
    }

    ajaxStart: function(arg1,arg2,arg3){
        $('#loading').fadeIn({duration:100});
    },
    ajaxComplete: function(){
        $('#loading').fadeOut({duration:100});
    }
    
## How to render tables

參考這篇的解答: [Render html table with underscore template engine using a backbone complex model]
    
## Post collections

這個我還沒試過，不過可以參考這篇解答的做法: [“How” to save an entire collection in Backbone.js - Backbone.sync or jQuery.ajax?]
    
## 2-way data binding

backbone 本身沒提供，只能用 jquery selector 來抓，看到有個 plugin 也許可以用用看，我是還沒用過lol: [backbone.stickit]


參考資料:  
[Backbone.js Beginner Video Tutorial]  
[backbone.js ajax calls]  
[How can I pass properties into a Backbone.Model which I do not wish to be treated as attributes?]  
[backbone.js - how and when to show a spinner]  
[AngularJS vs Ember]  

[backbone.js]: http://backbonejs.org
[underscore]: http://underscorejs.org
[ember.js]: http://emberjs.com
[angular.js]: http://angularjs.org
[Backbone parsing json response]: http://stackoverflow.com/questions/13257722/backbone-parsing-json-response
[jquery-serialize-object]: https://github.com/macek/jquery-serialize-object
[Serialize form inputs to JSON using Backbone.js]: http://stackoverflow.com/questions/14554111/serialize-form-inputs-to-json-using-backbone-js
[How can I pass properties into a Backbone.Model which I do not wish to be treated as attributes?]: http://stackoverflow.com/questions/7084651/how-can-i-pass-properties-into-a-backbone-model-which-i-do-not-wish-to-be-treate
[Render html table with underscore template engine using a backbone complex model]: http://stackoverflow.com/questions/10257401/render-html-table-with-underscore-template-engine-using-a-backbone-complex-model
[“How” to save an entire collection in Backbone.js - Backbone.sync or jQuery.ajax?]: http://stackoverflow.com/questions/6879138/how-to-save-an-entire-collection-in-backbone-js-backbone-sync-or-jquery-ajax
[backbone.stickit]: http://nytimes.github.io/backbone.stickit/
[Backbone.js Beginner Video Tutorial]: http://backbonetutorials.com/what-is-a-view/
[backbone.js ajax calls]: http://stackoverflow.com/questions/11331604/backbone-js-ajax-calls
[backbone.js - how and when to show a spinner]: http://stackoverflow.com/questions/5832295/backbone-js-how-and-when-to-show-a-spinner
[AngularJS vs Ember]: http://eviltrout.com/2013/06/15/ember-vs-angular.html

