Title: Restart uwsgi using git push
Date: 2014-05-05 21:30
Author: carlcarl
Post_ID: 1394
Category: linux
Tags: uwsgi,python
Slug: restart_uwsgi_using_git_push



因為一 push 完都要 ssh 進去重開 uwsgi server，實在很麻煩，所以 google 了一下有沒有什麼好的做法，雖然說用 [fabric] 進去下指令也是可以，不過想看看有沒有利用 git push 的 hook 來做的例子。

## 如何 restart uwsgi
查了一些資料，一般要 restart uwsgi 就要 root 權限，不過可以在 uwsgi 的設定檔中設定 `touch-reload` 這個參數，以我的 .ini 設定格式的話就是設 `touch-reload = /your_path/reload` 設完這個路徑後，一旦你在 `/your_path/` 底下 touch 了一個檔案叫做 `reload`，uwsgi 就會跟著 reload，相當方便，也不需要管什麼權限問題。

## 加進 git hook 裡

在 project 的 `.git/hooks/post-receive` 或 `.git/hooks/post-update` 裡，加入那段 touch 的指令，記得要在更新 git repo 之後做就可以了。


參考網址：  
[How do I make uWSGI restart when a Python script is modified?](http://serverfault.com/questions/411362/how-do-i-make-uwsgi-restart-when-a-python-script-is-modified)  
[The Art of Graceful Reloading](http://uwsgi-docs.readthedocs.org/en/latest/articles/TheArtOfGracefulReloading.html)  


[fabric]: http://www.fabfile.org
