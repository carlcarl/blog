Title: C define debug function
Date: 2013-08-13 15:50
Author: carlcarl
Post_ID: 1267
Category: C
Tags: debug, makefile
Slug: c-define-debug-function

參考[這篇][]，然後做了點修改。

<!--more-->

	:::text
    #undef CM_DBG
    #ifdef LTE_CM_DEBUG
    #   define CM_DBG(fmt, args...) do{   
    	printf("  (%d/%s): "fmt, __LINE__, __FILE__, ## args);   
    }while(0)
    #else
    #   define CM_DBG(fmt, args...)
    #endif

    #undef CM_DBGG
    #define CM_DBGG(fmt, args...) do{   
    	printf("  (%d/%s): "fmt, __LINE__, __FILE__, ## args);   
    }while(0)

大致除了命名外還做了點修改：

1.  把 `printk` 的部分拿掉，因為我不需要。
2.  `CM_DBGG` 改成跟原本功能一樣。這樣有個好處就是我可以先 disable
    所有的 debug function，然後將要看的 `CM_DBG` 後面加個
    `G`，就可以只顯示需要注意的部分。

至於 Makefile 的部分有個折衷的方法：

	:::makefile
    # DEBUG
    DEBUG = y
    ifeq ($(DEBUG),y)
    CFLAGS += -DLTE_CM_DEBUG
    endif

    debug: CFLAGS += -DLTE_CM_DEBUG
    debug: all

這樣可以透過修改 `DEBUG` 的值，來決定是否要開啟 debug
function，例如在開發時就可以先開啟，等到要 production 的時候再設定
`DEBUG = n`，另外也可以用 `make debug` 來直接開啓
debug，執行上會更簡單。

  [這篇]: http://www.makelinux.net/ldd3/chp-4-sect-2
