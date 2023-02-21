# moodlepdfdonwnloader
京都工芸繊維大学のmoodleにおいて，講義資料のpdfを自動でダウンロードするPythonプログラムです．

**追記**：LMSのログインに学認(シボレスIdP)を用いている大学であれば，サポートしている可能性があります．

# 2/21追記:GUI化を行い，exe化を行いました
ぜひ使ってみてください．それに伴い，LOGIN用のURLの入力が不要になりました．入力するURLはコースURLのみで結構です．
前提条件に記した条件は満たしている必要がありますが，ダブルクリックするだけで起動できるので便利になります．

# 現時点でMacでの動作しか保証していません．Windows環境では適宜コードを編集してください．
~~windowsで試した人いたら教えて欲しいかも．winでのPython環境構築がめんどくさいだけですが．~~

**2/13追記：別ブランチforwindowsverにwindows環境で動くように改変したコードがあります**

詳細は、そのブランチ内にあるREADMEを読んでください

# はじめに
**前提条件**
* chromeがインストール済みであること
* Pythonが実行できる環境であること
* seleniumとchrome driverが導入済みであること

(seleniumとchrome driverの導入の参考：https://qiita.com/memakura/items/20a02161fa7e18d8a693)

Pythonの環境があれば，pipでseleniumをインストールし，chrome driverもpipでインストールし，`chromedriver-path`でchrome driverがインストールされたディレクトリーがわかるので，コピーしてPATHを通せば完了です．

**追記**:batファイルにpipとバイナリのフルパスを表示するコマンドの例を載せているので，テキストエディタなどで参照してください．

**事前設定**

内部にある***user_info.txt***に以下の例に従ってユーザー情報を登録してください．

Ex)1行目にユーザー名，2行目にパスワード，3行目にLMSのトップページにおいてログインページへつながるリンクのURLを入力し，保存.

`ユーザー名`

`パスワード`

`LMSのログインページへと繋がるURL`
(ここはKITなら`https://moodle.cis.kit.ac.jp/login/index.php`となります）

# 使い方
* 通常のPythonファイルからの実行
1. `python test.py`等のコマンドで実行
2. ポップアップが表示される
3. `Cource URL`と表示されるので，コースURL（各講義のページのURL）をコピペ
4. `Folder name `と表示されるので，pdfを保存するディレクトリ(Folder name
5. `ID`と表示されるので，LMSにログインするためのIDを入力する．
6. `Password`と表示されるので，LMSにログインするためのパスワードを入力．
7. `file downloading...`と表示される．`Complete!`と表示されるまで待機
8. pdfはPythonのコードが置かれているディレクトリに，4で入力した名前のディレクトリで保存されている（はず）
9. あとは予習復習を頑張ってください

# 参考ページ
* https://qiita.com/memakura/items/20a02161fa7e18d8a693
* https://qiita.com/yumaloop/items/891b2476d47542d3ccf9
* https://senablog.com/python-selenium-pdf-download/
* https://tipstour.net/python-url-parse
* https://senablog.com/python-selenium-allpage-url/
* https://qiita.com/pd1/items/2f6ca7547d719c0262f0

# 今後の開発予定
~~GUI化を行う~~
done

* ユーザー情報の保存を任意にする

~~exe化も出来たらしたい~~
done
