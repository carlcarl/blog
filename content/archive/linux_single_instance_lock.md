Title: Linux Single Instance Lock
Date: 2015-04-15 15:00
Author: carlcarl
Post_ID: 1423
Category: linux
Tags: linux, c
Slug: linux_single_instance_lock


要實作 single instance 有幾種方式:

* file lock
* inet socket lock
* `sem_open` 

參照一些 daemon 的作法，感覺 file lock 較常見。inet socket bind 的作法有點麻煩，因爲還要找個 port 來 bind，所以不考慮，unix socket 大略等同於 file lock 的作法，不過步驟太煩雜，所以也不考慮，semaphore(`sem_open`)的作法看似比較好，因為 lock 是在 kernel 裡做管理，不用另外建 file，不過還是有一些問題在: [How do I recover a semaphore when the process that decremented it to zero crashes?]，一旦出問題就沒有 recover 的辦法，相對來講 file lock 比較算是可以接受的作法，就算出問題，把檔案移除掉就好XD，一般人也不會那麼閒會去動這檔案，所以最後還是決定用 file lock 的作法。

file lock 有幾個 function 可以用:

* fcntl
* flock
* lockf

相關比較可以參考以下連結：

* [Linux下各种编程锁的比较]
* [How to create a single instance application in C or C++]
* [fcntl, lockf, which is better to use for file locking?]


看起來 `flock` 和 `lockf` 有一些小缺點，像是 NFS 的支援性之類的，所以就乾脆用最原始的 `fcntl`。`fcntl` 的 usage 可以參考: 

* [How to lock and unlock pid file with “fcntl()”]
* [man fcntl]
* [linux系统编程之struct flock 结构体]


再來就是 file lock 的 file，裡面要填啥內容，一般是都填 process 的 pid 就是，在弄一些設定的時候也比較不會有問題: [Writing own daemon. systemd error: Failed to read PID from file: Invalid argument]。


Linux lock file 的 path 通常都放在 `/var/run/` 底下，檔案可以命名為 `<your_process>.pid`，`your_process` 改成你的 process 名稱。另外，假如執行這個 process 的 user 不是 root 的話，會有 pid 檔案建立權限的問題，所以可以考慮用 root 執行一個 script，script 裡在 `/var/run/` 下建立一個資料夾，再 `chown` + `chmod` 它，pid file 指定在這個資料夾底下，接著再用 `start-stop-daemon` 加上指定 exec 的 user 的參數來執行 process 就可以了。不過既然要用 `start-stop-daemon` 的話，乾脆 pid file 也給它管理就好啦(好像有點在打自己臉= =|||)，不過 `start-stop-daemon` 也不是每個 Linux distro 都有的樣子。


簡單範例如下:

	:::c
	int write_pid_file()
	{
    	int lock_file = open(PID_FILE_PATH, O_RDWR | O_CREAT | O_TRUNC, 0644);
    	if (lock_file == -1)
        	return ERROR;

    	struct flock fl;
    	fl.l_type = F_WRLCK;
    	fl.l_whence = SEEK_SET;
    	fl.l_start = 0;
    	fl.l_len = 0;

    	if (fcntl(lock_file, F_SETLK, &fl) == -1) {
        	close(lock_file);
        	return ERROR;
    	}

    	char pids[10];
    	snprintf(pids, sizeof(pids), "%d\n", getpid());
    	if ((size_t)write(lock_file, pids, strlen(pids)) != strlen(pids)) {
        	close(lock_file);
        	return ERROR;
    	}
    	return OK;
    }



[How do I recover a semaphore when the process that decremented it to zero crashes?]: https://stackoverflow.com/questions/2053679/how-do-i-recover-a-semaphore-when-the-process-that-decremented-it-to-zero-crashe
[Linux下各种编程锁的比较]: http://blog.csdn.net/qifengzou/article/details/37714025
[How to create a single instance application in C or C++]: https://stackoverflow.com/questions/5339200/how-to-create-a-single-instance-application-in-c-or-c
[fcntl, lockf, which is better to use for file locking?]: https://stackoverflow.com/questions/575328/fcntl-lockf-which-is-better-to-use-for-file-locking
[How to lock and unlock pid file with “fcntl()”]: https://stackoverflow.com/questions/16988256/how-to-lock-and-unlock-pid-file-with-fcntl
[man fcntl]: http://man7.org/linux/man-pages/man2/fcntl.2.html
[Writing own daemon. systemd error: Failed to read PID from file: Invalid argument]: https://unix.stackexchange.com/questions/118132/writing-own-daemon-systemd-error-failed-to-read-pid-from-file-invalid-argumen
[linux系统编程之struct flock 结构体]: http://blog.csdn.net/wallwind/article/details/7816221

