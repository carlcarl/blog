Title: Linux kernel space get time interval
Date: 2013-04-27 00:23
Author: carlcarl
Post_ID: 838
Category: C
Tags: linux, time
Slug: linux-kernel-space-get-time-interval

之前聽到可以用 `jiffies`
來抓時間，可是我自己測的結果是前後抓的時間會都一樣囧。查了一下
stackoverflow，也有[一個遇到一樣的問題][]，我猜可能 `jiffies` 也是用
period update 的方式做更新，由於中間測量的 function
太快，導致來不及更新就拿到了一樣的值這樣。而在下面的回答中看到可以用
`do_gettimeofday()` 來抓時間區間，簡單範例如下：  

	:::c
	#include <linux/time.h>
	// ...
	struct timeval begin, end;
	unsigned long val;
	
	do_gettimeofday(&begin);
	// Do something here
	do_gettimeofday(&end);

	// Get milliseconds 
	val = (end.tv_sec - begin.tv_sec) * 1000;
	val += ((end.tv_usec - begin.tv_usec) / 1000);
	printk("%lu msn", val);


另外也可以用 `getnstimeofday()`，可以取到 nano second，至於
`gettimeofday()` 則是 user space 的
function，故在這裡不考慮。ftrace 感覺好像很威，不過需要調設定，之後有機會再來試試看。

參考網址：  
<http://www.makelinux.net/ldd3/chp-7-sect-1>  
<http://stackoverflow.com/questions/10885685/jiffies-how-to-calculate-seconds-elapsed>

  [一個遇到一樣的問題]: http://stackoverflow.com/questions/4655711/measuring-execution-time-of-a-function-inside-linux-kernel
