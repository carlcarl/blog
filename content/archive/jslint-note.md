Title: JSLint note
Date: 2013-06-08 01:36
Author: carlcarl
Post_ID: 897
Category: js
Tags: jslint
Slug: jslint-note

記錄一些錯誤的處理方式。 <!--more-->

### 1. Document was used before it was defined

因為 JSLint 只是用來分析一般的 javascript code，像 `document`
這種在瀏覽器上才有用的 global variable，就要在檔案開始加個宣告：

	:::javascript
    /* jslint browser:true */

### 2. This is an ES5 feature

比較新的
feature。在一些舊瀏覽器可能會有問題，如果不想管那些舊瀏覽器的話，簡單加上以下這樣就可解決：

	:::javascript
    /* jslint es5: true */

### 3. Move the invocation into the parens that contain the function

改成用括弧將 function 和 參數 整個包起來就 OK 了，不過這部分不知道為啥
JSLint 要這樣做就是了 orz。

	:::javascript
    (function () {})()
    // 改成
    (function () {}())

### 4. Missing 'use strict' statement

在檔案 或 function 開頭加上下面這行即可。這個代表的是套用較嚴格的方式來
parse javascript，所以如果程式太亂寫的話，就會直接丟 exception
或是給你直接掛掉之類的，要注意。

	:::javascript
    "use strict";

### 5. The body of a for in should be wrapped in an if statement

會出現這個通常是因為你用以下的方式跑迴圈：

	:::javascript
    for (i in xxx) {
        // do something
    }

你需要改成如下：

	:::javascript
    for (i in xxx) {
        if (xxx.hasOwnProperty(i)) {
            // do something
        }
    }

    // 或者是

    for (i = 0; i < xxx.length; i += 1) {
        // do something
    }

第一種之所以會需要加上 `if` 的檢查是因為 `for in` 的方式會連 `prototype`
裡的 attirbute 也會被走到，加上 `hasOwnProperty`
可以避免這個問題。但是如果是直接 assign 的 attribute
的話，還是會被走到，要防止這種問題，用第二種方法會是比較一勞永逸的方式。

### 6. Unexpected 'continue'

連 `continue` 也不給用，也太龜毛，現在就先無視吧
XD。如果硬要解的話，因為 `continue` 通常會在某個 `if` 底下，例如這樣：

	:::javascript
    while (xxx) {
        if (yyy) {
            continue;
        }
        // do something
    }

這時就可以改成：

	:::javascript
    while (xxx) {
        if (!yyy) {
            // do something
        }
    }

其他還有一些比較複雜的組合，如果解不了的話，就選擇無視吧～～。

### 7. JSLint: Using a function before it's defined error function

可以調位置的話就調調看，如果有交互參考的話，就看實際執行是否會有問題，沒有的話也可以考慮不用理這樣。

### 8. unexpected ++

就乖乖改用 `+= 1` 吧(炸)，用 `++` 明明應該很 OK 的啊，我也不曉得 JSLint
在想啥。

參考資料：  

<http://stackoverflow.com/questions/10766201/how-to-rectify-document-was-used-before-it-was-defined-using-jslint>  
<http://jslinterrors.com/this-is-an-es5-feature/>  

<http://stackoverflow.com/questions/4979252/jslint-error-move-the-invocation-into-the-parens-that-contain-the-function>  
<http://stackoverflow.com/questions/1450721/solution-for-jslint-errors>
<http://stackoverflow.com/questions/1335851/what-does-use-strict-do-in-javascript-and-what-is-the-reasoning-behind-it>  

<http://stackoverflow.com/questions/1963102/what-does-the-jslint-error-body-of-a-for-in-should-be-wrapped-in-an-if-statemen>  
<http://stackoverflow.com/questions/6071762/unexpected-continue>
<http://stackoverflow.com/questions/806163/jslint-using-a-function-before-its-defined-error>  

<http://stackoverflow.com/questions/3000276/the-unexpected-error-in-jslint>
