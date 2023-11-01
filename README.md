# pyinstaller_demo
pyinstallerのデモです。回帰モデルのexeを作ります。
回帰モデルは同じフォルダのtrain.csvを学習して、test.csvを予測します。
予測結果は「predict_実行日時」フォルダとして出力されます。
## train, test データ形式
- CSV (UTF-8)で、exeファイルと同じフォルダにあること
- train
    - 予測する変数を「target」という列名にすること
    - 「target」以外の列をすべて特徴量として利用します
- test
    - trainと同じ順番で同じ数の特徴量が入っていること
    - 「target」は存在しないこと
## model
- scikit-learnの線形回帰
# ローカルPCで実行する場合
1. pythonが動くPCを用意します
2. このデモのregression_demo.py, train.csv, test.csvをダウンロードします
    - `git clone https://github.com/yom1215/pyinstaller_demo.git`
4. ダウンロードした3ファイルをpythonが参照できる同じフォルダに置きます
5. pythonが実行できる環境を開きます
    - Windowsの場合：コマンドプロンプト（あるいはPowerShell）を開きます
    - Macの場合：ターミナルを開きます
    - Anacondaを利用している場合：Anacondaを起動します
    - `python --version`を入力して、pythonのバージョン情報が表示されればPythonが実行できる環境です
6. pyinstaller をインストールします
    - `pip install pyinstaller`
    - Anacondaを利用している場合：`conda install pyinstaller`
7. regression_demo.pyの場所（フォルダ、パス）を確認し、移動します
    - `cd ./pyinstaller_demo`
8. regression_demo.pyを実行できるか確認します
    - `python regression_demo.py` あるいは `python3 regression_demo.py` 
    - 実行環境に pandas, scikit-learnが入っていなければいれてください
        - `pip install pandas scikit-learn`
9. pyinstaller コマンドを実行します。
    - `pyinstaller --onefile --hidden-import=pandas._libs.tslibs.timedeltas regression_demo.py`
    - regression_demo.pyの部分を参照すべきフォルダまでのパスに編集します
        - `../data/regression_demo.py`とか
10. exeファイルができれば完成です
    - 実行した場所の./dist/にexeファイルが出力されます。 ログに Copying bootloader EXE to XXX.exeと表示されます。
11. exeファイルをtrain.csv, test.csvと同じフォルダに置き、クリックして実行します
12. predictフォルダが作成されれば成功です
* Windowsで作成したexeはWindowsでしか、Macで作成したexeはMacでしか動きません
* Google ColabはLinuxベースのため、Colab上で作成したexeはLinuxでしか動きません
# exeファイルが重くなる場合
- pyinstallerは実行した環境に入っているmoduleを全部入れようとします
- なので、pipでたくさんのmoduleを入れていると、作成されるexeが重くなります
    - 実行環境にはいっているmoduleは`pip list`でみれます
- exeを軽くしたい場合、pyinstallerを実行する環境を仮想環境として用意するのが良いです
- ここではvenvをつかった仮想環境の作り方を紹介します（Windows）
- 参考：https://docs.python.org/ja/3/library/venv.html
- 参考：https://www.python.jp/install/windows/venv.html
1. venvを作る場所（フォルダ、パス）に移動する　`cd /my_dir/`
2. 仮想環境をつくる　`python -m venv .venv`
    - `my_dir`の中に `venv` というフォルダができます。この中に仮想環境用のファイルが入ってます。
3. 仮想環境を立ち上げる()　`.venv\Scripts\activate.bat`
    - venvフォルダの中の`Scripts\activate.bat`を実行します
4. コマンド入力部分の先頭に (.venv) と表示されれば、仮想環境内に入りました。
    - 仮想環境から出たいときは`deactivate`
5. 新しく作った仮想環境のmoduleを確認してみましょう `pip list`
6. demoの作成に必要なモジュールをpipでインストールします
    - pip install pandas scikit-learn pyinstaller
7. regression_demo.pyを実行できるか確認します
8. pyinstaller コマンドを実行します
