Title: Ajax Request Header
Date: 2015-02-22 23:00
Author: carlcarl
Post_ID: 1411
Category: js
Tags: ajax
Slug: ajax_request_header

小筆記一下～。

看了一下 browser 丟出的 request header 有包含 `X_REQUESTED_WITH`，不過在 Server side 收到的會在前面加個 `HTTP_`，所以會變成 `HTTP_X_REQUESTED_WITH`。值的話則是 `XMLHttpRequest`。

Ref:

* [Detect an ajax request]


[Detect an ajax request]: http://stackoverflow.com/questions/17816515/detect-an-ajax-request