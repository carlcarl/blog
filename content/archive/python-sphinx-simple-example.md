Title: Python Sphinx simple example
Date: 2013-10-02 02:32
Author: carlcarl
Post_ID: 1331
Category: python
Tags: python, sphinx
Slug: python-sphinx-simple-example

查了很多資料，遇到一堆鬼打牆問題，終於弄成我要的樣子了，不過其實也沒有加多少東西，只是基本的設定一直搞不定
orz。

<!--more-->

* * * * *

下面是一開始的 project 結構，接著會利用 `sphinx` 在根目錄下建立 `doc`
這個目錄：

Project 目錄架構
----------------

	:::text
    .
    ├── CHANGES.txt
    ├── MANIFEST.in
    ├── README.rst
    ├── test
    │   ├── __init__.py
    │   └── test.py
    ├── requirements.txt
    └── setup.py

* * * * *

安裝並產生設定
--------------

首先先安裝 `sphinx`(ex: `pip install sphinx`)，接著在 project
根目錄下輸入 `sphinx-quickstart`，設定步驟如下：

	::text
	Welcome to the Sphinx 1.1.3 quickstart utility.
	
	Please enter values for the following settings (just press Enter to
	accept a default value, if one is given in brackets).
	
	Enter the root path for documentation.
	> Root path for the documentation [.]: doc
	
	You have two options for placing the build directory for Sphinx output.
	Either, you use a directory "_build" within the root path, or you separate
	"source" and "build" directories within the root path.
	> Separate source and build directories (y/N) [n]:
	
	Inside the root directory, two more directories will be created; "_templates"
	for custom HTML templates and "_static" for custom stylesheets and other static
	files. You can enter another prefix (such as ".") to replace the underscore.
	> Name prefix for templates and static dir [_]:
	
	The project name will occur in several places in the built documentation.
	> Project name: test
	> Author name(s): carlcarl
	
	Sphinx has the notion of a "version" and a "release" for the
	software. Each version can have multiple releases. For example, for
	Python the version is something like 2.5 or 3.0, while the release is
	something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
	just set both to the same value.
	> Project version: 0.0.1
	> Project release [0.0.1]:
	
	The file name suffix for source files. Commonly, this is either ".txt"
	or ".rst".  Only files with this suffix are considered documents.
	> Source file suffix [.rst]:
	
	One document is special in that it is considered the top node of the
	"contents tree", that is, it is the root of the hierarchical structure
	of the documents. Normally, this is "index", but if your "index"
	document is a custom template, you can also set this to another filename.
	> Name of your master document (without suffix) [index]:
	
	Sphinx can also add configuration for epub output:
	> Do you want to use the epub builder (y/N) [n]:
	
	Please indicate if you want to use one of the following Sphinx extensions:
	> autodoc: automatically insert docstrings from modules (y/N) [n]: y
	> doctest: automatically test code snippets in doctest blocks (y/N) [n]:
	> intersphinx: link between Sphinx documentation of different projects (y/N) [n]:
	> todo: write "todo" entries that can be shown or hidden on build (y/N) [n]:
	> coverage: checks for documentation coverage (y/N) [n]:
	> pngmath: include math, rendered as PNG images (y/N) [n]:
	> mathjax: include math, rendered in the browser by MathJax (y/N) [n]:
	> ifconfig: conditional inclusion of content based on config values (y/N) [n]:
	> viewcode: include links to the source code of documented Python objects (y/N) [n]:
	
	A Makefile and a Windows command file can be generated for you so that you
	only have to run e.g. `make html' instead of invoking sphinx-build
	directly.
	> Create Makefile? (Y/n) [y]:
	> Create Windows command file? (Y/n) [y]: n
	
	Creating file doc/conf.py.
	Creating file doc/index.rst.
	Creating file doc/Makefile.
	
	Finished: An initial directory structure has been created.
	
	You should now populate your master file doc/index.rst and create other documentation
	source files. Use the Makefile to build the docs, like so:
	   make builder
	where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


比較要注意的是一開始的路徑輸入 `doc` 表示要在當前目錄的 `doc`
底下建立文件。 `autodoc` 這個記得選 `y`。因為不是用 Windows，所以
`Windows command file` 這個選項我就選 `n` 了。輸入完後會建立 `doc`
這個目錄。

* * * * *

產生 API 設定文件
-----------------

在 project 根目錄下輸入：`sphinx-apidoc -o doc/api test`，會將 API
設定文件放到 `doc/api` 底下。

* * * * *

修改設定檔
----------

接著進入 `doc` 這個目錄 (`cd doc`)，修改 `index.rst` 以及 `conf.py`。

### conf.py

首先是 `conf.py`。在 `import sys, os` 下面加上
`sys.path.insert(0, os.path.abspath('..'))` 即可，這邊是將 project 的
path 加入 `sys.path` 當中，不然 sphinx 會找不到。

### index.rst

這邊是我整個設定檔：

	:::restructuredtext
    .. test documentation master file, created by
       sphinx-quickstart on Wed Oct  2 00:41:51 2013.
       You can adapt this file completely to your liking, but it should at least
       contain the root `toctree` directive.

    Welcome to test's documentation!
    ======================================

    :doc:`API Documentation <api/test>`

    .. include:: ../README.rst


    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

    .. toctree::
       :hidden:

       api/modules

`API Documentation` 這段是程式的 API 連結。如果在 project 根目錄有
`README.rst` 的話，可以如上面這樣 include 進來。最下面的 `toctree` 到
`api/modules` 這段是因為 `sphinx-apidoc` 會產生一個 `modules.rst`
檔案，如果沒加到 `toctree` 會有警告，這邊就把它加進來，然後設隱藏，至於
`toctree` 是啥，可以參考 [這個連結][]，算是一個目錄架構這樣。

* * * * *

產生 html
---------

在 `doc` 底下輸入 `make html`，產生的 html 會放在 `_build/html`
下，到這裡就算大功告成了。

* * * * *

其他遇到的問題
--------------

### 為啥不在 rst 檔案中加入 automodule 的設定，而是用 `sphinx-apidoc` 產生 API 文件？

因為 automodule 做不到 recursive 尋找 submodule。相關討論連結如下：

[Automatically Generating Documentation for All Python Package Contents][]  
[Sphinx autodoc is not automatic enough][]  
[Sphinx, using automodule to find submodules][]

### sphinx-build option -b not recognized

這個錯誤的直接原因是因為 module 裡面有用 `argparse` 這類的 module，然後
`sphinx-build` 執行時有 `-b` 這個參數，傳進去之後就炸了。但是一般來說
module 裡用 `argparse`，本身不是個問題，問題是 sphinx
為啥執行了這段程式，有幾個可能的原因：

1.  module 裡沒用 `if __name__ == '__main__':` 這段，而是直接執行。
2.  sphix-apidoc 讀取的目錄裡包含 `setup.py`，即使 module
    裡有用上面的判斷包起來，還是會全執行。

所以我一開始才會用 `sphinx-apidoc -o doc/api test` 而不是
`sphinx-apidoc -o doc/api .`，就是要避開
`setup.py`。下面是找到的相關連結：

[Is OptionParser in conflict with sphinx?][]  
[How should I solve the conflict of OptionParser and sphinx-build in a large project?][]  
[Re: sphinx-dev option -b not recognized?][]

### WARNING: document isn't included in any toctree

參閱 [Location of Sphinx sources for my notes][]

* * * * *

參考資料
--------

[Documenting python code using sphinx and github][]  
[sphinx-build fail - autodoc can't import/find module][]  
<http://scienceoss.com/minimal-sphinx-setup-for-autodocumenting-python-modules/>  
[Example: PyMongo documentation][]

  [這個連結]: http://sphinx-doc.org/concepts.html
  [Automatically Generating Documentation for All Python Package Contents]: http://stackoverflow.com/questions/4616693/automatically-generating-documentation-for-all-python-package-contents
  [Sphinx autodoc is not automatic enough]: http://stackoverflow.com/questions/2701998/sphinx-autodoc-is-not-automatic-enough
  [Sphinx, using automodule to find submodules]: http://stackoverflow.com/questions/11508290/sphinx-using-automodule-to-find-submodules
  [Is OptionParser in conflict with sphinx?]: http://stackoverflow.com/questions/6912025/is-optionparser-in-conflict-with-sphinx
  [How should I solve the conflict of OptionParser and sphinx-build in a large project?]: http://stackoverflow.com/questions/14769962/how-should-i-solve-the-conflict-of-optionparser-and-sphinx-build-in-a-large-proj
  [Re: sphinx-dev option -b not recognized?]: http://www.mail-archive./om/sphinx-dev@googlegroups.com/msg05521.html
  [option -b not recognized?]: https://groups.google.com/forum/#!topic/sphinx-users/cOCOVCO9NbQ
  [Location of Sphinx sources for my notes]: http://stackoverflow.com/questions/1690757/location-of-sphinx-sources-for-my-notes
  [Documenting python code using sphinx and github]: http://raxcloud.blogspot.tw/2013/02/documenting-python-code-using-sphinx.html
  [sphinx-build fail - autodoc can't import/find module]: http://stackoverflow.com/questions/10324393/sphinx-build-fail-autodoc-cant-import-find-module
  [Example: PyMongo documentation]: http://api.mongodb.org/python/current/
