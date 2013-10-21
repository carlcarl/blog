Title: C++ redirect cout to file
Date: 2011-07-22 18:31
Author: carlcarl
Post_ID: 38
Category: C &amp; C++
Slug: c-plus-plus-redirect-cout-to-file

可能有些人會覺得說用 `fstream` 另外寫就好了

不過程式如果有設定可以輸出至螢幕或是檔案的話

分開兩個寫就會讓人覺得很麻煩

可能有關輸出的部份都需要用 `if` 判斷，然後分兩塊輸出

 

如果在一開始就設定 `cout` 是輸出到螢幕或是檔案的話

之後就不用再用 `if` 來一個一個判斷了，這個是我覺得的優點

 

程式碼片段範例

	:::c++
	bool readFromFile;
	//根據一些判斷去設定readFromFile的值
	readFromFile = true;
	if(readFromFile)
	{
		ofstream outputFile;
		string fileName = "file.txt";
		outputFile.open(fileName, fstream::out);
		cout.rdbuf(outputFile.rdbuf());
	}
	else //表示輸出到stdout
	{
		//不做任何事情 因為cout本來就是輸出到stdout
	}
	//之後就直接用cout就可以了~

 

參考網頁

<http://www.java2s.com/Tutorial/Cpp/0240__File-Stream/Redirectouputintothefile.htm>

