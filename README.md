# YELL for ALL 技術ドキュメント
このリポジトリでは、YELL for ALLにおける開発等で用いる技術・知識などをアーカイブしていく。

# Sphinxを編集するための準備

## セットアップ
事前の環境構築として、使用する端末に下記のものがすでにインストールされていること
1. VScode : https://azure.microsoft.com/ja-jp/products/visual-studio-code
2. Git :　https://git-scm.com/downloads
3. GitHub(Clone) が利用できること
4. Pythonのインストール : https://www.python.org/
5. PlantUMLのダウンロード　： https://plantuml.com/ja/download 　　
    ※今回はGPLの「Complied Jar」をクリックしてダウンロード
6. Graphviz : https://graphviz.org/download/
    ※上記から「（64bit）Zip archive」をダウンロード
7. TexLiveのダウンロード: https://www.tug.org/texlive/acquire-iso.html
    ※上記のリンク先から
    1. 「download from a nearby CTAN mirror」をクリック
    2. texlive2024.isoをダウンロード（注意：結構大きくて時間がかかります）
8. Inkscapeのインストール: https://inkscape.org/ja/release/inkscape-1.4.2/
    上記より各OSに合わせたものをダウンロード
    - Pathの確認
    CLI(Powershellやターミナル)で
    ```bash
    Inkscape --help
    ```
    上記をたたき、動作するかを確認。返ってこない場合はPathが通っていないことが考えられるので下記を確認
    1. Windowsキーを押下
    2. 検索ウィンドから「環境変数」を検索
    3. 「ユーザー環境変数」のpathを選択し、編集を押下
    4. 「新規」を押して、下記のディレクトリを追加
    ```
    C:\Program Files\Inkscape\bin

    ```
    5. 環境変数ウィンドのOKを押下し、閉じる
    6. Powershellなどを開いていた場合は一度閉じて、再起動する
    7. 再度CLIで、「Inkscape --help」を実行し、「Inkscape」が表示されたらOKです。

## このリポジトリを使用する上でのセットアップ

### 1. Poetry のインストール

macOS/Linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows(PowerShell)
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

インストール後、poetryコマンドが使えるかの確認
```bash
poetry --version
```

### WindowsOSでのPoetryパスが通っていないとき
poetry実行のための環境変数設定PATHを設定します。
1. Windowsキーを押下
2. 検索ウィンドから「環境変数」を検索
3. 「ユーザー環境変数」のpathを選択し、編集を押下
4. 下記のディレクトリを追加
```
%USERPROFILE%\AppData\Roaming\Python\Scripts\

```
5. 環境変数ウィンドのOKを押下し、閉じる
6. Powershellなどを開いていた場合は一度閉じて、再起動する

※poetry公式ドキュメント：https://python-poetry.org/docs/#installing-with-pipx

### 2. このリポジトリをクローンする
ターミナルまたはPowershellを使い、任意のディレクトリに移動してください。
移動方法は下記のコマンド
```bash
cd <任意のディレクトリパス>
```
指定したい場所で右クリックを「パスのコピー」などを行うとわかりやすいです。

任意のディレクトリに移動したら下記のコマンドを実行
```bash
git clone https://github.com/Michitaro28/YELL-for-ALL_docs.git
```

cloneが完了したら、cdコマンドでYELL-for-ALL_docフォルダに移動します。
```bach
cd YELL-for-ALL_doc
```

そこで下記のコマンドでVScodeが開きます。
```bash
code .
```


### 3. 依存関係のインストール
VSocde上のターミナルで下記のコマンドを実行してください。
```bash
poetry install --with=dev
```
上記を実行すると依存関係ファイルが一括してダウンロードされると思います。


### 4. 仮想環境のアクティベート
必要に応じて仮想環境の実行をしてください
```bash
poetry shell
```

## HTMLファイルの出力
更新作業において、.rstファイルを編集したのち、HTML出力してください。その際のは下記のコマンド
```bash
poetry run make html
```
出力のクリア
```bash
poetry run make clean        
```
PDF出力
```bash
poetry run make latexpdf     # PDF出力（LaTeX必要）
```



