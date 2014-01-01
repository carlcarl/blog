Title: Ubuntu install salt tool
Date: 2012-10-15 20:44
Author: carlcarl
Post_ID: 690
Category: python
Tags: saltstack
Slug: ubuntu-install-salt-tool

現在有操作多台機器執行同樣指令的需求，想說裝 [salt][]
來管理看看，詳細介紹可以點連結進去看看。簡單來講，這套工具可以讓你方便一次去對多個機器進行操作，另外還可以透過用 Python 並 import salt module 來處理整個流程和回傳的資料。  

salt 分成了兩個部份，`salt-master` 和 `salt-minion` ，`salt-master`
就是 server 端，也就是你用來管理其他機器的機器上要裝的 (有點饒舌=
=")，minion 則是 client 端，就是被管理的機器所要裝的套件。server
端會開個 service 讓 client 連，所以 client 端必須能夠知道 server 端的 IP
或者是 host name ，client 端連上來後，server 端可以決定是否接受這個
client 端的要求，接受的話，之後就能夠管理這個 client
。以下是兩邊所要裝的套件流程:

salt-master:

	:::bash
	sudo apt-get install python-software-properties
	sudo add-apt-repository ppa:saltstack/salt
	sudo apt-get update
	sudo apt-get install salt-master

salt-minion:

	:::bash
	sudo apt-get install python-software-properties
	sudo add-apt-repository ppa:saltstack/salt
	sudo apt-get update
	sudo apt-get install salt-minion

   
   
master 這邊裝好後，如果你的 master 有多個 IP
(如果沒有的話，可以跳過這步），可以選擇你要用哪個 IP 來 listen，修改
`/etc/salt/master`

	:::text
    interface: 改成你 master 要 listen 的 IP

修改完後，重啟 service:

	:::bash
	sudo /etc/init.d/salt-master restart

   
minion 這邊則要修改 `/etc/salt/minion`

	:::text
    master: master 的 IP 或者是 host name

修改完後，重啟 service:

	:::bash
	sudo /etc/init.d/salt-minion restart

   
   
安裝好之後，接下來要在 master 這邊加入 minion 這邊的機器，執行

	:::bash
	sudo salt-key -L


應該能夠看到 minion 端的 host name ，接著執行:

	:::bash
	sudo salt-key -a <minon_hostname>


就可以將這台機器納入管理中了。  
   
設定完後，可以輸入下面指令做測試，回傳 True 的話就表示 OK 啦

	:::bash
	sudo salt * test.ping
	

參考網址：  
<http://docs.saltstack.org/en/latest/topics/installation/ubuntu.html>  
<http://docs.saltstack.org/en/latest/topics/tutorials/modules.html>

  [salt]: http://docs.saltstack.org/en/latest/contents.html
