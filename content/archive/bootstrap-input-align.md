Title: bootstrap input align
Date: 2013-02-22 03:07
Author: carlcarl
Post_ID: 788
Category: css
Tags: bootstrap
Slug: bootstrap-input-align

使用 bootstrap 的 input element 的時候遇到 text 和 button
位置不齊的情況，去 stackoverflow 找了一下就看到[解決的辦法][]了：  
<!--more-->

	:::html
	<div class="form-horizontal">
    	<input name="search" id="search"/>
    	<button class="btn">button</button>
	</div>


簡單說就是在外面那層加上 `form-horizontal` 這個 class 屬性，另外
`input-append` 雖然也可以達到類似的效果，不過由於 input element
會貼在一起，所以不建議用。

  [解決的辦法]: http://stackoverflow.com/questions/10615872/bootstrap-align-input-with-button
