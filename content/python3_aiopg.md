Title: Python3 aiopg
Date: 2015-07-11 01:00
Author: carlcarl
Post_ID: 1432
Category: python
Tags: postgresql, python, coroutine
Slug: python3_aiopg


`aiopg` 是一個使用了 `aysncio` + `psycopg2` 的一個 library，最近在用的時候想到一個問題：aiopg 的 connection 能不能在各個 coroutine 間 share，從想法上是覺得好像不行，查了一下，看起來應該是會有問題：[Support for coroutine libraries]，所以就變成必須在各個 coroutine 裡建 connection，頂多就變成從 pool 裡面拿這樣。


另外 `aiopg` 在 transaction 的部分也要注意：[Transactions]，`BEGIN` 和 `COMMIT` 必須用 execute 的方式，而 method 的部分則不給使用。

再來就是 `psycopg2` 不是每個 method 在 `aiopg` 上都會有，例如：`psycopg2.extras.Json`，在 `aiopg` 上並沒有，就要另外再 import psycopg2 這樣。



[Support for coroutine libraries]: http://initd.org/psycopg/docs/advanced.html#green-support
[Transactions]: https://aiopg.readthedocs.org/en/stable/core.html#aiopg-core-transactions


