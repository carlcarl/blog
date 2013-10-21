Title: Quorum read
Date: 2012-02-17 21:43
Author: carlcarl
Post_ID: 254
Category: database
Tags: Cassandra, hbase
Slug: quorum-read

最近在看 paper，剛好看到這個名詞，似乎是 Cassandra 有用到的一個技巧。

在 cluster
的環境中，有時候並不能保證說讀取到的值一定會是最新的，可能會因為架構或設計上的不同，可能在做
replication 的部份是非同步進行的，所以更大大增加拿到舊值的機率。

此方法簡單說就是讀取多個 node 的值來作比較，基本上這些值都會有
timestamp，所以可以根據時間的新舊來決定該用哪個值，但是還是會有一些問題，像是如果讀到的值都是舊的那該怎麼辦，如果變成一次測全部
node 的值，效能上不用說一定會很慢，所以這個問題我不知道是怎麼解決的。

其實還滿詭異的，如果真的要要求資料一致性的話，我覺得還不如就選資料一致性較強的
HBase（不過我不太喜歡要分一堆角色的分散式系統，感覺在架構配置上會比較麻煩）。

