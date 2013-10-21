Title: tree command exclude multiple direcories
Date: 2013-07-14 17:57
Author: carlcarl
Post_ID: 1194
Category: Mac
Tags: tree
Slug: tree-command-exclude-multiple-direcories

### 安裝

一般 Linux 好像都會有裝，不過 OSX 上預設沒有，下個 `brew install tree`
裝就 OK 了。

### 使用

man 了一下，用 `-I pattern` 就可以略過資料夾，那如果有多個呢？本來猜是
`-I pattern1 pattern2`，結果不是囧，`-I pattern1 -I pattern2`
也不是囧。後來才看到[用法][]應該是 `-I pattern1|pattern2` 才對 orz。

  [用法]: http://unix.stackexchange.com/questions/61074/tree-command-for-multiple-includes-and-excludes
