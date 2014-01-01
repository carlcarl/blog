Title: github readme with image
Date: 2012-04-08 02:09
Author: carlcarl
Post_ID: 366
Category: version-control
Tags: git, github, markdown
Slug: github-readme-with-image

github readme 的圖片目前看到比較方便的作法好像都是放在程式的資料夾裡面
push 上去，然後再利用連結去連圖片。

github 圖片連結通常是這樣的格式：  

「http://github.com/`yourname`/`your-repository`/raw/master/`your-folder`/`xxx.png`」

要自己設定的：`yourname`, `your-repository`, `your-folder`, `xxx.png`。

-   `yourname`: 你的帳號。
-   `your-respository`: 你的 project 名稱。
-   `your-folder`: 你放圖片的資料夾名稱，如果是直接放在 project
    的目錄底下的話，就可以省略這個。
-   `xxx.png`: 你的圖片名稱。

 

另外再附上 markdown 寫法：

	:::markdown
	![alt text](http://github.com/yourname/your-repository/raw/master/your-folder/xxx.png)  
  
`alt text` 是圖片的替代文字，看你想打啥。

 

參考網址：  

<https://groups.google.com/forum/?fromgroups#!topic/github/T3X1iadPH14>
