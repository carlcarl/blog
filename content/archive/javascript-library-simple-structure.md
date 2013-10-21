Title: Javascript Library simple structure
Date: 2012-07-23 02:03
Author: carlcarl
Post_ID: 537
Category: js
Tags: javascript
Slug: javascript-library-simple-structure

之前在找 Javascript 這方面的 library
該怎麼寫，看了一些資料，覺得以下這種方式不錯  
<!--more-->

	:::javascript
	// library example
	var animal = function(window) {
    	var name = 'tom'; // private variable

    	var API = {
        	"getName": function(){ return name;}
    	};
    	return API;
	}(windows);

	animal.getName(); // call API


這樣寫法的優點：

-   透過將這個 library 當作一個物件並呼叫其中的
    function，使用上較不會跟其他 library function 混淆，也較好
    maintain。
-   使用這個 library 的時候，也能夠保護到內部的 private variable
    不被直接做 access。
-   可更直覺的知道哪些是提供出來的
    API，因為這邊透過變數命名和統一管理將這些 API 都放在 API varaible
    裡，最後再 return 這個 API
    variable。這樣子在外部使用的時候就限制只能操作這個 API variable
    裡頭所定義的 function 或 variable。

至於其他更詳細的可以看一下下面的參考網址，這邊的架構主要是從裏面學習來的。

參考網址：  
<http://www.atlanticbt.com/blog/create-your-own-javascript-library/>
