Title: wordpress social share plugin
Date: 2011-11-20 17:34
Author: carlcarl
Post_ID: 76
Category: blog
Tags: plurk, share, social, wordpress
Slug: wordpress-social-share-plugin

![Tweet, Like, Share and Google +1 Option Page][]

轉來 wordpress 之後，為了找社群分享外掛找了好久，最後找到這個[Tweet, Like,
Share and Google +1 Option Page][1] ，他的好處在於：

1.   按鈕大，明顯又好按，圖示也算不錯看

2.  可以自己加按鈕啊～～～，所以我後來自已加了個噗浪的按鈕。沒辦法，wordpress上幾乎沒有噗浪的分享外掛，所以就去這個網頁抓語法，然後搜尋自己想要的噗浪圖示之後，將圖示傳到自己的空間，並加到這個外掛裡。

3.  想要客製化
    css，裡面也有欄位可以輸入，不過似乎要指定 `id` 或 `class` 才行，直接輸入
    css 屬性，他不理我囧 。  
    另外講一下該怎麼加入自己想要的按鈕：

首先先將以下內容複製到「custom button」的欄位裡，我是只有複製到「large
icon」的欄位裡，看個人需要也可以複製到「small
icon」的欄位裡。另外內容中「圖片網址」的部份需要改為實際的網址，嫌麻煩也可以直接
google
網路上的圖示，不然如果有自己的空間的話，就下載下來傳到自己的空間，這樣管理也比較方便。

	:::html
	
	<div>
		<a target="_blank" href="http://plurk.com/?qualifier=shares&status= %%URL%% (%%TITLE%%)">
			<img title="分享到噗浪！" src="http://blog.carlcarl.tw/static/blog/images/plurk.png" border="0"  width="64" height="64"/>
		</a>
	</div>

另外要特別注意一點就是，只是用以上步驟，按鈕是不會出來的= =，還要在外掛
display 的設定將「custom button」的選項勾起來才行：  
![custom buttons checkbox][]

大致是以上步驟，弄完之後就可在文章的標題下方看到圖示囉。

參考網址：  
<http://www.moke.tw/wordpress/note/307>

  [Tweet, Like, Share and Google +1 Option Page]: http://i.imgur.com/AuifGS2l.png
    "Tweet, Like, Share and Google +1 Option Page"
  [1]: http://wordpress.org/extend/plugins/only-tweet-like-share-and-google-1/
  []: 圖片網址 "分享到噗浪！"
  [custom buttons checkbox]: http://i.imgur.com/AD3tc7Jl.png
    "custom buttons checkbox"
    