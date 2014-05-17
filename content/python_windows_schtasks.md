Title: Python Windows schtasks
Date: 2014-05-18 02:00
Author: carlcarl
Post_ID: 1396
Category: python
Tags: python, windows
Slug: python_windows_schtasks


最近在找 Windows 上有啥功能是像 Linux 上的 crontab 一樣可以設定週期性的工作，後來找到有 command line 版本的 `schtasks` 可以用。這邊我主要想做的事是透過執行 bat 檔案，將我要的執行檔加入 daily job 裡，同樣的也可以透過另一個 bat 檔案簡單移除掉這個 job，下面是我的程式範例:

## 加入 bat 檔案目錄下的某個執行檔到 daily task 中

	:::bat
    @SET file_dir=%~dp0
    @SET exec_file=%file_dir%a.exe
    schtasks /CREATE /TN "my_task" /SC DAILY /TR "%exec_file% -a" /ST 14:00
    pause

這邊的 `%~dp0` 表示為這個 bat 檔案的絕對路徑，`a.exe` 是我要執行的執行檔，將路徑和執行檔串起來後，利用 `schtasks` 加入，`/TN` 是 task name，必須是唯一，不可與其他 task 的一樣，`/SC DAILY` 表示為 daily job，`/TR` 是要執行的執行檔，參數的部分可以直接接在後面，`/ST` 表示何時執行，這裡的時間是設定下午兩點。然後最後記得加 `pause`，避免視窗出來後馬上就消失。

## 移除 task

    :::bat
    schtasks /DELETE /TN "my_task"
    pause

由於 task name 是唯一，所以刪除的話，只要指定 task name 就可以簡單的刪除掉 task 了。



參考資料：  
[How to Create, Modify and Delete Scheduled Tasks from the Command Line]  
[How do I create a scheduled task, via command line, which includes advanced options]  
[How to get the path of the batch script in Windows?]  
[How to delete scheduled task from command line without confirmation? (schtasks delete)]


[How to Create, Modify and Delete Scheduled Tasks from the Command Line]: http://www.howtogeek.com/51236/how-to-create-modify-and-delete-scheduled-tasks-from-the-command-line/
[How do I create a scheduled task, via command line, which includes advanced options]: http://stackoverflow.com/questions/3016452/how-do-i-create-a-scheduled-task-via-command-line-which-includes-advanced-opti
[How to get the path of the batch script in Windows?]: http://stackoverflow.com/questions/3827567/how-to-get-the-path-of-the-batch-script-in-windows
[How to delete scheduled task from command line without confirmation? (schtasks delete)]: http://serverfault.com/questions/319701/how-to-delete-scheduled-task-from-command-line-without-confirmation-schtasks-d#_=_






