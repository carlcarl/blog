Title: OSX Mavericks Beta header file position
Date: 2013-07-12 02:15
Author: carlcarl
Post_ID: 1120
Category: Mac
Slug: osx-mavericks-betaheader-file-position

Beta 版的 header file 位置有些不同，看到幾個地方都傳出災情：

-   [gpg-agent: Set correct stdint.h header path for Mac OSX Mavericks][]
-   [The gem doesn't yet build in Mavericks][]
-   [Installation fails on OS X Mavericks][]

<!--more-->

原本的 `/usr/include` 已經不見了，找了一下，位置是在：

    /Applications/Xcode5-DP.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/

如果像是 vim 有 plugin (ex: youcompleteme) 需要指定 header file
位置的話，可以另外把這個位置加上去。

  [gpg-agent: Set correct stdint.h header path for Mac OSX Mavericks]: https://github.com/mxcl/homebrew/pull/20938
  [The gem doesn't yet build in Mavericks]: https://github.com/jfahrenkrug/WWDC-Downloader/issues/5
  [Installation fails on OS X Mavericks]: https://github.com/josegonzalez/homebrew-php/issues/591
