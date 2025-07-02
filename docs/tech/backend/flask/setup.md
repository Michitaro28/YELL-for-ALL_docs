# Flask セットアップガイド（Poetry使用）

YELL for ALLではパッケージ管理として、[Poetry](https://python-poetry.org/)を使用してFlaskプロジェクトをセットアップします。

## 前提条件

- Python 3.8以上がインストールされていること
- Poetryがインストールされていること

### Poetryのインストール確認

```bash
# Poetryのバージョン確認
poetry --version

# インストールされていない場合（macOS/Linux）
curl -sSL https://install.python-poetry.org | python3 -

# Windows（PowerShell）
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

## 1. プロジェクトの作成

プロジェクトフォルダを作成し、Poetryで初期化します。

```bash
# 新しいプロジェクトの作成
mkdir flask-app
cd flask-app
poetry init
```

`poetry init`を実行すると、対話形式でプロジェクト情報を設定できます：
- パッケージ名
- バージョン
- 説明
- 作成者
- ライセンス
- 依存関係

## 2. 仮想環境の設定

Poetryは自動で仮想環境を管理しますが、明示的に設定することも可能です。

```bash
# 仮想環境の作成（Poetryが自動で行うため通常は不要）
poetry env use python3

# 仮想環境に入る
poetry shell

# 仮想環境の情報確認
poetry env info
```

## 3. Flaskのインストール

基本のFlaskパッケージをインストールします。

```bash
# Flaskをインストール
poetry add flask
```

## 4. 追加パッケージのインストール

`poetry init`で作成されたpyproject.tomlファイルに依存関係を追加します。
[Flask Tutorial](https://flask.palletsprojects.com/en/stable/installation/)に沿って、
開発に便利なパッケージをインストールします。

```bash
# 開発用パッケージをインストール
poetry add --group dev pytest black flake8

# その他の便利なパッケージ
poetry add python-dotenv flask-cors

# データベース関連（必要に応じて）
poetry add flask-sqlalchemy flask-migrate

# 認証関連（必要に応じて）
poetry add flask-login flask-wtf

# テンプレートエンジン関連（必要に応じて）
poetry add jinja2
```

## 5. 基本的なFlaskアプリケーションの作成

### プロジェクト構造の作成

```bash
# 基本的なディレクトリ構造を作成
mkdir app
mkdir tests
touch app.py
touch .env
touch .flaskenv
```

### 最小限のFlaskアプリケーション

`app.py`ファイルを作成し、以下の内容を記述します：

```python
from flask import Flask
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask with Poetry!'

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Flask app is running'}

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
```

### 環境設定ファイル

`.env`ファイルを作成：

```bash
FLASK_DEBUG=True
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

`.flaskenv`ファイルを作成：

```bash
FLASK_APP=app.py
```

## 6. アプリケーションの起動

```bash
# 仮想環境に入る
poetry shell

# Flaskアプリケーションを起動
python app.py

# またはFlaskコマンドを使用
flask run

# デバッグモードで起動
flask run --debug
```

ブラウザで `http://localhost:5000` にアクセスして動作確認を行います。

## 7. テストの設定

`tests/test_app.py`ファイルを作成：

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask with Poetry!' in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
```

テストを実行：

```bash
# テストの実行
poetry run pytest

# 詳細な出力でテストを実行
poetry run pytest -v
```