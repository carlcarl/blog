Title: Define Makefile variable in rule
Date: 2013-11-29 23:00
Author: carlcarl
Post_ID: 1380
Category: Linux
Tags: 
Slug: define_makefile_variable_in_rule


沒在寫啥 Makefile，要用的時候才發現不會在 rule 裡面 assign variable XD。具體用法如下:

	:::makefile
	all: 
    	$(eval tmp := $(shell echo 1))
		@echo $(tmp)



參考資料:  
[Define make variable at rule execution time][]  
[How to assign the output of a command to a Makefile variable][]  

[Define make variable at rule execution time]: http://stackoverflow.com/questions/1909188/define-make-variable-at-rule-execution-time
[How to assign the output of a command to a Makefile variable]: http://stackoverflow.com/questions/2019989/how-to-assign-the-output-of-a-command-to-a-makefile-variable

