Title: python argparse
Date: 2013-01-29 16:50
Author: carlcarl
Post_ID: 772
Category: python
Tags: argparse
Slug: python-argparse

紀錄一些 python argparse module 的使用方法和問題：  
<!--more-->

### 選項的參數為 optional
譬如說 `-f` 這選項允許一個檔案的路徑名稱： `-f test.txt`，如果沒給檔案名稱就預設使用 example.txt：

	:::python
	parser.add_argument('-f', nargs='?', default='example.txt')

### 設定各個選項分開，不允許放在一起使用
如果我希望 `-f` 和 `-b` 只有其中一個能被執行而已的話，這時候要用 `add_mutually_exclusive_group` 產生一個 group ，之後被加入這個 group 的參數就會套用這個分開使用的規則：

	:::python
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f', action='store_true')
	group.add_argument('-b', action='store_true')


### 同上，如果我還想要 `-f` 的選項再另外綁定一個參數 `-u` 的話(就是 `-f` 一定要加上 `-u` 的意思)

這個部份我查了很久，不過似乎找不太到解決的方法，所以我後來改套用 <a href="http://docs.python.org/2/library/argparse.html#sub-commands">subcommand</a> 的作法來實現，然後將原本的第一個選項改成用單字的方式來呈現，例如 `test -f` 改成 `test file` ，簡單說就是像 svn 和 git 的作法。

### 怎麼判斷現在是呼叫哪個 subcommand?

在 `add_subparsers` 的參數裡，指定 `dest` 的值, dest 的值給什麼都可以，不過這樣的話，程式下面的 `args.command` 中的 `command` 也要改成對應的值：

	:::python
	subparsers = parser.add_subparsers(dest='command')
	args = parser.parse_args()
	if args.command == 'list':
    	print('list')


參考網址：  
<http://docs.python.org/2/library/argparse.html>  
<http://www.doughellmann.com/PyMOTW/argparse/>  
<http://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments>  
<http://stackoverflow.com/questions/8250010/argparse-identify-which-subparser-was-used>  
[http://stackoverflow.com/questions/7869345/][]

  [http://stackoverflow.com/questions/7869345/]: http://stackoverflow.com/questions/7869345/how-to-make-python-argparse-mutually-exclusive-group-arguments-without-prefix
