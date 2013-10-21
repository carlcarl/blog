Title: Django ajax file upload
Date: 2012-04-03 21:56
Author: carlcarl
Post_ID: 342
Category: js, python
Tags: ajax, ajaxfileupload, csrf, django, python
Slug: django-ajax-file-upload

原本以為很簡單可以完成的東西，結果花了我不少時間解決囧。

Ajax 檔案上傳我用的是 [ajaxfileupload][] 這個 jQuery 套件，問題在於
Django 會檢查 csrf 的問題，如果我不在 settings.py 裡的
`MIDDLEWARE_CLASSES` 加上
`django.middleware.csrf.CsrfViewMiddleware`，上傳會出現 syntax
error，如果我加上了，則是會跟我說 csrf token 找不到。

後來找到的解決辦法就是在 views.py 裡拿到 csrf token 並傳到 template
中，然後再改寫 ajaxfileupload.js 中的內容，讓它支援傳送參數，接著將 csrf
token 當作參數傳送回去就 OK 了。

​1. 在 settings.py 中確認 `django.middleware.csrf.CsrfViewMiddleware` 是否在
 `MIDDLEWARE_CLASSES` 中，沒有的話就加進去，如以下範例：

	:::python
	MIDDLEWARE_CLASSES = (
    	'django.middleware.common.CommonMiddleware',
    	'django.contrib.sessions.middleware.SessionMiddleware',
    	'django.contrib.auth.middleware.AuthenticationMiddleware',
    	'django.middleware.csrf.CsrfViewMiddleware',
	)
	

​2. 在你的 views.py 中 `import get_token` ，然後將拿到的 token 傳到
template，以下是個簡單的範例：

	:::python
	from django.shortcuts import render_to_response
	from django.middleware.csrf import get_token
	from django.template import RequestContext

	def test(request):
    	csrf_token = get_token(request)
    	return render_to_response('test.html',
            	{
                	'csrf_token': csrf_token,
            	},
            	context_instance = RequestContext(request)
    	)
    	

​3. 改寫 ajaxfileupload.js  
這裡可以參考[這邊][]的「三、支持額外參數」的部份。  
4. 在 call ajaxfileupload 的 function 加上 csrf token 的參數

	:::javascript
	secureuri:false,
	data: {
    	'csrfmiddlewaretoken': '{{ csrf_token }}',
	},
	fileElementId:'fileToUpload',
	dataType: 'json',


​5. 大功告成！

  [ajaxfileupload]: http://www.phpletter.com/Our-Projects/AjaxFileUpload/
  [這邊]: http://www.linuxfly.org/post/519/
