Title: Python FTP Download Percent
Date: 2015-05-06 23:00
Author: carlcarl
Post_ID: 1425
Category: python
Tags: python, ftp
Slug: python_ftp_download_percent



本來是別人寫的一個 ftp download python script，因為不知道到底是不是有在下載中(?)，所以我多加了一個顯示現在 download 幾 percent 的 function:

	:::python
    def ftp_get(src_dir, name, dst_dir):
        def ftp_callback(chunk, file_size, dst_file):
            if not hasattr(ftp_callback, "progress_size"):
                ftp_callback.progress_size = 0
            if not hasattr(ftp_callback, "progress_percent"):
                ftp_callback.progress_percent = 0
            dst_file.write(chunk)
            ftp_callback.progress_size += len(chunk)
            tmp = ftp_callback.progress_size * 100 / file_size
            if ftp_callback.progress_percent != tmp:
                ftp_callback.progress_percent = tmp
                sys.stdout.write('\r%s' % str(ftp_callback.progress_percent) + '%')
                sys.stdout.flush()
        ftp = ftplib.FTP(ftp_url)
        ftp.login(ftp_account, ftp_password)
        ftp_dir = ftp_root + src_dir
        ftp.cwd(ftp_dir)
        ftp_file = ftp.nlst(name)
        if len(ftp_file) != 1:
            print "Confused with ftp files, please check server site"
            exit(-1)
        dst_path = "%s/%s" % (dst_dir, ftp_file[0])
        file_size = ftp.size(ftp_dir + '/' + ftp_file[0])
        dst_file = open(dst_path, "wb")
        try:
            print "Downloading " + ftp_file[0]
            ftp.retrbinary('RETR %s/%s' % (ftp_dir, ftp_file[0]), lambda chunk: ftp_callback(chunk, file_size, dst_file))
        except Exception, e:
            print "ERROR: %s" % e
            os.unlink(dst_path)
        else:
            print ''
            print "Download %s success" % ftp_file[0]


關鍵點在於 `ftp.retrbinary('RETR %s/%s' % (ftp_dir, ftp_file[0]), lambda chunk: ftp_callback(chunk, file_size, dst_file))` 的最後一個參數，是一個 callback function，接受一個參數為這次 download 的 chunk，chunk 是一個檔案的其中一小塊部分，每次在 download 完一個 chunk 後就會自動呼叫這個 function，所以可以先用 `file_size = ftp.size(ftp_dir + '/' + ftp_file[0])` 拿到檔案的總大小，然後在 callback 中用 `len(chunk)` 算這次拿到的 chunk 大小，做累加就可以算出現在 download 到幾 percent 了。累計的部分用 function 的 attribute 來做累加，算是一個小 tricky 的地方。percent 輸出的部分則用 `sys.stdout.write`，這樣才能用 `\r` 回到一行的最開始，並把這一行洗掉。



Ref:

* [Pass a value to the ftp.retrbinary callback]
* [What is the Python equivalent of static variables inside a function?]
* [Print in one line dynamically]

[Pass a value to the ftp.retrbinary callback]: http://stackoverflow.com/questions/12060033/pass-a-value-to-the-ftp-retrbinary-callback
[What is the Python equivalent of static variables inside a function?]: http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
[Print in one line dynamically]: http://stackoverflow.com/questions/3249524/print-in-one-line-dynamically