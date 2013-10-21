Title: Python setup.py package_data permission
Date: 2013-06-10 02:12
Author: carlcarl
Post_ID: 941
Category: python
Slug: python-setup-py-package_data-permission

最近嘗試把一些額外的 static 檔案加入到 python 的 package
裡來讓程式操作，後來有查到可以在 setup.py 裡設定
`package_data`，照著做之後好像滿順利的，但是在用 root 權限 install
完，用一般使用者執行就遇到 permission 的錯誤了。

<!--more-->

看了一下安裝目錄下的 static 檔案，結果權限是 `400`，owner 是
`root`，難怪一般使用者無法讀取，想說會不會是因為我的原本檔案權限的關係，檢查了一下，果然是
`400`，但是我改了權限再重新安裝居然還是一樣，這時我還想說會不會是原本就有這樣的限制，還查了一堆資料
orz。

最後想到，會不會是因為我那些 build 所產生的目錄的關係，於是我把
`xxx.pkg-info`，`build` 和 `dist`
這三個資料夾都移除掉後再重新安裝，果然就 OK 了 =.=。

所以結論是：

1.  setup.py 的 `package_data`
    裡的檔案在安裝的時候會繼承你原來的檔案讀寫權限，只是用 root
    安裝的話，owner 和 group 會變。
2.  鬼打牆的時候，記得把那些 build 資料夾刪一刪。

前面在查資料的時候，看到在 [stackoverflow][]
也有個人跟我有一樣的問題，後來就順便回了一下，不過不確定這樣是否能解決他的問題就是，而且也滿久以前發的了:P。

  [stackoverflow]: http://stackoverflow.com/questions/14861634/how-do-i-distribute-data-files-with-a-python-package-such-that-theyre-readable
