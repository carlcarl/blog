Title: rsync exclude file
Date: 2011-08-27 11:18
Author: carlcarl
Post_ID: 40
Category: linux
Tags: rsync
Slug: rsync-exclude-file

最近想打包線上在跑的網站(在 Ubuntu 上)。本來想說用 `cp` 就好，但是 `cp`
沒辦法去 exclude 一些檔案列表，偏偏網站上面有些是暫存檔和使用者上傳的東西，另外還有一些雜七雜八不該包的 code。

後來查到可以用 `rsync` 來作 因為有支援 exclude 的參數，以下是範例，a
參數包含了一堆其他參數的功能，v 參數就是將詳細資訊印出來：

	:::bash
	rsync -av --exclude 'dir' source destination


想要 exclude 多一點的話可以這樣下：

	:::bash
	rsync -av --exclude 'dir1' --exclude 'dir2' source destination

 

要注意的一點是：  
如果想要避掉 某幾個目錄下的子目錄
像是每個目錄下的 `.svn` 資料夾，可以直接用 `--exclude '.svn/'`，
他會**自動避掉所有符合名稱的子目錄**，而如果是每個子目錄底下的檔案的話，如 `templates_c/底下的檔案`，可以用 `--exclude 'templates_c/*'`。

參考網址:  

[http://unix.stackexchange.com/questions/5774/][]  
<http://www.thegeekstuff.com/2011/01/rsync-exclude-files-and-folders/>  
<http://blog.xuite.net/jyoutw/xtech/20025390>

 

  [http://unix.stackexchange.com/questions/5774/]: http://unix.stackexchange.com/questions/5774/rsync-excluding-a-particular-subdirectory-and-its-children-where-the-subdirecto#_
