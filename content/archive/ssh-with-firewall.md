Title: ssh with firewall
Date: 2013-06-19 00:19
Author: carlcarl
Post_ID: 1053
Category: linux
Tags: ssh
Slug: ssh-with-firewall

記錄一下實用的 ssh 穿牆指令，然後這邊有個前提是：在牆外要有可以 ssh
的主機，這裡以 `example.com` 為例。 (其實參考資料的連結內容更詳細
XD，有需要的人建議點進去看看唄～～。)

1.  從內部往外。

<!-- -->

	:::bash
    # 在 local 開一個 9999 的 port 轉到 `example.com` 的 22 port，
    # 接下來只要把 proxy 的設定指到 localhost 的 9999 就可以了。
    ssh -NfD 9999 user@example.com

1.  從外部連內。

<!-- -->

	:::bash
    # 這邊必須先在內部的 server 輸入下面這一行，連到 example.com，
    # 然後在 example.com 上開 9999 port 來建立一個通道，
    ssh -NfR 9999:localhost:22 user@example.com
     
    # 在 example.com 上連這個 port 即可。
    ssh -p 9999 -l user localhost
     
    # 如果需要 ssh 以外的連線，仿照第一個方法，加個 9998 的 port，
    # proxy 設定改成 example.com 9998 port 即可。
    ssh -p 9999 -l user -D 9998 localhost

怕斷線的話可以用 `autossh`，記得要另外安裝，通常預設不會有。前面 `ssh`
的指令改成 `autossh -M 12345`。`12345` 是自己隨便給的。

參考資料：  
[反向建立 SSH Tunnel、免 VPN 連回公司][]

  [反向建立 SSH Tunnel、免 VPN 連回公司]: http://josephj.com/entry.php?id=312
