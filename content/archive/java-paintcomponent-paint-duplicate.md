Title: Java paintComponent paint duplicate
Date: 2013-06-11 03:43
Author: carlcarl
Post_ID: 967
Category: java
Tags: java
Slug: java-paintcomponent-paint-duplicate

之前寫 Java 的時候遇到的小問題，在實作 `JPanel` 的 `paintComponent`
時，發現怎麼畫完後會出現多餘的重複物件。

後來找了一下資料，在 stackoverflow
發現[有人有一樣的問題][]。解決方法也很簡單，只要在 `paintComponent`
一開始加上
`super.paintComponent(g);`，可惜的是不懂為啥不呼叫的話會出現這樣的結果就是。

  [有人有一樣的問題]: http://stackoverflow.com/questions/13773315/java-paintcomponent-paints-a-copy-of-the-top-gui-panel-for-no-apparent-reason
