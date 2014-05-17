Title: tcp_tw_recycle note
Date: 2014-05-14 16:30
Author: carlcarl
Post_ID: 1395
Category: linux
Tags: linux
Slug: tcp_tw_recycle_note


## 簡單結論
* `/proc/sys/net/ipv4/tcp_tw_reuse` 可以開。
* `/proc/sys/net/ipv4/tcp_tw_recycle` 不應該開。


Links:  
[tcp_tw_recycle和tcp_timestamps导致connect失败问题]  
[打开tcp_tw_recycle引起的一个问题]  
[tcp_tw_reuse vs tcp_tw_recycle : Which to use (or both)?]  
[Linux Tweaking]  
[Dropping of connections with tcp_tw_recycle]  


[tcp_tw_recycle和tcp_timestamps导致connect失败问题]: http://blog.sina.com.cn/s/blog_781b0c850100znjd.html
[打开tcp_tw_recycle引起的一个问题]: http://www.pagefault.info/?p=416
[tcp_tw_reuse vs tcp_tw_recycle : Which to use (or both)?]: http://stackoverflow.com/questions/6426253/tcp-tw-reuse-vs-tcp-tw-recycle-which-to-use-or-both
[Linux Tweaking]: http://www.speedguide.net/articles/linux-tweaking-121
[Dropping of connections with tcp_tw_recycle]: http://stackoverflow.com/questions/8893888/dropping-of-connections-with-tcp-tw-recycle

