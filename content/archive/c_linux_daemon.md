Title: C Linux Daemon
Date: 2015-02-01 11:00
Author: carlcarl
Post_ID: 1406
Category: c
Tags: c
Slug: c_linux_daemon

查了一些在 Linux 上怎麼用 C 寫一支 daemon 的做法:

* [http://stackoverflow.com/questions/17954432/creating-a-daemon-in-linux]* [http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html]* [http://shahmirj.com/blog/beginners-guide-to-creating-a-daemon-in-linux]* [http://man7.org/tlpi/code/online/dist/daemons/become_daemon.c.html]* [http://www.freedesktop.org/software/systemd/man/daemon.html]

另外就是有建議說: 不要直接 call `unistd.h` 裡的 daemon function，因為每個平台的實作可能都不太一樣。再來就是還有一些延伸的問題需要處理，像是如何 reload config，做 single instance 和 error 訊息怎麼處理之類的。

[http://stackoverflow.com/questions/17954432/creating-a-daemon-in-linux]: http://stackoverflow.com/questions/17954432/creating-a-daemon-in-linux
[http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html]: http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html
[http://shahmirj.com/blog/beginners-guide-to-creating-a-daemon-in-linux]: http://shahmirj.com/blog/beginners-guide-to-creating-a-daemon-in-linux
[http://man7.org/tlpi/code/online/dist/daemons/become_daemon.c.html]: http://man7.org/tlpi/code/online/dist/daemons/become_daemon.c.html
[http://www.freedesktop.org/software/systemd/man/daemon.html]: http://www.freedesktop.org/software/systemd/man/daemon.html


