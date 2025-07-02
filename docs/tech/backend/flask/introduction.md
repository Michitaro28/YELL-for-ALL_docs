# Flask クイックスタート

[Flaskドキュメント](https://flask.palletsprojects.com/en/stable/quickstart/)を参考に最小限のFlaskアプリを動かし、アプリケーションの基本を学びましょう！ここではドキュメントの一部をピックアップしていきますので、より詳しく動かしたい場合は公式ドキュメントを参照してください。

## 基本的なアプリケーション

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

このコードを`app.py`として保存し、実行します：

```bash
python app.py
```

ブラウザで `http://localhost:5000` にアクセスすると、「Hello, World!」が表示されます。

### コードの説明

1. **Flask のインポート**: `from flask import Flask`
2. **アプリケーションの作成**: `app = Flask(__name__)`
3. **ルートの定義**: `@app.route('/')`でURLパスを指定
4. **ビュー関数**: `hello()`関数がリクエストを処理
5. **アプリケーションの実行**: `app.run(debug=True)`

## ルーティング

### 基本的なルーティング

```python
@app.route('/')
def index():
    return 'インデックスページ'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<name>')
def show_user_profile(name):
    return f'ユーザー: {name}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'投稿 ID: {post_id}'
```

### HTTPメソッドの指定

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'ログイン処理'
    else:
        return 'ログインフォーム'
```

## テンプレートの使用

### HTMLテンプレートの作成

ディレクトリ構造：
```
/
├── app.py
└── templates/
    ├── index.html
    └── user.html
```

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='ホーム')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)
```

### templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Flask クイックスタート</h1>
    <p>Flaskアプリケーションへようこそ！</p>
</body>
</html>
```

### templates/user.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>ユーザープロフィール</title>
</head>
<body>
    <h1>ユーザー: {{ username }}</h1>
    <p>{{ username }}さんのプロフィールページです。</p>
</body>
</html>
```

## フォームの処理

### HTMLフォーム

```python
from flask import Flask, render_template, request, redirect, url_for

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'名前: {name}, メール: {email}'
    
    return '''
    <form method="post">
        <p>名前: <input type="text" name="name"></p>
        <p>メール: <input type="email" name="email"></p>
        <p><input type="submit" value="送信"></p>
    </form>
    '''
```

## 静的ファイルの配信

### ディレクトリ構造

```
/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/
    └── base.html
```

### templates/base.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>Flask アプリケーション</h1>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

## エラーハンドリング

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

## JSON APIの作成

```python
from flask import jsonify

@app.route('/api/users')
def get_users():
    users = [
        {'id': 1, 'name': '田中太郎'},
        {'id': 2, 'name': '佐藤花子'}
    ]
    return jsonify(users)

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    user = {'id': user_id, 'name': f'ユーザー{user_id}'}
    return jsonify(user)
```

## 設定とデバッグ

### 開発環境の設定

```python
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your-secret-key'

# または環境変数から設定
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
```

### 本番環境での実行

```python
if __name__ == '__main__':
    # 開発環境
    app.run(debug=True)
else:
    # 本番環境
    app.run(host='0.0.0.0', port=5000)
```

## 次のステップ

Flaskの基本を理解したら、以下の topics について学習を進めてください：

- **データベース統合**: Flask-SQLAlchemy
- **ユーザー認証**: Flask-Login
- **フォーム処理**: Flask-WTF
- **ブループリント**: アプリケーションの構造化
- **テスト**: Flask-Testing

詳細については、[Flask公式ドキュメント](https://flask.palletsprojects.com/)を参照してください。


