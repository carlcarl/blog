Title: How to connect the server in virtualbox
Date: 2011-04-21 18:55
Author: carlcarl
Post_ID: 17
Category: linux
Slug: how-to-connect-the-server-in-virtualbox

如果是要用ssh連的話 就輸入以下指令

`C:Program FilesOracleVirtualBoxVBoxManage.exe" modifyvm "VM name" --natpf1
"guestssh,tcp,,2222,,22"`

前面如果有改 virtualbox 的安裝位置的話 就要跟著改

`VM name` 請輸入當初在建VM時所輸入的名稱

後面指的是如果連到本機的 2222 port 的話 就轉向到VM中的 22 port

同樣的也可以用 `guesthttp,tcp,,80,,80` 的方式來把連到本機 80 port的轉向連到VM中的 80 port

把server建在VM中這樣還可以降低本機被攻擊的危險(如果不考慮效能的因素的話):P

而且系統備份也很方便~~

 

參考資料:

<http://slo.twbbs.org/?p=417>
