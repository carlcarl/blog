Title: Python decorate method inside class
Date: 2013-06-02 04:45
Author: carlcarl
Post_ID: 865
Category: python
Tags: class, decorate, python
Slug: python-decorate-method-inside-class

簡易版的可以直接參考
<http://stackoverflow.com/questions/1367514/how-to-decorate-a-method-inside-a-class>。  
<!--more-->  
以我的例子來說，我需要對某些 method 加上 retry
的機制，除了需要有參數外，還希望能夠把 decorate method 放在 class
裡頭，這樣我才能呼叫 class 裡頭另外的 method。以下是簡單的例子：

	:::python
    class Test():
    
        def retry(tries=2, delay=1):
            def deco_retry(f):
                # f is the method decorated
                def f_retry(self, *args, **kwargs):
                    f(self, *args, **kwargs)
                    self.do_something()
                return f_retry
            return deco_retry
         

        @retry()
        def request(self):
            # do something

卡住的原因是因為不知道 `retry` 裡的 `self`
要從哪邊傳進來。而從上面的程式來看，整個參數傳遞的順序應該是：  
1. Arguments(from decorate method)  
2. decorated method  
3. Arguments(from decorated method)

第三個部分也就是 `f_retry`，`self` 會在這邊傳進來，因為它也是 `request`
的參數，所以後來想想其實也滿合理的就是。
