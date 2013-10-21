Title: Linux conntrack delete destination NAT
Date: 2013-06-27 16:41
Author: carlcarl
Post_ID: 1080
Category: linux
Tags: conntrack
Slug: linux-conntrack-delete-destination-nat

最近遇到在測 throughput 中，有一定機率無法關掉 DMZ
的問題，而且這邊只要關掉 throughput 後，DMZ 就會順利關掉，看起來像是
throughput 的連線讓被刪掉的 conntrack 連線又復活(?)了這樣 =.=。

<!--more-->

看了一下 firewall 的 rule，裡面確實是有刪除 conntrack connection 的
rule，指令如下：

	:::bash
    conntrack -D conntrack -g -r xxx.xxx.xxx.xxx

看了一下 `conntrack －L conntrack` 的記錄，grep 了在接收 throughput 的
port，發現還是有連線存在，來源是從 NAT
內部到外面...，所以看來這個連線也會讓外部的封包有機會進來的樣子。

第一直覺就是把這邊的連線也砍掉啦，規則就從
`conntrack -L conntrack -g -r` 這裡拿到所有的 dest ip，然後一個一個用
`conntrack -D conntrack -d dest_ip` 砍掉。

不過事情好像沒那麼美好 orz，後來用 `conntrack` 看，發現 source ip
的部分應該也要濾掉，而且因為 throughput
太大，有機會讓被砍掉的連線復活，所以又加了個迴圈來砍，聽起來有點暴力啊(汗)。這邊因為有些特殊需求，所以整個
shell 程式必須用 c 產生，判斷有沒有殺掉的部分就用
`popen("conntrack -L conntrack | grep xxx.xxx.xxx.xxx", "r")` 做，轉成
shell 的話大概如下，這邊迴圈就不寫了:P：

	:::bash
    # 因為有可能拿到複數個，所以需要用雙引號包起來
    outside_ip="$(conntrack -L conntrack -g -r xxx.xxx.xxx.xxx | awk '{ print $5 }' | cut -f2 -d=)"
    conntrack -D conntrack -g -r xxx.xxx.xxx.xxx

    check="$(conntrack -L conntrack | grep xxx.xxx.xxx.xxx)"
    if [ -n "$check" ]; then
        # -r 表示如果前面給的參數是空的話，就不執行後面的指令
        echo $outside_ip | xargs -r conntrack -D conntrack -d
        echo $outside_ip | xargs -r conntrack -D conntrack -s
    fi

整個解法其實沒有說很好，不知道還有沒有什麼更漂亮的解法就是了。

2013/10/03 補充
---------------

同事後來用了一個更好的方法修掉了，內容如下：

	:::bash
    iptables -t raw -I PREROUTING -s source_ip -j DROP
    conntrack -D conntrack -g -r source_ip
    iptables -t raw -D PREROUTING -s source_ip -j DROP

因為 raw 這張 table + PREROUTING 是在 ip conntrack
之前，所以先增加一個規則在前面將 source ip drop 掉，然後後面再清掉
conntrack 中的內容，清完後再把這條規則清掉就可以了。

參考網址：  
[conntrack manual][]  
[iptables中的conntrack記錄][]  
[用iptables的raw表解決ip_conntrack: table full, dropping packet的問題][]  

  [conntrack manual]: http://manpages.ubuntu.com/manpages/jaunty/man8/conntrack.8.html
  [iptables中的conntrack記錄]: http://hi.baidu.com/weioip/item/3a48aaf45efa600cd89e7296
  [用iptables的raw表解決ip_conntrack: table full, dropping packet的問題]: http://hi.baidu.com/farmerluo/item/f49bbdc0e390a52dee4665bb
