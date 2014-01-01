Title: Pixnet paste code
Date: 2011-03-14 16:11
Author: carlcarl
Post_ID: 6
Category: blog
Slug: pixnet-paste-code

在側邊欄位設定裡 -> 頁尾描述的部分貼上下面的 code

	:::html
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shCore.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shAutoloader.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushBash.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushCpp.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushCSharp.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushCss.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushPowerShell.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushJScript.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushPlain.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushSql.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushVb.js"></script>
	<script type="text/javascript" src="http://alexgorbatchev.com/pub/sh/current/scripts/shBrushXml.js"></script>
	<script type="text/javascript">
		SyntaxHighlighter.all();
	</script>

	<link type="text/css" rel="stylesheet" href="http://alexgorbatchev.com/pub/sh/current/styles/shCore.css"/>
	<link type="text/css" rel="stylesheet" href="http://alexgorbatchev.com/pub/sh/current/styles/shThemeDefault.css"/> 


使用的時候 將 code 用 `<pre class="brush: js"></pre>` 包起來就可以了

	:::text
	+--------------------------------------------------------------------------+
	|   -------------- ------------------------------- -------------------     |
	|   Brush name     Brush aliases                   File name               |
	|   Bash/shell     bash, shell                     shBrushBash.js          |
	|   C#            c-sharp, csharp                 shBrushCSharp.js         |
	|   C++            cpp, c                          shBrushCpp.js           |
	|   CSS            css                             shBrushCss.js           |
	|   Delphi         delphi, pas, pascal             shBrushDelphi.js        |
	|   Diff           diff, patch                     shBrushDiff.js          |
	|   Groovy         groovy                          shBrushGroovy.js        |
	|   JavaScript     js, jscript, javascript         shBrushJScript.js       |
	|   Java           java                            shBrushJava.js          |
	|   Perl           perl, pl                        shBrushPerl.js          |
	|   PHP            php                             shBrushPhp.js           |
	|   Plain Text     plain, text                     shBrushPlain.js         |
	|   Python         py, python                      shBrushPython.js        |
	|   Ruby           rails, ror, ruby                shBrushRuby.js          |
	|   Scala          scala                           shBrushScala.js         |
	|   SQL            sql                             shBrushSql.js           |
	|   Visual Basic   vb, vbnet                       shBrushVb.js            |
	|   XML            xml, xhtml, xslt, html, xhtml   shBrushXml.js           |
	|   -------------- ------------------------------- -------------------     |
	|                                                                          |
	|   : style                                                                |
	|                                                                          |
	|                                                                          |
	|                                                                          |
	+--------------------------------------------------------------------------+

 

參考網址:

[銅板人生][]

[威力手記本][]

<http://miakila.pixnet.net/blog/post/30926039>

  [銅板人生]: http://itzak.pixnet.net/blog/post/234830
  [威力手記本]: http://weiyiao.pixnet.net/blog/post/23484768
