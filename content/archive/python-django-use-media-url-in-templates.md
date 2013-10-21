Title: Python Django use MEDIA_URL in templates
Date: 2011-03-19 19:36
Author: carlcarl
Post_ID: 9
Category: python
Slug: python-django-use-media-url-in-templates

在 settings 裏面已經設好 `MEDIA_URL`了，可是一直不知道怎麼在 templates 中使用  
像是:

	:::html
	href="{{ MEDIA_URL }}styles/base.css"

 

後來看到一篇有說在 `retrun render_to_response` 這邊需要修改，改成這樣, 把第三個參數加上 `context_instance` 這句:

	:::python
	return render_to_response('base/index.html', {}, context_instance =
		RequestContext(request))
 

這樣就可以使用了~~。
