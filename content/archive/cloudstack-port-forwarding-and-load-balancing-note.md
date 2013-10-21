Title: CloudStack port forwarding and load balancing note
Date: 2012-08-09 04:15
Author: carlcarl
Post_ID: 555
Category: cloud
Tags: cloudstack
Slug: cloudstack-port-forwarding-and-load-balancing-note

我用的是 Advanced network 的架構，而當我在弄 CloudStack 的 VM port
forwarding 時，發現 port 怎麼樣都 forward 不到 VM
上，找了很多資料，後來才發現原來是前端的 firewall 也要開對應的 port
才行。  
<!--more-->  
![firewall
rule][] 

像是這邊我開了 5566 ~ 5567 port 的 TCP 連線，然後 Source
CIDR 設 0.0.0.0/0 表示接受來自所有的 IP。

![port
forwarding rule][] 

然後我在這邊就可以拿上面有開放出來的 5566
port，然後拿來 forward 到某台 VM 的 80 port 了

Load balance 也是差不多一樣，總之前面的 firewall 要先開 port
，不然預設都會在前面被擋掉，以至於到不了後面的 port forwarding 或 load
balancing 來處理。

  [firewall rule]: http://i.imgur.com/Q59NTKhl.png
    "firewall rule"
  [port forwarding rule]: http://i.imgur.com/aOeDQq2l.png
    "port forwarding rule"
