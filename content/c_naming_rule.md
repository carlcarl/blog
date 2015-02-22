Title: C Naming Rule
Date: 2015-02-22 23:30
Author: carlcarl
Post_ID: 1413
Category: C/C++
Tags: C/C++
Slug: c_naming_rule


最近看到的幾個 naming 的問題。

## `_t` 結尾的變數

`_t` 結尾的變數是 for POSIX 的，盡量避免這樣命名。


## `_` 開頭的變數

像是 `int _num;` 這樣，或是 `ifndef` 會用到:

	:::c
	#ifndef _HEADER_H
	#define _HEADER_H
	#endif
	
可是同樣的，`_` 或是 `__` 開頭的，都是 reserved names，所以一樣能避免就避免。


Ref:

* [Standard for typedef'ing]
* [Reserved Names]
* [#ifndef syntax for include guards in C++]
* [c++ #ifndef for include files, why is all caps used for the header file?]
* [What are the rules about using an underscore in a C++ identifier?]


[Standard for typedef'ing]: stackoverflow.com/questions/3538170/standard-for-typedefing
[Reserved Names]: http://www.gnu.org/software/libc/manual/html_node/Reserved-Names.html
[#ifndef syntax for include guards in C++]: stackoverflow.com/questions/10077025/ifndef-syntax-for-include-guards-in-c
[in C++ , what's so special about “_MOVE_H”?]: stackoverflow.com/questions/3345159/in-c-whats-so-special-about-move-h
[c++ #ifndef for include files, why is all caps used for the header file?]: stackoverflow.com/questions/3799478/c-ifndef-for-include-files-why-is-all-caps-used-for-the-header-file
[What are the rules about using an underscore in a C++ identifier?]: http://stackoverflow.com/questions/228783/what-are-the-rules-about-using-an-underscore-in-a-c-identifier/228797#228797



