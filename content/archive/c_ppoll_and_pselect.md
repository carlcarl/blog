Title: C ppoll and pselect
Date: 2015-02-03 20:00
Author: carlcarl
Post_ID: 1409
Category: c
Tags: poll, select
Slug: c_ppoll_and_pselect


通常 `ppoll` 和 `pselect` 會搭配 `sigprocmask` 使用，先透過 `sigprocmask` block signal，然後在 `ppoll` 和 `pselect` 這邊再 unblock signal 做處理，例如常見的 daemon reload 可以這樣做：

	:::c
	
	// C
	volatile sig_atomic_t reload_flag = 0, terminate_flag = 0;

	static void sig_handler(int sig)
	{
    	if (sig == SIGHUP) {
        	reload_flag = 1;
    	}
    	else if (sig == SIGTERM) {
        	terminate_flag = 1;
    	}
	}
	
	// A
	sigset_t mask, orig_mask;
    sigemptyset (&mask);
    sigaddset (&mask, SIGTERM);
    sigaddset (&mask, SIGHUP);

    if (sigprocmask(SIG_BLOCK, &mask, &orig_mask) < 0) {
        exit(EXIT_FAILURE);
    }
    
    // B
    struct sigaction sa;
    sigemptyset(&sa.sa_mask);
    sa.sa_handler = sig_handler;
    if (sigaction(SIGHUP, &sa, NULL) == -1) {
        exit(EXIT_FAILURE);
    }
    if (sigaction(SIGTERM, &sa, NULL) == -1) {
        exit(EXIT_FAILURE);
    }
	
    
    // Set socket blah blah
    
    // D
    while (1) {
        int poll_ret = ppoll(fds, MAX_FDS_SIZE, tv, orig_mask);
        if (poll_ret == -1) {
            if (errno != EINTR) {
                exit(EXIT_FAILURE);
            } else if (reload_flag) {
                // process reload
                reload_flag = 0;
            } else if (terminate_flag) {
                // process terminate
                terminate_flag = 0;
                break;
            }
        } else if (poll_ret > 0) {
            // process socket
        } else if (poll_ret == 0) {
            // process timeout
        } else {
            exit(EXIT_FAILURE);
        }
    }

`A` 這段先將 `SIGTERM` 和 `SIGHUP` block 起來，接著在 `B` 這邊設定這兩種 signal 的 callback，`C` 這裏的 callback function 中則去設定 flag，這裏的 `sig_atomic_t` 是表示這個 type 變數的操作保證是 atomic 的，通常會是 `int` 就是，資料的部分可以參考:

* [小学一下volatile和sig_atomic_t类型.]
* [Proper usage of volatile sig_atomic_t]

`D` 的部分，就是在 interrupt 進來之後，判斷這些 flag，做更進一步的處理。


至於 `pselect` 的部分可以參考這邊: 

* [Linux select() vs ppoll() vs pselect()]
* [Using pselect() to avoid a signal race]



另外，如果要用 `ppoll` 的話，要先 define 一個變數，不然會出現 `implicit definition` 的警告：

	:::c
	#ifndef __USE_GNU
	/* Define this to avoid a warning about implicit definition of ppoll.*/
	#define __USE_GNU
	#endif
	#include <poll.h>


為啥不用 `epoll`? 因為連線數很少，用 `epoll` 不見得比較好，`libevent` 差不多一樣道理。


Ref:

* [/src/lirc_srv.c]
* [sigprocmask 阻塞进程]
* [catching signals while reading from pipe with select()]
* [pselect 和 select]
* [poll、ppoll 浅析]
* [select / poll / epoll: practical difference for system architects]
* [aspyct / signal.c]
* [Sockets using poll()]


[/src/lirc_srv.c]: https://searchcode.com/codesearch/view/555780/
[sigprocmask 阻塞进程]: http://blog.csdn.net/muge0913/article/details/7334771
[小学一下volatile和sig_atomic_t类型.]: http://blog.csdn.net/realdragon2/article/details/2935533
[Proper usage of volatile sig_atomic_t]: https://stackoverflow.com/questions/8488791/proper-usage-of-volatile-sig-atomic-t#_=_
[Linux select() vs ppoll() vs pselect()]: http://stackoverflow.com/questions/9774986/linux-select-vs-ppoll-vs-pselect
[Using pselect() to avoid a signal race]: http://www.linuxprogrammingblog.com/code-examples/using-pselect-to-avoid-a-signal-race
[catching signals while reading from pipe with select()]: http://stackoverflow.com/questions/6962150/catching-signals-while-reading-from-pipe-with-select
[pselect 和 select]: http://www.cnblogs.com/diegodu/p/3988103.html
[poll、ppoll 浅析]: http://blog.csdn.net/feng19870412/article/details/9001857
[select / poll / epoll: practical difference for system architects]: http://www.ulduzsoft.com/2014/01/select-poll-epoll-practical-difference-for-system-architects/
[aspyct / signal.c]: https://gist.github.com/aspyct/3462238
[Sockets using poll()]: http://cboard.cprogramming.com/c-programming/158125-sockets-using-poll.html


