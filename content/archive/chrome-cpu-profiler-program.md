Title: chrome cpu profiler program
Date: 2013-06-17 15:26
Author: carlcarl
Post_ID: 1049
Category: js
Tags: chrome
Slug: chrome-cpu-profiler-program

查了一下 chrome 裡 cpu profiler 裡的 program 代表啥意思，像有人說是整個
js code 的 root，不過看了一下其他的意見，感覺比較像是 native code
所花的時間，包括 DOM 操作，gc 等一堆雜事等。舉個例子來說，假如你是要看你
function 處理一堆 array 結構的校能的話，就可以不需要理這欄。

參考資料：  
[Slow javascript execution in chrome, profiler yields (program)][]  
[What does (program) signify in the Chrome profiler?][]  
[Chrome debugger - what is “(program)” in the profiler?][]

  [Slow javascript execution in chrome, profiler yields (program)]: http://stackoverflow.com/questions/9494228/slow-javascript-execution-in-chrome-profiler-yields-program
  [What does (program) signify in the Chrome profiler?]: https://groups.google.com/forum/?fromgroups#!topic/chromium-discuss/02CEYDcuO18
  [Chrome debugger - what is “(program)” in the profiler?]: http://stackoverflow.com/questions/3847954/chrome-debugger-what-is-program-in-the-profiler
