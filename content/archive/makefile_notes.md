Title: Makefile Notes
Date: 2015-04-10 16:00
Author: carlcarl
Post_ID: 1422
Category: makefile
Tags: makefile
Slug: makefile_notes


## Implicit Make Rule

    :::makefile
    %.o:%.c
        $(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

* [CFLAGS vs CPPFLAGS]


## Target-specific Variables
ex:

    :::makefile
    target1: CFLAGS = -IINCLUDEPATH1
    target1: LDLIBS = -lLIB1
    target1: target1.o misc.o

* [Makefile - change variable value depending on a target]
* [Change Makefile variable value]
* [How to compile different c files with different CFLAGS using Makefile?]
* [What is the best approach to use different CFLAGS for the same source files?]


## LDFLAGS & LDLIBS

`LDLIBS` is for libraries, `LDFLAGS` should be used for flags/search paths (-L)

* [How to use LDFLAGS in makefile]

## Auto Dependency

ex:

    :::makefile
    Gpp = g++
    srcs = $(wildcard *.cpp)
    objs = $(srcs:.cpp=.o)
    deps = $(srcs:.cpp=.d)

    test: $(objs)
        $(Gpp) $^ -o $@

    %.o: %.cpp
        $(Gpp) -MMD -MP -c $< -o $@

    .PHONY: clean

    # $(RM) is rm -f by default
    clean:
        $(RM) $(objs) $(deps) test

    -include $(deps)

* [makefile dependency generation]
* [Makefile (Auto-Dependency Generation)]


## Others
* [http://chunchaichang.blogspot.tw/2010/12/makefile.html]
* [Makefile範例教學]
* [How to make SIMPLE C++ Makefile?]
* [http://www.chemie.fu-berlin.de/chemnet/use/info/make/make_10.html]

[CFLAGS vs CPPFLAGS]: http://stackoverflow.com/questions/2754966/cflags-vs-cppflags
[Makefile - change variable value depending on a target]: http://stackoverflow.com/questions/3261737/makefile-change-variable-value-depending-on-a-target
[Change Makefile variable value]: http://stackoverflow.com/questions/2711963/change-makefile-variable-value
[How to compile different c files with different CFLAGS using Makefile?]: http://stackoverflow.com/questions/1305665/how-to-compile-different-c-files-with-different-cflags-using-makefile
[What is the best approach to use different CFLAGS for the same source files?]: http://stackoverflow.com/questions/2517999/what-is-the-best-approach-to-use-different-cflags-for-the-same-source-files
[How to use LDFLAGS in makefile]: http://stackoverflow.com/questions/13249610/how-to-use-ldflags-in-makefile
[makefile dependency generation]: http://codereview.stackexchange.com/questions/2547/makefile-dependency-generation
[Makefile (Auto-Dependency Generation)]: http://stackoverflow.com/questions/8025766/makefile-auto-dependency-generation
[http://chunchaichang.blogspot.tw/2010/12/makefile.html]: http://chunchaichang.blogspot.tw/2010/12/makefile.html
[Makefile範例教學]: http://maxubuntu.blogspot.tw/2010/02/makefile.html
[How to make SIMPLE C++ Makefile?]: http://stackoverflow.com/questions/2481269/how-to-make-simple-c-makefile
[http://www.chemie.fu-berlin.de/chemnet/use/info/make/make_10.html]: http://www.chemie.fu-berlin.de/chemnet/use/info/make/make_10.html
