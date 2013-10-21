Title: ubuntu install oh my zsh
Date: 2012-05-05 23:41
Author: carlcarl
Post_ID: 410
Category: linux
Tags: oh-my-zsh, zsh
Slug: ubuntu-install-oh-my-zsh

在網路上看到 [oh my zsh][] 這套件，這個套件對 zsh
做了一些客製化，包含很多外掛以及提示字元主題，感覺還滿炫的，所以就想說從
bash 換成 zsh 看看囉。

 

### 首先要先安裝 zsh，因為 zsh 預設在 ubuntu 上是沒有安裝的

	:::bash
	sudo apt-get install zsh

 

### 下載 oh-my-zsh 套件到家目錄底下的 `.oh-my-zsh` 資料夾

	:::bash
	git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
 

### 複製設定檔樣板出來使用

	:::bash
	cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

 

### 改成預設使用 zsh，執行以下指令並輸入你的密碼

	:::bash
	chsh -s /bin/zsh

 

### 開啟 terminal 測試看看

 

下一篇再來講「提示字元主題」調整的部份。

  [oh my zsh]: https://github.com/robbyrussell/oh-my-zsh
