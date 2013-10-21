Title: virtualenvwrapper setting
Date: 2012-08-28 00:01
Author: carlcarl
Post_ID: 598
Category: python
Tags: python, virtualenvwrapper
Slug: virtualenvwrapper-setting

最近為了方便，加了幾個 virtualenvwrapper 的設定。  
<!--more-->

### 使用 `mkvirtualenv` 建立 virtualenv 時，自動建立資料夾並移到資料夾位置下。  
在 `~/.virtualenv/postmkvirtualenv`裡加入：

	:::bash
	proj_name=$(echo $VIRTUAL_ENV|awk -F'/' '{print $NF}')

	if [ ! -d "~/Projects/$proj_name" ]; then
    	mkdir ~/Projects/$proj_name
	fi

	if [ "${PWD##*/}" != "~/Projects/$proj_name" ]; then
    	cd ~/Projects/$proj_name
	fi

其中，把 `Projects` 換成你的 project 位置。

***

### 輸入 `workon 你的project` 時，自動切換至 project 位置下。  
    在 `~/.virtualenv/postactivate`裡加入：

	:::bash
	proj_name=$(echo $VIRTUAL_ENV|awk -F'/' '{print $NF}')

	if [ "${PWD##*/}" != "~/Projects/$proj_name" ]; then
    	cd ~/Projects/$proj_name
	fi


### 使用 rmvirtualenv 時自動刪除資料夾  
目前似乎沒辦法（炸），因為在 deactivate 狀態下 `$VIRTUAL_ENV` 是不會有值的，而在 activate 下又不能刪除環境，所以目前看來是無解，只能自己手動刪除了。

參考網址：  
[http://virtualenvwrapper.readthedocs.org/en/latest/tips.html][]  
[http://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv][]

  [http://virtualenvwrapper.readthedocs.org/en/latest/tips.html]: http://http://virtualenvwrapper.readthedocs.org/en/latest/tips.html
  [http://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv]: http://http://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv
