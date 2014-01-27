Title: OSX Mavericks ftp in finder
Date: 2014-01-27 23:00
Author: carlcarl
Post_ID: 1390
Category: mac
Tags: mac, ftp
Slug: osx_mavericks_ftp_in_finder


找了一下 OSX 怎麼把 ftp 的目錄顯示在 finder 中，finder 雖然有內建 `Connect to Server` 的功能，不過非常爛，帳密登入的一直沒辦法 work，而且好像還是 read only，ftp command line 卻都沒啥問題，所以建議就放棄內建的功能，別浪費時間了 = =。

後來看到 [MacFusion] 搭配 [OSXFUSE]，想說來試試看，就結果來看，還是沒有 KDE 的 Dolphin 來得方便啊QQ，不過也還算堪用就是。

兩個都裝完之後，開啓 MacFusion，加入要 mount 的 ftp 或其他種 folder，但是我的沒有在 Finder sidebar 中出現可以點選的 folder，要先點選 Finder 中你這台 device，在裡面就看得到你 mount 的 folder 了。我試過加到 finder 的 sidebar 中，不過在 umount 之後，點選 sidebar 中的圖示也不會自動 mount，有點麻煩...。

總之，目前先這樣用吧，以後有啥更好的用法再試試看。


[MacFusion]: http://macfusionapp.org
[OSXFUSE]: http://osxfuse.github.io



參考資料：  
[MacFuse and MacFusion]
[Can I edit content on an FTP server through Finder?]  
[FTP from Mac OS X]  
[Mac: Mounting FTP/SFTP volumes with the Finder]  
[Connect to FTP server in Finder not working]


[MacFuse and MacFusion]: http://help.pop.psu.edu/popnet-help/mac/macfuse-and-macfusion
[Can I edit content on an FTP server through Finder?]: https://apple.stackexchange.com/questions/24699/can-i-edit-content-on-an-ftp-server-through-finder
[FTP from Mac OS X]: http://osxdaily.com/2011/02/07/ftp-from-mac/
[Mac: Mounting FTP/SFTP volumes with the Finder]: http://www.thxbye.de/mac/mac-mounting-ftpsftp-volumes-with-the-finder.html
[Connect to FTP server in Finder not working]: https://apple.stackexchange.com/questions/110965/connect-to-ftp-server-in-finder-not-working
