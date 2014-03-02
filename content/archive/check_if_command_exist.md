Title: Check if command exist
Date: 2014-02-08 02:00
Author: carlcarl
Post_ID: 1391
Category: linux
Tags: linux
Slug: check_if_command_exist



本來直覺是用 `which`，不過查了一下資料，在 [How to check if a program exists from a bash script?] 發現有幾個不建議用 `which` 的理由：

1. cost 太大，需要另外 call 一個 process 來處理
2. exit status 在一些系統並沒有定義
3. 很多 operating system 會對 `which` 做額外的 tweak，可能會有其他的 side effect

在解答中建議可以用 `hash`, `command`, `type` 等指令來判斷，其中 `command` 的 exit code 在 POSIX 中是有明確定義的，其他的則無，所以使用 `command` 應該是最安全的方式。如果不 care 的話也是可以用另外兩種，而像 `hash` 本身執行會有額外的 side effect，那就是會算出 command 的 hash，讓下次可以更快找到並執行指令，以這點來看，似乎算是個不錯的好處。


[How to check if a program exists from a bash script?]: https://stackoverflow.com/questions/592620/how-to-check-if-a-program-exists-from-a-bash-script



