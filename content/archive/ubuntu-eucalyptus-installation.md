Title: Ubuntu Eucalyptus installation
Date: 2011-05-26 09:05
Author: carlcarl
Post_ID: 22
Category: cloud
Slug: ubuntu-eucalyptus-installation

我是在已有的 Ubuntu 上安裝 Eucalyptus，如果是直接用 Ubuntu Enterprise Cloud 應該會比較簡單 orz。

<!--more-->

大概講一下幾個我遇到的問題 orz。

### eucalyptus-cloud restart : Unknown instance

改直接執行 `eucalyptus-cloud`看看:

	:::text
	[error:0185] User 'eucalyptus' validated
	[error:0077] Path /usr/lib/jvm/java-6-openjdk is not a directory
	[error:0323] Cannot locate Java Home
	
如果出現以上的錯誤就是要裝 `openjdk-6-jre-headless`。


### 記得先執行 service
下面這行還滿方便的，不過記得要先到 `/etc/init.d/ `底下作: 

	:::bash
	for service in euca*; do start $service;done


### 註冊節點出現錯誤的問題

	:::text
	Warning: cannot file file node-cert.pem in //var/lib/eucalyptus/keys/
	Warning: cannot file file cluster-cert.pem in //var/lib/eucalyptus/keys/
	Warning: cannot file file node-pk.pem in //var/lib/eucalyptus/keys/


這個問題卡很久，明明就把 key 複製到 data node 上面了，用 `euca_conf --list-nodes` 還是空的沒東西= =

後來才想到我的 cluster node 裡 key 是放在 `keys/cluster/` 底下，所以把 key 複製到上一層 他就能找得到 key 了。上面那個錯誤訊息是在說找不到 cluster node 裡的 key 不是 data node 裡的。


參考網頁:  
[http://tamastarjanyi.blogspot.com/][]  
<http://open.eucalyptus.com/forum/problem-register-nodes>  
<http://open.eucalyptus.com/forum/node-controller-not-registering>  
<http://open.eucalyptus.com/forum/cannot-register-node>  
<http://open.eucalyptus.com/forum/problem-node-registration>  

  [http://tamastarjanyi.blogspot.com/]: http://tamastarjanyi.blogspot.com/2010/06/eucalyptus-problem-on-ubuntu-1004-lucid.html
