Title: JavaScript setTimeout focus
Date: 2015-04-10 01:30
Author: carlcarl
Post_ID: 1421
Category: js
Tags: js
Slug: javascript_settimeout_focus


stackoverflow 上可以看到幾個關於呼叫 `focus()` 沒有作用的問題：

* [jQuery Textarea focus]
* [Why isn't this textarea focusing with .focus()?]

其中有幾個答案提供了這種解法:

	:::js
    setTimeout(function() {
        $('#reply_message').focus();
    }, 0);


看起來還滿詭異的，為啥用個 timeout function 就可以解了，查了一下，這篇感覺是正解: [JS setTimeout延迟时间为0的详解]。

	:::text
	JavaScript 引擎在执行 onkeypress 时，由于没有多线程的同步执行，不可能同时去处理刚创建元素的 focus 和 select 事件，由于这两个事件都不在队列中，在完成 onkeypress 后，JavaScript 引擎已经丢弃了这两个事件，正如你看到的例子 1 的情况。而在例子 2 中，由于setTimeout可以把任务从某个队列中跳脱成为新队列，因而能够得到期望的结果。


[jQuery Textarea focus]: http://stackoverflow.com/questions/4191200/jquery-textarea-focus
[Why isn't this textarea focusing with .focus()?]: stackoverflow.com/questions/8380759/why-isnt-this-textarea-focusing-with-focus
[JS setTimeout延迟时间为0的详解]: http://blog.csdn.net/lsk_jd/article/details/6080772



