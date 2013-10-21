Title: git gnuTLS error
Date: 2012-02-22 15:53
Author: carlcarl
Post_ID: 269
Category: 版本管理
Tags: git, gnutls
Slug: git-gnutls-error

之前有台機器莫名沒辦法做「git clone https連結」，都會出現 `error: GnuTLS
recv error (-9): A TLS packet with unexpected length was
received`，查了老半天，還跟其他台的 git 比較設定，還是找不到答案，後來看到有人自己抓下來編譯好像就OK，所以我也想說自己抓 source code 下來試試看好了 XD。

去[官網][]抓了 source code
下來，編譯並裝到 `/usr/local` 底下，測試了一下，果然就可以了！反正更新啥的我也沒差，所以目前就先這樣囉～。

參考網址：  

<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=559371>  
<https://groups.google.com/group/google-code-hosting/browse_thread/thread/cfa3d43bca5d0774?pli=1>

  [官網]: http://git-scm.com/download
