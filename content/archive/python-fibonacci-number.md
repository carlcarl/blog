Title: Python fibonacci number
Date: 2013-08-04 02:35
Author: carlcarl
Post_ID: 1240
Category: python
Tags: fibonacci
Slug: python-fibonacci-number

在 Python Taiwan 社團看到的寫法：

<!--more-->

	:::python
    print (lambda n, p: (([p.append(p[-1]+p[-2]) for k in range(n-2)]) and False) or p[-1])(10, [1,1])

`n` 和 `p` 分別對應 `10` 和 `[1,1]` 這兩個參數，`10` 表示要 fibonacci
的第十個項數，`[1,1]` 是第一項和第二項的值。然後是一個 loop 將 `p`
陣列中最後兩個值加起來再 append 進 `p`，比較妙的是，因為這邊 loop append
完之後，整個會是一個
list，但是因為這邊只要最後一個值，而且又要忽略掉前面這個
list，於是用了 `and False` 將整個值算成 `False`，接著又由於
`False` 與 `or` 放在一起，所以會再進一步取後面的值，也就是
`p[-1]`，也就是算完後的最後一個值。
