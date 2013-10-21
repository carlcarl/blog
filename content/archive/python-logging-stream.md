Title: Python logging stream
Date: 2013-07-25 17:11
Author: carlcarl
Post_ID: 1230
Category: python
Tags: logging, uniout
Slug: python-logging-stream

在用 [uniout][] 的時候發現 logging
的時候沒辦法自動轉輸出為中文(因為資料有些是中文，然後有時候又需要做些log
囧)，看了一下 `uniout` 的 code，看來做法是另外用了一個物件，然後把
`sys.stdout` 的屬性複製上去，再加上編碼的功能，最後再將 `sys.stdout`
assign 成這個物件。

<!--more-->

### 我用的 logger 程式

	:::python
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)

想說 `logging` module 應該也是丟
`stdout`，不過怎麼設就是不行，所以還是看一下 source code。

### logging module

首先先隨便找個 function 下手 XD。這邊先看 `Logger` 的
`debug()`，`debug()` 裡面呼叫到 `_log()`，裡面做了一些 message
的處理，然後呼叫到 `handle()`，`handle()` 又呼叫
`callHandlers()`，底下是 `callHandlers()` 的 source code：

	:::python
    def callHandlers(self, record):
        """
        Pass a record to all relevant handlers.

        Loop through all handlers for this logger and its parents in the
        logger hierarchy. If no handler was found, output a one-off error
        message to sys.stderr. Stop searching up the hierarchy whenever a
        logger with the "propagate" attribute set to zero is found - that
        will be the last logger whose handlers are called.
        """
        c = self
        found = 0
        while c:
            for hdlr in c.handlers:
                found = found + 1
                if record.levelno >= hdlr.level:
                    hdlr.handle(record)
            if not c.propagate:
                c = None    #break out
            else:
                c = c.parent
        if (found == 0) and raiseExceptions and not self.manager.emittedNoHandlerWarning:
            sys.stderr.write("No handlers could be found for logger"
                                " \"%s\"\n" % self.name)
            self.manager.emittedNoHandlerWarning = 1

蠻好奇為啥不用 `break`，而是 assign `C = None`
來跳出迴圈，不過這個是題外話 XD。這邊主要要看的是
`hdlr.handle(record)`，本來以為是 call 回去剛才上面的
`handle()`，不過研究了一下發現應該不是這樣，這個是 call 到另外一個
`class Handler` 裡面的 `handle()` 才對。

`class Handler` 裡的 `handle()` 會呼叫
`emit()`，但是去看的時候發現裡面丟了個
`NotImplementedError Exception`，看來比較像是個 abstract
class。這邊有繼承 `Handler` 的主要有 `FileHandler` 和 `StreamHandler`
這兩個 class，直覺應該是要看 `StreamHander` :P，這邊在 `StreamHandler`
的 `__init__()` 可以看到：

	:::python
    Handler.__init__(self)
    if stream is None:
        stream = sys.stderr
    self.stream = stream

另外再回去看 `logging.basicConfig()` 的其中內容：

	:::python
    if filename:
        mode = kwargs.get("filemode", 'a')
        hdlr = FileHandler(filename, mode)
    else:
        stream = kwargs.get("stream")
        hdlr = StreamHandler(stream)

如果不是開檔的話，就是走 stream 這邊，然後因為我在呼叫的時候沒有指定
`stream` 的值，所以這邊拿到會是 `None`，然後當成 `StreamHandler`
的參數，然後又因為 `stream` 是 `None`，所以就會使用 `sys.stderr`
來當輸出。

其實我 trace 到中間的時候就想到是 `stderr` 了
XD，不過想說還是有始有終的的把它 trace 下去。接下來要 fix
開始那個問題就很簡單了，在程式裡加入 `sys.stderr = uniout.uniout` 就 OK
了，不過這樣的做法會把兩邊的輸出混在一起，所以應該也可以在
`basicConfig()` 裡面指定 `stream=sys.stdout`，logging 就不要走 `stderr`
這樣~~。

  [uniout]: https://github.com/moskytw/uniout
