Title: [vsphere]Failed to open disk scsi0:0
Date: 2012-02-19 00:55
Author: carlcarl
Post_ID: 258
Category: cloud
Tags: esx, esxi, vsphere
Slug: vsphere-failed-to-open-disk-scsi00

今天想試試看利用網路上的 Virtual Appliance 開 VM，下載完後利用 client
介面就可以上傳到 datastore，可是在新增 VM，並選擇完 vmdk
檔後，開啟VM時就出現了錯誤訊息囧。

錯誤訊息內容: `Failed to open disk scsi0:0: Unsupported and/or invalid
disk type 7. `

Google 了一下，似乎是下載下來後還要做轉換（後來看官方的安裝手冊也是的確講要這樣做 orz）。  
首先要先連到有和上傳的 datastore 連線的 esxi server，接著進到 `/vmfs/volumes/你的datastore/`，利用以下指令做轉換：

	:::text
	vmkfstools -i 你原來的vmdk檔 轉完的vmdk檔名


兩個檔案名稱不要重複，轉完之後，重新設定 VM 就可以正常開啟囉。

參考網址：  

<http://blog.learnadmin.com/2010/09/solution-vmware-vm-import-failed-to.html>
