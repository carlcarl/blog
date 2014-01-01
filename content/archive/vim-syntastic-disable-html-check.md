Title: vim syntastic disable html check
Date: 2013-02-22 02:58
Author: carlcarl
Post_ID: 785
Category: vim
Tags: syntastic, vim
Slug: vim-syntastic-disable-html-check

最近在用 vim 修改 html 的時候會在儲存的時候爛掉，後來發現好像是
[syntastic][] 的問題，而且只有 html 會有這個問題，所以看了一下有沒有關掉
html check 的設定，後來在 stackoverflow 看到[解答][]：  

	:::text
    let g:syntastic_mode_map={ 'mode': 'active',
                          'active_filetypes': [],
                          'passive_filetypes': ['html'] }

將以上內容複製到 `.vimrc` 內即可。

  [syntastic]: https://github.com/scrooloose/syntastic
  [解答]: http://stackoverflow.com/questions/12215710/how-to-invalid-syntastic-check-for-html-file-with-vim
