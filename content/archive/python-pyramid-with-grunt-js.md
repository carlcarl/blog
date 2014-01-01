Title: Python Pyramid with Grunt.js
Date: 2013-07-14 05:11
Author: carlcarl
Post_ID: 1131
Category: python
Tags: grunt, grunt.js, pyramid
Slug: python-pyramid-with-grunt-js

這幾天試玩了一下
[Grunt.js][]，感覺還不錯方便，所以來筆記一些自己的設定。一開始還在想
[Pyramid][] 和 Grunt 要怎麼結合，雖然有 Google
了一下，不過好像都沒有一個比較準確的答案，所以這邊我就照自己想的來做
XD。

我主要在 Grunt 中用的功能有：

1.  minify 和 combine css, js
2.  監控檔案的變化，有變動的話就做 1 的步驟
3.  做完 1 的步驟就自動 reload browser (livereload)

livereload 這邊是透過 Grunt bind 一個 port
並監視檔案的變化，接著網頁的部分加入這個 port 底下所提供的
javascript，一旦檔案發生變化，Grunt 就會 push 消息，通知 browser 做
reload 的動作。

### Project 架構

下面是整個 project 的大致架構，架構應該還算簡單 XD。附帶一提，template
我是使用 [jinja2][]。

	:::text
    .
    ├── CHANGES.txt
    ├── Gruntfile.js
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.txt
    ├── development.ini
    ├── package.json
    ├── production.ini
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── node_modules
    └── my_project
        ├── __init__.py
        ├── static
        │   ├── dist
        │   │   ├── css
        │   │   ├── favicon.ico
        │   │   ├── images
        │   │   ├── img
        │   │   ├── js
        │   │   └── manifest.mf
        │   └── src
        │       ├── css
        │       └── js
        ├── templates
        │   └── root.jinja2
        ├── tests.py
        └── views.py

`static` 底下該怎麼分類想了很久，Pyramid 的官方 doc
好像都沒提到該怎麼規劃比較好 orz，後來我是自己分類成 `src` 和 `dist`
兩個資料夾，處理過的 css, js 以及其他需要公開的檔案就放在 `dist`
裡頭。記得 route 也要改一下：

	:::python
    config.add_static_view('static', 'my_project:static/dist')

### Grunt CLI 安装

準備工作完成後，就可以來安裝 Grunt command line 了。

	:::bash
    npm install -g grunt-cli

### Grunt 設定檔

Grunt 基本需要兩個設定檔：第一個是 `package.json`，用來指定裝 `grunt`
以及其他一些外掛，像是上面提到的 minify, combine
這些功能都需要在這裡指定額外的外掛才能使用；第二個是
`Gruntfile.js`，這個則是用來設定這些外掛的參數和如何執行。基本上這兩個檔案直接放在同一層會比較好，我自己後來是決定都放在最上層，當然，如果確定只需要操縱
`static` 資料夾底下的檔案的話，也可以考慮都放在 `static` 底下，要執行
grunt 指令的時候再移到那一層執行就 OK 了。

下面是我的 package.json 內容：

	::javascript
    {
        "name": "my_project",
        "version": "0.1.0",
        "devDependencies": {
            "grunt": "*",
            "grunt-contrib-uglify": "*",
            "grunt-contrib-cssmin": "*",
            "grunt-contrib-watch": "*"
        }
    }

要裝的外掛就寫在 `devDependencies` 裡面。這邊 [grunt-contrib-uglify][]
和 [grunt-contrib-cssmin][] 分別是用來 minify, combine js 以及 css
用的，[grunt-contrib-watch][] 則是用來監控檔案變化和 livereload。

接下來則是 Gruntfile.js 的內容：

	:::javascript
    /*global node:true, module:true*/

    module.exports = function (grunt) {
        "use strict";
        // Project configuration.
        grunt.initConfig({
            pkg: grunt.file.readJSON('package.json'),
            uglify: {
                release: {
                    files: {
                        'my_project/static/dist/js/index.min.js': ['my_project/static/src/js/jquery-1.8.3.min.js', 'my_project/static/src/js/bootstrap.min.js', 'my_project/static/src/js/index.js']
                    }
                }
            },
            cssmin: {
                options: {
                    keepSpecialComments: 0
                },
                release: {
                    files: {
                        'my_project/static/dist/css/style.min.css': [
                            'my_project/static/src/css/bootstrap.css',
                            'my_project/static/src/css/bootstrap-responsive.css',
                            'my_project/static/src/css/style.css'
                        ]
                    }
                }
            },
            watch: {
                css: {
                    files: 'my_project/static/src/css/*.css',
                    tasks: ['cssmin'],
                    options: {
                        livereload: true
                    }
                },
                js: {
                    files: 'my_project/static/src/js/*.js',
                    tasks: ['uglify'],
                    options: {
                        livereload: true
                    }
                }
            }
        });

        // Load the plugins
        grunt.loadNpmTasks('grunt-contrib-uglify');
        grunt.loadNpmTasks('grunt-contrib-cssmin');
        grunt.loadNpmTasks('grunt-contrib-watch');

        // Default task(s).
        grunt.registerTask('default', ['uglify', 'cssmin', 'watch']);

    };

首先第一個是 `uglify`，`uglify` 除了 minify 和 combine
外，預設還會將所有變數名稱用較短的名稱來取代 (超貼心)，`files` 的 key
值是處理完後的檔案，array 裡則是要處理的檔案，以這裡的例子來看，就是把
`myproject/static/src/js` 底下的三個 js 檔案 combine 在一起，做 minify
和 mangle(將變數取代為較短的名稱)，最後放到 `my_project/static/dist/js`
底下，並命名為 `index.min.js`，如果不想要 combine 在一起的話就必須在
`files` 裡分開來寫；`cssmin` 也是 minify 和 combine，`options` 裡的
`keepSpecialComments: 0` 表示將 comment 拿掉；`watch`
則是指定要監控的檔案和要做的 task，另外還有設定 `livereload`，不過
`livereload` 的設定還沒結束，在 template 裡還需要加入一個
script，下面會提到。

### Grunt plugins 安裝

設定完後，在資料夾最上層輸入指令
`npm install`，接著會發現在現在的位置底下多了個
`node_modules`(可以回去對照一下一開始列出的 project 架構)，不過這個
node\_modules 不需要加入到 version control
中，所以可以設定一下，把這個資料夾忽略掉。

### Livereload

接著是設定 `livereload`，`livereload` 需要在 template 中加入
script，但是我不希望 production 環境中也跑出這個，所以我需要一個 flag
來幫助我判斷，於是我在 `development.ini` 以及 `production.ini`
分別加入了 `dev = true` 以及 `dev = false`，並在
`my_project/__init__.py` 的 `main` function 裡加入下面程式，在透過
subscriber 註冊的 function 會帶一個參數，這裡命名為
`event`，在這裡設值後，在 template 中就可以直接用 dev 這個變數。

	:::python
    if settings['dev'] == 'true':
        def add_global(event):
            event['dev'] = True
        config.add_subscriber(add_global, 'pyramid.events.BeforeRender')

在 `root.jinja2` 這個 template 的 `</body>` 上面加入以下程式就 OK 了：

	::jinja2
    {% if dev %}
    <script src="http://127.0.0.1:35729/livereload.js"></script>
    {% endif %}

### Test

寫完後先執行網頁，設定檔用 `development.ini`(ex:
`pserve development.ini`)，然後執行 `grunt watch`，接著嘗試改個 css 或
js 檔案並儲存看看，應該會自動產生處理後的檔案並自動 reload
網頁。`grunt watch`
預設不會放到背景執行，所以需要另外開個視窗來編輯檔案。

參考資料：  
[關於Grunt，從一個簡單的配置開始！][]  
[Grunt + RequireJS with multi-page website][]  
[Javascript command line tool GruntJS 介紹][]  
[初学grunt进行项目构建 二][]  
[Grunt.js 初使用][]  
[使用Grunt進行js、css壓縮合併][]  
[How to use grunt-contrib-livereload?][]

  [Grunt.js]: http://gruntjs.com
  [Pyramid]: http://www.pylonsproject.org
  [jinja2]: http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/
  [grunt-contrib-uglify]: https://github.com/gruntjs/grunt-contrib-uglify
  [grunt-contrib-cssmin]: https://github.com/gruntjs/grunt-contrib-cssmin
  [grunt-contrib-watch]: https://github.com/gruntjs/grunt-contrib-watch
  [關於Grunt，從一個簡單的配置開始！]: http://docs.spmjs.org/contrib/simple-grunt
  [Grunt + RequireJS with multi-page website]: http://gibuloto.com/blog/grunt-plus-requirejs-with-multi-page-website/
  [Javascript command line tool GruntJS 介紹]: http://blog.wu-boy.com/2013/03/javascript-command-line-tool-gruntjs/
  [初学grunt进行项目构建 二]: https://gist.github.com/appLhui/5283784/raw/093685c9971ac941be75d7ff7a718eca5173fcb1/初学grunt进行项目构建(二).md
  [Grunt.js 初使用]: http://www.jankerli.com/?p=1628
  [使用Grunt進行js、css壓縮合併]: http://www.k68.org/?p=1232
  [How to use grunt-contrib-livereload?]: http://stackoverflow.com/questions/16371022/how-to-use-grunt-contrib-livereload
