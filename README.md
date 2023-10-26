# pyinstaller_demo
pyinstallerのデモです。回帰モデルのexeを作ります。

# ローカルPCで実行する場合
1. pythonが動くPCを用意します
2. このデモのregression_demo.py, train.csv, test.csvをダウンロードします
3. ダウンロードした3ファイルをpythonが参照できるフォルダに置きます
    - 他のファイルがない場所が良いです
4. pythonが実行できる環境を開きます
    - Windowsの場合：コマンドプロンプト（あるいはPowerShell）を開きます
    - Macの場合：ターミナルを開きます
    - Anacondaを利用している場合：Anacondaを起動します
    - python --versionを入力して、pythonのバージョン情報が表示される場所です
5. pyinstaller をインストールします
    - pip install pyinstaller
    - Anacondaを利用している場合：conda install pyinstaller
6. regression_demo.pyの場所（フォルダ、パス）を確認します
    - python regression_demo.py あるいは python3 regression_demo.py を実行して結果が出力されるか確認してください
    - pandas, scikit-learnが入っていなければいれてください　pip install pandas scikit-learn
7. pyinstaller コマンドを実行します。
    - pyinstaller --onefile --hidden-import=pandas._libs.tslibs.timedeltas regression_demo.py
    - regression_demo.pyの部分を参照すべきフォルダまでのパスに編集します
        - ../data/regression_demo.pyとか
8. exeファイルができれば完成です
    - 実行した場所の./dist/にexeファイルが出力されます。 ログに Copying bootloader EXE to XXX.exeと表示されます。
10. exeファイルをtrain.csv, test.csvと同じフォルダに置き、クリックして実行します
11. predictフォルダが作成されれば成功です
