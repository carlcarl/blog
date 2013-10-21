Title: brunch watch stylesheet dependency
Date: 2013-09-09 02:10
Author: carlcarl
Post_ID: 1302
Category: css, js
Tags: grunch
Slug: brunch-watch-stylesheet-dependency

之前在改網站的 style，明明套用了 brunch，但是修改後，卻沒辦法自動產生
build 好的 css，這個問題一直困擾我很久，每次都要重新跑一次
`brunch watch --server` 實在是很不爽，今天晚上剛好有一點時間就來修了。

<!--more-->

網站是用 `less`，然後有一個主要的 less 檔來 `@import` 其他在 `less`
資料夾底下的 .less 檔，目錄架構大概像底下這樣：

	:::text
    ├── less
    │   ├── archives.less
    │   ├── index.less
    └── less_proxy.less

然後 `config.ls` (這邊是用 livescript) 裡對應的設定部分：

	:::livescript
    stylesheets:
      joinTo:
        'css/app.css': /^app\/styles\/\w+\.less/

(這邊在 watch 的時候只監看 `less_proxy.less` 有沒有變動再做 join，所以改
`less` 底下的檔案並不會有反應)

下面就直接給解法了，首先把 `less` 資料夾改名為 `_less`，接著在
`config.ls`，加上：

	:::livescript
    conventions:
        ignored: /^app\/styles\/_less/

這個設定會將 `_less` 底下的檔案都加入 watch，但是不會再額外
compile。這邊要注意的是資料夾必須是 `_` 開頭的，不然還是不行。

參考資料：  
[Stylesheet dependency compilation/watching][]  
[brunch config doc][]

  [Stylesheet dependency compilation/watching]: https://github.com/brunch/brunch/issues/681
  [brunch config doc]: https://github.com/brunch/brunch/blob/stable/docs/config.md
