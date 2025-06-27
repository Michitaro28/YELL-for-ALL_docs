# CLI（コマンドライン）入門ガイド

CLI（Command Line Interface）は、テキストベースでコンピューターと対話するためのインターフェースです。マウスを使わずにキーボードだけでファイル操作、プログラム実行、システム管理などができます。

## CLIとは

CLIは、グラフィカルユーザーインターフェース（GUI）とは対照的に、文字入力によってコンピューターに指示を与える方法です。開発者にとって必須のスキルで、効率的な作業を可能にします。

### CLIの利点

- **効率性**: マウス操作より高速な操作が可能
- **自動化**: スクリプト化により繰り返し作業を自動化
- **リモートアクセス**: SSH経由でのサーバー操作
- **精密制御**: 詳細なオプション指定が可能
- **バッチ処理**: 複数のファイルやディレクトリを一括処理

## ターミナルの起動方法

### macOS
```bash
# ターミナルアプリの起動
# Applications > Utilities > Terminal
# または Spotlight検索で「terminal」と入力

# よく使われるターミナル
# - Terminal（標準）
# - iTerm2（サードパーティ）
```

### Windows
```bash
# コマンドプロンプト
# Win + R > cmd

# PowerShell
# Win + R > powershell

# Windows Terminal（推奨）
# Microsoft Storeからインストール可能
```

### Linux
```bash
# ショートカットキー
# Ctrl + Alt + T

# GUI経由
# Applications > Terminal
```

## 基本概念

### プロンプト

```bash
# macOS/Linux の一般的なプロンプト
username@hostname:current_directory$ 

# 例
john@macbook:~/Documents$ 

# Windows コマンドプロンプト
C:\Users\username>

# PowerShell
PS C:\Users\username>
```

### カレントディレクトリ

```bash
# 現在いる場所（カレントディレクトリ）を表示
pwd    # macOS/Linux
cd     # Windows

# 出力例
/Users/john/Documents
```

### パス（Path）

```bash
# 絶対パス（ルートから始まる完全なパス）
/Users/john/Documents/project/file.txt    # macOS/Linux
C:\Users\john\Documents\project\file.txt  # Windows

# 相対パス（現在のディレクトリからの相対的なパス）
./file.txt        # 現在のディレクトリのfile.txt
../parent.txt     # 一つ上のディレクトリのparent.txt
../../root.txt    # 二つ上のディレクトリのroot.txt
```

## 基本的なファイル・ディレクトリ操作

### ディレクトリの確認と移動

```bash
# 現在のディレクトリを表示
pwd

# ディレクトリの内容を表示
ls          # macOS/Linux
dir         # Windows

# 詳細表示
ls -l       # macOS/Linux
ls -la      # 隠しファイルも表示
dir /a      # Windows（隠しファイルも表示）

# ディレクトリ移動
cd Documents              # Documentsディレクトリに移動
cd /Users/john/Desktop    # 絶対パスで移動
cd ..                     # 一つ上のディレクトリに移動
cd ~                      # ホームディレクトリに移動（macOS/Linux）
cd %USERPROFILE%          # ホームディレクトリに移動（Windows）
cd /                      # ルートディレクトリに移動（macOS/Linux）
cd C:\                    # Cドライブのルートに移動（Windows）
```

### ファイルとディレクトリの作成

```bash
# 新しいディレクトリを作成
mkdir new_folder
mkdir -p path/to/new/folder    # 中間ディレクトリも同時に作成（macOS/Linux）
mkdir path\to\new\folder       # Windows

# 複数のディレクトリを同時に作成
mkdir folder1 folder2 folder3

# 新しいファイルを作成
touch newfile.txt              # macOS/Linux
echo. > newfile.txt            # Windows
type nul > newfile.txt         # Windows（別の方法）

# 内容付きでファイルを作成
echo "Hello World" > hello.txt
echo "追加の内容" >> hello.txt  # ファイルに追加
```

### ファイルとディレクトリのコピー・移動・削除

```bash
# ファイルのコピー
cp source.txt destination.txt     # macOS/Linux
copy source.txt destination.txt   # Windows

# ディレクトリのコピー
cp -r source_folder dest_folder   # macOS/Linux
xcopy source_folder dest_folder /E # Windows

# ファイルの移動・リネーム
mv oldname.txt newname.txt        # macOS/Linux
move oldname.txt newname.txt      # Windows

# ファイルの削除
rm file.txt                       # macOS/Linux
del file.txt                      # Windows

# ディレクトリの削除
rm -r folder_name                 # macOS/Linux（中身も含めて削除）
rmdir /s folder_name              # Windows（中身も含めて削除）

# 確認付きで削除
rm -i file.txt                    # macOS/Linux
```

## ファイル内容の表示と編集

### ファイル内容の表示

```bash
# ファイル内容をすべて表示
cat file.txt                      # macOS/Linux
type file.txt                     # Windows

# ファイル内容をページ単位で表示
less file.txt                     # macOS/Linux
more file.txt                     # Windows/macOS/Linux

# ファイルの先頭部分を表示
head file.txt                     # macOS/Linux（先頭10行）
head -n 5 file.txt                # 先頭5行のみ

# ファイルの末尾部分を表示
tail file.txt                     # macOS/Linux（末尾10行）
tail -n 20 file.txt               # 末尾20行
tail -f log.txt                   # ファイルの変更をリアルタイムで監視
```

### テキストエディタ

```bash
# コマンドライン上でファイルを編集
nano file.txt                     # nano（初心者向け）
vim file.txt                      # Vim（上級者向け）
emacs file.txt                    # Emacs

# nano の基本操作
# Ctrl + O: 保存
# Ctrl + X: 終了
# Ctrl + K: 行の削除
# Ctrl + U: 削除した行を復元

# Vim の基本操作
# i: 挿入モード
# :w: 保存
# :q: 終了
# :wq: 保存して終了
# :q!: 保存せずに終了
```

## 検索とフィルタリング

### ファイル検索

```bash
# ファイル名で検索
find . -name "*.txt"              # macOS/Linux（現在のディレクトリ以下の.txtファイル）
find /home -name "config*"        # /home以下でconfigで始まるファイル
dir *.txt /s                      # Windows（.txtファイルを再帰検索）

# ファイル内容で検索
grep "search_term" file.txt       # macOS/Linux
findstr "search_term" file.txt    # Windows

# 複数ファイルから検索
grep -r "search_term" .           # カレントディレクトリ以下を再帰検索
grep -i "search_term" file.txt    # 大文字小文字を区別しない検索
grep -n "search_term" file.txt    # 行番号付きで表示
grep -v "exclude_term" file.txt   # 指定した語を含まない行を表示
```

### パイプとリダイレクト

```bash
# パイプ（|）：コマンドの出力を次のコマンドの入力にする
ls -l | grep "txt"                # lsの出力からtxtを含む行を抽出
cat file.txt | wc -l              # ファイルの行数をカウント
ps aux | grep "python"            # 実行中のpythonプロセスを表示

# リダイレクト（>）：出力をファイルに保存
ls -l > file_list.txt             # lsの結果をファイルに保存
echo "Hello" > greeting.txt       # 新しいファイルを作成（上書き）
echo "World" >> greeting.txt      # ファイルに追加

# 入力リダイレクト（<）
sort < unsorted.txt               # ファイルの内容をソート
```

## システム情報と管理

### システム情報の確認

```bash
# システム情報
uname -a                          # macOS/Linux（システム情報）
systeminfo                       # Windows（システム情報）

# CPU情報
lscpu                             # Linux
sysctl -n machdep.cpu.brand_string # macOS
wmic cpu get name                 # Windows

# メモリ使用量
free -h                           # Linux
vm_stat                           # macOS
wmic memorychip get size          # Windows

# ディスク使用量
df -h                             # macOS/Linux（ディスク使用量）
du -sh *                          # 各ディレクトリのサイズ
dir /-c                           # Windows
```

### プロセス管理

```bash
# 実行中のプロセス表示
ps aux                            # macOS/Linux
tasklist                          # Windows

# プロセスの終了
kill PID                          # macOS/Linux（プロセスIDを指定）
killall process_name              # macOS/Linux（プロセス名を指定）
taskkill /PID 1234                # Windows（プロセスIDを指定）
taskkill /IM notepad.exe          # Windows（プロセス名を指定）

# バックグラウンド実行
command &                         # macOS/Linux
start command                     # Windows
```

## ネットワーク関連コマンド

### 基本的なネットワークコマンド

```bash
# ネットワーク接続の確認
ping google.com                   # ネットワーク接続テスト
ping -c 4 google.com              # 4回だけpingを送信（macOS/Linux）
ping -n 4 google.com              # 4回だけpingを送信（Windows）

# ネットワーク設定の確認
ifconfig                          # macOS/Linux（ネットワーク設定）
ipconfig                          # Windows（ネットワーク設定）
ipconfig /all                     # Windows（詳細な設定）

# DNSの確認
nslookup google.com               # DNSルックアップ
dig google.com                    # macOS/Linux（詳細なDNS情報）

# ポートの確認
netstat -an                       # 開いているポートの表示
netstat -an | grep 80             # ポート80の状態を確認（macOS/Linux）
netstat -an | findstr 80          # ポート80の状態を確認（Windows）
```

### ファイルのダウンロード

```bash
# ファイルのダウンロード
curl -O https://example.com/file.zip    # macOS/Linux
wget https://example.com/file.zip       # Linux
powershell -Command "Invoke-WebRequest -Uri 'https://example.com/file.zip' -OutFile 'file.zip'"  # Windows

# HTTPリクエストの送信
curl -X GET https://api.example.com/data
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/data
```

## 圧縮とアーカイブ

### ファイルの圧縮・展開

```bash
# tar（macOS/Linux）
tar -czf archive.tar.gz folder/   # フォルダを圧縮
tar -xzf archive.tar.gz           # 圧縮ファイルを展開
tar -tzf archive.tar.gz           # 圧縮ファイルの内容を確認

# zip
zip -r archive.zip folder/        # フォルダをzip圧縮
unzip archive.zip                 # zipファイルを展開
unzip -l archive.zip              # zipファイルの内容を確認

# Windows固有
powershell -Command "Compress-Archive -Path 'folder' -DestinationPath 'archive.zip'"
powershell -Command "Expand-Archive -Path 'archive.zip' -DestinationPath '.'"
```

## 権限とセキュリティ

### ファイル権限（macOS/Linux）

```bash
# 権限の確認
ls -l file.txt

# 権限の変更
chmod 755 file.txt                # 所有者：読み書き実行、その他：読み実行
chmod u+x script.sh               # 所有者に実行権限を追加
chmod go-w file.txt               # グループとその他から書き込み権限を削除

# 所有者の変更
chown user:group file.txt         # ファイルの所有者とグループを変更
sudo chown root:root file.txt     # 管理者権限で変更

# 権限の数値表記
# 4: 読み込み（r）
# 2: 書き込み（w）
# 1: 実行（x）
# 例：755 = 4+2+1, 4+1, 4+1 = rwxr-xr-x
```

### 管理者権限

```bash
# 管理者権限でコマンドを実行
sudo command                      # macOS/Linux
runas /user:Administrator command # Windows

# 管理者権限でシェルを起動
sudo -i                           # macOS/Linux
runas /user:Administrator cmd     # Windows
```

## 環境変数

### 環境変数の確認と設定

```bash
# 環境変数の確認
env                               # すべての環境変数を表示（macOS/Linux）
set                               # すべての環境変数を表示（Windows）
echo $PATH                        # PATH変数を表示（macOS/Linux）
echo %PATH%                       # PATH変数を表示（Windows）

# 環境変数の設定
export VAR_NAME="value"           # macOS/Linux（一時的）
set VAR_NAME=value                # Windows（一時的）

# 永続的な環境変数の設定
echo 'export VAR_NAME="value"' >> ~/.bashrc    # Linux
echo 'export VAR_NAME="value"' >> ~/.zshrc     # macOS（zsh）
setx VAR_NAME "value"             # Windows（永続的）
```

## 便利なコマンド一覧

### ファイル操作
```bash
# ファイルサイズでソート
ls -lS                            # 大きい順
ls -lSr                           # 小さい順

# 更新日時でソート
ls -lt                            # 新しい順
ls -ltr                           # 古い順

# ファイル数のカウント
ls | wc -l                        # カレントディレクトリのファイル数
find . -type f | wc -l            # サブディレクトリも含めたファイル数

# 重複ファイルの削除
sort file.txt | uniq              # 重複行を削除
sort file.txt | uniq -d           # 重複行のみを表示
sort file.txt | uniq -c           # 各行の出現回数を表示
```

### テキスト処理
```bash
# 行数、単語数、文字数のカウント
wc file.txt                       # 行数、単語数、文字数
wc -l file.txt                    # 行数のみ
wc -w file.txt                    # 単語数のみ
wc -c file.txt                    # 文字数のみ

# テキストの置換
sed 's/old/new/g' file.txt        # oldをnewに置換
sed 's/old/new/g' file.txt > new_file.txt  # 結果を新しいファイルに保存

# 列の抽出
cut -d',' -f1 file.csv            # CSVファイルの1列目を抽出
awk -F',' '{print $1}' file.csv   # awxを使った列の抽出

# ファイルの比較
diff file1.txt file2.txt          # ファイルの差分を表示
comm file1.txt file2.txt          # ソート済みファイルの比較
```

### システム監視
```bash
# リアルタイムでプロセス監視
top                               # macOS/Linux
htop                              # Linux（より見やすい）
taskmgr                           # Windows（タスクマネージャー）

# ディスク使用量の監視
watch df -h                       # ディスク使用量をリアルタイム監視
iostat 1                          # I/O統計を1秒間隔で表示

# ログファイルの監視
tail -f /var/log/system.log       # ログファイルをリアルタイム監視
tail -f log.txt | grep "ERROR"    # エラーメッセージのみを監視
```

### 便利なショートカット

```bash
# 履歴操作
history                           # コマンド履歴を表示
!!                                # 直前のコマンドを再実行
!n                                # n番目のコマンドを再実行
!string                           # stringで始まるコマンドを再実行

# タブ補完
# Tabキーを押すとファイル名やコマンド名を補完

# カーソル移動
# Ctrl + A: 行の先頭に移動
# Ctrl + E: 行の末尾に移動
# Ctrl + U: カーソルから行の先頭までを削除
# Ctrl + K: カーソルから行の末尾までを削除
# Ctrl + L: 画面をクリア

# プロセスの制御
# Ctrl + C: 実行中のプロセスを停止
# Ctrl + Z: プロセスを一時停止
# bg: バックグラウンドで再開
# fg: フォアグラウンドで再開
```

## スクリプト作成の基礎

### シェルスクリプト（macOS/Linux）

```bash
#!/bin/bash
# backup.sh - バックアップスクリプトの例

# 変数の定義
SOURCE_DIR="/home/user/documents"
BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d)

# バックアップの実行
echo "バックアップを開始します..."
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "バックアップが完了しました: backup_$DATE.tar.gz"
else
    echo "バックアップに失敗しました"
    exit 1
fi

# 古いバックアップファイルの削除（7日より古いもの）
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
echo "古いバックアップファイルを削除しました"
```

```bash
# スクリプトの実行
chmod +x backup.sh                # 実行権限を付与
./backup.sh                       # スクリプトを実行
```

### バッチファイル（Windows）

```batch
@echo off
REM backup.bat - バックアップスクリプトの例

REM 変数の定義
set SOURCE_DIR=C:\Users\user\Documents
set BACKUP_DIR=C:\Backup
set DATE=%date:~0,4%%date:~5,2%%date:~8,2%

REM バックアップの実行
echo バックアップを開始します...
powershell -Command "Compress-Archive -Path '%SOURCE_DIR%' -DestinationPath '%BACKUP_DIR%\backup_%DATE%.zip'"

if %errorlevel% equ 0 (
    echo バックアップが完了しました: backup_%DATE%.zip
) else (
    echo バックアップに失敗しました
    exit /b 1
)

REM 古いバックアップファイルの削除（7日より古いもの）
forfiles /p "%BACKUP_DIR%" /m backup_*.zip /d -7 /c "cmd /c del @path"
echo 古いバックアップファイルを削除しました
```

## 開発関連コマンド

### Git（バージョン管理）

```bash
# Gitの初期設定
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# リポジトリの作成・クローン
git init                          # 新しいリポジトリを作成
git clone https://github.com/user/repo.git  # リポジトリをクローン

# 基本的なGit操作
git status                        # ファイルの状態を確認
git add file.txt                  # ファイルをステージング
git add .                         # すべての変更をステージング
git commit -m "コミットメッセージ" # コミット
git push origin main              # リモートリポジトリにプッシュ
git pull                          # リモートから変更を取得

# ブランチ操作
git branch                        # ブランチ一覧
git branch new-feature            # 新しいブランチを作成
git checkout new-feature          # ブランチを切り替え
git checkout -b new-feature       # ブランチを作成して切り替え
git merge new-feature             # ブランチをマージ
```

### Python関連

```bash
# Pythonのバージョン確認
python --version
python3 --version

# パッケージ管理
pip install package_name          # パッケージのインストール
pip list                          # インストール済みパッケージ一覧
pip freeze > requirements.txt     # 要件ファイルの作成
pip install -r requirements.txt   # 要件ファイルからインストール

# 仮想環境
python -m venv myenv              # 仮想環境の作成
source myenv/bin/activate         # 仮想環境の有効化（macOS/Linux）
myenv\Scripts\activate            # 仮想環境の有効化（Windows）
deactivate                        # 仮想環境の無効化

# Pythonスクリプトの実行
python script.py                  # スクリプトの実行
python -m module_name             # モジュールの実行
python -c "print('Hello World')"  # ワンライナー実行
```

### Node.js関連

```bash
# Node.jsのバージョン確認
node --version
npm --version

# パッケージ管理
npm init                          # package.jsonの作成
npm install package_name          # パッケージのインストール
npm install -g package_name       # グローバルインストール
npm install --save-dev package_name  # 開発依存関係
npm list                          # インストール済みパッケージ一覧
npm update                        # パッケージの更新

# スクリプトの実行
npm start                         # プロジェクトの開始
npm test                          # テストの実行
npm run build                     # ビルドの実行
```

## トラブルシューティング

### よくある問題と解決法

```bash
# コマンドが見つからない場合
which command_name                # コマンドの場所を確認（macOS/Linux）
where command_name                # コマンドの場所を確認（Windows）
echo $PATH                        # PATH環境変数を確認

# 権限エラーの場合
sudo command                      # 管理者権限で実行（macOS/Linux）
chmod +x script.sh                # 実行権限を付与

# ディスク容量不足の場合
df -h                             # ディスク使用量を確認
du -sh * | sort -hr               # ディレクトリサイズを大きい順で表示
find . -type f -size +100M        # 100MB以上のファイルを検索

# プロセスが応答しない場合
ps aux | grep process_name        # プロセスIDを確認
kill -9 PID                       # 強制終了

# ファイルが見つからない場合
find / -name "filename" 2>/dev/null  # システム全体から検索（エラーを非表示）
locate filename                   # ファイル名データベースから検索
```

### ログの確認

```bash
# システムログの確認
tail -f /var/log/syslog            # Linux
tail -f /var/log/system.log        # macOS
Get-EventLog -LogName System -Newest 50  # Windows（PowerShell）

# アプリケーションログ
tail -f /var/log/nginx/access.log  # Webサーバーのアクセスログ
tail -f /var/log/nginx/error.log   # Webサーバーのエラーログ
journalctl -u service_name -f      # systemdサービスのログ（Linux）
```

## 学習のコツとベストプラクティス

### 効率的な学習方法

1. **コマンドを少しずつ覚える**: 毎日1-2個の新しいコマンドを覚える
2. **マニュアルを読む**: `man command`（macOS/Linux）や`command /?`（Windows）でヘルプを確認
3. **エイリアスを活用**: よく使うコマンドに短縮名を付ける
4. **履歴を活用**: 過去のコマンドを再利用する
5. **スクリプト化**: 繰り返し作業は自動化する

### エイリアスの設定例

```bash
# ~/.bashrc または ~/.zshrc に追加（macOS/Linux）
alias ll='ls -la'
alias la='ls -la'
alias ..='cd ..'
alias ...='cd ../..'
alias grep='grep --color=auto'
alias h='history'
alias c='clear'

# PowerShell profile（Windows）
Set-Alias ll Get-ChildItem
Set-Alias la Get-ChildItem
function .. { cd .. }
function ... { cd ../.. }
```

### セキュリティのベストプラクティス

```bash
# 安全なファイル権限
chmod 600 ~/.ssh/id_rsa           # 秘密鍵は所有者のみ読み書き可能
chmod 644 ~/.ssh/id_rsa.pub       # 公開鍵は所有者のみ書き込み可能

# 安全なパスワード管理
# パスワードをコマンドライン引数で渡さない
# 環境変数や設定ファイルを使用

# ログの定期確認
grep "Failed password" /var/log/auth.log  # 失敗したログイン試行の確認
```

## まとめ

CLIは、開発者にとって必須のスキルです。この章で学習した内容：

- **基本概念**: ターミナル、プロンプト、パスの理解
- **ファイル操作**: 作成、コピー、移動、削除の基本操作
- **テキスト処理**: 検索、フィルタリング、編集の方法
- **システム管理**: プロセス、ネットワーク、権限の管理
- **開発支援**: Git、Python、Node.jsなどの開発ツール
- **自動化**: スクリプト作成による作業の効率化
- **トラブルシューティング**: 問題の診断と解決方法

CLIをマスターすることで、効率的な開発環境を構築し、自動化により生産性を大幅に向上させることができます。

## 次のステップ

1. **高度なシェルスクリプト**: 条件分岐、ループ、関数の活用
2. **正規表現**: 高度なテキスト処理とパターンマッチング
3. **DevOps**: CI/CD、Docker、Kubernetesなどのツール
4. **サーバー管理**: SSH、cron、systemdなどの管理機能
5. **セキュリティ**: ログ監視、侵入検知、脆弱性スキャン

毎日少しずつCLIを使うことで、自然にスキルが身についていきます。まずは基本的なファイル操作から始めて、徐々に高度な機能を学習していってください。