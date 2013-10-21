Title: vimrc check hostname
Date: 2011-09-05 18:51
Author: carlcarl
Post_ID: 44
Category: linux
Tags: vim
Slug: vimrc-check-hostname

因為在不同電腦用了一個共用的 vimrc 檔，但是又想在兩邊作一些不同的設定，所以找了一下資料看要怎麼作。雖然有判斷作業系統的方式，不過好像不太適合我的用法，然後我通常不同的電腦都會設個有意義的 hostname，所以最後想說就用 hostname 去作判斷啦，以下是一個範例：

	:::text
	let hostname = substitute(system('hostname'), 'n', '', '')
	if hostname == "lab"
		"do something
	elseif hostname == "home"
		"do something
	endif

另外附上判斷 OS 的方式：

	:::text
	if has('win32')
		"do something
	elseif has('mac')
		"do something
	elseif has('unix')
		"do something
	endif

 

參考網址：  

<http://superuser.com/questions/194715/how-to-make-vim-settings-computer-dependent-in-vimrc>
