# moodlepdfdonwnloader
京都工芸繊維大学のmoodleにおいて，講義資料のpdfを自動でダウンロードするPythonプログラムです

**前提条件**
* chromeがインストール済みであること
* Pythonが実行できる環境であること
* seleniumとchrome driverが導入済みであること

(seleniumとchrome driverの導入の参考：https://qiita.com/memakura/items/20a02161fa7e18d8a693)

Pythonの環境があれば，pipでseleniumをインストールし，chrome driverもpipでインストールし，`chromedriver-path`でchrome driverがインストールされたディレクトリーがわかるので，コピーしてPATHを通せば完了です．

**事前設定**

内部にある***user_info.txt***に以下の例に従ってユーザー情報を登録してください．

Ex)1行目にユーザー名，2行目にパスワード，3行目にLMSのトップページにおいてログインページへつながるリンクのURLを入力し，保存.

`ユーザー名`
`パスワード`
`LMSのログインページへと繋がるURL`

参考ページ
* https://qiita.com/memakura/items/20a02161fa7e18d8a693
* https://qiita.com/yumaloop/items/891b2476d47542d3ccf9
* https://senablog.com/python-selenium-pdf-download/
* https://tipstour.net/python-url-parse
* https://senablog.com/python-selenium-allpage-url/
* https://qiita.com/pd1/items/2f6ca7547d719c0262f0
