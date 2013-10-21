Title: ajaxfileupload SyntaxError: missing } in XML expression
Date: 2012-04-06 04:39
Author: carlcarl
Post_ID: 355
Category: js
Tags: ajax, ajaxfileupload
Slug: ajaxfileupload-syntaxerror-missing-in-xml-expression

本來用 [ajaxfileupload][]
用得好好的，結果不知道為什麼就突然出現這個錯誤，查了一下資料再加上自己比對的結果才發現，原來是因為我在
server 端的 response 加上 content type="application/json"
的關係，而這個結果導致在 client 這邊的 response 被 `<pre></pre>`
給包了起來，也因此在 parse 的時候出現錯誤。

解決方法有兩種：  
1. server 端拿掉 minetype  
2. client 端把 response 的 `<pre></pre>` 處理掉。  
這邊我是選擇了第2種方法來做，因為我覺得 minetype
這東西是需要加的，現在不加怕以後會有相容性問題。

這邊其實很簡單，只要在 ajaxfileupload.js 中修改 uploadHttpData functon
為以下的樣子就行了：

    :::javascript
    uploadHttpData: function( r, type ) {
        var data = !type;
        data = type == "xml" || data ? r.responseXML : r.responseText;
        // If the type is "script", eval it in global context
        if ( type == "script" )
            jQuery.globalEval( data );
        // Get the JavaScript object, if JSON is used.
        if ( type == "json" )
        {
            // If you add mimetype in your response,
            // you have to delete the '<pre></pre>' tag
            var data = r.responseText;
            if(data.indexOf('<pre>') != -1)
            {
                data = data.substring(5, data.length-6);
            }
            eval( "data = " + data );
        }
        // evaluate scripts within html
        if ( type == "html" )
            jQuery("<div>").html(data).evalScripts();
            //alert($('param', data).each(function(){alert($(this).attr('value'));}));
        return data;
    }


加上了一些修正之後，為了以後方便就丟到 [github][]
上面了，需要的可以直接抓下來用。

參考網址：  
<http://www.iteye.com/problems/34213>  
[http://stackoverflow.com/questions/3939741/][]

  [ajaxfileupload]: http://www.phpletter.com/Our-Projects/AjaxFileUpload/
  [github]: https://github.com/carlcarl/AjaxFileUpload
  [http://stackoverflow.com/questions/3939741/]: http://stackoverflow.com/questions/3939741/ajaxfileupload-syntaxerror-missing-in-xml-expression
