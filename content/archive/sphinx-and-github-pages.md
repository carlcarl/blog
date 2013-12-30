Title: sphinx and github pages
Date: 2013-10-04 21:26
Author: carlcarl
Post_ID: 1365
Category: python, 版本管理
Tags: github, sphinx
Slug: sphinx-and-github-pages

就之前產生的 sphinx document，接下來是如何 deploy 到 github page 上。

這個文章是根據 [Documenting python code using sphinx and github][] 和
[Sphinx documentation on GitHub][]
整理而成的，兩個地方的資料都不錯，不過都沒有很完美，所以就寫了這篇。

建立 github page repo
---------------------

這邊看到大部分的做法都是直接在 project 根目錄下直接開另外一個
branch，不過我後來在上面連結看到一個不錯的做法，就是直接把 branch 建立在
subdirectory 下。首先先在 project 根目錄下建立一個 gh-pages 的資料夾：

	:::bash
    mkdir gh-pages

接著利用 `git-new-workdir` 這個指令建立一個 subdirectory，這個指令一般在
`/usr/local/share/git-core/contrib/workdir/git-new-workdir`，在 Mac
下需要另外用 `brew` 裝 `git`，位置會放在
`/usr/local/Cellar/git/1.8.4/share/git-core/contrib/workdir/git-new-workdir`，`1.8.4`
要換成你現在的 git 版本，至於 Xcode 本身雖然也有裝
git，但是我就找不到它的 `git-new-workdir` 在哪了，然後可以自己建個 link
來用：

	:::bash
    sudo ln -s /usr/local/Cellar/git/1.8.4/share/git-core/contrib/workdir/git-new-workdir /usr/local/bin/git-new-workdir

然後繼續下面的步驟：

	:::bash
    git-new-workdir . gh-pages/html

接著進入資料夾並 checkout 一個新的 branch：

	:::bash
    cd gh-pages/html
    git checkout --orphan gh-pages

將裡面的東西都清光光：

	:::bash
    git rm -rf .

產生 sphinx document
--------------------

回到 project 根目錄下的 doc 下：

	:::bash
    cd ../../doc/

修改 Makefile：

	:::makefile
    BUILDDIR      = _build

改成

	:::makefile
    BUILDDIR      = ../gh-pages/html

這樣所有的輸出都會在 `gh-pages/html/` 底下。但是這樣 sphinx 的 html
變成會在 `gh-pages/html/` 底下再建一個 `html` 資料夾，所以 Makefile
還有一個地方要改：

	:::makefile
    html:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
    @echo
    @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

改成

	:::makefile
    html:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
    @echo
    @echo "Build finished. The HTML pages are in $(BUILDDIR)."

這樣它就會把 html 的部分直接輸出到 `gh-pages/html/` 底下，接著輸入
`Make html` 產生網頁。

github page push
----------------

先移到 gh-pages/html 下：

	:::bash
    cd ../gh-pages/html

這邊還有一個地方要注意，那就是 github 預設的 site 架構 (Jekyll)，會忽略
`_` 開頭的資料夾，所以要用個檔案來告訴 github 不要用這種架構：

	:::bash
    touch .nojekyll

接著加入所有檔案到 git 中， commit 並 push 上去就完成了：

	:::bash
    git add .
    git commit -m "First commit"
    git push -u origin gh-pages

參考資料
--------

[Bypassing Jekyll on GitHub Pages][]  
[git-new-workdir][]  
[git-new-workdir が便利][]

  [Documenting python code using sphinx and github]: http://raxcloud.blogspot.tw/2013/02/documenting-python-code-using-sphinx.html
  [Sphinx documentation on GitHub]: http://datadesk.latimes.com/posts/2012/01/sphinx-on-github/
  [Bypassing Jekyll on GitHub Pages]: https://github.com/blog/572-bypassing-jekyll-on-github-pages
  [git-new-workdir]: http://nuclearsquid.com/writings/git-new-workdir/
  [git-new-workdir が便利]: http://subtech.g.hatena.ne.jp/secondlife/20121207/1354854068
