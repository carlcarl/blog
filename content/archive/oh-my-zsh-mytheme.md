Title: oh my zsh: my theme
Date: 2012-05-06 00:34
Author: carlcarl
Post_ID: 414
Category: linux
Tags: oh-my-zsh, zsh
Slug: oh-my-zsh-mytheme

![zsh][]

在之前[安裝完 zsh 和 oh my zsh][]之後，就先來設定我的 theme 啦。

但是因為看了老半天沒有一個 theme
符合我的需求，所以我就自己另外弄了一個，大致是從 muse 這個 theme
去改的，另外在搭配部份其他 theme 中的一些小元件。這個 theme 包含了基本的
host name、時間、和 進 git repo 會有的提示，git repo
的狀態包含多種圖示，所以很容易可以看出 repo 中有什麼改變。

 

我的 theme 可以在這邊下載：[載點][]。（或是可以直接 clone 我的
[repo][]）

把這個檔案下載下來存成 `carlcarl.zsh-theme` 之後，放到
`~/.oh-my-zsh/themes/` 底下，修改 `~/.zshrc` 中的 `ZSH_THEME`：

	:::bash
    ZSH_THEME="carlcarl"

---

改完之後，重開
terminal，不過你可能會發現顏色不太一樣，這部份還需要透過設定 terminal
才行，terminal 配色可以參考[這個網站][]。以下這邊是他建議的色碼：

	:::text
    Black: 0, 0, 0
    Red: 229, 34, 34
    Green: 166, 227, 45
    Yellow: 252, 149, 30
    Blue: 196, 141, 255
    Magenta: 250, 37, 115 # 這個我是用 199, 32, 80 這組，我自己感覺是有比較好看XD
    Cyan: 103, 217, 240
    White: 242, 242, 242

---
 

以一般 terminal 來當作範例，可以從 Edit->Profile Preferences->Colors
這邊來選擇顏色

![terminal color][]


---


點一個顏色進去，就可以進行修改

![terminal color][1]

 

接著就把上面那個色碼表分別填入到對應顏色的 Red, Green, Blue
欄位裡，這邊可能會有點難懂，簡單講，你可以根據你現在 terminal
提示字元的樣子和顏色去對應設定中的顏色來做修改。

Theme 的設定大概就到這邊告一段落，本來還想加個有趣的表情符號到提示字元裡，不過想說這樣太花了，所以就算了XD。oh-my-zsh
另外還有 plugin 的部份我還沒試過，有空再來試試看唄。

附帶一提，terminal 我本來是使用 [guake][]，但是現在因為用 F12
開啟之後，會有亂碼出現，所以我後來改用 [yakuake][] 了。

 

參考網址：  
<http://stevelosh.com/blog/2010/02/my-extravagant-zsh-prompt/>  
<http://forrst.com/posts/Oh_my_zsh_iTerm2_Nice_Colors_git_hg_suppo-1Ct>

  [zsh]: http://i.imgur.com/abOdnAul.png
    "Selection_61b4e7"
  [安裝完 zsh 和 oh my zsh]: http://blog.carlcarl.tw/410/ubuntu%e5%ae%89%e8%a3%9d-oh-my-zsh
    "ubuntu 安裝 oh my zsh"
  [載點]: %20http://dl.dropbox.com/u/4413406/carlcarl.zsh-theme
  [repo]: https://github.com/carlcarl/oh-my-zsh
  [這個網站]: http://stevelosh.com/blog/2009/03/candy-colored-terminal/
  [terminal color]: http://i.imgur.com/tkCwL9x.png
    "Selection_4fadd9"
  [1]: http://i.imgur.com/9wkt1p3.png
    "Selection_fd4dd8"
  [guake]: http://projects.comum.org/guake
  [yakuake]: http://yakuake.kde.org/
