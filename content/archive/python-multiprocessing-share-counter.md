Title: Python multiprocessing share counter
Date: 2013-09-19 00:09
Author: carlcarl
Post_ID: 1315
Category: python
Tags: multiprocessing
Slug: python-multiprocessing-share-counter

找了一下，以下是基本的寫法：

<!--more-->

	:::python
    counter = 0

    def countdown(data):
        counter_lock = Lock()
        global counter
        with counter_lock:
            counter.value -= 1
        print(data)

    def main():
        def init(args):
            global counter
            counter = args
        data_list = ['a', 'b', 'c']
        global counter
        counter = multiprocessing.Value('i', len(data_list))
        pool = multiprocessing.Pool(
            initializer=init,
            initargs=(counter,)
        )
        pool.map(countdown, data_list)
        pool.close()
        pool.join()

這邊在找資料的時候發現一個問題，那就是 `counter.value`
在做運算的時候需不需要 lock？  
於是我看了一下 source code，`multiprocessing.Value` 等於
`multiprocessing.sharedctypes.Value`，下面是它的定義：

	:::python
    def Value(typecode_or_type, *args, **kwds):
        '''
        Return a synchronization wrapper for a Value
        '''
        lock = kwds.pop('lock', None)
        if kwds:
            raise ValueError('unrecognized keyword argument(s): %s' % kwds.keys())
        obj = RawValue(typecode_or_type, *args)
        if lock is False:
            return obj
        if lock in (True, None):
            lock = RLock()
        if not hasattr(lock, 'acquire'):
            raise AttributeError("'%r' has no method 'acquire'" % lock)
        return synchronized(obj, lock)

在沒有指定 lock 的情況下，會設 `None`，在是 `None` 的情況下會自動 assign
一個 `RLock`，`RLock` 是啥可以參考[這邊][]，總之也是 lock
的一種，那這邊這個 `lock` 會不會用到呢？再繼續看 `synchronized`
這個定義：

	:::python
    def synchronized(obj, lock=None):
        assert not isinstance(obj, SynchronizedBase), 'object already synchronized'

        if isinstance(obj, ctypes._SimpleCData):
            return Synchronized(obj, lock)
        elif isinstance(obj, ctypes.Array):
            if obj._type_ is ctypes.c_char:
                return SynchronizedString(obj, lock)
            return SynchronizedArray(obj, lock)
        else:
            cls = type(obj)
            try:
                scls = class_cache[cls]
            except KeyError:
                names = [field[0] for field in cls._fields_]
                d = dict((name, make_property(name)) for name in names)
                classname = 'Synchronized' + cls.__name__
                scls = class_cache[cls] = type(classname, (SynchronizedBase,), d)
            return scls(obj, lock)

這邊由於我當初指定是 `multiprocessing.Value('i', len(data_list))`，`'i'`
表示是 integer type，等於 `c_int`，而 `c_int`這個 class 本身是繼承
`_SimpleCData`，所以在上面的判斷式會走第一個 `if`，並 return
`Synchronized(obj, lock)`。

	::python
    class Synchronized(SynchronizedBase):
        value = make_property('value')

`Synchronized` 這邊繼承 `SynchronizedBase`，不過重點是接下來的
value，這邊的 `make_property` 是另外寫的，定義如下：

	:::python
    def make_property(name):
        try:
            return prop_cache[name]
        except KeyError:
            d = {}
            exec template % ((name,)*7) in d
            prop_cache[name] = d[name]
            return d[name]

    template = '''
    def get%s(self):
        self.acquire()
        try:
            return self._obj.%s
        finally:
            self.release()
    def set%s(self, value):
        self.acquire()
        try:
            self._obj.%s = value
        finally:
            self.release()
    %s = property(get%s, set%s)
    '''

還滿有趣的寫法，可以看到針對 `value` 這個變數提供了對應的 get 和 set
method，`self.acquire()` 和 `self.release()` 分別是要求和釋放
lock，這邊可以再看一下 `SynchronizedBase` 的定義：

	:::python
    class SynchronizedBase(object):

        def __init__(self, obj, lock=None):
            self._obj = obj
            self._lock = lock or RLock()
            self.acquire = self._lock.acquire
            self.release = self._lock.release

        def __reduce__(self):
            assert_spawning(self)
            return synchronized, (self._obj, self._lock)

        def get_obj(self):
            return self._obj

        def get_lock(self):
            return self._lock

        def __repr__(self):
            return '<%s wrapper for %s>' % (type(self).__name__, self._obj)

這邊的 `self.acquire` 和 `self.release` 其實就會分別呼叫 `_lock` 裡的
`acquire` 和 `release` method。

所以不需要再自己 lock 囉？......No,
還是需要(炸)。以上面的程式來排一個流程，假如 A process 和 B process
分別對 `counter.value` 做遞增 (`counter.value += 1`)：

	:::python
    counter.value = 10
    counter.value + 1  # 暫存值 11, A process
    counter.value + 1  # 暫存值 11, B process
    counter.value = 11 # A process
    counter.value = 11 # B process

依然會得到錯誤的結果~~。

參考資料：  
[Python multiprocessing easy way to implement a simple counter?][]  
[Python multiprocessing and a shared counter][]  
[multiprocessing.sharedctypes.synchronized][]  
[Shared counter with Python’s multiprocessing][]  
[python multiprocessing lock issue][]

  [這邊]: http://blog.csdn.net/JGood/article/details/4305604
  [Python multiprocessing easy way to implement a simple counter?]: http://stackoverflow.com/questions/1233222/
  [Python multiprocessing and a shared counter]: http://stackoverflow.com/questions/1233222/python-multiprocessing-easy-way-to-implement-a-simple-counter
  [multiprocessing.sharedctypes.synchronized]: http://docs.python.org/2/library/multiprocessing.html#multiprocessing.sharedctypes.synchronized
  [Shared counter with Python’s multiprocessing]: http://eli.thegreenplace.net/2012/01/04/shared-counter-with-pythons-multiprocessing/
  [python multiprocessing lock issue]: http://stackoverflow.com/questions/8276933/python-multiprocessing-lock-issue
