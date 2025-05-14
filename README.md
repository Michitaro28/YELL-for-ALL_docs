# YELL for ALL 技術ドキュメント
このリポジトリでは、YELL for ALLにおける開発等で用いる技術・知識などをアーカイブしていく。

# Sphinxを編集するための準備

## セットアップ
事前の環境構築として、使用する端末に下記のものがすでにインストールされていること
1. VScode : https://azure.microsoft.com/ja-jp/products/visual-studio-code
2. Git :　https://git-scm.com/downloads
3. GitHub(Clone) が利用できること
4. Pythonのインストール : https://www.python.org/

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
git clone https://github.com/Michitaro28/YELL-for-ALL_doc.git
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



