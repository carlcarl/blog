Title: popen check empty
Date: 2013-04-26 20:31
Author: carlcarl
Post_ID: 835
Category: C &amp; C++
Tags: popen
Slug: popen-check-empty

最近常在用 `popen` 呼叫系統指令，並讀取執行的結果作判斷，而有時候會有想確認內容是否會為空的需求，因為 popen return 的是一個 file descriptor，本來想說能不能用 `ftell`
找出大小來做判斷，不過[後來證明不行][]，pipe 跟一般的檔案還是有差別。

找了一堆資料，後來只想到用 `fgetc` 來讀，再用讀不讀得到值作為判斷 orz，不知道有沒有其他更好的解法就是。

  [後來證明不行]: http://stackoverflow.com/questions/7705338/ftell-function-giving-1-in-c-for-stdout
