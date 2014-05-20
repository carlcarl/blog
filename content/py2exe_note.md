Title: py2exe note
Date: 2014-05-20 11:30
Author: carlcarl
Post_ID: 1397
Category: python
Tags: py2exe
Slug: py2exe_note


setup.py 簡單範例:

    :::python
    #!/usr/bin/env python
    # encoding: utf-8

    from setuptools import setup
    from setuptools import find_packages
    import py2exe
    assert py2exe

    setup(
        name='<your_package_name>',
        description='<your_package_description>',
        author='<author name>',
        author_email='author email',
        packages=find_packages(),
        license='MIT',
        console=['xxx.py'],
        data_files=[
            'xxx.conf.sample'
        ]
    )

`assert py2exe` 是因為 editor 會警告 `py2exe` import 後沒有使用，所以用個 `assert` trick 來避掉。其他的資訊就看個人要不要加吧。

接下來下指令:

    :::bash
    python setup.py install
    python setup.py py2exe

生出來的 exe 執行檔和附加的 data file 會存到 `dist` 目錄下。

另外要注意的一點是 python 檔案中如果有用到 `__file__` 的話，要換成用 `sys.argv[0]`，不然 exe 執行會說找不到 `__file__`。



參考連結:  
[py2exe 的使用方法 教學]  
[p​y​2​e​x​e​使​用​方​法​详​解]  


[py2exe 的使用方法 教學]: http://ghaouse.blogspot.jp/2011/09/py2exe.html
[p​y​2​e​x​e​使​用​方​法​详​解]: http://wenku.baidu.com/view/7d40634acf84b9d528ea7a5f.html
