Title: appfog deploy pyramid
Date: 2013-04-14 23:45
Author: carlcarl
Post_ID: 827
Category: python
Tags: appfog, pyramid, python
Slug: appfog-deploy-pyramid

這篇是參考
<http://antoineleclair.ca/2012/08/28/deploying-a-pyramid-app-on-appfog/>
這篇所講的，其實他講的就差不多了，但是漏掉了一些細節，所以幫忙補完一下。  

[appfog][] 的 deploy 相對 [openshift][] 來說，算是簡單很多 (不過
openshift 也有一堆 quickstart 的 github repo 可以直接用就是)，以
[pyramid][] 來講，主要就是在 project 根目錄新增一個 `wsgi.py`
的檔案，內容引用文章連結內的程式：

	:::python
	import os
	from paste.deploy import loadapp

	os.system('python setup.py develop')
	path = os.getcwd()
	application = loadapp('config:appfog.ini', 	relative_to=path)


程式的執行就從這個檔案開始，`appfog.ini` 其實就是原本的
`development.ini` 和 `production.ini`，看有沒有需要另外新增一個檔案針對
appfog 使用，不然用原本的兩個設定檔也是可以。

接下來這段：

	:::python
	if settings.get('appfog') == 'true':
    	engine = appfog_engine(settings)
	else:
    	from sqlalchemy import engine_from_config
    	engine = engine_from_config(settings, 'sqlalchemy.')


這邊 settings 拿 appfog 可以拿到值是因爲他在 `appfog.ini` 裏，加上了
`appfog=true`，所以這邊也要記得。

大致比較要注意的就是這些，另外還有 `requirements.txt` 要弄，DB
設定的部分就從 `os.getenv("VCAP_SERVICES")`裏去讀取就 OK 了。

另外這個是那篇文章作者的 [appfog repo][]，也可以參考看看。

  [appfog]: https://www.appfog.com/
  [openshift]: https://www.openshift.com/
  [pyramid]: http://www.pylonsproject.org/
  [appfog repo]: https://github.com/antoineleclair/OpenCode20121030/tree/master/shout
