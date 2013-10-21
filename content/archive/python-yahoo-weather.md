Title: Python Yahoo weather
Date: 2013-07-16 18:30
Author: carlcarl
Post_ID: 1212
Category: python
Tags: weather, yahoo, yql
Slug: python-yahoo-weather

實際做起來不難，是說弄完才發現有 [yweather][] 這個可以用囧。

<!--more-->

首先到 [YQL][] 這邊下 query，這邊可以參考[這篇][]最下面的兩種 query
方法。格式可以選 JSON 然後把 callback 名稱拿掉，下完 query
就可以產生一段網址，以新竹的例子來說就是:

	:::text
    http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20location%3D%22TWXX0009%22%20and%20u%3D%22c%22&format=json&diagnostics=true&callback= 

接著用 python 處理一下就可以了：

	::python
    import json
    import requests

    url = 'blahblah..'
    raw_data = requests.get(url)
    json_data = json.loads(raw_data)
    print(json_data)

`requests` 很方便，不過不是內建的，要先安裝：`pip install requests`，最後得到的
`json_data` 就是天氣資料。

  [yweather]: https://pypi.python.org/pypi/yweather/0.1
  [YQL]: http://developer.yahoo.com/yql/console/
  [這篇]: http://my.opera.com/weiyu/blog/2012/04/08/yql-yahoo
