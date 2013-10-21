Title: CloudStack comment
Date: 2012-05-23 19:56
Author: carlcarl
Post_ID: 473
Category: cloud
Tags: cloudstack, openstack, xenserver
Slug: cloudstack

![CloudStack][]
<!--more-->  
用 CloudStack 也算用了一段時間了，來講一下心得好了 XD。 當初會看到是在
Youtube 上面看到教學影片，覺得安裝還滿方便的，而且是 Citrix
推出的，所以搭配 XenServer 的效果看起來還不錯，所以就來裝裝看了。

安裝算是還滿簡單的，跟 OpenStack 比起來......( 感覺 OpenStack
還是比較注重在 KVM
上)，網路架構配置也不用太花腦筋，我自己是只配置一張網卡在 CloudStack
的架構上，並未將外網和內網分開，照理來說分開來會比較好啦，但是覺得這樣做，以後就能直接拿一般的
PC(單網卡) 來擴充當 compute node。management ip address 和 guest ip
address 就直接分在同個網段下的不同區域，例如 192.168.1.10\~192.168.1.30
是 management，192.168.1.60 ~ 192.168.1.199 是
guest，這邊只是例子，看你要怎麼搭配。

這邊順便補充一下，management ip 是拿來提供給 CloudStack 的 System VM
用的，CloudStack 的一些服務都會透過建立成 VM
的方式來運作，一般是不會用到太多，至於要給多少，這個我就沒什麼建議了，因為我也不太清楚到底會用到幾個XD，就我現在的情況，3個
compute node，共開了 3 個 System VM 這樣，可以當作個參考唄。

節點的角色就簡略的分成兩種：CloudStack 和 compute， CloudStack node
是負責管理 compute node 和提供 WebUI 用的，所以灌在 vm
上也沒關係，我就灌在另外有使用的 ESX
上，而且這樣子如果要做啥修改，先做個 snapshot
就好，也不用太怕他炸掉這樣XD。compute node
就必須用實體的機器了，我是使用 XenServer 5.6
sp2，不管是要本身安裝或是要整合到 CloudStack
中都算是非常方便，比較要注意的是在第一次安裝 CloudStack，必須搭配一個
XenServer(或其他種類的 hypervisor: 如 KVM) 來做安裝，因為必須用這個
hypervisor 開啟幾個 System VM ，CloudStack 才能運作。

 

接著來總結一下幾項優缺點。

優點：

-   安裝方便
-   跟 XenServer 整合良好 ( 因為是同一家公司嘛XD )
-   WebUI 管理方便，特別是在外面的時候，也不是每台電腦都能讓你灌
    Xencenter 的
-   升級還算簡單，照著官方 release notes 裡的 upgrade instruction
    步驟去做通常都 OK
-   可以設定自動備份和備份的周期 ( 夠強大的話也是可以考慮自己寫 script
    直接去操作 XenServer 的 API 來做啦 )

缺點：

-   3.x 版之後的 WebUI 有點華而不實，導致原本在 2.x
    版中很簡單的操作程序在 3.x
    版中被拉的很冗長，不過看最近的升級，是有在改進啦......
-   沒辦法利用 CloudStack 的 snapshot 直接復原 VM 的 Root disk，只能利用
    snapshot 另外做一個 VM 出來，但是這樣子出來的 VM ip
    就不一樣了，所以對這點有點傷腦筋，VM 的 datadisk 則是可以根據
    snapshot 直接做復原。
-   最近比較紅的還是
    OpenStack，參與和開發的公司非常多，所以會讓人有點懷疑 CloudStack
    未來的發展性

最後再補充一些東西：

-   想用 local storage 的話，必須用管理者權限進入 WebUI 去改設定啟用
    local storage 才行，不然只能用 shared storage
-   安裝 XenServer 的時候，選擇 XenDesktop optimized 的話，storage 會從
    lvm 轉為 ext，但是在 CloudStack 中當作 local storage
    還是可以正常使用的，效能的話我就不太清楚了。
-   不建議將已經有開啟 VM 的 hypervisor 加入到 CloudStack
    中，這點是官方講的，還是要注意一下。
-   刪除 host 或 storage 或其他啥的會失敗無法刪的話，請參考
    <http://wiki.cloudstack.org/display/QA/Organization+states>
    ，這篇會告訴你該如何處理

 

  [CloudStack]: http://i.imgur.com/QqDmZipl.png
    "Selection_49cef6"
