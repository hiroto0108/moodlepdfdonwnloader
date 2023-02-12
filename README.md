# moodlepdfdonwnloader
京都工芸繊維大学のmoodleにおいて，講義資料のpdfを自動でダウンロードするPythonプログラムです．

**追記**：LMSのログインに学認(シボレスIdP)を用いている大学であれば，サポートしている可能性があります．

# Windows環境向けのコードです．
Mac OSやLinux系OSの場合は，mainブランチのコードを使うことをお勧めします．

# はじめに
**前提条件**
* chromeがインストール済みであること
* Pythonが実行できる環境であること
* seleniumとchrome driverが導入済みであること

(seleniumとchrome driverの導入の参考：https://qiita.com/memakura/items/20a02161fa7e18d8a693)

Pythonの環境があれば，`pip install selenium`でseleniumをインストールし，chrome driverも`pip install chromedriver-binary`でインストールしてください．~~エラーが出る場合は，~~`chromedriver-path`でchrome driverがインストールされたディレクトリーがわかるので，コピーしてPATHを通せば完了です．PATHを通さないとpdfがダウンロードできません. 

**追記**:batファイルにpipとバイナリのフルパスを表示するコマンドの例を載せているので，テキストエディタなどで参照してください．PowerShellでpipを実行した場合は、インストール完了後にもう一度同じコマンドを打つと、pipで管理されているパッケージが置かれているディレクトリが表示されるので、そこからchromedrive-binaryディレクトリを探し、その中にある`chromedrive-binary.exe`のパスで、PATHを通してください．

Ex)***太字***になっている部分がpipで管理されているパッケージが置かれているディレクトリです．

>PS C:\git\workspace_kmc\moodlepdfdonwnloader> pip install chromedriver-binary-auto
>>WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\site-packages)
Requirement already satisfied: chromedriver-binary-auto in ***[c:\python310\lib\site-packages]***　(0.2.3)
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Ignoring invalid distribution - (c:\python310\lib\........

**事前設定**

内部にある***user_info.txt***に以下の例に従ってユーザー情報を登録してください．

Ex)1行目にユーザー名，2行目にパスワード，3行目にLMSのトップページにおいてログインページへつながるリンクのURLを入力し，保存.

`ユーザー名`

`パスワード`

`LMSのログインページへと繋がるURL`
(ここはKITなら`https://moodle.cis.kit.ac.jp/login/index.php`となります）

# 使い方
1. 事前設定を行う
2. `python test.py`等のコマンドで実行
3. `Enter cource URL  : `と表示されるので，コースURL（各講義のページのURL）をコピペ
4. `Enter directory name  : `と表示されるので，pdfを保存するディレクトリ(フォルダ)の名前を入力
5. `file downloading...`と表示される．`Complete!`と表示されるまで待機
6. pdfはPythonのコードが置かれているディレクトリに，4で入力した名前のディレクトリで保存されている（はず）
7. あとは予習復習を頑張ってください

# 参考ページ
* https://qiita.com/memakura/items/20a02161fa7e18d8a693
* https://qiita.com/yumaloop/items/891b2476d47542d3ccf9
* https://senablog.com/python-selenium-pdf-download/
* https://tipstour.net/python-url-parse
* https://senablog.com/python-selenium-allpage-url/
* https://qiita.com/pd1/items/2f6ca7547d719c0262f0
* https://isgs-lab.com/183/

# 今後の開発予定
* GUI化を行う
* ユーザー情報の保存を任意にする
* exe化も出来たらしたい
