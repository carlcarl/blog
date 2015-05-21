Title: C search.h
Date: 2015-05-21 11:00
Author: carlcarl
Post_ID: 1427
Category: c
Tags: c
Slug: c_search_h

TL;DR: 不要用 search.h 裡的 function.


最近需要改寫別人的程式，裡面有用到 search.h 裡的 function: `hsearch`，hsearch 其實就是 hash table，搭配其他的一些 function 就可以不用自己實作。但是，這個 hsearch 的缺點卻非常多:

1. hash table 的 size 必須是固定的
2. 沒有 method 可以 traverse 整個 table 的 entry
3. 記憶體管理很麻煩，可能還必須自己再 maintain 一個 linked list 才行


這邊是 wiki 上的範例: [http://rosettacode.org/wiki/Associative_arrays/Creation/C#To_delete_or_iterate]，如果還要再寫一個 linked list，那還不如 hash table 就自己實作算了= =。

後來改看 `tsearch`，t 是 tree search，比起 `hsearch`，可以 traverse 整個 tree，size 也是 dynamic，然後記憶體管理的話，也有額外的 callback function 可以自己做 free，完全就是好用多了，除了時間複雜度比較高以外，但是，後來還是遇到了問題......，那就是 tsearch return 的 pointer，它的 return pointer 型態是 `void*`，但是回傳的值是存 node 記憶體位址的變數的記憶體位址(好像有點饒舌...)，我本來以為會直接就是 node 的記憶體位址，於是我用: 

	:::c
	XXX *ptr;
	ptr = (XXX*)tsearch(blahblah...);
	printf("%s\n", ptr->xxx);

結果卻印出一堆亂碼，後來找了很久，找到這篇: [Don't understand how tsearch return pointers work]，才發現原來不是這樣...。所以正確寫法應該是

	:::c
	XXX **ptr;
	ptr = (XXX**)tsearch(blahblah...);
	printf("%s\n", (*ptr)->xxx);


就是一個不管怎麼用都會撞到牆的概念，感覺自己寫好像還比較快...。





[http://rosettacode.org/wiki/Associative_arrays/Creation/C#To_delete_or_iterate]: http://rosettacode.org/wiki/Associative_arrays/Creation/C#To_delete_or_iterate
[Don't understand how tsearch return pointers work]: https://stackoverflow.com/questions/21840116/dont-understand-how-tsearch-return-pointers-work



