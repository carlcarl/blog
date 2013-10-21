Title: Mac virtualenvwrapper "No module named setuptools" error
Date: 2012-10-22 01:05
Author: carlcarl
Post_ID: 709
Category: Mac, python
Tags: virtualenvwrapper
Slug: mac-virtualenvwrapper-no-module-named-setuptools-error

在 Mac 上安裝 virtualenvwrapper 的時候遇到的錯誤，解決方法：  
<!--more-->  
### 首先先重新安裝 setuptools [載點][] ，下載完執行：

	:::bash
	sudo python ez_setup.py

### 移除 setuptools

	:::bash
	sudo pip uninstall setuptools

### [下載 distribute 套件][] ，解壓縮後進去資料夾執行：

	:::bash
	sudo python distribute_setup.py


到這邊就 OK 了。

參考網址：  

<http://code.doughellmann.com/virtualenvwrapper/issue/158/installing-virtualenvwrapper-on-on-osx-108>

  [載點]: http://peak.telecommunity.com/dist/ez_setup.py
  [下載 distribute 套件]: http://pypi.python.org/pypi/distribute
