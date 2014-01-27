Title: OSX Mavericks ext4
Date: 2014-01-26 01:00
Author: carlcarl
Post_ID: 1389
Category: mac
Tags: mac, ext4
Slug: osx_mavericks_ext4



記錄一下 OSX Mavericks 讀寫 ext4 的方法：

先裝 [OSXFUSE]，安裝過程中記得選 `MacFUSE Compatibility Layer`。

裝 [fuse-ext2]。

接下來如果接上 ext4 的隨身碟，應該是能讀，但是卻還是不能寫(死)。根據 [Read and write ext4 file system on Mac OS X Lion] 這篇的做法，需要變成用手動 mount 的方式:

    :::bash
    fuse-ext2 -o force /dev/disk1s1　/where/to/mount/your/ext4/file/system

記得這邊的 `disk1s1` 和 `/where/to/mount/your/ext4/file/system` 要換成你自己對應的 device 和要 mount 上去的資料夾。之後再看看有沒有比較好的解決方案orz。


參考網址:  
[How can I mount an ext4 file system on OS X?]  
[How can I uninstall fuse-ext2 and macfuse on Mac OS X]  



[OSXFUSE]: http://osxfuse.github.io/
[fuse-ext2]: http://sourceforge.net/projects/fuse-ext2/
[How can I mount an ext4 file system on OS X?]: https://apple.stackexchange.com/questions/29842/how-can-i-mount-an-ext4-file-system-on-os-x
[How can I uninstall fuse-ext2 and macfuse on Mac OS X]: http://superuser.com/questions/87547/how-can-i-uninstall-fuse-ext2-and-macfuse-on-mac-os-x
[Read and write ext4 file system on Mac OS X Lion]: http://tex-numerics.blogspot.tw/2013/05/read-and-write-ext4-file-system-on-mac.html

