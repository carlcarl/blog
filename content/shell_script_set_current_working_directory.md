Title: Shell script set current working directory
Date: 2014-01-25 23:00
Author: carlcarl
Post_ID: 1388
Category: linux
Tags: bash
Slug: shell_script_set_current_working_directory



在 [stackoverflow] 上看到的，好像很常會用到所以先記下來，兩種方法:

    :::bash
    # First method
    cd ${0%\*} 

    # Second method
    cd "$(dirname "$0")"

第一個是用 [parameter expansion]。


[stackoverflow]: http://stackoverflow.com/questions/3349105/bash-script-set-current-working-directory-to-the-directory-of-the-script
[parameter expansion]: http://stackoverflow.com/questions/6393551/what-is-the-meaning-of-0-in-a-bash-script