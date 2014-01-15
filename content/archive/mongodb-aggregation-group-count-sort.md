Title: mongodb aggregation group count sort
Date: 2012-09-14 05:05
Author: carlcarl
Post_ID: 645
Category: database
Tags: mongodb
Slug: mongodb-aggregation-group-count-sort

感覺不是很難的 query，想說用 mongodb aggregation 來解決，不過查資料查了好久才知道怎麼用。  
以 sql 來說的話，我是要對某個欄位作 group by，分類完之後再對分類完的欄位作 count，算完之後再根據 count 的數字作 sort。下面這段是 MongoDB 中的用法：

	:::javascript
    db.mytable.aggregate({ $group:{ _id: "$b_cd", num: {$sum:1} }}, {$sort:{num:1}} );

`$b_cd` 是我要分類的欄位，`num` 是各分類欄位的數目，這邊利用 `$sum`
作累加，接著再用 `$sort` 對 num 作排序。

中間我卡很久的原因是因為 syntax
搞錯（**大括弧的位置要注意！！！！！**），不應該把 `$group` 和 `$sort`
放在同一個 object ，而是要分開來分別當作 `aggregate` 的參數才對，有幾個
operator ($project, $group, $sort...,etc.) ，`aggregate`
就會有幾個參數，另外要記得就是這些參數要**分別用大括弧各包成
object** 才行。

另外再補充一下另一個寫法，跟上面的是一樣的意思，我比較喜歡上面的寫法就是了：

	:::javascript
    db.runCommand( { aggregate: "mytable", pipeline: [ {$group: {_id:"$b_cd", num:{$sum:1}}}, {$sort:{num:1}} ] });

參考網址：  
<http://docs.mongodb.org/manual/applications/aggregation/>  
<http://docs.mongodb.org/manual/reference/aggregation/>
