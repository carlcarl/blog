Title: Python functools.wraps note
Date: 2013-08-06 15:38
Author: carlcarl
Post_ID: 1249
Category: python
Tags: wraps
Slug: python-functools-wraps-note

研究一下 `functools.wraps`。

<!--more-->

### 用法
	
	:::python
    def deco(f):
        # @wraps(f)
        def hello(*args, **kwargs):
            print(f.__name__) # print `test`
        return wrapper

    @deco
    def test():
        return 1 + 1

    print(test.__name__) # print `hello`

在 `hello` 裡 print 出
'test'，這個沒什麼問題，但是在宣告完後，如果想確認 `test` 的 `__name__`
attribute，會發現 print 出的是 'hello'，這是因為 `test` 在被 decorate
後，其實已經變成 `hello`，真正的 `test` 則被包在 `hello` 裡執行。如果把
`@wraps` 前的註解拿掉，就會發現最後 print 出來的會變回原來的
'test'，因為 `wraps` 這個 decorator 會將一些原本 function 的 attribute
複製到外面的 function 上，可以看一下內部實作。

### 實作

	:::python
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
    WRAPPER_UPDATES = ('__dict__',)

    def update_wrapper(wrapper,
                       wrapped,
                       assigned = WRAPPER_ASSIGNMENTS,
                       updated = WRAPPER_UPDATES):
        for attr in assigned:
            setattr(wrapper, attr, getattr(wrapped, attr))
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
        # Return the wrapper so this can be used as a decorator via partial()
        return wrapper

    def wraps(wrapped,
              assigned = WRAPPER_ASSIGNMENTS,
              updated = WRAPPER_UPDATES):
        return partial(update_wrapper, wrapped=wrapped,
                       assigned=assigned, updated=updated)

首先先看 `wraps` 這個 function，參數中 `wrapped` 是參數傳進來的
function，`assigned` 是要複製的 attribute，`updated` 是要更新的
attribute， 這邊可以看到是直接呼叫 `partial`，至於這個 function
的用法可以參考：

-   [python的functools.partial用法解释][]
-   [python 的 functools.partial 函數][]

簡單說就是像把 `wrapped`, `assigned`, `updated` 丟進 `update_wrapper`
的參數裡，並 return 一個新 function，接著只要把還沒填的參數丟進這個新的
function 就可以了。因為是 decorator 的用法，所以 `parital` 產生的
function 在 return 時會被執行，接著跑到 `update_wrapper`。

`update_wrapper` 這邊多了個 `wrapper` 參數，也就是被 `@wraps` 裝飾 的
function，以最上面的例子來看，就是 `hello` function
。這邊可以順便注意一下傳進 decorator function
參數的順序，首先會先傳進來的是 decorator function 的參數(剛才的
`wrapped`)，再來是被 decorate 的 function 本身(`wrapper`)，再來則是被
decorate 的 function 的參數這樣(這邊沒有使用)。

接著 `update_wrapper` 會將 `wrapped` 裡的 `__module__`, `__name__`,
`__doc__` 複製到 `wrapper` 上，並將 `__dict__`
也更新過去，大致就完成了~~。

這邊好奇為啥 `__dict__` 也要複製過去，應該說 function 為啥要有
`__dict__`，搜尋了一下，看到 [stackoverflow
上也有人問][]，在答案的連結裡可以看到一些用法：

	:::python
    def a():
        pass

    a.publish = 1
    a.unittest = '''...'''

    if a.publish:
        print a()

    if hasattr(a, 'unittest'):
        testframework.execute(a.unittest)

參考網址：  
[What does functools.wraps do?][]  
[Python: Why to use @wraps with decorators?][]  
[what is the difference between functools.wraps and update_wrapper][]

  [python的functools.partial用法解释]: http://www.au92.com/archives/how-to-use-functools-partial-in-python.html
  [python 的 functools.partial 函數]: http://blog.blackwhite.tw/2013/02/python-functoolspartial.html
  [stackoverflow 上也有人問]: http://stackoverflow.com/questions/7439023/why-do-python-functions-have-a-dict
  [What does functools.wraps do?]: http://stackoverflow.com/questions/308999/what-does-functools-wraps-do
  [Python: Why to use @wraps with decorators?]: http://artemrudenko.wordpress.com/2013/04/15/python-why-you-need-to-use-wraps-with-decorators/
  [what is the difference between functools.wraps and update_wrapper]: http://stackoverflow.com/questions/15357776/what-is-the-difference-between-functools-wraps-and-update-wrapper
