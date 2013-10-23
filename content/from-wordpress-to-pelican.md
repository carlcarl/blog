Title: From wordpress to pelican
Date: 2013-10-24 02:18
Author: carlcarl
Post_ID: 1376
Category: python, blog
Tags: pelican
Slug: from-wordpress-to-pelican

終於從 [wordpress][] 轉到 [pelican][] 了，中間經歷了不少的問題，之所以從 wordpress 離開到 pelican，主要是覺得 wordpress 本身其實綁了很多我不需要的功能，現在我只是想純粹做一些筆記而已，於是朝 static site generator 這方面去看，之前是有看過 [octopress][]，但是對 ruby 實在沒啥興趣，找了一下 python 寫的，發現其實也有蠻多種的，後來看 pelican 有蠻多人都有試過，而且開發也還蠻熱烈的，於是就選擇了這個 blog 系統。

接下來就是想想該怎麼轉移，從 wordpress export 文章出來之後，pelican 提供了 `pelican-import` 這個工具可以將 wordpress 文章匯入的功能，還蠻方便的，但是卻沒有支援 `post_id` 這個文章屬性，於是我自己 [fork] 了出來，加上了這個功能，丟了一個 pull request 過去，只可惜作者好像不領情，內容大概是說我不應該這樣做，會變成要加一個屬性，就得加一個參數進去之類的，後來想想也沒錯，而且不一定每個人都需要這個 id，但是其實我覺得可以透過參數來加入自己要的 metadata，而且這些額外的 metadata 也可以考慮直接丟到一個 list，直接 loop scan就可以了，但是作者後來就沒理我了 orz。

import 完之後就是惡夢的開始了，因為我中間轉了很多次 blog 平台，從 pixnet，wordpress(轉了幾次放的地方)，現在到 pelican，發現以前很多連結和圖片，還有一些 code snippet 都出問題，還有就是 code highlight 的 syntax 也不同，還有修補以前不愛用標點符號的文章，於是我每天花一點時間改個十多篇，過了幾個禮拜終於改完了 QQ。

domain name......，決定改成 carlcarl.me！原本是 carlcarl.tw，後來覺得前者比較順眼，於是就決定換掉了，以後可能就要跟這個 carlcarl.tw 說再見了。

接下來是選擇要把 blog 放哪裏，其實也想了很久，最後還是決定放在 github 上，放的方式很簡單，用 github page 的方式丟上去就可以了，另外再把 domain name 設定的部分用一用，前面再放個 cloudflare，就沒啥問題哩。

下面是一些我找資料看到的網址，這些都可以參考看看：

[Pelican Guide - Moving From WordPress and Initial Setup][]  
[WordPress to Pelican][]  
[How I Migrated my Wordpress Blog to a Static Site][]  
[Migrating to Pelican - Extracting WordPress Data][]  
[嘗試一下 Pelican][]  
[網誌搬家！改用 Pelican + GitHub Pages][]  
[博客诞生记:基于GitHub+Pelican创建博客的整个过程][]  
[pelican settings][]  
[pelican-themes][]  
[Import from other blog software][]  
[pelican-themes][]  


[wordpress]: http://tw.wordpress.org
[pelican]: https://github.com/carlcarl/pelican/tree/support-post-id
[fork]: https://github.com/carlcarl/pelican/tree/support-post-id
[cloudflare]: https://www.cloudflare.com
[Pelican Guide - Moving From WordPress and Initial Setup]: http://www.macdrifter.com/2012/08/pelican-guide-moving-from-wordpress-and-initial-setup.html
[WordPress to Pelican]: http://kevin.deldycke.com/2013/02/wordpress-to-pelican/
[How I Migrated my Wordpress Blog to a Static Site]: http://jamesmurty.com/2013/05/23/migrate-wordpress-blog-to-static-site/
[Migrating to Pelican - Extracting WordPress Data]: http://www.macdrifter.com/2012/07/migrating-to-pelican-extracting-wordpress-data.html
[嘗試一下 Pelican]: http://farseerfc.github.io/try-pelican.html
[網誌搬家！改用 Pelican + GitHub Pages]: http://jsliang.com/blog/2013/02/moving-to-pelican-hosting-on-github-pages.html
[博客诞生记:基于GitHub+Pelican创建博客的整个过程]: http://frantic1048.com/bo-ke-dan-sheng-ji-ji-yu-githubpelicanchuang-jian-bo-ke-de-zheng-ge-guo-cheng.html
[pelican settings]: http://docs.getpelican.com/en/latest/settings.html
[pelican-themes]: http://docs.getpelican.com/en/latest/pelican-themes.html
[Import from other blog software]: http://docs.getpelican.com/en/3.3.0/importer.html
[pelican-themes]: https://github.com/getpelican/pelican-themes

