Title: Python mocking requests
Date: 2014-04-24 15:00
Author: carlcarl
Post_ID: 1393
Category: python
Tags: python
Slug: python_mocking_requests


查了一下有沒有相關的 library 可以做 web request 的 mocking，後來看到 [httpretty] 這個可以用，除了內建的 `urlopen` 這類以外，也支援 `requests` library，不過有點可惜的是 `httpretty` 不是內建的，所以必須用 `pip` 先安裝來用。它的用法還算簡單，以下是個簡單的例子：

    :::python
    import requests
    import httpretty
    
    @httpretty.activate
    def test_request_new_token():
        data = {}
        headers = []
        token_response = '123'
        
        httpretty.register_uri(
            httpretty.POST,
            "https://api.imgur.com/oauth2/token",
            body=token_response,
            status=200
        )
        response = requests.post(
            'https://api.imgur.com/oauth2/token',
            params=data,
            headers=headers
        )
        assert response.text == token_response
        
 上面的例子，先在 test function 上加入 `httpretty.activate` decorator，接著在 function 裡頭用 `httpretty.register_uri` 去註冊要 mocking 的 http method + url，回傳的資料則指定在 `body` 這個參數，且必須是字串，回傳的 status code 則是指定在 `status` 這個參數。接著可以測試發出的 request 所回傳的 response 是否會和預期的一樣，這邊的 `response.text` 會等於 `token_response`。
 
另外，如果想在同一個 test function 去測試同樣的 http method + url，然後需要回傳不一樣的結果的話，必須在兩個 `register_uri` function 中間呼叫 `httpretty.reset()` 來 cancel 掉之前的 register。 

參考網址:  
[Mocking HTTP requests in python]  


[httpretty]: https://github.com/gabrielfalcao/HTTPretty
[Mocking HTTP requests in python]: http://marekbrzoska.wordpress.com/2013/08/28/mocking-http-requests-in-python/




