Title: C UNIX Socket
Date: 2015-02-03 15:00
Author: carlcarl
Post_ID: 1408
Category: c
Tags: c, socket, select, poll
Slug: c_unix_socket


可以參考這個連結的 code: [Unix Domain Socket]，我後來發現我們 project 裡的 code 也是參考這邊的= =|||，不過的確是還缺少一些東西，像是可以再加上 `select` 或是 `pselect` 來另外處理 signal，我自己是用 `pselect` 就是，有想過用 `ppoll` 來做，不過實際會聽的連線很少，感覺沒必要就直接用 `pselect` 了。

修正一下，之後還是改用 `ppoll` 好了XD，查了一下資料，就算是一個 socket，`poll` 還是比 `select` 快～～，參照 [Comparative measurements and analysis of I/O event notification mechanisms]。`epoll`看起來還是不用考慮，因為 event-based 在基本處理上的 overhead 都會比較大，只有一個 socket 的話還會比 poll 慢，上面連結內的數據也是顯示如此。

另外就是傳送資料的方式，因為是 local UNIX socket，所以就直接用 struct 轉了(炸)，如果是不同機器上用 TCP socket 的話，這樣其實會有 endian 和 padding 的問題，參照以下連結:

* [Passing a structure through Sockets in C]
* [passing a struct over TCP (SOCK_STREAM) socket in C]

不是改用 Protocol Buffers 這類的 library 封裝，不然就是直接用字串傳了。



Ref:

* [With a single file descriptor, Is there any performance difference between select, poll and epoll and …?]
* [unix domain socket]
* [poll vs select vs event-based]
* [poll、ppoll 浅析]
* [select / poll / epoll: practical difference for system architects]
* [The problem with select() vs. poll() (code)]


[Unix Domain Socket]: http://ohohsblog.blogspot.jp/2010/12/unix-domain-socket.html
[Comparative measurements and analysis of I/O event notification mechanisms]: http://www.intelliproject.net/articles/showArticle/index/io_multiplexing
[Passing a structure through Sockets in C]: https://stackoverflow.com/questions/1577161/passing-a-structure-through-sockets-in-c
[passing a struct over TCP (SOCK_STREAM) socket in C]: https://stackoverflow.com/questions/8000851/passing-a-struct-over-tcp-sock-stream-socket-in-c
[Protocol Buffers]: https://code.google.com/p/protobuf/
[With a single file descriptor, Is there any performance difference between select, poll and epoll and …?]: http://stackoverflow.com/questions/5647503/with-a-single-file-descriptor-is-there-any-performance-difference-between-selec/28294561#28294561
[unix domain socket]: http://kezeodsnx.pixnet.net/blog/post/33616080-unix-domain-socket-
[poll vs select vs event-based]: http://daniel.haxx.se/docs/poll-vs-select.html
[poll、ppoll 浅析]: http://blog.csdn.net/feng19870412/article/details/9001857
[select / poll / epoll: practical difference for system architects]: http://www.ulduzsoft.com/2014/01/select-poll-epoll-practical-difference-for-system-architects/
[The problem with select() vs. poll() (code)]: http://beesbuzz.biz/blog/e/2013/10/10-the_problem_with_select_vs_poll.php


